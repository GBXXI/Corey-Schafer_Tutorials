
# %% markdown
# Context managers, allows us to proprerly manage resources in order to specify excplicity what we want to set-up and tear-down, when working with certain objects.
# %% markdown
# In the example bellow, we create a context manager, using a class.
# %% codecell
class CustomOpen(object):

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file  = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

# %% markdown
# Now, we can check if our context manager works, by creating a file and then checking if it is automatically, closed.
# %% codecell
with CustomOpen(r'Corey Schafer_Tutorials\Various\Context_Manager_test.txt', 'w+') as file:
    file.write('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

print(file.closed)

# %% markdown
# Creating a context manager using a function and the contextlib module.
# %% codecell
from contextlib import contextmanager

@contextmanager
def Custom_Open(filename, mode):
    try:
        file = open(filename, mode)
        yield(file)
    finally:
        file.close()

# %% markdown
# Now, we can check if our context manager works, by creating a file and then checking if it is automatically, closed.
# %% codecell
with Custom_Open(r'Corey Schafer_Tutorials\Various\Context_Manager_test.txt', 'w+') as file:
    file.write("""Shut up! Will you shut up?! I don't want to talk to you no more, you empty-headed animal food trough water! I fart in your general direction! Your mother was a hamster and your father smelt of elderberries! Now leave before I am forced to taunt you a second time!

On second thoughts, let's not go there. It is a silly place. And the hat. She's a witch! Why do you think that she is a witch? And the hat. She's a witch! Did you dress her up like this? Bring her forward!

Burn her anyway! But you are dressed as one… What a strange person. No, no, no! Yes, yes. A bit. But she's got a wart.

Well, I didn't vote for you. The swallow may fly south with the sun, and the house martin or the plover may seek warmer climes in winter, yet these are not strangers to our land. How do you know she is a witch?

He hasn't got shit all over him. You don't vote for kings. Why do you think that she is a witch? Now, look here, my good man.

Burn her! Bring her forward! Well, I got better. Look, my liege!

We found them. Oh, ow! Burn her! Bring her forward! How do you know she is a witch?

Well, what do you want? A newt? I don't want to talk to you no more, you empty-headed animal food trough water! I fart in your general direction! Your mother was a hamster and your father smelt of elderberries! Now leave before I am forced to taunt you a second time!

Oh! Come and see the violence inherent in the system! Help, help, I'm being repressed! Shh! Knights, I bid you welcome to your new home. Let us ride to Camelot! The Knights Who Say Ni demand a sacrifice!

Well, I didn't vote for you. I have to push the pram a lot. Burn her anyway! Well, how'd you become king, then?

Well, we did do the nose. You don't frighten us, English pig-dogs! Go and boil your bottoms, sons of a silly person! I blow my nose at you, so-called Ah-thoor Keeng, you and all your silly English K-n-n-n-n-n-n-n-niggits!""")

print(file.closed)

# %% markdown
# As a practical example, we will create a context manager that will allow us, after the resources tear-down to return to our current working directory. As opposed to our previous function the yield statement does not return anything since we do not work with any variables with our context manager.
# %% codecell
import os
from contextlib import contextmanager

@contextmanager
def switch_directory(directory):
    try:
        cwd = os.getcwd()
        os.chdir(directory)
        yield
    finally:
        os.chdir(cwd)

# %% markdown
# Now we can test our context manager.
# %% codecell

with switch_directory('Code_Wars'):
    print(f"Directory's {os.getcwd()} elements are:\n{os.listdir()}")

with switch_directory('DataSchool_Tutorials'):
    print(f"Directory's {os.getcwd()} elements are:\n{os.listdir()}")

print(f"The original directory is:\n{os.getcwd()}")
