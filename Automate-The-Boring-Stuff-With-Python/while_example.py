# This is x3830s python files from the book Automate Python The
# Boring Stuff with Python. 

# While true increase the value till it is no longer less than 5
spam = 0
while spam < 5:
    print('Hello World')
    spam = spam + 1


# Condition is constantly true, loops until stated condition is false 'input validation'
name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')

name = ''
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break # causes the loop to jump out and continue on.
print('Thank you!')

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is {}'.format(spam))
