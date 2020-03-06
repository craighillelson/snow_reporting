""" __doc__ """

import csv
import functions

def usr_input_date(a):
    """ get user input """
    print(a)
    a = input()

    return a


def usr_input_incs(a):
    """ get user input """
    print(a)
    a = int(input())

    return a


def fmt_perc(a, b, c):
    """ format percentage """
    perc_change = a / b * 100
    c = '{0:.2f}'.format(perc_change)+'%'

    return c


def add_to_dct(a, b, c):
    """ add to dictionary """
    a[b] = c

    return a


def write_to_csv(name_of_file, HEADERS, dct):
    """ write dictionary to csv """
    import csv

    with open(name_of_file, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(HEADERS)
        for k, v in dct.items():
            keys_values = (k, v)
            out_csv.writerow(keys_values)


print(functions.RTN())
wk_end_date = usr_input_date('enter week ending date (YYYY-MM-DD)')

print(functions.RTN())
tix_last_wk = usr_input_incs('how many incidents were created last week?')

print(functions.RTN())
tix_this_wk = usr_input_incs('how many incidents were created this week?')
print(functions.RTN())

diff = tix_this_wk - tix_last_wk
print(f'difference: {diff}')
PERC_CHANGE_DCT = {}
if diff < 0:
    perc_change_fmt = fmt_perc(diff, tix_last_wk, 'perc_change_fmt')
    print(f'percentage change: {perc_change_fmt}')
    add_to_dct(PERC_CHANGE_DCT, wk_end_date, perc_change_fmt)
else:
    perc_change_fmt = fmt_perc(diff, tix_last_wk, 'perc_change_fmt')
    perc_change_fmt = '+' + perc_change_fmt
    print(f'percentage change: {perc_change_fmt}')
    add_to_dct(PERC_CHANGE_DCT, wk_end_date, perc_change_fmt)

print(functions.RTN())

write_to_csv('perc_change_incidents_created_week_over_week.csv',
             ['week','perc_change'], PERC_CHANGE_DCT)

print('"perc_change_incidents_created_week_over_week.csv" exported succesfully')

print(functions.RTN())
