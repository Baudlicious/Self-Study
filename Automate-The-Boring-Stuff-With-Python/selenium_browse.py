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

title('Using Selenium to control the browser', '16/07/18')
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')

sep('Click a link by using browswer.find_element_by_css_selector()')
#Unique selector string copied from the inspect element in the browswer for a link
elem = browser.find_element_by_css_selector('.entry-content > ol:nth-child(15) > li:nth-child(1) > a:nth-child(1)')
print(elem)

elem.click()

sep('Fill in search/text fields')
search_elem = browser.find_element_by_css_selector('.search-field')
# Text to add
search_elem.send_keys('zophie')
searchElem.submit()

sep('We can also use the browsers navigation')
print('browser.back()')
print('browser.forward()')
print('browser.refresh()')
print('browswer.quit()')

#Bring up another webbrowser
browser = webdriver.Firefox()

sep('Selenium can read the content with browser.find_element_by_css_selector("body")')



