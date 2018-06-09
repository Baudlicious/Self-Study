# This is x3830s python files from the book Automate Python The
# Boring Stuff with Python. 

spam = 42 # global variable

def eggs():
    spam = 42 # local variable

print('Some code here.')
print('Some more code.')

def spam():
    eggs = 99
    bacon()
    print(eggs)
    
def bacon():
    ham = 101
    eggs = 0

spam()
