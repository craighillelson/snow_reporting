""" __doc__ """

import codecs
from collections import defaultdict
import csv
import functions
from collections import namedtuple

SHORT_DESC_DCT = {}
INCS_COUNT = []
INCS = []
DCT = defaultdict(list)

# import csv and populate a dictionary with its contents
with codecs.open('raw_data.csv', 'r', encoding='utf-8', \
errors='ignore') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        if row.company != "":
            SHORT_DESC_DCT[row.number] = [row.company, row.short_description]

for k, v in sorted(SHORT_DESC_DCT.items(), key=lambda x: x[1], reverse=True):
    company = v[0]
    short_description = v[1]
    company_short_description = company, short_description
    INCS.append(company_short_description)

for i in sorted(set(INCS)):
    co = i[0]
    inc = i[1]
    count = INCS.count(i)
    co_inc_count = co, inc, int(count)
    INCS_COUNT.append(co_inc_count)

for k, *v in INCS_COUNT:
    DCT[k].append(v)

print(functions.RTN())

for co, v in sorted(DCT.items()):
    print(co)
    for i in sorted(v, key = lambda x: x[1], reverse=True):
        short_description = i[0]
        count = i[1]
        tup = (short_description, count)
        print(tup[0], tup[1])
    print(functions.RTN())
