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
p_df.columns

# %% codecell
# Assign names with a list
p_df.columns = ['First name', 'Last name', 'E-mail']

# %% codecell
# List comprehension
p_df.columns = [x.capitalize() for x in p_df.columns]

# %% codecell
# Stripping whitespace between words and repalcing it with underscore
p_df.columns = p_df.columns.str.replace(' ', '_')

# %% codecell
# Changing the name for some columns, as a view
p_df.rename(columns={'First_name':'FirstName', 'Last_name':'LastName'})

# %% codecell
# Changing the name for some columns, Permanently
p_df.rename(columns={'First_name':'FirstName', 'Last_name':'LastName'}, inplace=True)

# %% codecell
# Updating a single value
# Finding the row whose value we want to update
p_df.loc[2]

# %% codecell
# Changing the last name
p_df.loc[2] = ['John', "Smith", "JohnSmith@company.com"]

# %% codecell
# An easier way is by selecting only the values we want to change
p_df.loc[2, ['LastName', 'E-mail']]
# %% codecell
p_df.loc[2, ['LastName', 'E-mail']] = ["Smithen", "JohnSmithen@company.com"]

# %% codecell
# Updating a column
# Returned as a view
p_df['E-mail'].str.lower()

# %% codecell
# Updating permanently
p_df['E-mail'] = p_df['E-mail'].str.lower()

# %% codecell
# The four(4) methods for updating a column are:
#       apply, is used for calling a function on our values and can work on
               # either a data frame or a series object
#       map, is used for substituting each value in a series.
             # Only works on a series.
#       applymap, is used to apply  a function to every individual in a
                  # dataframe. Only works on dataframes
#       replace

# %% codecell
# Apply on a series
p_df['E-mail'].apply(len)

# %% codecell
def updt_email(email):
    return email.upper();

# %% codecell
p_df['E-mail'].apply(updt_email)

# %% codecell
# Same execution as above but with a lambda function
p_df['E-mail'].apply(lambda e: e.lower())

# %% codecell
# Applying a function on a dataframe
p_df.apply(len)  # Applyies each function on each series on a dataframe

# %% codecell
# Taking the minimum value from a series of strings
p_df.apply(pd.Series.min)

# %% codecell
# Same execution as above but with a lambda function
p_df.apply(lambda m: m.min())

# %% codecell
# Using applymap. Applying len() function for each element in the dataframe
p_df.applymap(len)

# %% codecell
# Applying lower() function for each element in the dataframe
p_df.applymap(str.lower)

# %% codecell
# Using map. Substituting first names
p_df['FirstName'].map({'Corey': 'Petros', 'Jane': 'Johnanna'})
