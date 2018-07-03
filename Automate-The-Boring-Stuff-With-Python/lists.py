# This is x3830s python files from the book Automate Python The
# Boring Stuff with Python. 

# Lists begin with []
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam) # Prints the list

# First item in list 'cat' this can be gotten by using the index
print(spam[0])

# A list inside a list
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]

# List inside the list
print(spam[0])
# Item within a list within a list 'bat'
print(spam[0][1])
# Item within a list, within a list '40'
print(spam[1][3])


spam = ['cat', 'bat', 'rat', 'elephant']
# We can also move through lists backwards, however it doesn't start at 0.
print(spam[-1])

# List in practice
print('The {} is afraid of the {}.'.format(spam[-1],spam[-3]))

# Slices grab several values from a list, up to but does not include the 
# last value, brand new list from a previous list.
print(spam[1:3])

spam = [10, 20, 30]

# we can assign new values to indexes
spam[1] = 'Hello'

print(spam)
# same can be done with Slices
spam[1:3] = ['CAT', 'DOG', 'MOUSE']
print(spam)

# We can delete values from a list with the del statement
spam = ['cat', 'bat', 'rat', 'elephant']
# 'Unassignment' statement
del spam[2]

# the Len operator can return the total numbers in a list
print(len(spam))

# lists can be added together like string concat.
set1 = [1, 2, 3]
set2 = [4, 5, 6]

print(set1 + set2)

# Lists can also have string replication
print(set1 * 3)

# There is also a list function
hello_list =list('hello')
print(hello_list)

# you can also test to see if a value is in a list with 'in' and 'not in' and produce a boolean value
print(1 in set1)
print(6 in set1)
