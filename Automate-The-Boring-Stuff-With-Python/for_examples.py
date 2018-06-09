# This is x3830s python files from the book Automate Python The
# Boring Stuff with Python. 

print('My name is')
for i in range(5):
    print('Jimmy Five Times {}'.format(i))

total = 0
for num in range(101):
    total = total + num

print(total)

# This one loops backwards and determines the 'step'
print('My name is')
for i in range(5, -1, -1):
    print('Jimmy Five Times {}'.format(i))
