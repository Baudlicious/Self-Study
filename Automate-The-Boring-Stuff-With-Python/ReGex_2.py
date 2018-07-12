#!/usr/bin/env python
# This is x3830s python files from the book Automate Python The
# Boring Stuff with Python. 
import re
def sep():
    print('-' * 81)

print("Dot-Star and Caret Symbols")
print("Starts with the word 'Hello'")
begins_w_hello = re.compile(r'^Hello')
print(begins_w_hello.search('Hello there!'))
print(begins_w_hello.search('He said "Hello!"'))
sep()

print('Ends with, we can use the "$"')
ends_w_world = re.compile(r'world!$')
print(ends_w_world.search('Hello World!'))

print(ends_w_world.search('Hello World!srghuiajjdskaa'))

sep()
print("All digits, starts with a digit '^', one or more '+', ends with '$'")
print('^\d+$')
all_digits = re.compile(r'^\d+$')
print(all_digits.search('23243243243258789798374823'))

print("If there is a letter in the middle, it wont match because it has a non digit character")
print(all_digits.search('232432432432587x89798374823'))

sep()
print("Having a '.' stands for any character except for a new line")
print("Anything followed by 'at' re = .at")
at_regex = re.compile(r'.at')
print(at_regex.findall('The cat in the hat sat on the flat mat.'))

print("one or two characters of anything '.{1,2}at'")
at_regex = re.compile(r'.{1,2}at')
print(at_regex.findall('The cat in the hat sat on the flat mat.'))

sep()
print(" We can use the '*' to match anything, a wildcard")
print("First Name: (.*) Last Name: (.*)")
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
print("First Name: Al Last Name: Sweigart")
print(name_regex.findall('First Name: Al Last Name: Sweigart'))

print("To use '*' in a non-greedy way we can use:")
serve = '<To serve humans> for dinner.>'
print(serve)
print("<(.*?)>")
non_greedy = re.compile(r'<(.*?)>') 
print(non_greedy.findall(serve))

print("For greedy matching we can:")
print("<(.*)>")
greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))

sep()
print("To get all characters including newlines with the '*' we can:")
print(" use '.*', re.DOTALL")
prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'
print(prime)
dot_star = re.compile(r'.*', re.DOTALL)
print(dot_star.search(prime))

sep()
print("We can do case insensitive matching with 're.IGNORECASE', 're.I'")
