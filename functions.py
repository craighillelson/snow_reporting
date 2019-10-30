""" __doc__ """

import csv
from collections import namedtuple

RTN = lambda: "\n"

DESCRIPTIONS_DCT = {}
DESCRIPTIONS_LST = []

def populate_dct():
    """ populates a dictionary with contents of a csv """
    with open('file.csv') as csv_file:
        f_csv = csv.reader(csv_file)
        column_headings = next(f_csv)
        csv_row = namedtuple('Row', column_headings)
        for rows in f_csv:
            row = csv_row(*rows)
            DESCRIPTIONS_LST.append(row.short_description)
            DESCRIPTIONS_DCT[row.number] = [row.company, row.short_description,\
            DESCRIPTIONS_LST.count(row.short_description)]
