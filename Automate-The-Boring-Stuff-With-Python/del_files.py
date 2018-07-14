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

title('Deleting Files', '13/07/18')

import os

sep("Delete a single file with os.unlink('filename')")

sep("Delete a directory with os.rmdir('directory')")
function('This will not delete if the dir is not empty')

sep("Delete a directory and all of its files shutil.rmtree('directory')")
