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

title('Logging in Python', '14/07/18')
sep('We can log by importing the logging library and call logging.basicConfig()')

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
print("logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')")
# logging.disable(logging.CRITICAL)


function('This code has a bug in it and we will use it to show loggings function')
function('They are like print function calls, but with a lot of information')

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial (%s)' % (n))
    total = 1
    # to fix this code we must start range at 1 'range(1,n +1)'
    for i in range(n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))
logging.debug('End of program')

sep('We can add logging.disable(logging.CRITICAL) at the top to stop all logging messages')
function('There are multiple levels of errors')
print('logging.DEBUG()\nlogging.INFO()\nlogging.WARNING\nlogging.ERROR\nlogging.CRITICAL')

sep('We can log to a file by declaring a "filename="filename" in our basicConfig()')
print("logging.basicConfig(fielname='myprogram.log',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')")

