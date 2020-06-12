
# %% markdown
# Class variables, are variables that are shared among all instances of a class.
# %% codecell
class Employee:

    raise_amount = 1.07  # Creating a variable to show the raise amount for our class.
    number_of_employees = 0  # Creating a counter for the number of employees.

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
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

# %% markdown
# We instantiate 2 objects of our class.
# %% codecell
employee_1 = Employee('Josheph', 'Stalin', 100_000)
employee_2 = Employee('Josip', 'Broz', 95_000)

# %% markdown
# Applying raise for all our instances
# %% codecell
Employee.raise_amount
employee_1.apply_raise()
employee_1.pay
employee_2.apply_raise()
employee_2.pay

# %% markdown
# Updating the raise amount for our first employee.
# %% codecell
Employee.raise_amount
employee_1.raise_amount = 1.09
employee_1.apply_raise()
employee_1.pay
employee_2.apply_raise()
employee_2.pay

# %% markdown
# In the above case what happens is, that when we try to access an attribute on an instance, it will first check if the instance contains that attribute. If it does, the instance's value will be used, like we see in our employee_1, otherwise it will check to see if the class or anyother class that inherits from has that attribute, like we see on our employee_2. The example that follows shows the attributes and the names of our class and our instances.
# %% codecell
Employee.__dict__
employee_1.__dict__
employee_2.__dict__

# %% markdown
# Finally, we can check the total number of our employees through our class variable.
# %% codecell
Employee.number_of_employees
