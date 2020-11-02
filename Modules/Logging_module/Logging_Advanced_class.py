
import logging
import sys

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

        logger.info(
            f'#{Employee.number_of_employees}: Created Employee: {self.firstname}-{self.lastname}'
        )

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
# ------------------------------MODULARISED LOGGER------------------------------
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# log_format = logging.Formatter('%(asctime)s %(levelname)s\n%(funcName)s: %(message)s')
log_format = logging.Formatter('%(asctime)s %(levelname)s\n%(message)s')

if sys.platform.startswith('win32'):
    file_handler = logging.FileHandler(r'Corey Schafer_Tutorials\Modules\Logging_module\
                                        Logging_Advanced_Employee.log')

elif sys.platform.startswith('linux'):
    file_handler = logging.FileHandler("Modules/Logging_module/Logging_Advanced_Employee.log")

file_handler.setFormatter(log_format)

logger.addHandler(file_handler)

if __name__ == '__main__':

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
