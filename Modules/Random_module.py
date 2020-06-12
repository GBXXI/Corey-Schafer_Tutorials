# %% markdown
# We can use the random module for creating "dummy" data or creating random values for us to use in an application.
# %% codecell
import random

# %% markdown
# For creating a value between 0 and 1(exclusive) we can use the .random, method.
# %% codecell
value = random.random()
value

# %% markdown
# Creating a random floating point value in a specified range with the .uniform, method.
# %% codecell
value = random.uniform(1, 10)
value

# %% markdown
# Creating a random integer value in a specified range with the .randint, method.
# %% codecell
value = random.randint(1, 10)
value

# %% markdown
# Picking a random value from a list of values, with the .choice method.
# %% codecell
greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']
value = random.choice(greetings)
value

# %% markdown
# Picking a random value from a list of values, given significance to each value outcome with the .choices method. k is the number of repetitions to be applyed to our choices.
# %% codecell
colours = ['Black', 'Red', 'Green']
value = random.choices(colours, weights=[18,18,2], k=10)
value

# %% markdown
# Randomly suffle a list of values with the .shuffle, method. This method shuffles the list in place so if we want to keep the order of the original list we must first create a copy of it to be shuffled.
# %% codecell
deck = list(range(1,53))
random.shuffle(deck)
print(deck)

# %% markdown
# Randomly selecting unique values from a sequence with the .sample, method.
# %% codecell
deck = list(range(1,53))
hand = random.sample(deck, k=5)
hand
