# %% codecell
import pandas as pd
# %% codecell
df = pd.read_csv('D:\\GBXXI\\PROGRAMMING\\GB Python\\Corey Schafer_Tutorials\\Libraries\\Pandas\\developer_survey_2019\\survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('D:\\GBXXI\\PROGRAMMING\\GB Python\\Corey Schafer_Tutorials\\Libraries\\Pandas\\developer_survey_2019\\survey_results_schema.csv', index_col='Column')
# %% codecell
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
# %% codecell
df.head()

# %% markdown
# ### We filter the country column and we write our results to a new csv file.
# First, we create our filter and our new dataframe.
# %% codecell
fltr = df['Country'] == 'Greece'
gr_df = df[fltr]
gr_df.head()

# %% markdown
# Writing our new dataframe to a new csv.
# %% codecell
gr_df.to_csv('D:\\GBXXI\\PROGRAMMING\\GB Python\\Corey Schafer_Tutorials\\Libraries\\Pandas\\To_file\\gr_df.csv')

# %% markdown
# Writing our new dataframe to a tab delimited file. In order to do that, we must assing a seperator.
# %% codecell
gr_df.to_csv('D:\\GBXXI\\PROGRAMMING\\GB Python\\Corey Schafer_Tutorials\\Libraries\\Pandas\\To_file\\gr_df.tsv', sep='\t')

# %% markdown
# Writing our new dataframe to an excel file.
# %% codecell
gr_df.to_excel('D:\\GBXXI\\PROGRAMMING\\GB Python\\Corey Schafer_Tutorials\\Libraries\\Pandas\\To_file\\gr_df.xlsx')

# %% markdown
# Reading from an excel file.
# %% codecell
df_gr = pd.read_excel('D:\\GBXXI\\PROGRAMMING\\GB Python\\Corey Schafer_Tutorials\\Libraries\\Pandas\\To_file\\gr_df.xlsx', index_col='Respondent')
df_gr.head()

# %% markdown
# Writing to a JSON file, with default arguments
# %% codecell
gr_df.to_json('D:\\GBXXI\\PROGRAMMING\\GB Python\\Corey Schafer_Tutorials\\Libraries\\Pandas\\To_file\\gr_df.json')

# %% markdown
# Writing to a list-like JSON file
# %% codecell
gr_df.to_json('D:\\GBXXI\\PROGRAMMING\\GB Python\\Corey Schafer_Tutorials\\Libraries\\Pandas\\To_file\\gr_df_ll.json', orient='records', lines=True)

# %% markdown
# Reading from a JSON file.
# %% codecell
df_gr = pd.read_json('D:\\GBXXI\\PROGRAMMING\\GB Python\\Corey Schafer_Tutorials\\Libraries\\Pandas\\To_file\\gr_df_ll.json', orient='records', lines=True)
df_gr.head()

# %% markdown
# Writting data to a database.
# %% codecell
from sqlalchemy import create_engine
import psycopg2 as ps2
from Apothikarios_postgres_db import psql_connect
# %% codecell
conn = create_engine("postgresql://gbxxi:akr450_YM2171.@localhost:5432/stackoverflow")
# %% codecell
gr_df.to_sql('gr_table', conn, if_exists='replace')

# %% markdown
# Reading data from a database
# %% codecell
sql_gr = pd.read_sql('gr_table', conn, index_col='Respondent')
sql_gr.head()

# %% markdown
# Running a query to our db.
# %% codecell
sql_gr = pd.read_sql_query('SELECT * FROM gr_table LIMIT 3', conn, index_col='Respondent')
sql_gr.head()
