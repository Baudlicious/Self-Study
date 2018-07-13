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

title('Filenames and Absolute/Relative file paths', '07/12/18')
sep('OS paths os.path.join')
function('We can make OS paths suitable for the environment that the program is running in')
import os
path = os.path.join('folder1', 'folder2', 'folder3', 'file.png')
print(path)

function("We can detect the seperator")
print(os.sep)
sep('We can get the current working directory with os.getcwd()')
print(os.getcwd())
home = os.getcwd()

sep('Change directories os.chdir()')
function('We can change the current working directory which will change the output of .getcwd()')
print("Change to /etc with os.chdir('/etc')")
os.chdir('/etc')
print(os.getcwd())
os.chdir(home)

sep('Covert relative into absolute path with os.path.abspath()')
function("Relative path for Automate_regex.py with os.path.abspath()")
print(os.path.abspath('Automate_regex.pdf'))
function("We can test to see if the path provided is abs or relative with .isabs()")
print(os.path.isabs('Automate_regex.pdf'))
print(os.path.isabs(home +'Automate_regex.pdf'))

sep('Retrieve Directories with os.path.dirname()')

sep('Retrieve after the final slash with os.path.basename()')

sep('Check to see if path/file exists with os.path.exists()')

sep('Check to see if file with os.path.isfile()')

sep('Check to see if directory with os.path.isdir()')

sep('Check size in bytes with os.path.getsize()')
print('/mnt/c/windows/system32/calc.exe')
print(os.path.getsize('/mnt/c/windows/system32/calc.exe'))

sep('List the files and folders within a dir with os.listdir()')
print("os.listdir('/home/x3830s/github/Self-Study')")
print(os.listdir('/home/x3830s/github/Self-Study'))

sep('Create new folders os.makedirs()')
