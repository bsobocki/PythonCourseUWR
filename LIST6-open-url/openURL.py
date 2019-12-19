from bs4 import BeautifulSoup as BS
import urllib.request
import urllib.error

def openFromURL(url):
    try: 
        page = urllib.request.urlopen(url)
    except urllib.error.HTTPError: 
        return ""
    mybytes = page.read()
    page.close()
    try : 
        return mybytes.decode("utf8")
    except UnicodeDecodeError: 
        return ""

def BeautifulSoupFromURL(url):
    openedWebsite = openFromURL(url)
    if not (openedWebsite == "" ): 
        return BS(openedWebsite, "html.parser")
    else: 
        return None