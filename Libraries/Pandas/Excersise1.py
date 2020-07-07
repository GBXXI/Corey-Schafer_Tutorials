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

# %% markdown
# Creating a groupby object, with 'Country' as a parameter.
# %% codecell
grp_country = df.groupby('Country')

# %% markdown
# Applying a string method in our grouped object to see the total<br>
# users of Python in each country.
# %% codecell
total_pthn = grp_country['LanguageWorkedWith'].apply(lambda pthn: pthn.str.contains('Python').sum())
total_pthn

# %% markdown
# Counting the total interviewees by country.
# %% codecell
total_int = df['Country'].value_counts().sort_index()
total_int

# %% markdown
# Creating a dataframe where we concatenate the above series.<br>
# We set the parameter 'axis' equal to 'Coulumns' because by default it's going<br>
# to concatenate on row
# %% codecell
pthn_df = pd.concat([total_int, total_pthn], axis='columns')
pthn_df

# %% markdown
# Renaming our columns for better presentation.
# %% codecell
pthn_df.rename(columns={'Country':'# Of interviewees', 'LanguageWorkedWith':'# Of Python Users'}, inplace=True)
pthn_df

# %% markdown
# Assigning a new column for our result.
# %% codecell
pthn_df['% Python Users'] = (
(pthn_df['# Of Python Users']/pthn_df['# Of interviewees']) *100
)
pthn_df

# %% markdown
# Sorting based on the largest percentage, in desceding order
# %% codecell
pthn_df.sort_values(by=['% Python Users', 'Country'], ascending=[False, True], inplace=True)
pthn_df

# %% markdown
# Searching for a specific country
# %% codecell
pthn_df.loc['Greece']
