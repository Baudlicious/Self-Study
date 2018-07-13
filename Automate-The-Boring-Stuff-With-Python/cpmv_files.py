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

title('Copying and Moving Files', '13/07/18')

sep('We can import shutil to do our copy functions')

import shutil

sep('Can use shutil.copy(source,destination) to copy a single file')
print("shutil.copy('/home/x3830s/file', '/home/x3830s/github/file')")


sep('Copy entire folder full of folders and files shutil.copytree(source, destination)')
print("shutil.copytree('/home/x3830s/', '/home/x3830s.bak/')")

sep('To move files we can use shutil.move(source, destination)')
print("shutil.move('/home/file.txt', '/home/x3830s/')")

function('To rename files shutil.move(oldname, newname)')
