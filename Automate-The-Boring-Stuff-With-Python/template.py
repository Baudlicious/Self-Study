#!/usr/bin/env python
# This is x3830s python files from the book Automate Python The
# Boring Stuff with Python. 

def title(big_title, date):
    print('!!!!' + big_title.upper().center(70) + ' !!!!')
    print(date.upper().center(80))

def sep(title, function):
    print("-" * 80)
    print('[ + ] ' + title.title())
    print("-" * 80 +"\n")

    print(">> " + function + ":")

def function(func):
    print(">> " + func + ":")


