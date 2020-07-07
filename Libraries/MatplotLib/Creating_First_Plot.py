
# %% codecell
from matplotlib import pyplot as plt

# %% markdown
# Creating a list for the values of the x axis.
# %% codecell
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# %% markdown
# Creating a list for the values of the y axis.
# %% codecell
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

# %% markdown
# Making our first plot.
# %% codecell
plt.plot(dev_x, dev_y)
plt.show()

# %% markdown
# Giving a title to our entrire plot and our axes.
# %% codecell
plt.plot(dev_x, dev_y)

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Media Salary (USD) by Age')
plt.show()

# %% markdown
# Using data with the same x axis and different y axes. In this example we will use the media salary for all developers and it's subset for python developers.
# %% codecell
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
# %% codecell
plt.plot(dev_x, dev_y)
plt.plot(dev_x, py_dev_y)

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Media Salary (USD) by Age')
plt.show()

# %% markdown
# ### Adding a legend to our data.<br>
# There are two ways to add legend to our data. The first one is to pass a list for the values.
# %% codecell
plt.plot(dev_x, dev_y)
plt.plot(dev_x, py_dev_y)

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Media Salary (USD) by Age')

plt.legend(['All Devs', 'Python Devs'])

plt.show()

# %% markdown
# The second one is passing a label argument to our plot methods.
# %% codecell
plt.plot(dev_x, dev_y, label='All Devs')
plt.plot(dev_x, py_dev_y, label='Python Devs')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Media Salary (USD) by Age')
plt.legend()
plt.show()

# %% markdown
# ### Styling our plots.<br>
# Passing all the styling values at once.
# %% codecell
plt.plot(dev_x, dev_y, 'k--',label='All Devs')
plt.plot(dev_x, py_dev_y, 'b', label='Python Devs')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Media Salary (USD) by Age')
plt.legend()
plt.show()

# %% markdown
# Passing the styling values more verbose.
# %% codecell
plt.plot(dev_x, dev_y, color='k', linestyle='--',label='All Devs')
plt.plot(dev_x, py_dev_y, color='b', label='Python Devs')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Media Salary (USD) by Age')
plt.legend()
plt.show()

# %% markdown
# Adding markers to our styling values.
# %% codecell
plt.plot(dev_x, dev_y, color='k', linestyle='--', marker='.', label='All Devs')
plt.plot(dev_x, py_dev_y, color='b', marker='o', label='Python Devs')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Media Salary (USD) by Age')
plt.legend()
plt.show()

# %% markdown
# Using hex values for our colour. There are hex pallets online.
# %% codecell
plt.plot(dev_x, dev_y, color='#444444', linestyle='--', marker='.', label='All Devs')
plt.plot(dev_x, py_dev_y, color='#5a7d9a', marker='o', label='Python Devs')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Media Salary (USD) by Age')
plt.legend()
plt.show()

# %% markdown
# Automatically adjust our plot parameters
# %% codecell
plt.plot(dev_x, dev_y, color='#444444', linestyle='--', marker='.', label='All Devs')
plt.plot(dev_x, py_dev_y, color='#5a7d9a', marker='o', label='Python Devs')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Media Salary (USD) by Age')
plt.legend()

plt.tight_layout()

plt.show()

# %% markdown
# Adding a grid to our plot
# %% codecell
plt.plot(dev_x, dev_y, color='#444444', linestyle='--', marker='.', label='All Devs')
plt.plot(dev_x, py_dev_y, color='#5a7d9a', marker='o', label='Python Devs')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Media Salary (USD) by Age')
plt.legend()

plt.tight_layout()
plt.grid(True)

plt.show()

# %% markdown
# By using the plt.style.available attribute we can see the available styles for our plot.
# %% codecell
print(plt.style.available)

# %% markdown
# Using a style to our plot.
# %% codecell
plt.style.use('seaborn-dark')

plt.plot(dev_x, dev_y, color='#444444', linestyle='--', marker='.', label='All Devs')
plt.plot(dev_x, py_dev_y, color='#5a7d9a', marker='o', label='Python Devs')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Media Salary (USD) by Age')
plt.legend()

plt.tight_layout()
plt.grid(True)

plt.show()

# %% markdown
# Saving a plot as a .png file
# %% codecell
plt.style.use('seaborn-dark')

plt.plot(dev_x, dev_y, color='#444444', linestyle='--', marker='.', label='All Devs')
plt.plot(dev_x, py_dev_y, color='#5a7d9a', marker='o', label='Python Devs')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Media Salary (USD) by Age')
plt.legend()

plt.tight_layout()
plt.grid(True)

plt.savefig('First_plot.png')

plt.show()
