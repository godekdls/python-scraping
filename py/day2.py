from urllib2 import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup
import re

def getHtml(url):
    try:
        return urlopen(url)
    except HTTPError as e:
        print("failed to open url")
        return None

html = getHtml("http://pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read(), "html.parser")
nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())

html = getHtml("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
children = bsObj.find("table", {"id": "giftList"}).children
descendants = bsObj.find("table", {"id": "giftList"}).descendants
siblings = bsObj.find("table", {"id":"giftList"}).tr.next_siblings
price = bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text()

regularExp = re.compile("\.\.\/img\/gifts\/img.*\.jpg")
images = bsObj.findAll("img", {"src": regularExp})
for image in images:
    print(image["src"])