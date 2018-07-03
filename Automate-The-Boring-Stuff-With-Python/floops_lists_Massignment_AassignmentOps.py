# This is x3830s python files from the book Automate Python The
# Boring Stuff with Python. 

# These two are essentially the same
for i in range(0,4):
    print(i)
    
for i in [0, 1, 2, 3]:
    print(i)

# Allows for the creation of the values in a list
spam = list(range(4))
print(spam)

# Start at 0, go up to but not including 100, go up by 2s
spam = list(range(0, 100, 2))
print(spam)

# We can interate through the items in a list
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index {} in supplies is {}'.format(str(i), supplies[i]))

# Multiple assignment allows for the assignment of variables on the same line 
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
print('The size of the cat is {}, the color of the cat is {}, the disposition of the cat is {}'.format(size, color, disposition))
# can also be used this way for swap operations
size, color, disposition = 'skinny', 'black', 'quiet'
a = 'AAA'
b = 'BBB'
print(a, b)
a, b = b, a
print(a, b)

# Augmented assignment operators can be used as shortcuts
spam = 42
spam += 1
print(spam)

