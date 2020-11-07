# %% [markdown]
# # OS MODULE

# %% [codecell]
import os

# %% [markdown]
# Accessing a modules attributes.
# %% [codecell]
print(dir(os))

# %% [markdown]
# Finding out the directory we are in we use the .getcwd, method.
# %% [codecell]
print(os.getcwd())

# %% [markdown]
# Changing the directory we want to work with the .chdir, method.
# %% [codecell]
os.chdir('D:\\Test GB Python\\Corey Schafer_Tutorials\\OS_module')

# %% [markdown]
# Showing the contents of a directory with the .lisdir, method.
# We can pass a path as a parameter but by default we are presented with the current directory's contents.
# %% [codecell]
print(os.listdir())

# %% [markdown]
# Making a new folder inside our directory, can happen with two methods, .mkdir() which makes the folder we want but cannot make sub-directories and .makedirs() which can create sub-directories if we want.
# %% [codecell]
os.mkdir('os_mkdir_exmpl')
os.makedirs('os_mkdirs_exmpl\\subdirectory_example')

# %% [markdown]
# Deleting directories can also happen with two methods, .rmdir() which can remove a directory which has no sub-directories and .removedirs() which removes a directory and all it's sub-directories.

# %% [codecell]
os.rmdir('os_mkdir_exmpl')
os.removedirs('os_mkdirs_exmpl\\subdirectory_example')

# %% [markdown]
# Renaming a file or a folder with the .rename(), method.
# %% [codecell]
os.rename('rename.txt', 'renameD.txt')

# %% [markdown]
# Looking informations about a file with the .stat(), method.
# From the documentation we know that:<br>
# >
# 1. st_size, stands for the size of the file.<br>
# 2. st_mtime, stand for the last modification time.
# %% [codecell]
os.stat('renameD.txt')

# %% [markdown]
# If we want to print all the directories and the files within a path we use .walk() method. .walk() is a generator that yields a tuple of 3 values. The directory's path, the directories within that path and the files within that path. That is the reason we use this method in a 'for-loop' with 3 variables. By default this method traverses from the top-down.
# %% [codecell]
walk_gen = os.walk(r"D:\GBXXI\PROGRAMMING\GB_Python\CoreySchafer_Tutorials")

for dir_path, dir_names, dir_files in walk_gen:
    print(
        f'''
            Current path: {dir_path}
            Directories: {dir_names}
            Files: {dir_files}
        '''
    )

# %% [markdown]
# Accessing enviroment variables with the .environ, method. If we want a specific path variable we use the .get attribute.
# %% [codecell]
os.environ
os.environ.get('PATH')

# %% [markdown]
# If we want to manipulate a file in a certain path we use the .path module, so as the path we want to use is consistent with our os.
# %% [codecell]
print(dir(os.path))

# %% [markdown]
# The .basename method of the path attribute, shows us the file name of any given path. The path does not have to be a real one or even in the same format as our O.S..
# %% [codecell]
os.path.basename('/temp/greenland/green.jpeg')

# %% [markdown]
# The .dirname method of the path attribute, shows us the directory to any given path. The path does not have to be a real one or even in the same format as our O.S..
# %% [codecell]
os.path.dirname('/temp/greenland/green.jpeg')

# %% [markdown]
# When we want both the directory name and the file name, we use the .split method of the path attribute. The path does not have to be a real one or even in the same format as our O.S..
# %% [codecell]
os.path.split('/temp/greenland/green.jpeg')

# %% [markdown]
# To check if a path existis, we use the .exists method of the path attribute.
# %% [codecell]
print(os.path.exists('/temp/greenland/green.jpeg'))
print(os.path.exists('D:\\NodeJs\\node_modules'))

# %% [markdown]
# To check if a path leads to a directory or a file, we use the .isdir and the .isfile methods of the path attribute.
# %% [codecell]
os.path.isdir('D:\\NodeJs\\node_modules')
os.path.isfile('D:\\NodeJs\\node_modules')

# %% [markdown]
# In order to take the extention of a file, we use the .splitext method of the path attribute. The path does not have to be a real one or even in the same format as our O.S..
# %% [codecell]
print(os.path.splitext('/temp/greenland/green.jpeg'))
print(os.path.splitext('D:\\NodeJs\\node_modules\\npm\\bin\\node-gyp-bin\\node-gyp.cmd'))
