__author__ = 'neslin'
# App to find russian region from license plate number


import bs4
import re

htmlFile = open('plates.html', 'rb')
soup = bs4.BeautifulSoup(htmlFile)
# search = str(input('Enter area code:'))
search = '3123'
table = soup.find('table', attrs={'class':'wikitable'})

rows = []
rowsDict = {}


for row in table.findAll('tr'):
    cells = []
    for cell in row.findAll('td'):
        text = re.sub(r'^0|(\[2\]|\(|\))','', cell.getText()) # Strip leading zeros and [2]
        cells.append(text)
        rows.append(cells)


for row in rows:
    rowsDict[row[1]] = row[0]

for region, code in rowsDict.items():
    # Try to match search string in the beginning, middle and end
    m = re.search(r'(^{}$)|(^{}\D)|(\D{}\D)|(\D{}$)'.format(search, search, search, search), code)
    if m:
        print(m.group(), region)
    else:
        print("Not found")
