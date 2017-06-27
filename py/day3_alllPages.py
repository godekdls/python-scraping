# -*- coding: utf-8 -*-

from urllib2 import urlopen
from urlparse import urlparse
from bs4 import BeautifulSoup

import day3_randomPage
import re

#Collects a list of all external URLs found on the site
allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    domain = urlparse(siteUrl).scheme + "://" + urlparse(siteUrl).netloc
    bsObj = BeautifulSoup(html, "html.parser")
    internalLinks = getInternalLinks(bsObj,domain)
    externalLinks = getExternalLinks(bsObj,domain)

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            getAllExternalLinks(link)

followExternalOnly("http://oreilly.com")

allIntLinks.add("http://oreilly.com")
getAllExternalLinks("http://oreilly.com")