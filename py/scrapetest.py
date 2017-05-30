from urllib2 import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup

def getHtml(url):
    try:
        return urlopen(url)
    except HTTPError as e:
        print("failed to open url")
        return None

def getTitle(html):
    # what if html is none?? -> AttributeError
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        return bsObj.body.h1
    except AttributeError as e:
        return None

html = getHtml("http://pythonscraping.com/pages/page1.html")
title = getTitle(html)
if (title == None):
    print("Title is not found")
else:
    print(title)