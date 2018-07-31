from coin_desk_api import CoinDeskApi
# Hard coded number or get_btc_value()
BTC_USD = CoinDeskApi().get_btc_value()

# cost of electricity per kilowatt hour in USD
PRICE_PER_KWH = 0.07

# magical number that probably changes and we don't understand
EQUIHASH_POOL_HASHRATE = 0.00055

# options: 'current' or '24hr'
DIFFICULTY = 'current'
# DIFFICULTY = '24hr'

# options: 'current' or '24hr'
BLOCK_REWARD = 'current'
# BLOCK_REWARD = '24hr'

# number of days for which to total the daily profit
PROFIT_DAYS = 1

GPU_COUNTS = {
    '_1080': 8,
    '_280x': 0,
    '_380': 0,
    'Fury': 0,
    '_470': 0,
    '_480': 0,
    '_570': 0,
    '_580': 0,
    'Vega56': 0,
    'Vega64': 0,
    '_750Ti': 0,
    '_1050Ti': 0,
    '_1060': 0,
    '_1070': 0,
    '_1080Ti': 0
}
