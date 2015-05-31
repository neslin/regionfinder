__author__ = 'neslin'
# App to find russian region from license plate number


import sys


args = sys.argv
found = False

if len(args) > 2:
    search = sys.argv[1]
else:
    search = input("Enter plate number:")


records = {'moscow': [77, 97, 99, 177, 197, 199, 777],
           'st. petersburg': [78, 98, 178]

           }

for region, number in records.items():
    if int(search) in number:
        print("{} is from {}".format(search, region.title()))
        found = True

if not found:
    print("Not found")