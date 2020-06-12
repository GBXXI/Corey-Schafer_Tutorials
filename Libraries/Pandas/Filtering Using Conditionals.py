# %% codecell
import pandas as pd

# %% codecell
df = pd.read_csv('D:\\GBXXI\\Software_Tests\\Test GB Python\\Corey Schafer_Tutorials\\Pandas\\developer_survey_2019\\survey_results_public.csv')
schema_df = pd.read_csv('D:\\GBXXI\\Software_Tests\\Test GB Python\\Corey Schafer_Tutorials\\Pandas\\developer_survey_2019\\survey_results_schema.csv')

# %% codecell
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

# %% codecell
df.head()

# %% codecell
# Searching for the column that the question is the salary
schema_df.set_index('Column').sort_index()

# %% codecell
# Setting the filter for high salaries, arbitary to 70,000
high_salary = (df['ConvertedComp'] >= 70_000)

# %% codecell
df.loc[high_salary]

# %% codecell
# Setting the output to certain columns
df.loc[high_salary, ['Country', 'LanguageWorkedWith', 'ConvertedComp']]

# %% codecell
# Filtering with certain critiria
countries = ['United Kingdom', 'Germany', 'Canada']
fltr = df['Country'].isin(countries)

# %% codecell
df.loc[fltr, ['Country', 'LanguageWorkedWith', 'ConvertedComp']]

# %% markdown
# The '~' symbol returns everything that does not match our filter.
# %% codecell
df.loc[~fltr, ['Country', 'LanguageWorkedWith', 'ConvertedComp']]

# %% codecell
# Filtering by manipulating sting values
fltr1 = df['LanguageWorkedWith'].str.contains('Python', na=False)

# %% codecell
df.loc[fltr1, ['Country', 'LanguageWorkedWith', 'ConvertedComp']]
