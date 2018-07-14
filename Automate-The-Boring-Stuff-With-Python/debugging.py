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

title('Debugging', '14/07/18')

sep('Exceptions can be raised with \'raise Exception(\'errormessage\')')

function('With a program like this there should be a way of checking errors')
def box_print(symbol, width, height):
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol) 
    print(symbol * width)

box_print('*', 15, 5)
box_print('**', 15, 5)
function('By adding raise Exception() here we can guide / correct output')
def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1.')
    if (width < 2) or (height < 2):
        raise Exception("'Width' and 'height' must be greater or equal to 2.")
        
        
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol) 
    print(symbol * width)


box_print('*', 15, 5)
# this string would throw an error box_print('**', 15, 5)

sep('We can get the traceback text as a string value by importing traceback')
function('This is good for allowing the program to continue, but creating a log of errors')

import traceback
try:
    raise Exception('This is the error message.')
except:
    error_file = open('errors.log', 'a')
    error_file.write(traceback.format_exc())
    error_file.close()
    print('The traceback info was written errors.log')

sep('We can use assert statements for sanity checks for programming errors')
market_2nd = {'ns': 'green', 'ew': 'red'}

def switch_lights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    # I declare that this should always hold true, if it fails there is a bug
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

switch_lights(market_2nd)
