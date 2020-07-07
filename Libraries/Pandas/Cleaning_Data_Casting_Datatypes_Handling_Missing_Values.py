# %% codecell
import pandas as pd
# %% markdown
# If we want to ignore custom missing values while loading the csv, we can pass an argument of a list that it's elements we want to be treated as missing.
# %% codecell
na_vals = ['NA', 'Missing']
df = pd.read_csv('D:\\GBXXI\\Software_Tests\\Test GB Python\\Corey Schafer_Tutorials\\Libraries\\Pandas\\developer_survey_2019\\survey_results_public.csv', na_values=na_vals)
schema_df = pd.read_csv('D:\\GBXXI\\Software_Tests\\Test GB Python\\Corey Schafer_Tutorials\\Libraries\\Pandas\\developer_survey_2019\\survey_results_schema.csv', na_values=na_vals)
# %% codecell
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
# %% codecell
df.head()
# %% codecell
schema_df

# %% markdown
# Calculating the average years of coding for our dataframe.<br>
# First we see all the unique values of our column with the .unique, method.
# %% codecell
df['YearsCode'].unique()
# %% markdown
# Replacing our string values.
# %% codecell
df['YearsCode'].replace('Less than 1 year', 0, inplace=True)
df['YearsCode'].replace('More than 50 years', 51, inplace=True)
# %% markdown
# Converting our column to a float
# %% codecell
df['YearsCode'] = df['YearsCode'].astype(float)
df['YearsCode'].mean()
df['YearsCode'].median()
