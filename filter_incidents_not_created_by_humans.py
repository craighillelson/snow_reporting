""" __doc__ """

import functions

def format_percentage(a, b, c, d):
    """ formats float as a percentage to the second decimal """
    a = b / c * 100
    d = '{0:.2f}'.format(a)+'%'

    return d


def concat_lists(lst1, lst2, concatenated_list):
    """ concatenate lists """
    concatenated_list = lst1 + lst2

    return concatenated_list


def filtered_dct(a, b):
    """ return an enumerated dictionary containing filtered incidents """
    finalized_dct = {}

    for num, (incident_num, short_description) in \
              enumerate(a.items(), 1):
        check = any(item in short_description for item in b)
        if check is True:
            pass
        else:
            finalized_dct[incident_num] = short_description

    return finalized_dct


def open_csv_populate_dct(dct):
    """
    return a dictionary that includes only the incidents that do not
    include strings in short_descriptions_to_skip.csv
    """
    import codecs
    import csv
    from collections import namedtuple

    dct = {}

    with codecs.open('raw_data.csv', 'r', encoding='utf-8', errors='ignore') \
                     as csv_file:
        F_CSV = csv.reader(csv_file)
        COLUMN_HEADINGS = next(F_CSV)
        CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
        for rows in F_CSV:
            row = CSV_ROW(*rows)
            dct[row.number] = row.short_description

    return dct


def open_csv_populate_lst(file, lst):
    """
    return a dictionary that includes only the incidents that do not
    include strings in short_descriptions_to_skip.csv
    """
    import codecs
    import csv
    from collections import namedtuple

    lst = []

    with codecs.open(file, 'r', encoding='utf-8', errors='ignore') \
                     as csv_file:
        F_CSV = csv.reader(csv_file)
        COLUMN_HEADINGS = next(F_CSV)
        CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
        for rows in F_CSV:
            row = CSV_ROW(*rows)
            lst.append(row.short_description)

    return lst


def prompt_user():
    """
    prompt user for strings in short descriptions that they'd like to
    skip
    write those results to a csv
    """
    short_descriptions_to_add = []

    while True:
        print('please enter a string you\'d like filtered out of results or '
              'return to quit')
        short_description_to_add = input()
        if short_description_to_add == '':
            break
        short_descriptions_to_add = short_descriptions_to_add + \
                                     [short_description_to_add]

    return short_descriptions_to_add


def write_lst_to_csv(a):
    """ write results to a csv """
    import csv

    with open('short_descriptions_to_skip.csv', 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(['short_description'])
        for i in a:
            out_csv.writerow([i])

    print('"short_descriptions_to_skip.csv" exported successfully')


def write_dct_to_csv(a, b, c):
    """ """
    import csv
    import functions

    with open(a, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(b)
        for k, v in c.items():
            keys_values = (k, v)
            out_csv.writerow(keys_values)

    print(functions.RTN())
    print(f'"{a}" exported successfully')
    print(functions.RTN())


INCIDENTS = open_csv_populate_dct('incidents')
for i, (incident_num, short_description) in enumerate(INCIDENTS.items(), 1):
    print(i, incident_num, short_description)

SHORT_DESCRIPTIONS = open_csv_populate_lst('raw_data.csv', 'short_descriptions')
SHORT_DESCRIPTION_TO_ADD = prompt_user()
SHORT_DESCRIPTION_TO_SKIP = \
open_csv_populate_lst('short_descriptions_to_skip.csv',
                      'short_descriptions_to_skip')
ALL_SHORT_DESCRIPTIONS_TO_SKIP = concat_lists(SHORT_DESCRIPTION_TO_ADD,
                                              SHORT_DESCRIPTION_TO_SKIP, all)

write_lst_to_csv(ALL_SHORT_DESCRIPTIONS_TO_SKIP)
FILTERED_DCT = filtered_dct(INCIDENTS, ALL_SHORT_DESCRIPTIONS_TO_SKIP)
for i, (incident_num, short_description) in enumerate(FILTERED_DCT.items(), 1):
    print(i, incident_num, short_description)

write_dct_to_csv('incidents_created_by_humans.csv',
                 ['num','short_description'], FILTERED_DCT)

percentage_created_by_humans_formatted = \
format_percentage('percentage_created_by_humans', len(FILTERED_DCT),
                  len(INCIDENTS), 'percentage_created_by_humans_formatted')

print(f'percentage created by humans: {percentage_created_by_humans_formatted}')

print(functions.RTN())
