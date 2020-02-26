""" __doc__ """

import codecs
import csv
import functions
from collections import namedtuple

SHORT_DESC_DCT = {}
INCS_COUNT = []
INCS = []

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
    co = v[0]
    s_desc = v[1]
    co_s_desc = co, s_desc
    INCS.append(co_s_desc)

for i in sorted(set(INCS)):
    co = i[0]
    inc = i[1]
    count = INCS.count(i)
    co_inc_count = co, inc, int(count)
    INCS_COUNT.append(co_inc_count)

from collections import defaultdict

d = defaultdict(list)

for k, *v in INCS_COUNT:
    d[k].append(v)

print('\n')

results = {}

for k, v in sorted(d.items()):
    print(k)
    for i in sorted(v, key = lambda x: x[1], reverse=True):
        s_desc = i[0]
        count = i[1]
        tup = (s_desc, count)
        print(tup[0], tup[1])
    print('\n')
