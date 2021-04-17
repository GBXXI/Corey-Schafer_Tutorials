
# %% markdown
# We can access a file with the open command. It is important to remember to close the file after any operation or set of operations have taken place in order not to surpass our maximum allowed file descriptors in our system.
# %% codecell
file_obj = open('D:\\GBXXI\\Software_Tests\\Test GB Python\\Corey Schafer_Tutorials\\File_objects_manipulation\\Fl_obj.txt', 'r+')
print(file_obj.name)
print(file_obj.mode)
file_obj.close()

# %% markdown
# We can also access a file with a contex manager, which is the preffered practice, since after the complition of the operation or set of operations to the file, the manager closes the file automatically.
# %% codecell
with open('D:\\GBXXI\\Software_Tests\\Test GB Python\\Corey Schafer_Tutorials\\File_objects_manipulation\\Fl_obj.txt', 'r+') as file_obj:
    print(file_obj.name)
    print(file_obj.mode)

# %% markdown
# Reading the contents of a file with the .read, method.
# %% codecell
with open('D:\\GBXXI\\Software_Tests\\Test GB Python\\Corey Schafer_Tutorials\\File_objects_manipulation\\Fl_obj.txt', 'r+') as file_obj:
    file_obj_cont = file_obj.read()
    print(file_obj_cont)

# %% markdown
# ### In case we have a large file, as to not load the entrire file to our memory, we can:

# %% markdown
# Read the contents of a file with the .read, method and pass a character number parameter with a "while-loop"
# %% codecell
with open('D:\\GBXXI\\Software_Tests\\Test GB Python\\Corey Schafer_Tutorials\\File_objects_manipulation\\Fl_obj.txt', 'r+') as file_obj:

    size_to_read = 100
    file_obj_cont = file_obj.read(size_to_read)
    while len(file_obj_cont) > 0:
        print(file_obj_cont)
        file_obj_cont = file_obj.read(size_to_read)

# %% markdown
# Use the .readlines method, which will return a list with all the content of our file.
# %% codecell
with open(r'D:\GBXXI\PROGRAMMING\GB_Python\CoreySchafer_Tutorials\Various\File_objects_manipulation\Fl_obj.txt', 'r+') as file_obj:

    file_obj_cont = file_obj.readlines()
    print(file_obj_cont)

# %% markdown
# Access it with a "for-loop". We pass the parameter 'end = ""' in our print statement so we will not get an empty line after each itteration.
# %% codecell
with open('D:\\GBXXI\\Software_Tests\\Test GB Python\\Corey Schafer_Tutorials\\File_objects_manipulation\\Fl_obj.txt', 'r+') as file_obj:

    for file_line in file_obj:
        file_obj_cont = file_line
        print(file_obj_cont, end='')

# %% markdown
# The .tell method returns the place where our cusror is when accessing a file and the .seek method puts our cursor to a desirable position.
# %% codecell
with open('D:\\GBXXI\\Software_Tests\\Test GB Python\\Corey Schafer_Tutorials\\File_objects_manipulation\\Fl_obj.txt', 'r+') as file_obj:

    size_to_read = 21

    file_obj_cont = file_obj.read(size_to_read)
    print(file_obj_cont, end='')

    # print(file_obj.tell())

    file_obj.seek(0)  # Returning our cusror to the begining of the file.

    file_obj_cont = file_obj.read(size_to_read)
    print(file_obj_cont)

# %% markdown
# Copying one file to another with the .write method.
# %% codecell
with open('D:\\GBXXI\\Software_Tests\\Test GB Python\\Corey Schafer_Tutorials\\File_objects_manipulation\\Fl_obj.txt', 'r+') as rfile:
    with open('Fl_obj_copy.txt', 'w+') as wfile:

        for file_line in rfile:
            wfile.write(file_line)

# %% markdown
# Copying binary files, such as an image, with the .write method.
# %% codecell
with open('Corey Schafer_Tutorials\\File_objects\\panousis-flag.jpg', 'rb+') as rpict:
    with open('Corey Schafer_Tutorials\\File_objects\\panousis-flag_copy.jpg', 'wb+') as wpict:
        for file_line in rpict:
            wpict.write(file_line)

# %% markdown
# Copying binary files, with specific datasize read and a 'while-loop'.
# %% codecell
with open('Corey Schafer_Tutorials\\File_objects\\panousis-flag.jpg', 'rb+') as rpict:
    with open('Corey Schafer_Tutorials\\File_objects\\panousis-flag_copy.jpg', 'wb+') as wpict:
        sizebite = 4096
        r_sizebite = rpict.read(sizebite)

        while len(r_sizebite) > 0:
            wpict.write(r_sizebite)
            r_sizebite = rpict.read(sizebite)  # Moving to the next sizebite, else we would have an endless loop.
