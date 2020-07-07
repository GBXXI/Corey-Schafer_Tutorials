
##############################Zero padding example##############################
for i in range(15):
    t_out = f'Value is: {i:02}'
    print(t_out)
        # Value is: 00
        # Value is: 01
        # Value is: 02
        # Value is: 03
        # Value is: 04
        # Value is: 05
        # Value is: 06
        # Value is: 07
        # Value is: 08
        # Value is: 09
        # Value is: 10
        # Value is: 11
        # Value is: 12
        # Value is: 13
        # Value is: 14

print()

for i in range(15):
    t_out = f'Value is: {i:03}'
    print(t_out)
    # Output:
        # Value is: 000
        # Value is: 001
        # Value is: 002
        # Value is: 003
        # Value is: 004
        # Value is: 005
        # Value is: 006
        # Value is: 007
        # Value is: 008
        # Value is: 009
        # Value is: 010
        # Value is: 011
        # Value is: 012
        # Value is: 013
        # Value is: 014

#############################FLOATING POINT EXAMPLE#############################

e=2.718281828459045235360287471352662497757

# Retrieving only the first 3 decimal digits
print(f'e is equal to {e:.3f}')
# Output:
    # e is equal to 2.718
# If we ommit the 'f' in the '{e:.3f}' statement, so to become '{e:.3}'
# we get the following result:
    # e is equal to 2.72

###############################DATE TIME EXAMPLE################################

from datetime import datetime

bday = datetime(2001, 12, 30)

print(f'Sin has a birthday on {bday}')
# Output:
    # Sin has a birthday on 2001-12-30 00:00:00

# Datetime formats can be found in python's documentation
print(f'Sin has a birthday on {bday:%B %d, %Y}')
# Output:
    # Sin has a birthday on December 30, 2001
