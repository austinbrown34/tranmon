from lib.coin import Wallet, Transaction, Payment
from lib.api import Api


class BtgApi(Api):
    """A simple API for Btg"""

    def __init__(self):
        # Api.__init__(self, 'http://btgexp.com')
        Api.__init__(self, 'http://btgblocks.com')

class BtgWallet(Wallet):
    """A crypto currency wallet for Btg

    Attributes:
        currency_id: A string representing the wallet's unique currency_id.
        address: A string representing the wallet's address.
    """

    def __init__(self, currency_id, address):
        Wallet.__init__(self, currency_id, address)
        self.api = BtgApi()

    def load(self, deep=False):
        self.log("load(deep={})".format(deep))

        details = self.api.get('/ext/getaddress/{}'.format(self.address))
        if 'error' in details:
            return False

        self.details['balance'] = float(details['balance'])
        self.details['total_sent'] = float(details['sent'])
        self.details['total_received'] = float(details['received'])

        self.log("found {} transactions".format(len(details['last_txs'])))
        transactions = []
        for i, transaction in enumerate(details['last_txs']):
            # The api refers to a transaction id as the key 'addresses'
            t = BtgTransaction(transaction['addresses'])
            if deep:
                t.load()
            transactions.append(t)

        self.details['transactions'] = transactions
        return True

class BtgTransaction(Transaction):
    """An Btg transactions

    Attributes:
        id: A string representing the transaction's id.
    """

    def __init__(self, id):
        Transaction.__init__(self, id)
        self.api = BtgApi()

    def load(self):
        self.log("load()")

        details = self.api.get('/api/getrawtransaction?txid={}&decrypt=1'.format(self.id), use_cache=True)
        if 'error' in details:
            return False

        self.details['timestamp'] = int(details['time'])

        self.log("attempting to inflate {} payments".format(len(details['vout'])))
        payments = []
        for i, payment in enumerate(details['vout']):
            recipients = payment['scriptPubKey']['addresses']
            value = float(payment['value'])
            payments.append(Payment(recipients, value))

        self.details['payments'] = payments
        self.log("inflated {} payments".format(len(self.details['payments'])))
        return True
