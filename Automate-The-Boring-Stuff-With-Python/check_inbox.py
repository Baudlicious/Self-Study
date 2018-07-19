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

title('Checking email inboxes with imap')

import imapclient
sep("Create a connection object with imapclient.IMAPClient('server', ssl=True)")
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)

sep("Log in with conn.login('email', 'password')")
conn.login('email', 'password')

sep("Select the specific folder with .select_folder('FOLDER', readonly=True)"
conn.select_folder('FOLDER', readonly=True)
function('Readonly = True makes sure you dont accidently modify things')

sep("To find the emails we can use the .search([]) method")
function("Returns a list of UIDs that meet the search criteria")
UIDs = conn.search(['SINCE 20-Aug-2015'])
print(UIDs)

sep("To get the content based on the UIDs use .fetch([UID], ['BODY[]', 'FLAGS'])")
print("raw_message = conn.fetch([47474],  ['BODY[]', 'FLAGS'])")

sep("We can use pyzmail to parse the content of the the raw message")
import pyzmail
print("message = pyzmail.PyzMessage.factory(raw_message[47474][b'BODY[]']")

sep("To get the subject of the email use .get_subject()")

sep("To get the address use .get_address")
print("message.get_address()")
print("message.get_address('from')")
print("message.get_address('to')")
print("message.get_address('bcc')")

sep("We can check to see if email has text or html with .text_part .html_part")
function("We get the body once we know this and decode it properly with .text_part.get_payload().decode('UTF-8')")

