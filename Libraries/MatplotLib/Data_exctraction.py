# %% markdown
# This module is to exctract data from the stackoverflow's csv, in order to be used in the matplotlib tutorial.
# %% codecell
import pandas as pd
# %% codecell
df = pd.read_csv(r'D:\GBXXI\PROGRAMMING\GB Python\Corey Schafer_Tutorials\Libraries\Pandas\developer_survey_2019\survey_results_public.csv', index_col='Respondent')
# %% codecell
df.shape
# %% codecell
pd.set_option('display.max_columns', 85)
# %% codecell
df.head(3)
# %% codecell
lg_df = df['LanguageWorkedWith']
lg_df
# %% markdown
# Getting our current directory and creating the appropriate path for saving the CSV file
# %% codecell
import os
drcr = os.getcwd()

c_path = os.path.join(drcr, 'Corey Schafer_Tutorials\Libraries\MatplotLib\Exct_Data.csv')
c_path
# %% codecell
lg_df.to_csv(c_path)

# %% codecell
df = pd.read_csv(r'D:\GBXXI\PROGRAMMING\GB Python\Corey Schafer_Tutorials\Libraries\Pandas\developer_survey_2019\survey_results_public.csv')

grp_age = df.groupby(['Age'])
grp_age['CompTotal'].value_counts()
grp_age.describe(include=['object'])
all_devs = grp_age['ConvertedComp'].median()
all_devs
