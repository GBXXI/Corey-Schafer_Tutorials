
# %% markdown
# Since every time we import a module, it is first runned, the root logger is configured by the module that gets imported first. To avoid that and also to add the functionality of different loggers, we must modularise our loggers. After that when we run our main module we can see we have a number of differnt loggers.
# %% codecell
import logging
from Logging_Advanced_class import Employee
from Logging_Advanced_Function import add, subtract, multiply, divide

# %% markdown
# Now we can create a logger who only prints to our screen, also known as a streamer.
# %% codecell
logger = logging.getLogger(__name__)
logger.setLevel(10)

log_format = logging.Formatter('%(created)f \t %(lineno)d \n %(thread)d:%(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_format)
stream_handler.setLevel(10)


logger.addHandler(stream_handler)


# %% codecell
num_x = 15
num_y = 10
# %% codecell
add_result = add(num_x, num_y)
logger.debug(f'Adding: {num_x} + {num_y} = {add_result}')
subtract_result = subtract(num_x, num_y)
logger.debug(f'Subtracting: {num_x} - {num_y} = {subtract_result}')
multiply_result = multiply(num_x, num_y)
logger.debug(f'Multipling: {num_x} * {num_y} = {multiply_result}')
divide_result = divide(num_x, num_y)
logger.debug(f'Dividing: {num_x} / {num_y} = {divide_result}')
# %% codecell
str_employee_4 = 'Nikita-Khrushchev-140_000'
str_employee_5 = 'Aleka-Papariga-85_000'
str_employee_6 = 'Yuri-Andropov-93_000'
str_employee_7 = 'Konstantinos-Koligiannis-45_000'
str_employee_8 = 'Grigoris-Farakos-55_000'

employee_4 = Employee.from_string(str_employee_4)
employee_5 = Employee.from_string(str_employee_5)
employee_6 = Employee.from_string(str_employee_6)
employee_7 = Employee.from_string(str_employee_7)
employee_8 = Employee.from_string(str_employee_8)
