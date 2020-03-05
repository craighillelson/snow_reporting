""" __doc__ """

RTN = lambda: '\n'

def format_percentage(a, b, c, d):
    """ formats float as a percentage to the second decimal """
    a = b / c * 100
    d = '{0:.2f}'.format(a)+'%'

    return d


def open_csv():
    """
    open a csv and populate the list short_descriptions_to_skip with its
    contents
    """
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


def concat_lists(lst1, lst2, concatenated_list):
    """ concatenate lists """
    concatenated_list = lst1 + lst2
    return concatenated_list


def filter_dct():
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


def finalize_dct():
    """ return an enumerated dictionary containing filtered incidents """
    finalized_dct = {}

    for num, (incident_num, short_description) in enumerate(filtered_dct.items(), 1):
        check = any(item in short_description for item in \
                    all_short_descriptions_to_skip)
        if check is True:
            pass
        else:
            finalized_dct[incident_num] = short_description

    return finalized_dct


def output_enum_dct():
    """
    output the enumerated dictionary containing only those incidents that
    do not
    include strings in short_descriptions_to_skip.csv
    """
    for num, (incident_num, short_description) in \
              enumerate(finalized_dct.items(), 1):
        print(num, incident_num, short_description)


short_descriptions_to_skip = open_csv()
short_descriptions_to_add = prompt_user()
all_short_descriptions_to_skip = concat_lists(short_descriptions_to_skip,
                                              short_descriptions_to_add,
                                              'all_short_descriptions_to_skip')

write_to_csv(all_short_descriptions_to_skip)
filtered_dct = filter_dct()
finalized_dct = finalize_dct()
output_enum_dct()
print(RTN())

total_incs = len(filtered_dct)
human_created_incs = len(finalized_dct)

print(f'total incidents: {total_incs}')
print(f'incidents created by humans: {human_created_incs}')

perc_human_created_fmt = format_percentage('perc_human_created',
                                           human_created_incs, total_incs,
                                           'perc_human_created_fmt')
print(perc_human_created_fmt)
print(RTN())
