
# %% [markdown]
# Creating a simple logger in order to view how it works and how we can use it 
# for debugging and other functions. There are five levels of logging as we see bellow:
# <li>DEBUG:	Information only for problem diagnostics<br>
# <li>INFO:	    The program is running as expected<br>
# <li>WARNING:	Indicate something went wrong<br>
# <li>ERROR:	The software will no longer be able to function<br>
# <li>CRITICAL:	Very serious error<br>
# Firstly we will import the built-in logging module and then we will create some
# functions for examples.

# %% codecell
import logging
import sys
# %% codecell
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

# %% [markdown]
# Now we can print the results of our functions or we can log them on to the screen.
# %% codecell
num_x = 15
num_y = 10
# %% codecell
add_result = add(num_x, num_y)
logging.warning(f'Adding: {num_x} + {num_y} = {add_result}')
subtract_result = subtract(num_x, num_y)
logging.warning(f'Subtracting: {num_x} - {num_y} = {subtract_result}')
multiply_result = multiply(num_x, num_y)
logging.warning(f'Multipling: {num_x} * {num_y} = {multiply_result}')
divide_result = divide(num_x, num_y)
logging.warning(f'Dividing: {num_x} / {num_y} = {divide_result}')

# %% [markdown]
# As we see in the example above, our log is set as warnings, but as we conclude
# by our introduction, they are not really warnings, they are info(maybe debug).
# So we will change our logging level, using the .basicConfig method. The 
# logging.DEBUG attribute we pass on our method, is a constant that represents an
#  integer as the level of our logging. We can see those values in the table that
#  follows:<br>
#<li> CRITICAL: 50<br>
#<li> ERROR: 40<br>
#<li> WARNING: 30<br>
#<li> INFO: 20<br>
#<li> DEBUG: 10<br>
#<li> NOTSET: 0<br>
# %% codecell
logging.basicConfig(level=logging.DEBUG)
# %% codecell
add_result = add(num_x, num_y)
logging.debug(f'Adding: {num_x} + {num_y} = {add_result}')
subtract_result = subtract(num_x, num_y)
logging.debug(f'Subtracting: {num_x} - {num_y} = {subtract_result}')
multiply_result = multiply(num_x, num_y)
logging.debug(f'Multipling: {num_x} * {num_y} = {multiply_result}')
divide_result = divide(num_x, num_y)
logging.debug(f'Dividing: {num_x} / {num_y} = {divide_result}')

# %% [markdown]
# We can save our logs to a file by using the .basicConfig method.
# %% codecell
if sys.platform.startswith('win32'):
    logging.basicConfig(filename=r'Corey Schafer_Tutorials\Modules\Logging_module\
                        Logging_Basics.log', level=logging.DEBUG)

elif sys.platform.startswith('linux'):
    logging.basicConfig(filename="Modules/Logging_module/Logging_Basics.log", level=logging.DEBUG)
# %% codecell
add_result = add(num_x, num_y)
logging.debug(f'Adding: {num_x} + {num_y} = {add_result}')
subtract_result = subtract(num_x, num_y)
logging.debug(f'Subtracting: {num_x} - {num_y} = {subtract_result}')
multiply_result = multiply(num_x, num_y)
logging.debug(f'Multipling: {num_x} * {num_y} = {multiply_result}')
divide_result = divide(num_x, num_y)
logging.debug(f'Dividing: {num_x} / {num_y} = {divide_result}')

# %% [markdown]
# Through the .basicConfig method we can also configure the format of our logs as
# is shown bellow. The parameters for formating are shown in the documentation:
# https://docs.python.org/3/library/logging.html#logrecord-attributes
# %% codecell
if sys.platform.startswith('win32'):
    logging.basicConfig(filename=r'Corey Schafer_Tutorials\Modules\Logging_module\Logging_Basics.log', format="%(asctime)s\t%(levelname)s\n%(funcName)s:%(message)s", level=logging.DEBUG)

elif sys.platform.startswith('linux'):
    logging.basicConfig(filename="Modules/Logging_module/Logging_Basics.log", format="%(asctime)s\t%(levelname)s\n%(funcName)s:%(message)s", level=logging.DEBUG)

# %% [markdown]
# We can use logging with classes aswell. We can see the example with our Employee class.
# %% codecell
if sys.platform.startswith('win32'):
    logging.basicConfig(filename=r'Corey Schafer_Tutorials\Modules\Logging_module\Logging_Basics_Employee.log', format="%(asctime)s %(levelname)s\n%(funcName)s: %(message)s", level=logging.INFO)

elif sys.platform.startswith('linux'):
    logging.basicConfig(filename="Modules/Logging_module/Logging_Basics_Employee.log", format="%(asctime)s %(levelname)s\n%(funcName)s: %(message)s", level=logging.INFO)
    
# %% codecell
class Employee:

    raise_amount = 1.07  # Creating a variable to show the raise amount for our class.
    number_of_employees = 0  # Creating a counter for the number of employees.

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = float(pay)
        self.email = f'{firstname}.{lastname}@comintern.comm'

        Employee.number_of_employees += 1  # We access the counter through our
                        # class so every time we instantiate the class, we have
                        # the counter to pass the number.

        logging.info(f'#{Employee.number_of_employees}: Created Employee: \
                        {self.firstname}-{self.lastname}')

    # Creating a simple method for the Employee class.
    # We use the self argument, because every time we call this method, the
    # class will automatically pass the instance as an argument.
    def fullname(self):
        return f'{self.firstname}, {self.lastname}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # We use the self argument
                                # so we can manipulate the raise amount variable
                                # for each instance of our class.

    @classmethod
    def set_raise_amount(cls, RaiseAmount):
        cls.raise_amount = RaiseAmount  # With this method, we now can change
                                        # our raise_amount class variable.

    @classmethod
    def from_string(cls, employee_string):
        firstname, lastname, pay = employee_string.split('-')
        pay = float(pay)  # Transform our str value to a float for consistency.
        return cls(firstname, lastname, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:  # 5 is Saturday and 6 is Sunday
            return False
        return True

    def __repr__(self):
        return f'{self.firstname}, {self.lastname}, {self.pay}'

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay
        return NotImplemented

    def __len__(self):
        return len(self.fullname())

# %% [markdown]
# Creating instances of our class using our .from_string classmethod.
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
# %% codecell
employee_4.fullname()
