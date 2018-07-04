#!/usr/bin/env python
# This is x3830s python files from the book Automate Python The
# Boring Stuff with Python. 

# None ReGex solution

def is_phone_num(text):
    if len(text) != 12:
        return False # not phone number-sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # no first 3 digits
    if text[7] != '-':
        return False # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False # missing last 4 digits
    return True

print(is_phone_num('415-555-1234'))
print(is_phone_num('Hello'))

message = 'Call me 415-555-1011 tomorrw, or at 415-555-9999'
found_num = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_num(chunk):
        print('Phone number found: {}'.format(chunk))
        found_num = True
if not found_num:
    print('Could not find any phone numbers.')


# ReGex can shorten the effort you need to spend writing a similar code
import re
# since ReGex ahs a lot of back slashes we will use raw strings when setting a ReGex Pattern
phone_re = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Create a match object
mo = phone_re.search(message)

# find first occurence
print(mo.group())
# find all and return a list
print(phone_re.findall(message))
