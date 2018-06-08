# This is x3830s python files from the book Automate Python The
# Boring Stuff with Python. 

# if example
name = 'Alice'
if name == 'Alice':
    print('Hi Alice')
print('Done')

# should not print anything other than 'Done'
name = 'Bob'
if name == 'Alice':
    print('Hi Alice')
print('Done')

# Adding else elements to deal with conditional statements.
password = 'swordfish'
if password == 'swordfish':
    print('Access granted. ')
else:
    print("Wrong Password!")


name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, ALice is not an undead, immortal vampire')
elif age > 100: 
    print('You are not Alice, grannie.')


# Truthy and Falsey values
print('Enter a name')
name = input()
if name:
    print('Thank you for entering a name.')
else:
    print('You did not enter a name.')

print('Enter a name')
name = input()
if name != '': # Better way of doing the above statement
    print('Thank you for entering a name.')
else:
    print('You did not enter a name.')
