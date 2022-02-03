# CB site xml parser. Currency type. N = 34. format = (id, label, name, value, something)
# http://librerussia.blogspot.com/2014/12/python-3-xml.html
# https://coderoad.ru/
import urllib.request
from xml.dom import minidom


# open xml page and download data in xml format
url = "http://www.cbr.ru/scripts/XML_daily.asp"

webFile = urllib.request.urlopen(url)
data = webFile.read()

UrlSplit = url.split("/")[-1]
ExtSplit = UrlSplit.split(".")[1]
FileName = UrlSplit.replace(ExtSplit, "xml")
with open(FileName, "wb") as localFile:
    localFile.write(data)
webFile.close()

# xml parsing
doc = minidom.parse(FileName)
root = doc.getElementsByTagName("ValCurs")[0]
date = "{date}\n".format(date=root.getAttribute('Date'))

currency = doc.getElementsByTagName("Valute")
data = []
i = 0
for rate in currency:
    sid = rate.getAttribute("ID")
    charcode = rate.getElementsByTagName("CharCode")[0].firstChild.nodeValue
    name = rate.getElementsByTagName("Name")[0].firstChild.nodeValue
    value = rate.getElementsByTagName("Value")[0].firstChild.nodeValue
    nominal = rate.getElementsByTagName("Nominal")[0].firstChild.nodeValue
    data.append((sid, charcode, name, value, nominal))
    i = i+1

for dat in data:
    print(dat)

print(i)

with open("D:/Based_bot/dbs/header.csv", "w") as out:
    for dat in data:
        out.write("{0};{1}\n".format(dat[0], dat[1]))
