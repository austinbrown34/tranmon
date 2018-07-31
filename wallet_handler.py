import traceback, settings, os
from lib.currency_loader import CurrencyLoader
from lib.tranmon_service import TranmonService
from lib.nice_logger import NiceLogger

logger = NiceLogger.get_logger()
ts = TranmonService(os.environ.get("API_HOST"))

def overview(event, context):
    try:
        wallet = CurrencyLoader(event['currency_id']).Wallet(event['currency_id'], event['address'])
        if wallet.load(True):
            response = ts.post('/wallets', {'wallet': wallet.toJSON()})
            logger.info(response)
        else:
            logger.error("Failed to load wallet for some reason")
    except Exception as e:
        t = traceback.format_exc()
        logger.error(t)

def transactions(event, context):
    try:
        wallet = CurrencyLoader(event['currency_id']).Wallet(event['currency_id'], event['address'])
        if wallet.load(True):
            transactions = wallet.filter_transactions_and_filter_transaction_payments_by_wallet('timestamp', 'desc')
            responses = []
            for transaction in transactions:
                responses.append(ts.post('/wallets/{}/transactions'.format(event['address']), {'transactions': [transactions]}))
            logger.info(responses)
        else:
            logger.error("Failed to load wallet for some reason")
    except Exception as e:
        t = traceback.format_exc()
        logger.error(t)
