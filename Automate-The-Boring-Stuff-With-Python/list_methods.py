# This is x3830s python files from the book Automate Python The
# Boring Stuff with Python. 

spam = ['hello', 'hi', 'howdy', 'heyas']

# index method returns the index where the value is found
print(spam.index('hello'))
print(spam.index('heyas'))
print(spam.index('hi'))

# index method will return the index of the first time it encounters the value
spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
print(spam.index('Pooka'))

# Values can be added with the 'append' method
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)

# We can insert new values at specific indexes with 'insert'
spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam)

# Items can also be removed from a list with 'remove' wherever it 
# is in the list and only the first value
spam = ['hello', 'hi', 'howdy', 'heyas','howdy']
spam.remove('howdy')
print(spam)

# We can place a list in order with 'sort'
spam = [ 2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

# we can also sort ASCIIBetically.. all lowercase come first and we can reverse
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort(reverse=True)
print(spam)

# WE CANNOT SORT STRINGS AND INTEGERS IN THE SAME LIST

# If we want true alphabetical sorting
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)

