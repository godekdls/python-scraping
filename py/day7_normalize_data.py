from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import re
import string
import ssl

def cleanInput(input):
    input = re.sub('\n+', " ",  input)
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if (len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i')):
            cleanInput.append(item)
    return cleanInput

def ngrams(input, n):
    input = cleanInput(input)
    output = []
    for i in range(len(input) -n+1):
        output.append(input[i:i+n])
    return output


context = ssl._create_unverified_context()
html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)", context=context)
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
ngrams = ngrams(content, 2)
# ngrams = OrderedDict(sorted(ngrams, key=lambda t: t[1], reverse=True))
print(ngrams)