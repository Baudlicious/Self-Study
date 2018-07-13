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

import os

total_size = 0

for filename in os.listdir('/home/x3830s/github/Self-Study/'):
    if os.path.isfile(os.path.join('/home/x3830s/github/Self-Study/', filename)):
            continue
    total_size = total_size + os.path.getsize(os.path.join(os.path.join('/home/x3830s/github/Self-Study/', filename)))


            
print(total_size)
