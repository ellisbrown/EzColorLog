import logging

from easylog import root_logger as logger

# debug level
logger.setLevel(logging.DEBUG)
for handler in logger.handlers:
    handler.setLevel(logging.DEBUG)


logger.info("This is a test")
logger.debug("This is a test")
logger.warning("This is a test")
logger.error("This is a test")
logger.critical("This is a test")
