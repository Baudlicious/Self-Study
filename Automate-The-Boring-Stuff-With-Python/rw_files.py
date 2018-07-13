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
title('Reading and Writing Files', '07/13/2018')
sep('Open files with open()')
hello_file = open('/home/x3830s/hello')
content = hello_file.read()

sep('Read whole files with .read()')
print(content)
sep('Read lines with .readlines()')
hello_file = open('/home/x3830s/hello')
content = hello_file.readlines()
print(content)
sep('be sure to close files after reading them with .close()')
hello_file.close()

sep('Content can be written with adding "w", it will start from scratch')
print("'/home/x3830s/hello', 'w'")
print("hello_file.write('\\nSup')")
print("hello_file.close()")
sep('Content can be appended by adding a "a"')
print("'/home/x3830s/hello', 'a'\n")
print("hello_file.write('\\nSup')")
print("hello_file.close()")
function('If the file does not exist for W or A modes, it will create a new one')

sep('Shelf file objects are similar to dictionaries and stores in a binary file')
import shelve
shelf_file = shelve.open('mydata')
print("shelve.open('mydata')")
print("shelf_file['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']")
shelf_file['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']
shelf_file.close()

shelf_file = shelve.open('mydata')
print(shelf_file['cats'])
