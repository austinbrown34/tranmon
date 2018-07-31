import traceback, settings, os
from lib.coin import Market
from lib.tranmon_service import TranmonService
from lib.nice_logger import NiceLogger

logger = NiceLogger.get_logger()
ts = TranmonService(os.environ.get("API_HOST"))

def overview(event, context):
    try:
        market = Market(event['currency_id'])
        data = market.get_market_data()
        response = ts.post('/markets', {'market': data})
        logger.info(response)
    except Exception as e:
        t = traceback.format_exc()
        logger.error(t)
