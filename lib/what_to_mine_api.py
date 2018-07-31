from lib.api import Api

class WhatToMineApi(Api):
    """A simple API for Whattomine"""

    def __init__(self):
        Api.__init__(self, 'https://whattomine.com/')
        self._coins = []


    def get_coin_data(self, ticker):
        if len(self._coins) == 0:
            self._coins = self.get('coins.json')['coins']

        # print self._coins
        formatted_coins = [self._coins[coin] for coin in self._coins if self._coins[coin]['tag'] == ticker.upper()]
        #TODO: Figure out how to handle when a ticker returns more than one currency
        formatted_coin = {}
        if formatted_coins:
            formatted_coin = formatted_coins[0]
        return formatted_coin
