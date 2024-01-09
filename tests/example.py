import logging
import tempfile

from easylog import root_logger, setup_logging, log_stdout


root_logger.info("Setting up logging...")
logger = logging.getLogger("my_logger")


with tempfile.NamedTemporaryFile("w") as temp:
    temp.write("""
user:
  log_fmt: my_log_format

format:
  my_log_format: "%(asctime)s %(filename)s:%(lineno)s\t[%(levelname).1s]→ %(message)s"

style:
  asctime:
    color: magenta
""")
    temp.flush()
    setup_logging(logger, cfg_file=temp.name)

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
