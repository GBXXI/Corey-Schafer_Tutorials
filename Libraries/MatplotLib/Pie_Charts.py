
# %% markdown
# Creating a basic pie chart.
# %% codecell
from matplotlib import pyplot as plt
# %% codecell
plt.style.use('seaborn-dark')

slices = [79,21]
labels = ['Maj', 'Minor']
plt.pie(slices, labels=labels, wedgeprops={'edgecolor':'black'})

plt.title('My first pie-chart')
plt.tight_layout()
plt.show()

# %% codecell
plt.style.use('seaborn-dark')

slices = [79, 21, 23, 77, 45, 55]
labels = ['Maj', 'Minor', 'minor', 'maj', 'min', 'avg']
colours = ['cyan', 'red', 'green', 'yellow', 'magenta', 'purple']
plt.pie(slices, labels=labels, colors=colours, wedgeprops={'edgecolor':'black'})

plt.title('My first pie-chart')
plt.tight_layout()
plt.show()

# %% markdown
# Using the explode parameter to single-out slices.
# %% codecell
plt.style.use('seaborn-dark')

slices = [59219, 55466, 47544, 36433, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explotion = [0, 0, 0, 0.3, 0]
plt.pie(slices, labels=labels, explode=explotion, colors=colours, wedgeprops={'edgecolor':'black'})

plt.title('My first pie-chart')
plt.tight_layout()
plt.show()

# %% markdown
# Adding shadows to our chart and changing the angle.
# %% codecell
plt.style.use('seaborn-dark')

slices = [59219, 55466, 47544, 36433, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explotion = [0, 0, 0, 0.3, 0]
plt.pie(slices, labels=labels, explode=explotion, shadow=True, startangle=45, colors=colours, wedgeprops={'edgecolor':'black'})

plt.title('My first pie-chart')
plt.tight_layout()
plt.show()

# %% markdown
# Adding percentage to our chart.
# %% codecell
plt.style.use('seaborn-dark')

slices = [59219, 55466, 47544, 36433, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explotion = [0, 0, 0, 0.3, 0]
plt.pie(slices, labels=labels, explode=explotion, shadow=True, startangle=45, autopct='%1.1f%%', colors=colours, wedgeprops={'edgecolor':'black'})

plt.title('My first pie-chart')
plt.tight_layout()
plt.show()
