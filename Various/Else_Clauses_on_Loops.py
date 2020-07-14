
# %% [markdown]
# We can consider the "else" statement on loops as a "no-break", statement.<br>
# As is shown in the examples below the else statement is met if a conditional is
# not fullfiled.

# %% [markdown]
# Setup.
# %% [codecell]
list_ = [1, 2, 3, 4, 5]
list_names = ['Marx', 'Luxemburg', 'Ruso']

# %% [markdown]
# Example 1
# %% [codecell]
for element in list_:
    print(element)
    if element == 3:
        print()
        break
else:
    print("Hit the For/Else Statement")

# %% [markdown]
# Example 2
# %% [codecell]
index = 1
while index <= len(list_):
    print(index)
    index += 1
else:
    print("Hit the While/Else Statement")
    print()

# %% [markdown]
# Example 3
# %% [codecell]
def find_index(to_search, target):
    for index, element in enumerate(to_search):
        if element == target:
            break
    else:
        return -1
    return index, element

index_loc = find_index(list_names, 'Luxemburg')
index_loc1 = find_index(list_names, 'Ruso')

print(f'Location of the target "{index_loc[1]}" is index: {index_loc[0]}')
print(f'Location of the target "{index_loc1[1]}" is index: {index_loc1[0]}')
