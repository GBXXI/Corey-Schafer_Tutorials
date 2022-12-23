
# %% [codecell]
from datetime import datetime
from calendar import monthrange

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from openpyxl import Workbook, load_workbook

# %% [codecell]
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
report_lines = [7, 10, 11, 14, 15, 22, 23, 33, 37, 49]

# %% [codecell]
df_data = pd.read_excel('26.xlsx')

# %% [codecell]
# df_data.dropna(axis='index', how='all')

# # %% [codecell]
# df_data.replace(np.nan, ' ', inplace=True)
# df_data.drop(columns=df_data.iloc[:, [0, 6, 8, 9]], inplace=True)
# df_data

# # %% [codecell]
# value_date = df_data.iloc[7, 3]
# print(value_date.strftime('%d-%b-%y'))
# print(df_data.iloc[7, 3].strftime('%d-%b-%y'))

# # %% [codecell]
# ge1_hours = df_data.iloc[10, 5]
# ge2_hours = df_data.iloc[11, 5]
# print(ge1_hours)
# print(ge2_hours)

# # %% [codecell]
# ge1_gen = df_data.iloc[14, 5]
# ge2_gen = df_data.iloc[15, 5]
# print(ge1_gen)
# print(ge2_gen)

# %% [codecell]
df_values = df_data.iloc[
    [value for value in report_lines],
    5
]

df_values.iloc[[0]] = df_data.iloc[7, 3]

df_values
