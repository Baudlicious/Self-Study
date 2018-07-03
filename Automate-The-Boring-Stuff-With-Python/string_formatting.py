# This is x3830s python files from the book Automate Python The
# Boring Stuff with Python. 

name = 'Alice'
place = 'Main Street'
time = '6 pm'
food = 'turnips'

# Below works in python 3.6 and above
# print(f'Hello {name}, you are inivted to a party at {place} at {time}. Please bring {food}')
 print('Hello {}, you are inivted to a party at {} at {}. Please bring {}'.format(name, place, time, food))
