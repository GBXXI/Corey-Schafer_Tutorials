
class Employee:
    """docstring for Employee."""

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return f'{self.first} {self.last}'

emp_1 = Employee('John', 'Carter')

print(emp_1.first)  # Output: John
print(emp_1.email)  # Output: John.Carter@email.com
print(emp_1.fullname())  # Output: John Carter
print(emp_1.fullname)  # Output: <bound method Employee.fullname of <__main__.Employee object at 0x0000020283F2F8E0>> , because we do not run our method

# If we change for any reason the emp_1, name attribute we see that the
# email attribute does not change. The reason for that, is because when we
# created our class instance, emp_1, the attribute email was created from our
# original parameters.

emp_1.first = 'Jackie'

print(emp_1.first)  # Output: Jackie
print(emp_1.email)  # Output: John.Carter@email.com
print(emp_1.fullname())  # Output: Jackie Carter

################################################################################
# In order to solve the problem above, we can create a method for the email.
# The caviat here is, that if anyone is using our code, it will break, because
# they use the email as an attribute, not a method. So for us to compensate, we
# can create a method with a "@property" decorator, so as our method continues
# to behave like an attribute.

print()
print('Example 1')
print()

class Employee:
    """docstring for Employee."""

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    def fullname(self):
        return f'{self.first} {self.last}'



emp_1 = Employee('John', 'Carter')

print(emp_1.first)  # Output: John
print(emp_1.email)  # Output: John.Carter@email.com
print(emp_1.fullname())  # Output: John Carter

emp_1.first = 'Jackie'

print(emp_1.first)  # Output: Jackie
print(emp_1.email)  # Output: Jackie.Carter@email.com
print(emp_1.fullname())  # Output: Jackie Carter

################################################################################
# if we had our class redesinged and we wanted also to set the fullname as an
# attribute.

print()
print('Example 2')
print()

class Employee:
    """docstring for Employee."""

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'


emp_1 = Employee('John', 'Carter')

print(emp_1.first)  # Output: John
print(emp_1.email)  # Output: John.Carter@email.com
print(emp_1.fullname)  # Output: John Carter

# Now if we try to change our classe's instance, by the attribute fullname, we
# will get an error.

# emp_1.fullname = 'Jackie Carter'  #Output: emp_1.fullname = 'Jackie Carter'
                                  # AttributeError: can't set attribute

################################################################################
# So, to compensate for that also we have to create a 'setter'

print()
print('Example 3')
print()

class Employee:
    """docstring for Employee."""

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter  #This is our setter decorator. It must point to the function
    def fullname(self, name):  #name is the value we want to recieve i.e 'Jackie Carter'

        first, last = name.split(' ')
        self.first = first
        self.last = last


emp_1 = Employee('John', 'Carter')

print(emp_1.first)  # Output: John
print(emp_1.email)  # Output: John.Carter@email.com
print(emp_1.fullname)  # Output: John Carter

# Now with the 'setter' in place

emp_1.fullname = 'Jackie Carter'

print()
print(emp_1.first)  # Output: Jackie
print(emp_1.email)  # Output: Jackie.Carter@email.com
print(emp_1.fullname)  # Output: Jackie Carter
# print(emp_1.fullname())  # Output: TypeError: 'str' object is not callable


################################################################################
# If we want to delete attributes from our class, we use a deleter!

print()
print('Example 4')
print()

class Employee:
    """docstring for Employee."""

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter  #This is our setter decorator. It must point to the function
    def fullname(self, name):  #name is the value we want to recieve i.e 'Jackie Carter'

        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):  #Takes no other argument than the instance
        print('fullname deleted')
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Carter')

print(emp_1.first)  # Output: John
print(emp_1.email)  # Output: John.Carter@email.com
print(emp_1.fullname)  # Output: John Carter

# Now with the 'setter' in place

emp_1.fullname = 'Jackie Carter'

print()
print(emp_1.first)  # Output: Jackie
print(emp_1.email)  # Output: Jackie.Carter@email.com
print(emp_1.fullname)  # Output: Jackie Carter
# print(emp_1.fullname())  # Output: TypeError: 'str' object is not callable

del emp_1.fullname

print(emp_1.first)  # Output: None
print(emp_1.email)  # Output: None.None@email.com
print(emp_1.fullname)  # Output: None None

# If we print our instance, as bellow, we observe that only the attributes were
# deleted and not our instance, which still exists in our memory.
print(emp_1)  # Output: <__main__.Employee object at 0x000001ED896DA1F0>
