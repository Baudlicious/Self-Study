# This is x3830s python files from the book Automate Python The
# Boring Stuff with Python. 

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 1

print(count)
