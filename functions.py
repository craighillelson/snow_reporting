""" __doc__ """

import codecs
import csv
from collections import namedtuple

RTN = lambda: '\n'

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


def print_headers():
    """ print headers """
    print('number,company,short description')
    print(RTN())


def print_break():
    """ print visual divider """
    print('*' * 10)


def format_percentage(a, b):
    per = float(a / b) * 100
    per_fmt = '{0:.2f}'.format(per)+'%'
    return per_fmt


def write_to_csv(name_of_file, dct):
    """ write dictionary to csv """
    import csv

    # define HEADERS
    # HEADERS =

    with open(name_of_file, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(HEADERS)
        for k, v in dct.items():
            keys_values = (k, v)
            out_csv.writerow(keys_values)


def count_words(a):
    """ count words """
    # count words
    a = short_desc_str.split()

    for w in a:
        wordfreq.append(a.count(w))

    # zip lists
    for word_count in zip(a, wordfreq):
        dct[word_count[0]] = word_count[1]

    # output results
    print('word, count')
    for word, count in sorted(dct.items(), key=lambda x: x[1], reverse=True):
        print(word, count)


def total_tasks(a):
    total_tasks = len(a)
    return total_tasks


# def concat_terms_data_stores(a):
#     term_dct = a.lower() + '_dct'
#     term_dct = {}
#     term_csv = a.lower() + '.csv'
