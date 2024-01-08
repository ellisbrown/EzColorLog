[![Build Status](https://travis-ci.com/ellisbrown/easylog.svg?branch=master)](https://travis-ci.com/ellisbrown/easylog)
[![codecov](https://codecov.io/gh/ellisbrown/easylog/branch/master/graph/badge.svg)](https://codecov.io/gh/ellisbrown/easylog)
[![Docs](https://readthedocs.org/projects/easylog/badge)](http://easylog.readthedocs.org/en/latest/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/ellisbrown/easylog/blob/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/easylog.svg)](https://badge.fury.io/py/easylog)

# easylog

`easylog` is a simple pretty Python logging interface.

## Installation
```shell
pip install easylog
```

## Usage
```python
import logging
from easylog import root_logger, setup_logging, log_stdout


root_logger.info('Setting up logging...')
logger = logging.getLogger("my_logger")

logger.info('This is a log message')
logger.debug('This is a debug message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
```