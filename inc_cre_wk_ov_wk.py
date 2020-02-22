""" __doc__ """

import csv

PERC_CHANGE_DCT = {}

# HEADERS = # name headers

def usr_input_date(a, b):
    """ get user input """
    print(a)
    b = input()

    return b


def usr_input_incs(a, b):
    """ get user input """
    print(a)
    b = int(input())

    return b


def fmt_perc():
    """ format percentage """
    perc_change = diff / tix_last_wk * 100
    # print(perc_change)
    perc_change_fmt = '{0:.2f}'.format(perc_change)+'%'

    return perc_change_fmt


def add_to_dct():
    """ """
    PERC_CHANGE_DCT[wk_end_date] = perc_change_fmt


def write_to_csv(name_of_file, HEADERS, dct):
    """ write dictionary to csv """
    with open(name_of_file, "w") as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(HEADERS)
        for k, v in dct.items():
            keys_values = (k, v)
            out_csv.writerow(keys_values)


wk_end_date = usr_input_date('enter week ending date (YYYY-MM-DD)',
                             'wk_end_date')
tix_last_wk = usr_input_incs('how many incidents were created last week?',
                             'tix_last_wk')
tix_this_wk = usr_input_incs('how many incidents were created this week?',
                             'tix_this_wk')

diff = tix_this_wk - tix_last_wk
print('diff:', diff)
if diff < 0:
    perc_change_fmt = fmt_perc()
    add_to_dct()
    print(perc_change_fmt)
else:
    perc_change_fmt = fmt_perc()
    add_to_dct()
    print('+' + perc_change_fmt)

write_to_csv('perc_change_incidents_created_week_over_week.csv',
             ['week','perc_change'], PERC_CHANGE_DCT)

print('"perc_change_incidents_created_week_over_week.csv" exported succesfully')
