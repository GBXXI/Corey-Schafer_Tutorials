
# %% codeblock
import pandas as pd

df = pd.read_csv('D:\\Test GB Python\\Corey Schafer_Tutorials\\Pandas\\developer_survey_2019\\survey_results_public.csv')
schem_df = pd.read_csv('D:\\Test GB Python\\Corey Schafer_Tutorials\\Pandas\\developer_survey_2019\\survey_results_schema.csv')
# %% codecell
pd.set_option('display.max_columns', 85)
# %% codeblock
df
# %% codeblock
people = {"first": ["Corey", "Jane", "John"],
         "last": ["Schafer", "Doe", "Doe"],
         "email": ["CoreySchafer@gmail.com", "JaneDoe@bogusmail.org", "JohnDoe@company.com"]}
# %% codecell
p_df = pd.DataFrame(people)
# %% codecell
p_df
# %% codecell
p_df['email']
# %% codecell
type(p_df['email'])
# %% codecell
p_df[['last', 'email']] # Passing a list as an argument
# %% codecell
type(p_df[['last','email']])
# %% codecell
# Accessing rows in a dataframe
# iloc, stands for integer location
# loc, stands for location
# %% codecell
p_df.iloc[0]
# %% codecell
p_df.iloc[[0,1], 1]  # The first list is our rows and the second is our columns,
# with ilock we cannot pass a column name, only it's inde
# %% codecell
p_df.loc[[0,1], 'email']  # With loc we can pass columns name

# %% codecell
p_df.loc[[0,1], ['email', 'last']]  # With loc we can pass columns name

# %% codecell
# Setting index as a view
p_df.set_index('email')

# %% codecell
# Setting index permanantly
p_df.set_index('email', inplace=True);

# %% codecell
p_df

# %% codecell
# This helps us to find information about a row more easily
p_df.loc['JaneDoe@bogusmail.org']

# %% codecell
# Reseting the indexes
p_df.reset_index(inplace=True)

# %% codecell
p_df
