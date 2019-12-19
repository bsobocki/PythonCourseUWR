from bs4 import BeautifulSoup as BS
import urllib.request as url
import openURL as op
import re
import requests

def crawl(start_page, distance, action):
    startPageSoup = op.BeautifulSoupFromURL(start_page)
    if startPageSoup is None: 
        return []

    result = [(start_page, action(start_page))]

    urls = [makeURL(link.get('href'), start_page) for link in startPageSoup.findAll('a')]
    for i in range( 0, min( [len(urls), distance] ) ):
        if urls[i] is not None :
            result += [(urls[i], action(urls[i]))]
    
    for i in result:
        yield i

def makeURL(link, url):
    try: 
        if re.match("https*://.*",link): 
            return link
        else : 
            newURL = url+link
            if not re.match(".*/\Z", link): 
                newURL+= '/'
            return newURL
    except TypeError: 
        return url

def action(url):  
    html = op.BeautifulSoupFromURL(url)
    if html is None: 
        return 0

    html_text = html.get_text() 
    founded = re.findall('.*[Pp][Yy][Tt][Hh][Oo][Nn].*', html_text)
    
    if founded is not None : 
        return len(founded)
    return 0