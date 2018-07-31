import os, json, requests, base64, uuid
from nice_logger import NiceLogger
from s3_service import S3Service

class Api(NiceLogger):
    """A Simple API

    Attributes:
        hostname: A string representing the name of the host
    """

    def __init__(self, hostname):
        """Return an API object for a given crypto currency API"""
        self.hostname = hostname

        if os.environ.get("API_CACHE_TYPE") == "DumbCache":
            self.log('Using DumbCache because os.environ.get("API_CACHE_TYPE") == "DumbCache"')
            self.cache = DumbCache(os.path.join(os.path.dirname(__file__), '.cache'))
        else:
            self.log('Using S3Cache because os.environ.get("API_CACHE_TYPE") != "DumbCache" - got "{}"'.format(os.environ.get("API_CACHE_TYPE")))
            self.cache = S3Cache(os.getenv('AWS_CACHE_BUCKET'), os.getenv('AWS_ACCESS_KEY_ID'), os.getenv('AWS_SECRET_ACCESS_KEY'))

        self.log("initialized for hostname '{}'".format(self.hostname))

    def post(self, endpoint, data):
        """Return a Response dict after performing a post to an endpoint"""
        self.log('post(endpoint={}, data={})'.format(endpoint, data))
        address = requests.compat.urljoin(self.hostname, endpoint)
        self.log('resolves to {}'.format(address))
        request_id = str(uuid.uuid4())
        response = requests.post(address, data=json.dumps(data), headers={'content-type': 'application/json', 'X-Request-ID': request_id})
        self.log('response.headers={}'.format(response.headers))
        self.log('post(endpoint={}, status={}, X-Request-ID={}, data={}, response={})'.format(endpoint, response.status_code, request_id, "...", "..."), level="INFO")
        response.raise_for_status()
        return json.loads(response.content)

    def get(self, endpoint, use_cache=False):
        """Return a Response dict for a given endpoint"""
        address = requests.compat.urljoin(self.hostname, endpoint)
        self.log('get(endpoint={}, use_cache={})'.format(endpoint, use_cache))
        self.log('resolves to {}'.format(address))

        if use_cache:
            cached = self.cache.get(address)
            if cached:
                self.log('cache hit!')
                return json.loads(cached)
            self.log('cache miss!')
            response = requests.get(address)
            self.cache.set(address, response.content)
        else:
            self.log('cache not allowed...')
            response = requests.get(address)
        return json.loads(response.content)

class Cache(NiceLogger):
    """A dumb url-based file DumbCache

    Attributes:

    """

    def __init__(self ):
        """This function is to be overwritten by the subclass """
        return False


    def get(self, key):
        """ Given a key, returns a value if in the cache """
        """This function is to be overwritten by the subclass """
        return False

    def set(self, key, value):
        """ Given a key, sets a value in the cache """
        """This function is to be overwritten by the subclass """
        return False

class S3Cache(NiceLogger):
    """A dumb S3 based URL caching library

    Attributes:
        bucket: A string representing a bucket
        access_key: A string representing the S3 access_key
        secret_key: A string representing the S3 secret_key
    """

    def __init__(self, bucket, access_key, secret_key):
        credentials = {
            'aws_access_key_id': access_key,
            'aws_secret_access_key': secret_key
        }

        if access_key == '' or access_key == None or secret_key == '' or secret_key == None:
            self.log('setting credentials to None')
            credentials = None

        self.s3_api = S3Service(None, bucket)

    def __format_key(self, key):
        # ensure that we use a safe filename by just base64'ing that sucka.
        formatted_key = str(uuid.uuid5(uuid.NAMESPACE_URL, key.strip()))
        self.log("converted cached url '{}' to cache key '{}'".format(key, formatted_key))
        return formatted_key

    def get(self, key):
        """ Given a key, returns a value if in the cache """
        """This function is to be overwritten by the subclass """
        formatted_key = self.__format_key(key)
        try:
            return self.s3_api.read_value(formatted_key)
        except Exception as e:
            print str(e)

    def set(self, key, value):
        """ Given a key, sets a value in the cache """
        """This function is to be overwritten by the subclass """
        formatted_key = self.__format_key(key)
        self.s3_api.write_value(formatted_key, value)


class DumbCache(Cache):
    """A dumb url-based file DumbCache

    Attributes:
        target_dir: A string representing a directory where the cache lives
    """

    def __init__(self, target_dir):
        self.target_dir = target_dir
        if not os.path.exists(target_dir):
            self.log("creating directory '{}'".format(self.target_dir))
            os.mkdir(target_dir)
        self.log("initialized cache at '{}'".format(self.target_dir))

    def __format_key(self, key):
        # ensure that we use a safe filename by just base64'ing that sucka.
        return base64.urlsafe_b64encode(key)

    def __get_filename_for_key(self, key):
        formatted_key = self.__format_key(key)
        filepath = os.path.join(self.target_dir, formatted_key)
        self.log("cache key '{}' resolves to '{}'".format(key, formatted_key))
        return filepath

    def get(self, key):
        """ Given a key, returns a value if in the cache """
        self.log('get(key={})'.format(key))

        filename = self.__get_filename_for_key(key)
        value = ""
        if os.path.exists(filename):
            with open(filename) as cache_file:
                value = cache_file.read()
        return value

    def set(self, key, value):
        """ Given a key, sets a value in the cache """
        self.log('set(key={}, value=...truncated...)'.format(key))

        formatted_key = self.__format_key(key)
        with open(os.path.join(self.target_dir, formatted_key), 'w') as cache_file:
            cache_file.write(value)
