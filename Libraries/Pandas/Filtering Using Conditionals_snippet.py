# %% codecell
import pandas as pd

# %% codecell
people = {"first": ["Corey", "Jane", "John"],
         "last": ["Schafer", "Doe", "Doe"],
         "email": ["CoreySchafer@gmail.com", "JaneDoe@bogusmail.org", "JohnDoe@company.com"]}

# %% codecell
p_df = pd.DataFrame(people)

# %% codecell
p_df

# %% codecell
# Showing data by last name, True/False values
p_df['last'] == 'Doe'

# %% codecell
# Filtering data by last name, filter is a built-in python keyword
filt = (p_df['last'] == 'Doe')

# %% codecell
p_df[filt]

# %% codecell
# In order to have a specific column in our filter we use the .loc
p_df.loc[filt, 'email']

# %% codecell
# XOR operators: Since 'and' and 'or' are python built-in keywords we use
# the '&', '|' symbols
filt = (p_df['last'] == 'Doe') & (p_df['first'] == 'John')

# %% codecell
# Using '|' 'or' operator
filt = (p_df['last'] == 'Schafer') | (p_df['first'] == 'John')

# %% codecell
# The exclution operator '~' gives us results where our filter does not apply
p_df.loc[~filt, 'email']
