
def decorator_function(og_function):
    def wrapper_function(*args, **kwargs):

        print('Executed before', og_function.__name__)

        result = og_function(*args, **kwargs)

        print('Executed after', og_function.__name__, '\n')

        return result
    return wrapper_function

@ decorator_function
def display_info(name, age):
    print(f'display_info ran with arguments ({name}, {age})')

display_info('Peter', 33)
display_info('Leia', 22)  # Output:
                          # Executed before display_info
                          # display_info ran with arguments (Peter, 33)
                          # Executed after display_info
                          #
                          # Executed before display_info
                          # display_info ran with arguments (Leia, 22)
                          # Executed after display_info

################################################################################
# Now if we want to add an argument -ie prefix- to the decorator_function, we
# have to indent one level the decorator_function and add the prefix_function
# to the top, witch takes the argument we want.
# so our function becomes like this:

def prefix_function(prefix):
    def decorator_function(og_function):
        def wrapper_function(*args, **kwargs):

            print(prefix,'Executed before', og_function.__name__)

            result = og_function(*args, **kwargs)

            print(prefix, 'Executed after', og_function.__name__, '\n')

            return result
        return wrapper_function
    return decorator_function  # Since we indented one level, we have to return
                               # the decorator_function's value.

@ prefix_function('Entered Prefix: ')  # We also change the decorator so it
def display_info(name, age):           # matches our indentation's top level.
    print(f'display_info ran with arguments ({name}, {age})')

display_info('Adam', 99)
display_info('Virgil', 65)  # Output:
                          # Entered Prefix:  Executed before display_info
                          # display_info ran with arguments (Adam, 99)
                          # Entered Prefix:  Executed after display_info
                          #
                          # Entered Prefix:  Executed before display_info
                          # display_info ran with arguments (Virgil, 65)
                          # Entered Prefix:  Executed after display_info
