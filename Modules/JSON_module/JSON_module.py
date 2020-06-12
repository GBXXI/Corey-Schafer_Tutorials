""" JavaScript Object Notation"""

import json

people_string = '''
{
 "people":[
    {
    "name": "John Smith",
    "phone": "615-555-7164",
    "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
    "has_license": false
    },
    {
    "name": "Jane Crane",
    "phone": "560-55-5153",
    "emails": null,
    "has_license":true
    }
 ]
}
'''
# Loading a JSON into a python object
data = json.loads(people_string)

print(type(data))
print(type(data['people']))
print(data)

for person in data['people']:
    print(person)

print()
for person in data['people']:
    print(person['name'])

# Dumping a Python object to JSON object

# Creating a new json string without the phone number element

data1 = json.loads(people_string)

for person in data1['people']:
    del person['phone']

new_json_string = json.dumps(data1)
# To make our string more readable we use the indent attribute
new_json_string = json.dumps(data1, indent=2)
# To furthermore make our sting more readable we use the sort attribute
print()
new_json_string = json.dumps(data1, indent=2, sort_keys=True)

print()
print(new_json_string)

################################################################################
# Importing a json file
with open('JSON\\US_states.json') as jnf:
    data = json.load(jnf)

# We can see from our json file that there is a 'states' key. So we use it in
# order to loop over our data.

for state in data['states']:
    print(state['name'], state['abbreviation'])

# We delete the 'area' element from our json file and we create an new file

for state in data['states']:
    del state['area_codes']

# Now we can create new file with our new data
with open('JSON\\n_US_states.json', 'w+') as njsf:
    json.dump(data, njsf, indent=2)
