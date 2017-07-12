import ssl
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

# https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error
context = ssl._create_unverified_context()
html = urlopen("https://en.wikipedia.org/wiki/Comparison_of_text_editors", context=context)
bsObj = BeautifulSoup(html, "html.parser")
table = bsObj.findAll("table", {"class":"wikitable"})[0] # first table
rows = table.findAll("tr")

csvFile = open("../files/editors.csv", 'wt')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            text = cell.get_text()
            csvRow.append(text)
        writer.writerow(csvRow)
finally:
    csvFile.close()