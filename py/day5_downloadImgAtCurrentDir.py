# -*- coding: utf-8 -*-
# 오늘부터 python3

import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "downloaded"
baseUrl = "http://pythonscraping.com"

def getAbsoluteURL(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://" + source[11:] # www. 제거
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = "http://" + source[4:]
    else:
        url = baseUrl + "/" + source

    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl, absoulteUrl, downloadDirectory):
    path = absoulteUrl.replace("www.", "")
    path = path.replace(baseUrl, "")
    path = downloadDirectory + path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)

    return path


html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html, "html.parser")
downloadList = bsObj.findAll(src=True)

for download in downloadList:
    sourceUrl = download["src"]
    fileUrl = getAbsoluteURL(baseUrl, sourceUrl)
    if fileUrl is not None:
        print(fileUrl)

downloadDirectory = "./"
downloadPath = getDownloadPath(baseUrl, fileUrl, downloadDirectory)
urlretrieve(fileUrl, downloadPath)