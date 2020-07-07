# %% codecell
import numpy as np
import pandas as pd
# %% codecell
people = {
    'first': [
        'Correy',
        'Jane',
        'John',
        'Chris',
        np.nan,
        None,
        'NA'
    ],

    'last': [
        'Schafer',
        'Doe',
        'Doe',
        'Schafer',
        np.nan,
        np.nan,
        'Missing'
    ],

    'email': [
        'CoreyMSchafer@gmail.com',
        'JaneDoe@email.com',
        'JohnDoe@email.com',
        None,
        np.nan,
        'Anonymous@email.com',
        'NA'
    ],

    'age': [
        '33',
        '55',
        '63',
        '36',
        None,
        None,
        'Missing'
    ]
}
# %% codecell
p_df = pd.DataFrame(people)
p_df

# %% markdown
# **Removing data with the .dropna, method.**
# %% codecell
p_df.dropna()
# %% markdown
# **Using the default arguments of the .dropna method.**<br>
# The axis parameter can have 2 values, index or columns. If index value is passed this means that any row with missing data will not be shown. If the columns value is passed, any column with missing data will not be showed.<br>
# The how parameter is the criteria for dropping a row or a column.
# %% codecell
p_df.dropna(axis='index', how='any')
p_df.dropna(axis='index', how='all')

# %% markdown
# Dropping rows that have a specific column(s) without values.
# %% codecell
p_df.dropna(axis='index', how='all', subset=['email'])

p_df.dropna(axis='index', how='all', subset=['email', 'last'])

# %% markdown
# Dropping custom missing values.<br>
# We can manually replace the values.
# %% codecell
p_df.replace('NA', np.nan, inplace=True)
p_df.replace('Missing', np.nan, inplace=True)
p_df
p_df.isna()

# %% markdown
# Replacing missing or Na values with a custom value via the .fillna, method.
# %% codecell
p_df.fillna(0)

# %% codecell
# **Casting data types.**<br>
# Say we want to change the datatype of our age column, since it's string datatype, we use the float datatype to convert because we have NaN values and those are floats. So in the .astype method we pass float as a parameter.
# %% codecell
p_df['age'] = p_df['age'].astype(float)
p_df.dtypes
p_df['age'].mean()
