import boto3, os
from safe_extractor import safe_extractor

class S3Service(object):
    def __init__(self, credentials=None, bucket_name=None):
        if credentials is None:
            self.credentials = None
            self.session = boto3.Session()
        else:
            self.credentials = credentials
            self.session = boto3.Session(
                aws_access_key_id=credentials['aws_access_key_id'],
                aws_secret_access_key=credentials['aws_secret_access_key']
            )
        if bucket_name is None:
            return
        self.bucket_name = bucket_name
        self.s3 = self.session.resource('s3')
        self.s3_client = self.session.client('s3')
        self.bucket_instance = self.s3.Bucket(self.bucket_name)

    def get_bucket_contents(self, prefix):
        contents = []
        for content in self.bucket_instance.objects.filter(Prefix=prefix):
            contents.append(content)
        return contents

    def get_keys_starting_with(self, prefix):
        keys = []
        for obj in self.get_bucket_contents(prefix):
            keys.append(obj.key)
        return keys

    def write_value(self, key, value, ACL='private'):
        self.s3.Bucket(self.bucket_name).put_object(Key=key, Body=value, ACL=ACL)

    def read_value(self, key):
        obj = self.s3.Object(self.bucket_name, key)
        return obj.get()['Body'].read().decode('utf-8')

    def upload_file(self, key, source, ACL='private'):
        self.s3.Bucket(self.bucket_name).put_object(Key=key, Body=open(source, 'rb'), ACL=ACL)

    def download_file(self, key, destination, extract=False):
        try:
            if not os.path.exists(destination):
                os.makedirs(destination)
            self.s3.meta.client.download_file(
                self.bucket_name,
                key,
                os.path.join(destination, key)
                )
        except Exception as e:
            print 'Download Exception\n' + str(e)
        if extract:
            if os.path.splitext(key)[1] == '.zip':
                safe_extractor().unzip_it(os.path.join(destination, key), os.path.join(destination, os.path.splitext(key)[0]))
            if os.path.splitext(key)[1] == '.tar':
                safe_extractor().untar_it(os.path.join(destination, key), os.path.join(destination, os.path.splitext(key)[0]))


    def download_files(self, keys, destination, extract=False):
        for key in keys:
            self.download_file(key, destination, extract=extract)
