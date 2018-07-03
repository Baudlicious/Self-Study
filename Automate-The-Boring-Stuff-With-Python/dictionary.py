# This is x3830s python files from the book Automate Python The
# Boring Stuff with Python. 

# dictionary is a collection of many values, and can use many different data types
# they use 'key:value' pairs

my_cat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

print('My cat has {} color fur'.format(my_cat['color']))

spam = {12345: 'Luggage combination', 42: 'The Answer'}

# Dictionaries are unordered, python sees these lists as holding the same content, even undordered.

eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
ham = {'species': 'cat', 'name': 'Zophie', 'age': 8}
print(eggs == ham)

# Keys can be checked with the 'in' and 'not in' operators
print('name' in eggs)
print('name' not in eggs)

# There is three methods that return list like values
# keys, values, items
print(list(eggs.keys()))
print(list(eggs.values()))
print(list(eggs.items()))

# We can use this in a for loop
for k in eggs.keys():
    print(k)

# we can use massassignment
for k, v in eggs.items():
    print(k, v)

# or we can just print the pairs
for i in eggs.items():
    print(i)

# we can use the 'get' method to grab keys in a better manner than an if statement
if 'color' in eggs:
    print(eggs['color'])

# much better solution
print(eggs.get('age', 0))
print(eggs.get('color', ''))

# opposite of the 'get' method is the 'setdefault()', only if it doesnt have a setting in the dictionary
if 'color' not in eggs:
    eggs['color'] = 'black'

eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}

eggs.setdefault('color', 'black')
print(eggs)


message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 1

print(count)

# we can use the library 'pprint' to print out nicer looking dictionaries
import pprint 
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)


# Data structures

cat = {'name': 'Zophie', 'age': 7, 'color': 'gray'}
all_cats = []
all_cats.append({'name': 'Pooka', 'age': 5, 'color': 'black'})
all_cats.append({'name': 'Fat-tail', 'age': 5, 'color': 'gra)y'})
all_cats.append({'name': '???', 'age': 5, 'color': 'orange'})
print(all_cats)

# Tic tac toe example how dictionaries can be used to model real objects
import pprint
the_board = {'top-L': ' ', 'mid-M': 'X', 'low-L': ' ', 'low-R': ' ', 'top-M': ' ', 'mid-R': ' ', 'low-M': ' ', 'top-R': ' ', 'mid-L': ' '}

pprint.pprint(the_board)

the_board['mid-M'] = ' '
pprint.pprint(the_board)

the_board['mid-M'] = 'X'
def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    
print_board(the_board)


