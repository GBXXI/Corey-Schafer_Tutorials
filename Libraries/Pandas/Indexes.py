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
# Setting the Respondent column as an index to our data from the begining
df = pd.read_csv('D:\\Test GB Python\\Corey Schafer_Tutorials\\Pandas\\developer_survey_2019\\survey_results_public.csv', index_col='Respondent')

# %% codecell
# Setting index in order to see the question to a column
schema_df = pd.read_csv('D:\\Test GB Python\\Corey Schafer_Tutorials\\Pandas\\developer_survey_2019\\survey_results_schema.csv', index_col='Column')

# %% codecell
schema_df.loc['MgrIdiot']

# %% codecell
schema_df.loc['MgrIdiot', 'QuestionText']

# %% codecell
# Sorting our indexes alphabetically ASC as a view
schema_df.sort_index()

# %% codecell
# Sorting our indexes alphabetically DESC as a view
schema_df.sort_index(ascending=False)
