import logging
from ezcolorlog import root_logger, setup_logging, log_stdout


root_logger.info("Setting up logging...")
logger = logging.getLogger("my_logger")

setup_logging(logger, cfg_file="./config.yaml")

logger.info("Info test")
logger.debug("Debug test")
logger.warning("Warning test")
logger.error("Error test")
logger.critical("Critical test")


def test_func():
    print("This will be printed to stdout, not logged")


@log_stdout
def test_func2():
    print("This will be logged instead of printed to stdout!")


test_func()
test_func2()
