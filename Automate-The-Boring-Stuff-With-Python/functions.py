# This is x3830s python files from the book Automate Python The
# Boring Stuff with Python. 
def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

hello()
hello()
hello()

def hello2(name):
    print('Hello {}'.format(name))

hello2('Alice')
hello2('Bob')

def plus_one(number):
    return number + 1

new_number = plus_one(5)
print(new_number)

print("Hello", end='')
print('World')


