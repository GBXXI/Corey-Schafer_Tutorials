# %% codecell
import pandas as pd
# %% codecell
df = pd.read_csv('Test GB Python\\Corey Schafer_Tutorials\\Libraries\Pandas\\Etherium_DateTime\\Etherium_1h_datetime.csv')
# %% codecell
df.head()
# %% codecell
df.dtypes
# %% markdown
# Converting the Date column to a datetime object. We explicitly declare the datetime format.
# %% codecell
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p' )
df['Date']

# %% markdown
# Grabbing the day of the date with the .day_name, method.
# %% codecell
df.loc[0, 'Date'].day_name()

# %% markdown
# Converting a string to a date with the .strptime attribute of the .datetime method.
# %% codecell
d_parser = lambda d: pd.datetime.strptime(d, '%Y-%m-%d %I-%p')
d_parser(df['Date'][0])

# %% markdown
# Getting the day name for all the elements of the Date column.
# %% codecell
df['Date'].dt.day_name()

# %% markdown
# Finding the earliest and the latest date from our df with the .min and .max methods. Also showing the Timedelta.
# %% codecell
df['Date'].min()
df['Date'].max()
df['Date'].max() - df['Date'].min()

# %% markdown
# Using filters for our date ranges.
#  Using strings.
# %% codecell
fltr = (df['Date'] >= '2019') & (df['Date'] < '2020')
df.loc[fltr]
# %% markdown
# Using .to_datetime method.
# %% codecell
fltr = (df['Date'] >= pd.to_datetime('2019-01-01')) & (df['Date'] < pd.to_datetime('2020-01-01'))
df.loc[fltr]

# %% markdown
# Using the dates as indexes.
# %% codecell
df.set_index('Date', inplace=True)
df['2019']

# %% markdown
# Using slices.
# %% codecell
df['2020-01':'2020-03']

# %% markdown
# Calculating the average closing value for the above date range.
# %% codecell
df['2020-01':'2020-03']['Close'].mean()

# %% markdown
# Resampling our df in order to get the maximum value of the Highest column.
# %% codecell
daily_highs = df['High'].resample('1D').max()
daily_highs['2020-01-01']

# %% markdown
# Plotting in line.

# %%matplotlib inline
daily_highs.plot()

# %% markdown
# Resampling with multiple aggregation methods on multiple columns.
# %% codecell
df.resample('W').agg({'Close':'mean', 'High':'max', 'Low':'min', 'Volume':'sum'})
