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

title('Using the Webbrowser Module to webscrape', '14/07/18')

import webbrowser, sys, pyperclip
sep('We can use webbrowser to open pages in our default browser')
# TODO: Check if command line arguments were passed.
if len(sys.argv) > 1:
    # take all space seperated values in the list, and join into a single string value 
    address = ' '.join(sys.argv[1:])
else:
    # assume if not a cli argument its on the clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/{}'.format(address))
