import unittest, mock
from mock import patch
from api import Api

class HttpRequestsTestCase(unittest.TestCase):

    @patch("api.requests.get")
    def test_get_content_should_use_get_properly(self, mock_requests):
        # Notice the extra param in the test. This is the instance of `Mock` that the
        # decorator has substituted for us and it is populated automatically.
        url = "http://example.com/poop"

        # Exercise
        http_client = Api('http://example.com')
        http_client.get('/poop')

        # The param is now the object we need to make our assertions against
        self.mock_requests.get.assert_called_with(url)

if __name__ == '__main__':
    unittest.main()
