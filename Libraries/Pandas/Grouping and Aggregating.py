# %% codecell
import pandas as pd
# %% codecell
df = pd.read_csv(r'Corey Schafer_Tutorials\Libraries\Pandas\developer_survey_2019\survey_results_public.csv')
schema_df = pd.read_csv(r'Corey Schafer_Tutorials\Libraries\Pandas\developer_survey_2019\survey_results_schema.csv')
# %% codecell
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
# %% codecell
df.head()

# %% markdown
# Using the 'median' method to our dataframe, <br>
# ignores the NaN(Null) values.
# %% codecell
df['ConvertedComp'].median()

# %% markdown
# Using the 'describe' method, we get a quick overview of our dataframe
# %% codecell
df.describe()

# %% markdown
# Using the 'value_counts' on a series in our dataframe.
# %% codecell
df['Hobbyist'].value_counts()

# %% markdown
# Finding out the most popular social media platform of our dataframe

# %% codecell
# Setting index in order to see the question to a column
schema_df = schema_df.set_index(['Column'])

# %% codecell
schema_df.loc['SocialMedia']

# %% codecell
df['SocialMedia'].value_counts()

# %% markdown
# Presenting our results as a percentage of the total values in our dataframe.

# %% codecell
df['SocialMedia'].value_counts(normalize=True)

# %% markdown
# ### Seeing results with the 'group by' method.<br>

# %% markdown
# Seeing the value_counts for each country
# %% codecell
df['Country'].value_counts().sort_index()

# %% markdown
# Creating a groupby object with the 'Country' parameter of our dataframe.
# %% codecell
grp_country = df.groupby(['Country'])

# %% markdown
# Inputing a specific country whose results we want to present.
# %% codecell
cinpt = input('Select Country: ')

# %% codecell
grp_country['SocialMedia'].value_counts().loc[f'{cinpt}']

# %% markdown
# Seeing the median salary for all countries in USD

# %% codecell
grp_country['ConvertedComp'].median()

# %% markdown
# If we want to see the median for a specific country:

# %% codecell
grp_country['ConvertedComp'].median().loc[f'{cinpt}']

# %% markdown
# Using the 'agg' method to see multiple aggregate functions on our group:

# %% codecell
grp_country['ConvertedComp'].agg(['median', 'mean'])

# %% markdown
# Seeing multiple aggregate functions for a specific country:

# %% codecell
grp_country['ConvertedComp'].agg(['median', 'mean']).loc[f'{cinpt}']

# %% markdown
# Finding all the values that contain 'Python' as a programming language:

# %% codecell
# Since grp_country is a groupby object we use the '.apply' method
# to use a function, in order to get our results.
# In this case the pht of the lamba function is a series, so we can apply
# our '.str' and other series related methods.
grp_country['LanguageWorkedWith'].apply(lambda pht: pht.str.contains('Python').sum())
