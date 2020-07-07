
# %% markdown
# Ways of sortind data structures.

# %% codecell
li = [9,1,8,2,7,3,6,4,5]
s_li = sorted(li)
s_li_rev = sorted(li, reverse=True)
print('Sorted variable:\t', s_li)
print('Sorted variable:\t', s_li_rev)
print('Original list', li)

# %% markdown
# If we run the .sort, method will sort the list inplace
# %% codecell
li.sort()
print(li)

# %% markdown
# Shorting a list based on the absolute values.
# %% codecell
li = [-6,-5,-4,1,2,3]
s_li = sorted(li, key=abs)
print(s_li)

# %% markdown
# When dealing with classes in order to sort class instances we have to create a function that allows the sorted method to recognize by which attribute will sort the instances.
# %% codecell

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def __repr__(self):
        return f'{self.first}, {self.last}, {self.pay}€'

e1 = Employee('Calr', 'Marx', 55_000)
e2 = Employee('Josheph', 'Stalin', 78_000)
e3 = Employee('Nikos', 'Belogiannis', 47_000)

employees = [e1, e2, e3]

# def f_key(emp):
    # return emp.first  # Using a function a key.

# f_key = lambda emp: emp.first # Using a variable with a lambda function as the key.

s_employees = sorted(employees, key=lambda emp: emp.first)
print(s_employees)

s_employees_rev = sorted(employees, key=lambda emp: emp.first, reverse=True)
print(s_employees_rev)

# %% markdown
# We can also use the .attrgetter method from the operator module.
# %% codecell
from operator import attrgetter

s_employees = sorted(employees, key=attrgetter('first'))
print(s_employees)

s_employees_rev = sorted(employees, key=attrgetter('first'), reverse=True)
print(s_employees_rev)
