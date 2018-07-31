import os, sys, imp


class CurrencyLoader(object):
    """A simple interface to load a given currencie's modules"""

    def __init__(self, ticker):
        self.ticker = ticker

    def _load(self, class_name):
        filepath = os.path.join(os.path.dirname(__file__), '..', 'currencies')
        filename = '{}_coin.py'.format(self.ticker)
        _module = imp.load_source(self.ticker, os.path.join(filepath, filename))
        return getattr(_module, class_name)

    def Wallet(self, *args, **kwargs):
        _class = self._load('{}Wallet'.format(self.ticker.title()))
        return _class(*args, **kwargs)

    def Transaction(self, *args, **kwargs):
        _class = self._load('{}Transaction'.format(self.ticker.title()))
        return _class(*args, **kwargs)
