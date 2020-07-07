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
# Renaming column as a view
df.rename(columns={'ConvertedComp': 'SalaryUSD'})

# %% codecell
# Renaming column as permanantly
df.rename(columns={'ConvertedComp': 'SalaryUSD'}, inplace=True)

# %% codecell
df['SalaryUSD']

# %% codecell
# Changing the values of the Hobbyist column, as a view
df['Hobbyist'].map({'Yes': 'True', 'No': 'False'})

# %% codecell
# Changing the values of the Hobbyist column, as permanantly
df['Hobbyist'] = df['Hobbyist'].map({'Yes': 'True', 'No': 'False'})

# %% codecell
df
