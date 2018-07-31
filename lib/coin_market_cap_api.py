from lib.api import Api
import json


class CoinMarketCapApi(Api):
    """A simple API for CoinMarketCap"""

    def __init__(self):
        Api.__init__(self, 'https://api.coinmarketcap.com/v1/')
        self.coin_map = json.loads(open('./lib/cmc_currencies.json').read())

    def lookup_currency_by_ticker(self, ticker):
        results = [match for match in self.coin_map if match['cmc_ticker'] == ticker.upper()]
        return results

    def get_current_market(self, ticker):
        currencies = self.lookup_currency_by_ticker(ticker)
        current_market_values = []
        for currency in currencies:
            current_market_values.append(self.get('ticker/{}'.format(currency['cmc_id']))[0])
        print current_market_values
        return current_market_values
