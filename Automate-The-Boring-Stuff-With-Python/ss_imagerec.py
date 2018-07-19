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

title('Screenshots and Image Recognition', '19/07/18')
sep('pyautogui.screenshot() can be used to take screen shots')
print('pyautogui.screenshot("path/to/file")')

sep('We can do image recognition with pyautogui.locateOnScreen("file/of/image")')
function('Taking a screenshot of what you want to locate will allow the mouse to intelligently select specific buttons')
print('pyautogui.locateCenterOnScreen("image/we/want")')
