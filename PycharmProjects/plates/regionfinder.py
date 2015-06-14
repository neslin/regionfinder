__author__ = 'neslin'
# App to find russian region from license plate number

import sys
import bs4
import re

# if len(sys.argv) < 2:
#     search = str(input('Enter area code:'))
# else:
#     search = sys.argv[1]
search = '1'


def get_rows():
    htmlfile = open('plates.html', 'rb')
    soup = bs4.BeautifulSoup(htmlfile)
    table = soup.find('table', attrs={'class': 'wikitable'})

    rows = []
    rowsdict = {}

    for row in table.findAll('tr'):
        cells = []
        for cell in row.findAll('td'):
            text = re.sub(r'^0|(\[2\])', '', cell.getText())  # Strip leading zeros and [2]
            cells.append(text)
            rows.append(cells)

    for line in rows:
        rowsdict[line[1]] = line[0]

    return rowsdict


def main():
    found = False
    for region, code in get_rows().items():
        # Try to match search string in the beginning, middle and end
        matchgroup = re.search(r'''
                        (^{0}$) # Match beginning, regions with one code
                        |(^{0}\b) # Match beginning, regions with multiple codes, not sure if this is needed
                        |(\b{0}\b) # Match codes among other codes, in order to display only one code
                        |(\b{0}$) # Match code at the end
                        '''.format(search), code, re.VERBOSE)
        if matchgroup:
            match = matchgroup.group()
            print('Area code {} belongs to {}'.format(match.strip(', '), region))
            found = True
    if not found:
        print("Not found")


if __name__ == '__main__':
    main()

# ^{}$)|(^{}\D)|(\D{}\D)|(\D{}$
