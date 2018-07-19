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

title('GUI automation using pyautogui', '19/07/18')

import pyautogui
sep('To return the screen resolution we can use pyautogui.size()')
print('width, height = pyautogui.size()')

sep('To look at the current mouse position we can use pyautogui.position()')
print('x, y = pyautogui.position()')

sep('TO move the mouse we use pyautogui.moveTo(x, y)')
print('pyautogui.moveTo(10,10)')
print('pyautogui.moveTo(10,10, duration=1.5)')

sep('To have the mouse click use pyautogui.click(x,y)')
print('pyautogui.click(339, 38)')
print('pyautogui.Doubleclick(339, 38)')
print('pyautogui.Doubleclick()')

sep('THere is a failsafe that allows you to put the mouse in the top left to stop')

sep('With the pyautogui.displayMousePosition() we can see realtime coordinates for mouse position')
