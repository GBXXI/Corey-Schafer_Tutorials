
# %% markdown
# Methods are the functions associated with a class.<br>
# Instance varables contain data that is unique to each instance.<br>
# In the example bellow, the parameters firstname, lastname, pay and also the email, are attributes of this class.
# %% codecell
class Employee:

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = f'{firstname}.{lastname}@comintern.comm'

    # Creating a simple method for the Employee class.
    # We use the self argument, because every time we call this method, the
    # class will automatically pass the instance as an argument.
    def fullname(self):
        return f'{self.firstname}, {self.lastname}'

# %% markdown
# We instantiate 2 objects of our class.
# %% codecell
employee_1 = Employee('Josheph', 'Stalin', 100_000)
employee_2 = Employee('Josip', 'Broz', 95_000)

# %% markdown
# We now can call our instances and view their attributes.
# %% codecell
employee_1.email
employee_2.lastname

# %% markdown
# Calling a method of our class can be performed with 2 ways.<br>
# First, we access the method through the instance.
# %% codecell
employee_1.fullname()

# %% markdown
# Secondly, we access the method through the class. Note that in this case we have<br>
# to pass the instance as an argument.
# %% codecell
Employee.fullname(employee_2)
