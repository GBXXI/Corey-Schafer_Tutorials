# %% codecell
import pandas as pd
# %% codecell
df = pd.read_csv('D:\\GBXXI\\PROGRAMMING\\GB Python\\Corey Schafer_Tutorials\\Libraries\\Pandas\\developer_survey_2019\\survey_results_public.csv')
schema_df = pd.read_csv('D:\\GBXXI\\PROGRAMMING\\GB Python\\Corey Schafer_Tutorials\\Libraries\\Pandas\\developer_survey_2019\\survey_results_schema.csv')
# %% codecell
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
# %% codecell
df.head()
# %% codecell
schema_df
# %% codecell
df.shape
# %% codecell
df.columns
# %% codecell
df['Hobbyist']
# %% codecell
# Checking how many values of yes or no there are
df['Hobbyist'].value_counts()
# %% codecell
df.loc[0]  # The whole survay from the person in index 0
# %% codecell
df.loc[0:39, 'Hobbyist']  # The slice is inclusive
# %% codecell
df.loc[0:39, 'Hobbyist':'Employment']
