
# Closures
#
# A closure is a record storing a function together with an enviroment:
# a mapping associating each free variable of the function with the value or
# storage location to which the name was bound when the closure was created.
# A closure, unlike a plain function, allows the function
# to access those captured variables through the closure's reference to them,
# even when the function is invoked outside their scope

print('Example 1')

def outer_func():
    message = 'Hilo'

    def inner_func():
        print(message, '::Inner function')

    return inner_func  # Without the () the inner_func is not called
# outer_func()

my_func = outer_func()

print(my_func.__name__, '::my_func.__name__')  # Output: inner_func

# So we can execute the variable my_func as a function
my_func()  # Output: Hilo

# In simple: A closure is an inner function tha remebers and has access to
# variables in the local scope in which it was created, even after the outer
# function has finished executing

################################################################################
# Function with parameters

print('Example 2')

def outer_func(msg):
    message = msg

    def inner_func():
        print(message, '::Inner function')

    return inner_func  # Without the () the inner_func is not called

my_func = outer_func  # Without the () the function is not called

per_func = my_func('msg Test')

print(per_func)  # Output: <function outer_func.<locals>.inner_func at 0x000001EA571C5160>

per_func()  # Output: msg Test ::Inner function.
            # By putting the ()  we see that the function is called so
            # the inner's fuction body is executed

################################################################################
# Example with JavaScript

print('Example 3')
'''
function html_tag(tag){
    function wrap_text(msg){
    console.log('<' + tag + '>' + msg + '</' + tag + '>')
    }
    return wrap_text
}

var print_h1 = html_tag('h1')

print_h1('Testing headline')  // Output: <h1>Testing headline</h1>

var print_pargraph = html_tag('p')

print_pargraph('Testing paragraph')  // Output: <p>Testing paragraph</p>
'''

################################################################################

print('Example 4')

import logging as lg

lg.basicConfig(filename='Closures_example.log', level=lg.INFO)

def logger(func):

    def log_func(*args):
        # lg.info('Running "{}" with arguments {}'.format(func.__name__, args))
        lg.info(f'Running "{func.__name__}" with arguments {args}')
        print(func(*args))

    return log_func

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

add_logger = logger(add)  # Parameter is passed to the outer logger function
sub_logger = logger(sub)  # Parameter is passed to the outer logger function

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(9, 12)
