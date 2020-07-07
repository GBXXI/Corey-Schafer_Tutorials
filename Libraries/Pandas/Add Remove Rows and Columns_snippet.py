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

# %% markdown
# Creating the values for fullname, as a view
# %% codecell
p_df['first'] + ' ' + p_df['last']

# %% markdown
# Creating a new column and assigning the fullname values
# %% codecell
p_df['full name'] = p_df['first'] + ' ' + p_df['last']

# %% codecell
p_df

# %% markdown
# Deleting multiple columns, as a view
# %% codecell
p_df.drop(columns=['first', 'last'])

# %% markdown
# Deleting multiple columns, permanently
# %% codecell
p_df.drop(columns=['first', 'last'], inplace=True)

# %% codecell
p_df

# %% markdown
# Recreating the first and last name columns, as a view
# %% codecell
p_df['full name'].str.split(' ')

# %% markdown
# We see that from the above split we take a list as an output, <br>
# So in order to have them individualy so as to recreate the first and last<br>
# name columns we do the following:
# %% codecell
p_df['full name'].str.split(' ', expand=True)

# %% markdown
# As we see now we can assign those column values to our recreated columns
# %% codecell
p_df[['first', 'last']] = p_df['full name'].str.split(' ', expand=True)

# %% codecell
p_df

# %% markdown
# Appending a single row, using the ignore_index parameter
# %% codecell
p_df.append({'first': 'Trevor', 'last': 'Michaels',
'email': 'TrevorMichaels@hotmail.com',
'full name': 'Trevor Michaels'}, ignore_index=True)

# %% markdown
# Appending one dataframe to another. <br>
# First we create the second dataframe:
# %% codecell
heroes = {
'first': ['Tony', 'Steve'],
'last': ['Stark', 'Rogers'],
'email': ['IronMan@aveng.com', 'CapAm@aveg.com']
}

p_df2 = pd.DataFrame(heroes)

# %% markdown
# Appending the second dataframe, as a view: <br>
# We use the ignore_index parameter because our dataframes do not have<br>
# the same indexes
# %% codecell
p_df.append(p_df2, ignore_index=True)
# %% markdown
# Appending the second dataframe, permanently: <br>
# We use the ignore_index parameter because our dataframes do not have<br>
# the same indexes
# %% codecell
p_df = p_df.append(p_df2, ignore_index=True)

# %% markdown
# Droping a row by index number
# %% codecell
p_df.drop(index=4)

# %% markdown
# Deleting rows with a conditional value, as a view.<br>
# We also use the '.index' method so as the indexes of our contitional<br>
# to be used.
# %% codecell
contitional = p_df['last'] == 'Doe'
p_df.drop(index=p_df[contitional].index)
