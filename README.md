[![Build Status](https://travis-ci.com/ellisbrown/ezcolorlog.svg?branch=master)](https://travis-ci.com/ellisbrown/ezcolorlog)
[![codecov](https://codecov.io/gh/ellisbrown/ezcolorlog/branch/master/graph/badge.svg)](https://codecov.io/gh/ellisbrown/ezcolorlog)
[![Docs](https://readthedocs.org/projects/ezcolorlog/badge)](http://ezcolorlog.readthedocs.org/en/latest/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/ellisbrown/ezcolorlog/blob/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/ezcolorlog.svg)](https://badge.fury.io/py/ezcolorlog)

# EzColorLog

`EzColorLog` is a simple pretty Python logging interface.

## Installation
```shell
pip install ezcolorlog
```

## Usage

### Basic Root Logger Usage
```python
from ezcolorlog import root_loggger as logger

logger.info('This is a log message')
logger.debug('This is a debug message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
```

### Basic Logger Usage
```python
import logging
from ezcolorlog import root_logger, setup_logging, log_stdout

root_logger.info('Setting up logging...')
logger = logging.getLogger("my_logger")

logger.info('This is a log message')
logger.debug('This is a debug message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
```

