# This is x3830s python files from the book Automate Python The
# Boring Stuff with Python. 

# Strings and lists share a lot of simularities
print(list('Hello'))
name = 'Zophie'
print(name[0])

# However lists are mutable

# Strings are immutable


# We can use slices to change the string
name = 'Zophie a cat'
new_name = name[:7] + 'the' + name[8:12]
print(new_name)

# This example references the same list, so both change. Mutable values store references, not the actual list. 
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
print(cheese)
print(spam)

# example of where this is important. Changes inside the function are seen outside.
def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

# We can make total copies of a list, that creates a brand new list and not just copy the references
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(spam)
print(cheese)

# Lists can span multiple lines of code
spam = ['apples',
        'oranges',
        'bananas',
        'cats']

# The \ can be used to do the same for strings
print('Four score and seven ' + \
        'years ago')


