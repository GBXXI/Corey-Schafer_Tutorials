
# %% codecell
from matplotlib import pyplot as plt
# %% codecell
plt.style.use('seaborn-dark')

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 =  [1, 2, 3, 3, 4, 4, 4, 4, 5]
player2 =  [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 =  [1, 1, 1, 2, 2, 2, 3, 3, 3]

labels = ['player1', 'player2', 'player3']
colours = ['cyan', 'magenta', 'blue']

plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colours)

plt.legend(loc='upper left')
plt.title('My first Stack Plot')
plt.tight_layout()
plt.show()

# %% codecell
days = [1, 2, 3, 4, 5, 6, 7, 8, 9]

dev1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
dev2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
dev3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ['Dev1', 'Dev2', 'Dev3']
colours = ['khaki', 'orange', 'cyan']

plt.stackplot(days, dev1, dev2, dev3, labels=labels, colors=colours)

plt.legend(loc='upper right')
plt.title('My first Stack Plot')
plt.tight_layout()
plt.show()
