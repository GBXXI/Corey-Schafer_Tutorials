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
# Sorting our dataframe by country, as a view<br>
# %% codecell
df.sort_values(by='Country')

# %% markdown
# The statement below gives us the first 50 values of our dataframe and then<br>
# sorts them by country
# %% codecell
df[['Country', 'ConvertedComp']].head(50).sort_values(by='Country')

# %% markdown
# The statement below gives us the first 50 values sorted by country
# %% codecell
df[['Country', 'ConvertedComp']].sort_values(by='Country').head(50)

# %% markdown
# Sorting our values with multiple criteria
# %% codecell
df[['Country', 'ConvertedComp']].sort_values(by=['Country', 'ConvertedComp'], ascending=[True, False]).head(50)

# %% markdown
# Using the 'N largest' method, from a series on one column
# %% codecell
df['ConvertedComp'].nlargest(50)

# %% markdown
# Using the 'N largest' method, from a series to our dataset
# %% codecell
df.nlargest(50, 'ConvertedComp')

# %% markdown
# Using the 'N smallest' method, from a series to our dataset
# %% codecell
df.nsmallest(50, 'ConvertedComp')
