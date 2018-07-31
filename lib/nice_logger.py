import logging

class NiceLogger(object):
    def log(self, message, level='DEBUG'):
        """Wraps the logger and gives us a pretty version of the name of this
            class or a subclass calling it
        """
        NiceLogger.log(message, level=level, context=type(self).__name__)

    @staticmethod
    def log(message, level='DEBUG', context=''):
        """Wraps the logger and gives us a pretty version of the name of this
            class or a subclass calling it
        """
        logger = NiceLogger.get_logger()
        level = level.upper()

        if level == "DEBUG":
            logger.debug("{} - {}".format(context, message))
        elif level == "INFO":
            logger.info("{} - {}".format(context, message))
        elif level == "WARNING":
            logger.warning("{} - {}".format(context, message))
        elif level == "ERROR":
            logger.error("{} - {}".format(context, message))
        elif level == "CRITICAL":
            logger.critical("{} - {}".format(context, message))
        else:
            logger.debug("{} - {}".format(context, message))


    @staticmethod
    def get_logger():
        root = logging.getLogger()
        if root.handlers:
            for handler in root.handlers:
                root.removeHandler(handler)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger = logging.getLogger('root')
        return logger
