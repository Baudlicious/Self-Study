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

title('Beautiful Soup', '16/07/18')
sep('URL is broken here but I have experience with bs4 so im not concerned with fixing')

import bs4
import requests

res = requests.get('http://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/')

res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

soup.select('#mediaNoAccordion > div.a-row > div.a-column.a-span7.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')

elems = soup.select('#mediaNoAccordion > div.a-row > div.a-column.a-span7.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')
print(elems)
#print(elems[0].text.strip())
