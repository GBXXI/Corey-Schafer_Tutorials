
# %% markdown
# This is our previous plot.
# %% codecell
from matplotlib import pyplot as plt
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(dev_x, dev_y, color='#444444', linestyle='--', marker='.', label='All Devs')
plt.plot(dev_x, py_dev_y, color='#5a7d9a', marker='o', label='Python Devs')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Media Salary (USD) by Age')
plt.legend()
plt.tight_layout()
plt.show()

# %% markdown
# Using a bar chart for our representation.
# %% codecell
plt.bar(dev_x, dev_y, color='#444444', linestyle='--', label='All Devs')
plt.bar(dev_x, py_dev_y, color='#5a7d9a', label='Python Devs')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Media Salary (USD) by Age')
plt.legend()
plt.tight_layout()
plt.show()

# %% markdown
# Having mixed representation of our data
# %% codecell
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
###################################Line Plot####################################
plt.plot(dev_x, py_dev_y, color='#008fd5', label='Python Devs')
plt.plot(dev_x, js_dev_y, color='#e5ae38', label='JavaScript Devs')
####################################Bar Plot####################################
plt.bar(dev_x, dev_y, color='#444444', label='All Devs')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Media Salary (USD) by Age')
plt.legend()
plt.tight_layout()
plt.show()

# %% codecell
# Presenting data side by side as bar chart. It is possible by offsetting the x data axis. To do so, we must import NumPy,<br>
# Create an np.arange of our x axis and use this instead<br>
# Specify a width for each bar.<br>
# Add or subtract the width value to move the bars.
# %% codecell
import numpy as np
x_indexes = np.arange(len(dev_x))
width = 0.25

plt.bar(x_indexes, py_dev_y, width=width, color='#008fd5', label='Python Devs')
plt.bar(x_indexes-width, dev_y, width=width, color='#444444', label='All Devs')
plt.bar(x_indexes+width, js_dev_y, width=width, color='#e5ae38', label='JavaScript Devs')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Media Salary (USD) by Age')
plt.legend()
plt.tight_layout()
plt.show()

# %% markdown
# In order to make the above's example x axis to represent out data correctly, we use the .xticks method.
# %% codecell
x_indexes = np.arange(len(dev_x))
width = 0.25

plt.bar(x_indexes, py_dev_y, width=width, color='#008fd5', label='Python Devs')
plt.bar(x_indexes-width, dev_y, width=width, color='#444444', label='All Devs')
plt.bar(x_indexes+width, js_dev_y, width=width, color='#e5ae38', label='JavaScript Devs')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Media Salary (USD) by Age')
plt.legend()
plt.tight_layout()

plt.xticks(ticks=x_indexes, labels=dev_x)

plt.show()

# %% markdown
# ### Plotting data from a CSV file with the CSV module.<br>
# We will use the assistance of the Counter module.
# %% codecell
import csv
from collections import Counter

with open(r'Corey Schafer_Tutorials\Libraries\MatplotLib\Exct_Data.csv') as c_file:
    c_reader = csv.DictReader(c_file)

    lang_counter = Counter()

    for row in c_reader:
        lang_counter.update(row['LanguageWorkedWith'].split(';'))
# %% markdown
# Filtering the most common responses from our counter and creating 2 lists with the elements of the returned tuples.
# %% codecell
lang_comm = lang_counter.most_common(15)
lang_type = [i[0] for i in lang_comm]
lang_pop = [i[1] for i in lang_comm]

# %% markdown
# Having the above values we now can plot our vertical bar chart.
# %% codecell
plt.barh(lang_type, lang_pop)

plt.title('Most Popular Programming Languages')
plt.xlabel('Popularity')
plt.tight_layout()
plt.show()
# %% markdown
# Since we want the most popular languages on top, we reverse our axes.
# %% codecell
lang_type.reverse()
lang_pop.reverse()

plt.barh(lang_type, lang_pop)

plt.title('Most Popular Programming Languages')
plt.xlabel('Popularity')
plt.tight_layout()
plt.show()

# %% markdown
# ### Plotting data from a CSV using pandas module.
# %% codecell
import pandas as pd
from collections import Counter

data = pd.read_csv(r'Corey Schafer_Tutorials\Libraries\MatplotLib\Exct_Data.csv')

resp_id = data['Respondent']
resp_lang = data['LanguageWorkedWith']
lang_counter = Counter()

for response in resp_lang:
    lang_counter.update(response['LanguageWorkedWith'].split(';'))
# %% codecell
lang_comm = lang_counter.most_common(15)
lang_type = [i[0] for i in lang_comm]
lang_pop = [i[1] for i in lang_comm]

# %% codecell
lang_type.reverse()
lang_pop.reverse()

plt.barh(lang_type, lang_pop)

plt.title('Most Popular Programming Languages')
plt.xlabel('Popularity')
plt.tight_layout()
plt.show()
