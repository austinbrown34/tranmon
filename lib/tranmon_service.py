from lib.api import Api

class TranmonService(Api):
    """A simple API for the Tranmon Service"""

    def __init__(self, base_url="http://localhost:3000"):
        self.base_url = base_url
        Api.__init__(self, self.base_url)
