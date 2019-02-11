import logging
logging.basicConfig(filename='logging_stuff.log',
                    filemode='w',
                    format='%(asctime)s = %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)
logging.disable(logging.CRITICAL)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial {}'.format(n))
    total =1
    for i in range(1, n+1):
        total *= i
        logging.info('i is {}, total is {}'.format(i,total))
    logging.debug('Return value is {}'.format(total))
    return total

print(factorial(5))

logging.debug('End of program')