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

title('Sending emails with smtplib', '18/07/18')
import smtplib

sep('Established a connection with smtplib.SMTP("server", port) or smtplib.SMTP("server:port")')
conn = smtplib.SMTP('smtp.gmail.com', 587)

sep('Start the connection with .ehlo()')
conn.ehlo()

sep('Start a TLS with .starttls()')
conn.starttls()


sep('Login to an email account with .login("email", "password")')

sep("Send mail with logged in account with .sendmail('S email','R email', 'Subject: Text\\n\\nBody'")
function('There will be a blank dictionary if all emails sent correctly, and a populated one with the ones that failed to send')

sep('Close the connection with .quit()')
