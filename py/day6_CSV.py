from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
dataFile = StringIO(data)
# csvReader = csv.reader(dataFile) # return list
csvReader = csv.DictReader(dataFile) # return dictionary

for row in csvReader:
    # print("The album \"" + row[0] + "\" was released in " + str(row[1])) # list
    print("The album \"" + row["Name"] + "\" was released in " + str(row["Year"])) #  dictionary