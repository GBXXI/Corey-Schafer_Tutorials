
#################################CLOSURE RECAP##################################
print('CLOSURE RECAP')
print()

def outer_func(msg):
    message = msg

    def inner_func():
        print(message, '::Inner function')

    return inner_func

hi_f = outer_func
b_f = outer_func

hi_f('hi')()  # The same as the function assingment and calling as below
print()
bye_f = b_f('bye')
bye_f()

# Alternatively written as:
print()

def outer_func(msg):
    def inner_func():
        print(msg, '::Inner function')

    return inner_func

hi_f = outer_func
b_f = outer_func

hi_f('hi')()  # The same as the function assingment and calling as below
print()
bye_f = b_f('bye')
bye_f()

################################################################################
# Decorator is a function that takes another function as an argument adds
# functionality and returns another function. All of this, without altering
# the source code of the original function

print()
print('DECORATORS_EXAMPLE 1')
print()

def decorator_function(og_function):
    def wrapper_function():
        print(f'Wrapper_function is now executing: {og_function.__name__}')
        return og_function()
    return wrapper_function

def display():
    print('def display(), ran')

decorated_display = decorator_function(display)

decorated_display()  # Output:
            # Wrapper_function is now executing: display
            # def display(), ran

################################################################################
# The above example can also be written as follows:
print()
print('DECORATORS_EXAMPLE 2')
print()

def decorator_function(og_function):
    def wrapper_function():
        print(f'Wrapper_function is now executing: {og_function.__name__}')
        return og_function()
    return wrapper_function

@decorator_function
def display():
    print('def display(), ran')

print('Calling the function display(): ')
display()  # With the decorator we get the excact output as the example above
           # just by calling the function. It is the same as writting
           # display = decorator_function(display)

################################################################################
# The examples above would not work if we had an og_function that has arguments

print()
print('DECORATORS_EXAMPLE 3')
print()

def decorator_function(og_function):
    def wrapper_function():
        print(f'Wrapper_function is now executing: {og_function.__name__}')
        return og_function()
    return wrapper_function

@decorator_function
def display():
    print('def display(), ran')

@decorator_function
def display_info(name, age):
    print(f'display_info ran with arguments ({name}, {age})')

# Using a try\except block so the programm does not crash

try:
    display_info('Elias', 45)

except Exception as e:
    print('The exeption occured is :', e)

print()
print('Calling the function display(): ')
display()

################################################################################
# In order to correct the problem of the above example we rewrite as follows
print()
print('DECORATORS_EXAMPLE 4')
print()

def decorator_function(og_function):
    def wrapper_function(*args, **kwargs):
        print(f'Wrapper_function is now executing: {og_function.__name__}')
        return og_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print('def display(), ran')

@decorator_function
def display_info(name, age):
    print(f'display_info ran with arguments ({name}, {age})')

print('Calling the function display_info()')
display_info('Tom', 79)

print()
print('Calling the function display(): ')
display()

################################################################################
# Using Classes as decorators
print()
print('DECORATORS_EXAMPLE 5')
print()

class decorator_class(object):

    def __init__(self, og_function):

        self.og_function = og_function

    def __call__(self, *args, **kwargs):  # This mimics the operation of our
                                          # wrapper_function as the examples
                                          # above
        print(f'__call__ function is now executing: {self.og_function.__name__}')
        return self.og_function(*args, **kwargs)

@decorator_class
def display():
    print('def display(), ran')

@decorator_class
def display_info(name, age):
    print(f'display_info ran with arguments ({name}, {age})')

print('Calling the function display_info(): ')
display_info('Nick', 55)

print()
print('Calling the function display(): ')
display()

################################################################################
# Practical example: A simple logger
print()
print('DECORATORS_EXAMPLE 6')
print()


def my_logger(og_function):
    import logging as lg

    lg.basicConfig(filename=f'{og_function.__name__}.log', level=lg.INFO)
    # lg.basicConfig(filename='{}.log'.format(og_function.__name__), level=lg.INFO)

    def logger_wrapper_function(*args, **kwargs):

        lg.info(f'Logger_wrapper_function ran with args: {args} and kwargs: {kwargs}')
        return og_function(*args, **kwargs)

    return logger_wrapper_function

def my_timer(og_function):
    import time

    def timer_wrapper_function(*args, **kwargs):
        t1 = time.time()
        result = og_function(*args, **kwargs)
        dt = time.time() - t1
        print(f'{og_function.__name__} ran in: {dt} sec')
        return result

    return timer_wrapper_function

@ my_logger
def display_info(name, age):
    import time
    time.sleep(2)  # Introducing sleep function in order to have visble results

    print(f'display_info ran with arguments ({name}, {age})')

display_info('Kelly', 34)

################################################################################
# Practical example: A simple logger, stacking decorators
print()
print('DECORATORS_EXAMPLE 7')
print()

def my_logger(og_function):
    import logging as lg

    lg.basicConfig(filename=f'{og_function.__name__}.log', level=lg.INFO)
    # lg.basicConfig(filename='{}.log'.format(og_function.__name__), level=lg.INFO)

    def logger_wrapper_function(*args, **kwargs):

        lg.info(f'Logger_wrapper_function ran with args: {args} and kwargs: {kwargs}')
        return og_function(*args, **kwargs)

    return logger_wrapper_function

def my_timer(og_function):
    import time

    def timer_wrapper_function(*args, **kwargs):
        t1 = time.time()
        result = og_function(*args, **kwargs)
        dt = time.time() - t1
        print(f'{og_function.__name__} ran in: {dt} sec')
        return result

    return timer_wrapper_function

@ my_timer
@ my_logger
def display_info(name, age):
    import time
    time.sleep(2)  # Introducing sleep function in order to have visble results

    print(f'display_info ran with arguments ({name}, {age})')

display_info('Marlo', 51)  #Output: display_info ran with arguments (Marlo, 51)
                        # logger_wrapper_function ran in: 2.0007567405700684 sec

print(display_info.__name__)  #Output: timer_wrapper_function

#Here we see that the time_wrapper_function was ran, because of the decorators
# stacking, something we do not want

###########################SWITCHING DECORATORS ORDER###########################
print()
print('DECORATORS_EXAMPLE 7.1')
print()

def my_logger(og_function):
    import logging as lg

    lg.basicConfig(filename=f'{og_function.__name__}.log', level=lg.INFO)
    # lg.basicConfig(filename='{}.log'.format(og_function.__name__), level=lg.INFO)

    def logger_wrapper_function(*args, **kwargs):

        lg.info(f'Logger_wrapper_function ran with args: {args} and kwargs: {kwargs}')
        return og_function(*args, **kwargs)

    return logger_wrapper_function

def my_timer(og_function):
    import time

    def timer_wrapper_function(*args, **kwargs):
        t1 = time.time()
        result = og_function(*args, **kwargs)
        dt = time.time() - t1
        print(f'{og_function.__name__} ran in: {dt} sec')
        return result

    return timer_wrapper_function

@ my_logger
@ my_timer
def display_info(name, age):
    import time
    time.sleep(2)  # Introducing sleep function in order to have visble results

    print(f'display_info ran with arguments ({name}, {age})')

display_info('Braian', 44)  # Output: display_info ran with arguments (Braian, 44)
                            # display_info ran in: 2.0007410049438477 sec

print(display_info.__name__)  # Output: logger_wrapper_function

# Here we see that the logger_wrapper_function was ran, because of the decorators
# stacking, something we do not want

##############################INTODUCING FUNCTOLLS##############################

from functools import wraps

print()
print('DECORATORS_EXAMPLE 7.2')
print()

def my_logger(og_function):
    import logging as lg

    lg.basicConfig(filename=f'{og_function.__name__}.log', level=lg.INFO)
    # lg.basicConfig(filename='{}.log'.format(og_function.__name__), level=lg.INFO)

    @wraps(og_function)
    def logger_wrapper_function(*args, **kwargs):

        lg.info(f'Logger_wrapper_function ran with args: {args} and kwargs: {kwargs}')
        return og_function(*args, **kwargs)

    return logger_wrapper_function

def my_timer(og_function):
    import time

    @wraps(og_function)
    def timer_wrapper_function(*args, **kwargs):
        t1 = time.time()
        result = og_function(*args, **kwargs)
        dt = time.time() - t1
        print(f'{og_function.__name__} ran in: {dt} sec')
        return result

    return timer_wrapper_function

@ my_logger
@ my_timer
def display_info(name, age):
    import time
    time.sleep(2)  # Introducing sleep function in order to have visble results

    print(f'display_info ran with arguments ({name}, {age})')

display_info('Annie', 21)  # Output: display_info ran with arguments (Annie, 21)
                           # display_info ran in: 2.000760078430176 sec

print(display_info.__name__)  # Output: display_info
