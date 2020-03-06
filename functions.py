""" __doc__ """

import codecs
import csv
from collections import namedtuple

RTN = lambda: '\n'

def format_days(a, b):
    """ format days as floats to the second decimal """
    b = '{0:.2f}'.format(a)

    return b


def format_percentage(a, b):
    per = float(a / b) * 100
    per_fmt = '{0:.2f}'.format(per)+'%'
    return per_fmt


def open_csv(a, b):
    with codecs.open('raw_data.csv', 'r', encoding='utf-8',
                errors='ignore') as csv_file:
        F_CSV = csv.reader(csv_file)
        COLUMN_HEADINGS = next(F_CSV)
        CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
        for rows in F_CSV:
            row = CSV_ROW(*rows)
            if row.company != "":
                a.append(row.company)
                b[row.number] = row.company, row.short_description


def switch_case(a, b):
    """ switch case statement """
    a
    return a.get(b, 'nothing')


def total_tasks(a):
    total_tasks = len(a)
    return total_tasks
