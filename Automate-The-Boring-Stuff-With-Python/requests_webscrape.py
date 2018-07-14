#!/usr/bin/env python
# This is x3830s python files from the book Automate Python The
# Boring Stuff with Python. 

def title(big_title, date):
    print('!!!!' + big_title.upper().center(70) + ' !!!!')
    print(date.upper().center(80))

def sep(title):
    print("-" * 80)
    print('[ + ] ' + title.title())
    print("-" * 80 +"\n")

def function(func):
    print(">> " + func + ":")
title('Getting page content with requests library', '14/07/08')
import requests

sep('To get a website use requests.get("website")')
res = requests.get('https://www.automatetheboringstuff.com/files/rj.txt')

sep('To test to see that the request was successful use .status_code()')
print(res.status_code)

sep('We can raise an exception if there is a problem, but nothing if success with .raise_for_status()')
function('It can also be put into a try and except statement to stop the program from halting')
print(res.raise_for_status())
sep('To grab the text from the page use .text, we can grab a specific amount')
function('Grab the first 500 characters with .text[:500]')
print(res.text[:500])

sep('We can write the content of a page to a file using open() and iter_content()')
play_file = open('romeoandjuliet', 'wb') # must use binary to maintain encoding
for chunk in res.iter_content():
    play_file.write(chunk)

play_file.close()
