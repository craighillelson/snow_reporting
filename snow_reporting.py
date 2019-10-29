""" __doc__ """

import csv
from collections import namedtuple

RTN = lambda: "\n"

DESCRIPTIONS_DCT = {}
DESCRIPTIONS_LST = []

with open('file.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        DESCRIPTIONS_DCT[row.number] = [row.company, row.short_description]
        DESCRIPTIONS_LST.append(row.short_description)

# company field is empty
print RTN()
print "company is empty".upper()
for k, v in DESCRIPTIONS_DCT.items():
    if not v[0]:
        print k, v[1]

# short description is empty
print RTN()
print "short description is empty".upper()
for k, v in DESCRIPTIONS_DCT.items():
    if not v[1]:
        print k

# print short descriptions
print RTN()
print "short descriptions".upper()
for description in sorted(DESCRIPTIONS_LST):
    if description:
        print description

# print short descriptions
print RTN()
print "unique short descriptions".upper()
for description in sorted(set(DESCRIPTIONS_LST)):
    if description:
        print description

# count occurances short descriptions
