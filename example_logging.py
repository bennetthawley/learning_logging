# https://realpython.com/python-logging/

import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='log.log',
                    filemode='w',
                    format='Filename: %(filename)s - Timestamp: %(asctime)s'
                           ' - %(levelname)s - Line Number: %(lineno)d - '
                           'Message: %(message)s\n',
                    datefmt='%x %X')

something = 'and stuff'

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message {}'.format(something))
logging.critical('This is a critical message')

a = 5
b = 0

try:
  c = a / b
except Exception as e:
  logging.exception("Exception occurred")
