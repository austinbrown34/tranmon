import traceback, settings, os
from lib.coin import Profitability, ProfitabilityFactory
from lib.tranmon_service import TranmonService
from lib.nice_logger import NiceLogger

from lib.coin_market_cap_api import CoinMarketCapApi
from lib.what_to_mine_api import WhatToMineApi
from lib.coin_desk_api import CoinDeskApi

ts = TranmonService(os.environ.get("API_HOST"))

def all_currencies(event, context):
    try:
        # Instaniate the APIs from which to scrape this data
        what_to_mine_api = WhatToMineApi()
        coin_desk_api = CoinDeskApi()

        coin_market_cap_api = CoinMarketCapApi()
        coins = coin_market_cap_api.coin_map

        profitabilites = ProfitabilityFactory.All(coins, what_to_mine_api, coin_desk_api)
        responses = []
        for profitability in profitabilites:
            if profitability['coins_day'] != 0.0:
                responses.append(ts.post('/profitabilities', {'profitability': profitability}))
        NiceLogger.log(responses)
    except Exception as e:
        t = traceback.format_exc()
        NiceLogger.log(t, level="ERROR")

def for_currency(event, context):
    try:
        what_to_mine_api = WhatToMineApi()
        coin_desk_api = CoinDeskApi()
        profitability = Profitability(event['currency_id'], what_to_mine_api, coin_desk_api).calculate()
        print profitability
        response = ts.post('/profitabilities', {'profitability': profitability})
        NiceLogger.log(response)
    except Exception as e:
        t = traceback.format_exc()
        NiceLogger.log(t, level="ERROR")
