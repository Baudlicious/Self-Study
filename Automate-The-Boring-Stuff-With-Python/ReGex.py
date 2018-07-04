#!/usr/bin/env python
# This is x3830s python files from the book Automate Python The
# Boring Stuff with Python. 

# None ReGex solution for phone numbers

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


# Seperating parts of a ReGex pattern into groups using () to mark where the group begins and ends
import re
phone_re = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_re.search('My Number is 416-666-4242')
print(mo.group(1))
print(mo.group(2))
print(mo.group())

# if we want to find the string with actual () they need to be escaped.
phone_re = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phone_re.search('My Number is (416) 666-4242')
print(mo.group())

# We can match word starting or ending with the same name
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1)) # To find out exactly what was matched
mo = bat_regex.search('Batmotorcycle lost a wheel')

# Matching for a specific number of repetitions
# We can use '?' for this
bat_regex = re.compile(r'Bat(wo)?man')
mo = bat_regex.search('The Adventures of Batman')
print(mo.group())
mo = bat_regex.search('The Adventures of Batwoman')
print(mo.group())

# We can make a search pattern optional
phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phone_regex.search('My phone number is 415-555-1234. Call me tomorrow.')
print(mo.group())

# WE can also test to see if a pattern matches at all  
bat_regex = re.compile(r'Bat(wo)*man')
mo = bat_regex.search('The Adventures of Batman')
print(mo.group())
mo = bat_regex.search('The Adventures of Batwoman')
print(mo.group())
mo = bat_regex.search('The Adventures of Batwowowowowowoman')
print(mo.group())

# We can also set it so that the pattern must appear at least once
bat_regex = re.compile(r'Bat(wo)+man')
mo = bat_regex.search('The Adventures of Batman')
print(bat_regex.search('The Adventures of Batman') == None)
mo = bat_regex.search('The Adventures of Batwoman')
print(mo.group())
mo = bat_regex.search('The Adventures of Batwowowowowowoman')
print(mo.group())

# match a specific number of times
ha_regex = re.compile(r'(Ha) {3}')
print(ha_regex.search('He said "HaHaHa"'))
