from lib.api import Api


class CoinDeskApi(Api):
    """A simple API for CoinDesk"""

    def __init__(self):
        Api.__init__(self, 'https://api.coindesk.com/v1/')


    def get_btc_value(self):
        return self.get('bpi/currentprice.json')['bpi']['USD']['rate_float']
