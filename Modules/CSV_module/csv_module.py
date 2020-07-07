
# %% codecell
import csv

# %% markdown
# First, we can see how we can read from a csv file.
# NOTE: Check out the File_objects_manipulation in the Various file.
# %% codecell
with open(r'Corey Schafer_Tutorials\Modules\CSV_module\data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)

# %% markdown
# We also can access certain values from our file, by using the indexes of the reader list.
# %% codecell
with open(r'Corey Schafer_Tutorials\Modules\CSV_module\data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line[2])  # email, values

# %% markdown
# We can write a new csv file with a different delimiter.
# %% codecell
with open(r'Corey Schafer_Tutorials\Modules\CSV_module\data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open(r'Corey Schafer_Tutorials\Modules\CSV_module\new_data.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter=';')

        for line in csv_reader:
            csv_writer.writerow(line)

# %% markdown
# Reading a csv file with the .DictRead method, for better viewability.
# %% codecell
with open(r'Corey Schafer_Tutorials\Modules\CSV_module\data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_reader)

    for line in csv_reader:
        print(line)

# %% markdown
# We also can access certain values from our file, by using the keys of the DictReader dictionary.
# %% codecell
with open(r'Corey Schafer_Tutorials\Modules\CSV_module\data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        print(line['email'])

# %% markdown
# When writting with a dictionary writter, we have to provide fieldnames for our file.
# %% codecell
with open(r'Corey Schafer_Tutorials\Modules\CSV_module\data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open(r'Corey Schafer_Tutorials\Modules\CSV_module\new_data.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()  # With this method, our headers, are passed in our new file.

        for line in csv_reader:
            csv_writer.writerow(line)

# %% markdown
# With the .DictWriter method we can also write certain columns in our new file
# This can be achieved by removing the unwanted values from our fieldnames list and also by deleting that key from our line.
# %% codecell
with open(r'Corey Schafer_Tutorials\Modules\CSV_module\data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open(r'Corey Schafer_Tutorials\Modules\CSV_module\new_data.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']  # Passing the values that we want.
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()  # With this method, our headers, are passed in our new file.

        for line in csv_reader:
            del line['email']  # Removing the values tha we do not want in our new file.
            csv_writer.writerow(line)
