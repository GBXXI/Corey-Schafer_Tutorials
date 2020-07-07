
import re

text_to_search = """ abcdefghijklmnopqrstuvwxyz
                     ABCDEFGHIJKLMNOPQRSTUVWXYZ
                     1234567890
Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

https://www.google.com
http://gbxxi.edu.gr
https://youtube.com
http://www.nasa.gov
"""

sentence = 'Start a sentence and then bring it to an end'

###################################EXAMPLE_1####################################
print('EXAMPLE_1')
pattern = re.compile(r'abc')  # r stand for raw string.
                              # The statement is case-sensitive

matches = pattern.finditer(text_to_search) # Returns an iterrator with our match

# Printing all our matches
for match in matches:
    print(match) # Output: <re.Match object; span=(1, 4), match='abc'>
                 # Where span is the begining and end index of out match
                 # match = , is the string we have for comparison.

pattern = re.compile(r'coreyms\.com')  # r stand for raw string.
                                       # The statement is case-sensitive
                                       # The '.' as a meta-character must be
                                       # ecaped

matches = pattern.finditer(text_to_search) # Returns an iterrator with our match

# Printing all our matches
for match in matches:
    print(match) # Output:
                 # <re.Match object; span=(175, 186), match='coreyms.com'>
                 # Where span is the begining and end index of out match
                 # match = , is the string we have for comparison.

###################################EXAMPLE_2####################################
print('EXAMPLE_2')

pattern = re.compile(r'\bHa')  # r stand for raw string.
                              # The statement is case-sensitive
                              # The '\b' Word Boundry BEFORE

matches = pattern.finditer(text_to_search) # Returns an iterrator with our match

# Printing all our matches
for match in matches:
    print(match) # Output:
                 # <re.Match object; span=(108, 110), match='Ha'>
                 # <re.Match object; span=(111, 113), match='Ha'>
                 # Where span is the begining and end index of out match
                 # match = , is the string we have for comparison.
                 # Returns the first 'Ha' and the begining of the 'HaHa'

###################################EXAMPLE_3####################################
print('EXAMPLE_3')

pattern = re.compile(r'\BHa')  # r stand for raw string.
                               # The statement is case-sensitive
                               # The '\B' do not have Word Boundry BEFORE

matches = pattern.finditer(text_to_search) # Returns an iterrator with our match

 # Printing all our matches
for match in matches:
    print(match) # Output:
                 # <re.Match object; span=(113, 115), match='Ha'>
                 # Where span is the begining and end index of out match
                 # match = , is the string we have for comparison.
                 # Returns the second 'Ha' of the word 'HaHa'

###################################EXAMPLE_4####################################
print('EXAMPLE_4')

pattern = re.compile(r'^Start')  # r stand for raw string.
                               # The statement is case-sensitive
                               # The '^' search for string literal
                               # at the begining of the string

matches = pattern.finditer(sentence) # Returns an iterrator with our match

 # Printing all our matches
for match in matches:
    print(match) # Output:
                 # <re.Match object; span=(0, 5), match='Start'>
                 # Where span is the begining and end index of out match
                 # match = , is the string we have for comparison.

###################################EXAMPLE_5####################################
print('EXAMPLE_5')

pattern = re.compile(r'end$')  # r stand for raw string.
                               # The statement is case-sensitive
                               # The '$' search for string literal
                               # at the end of the string

matches = pattern.finditer(sentence) # Returns an iterrator with our match

 # Printing all our matches
for match in matches:
    print(match) # Output:
                 # <re.Match object; span=(41, 44), match='end'>
                 # Where span is the begining and end index of out match
                 # match = , is the string we have for comparison.

###################################EXAMPLE_6####################################
print('EXAMPLE_6')

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')  # r stand for raw string.
                               # The statement is case-sensitive
                               # The pattern we want to search
                               # The '.' matches any character


matches = pattern.finditer(text_to_search) # Returns an iterrator with our match

 # Printing all our matches
for match in matches:
    print(match) # Output:
                 # <re.Match object; span=(196, 208), match='321-555-4321'>
                 # <re.Match object; span=(209, 221), match='123.555.1234'>
                 # <re.Match object; span=(222, 234), match='123*555*1234'>
                 # <re.Match object; span=(235, 247), match='800-555-1234'>
                 # <re.Match object; span=(248, 260), match='900-555-1234'>
                 # Where span is the begining and end index of out match
                 # match = , is the string we have for comparison.

###################################EXAMPLE_7####################################
print('EXAMPLE_7')

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')  # r stand for raw string.
                               # The statement is case-sensitive
                               # The pattern we want to search
                               # The '.' matches any character

# Creating a contex manager to parse through our Data.txt
with open('Data.txt', 'r', errors='ignore') as dat:
    contents = dat.read()
    matches = pattern.finditer(contents) # Returns an iterrator
                                               # with our match
    # Printing all our matches
    for match in matches:
        print(match) # Output:
                    # <re.Match object; span=(12, 24), match='615-555-7164'>
                    # <re.Match object; span=(102, 114), match='800-555-5669'>
                    # <re.Match object; span=(191, 203), match='560-555-5153'>
                    # <re.Match object; span=(281, 293), match='900-555-9340'>
                    # <re.Match object; span=(378, 390), match='714-555-7405'>
                    # ....
                    # <re.Match object; span=(8569, 8581), match='178-555-4899'>
                    # <re.Match object; span=(8653, 8665), match='952-555-3089'>
                    # <re.Match object; span=(8746, 8758), match='900-555-6426'>

###################################EXAMPLE_8####################################
print('EXAMPLE_8')

pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')  # r stand for raw string.
                               # The statement is case-sensitive
                               # The pattern we want to search
                               # The '[]' is a character set that only matches
                               # ONLY ONE of the included characters

# Creating a contex manager to parse through our Data.txt
with open('Data.txt', 'r', errors='ignore') as dat:
    contents = dat.read()
    matches = pattern.finditer(contents) # Returns an iterrator
                                               # with our match
    # Printing all our matches
    for match in matches:
        print(match) # Output:
                    # <re.Match object; span=(12, 24), match='615-555-7164'>
                    # <re.Match object; span=(102, 114), match='800-555-5669'>
                    # <re.Match object; span=(191, 203), match='560-555-5153'>
                    # <re.Match object; span=(281, 293), match='900-555-9340'>
                    # <re.Match object; span=(378, 390), match='714-555-7405'>
                    # ....
                    # <re.Match object; span=(8569, 8581), match='178-555-4899'>
                    # <re.Match object; span=(8653, 8665), match='952-555-3089'>
                    # <re.Match object; span=(8746, 8758), match='900-555-6426'>

###################################EXAMPLE_9####################################
print('EXAMPLE_9')

pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')  # r stand for raw string.
                               # The statement is case-sensitive
                               # The pattern we want to search
                               # The '[]' is a character set that only matches
                               # ONLY ONE of the included characters.
                               # So in order to get only 800 or 900 telephone
                               # numbers we use '00' literals

# Creating a contex manager to parse through our Data.txt
with open('Data.txt', 'r', errors='ignore') as dat:
    contents = dat.read()
    matches = pattern.finditer(contents) # Returns an iterrator
                                               # with our match
    # Printing all our matches
    for match in matches:
        print(match) # Output:
                    # <re.Match object; span=(102, 114), match='800-555-5669'>
                    # <re.Match object; span=(281, 293), match='900-555-9340'>
                    # <re.Match object; span=(467, 479), match='800-555-6771'>
                    # <re.Match object; span=(1092, 1104), match='900-555-3205'>
                    # <re.Match object; span=(1441, 1453), match='800-555-6089'>
                    # <re.Match object; span=(1792, 1804), match='800-555-7100'>
                    # <re.Match object; span=(2053, 2065), match='900-555-5118'>
                    # <re.Match object; span=(2828, 2840), match='900-555-5428'>
                    # <re.Match object; span=(3287, 3299), match='800-555-8810'>
                    # <re.Match object; span=(3974, 3986), match='900-555-9598'>
                    # <re.Match object; span=(4948, 4960), match='800-555-2420'>
                    # <re.Match object; span=(5569, 5581), match='900-555-3567'>
                    # <re.Match object; span=(6192, 6204), match='800-555-3216'>
                    # <re.Match object; span=(6893, 6905), match='900-555-7755'>
                    # <re.Match object; span=(7868, 7880), match='800-555-1372'>
                    # <re.Match object; span=(8746, 8758), match='900-555-6426'>

###################################EXAMPLE_10###################################
print('EXAMPLE_10')

pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d[1-5]')# r stand for raw string.
                               # The statement is case-sensitive
                               # The pattern we want to search
                               # The '[]' is a character set that only matches
                               # ONLY ONE of the included characters.
                               # So in order to get only 800 or 900 telephone
                               # numbers we use '00' literals
                               # The '-' inside the '[1-5]' now acts as a range
                               # so we get only numbers wich end in 1 trough 5

# Creating a contex manager to parse through our Data.txt
with open('Data.txt', 'r', errors='ignore') as dat:
    contents = dat.read()
    matches = pattern.finditer(contents) # Returns an iterrator
                                               # with our match
    # Printing all our matches
    for match in matches:
        print(match) # Output:
                    # <re.Match object; span=(467, 479), match='800-555-6771'>
                    # <re.Match object; span=(1092, 1104), match='900-555-3205'>
                    # <re.Match object; span=(6893, 6905), match='900-555-7755'>
                    # <re.Match object; span=(7868, 7880), match='800-555-1372'>
###################################EXAMPLE_11###################################
print('EXAMPLE_11')

pattern = re.compile(r'[^89]00[-.]\d\d\d[-.]\d\d\d[1-5]')# r stand for raw string.
                               # The statement is case-sensitive
                               # The pattern we want to search
                               # The '[]' is a character set that only matches
                               # ONLY ONE of the included characters.
                               # The '^' inside '[]' matches everything that is
                               # NOT 8 or 9
                               # The '-' inside the '[1-5]' now acts as a range
                               # so we get only numbers wich end in 1 trough 5

# Creating a contex manager to parse through our Data.txt
with open('Data.txt', 'r', errors='ignore') as dat:
    contents = dat.read()
    matches = pattern.finditer(contents) # Returns an iterrator
                                               # with our match
    # Printing all our matches
    for match in matches:
        print(match) # Output:
                    # <re.Match object; span=(7957, 7969), match='300-555-7821'>

###################################EXAMPLE_12###################################
print('EXAMPLE_12')

pattern = re.compile(r'[^89]00[-.]\d{3}[-.]\d{3}[1-5]')# r stand for raw string.
                               # The statement is case-sensitive
                               # The pattern we want to search
                               # The '[]' is a character set that only matches
                               # ONLY ONE of the included characters.
                               # The '^' inside '[]' matches everything that is
                               # NOT 8 or 9
                               # The '-' inside the '[1-5]' now acts as a range
                               # so we get only numbers wich end in 1 trough 5
                               # The '{}' provides us with the number of
                               # characters that we want to search

# Creating a contex manager to parse through our Data.txt
with open('Data.txt', 'r', errors='ignore') as dat:
    contents = dat.read()
    matches = pattern.finditer(contents) # Returns an iterrator
                                               # with our match
    # Printing all our matches
    for match in matches:
        print(match) # Output:
                    # <re.Match object; span=(7957, 7969), match='300-555-7821'>

###################################EXAMPLE_13###################################
print('EXAMPLE_13')

pattern = re.compile(r'Mr\.?\s[A-Z]\w*') # r stand for raw string.
                               # The statement is case-sensitive
                               # The pattern we want to search
                               # The '?' provides the option for the '.' to be
                               # or not to be in our pattern
                               # After the first search there is a space
                               #  following '\s'
                               # After that we search for capital letters in the
                               # range A throug Z, with '[A-Z]'
                               # And finally we search for none or more letters
                               # after our capital letter with the quantifier '*'

matches = pattern.finditer(text_to_search) # Returns an iterrator with our match

 # Printing all our matches
for match in matches:
    print(match) # Output:
                 # <re.Match object; span=(262, 273), match='Mr. Schafer'>
                 # <re.Match object; span=(274, 282), match='Mr Smith'>
                 # <re.Match object; span=(306, 311), match='Mr. T'>

###################################EXAMPLE_14###################################
print('EXAMPLE_14')

pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*') # r stand for raw string.
                               # The statement is case-sensitive
                               # The pattern we want to search
                               # The '(r|s|rs)' provides us with the option of a
                               # literal 'r' or 's' or 'rs' after the 'M'
                               # The '?' provides the option for the '.' to be
                               # or not to be in our pattern
                               # After the first search there is a space
                               #  following '\s'
                               # After that we search for capital letters in the
                               # range A throug Z, with '[A-Z]'
                               # And finally we search for none or more letters
                               # after our capital letter with the quantifier '*'

matches = pattern.finditer(text_to_search) # Returns an iterrator with our match

 # Printing all our matches
for match in matches:
    print(match) # Output:
                 # <re.Match object; span=(262, 273), match='Mr. Schafer'>
                 # <re.Match object; span=(274, 282), match='Mr Smith'>
                 # <re.Match object; span=(283, 291), match='Ms Davis'>
                 # <re.Match object; span=(292, 305), match='Mrs. Robinson'>
                 # <re.Match object; span=(306, 311), match='Mr. T'>

###################################EXAMPLE_15###################################
print('EXAMPLE_15')

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)') # r stand for raw string.
                               # The statement is case-sensitive
                               # The pattern we want to search
                               # The 's' in 'https' is optional since is
                               # followed by the '?'.
                               # The first group (www\.) is optional since is
                               # followed by the '?'.
                               # The second group '(\w+)' is the domain name
                               # The third group '(\.\w+)' is the top level
                               # domain

matches = pattern.finditer(text_to_search) # Returns an iterrator with our match

 # Printing all our matches
for match in matches:
    print(match.group(0)) # Output:
                          # https://www.google.com
                          # http://gbxxi.edu
                          # https://youtube.com
                          # http://www.nasa.gov

matches = pattern.finditer(text_to_search) # Returns an iterrator with our match
for match in matches:
    print(match.group(1)) # Output:
                          # www.
                          # None
                          # None
                          # www.

matches = pattern.finditer(text_to_search) # Returns an iterrator with our match
for match in matches:
    print(match.group(2)) # Output:
                          # google
                          # gbxxi
                          # youtube
                          # nasa

matches = pattern.finditer(text_to_search) # Returns an iterrator with our match
for match in matches:
    print(match.group(3)) # Output:
                          # .com
                          # .edu
                          # .com
                          # .gov

# Special care to be taken because this RegEx does not support 2 Top level
# domains, as seen in the example: http://gbxxi.edu.gr

###################################EXAMPLE_16###################################
print('EXAMPLE_16')

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)') # r stand for raw string.
                               # The statement is case-sensitive
                               # The pattern we want to search
                               # The 's' in 'https' is optional since is
                               # followed by the '?'.
                               # The first group (www\.) is optional since is
                               # followed by the '?'.
                               # The second group '(\w+)' is the domain name
                               # The third group '(\.\w+)' is the top level
                               # domain

matches = pattern.finditer(text_to_search) # Returns an iterrator with our match

# Using substitution to get the domain and the top level domain only
# we use the groups number, from our RegEx as follows '(r'\2\3')'
subbed_urls = pattern.sub(r'\2\3', text_to_search)

print(subbed_urls) # Output:
                   # abcdefghijklmnopqrstuvwxyz
                   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
                   # 1234567890
                   # Ha HaHa
                   #
                   # MetaCharacters (Need to be escaped):
                   # . ^ $ * + ? { } [ ] \ | ( )
                   #
                   # coreyms.com
                   #
                   # 321-555-4321
                   # 123.555.1234
                   # 123*555*1234
                   # 800-555-1234
                   # 900-555-1234
                   #
                   # Mr. Schafer
                   # Mr Smith
                   # Ms Davis
                   # Mrs. Robinson
                   # Mr. T
                   #
                   # google.com   # Values that got substituted by our RegEx
                   # gbxxi.edu.gr # Values that got substituted by our RegEx
                   # youtube.com  # Values that got substituted by our RegEx
                   # nasa.gov     # Values that got substituted by our RegEx

###################################EXAMPLE_17###################################
print('EXAMPLE_17')

pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*') # r stand for raw string.
                               # The statement is case-sensitive
                               # The pattern we want to search
                               # The '(r|s|rs)' provides us with the option of a
                               # literal 'r' or 's' or 'rs' after the 'M'
                               # The '?' provides the option for the '.' to be
                               # or not to be in our pattern
                               # After the first search there is a space
                               #  following '\s'
                               # After that we search for capital letters in the
                               # range A throug Z, with '[A-Z]'
                               # And finally we search for none or more letters
                               # after our capital letter with the quantifier '*'

matches = pattern.findall(text_to_search) # Returns a list of stings with all
                                          # our matches.
                                          # It is only going to match the group

 # Printing all our matches
for match in matches:
    print(match) # Output:
                 # r
                 # r
                 # s
                 # rs
                 # r

###################################EXAMPLE_18###################################
print('EXAMPLE_18')
# Equivalent with example_4

pattern = re.compile(r'Start')  # r stand for raw string.
                                # The statement is case-sensitive

matches = pattern.match(sentence) # Returns the first match
                                  # At the begining of the string.

 # Printing all our match
print(matches) # Output:
               # <re.Match object; span=(0, 5), match='Start'>
               # Where span is the begining and end index of out match
               # match = , is the string we have for comparison.

###################################EXAMPLE_19###################################
print('EXAMPLE_19')

pattern = re.compile(r'sentence')  # r stand for raw string.
                                   # The statement is case-sensitive

matches = pattern.search(sentence) # Returns the first match
                                   # searching the entire string.

 # Printing all our match
print(matches) # Output:
               # <re.Match object; span=(8, 16), match='sentence'>
               # Where span is the begining and end index of out match
               # match = , is the string we have for comparison.

###################################EXAMPLE_20###################################
print('EXAMPLE_20')

pattern = re.compile(r'sentence', re.I)  # r stand for raw string.
                                   # The statement is case-insensitive
                                   # The 're.I' or 're.IGNORE' is a flag
                                   # that allow for a case-insensitive search

matches = pattern.search(sentence) # Returns the first match
                                   # searching the entire string.

 # Printing all our match
print(matches) # Output:
               # <re.Match object; span=(8, 16), match='sentence'>
               # Where span is the begining and end index of out match
               # match = , is the string we have for comparison.
