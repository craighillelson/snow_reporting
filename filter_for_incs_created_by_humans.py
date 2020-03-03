""" __doc__ """

def open_csv():
    """ """
    import csv
    from collections import namedtuple

    short_descriptions_to_skip = []

    with open('short_descriptions_to_skip.csv') as csv_file:
        F_CSV = csv.reader(csv_file)
        COLUMN_HEADINGS = next(F_CSV)
        CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
        for rows in F_CSV:
            row = CSV_ROW(*rows)
            short_descriptions_to_skip.append(row.short_descriptions)

    return short_descriptions_to_skip


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


def write_to_csv(a):
    """ write results to a csv """
    import csv

    with open('short_descriptions_to_skip.csv', 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(['short_descriptions'])
        for i in a:
            out_csv.writerow([i])


def concat_lists(a, b, c):
    """ """
    c = a + b
    return c


def filter_dct():
    """ """
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


def finalize_dct():
    """ """
    finalized_dct = {}

    for i, (k, v) in enumerate(filtered_dct.items(), 1):
        check = any(item in v for item in all_short_descriptions_to_skip)
        if check is True:
            pass
        else:
            finalized_dct[k] = v

    return finalized_dct


def output_enum_dct():
    """ """
    for i, (k, v) in enumerate(finalized_dct.items(), 1):
        print(i, k, v)


short_descriptions_to_skip = open_csv()
short_descriptions_to_add = prompt_user()
all_short_descriptions_to_skip = concat_lists(short_descriptions_to_skip,
                                              short_descriptions_to_add,
                                              'all_short_descriptions_to_skip')

write_to_csv(all_short_descriptions_to_skip)
filtered_dct = filter_dct()
finalized_dct = finalize_dct()
output_enum_dct()

print('\n')
total_incs = len(filtered_dct)
human_created_incs = len(finalized_dct)
print(f'total incidents: {total_incs}')
print(f'incidents created by humans: {human_created_incs}')
perc_human_created = human_created_incs / total_incs * 100
perc_human_created_fmt = '{0:.2f}'.format(perc_human_created)+'%'
print(perc_human_created_fmt)
print('\n')
