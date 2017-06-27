# -*- coding: utf-8 -*-

from urllib2 import urlopen
from urlparse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set() # collection
random.seed(datetime.datetime.now())

def getInternalLinks(bsObj, includeUrl):
    # url pattern : scheme://netloc/path;parameters?query#fragment
    # find all internal urls
    includeUrl = urlparse(includeUrl).scheme + "://" + urlparse(includeUrl).netloc
    internalLinks = []
    # find all links that start with '/'
    for link in bsObj.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith("/")):
                    internalLinks.append(includeUrl + link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks

def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # find all links that don't have the current url and start with http or www
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
    # if there is no external link, try to get a random internal link and expect it has any external link
    if len(externalLinks) == 0:
        domain = urlparse(startingPage).scheme + "://" + urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsObj, domain)
        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(staringSite):
    externalLink = getRandomExternalLink(staringSite)
    print("Random external link is : " + externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")