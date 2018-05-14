import requests
import sys
from bs4 import BeautifulSoup
from urllib.parse import urlparse

extensions = []
gextensions = []
directories = []
ghrefs = []

# Grabs headers from the Target for enumeration
def finger_print(url):
    request = requests.get(url)
    if request.status_code == requests.codes.okay:
        print("*" * 80)
        print("RHOST returned {}".format(request.status_code))
        print("*" * 80)
        for key, value in request.headers.items():
            print("{0} : {1}".format(key, value))
    else:
        print("RHOST returned {}".format(requests.exceptions.RequestException))
    print("*" * 80)


# Displays specificed file type and directories from a wordlist if response back is Ok.
def python_buster(url,filetype,wlist):
    rhost = url 
    file_ext = filetype
    wordlist = wlist 
# Scan website for links
    print("Links found on home page:")
    href_request = requests.get("http://" + url)
    href_c = href_request.content
    soup = BeautifulSoup(href_c, "lxml") 
    hrefs = soup.find_all('a')
    i = 0
    for item in hrefs:
        #get the text contained in href
        stripped = item.attrs['href']
        i += 1
        print("{0} [+] http://{1}/{2}" .format(i,url,stripped.strip('/')))
        ghrefs.append("http://{0}/{1}" .format(url,stripped.strip('/')))
    print("*" * 80)

    # Open the file, sum number of words
    with open(wlist, 'r') as words_file:
        count = sum(1 for line in open(wlist))
        print("Using {0} Wordlist with {1} possibilities, starting directory and \nfile search on http://{2}/".format(wordlist, count, rhost))
        print("*" * 80)  
        #parse word list form a URL and make request for extensions and directories
        for word in words_file:
            parse = word.rstrip()
            req_url = "http://" + url +"/" + parse
            request = requests.get(req_url, timeout=3)
            if request.status_code == requests.codes.okay:
                ext_req_url = "http://" + url +"/" + parse + "." + file_ext
                ext_request = requests.get(ext_req_url, timeout=3)
                #Assume it is directory, if if the request has an extension go to the else
                if ext_request.status_code != requests.codes.okay: 
                    directories.append("[+] (Status: {0}) Valid extenisons: {1}".format(str(request.status_code),request.url))
                else:
                    extensions.append("[+] (Status: {0}) Valid extenisons: {1}".format(str(ext_request.status_code),ext_request.url))
                    gextensions.append(ext_request.url)
    words_file.closed

    

    print("Directories:")
    i = 0
    for item in directories:
        i += 1
        print(i,item)
    print("-" * 80)
    print("Extension '{0}': ".format(filetype))
    i = 0
    for item in extensions:
        i += 1
        print(i,item)
    print("*" * 80)

def query_check():
    print("The following possible pages may be vulnerable to SQL injection:")
    query_urls = []
    for item in ghrefs:
        parsed = urlparse(item)
        if parsed.query != "":
            print(parsed.geturl())
            query_urls.append(parsed.geturl())
            print("-"*80)

    for url in query_urls:
        page_request = requests.get(url)
        page_imgs = []
        page_c = page_request.content
        soup = BeautifulSoup(page_c, "lxml")
        img_tag = soup.find_all('img')
        print(url+":")
        for item in img_tag:
            page_imgs.append(item.attrs['src'])
        print(", ".join(page_imgs))

print("-"*80)
        

"""
    sql = input("Which page would you like to test for SQLi: ")    
    i = 0
    options = {} 
    for item in gextensions:
        i += 1
        options.update({str(i): item})
    
    if sql in options: 
        query = input("Enter query parameter: ")
        page = options.get(sql, None)
        sql_request = requests.get(page + "?" + query + "=" + "`")
        sql_c = sql_request.content
        soup = BeautifulSoup(sql_c, "lxml")
        text = soup.find("div", {"id": "content"}).get_text()
        print(text)
        href_text = soup.find_all('a', href=True)
        print(href_text) 

    else:
        print("nopes")

"""




    
pen_url = input("Input an host (vulnerable): ")
file_ext = input("What file extension are you looking for: ")
finger_print("http://" + pen_url)
python_buster(pen_url,file_ext,"small.txt")

query_check()
