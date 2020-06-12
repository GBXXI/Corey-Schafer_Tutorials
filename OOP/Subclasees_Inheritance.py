
# %% markdown
# Inheritance allows us to inherit attributes and methods from a "parent" class. This means we can create subclasses and get all of the functionality of our parent class. We then can overwrite or add completely new functionality without affecting the "parent" class.

# %% markdown
# Fist we create our parent class, Employee.
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

# %% markdown
# Now we can create a subclasse called Developers. First we pass as an argument the class we inherit from. Then we instantiate the parent class to have all of it's attributes and functionality.
# %% codecell
class Developer(Employee):

    def __init__(self, firstname, lastname, pay, programmming_language):
        Employee.__init__(self, firstname, lastname, pay)
        self.programmming_language = programmming_language

# %% markdown
# Creating instances of our subclass.
# %% codecell
dev_1 = Developer('Andreas', 'Tsipas', 87_000, 'JavaScript')
dev_2 = Developer('Nikolaos', 'Dimitratos', 72_5000, 'Python')
dev_3 = Developer('Erich', 'Honecker', 96_743, 'Objective C')
dev_4 = Developer('Wilhelm', 'Pieck', 108_350, 'C++')

# %% markdown
# Viewing the inherited attributes and functions of our parent class.
# %% codecell
dev_1.email
dev_3.fullname()
# %% codecell
Developer.raise_amount
dev_1.pay
Developer.set_raise_amount(1.11)
Employee.raise_amount  # Our parent class is not afflicted by our chances.
dev_1.apply_raise()
dev_1.pay

# %% markdown
# We can now create another subclass, named Manager.
# %% codecell
class Manager(Employee):

    def __init__(self, firstname, lastname, pay, subordinates=None):
        Employee.__init__(self, firstname, lastname, pay)

        if subordinates is None:
            self.subordinates = []
        else:
            self.subordinates = subordinates

    def add_subordinate(self, employee):
        if employee not in self.subordinates:
            self.subordinates.append(employee)

    def remove_subordinate(self, employee):
        if employee in self.subordinates:
            self.subordinates.remove(employee)

    def print_subordinates(self):
        for employee in self.subordinates:
            print('--->', employee.fullname())

# %% markdown
# Creating instances of our subclass.
# %% codecell
manager_1 = Manager('Apostolos', 'Grozos', 120_000, [employee_4, employee_5, dev_1])
manager_2 = Manager('Vladimir', 'Lenin', 210_000, [employee_6, employee_7, dev_2, dev_4])
manager_3 = Manager('Nikita', 'Khrushchev', 37_000, [employee_8, dev_3])

# %% markdown
# Viewing how our parent class counter is affected by the instances of our subclasses.
# %% codecell
Manager.number_of_employees
Employee.number_of_employees
Developer.number_of_employees

# %% markdown
# Viewing our manger's subclass methods and attributes, both inherited and not.
# %% codecell
manager_2.print_subordinates()

manager_2.add_subordinate(manager_1)
manager_2.add_subordinate(manager_3)
manager_2.print_subordinates()

manager_2.remove_subordinate(manager_3)
manager_2.print_subordinates()

manager_1.fullname()
manager_3.pay

from datetime import date
day = date(2020, 5, 3)
manager_2.is_workday(day)
