import traceback

from nice_logger import NiceLogger

from constants import (
    DAY_SECONDS, MHS_HASH, SOLS_PER_HASH, FULL_MINER_SHARE, REDUCED_MINER_SHARE,
    EQUIHASH_BLOCK_HEIGHT_CUTOFF, HOUR_SECS, DAY_HOURS, HASH_NUMBER,
    KW_WATS, FORMULA_A_ALGORITHMS, FORMULA_B_ALGORITHMS,
    FORMULA_C_ALGORITHMS, GPU_ALGORITHM_PERFORMANCE
)
from config import (
    PRICE_PER_KWH, BTC_USD, EQUIHASH_POOL_HASHRATE, DIFFICULTY,
    BLOCK_REWARD, PROFIT_DAYS, GPU_COUNTS
)

class ProfitabilityFactory(NiceLogger):
    """The profitability for a given currency

    Attributes:
        ticker: A string representing the currency
    """

    @staticmethod
    def All(coins, coin_data_api, price_data_api):
        results = []

        for coin in coins:
            ticker = coin['cmc_ticker']
            name = coin['cmc_name']
            profitability = Profitability(ticker, coin_data_api, price_data_api)
            calculated = profitability.calculate()
            calculated.update({'name': name})
            results.append(calculated)
        results.sort(key=lambda x: x['net_profit'], reverse=True)
        return results

class Profitability(NiceLogger):
    """The profitability for a given currency

    Attributes:
        ticker: A string representing the currency
    """

    def __init__(self, ticker, coin_data_api, price_data_api):
        self.ticker = ticker
        self.coin_data_api = coin_data_api
        self.price_data_api = price_data_api

    def _coins_to_btc(self, coins, exchange_rate):
        return float(coins) * float(exchange_rate)

    def _btc_to_usd(self, btc, btc_usd):
        return float(btc) * float(btc_usd)

    def _get_gross_profit(self, usd, profit_days):
        return float(usd) * profit_days

    def _do_formula_a(self, block_reward, difficulty, hashrate):
        block_reward = float(block_reward)
        difficulty = float(difficulty)
        hashrate = float(hashrate)
        coins_day_mhs = (block_reward * DAY_SECONDS * MHS_HASH) / (difficulty * HASH_NUMBER)
        coins_day = coins_day_mhs * hashrate
        return coins_day

    def _do_formula_b(self, block_reward, difficulty, hashrate):
        block_reward = float(block_reward)
        difficulty = float(difficulty)
        hashrate = float(hashrate)
        coins_day_mhs = (block_reward * DAY_SECONDS * MHS_HASH) / difficulty
        coins_day = coins_day_mhs * hashrate
        return coins_day

    def _do_formula_c(self, hashrate, equihash_pool_hashrate, nethash, block_time, last_block, block_reward):
        hashrate = float(hashrate)
        nethash = float(nethash)
        block_time = float(block_time)
        last_block = float(last_block)
        block_reward = float(block_reward)
        hashrate = hashrate * MHS_HASH * SOLS_PER_HASH
        pool_hash_rate = equihash_pool_hashrate * MHS_HASH * SOLS_PER_HASH
        nethash = nethash * SOLS_PER_HASH
        miner_share = FULL_MINER_SHARE
        if last_block < EQUIHASH_BLOCK_HEIGHT_CUTOFF:
            miner_share = REDUCED_MINER_SHARE
        block_find_time = (block_time / (hashrate / nethash)) / HOUR_SECS
        blocks_per_hour = 1 / block_find_time
        coins_day = (hashrate / pool_hash_rate) * blocks_per_hour * block_reward * DAY_HOURS * miner_share
        return coins_day

    def _get_cost(self, power, price_per_kwh):
        return (float(power) / KW_WATS) * price_per_kwh * DAY_HOURS

    def _get_total_cost(self, cost, cost_days):
        return float(cost) * cost_days

    def _get_net(self, gross_profit, costs):
        return gross_profit - costs

    def calculate(self):
        from re import sub
        from decimal import Decimal
        coin_data = self.coin_data_api.get_coin_data(self.ticker)

        results = {
            'currency_id': Currency.Lookup(self.ticker, ''),
            'coins_day': 0,
            'btc_day': 0,
            'usd_day': 0,
            'gross_profit': 0,
            'cost_day': 0,
            'costs': 0,
            'net_profit': 0,
            'profit_days': 0,
            'currency_detail': {
                "algorithm": coin_data.get('algorithm', None),
                "block_reward": coin_data.get('block_reward', None),
                "block_reward24": coin_data.get('block_reward24', None),
                "block_time": coin_data.get('block_time', None),
                "btc_revenue": coin_data.get('btc_revenue', None),
                "btc_revenue24": coin_data.get('btc_revenue24', None),
                "currency_id": Currency.Lookup(self.ticker, ''),
                "difficulty": coin_data.get('difficulty', None),
                "difficulty24": coin_data.get('difficulty24', None),
                "estimated_rewards": coin_data.get('estimated_rewards', None),
                "estimated_rewards24": coin_data.get('estimated_rewards24', None),
                "exchange_rate": coin_data.get('exchange_rate', None),
                "exchange_rate24": coin_data.get('exchange_rate24', None),
                "exchange_rate_curr": coin_data.get('exchange_rate_curr', None),
                "exchange_rate_vol": coin_data.get('exchange_rate_vol', None),
                "lagging": coin_data.get('lagging', None),
                "last_block": coin_data.get('last_block', None),
                "market_cap": float(sub(r'[^\d.]', '', coin_data.get('market_cap', '$0.00'))),
                "name": coin_data.get('name', None),
                "net_hash": coin_data.get('nethash', None),
                "profitability_ratio": coin_data.get('profitability', None),
                "profitability_ratio24": coin_data.get('profitability24', None),
                "ticker": self.ticker
            },
            'gpu_configuration': GPU_COUNTS
        }
        try:
            difficulty = coin_data['difficulty']
            block_reward = coin_data['block_reward']
            if DIFFICULTY == '24hr':
                difficulty = coin_data['difficulty24']
            if BLOCK_REWARD == '24hr':
                block_reward = coin_data['block_reward24']
            last_block = coin_data['last_block']
            algorithm = coin_data['algorithm']
            exchange_rate = coin_data['exchange_rate']
            nethash = coin_data['nethash']
            block_time = coin_data['block_time']
            coins_day = 0
            btc_day = 0
            usd_day = 0
            cost_day = 0
            gross_profit = 0
            costs = 0
            net_profit = 0
            if last_block != 0:
                for gpu in GPU_COUNTS:
                    if GPU_COUNTS[gpu] > 0 and coin_data['algorithm'] in GPU_ALGORITHM_PERFORMANCE[gpu]:
                        hashrate = GPU_ALGORITHM_PERFORMANCE[gpu][coin_data['algorithm']]['hashrate']
                        power = GPU_ALGORITHM_PERFORMANCE[gpu][algorithm]['power']

                        if algorithm in FORMULA_A_ALGORITHMS:
                            coins_day += self._do_formula_a(block_reward, difficulty, hashrate) * GPU_COUNTS[gpu]

                        if algorithm in FORMULA_B_ALGORITHMS:
                            coins_day += self._do_formula_b(block_reward, difficulty, hashrate) * GPU_COUNTS[gpu]

                        if algorithm in FORMULA_C_ALGORITHMS:
                            coins_day += self._do_formula_c(hashrate, EQUIHASH_POOL_HASHRATE, nethash, block_time, last_block, block_reward) * GPU_COUNTS[gpu]

                        btc_day += self._coins_to_btc(coins_day, exchange_rate)
                        usd_day += self._btc_to_usd(btc_day, BTC_USD)
                        gross_profit += self._get_gross_profit(usd_day, PROFIT_DAYS)
                        cost_day += self._get_cost(power, PRICE_PER_KWH) * GPU_COUNTS[gpu]
                        costs += self._get_total_cost(cost_day, PROFIT_DAYS)
                        net_profit += self._get_net(gross_profit, costs)

            results.update({
                'coins_day': coins_day,
                'btc_day': btc_day,
                'usd_day': usd_day,
                'gross_profit': gross_profit,
                'cost_day': cost_day,
                'costs': costs,
                'net_profit': net_profit,
                'profit_days': PROFIT_DAYS
            })

        except Exception as e:
            t = traceback.format_exc()
            NiceLogger.log(t, level="ERROR")
        return results


class Market(NiceLogger):
    """A simple API wrapper for CoinMarketCap

    Attributes:
        ticker: A string representing the currency
    """

    def __init__(self, ticker):
        self.ticker = ticker
        self.api = CoinMarketCapApi()
        self.parse({})

    def get_market_data(self):
        d = self.api.get_current_market(self.ticker)
        self.parse(d[0])
        return self._data

    def parse(self, data):
        self._data = {
            "_24h_volume_usd": data.get('24h_volume_usd', 0),
            "available_supply": data.get('available_supply', 0),
            "currency_id": Currency.Lookup(self.ticker, ''),
            "market_cap_usd": data.get('market_cap_usd', 0),
            "max_supply": data.get('max_supply', 0),
            "name": data.get('name', ''),
            "percent_change_1h": data.get('percent_change_1h', 0),
            "percent_change_24h": data.get('percent_change_24h', 0),
            "percent_change_7d": data.get('percent_change_7d', 0),
            "price_btc": data.get('price_btc', 0),
            "price_usd": data.get('price_usd', 0),
            "rank": data.get('rank', 0),
            "ticker": self.ticker,
            "total_supply": data.get('total_supply', 0)
        }

    def toJSON(self):
        return self._data


class Wallet(NiceLogger):
    """A crypto currency wallet

    Attributes:
        currency_id: A string representing the wallet's unique currency_id.
        address: A string representing the wallet's address.
    """

    def __init__(self, currency_id, address, details=None):
        """Return a Wallet object for a given crypto currency address"""
        self.currency_id = currency_id
        self.address = address

        if details is None:
            details = {}

        self.details = {
            'balance': 0.0,
            'total_sent': 0.0,
            'total_received': 0.0,
            'transactions': []
        }
        self.details.update(details)
        self.log("initialized for address '{}'".format(address))

    def toJSON(self):
        return {
            'currency_id': self.currency_id,
            'address': self.address,
            'balance': self.details['balance'],
            'total_sent': self.details['total_sent'],
            'total_received': self.details['total_received'],
            'last_incoming_transaction': self.get_last_incoming_transaction()
        }

    def __calculate_transaction_value_by_wallet(self, transaction):
        return transaction.get_value_by_wallet_address(self.address)

    def get_last_incoming_transaction(self):
        """Return the last incoming transaction for this wallet"""
        return self.filter_transactions_and_filter_transaction_payments_by_wallet('timestamp', 'desc')[0]

    def filter_transactions_and_filter_transaction_payments_by_wallet(self, key='timestamp', order_by="desc"):
        """Return a list of transactions modified to only account for payments
        made this wallet address."""
        transactions = self.get_transactions()

        filtered_transactions = []
        for transaction in transactions:
            filtered_transactions.append({
                'transaction_id': transaction.id,
                'timestamp': transaction.details['timestamp'],
                'value': self.__calculate_transaction_value_by_wallet(transaction),
                'outgoing_payments': [payment.toJSON() for payment in transaction.details['payments']]
            })

        reverse = True
        if order_by.lower() == "asc":
            reverse = False

        filtered_transactions.sort(key=lambda x: x[key.lower()], reverse=reverse)

        return filtered_transactions

    def get_transactions(self):
        """Return a list of transaction entries available for this wallet"""
        self.details['transactions'].sort(key=lambda x: x.details['timestamp'], reverse=True)
        return self.details['transactions']

    def get_transactions_sorted_by(self, key='timestamp', order_by="desc"):
        """Return a list of transaction entries available for this wallet sorted
        """
        reverse = True
        if order_by.lower() == "asc":
            reverse = False

        if key.lower() == 'value':
            self.details['transactions'].sort(key=lambda x: x.get_value(), reverse=reverse)
        else:
            self.details['transactions'].sort(key=lambda x: x.details[key.lower()], reverse=reverse)
        return self.details['transactions']

    def get_balance(self):
        """Returns a float representing the current balance of this wallet"""
        return self.details['balance']

    def get_total_sent(self):
        """Returns a float representing the total sent to this wallet"""
        return self.details['total_sent']

    def get_total_received(self):
        """Returns a float representing the total sent from this wallet"""
        return self.details['total_received']

    def load(self, deep=False):
        """This function is to be overwritten by the subclass and will populate
            self.details using self.address as a key"""
        return False


class Transaction(NiceLogger):
    """A crypto currency transaction

    Attributes:
        id: A string representing the transactions's id.
    """

    def __init__(self, id, details=None):
        """Return a Transaction object for a given crypto currency transaction"""
        self.id = id

        if details is None:
            details = {}

        self.details = {
            'timestamp': 0,
            'currency_id': '',
            'payments': []
        }
        self.details.update(details)
        self.log("initialized for transaction '{}'".format(self.id))

    def toJSON(self):
        return {
            'timestamp': self.details['timestamp'],
            'transaction_id': self.id,
            'value': self.get_value(),
            # 'currency_id': self.details['currency_id'],
            'outgoing_payments': [payment.toJSON() for payment in self.details['payments']]
        }

    def get_value_by_wallet_address(self, wallet_address):
        """Given an address, find out how much was sent to that address during this transaction"""
        value = 0.0
        for i,payment in enumerate(self.details['payments']):
            if payment.has_wallet_address(wallet_address):
                value += payment.value
        return value

    def get_value(self):
        """Find out total value of transaction"""
        value = 0.0
        for i,payment in enumerate(self.details['payments']):
            value += payment.value
        return value

    def load(self):
        """This function is to be overwritten by the subclass and will populate
            self.details using self.id as a key"""
        return False


class Payment(NiceLogger):
    """A crypto currency payment

    Attributes:
        recipients: A list of wallet addresses
        value: A float representing the amount sent
    """

    def __init__(self, recipients, value):
        """Return a payment object for a given crypto currency payment"""
        self.recipients = recipients
        self.value = value

    def toJSON(self):
        return {
            'value': self.value,
            'recipients': self.recipients
        }

    def has_wallet_address(self, wallet_address):
        return wallet_address in self.recipients

from fuzzywuzzy import fuzz, process
import json
currency_list = json.loads(open('./lib/cmc_currencies.json').read())
class Currency(NiceLogger):
    """A crypto currency

    Attributes:

    """

    @staticmethod
    def _cleanit(val):
      return "_".join(val.strip().split()).lower()

    @staticmethod
    def _generate_currency_id(ticker, name):
      return "{}-{}".format(Currency._cleanit(ticker),Currency._cleanit(name))

    @staticmethod
    def Lookup(ticker, name):
        NiceLogger.log("Lookup(ticker={}, name={})".format(ticker, name))
        ticker = ticker.strip().lower()

        possibilities = []
        for i in currency_list:
            if i["cmc_ticker"].strip().lower() == ticker:
                possibilities.append(i)

        if len(possibilities) == 1:
            id = Currency._generate_currency_id(possibilities[0]['cmc_ticker'], possibilities[0]['cmc_name'])
            NiceLogger.log("Resolved ticker={}, name={} to id={}".format(ticker, name, id))
            return id
        elif len(possibilities) > 1:
            match = process.extractOne(name, possibilities)[0]
            id = Currency._generate_currency_id(match['cmc_ticker'], match['cmc_name'])
            NiceLogger.log("Resolved ticker={}, name={} to id={}".format(ticker, name, id))
            return id
        else:
            NiceLogger.log("Nothing found that matched {} or {}".format(ticker, name))
            raise Exception("Nothing found that matched {} or {}".format(ticker, name))
