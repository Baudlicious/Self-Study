#!/usr/bin/env python3
# This is x3830s python files from the book Automate Python The
# Boring Stuff with Python. 
import re, pyperclip

def title(big_title, date):
    print('!!!!' + big_title.upper().center(70) + ' !!!!')
    print(date.upper().center(80))

def sep(title):
    print("-" * 80)
    print('[ + ] ' + title.title())
    print("-" * 80 +"\n")

def function(func):
    print(">> " + func + ":")

title('RegEx PDF Scraper', '07/12/18')
function("Takes emails and phone numbers from clipboard, and places that back into the clipboard")

# Create a regex for phone numbers
phone_regex = re.compile(r'''
           (
           ((\d\d\d) | (\(d\d\d\)))?    # area code (optional)
           (\s|-)                       # first seperator
           \d\d\d                       # first three digits
           -                            # separator
           \d\d\d\d                     # last 4 digits
           ((ext(\.)?\s |x)             # extension  word-part(optional)
           (\d{2,5}))?                  # extension number-part(optional) 
           )
           ''', re.VERBOSE)

# Create a regex for email add 
email_regex = re.compile(r'''
                        [a-zA-Z0-9_.+]+ # name part
                        @               # @ symbol
                        [a-zA-Z0-9_.+]+ # domain name part
                        ''', re.VERBOSE)
# Get the text off the clipboard 
text = pyperclip.paste()

# Extract the email/phone from this text
extracted_phone = phone_regex.findall(text)
extracted_email = email_regex.findall(text)

all_phone_numbers = []

for number in extracted_phone:          # put all the first numbers from re into a list
    all_phone_numbers.append(number[0])


# Copy the extracted email/phone to clipboard 
phone_format = '\n'.join(all_phone_numbers)         # one number per line
email_format = '\n'.join(extracted_email)                 # one email per line 
results = phone_format + email_format               # All together 
pyperclip.copy(results)

