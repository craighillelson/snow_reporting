""" __doc__ """

import codecs
import csv
from collections import namedtuple
import functions

INCIDENTS = {}

with codecs.open('raw_data.csv', 'r', encoding='utf-8',
            errors='ignore') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        if row.company == "":
            INCIDENTS[row.number] = row.company, row.short_description

print(functions.RTN())

if not INCIDENTS:
    print('no results')
else:
    print('company is empty'.upper())
    for num, company_short_description in INCIDENTS.items():
        company = company_short_description[0]
        short_description = company_short_description[1]
        if not company:
            print(num, short_description)

print(functions.RTN())
