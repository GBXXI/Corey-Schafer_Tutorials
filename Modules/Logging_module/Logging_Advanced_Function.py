
import logging
import sys

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

# ------------------------------MODULARISED LOGGER------------------------------
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

log_format = logging.Formatter('%(asctime)s %(name)s\n:%(message)s')

if sys.platform.startswith('win32'):
    file_handler = logging.FileHandler(
        r'Modules\Logging_module\Logging_Advanced_Employee.log'
    )

elif sys.platform.startswith('linux'):
    file_handler = logging.FileHandler("Modules/Logging_module/Logging_Advanced_Employee.log")

file_handler.setFormatter(log_format)
logger.addHandler(file_handler)

if __name__ == '__main__':

    num_x = 15
    num_y = 10

    add_result = add(num_x, num_y)
    logger.debug(f'Adding: {num_x} + {num_y} = {add_result}')
    subtract_result = subtract(num_x, num_y)
    logger.debug(f'Subtracting: {num_x} - {num_y} = {subtract_result}')
    multiply_result = multiply(num_x, num_y)
    logger.debug(f'Multipling: {num_x} * {num_y} = {multiply_result}')
    divide_result = divide(num_x, num_y)
    logger.info(f'Dividing: {num_x} / {num_y} = {divide_result}')
