__author__ = 'neslin'
# App to find russian region from license plate number

import sys
import bs4
import re

if len(sys.argv) < 2:
    search = str(input('Enter area code:'))
else:
    search = sys.argv[1]
# search = '77'


htmlFile = open('plates.html', 'rb')
soup = bs4.BeautifulSoup(htmlFile)

table = soup.find('table', attrs={'class': 'wikitable'})
found = False

rows = []
rowsDict = {}


for row in table.findAll('tr'):
    cells = []
    for cell in row.findAll('td'):
        text = re.sub(r'^0|(\[2\]|\(|\)|)', '', cell.getText())  # Strip leading zeros and [2]
        cells.append(text)
        rows.append(cells)

for row in rows:
    rowsDict[row[1]] = row[0]

for region, code in rowsDict.items():
    # Try to match search string in the beginning, middle and end
    matchGroup = re.search(r'(^{}$)|(^{}\D)|(\D{}\D)|(\D{}$)'.format(search, search, search, search), code)
    if matchGroup:
        match = matchGroup.group()
        print('Area code {} belongs to {}'.format(match.strip(','), region))
        found = True

if not found:
    print("Not found")

# ^{}$)|(^{}\D)|(\D{}\D)|(\D{}$
