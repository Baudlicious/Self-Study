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

title('Walking Directory Tree\'s', '14/07/18')
import os
sep('The os.walk(\'rootfolder\') allows you to go through a directory tree' )
for folder_name, sub_folders, file_names in os.walk('/home/x3830s/github/'):
    print('The folder is {}'.format(folder_name))
    print('The sub folders in {} are: {}'.format(folder_name, str(sub_folders)))
    print('The file names in {} are: {}'.format(folder_name, str(file_names)))
    print()



