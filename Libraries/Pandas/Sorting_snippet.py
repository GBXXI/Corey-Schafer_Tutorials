# %% codecell
import pandas as pd

# %% codecell
people = {"first": ["Corey", "Jane", "John"],
         "last": ["Schafer", "Doe", "Doe"],
         "email": ["CoreySchafer@gmail.com", "JaneDoe@bogusmail.org", "JohnDoe@company.com"]}

# %% codecell
p_df = pd.DataFrame(people)

# %% codecell
p_df

# %% markdown
# Sorting our dataframe by column values, ASC, as a view.<br>
# %% codecell
p_df.sort_values(by='last')

# %% markdown
# Sorting our dataframe by column values, DESC, as a view.<br>
# %% codecell
p_df.sort_values(by='last', ascending=False)

# %% markdown
# Sorting our dataframe by column values, ASC, as a view.<br>
# Shorting values with multiple criteria
# %% codecell
p_df.sort_values(by=['last', 'first'])

# %% markdown
# Sorting our dataframe by column values, DESC, as a view.<br>
# Shorting values with multiple criteria
# %% codecell
p_df.sort_values(by=['last', 'first'], ascending=False)

# %% markdown
# Sorting our dataframe by column values, as a view.<br>
# Shorting values with multiple criteria
# %% codecell
p_df.sort_values(by=['last', 'first'], ascending=[False, True])
