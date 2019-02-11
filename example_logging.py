# https://realpython.com/python-logger/

import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')
stream_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

# Create formatters and add it to handlers
stream_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(stream_formatter)
file_handler.setFormatter(file_formatter)

# Add handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

something = 'and stuff'

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message {}'.format(something))
logger.critical('This is a critical message')

a = 5
b = 0

try:
  c = a / b
except Exception as e:
    logger.exception("Exception occurred")
