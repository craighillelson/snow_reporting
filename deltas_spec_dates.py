""" __doc__ """

import csv
from collections import namedtuple

def switch_case(argument):
    """ switch case statement """
    dct_enum
    return dct_enum.get(argument, 'nothing')


dct = {}
dct_enum = {}

with open('tix_cre_wkly.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        tix = int(row.num)
        dct[row.date] = tix

print('select two dates from below')
for i, (k, v) in enumerate(dct.items(), 1):
    dct_enum[i] = k, v
    print(i, k, v)

print('\n')

usr_sel_date1 = int(input('choose a date from the options above '))
usr_sel_date2 = int(input('choose a later date from the options above '))

date1_lst = switch_case(usr_sel_date1)
date2_lst = switch_case(usr_sel_date2)

date1 = date1_lst[0]
date2 = date2_lst[0]

tix1 = date1_lst[1]
tix2 = date2_lst[1]

delta = tix2 - tix1

perc = int(delta / tix2 * 100)
if perc > 0:
    perc_fmt = '+{0:.0f}'.format(perc) +'%'
else:
    perc_fmt = '{0:.0f}'.format(perc) +'%'

print('\n')

print(f'dates: {date1} - {date2}')
print(f'delta: {delta}')
print(f'percent change: {perc_fmt}')

print('\n')
