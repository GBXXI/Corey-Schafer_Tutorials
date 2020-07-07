
import random
import csv

with open(r'Random_Mock_data\Names.txt') as names:

    csv_reader = csv.reader(names, delimiter=',')

    fullname = ["".join(line).split(' ') for line in csv_reader]
# fullname = [namelist[i].split(' ') for i in range(len(namelist))]

firstname = [name[0] for name in fullname]
lastname = [surname[1] for surname in fullname]

repetitions = 5

for i in range(repetitions):
    name = random.choice(fullname)
    print(' '.join(name))
