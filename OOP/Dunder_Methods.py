
# %% markdown
# Special methods allows us to emulate some built-in Python behavior and operator overloading, in our classes.

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
# The special method __repr__ is meant to be an unambiguous representation of an object, and should be used for debugging and logging. Furthermore, __repr__ is the fallback of the __str__ method. A good rule is that the __repr__ method should display an output that will allow us to recreate the object, if we copy-paste the output in Python code.
# %% codecell
repr(employee_5)

# %% markdown
# The special method __str__ is meant to be a redable representation of an object and should be used as a display to the end user every time we print that object.
# %% codecell
print(employee_5)

# %% markdown
# The special method __add__ is what is called an operator overload. Because Python does not know how to perform certain actions with our objects, we must specify that with those special methods. In the documentation we can see that there are many more special methods such as: __module__, __name__ etc. In our example here we instruct Python to add the salary of our instances, every time the '+' operator is used.
# %% codecell
employee_7 + employee_8
# %% markdown
# Finally, the special method __len__ is also an operation overload. Same as with the operator '+' and the __add__ method, here we must also instruct Python how to perform this operation. In our example we use the fullname, as the length of our object.
# %% codecell
employee_4.fullname()
len('Nikita, Khrushchev')
len(employee_4)
