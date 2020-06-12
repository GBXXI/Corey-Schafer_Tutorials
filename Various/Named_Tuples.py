
import collections

# tuple
colour = (33, 55, 289)  # We don't know what these numbers represent

# dictionary
dict_colour = {'red': 33, 'green': 55, 'blue': 289}  # Much more readable
                                                    # still a lot of typing.

# namedtuple
colours = collections.namedtuple('colours', ['red', 'green', 'blue'])
colour = colours(red=33, green=55, blue=289)
# Also can be written as:
colour = colours(33, 55, 289)
black = colours(0, 0, 0)
# And now we can print or search much more easyly

print(colour[0])
print(colour.red)
print(colour)
print()
print(black[1])
print(black.green)  # Output:
                    # 33
                    # 33
                    #
                    # 0
                    # 0
