import argparse
import requests
import json 
# Lines
def single_line():
    print("-" * 80)
def double_line():
    print("=" * 80)

# URL info
def url_information():
    single_line() 
    print("URL: {0}, Port: {1}, Status: {2}".format(argument.url, argument.port,request.status_code))
    single_line() 

# CLI options for interacting with the parser
parser = argparse.ArgumentParser(
    description='This is an HTTP request client')

parser.add_argument('-u', '--url', help="Store a url 'http(s)://www.web.site'")
parser.add_argument('-e', '--header', action="store_true", help="Grab headers from Target")
parser.add_argument('-p', '--port', help="Specify a port number")
parser.add_argument('-c', '--content', action="store_true", help="Grab page content")

argument  = parser.parse_args()
print("\t\t\tx3830s Simple HTTP client")
# GET request for the HTTP req client
if argument.url: 
     double_line()
     #if a port is defined use that   
     if argument.port: 
         request = requests.get(argument.url + ":" + argument.port.strip())
     else:
        request = requests.get(argument.url)
    
     url_information()

    # check to make sure the status code is okay, then check the arguments
     if request.status_code == requests.codes.ok:
         if argument.content:
            print(request.text)
            url_information()
         if argument.header:
            print("Headers:")
            for key, value in request.headers.items():
                print("\t{0}: {1}".format(key, value))
            double_line()
     else:
        print("Error Connecting")

else:
    print("Must supply a url\n")
    parser.print_usage()




