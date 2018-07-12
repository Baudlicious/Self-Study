#!/usr/bin/env python
# This is x3830s python files from the book Automate Python The
# Boring Stuff with Python. 

def title(big_title, date):
    print('!!!!' + big_title.upper().center(70) + ' !!!!')
    print(date.upper().center(80))

def sep(title):
    print("-" * 80)
    print('[ + ] ' + title.title())
    print("-" * 80)


def function(func):
    print(">> " + func + ":")

title('RegEx sub() Method', '07/12/18')
import re

sep('Find and replace with sub()')
print("Agent Alice gave the secret documents to Agent Bob.")
names_regex = re.compile(r'Agent \w+')
print("Re = Agent \w+")
print(names_regex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.'))

sep('Find and replace with sub() by grouping of ReGex match')
names_regex = re.compile(r'Agent (\w+)\w*')
print("Re = Agent (\w+)\w*")
print(names_regex.sub(r'Agent \1*****','Agent Alice gave the secret documents to Agent Bob.'))

sep('Using "re.VERBOSE()" with .compile')
function('Allows for white space to be ignored when using .compile(), which can be used \n\tfor documentation of complex RegEx')
complex_phone = re.compile(r'''
        (\d\d\d-) | # Area code without parens, with dash
        (\(\d\d\d\) ) # -or- area code with parens and no dash
        \d\d\d # first 3 digits
        - # Second Dash
        \d\d\d\d #Last 4 digits
        \sx\d{2,4} # extension, like x1234''', re.VERBOSE)
print('415-212-5555')
print(complex_phone.search('415-212-5555'))

sep('Bitwise operators for the re.compile()')
function('re.IGNORECASE | re.DOTALL | re.VERBOSE')
complex_phone = re.compile(r'''
        (\d\d\d-) | # Area code without parens, with dash
        (\(\d\d\d\) ) # -or- area code with parens and no dash
        \d\d\d # first 3 digits
        - # Second Dash
        \d\d\d\d #Last 4 digits
        \sx\d{2,4} # extension, like x1234''', re.IGNORECASE | re.DOTALL | re.VERBOSE)

print('415-212-5555')
print(complex_phone.search('415-212-5555'))
