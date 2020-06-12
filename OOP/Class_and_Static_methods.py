
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

# %% markdown
# We instantiate 2 objects of our class.
# %% codecell
employee_1 = Employee('Josheph', 'Stalin', 210_000)
employee_2 = Employee('Josip', 'Broz', 95_000)

# %% markdown
# In case we want to change our class variable's raise_amount we can do it by simply setting the variable directly via the class, or we can create a class method that allows us to do the same. Both ways are viewed in the example that follows:
# %% codecell
Employee.raise_amount = 1.05

Employee.raise_amount
employee_1.raise_amount
employee_2.raise_amount
# %% codecell
Employee.set_raise_amount(1.09)

Employee.raise_amount
employee_1.raise_amount
employee_2.raise_amount

# %% markdown
# Using class methods as an alternative constractor. This means we can use the class methods in order to provide multiple ways of creating our objects.<br>
# In the example bellow, we have many use cases where the values we want to create an Employee object are separated by a hyphens. So to tackle this problem we created the 'from\_string', class method. By using this method we managed to seperate the values of our string and simultaneously to have this method return the Employee objects that we want. The alternative constractors, as a convention, begin with the 'from_' title. Then we pass the class as the first argument, also by convention we use the cls name. Our second argument is the string we want to parse and seperate. Finally we return the Employee object, by using the class(cls). We could also have written the return as Employee(firstname, lastname, pay).
# %% codecell
str_employee_4 = 'Nikita-Khrushchev-140_000'
str_employee_5 = 'Aleka-Papariga-85_000'
str_employee_6 = 'Yuri-Andropov-93_000'
str_employee_7 = 'Nikolaos-Dimitratos-45_000'
str_employee_8 = 'Andreas-Tsipas-55_000'

employee_4 = Employee.from_string(str_employee_4)
employee_5 = Employee.from_string(str_employee_5)
employee_6 = Employee.from_string(str_employee_6)
employee_7 = Employee.from_string(str_employee_7)
employee_8 = Employee.from_string(str_employee_8)

# %% markdown
# So now to see that our class method works
# %% codecell
employee_4.fullname()
employee_5.pay
employee_6.lastname
employee_7.firstname
employee_8.email

# %% markdown
# Static methods are regular functions that are not bound by the class or an instance of a class. They are included in a class because they have a logical connection with that class. Therefor static methods accept only the parameters we need as an argument. We can see the example bellow.
# %% codecell
import datetime

my_date = datetime.date(2019, 7, 7)

Employee.is_workday(my_date)
