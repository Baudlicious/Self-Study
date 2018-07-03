# This is x3830s python files from the book Automate Python The
# Boring Stuff with Python. 

# You may need to escape certain characters within a string
my_string = "That is Alice's cat."
print(my_string)
my_string = 'That is Alice\'s cat.'
print(my_string)

# Or you may want to change spacing
my_string = 'That is Alice\'s \ncat.'
print(my_string)
my_string = 'That is Alice\'s \tcat.'
print(my_string)

# Raw strings can be used to print the literal strings including backslashes 
print(r'That is Carol\'s cat.')

# If we have a multi line text we can use tripple quotes
print(""" Dear Alice,
        Eve's cat has been arrested for catnapping, 
        cat burglary, and extortion. Sincerly, Bob.""")
# if saved as a variable it automatically places the escape characters


# String methods 'upper()' and 'lower()'
spam = 'Hello World!'
print(spam.upper())
print(spam.lower())
print('Hello'.upper())
print('Hello'.lower())

# Boolean for upper and lower with 'islower()' and 'isupper()'
spam = 'Hello World!'
print(spam.islower())
spam = 'hello world!'

# Only consists of letters can be checked with 'isalpha()'
print('hello'.isalpha())
# Contains letters or numbers?
print('hello123'.isalnum())
# Is number?
print('123'.isdecimal())
# Is it a space?
print('    '.isspace())
# Is it in title case?
print('This Is Title Case'.istitle())
# Does it start with ?
print('Hello World'.startswith('Hello'))
print('Hello World'.startswith('H'))
# Does it end with ?
print('Hello World'.endswith('d'))
print('Hello World'.endswith('World'))

# we can join strings and decide the seperator
print(','.join(['cats', 'rats', 'bats']))
print(''.join(['cats', 'rats', 'bats']))
print(' '.join(['cats', 'rats', 'bats']))

# we can also split using the 'split()' method and decide where to split
print('My name is Simon'.split())
print('My name is Simon'.split('m'))

# left and right justify can be achieved with ljust() and rjust() and center()
print('Hello'.ljust(10))
print('Hello'.rjust(10))
print('Hello'.center(10))
print('Hello'.rjust(10, '*'))
print('Hello'.ljust(10, '~'))
print('Hello'.center(20, '='))

# we can remove specific characters with strip(), rstrip(), lstrip()
print('        x       '.strip())
print('        x       '.rstrip())
print('        x       '.lstrip())

# Remove all letters that are mpSa from both sides till you reach something that isnt that 
print('SpamSpamBaconSpamEggsSpamSpam'.strip('mpSa'))

# If we want to replace specific instances of a letter
spam = 'Hello There!'
print(spam)
print(spam.replace('e', 'XYZ'))
