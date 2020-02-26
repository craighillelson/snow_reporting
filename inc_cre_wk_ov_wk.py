""" __doc__ """

from datetime import datetime
from datetime import timedelta

weekdays = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
]

RTN = lambda: '\n'

PERC_CHANGE_DCT = {}

def next_fri(dayname, start_date):
    """ """
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date + timedelta(days=days_ago)
    return target_date


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


def fmt_perc(a, b):
    """ format percentage """
    perc_change = a / b * 100
    perc_change_fmt = '{0:.2f}'.format(perc_change)+'%'

    return perc_change_fmt


def add_to_dct(a, b, c):
    """ """
    a[b] = c


def write_to_csv(name_of_file, HEADERS, dct):
    """ write dictionary to csv """

    import csv

    with open(name_of_file, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(HEADERS)
        for k, v in dct.items():
            keys_values = (k, v)
            out_csv.writerow(keys_values)


print(RTN())

wk_end_date = usr_input_date('enter week ending date (YYYY-MM-DD)',
                             'wk_end_date')
tix_last_wk = usr_input_incs('how many incidents were created last week?',
                             'tix_last_wk')
tix_this_wk = usr_input_incs('how many incidents were created this week?',
                             'tix_this_wk')

print(RTN())

diff = tix_this_wk - tix_last_wk
if diff == 0:
    print('no change')
else:
    print('difference:', diff)
    perc_change_fmt = fmt_perc(diff, tix_last_wk)
    add_to_dct(PERC_CHANGE_DCT, wk_end_date, perc_change_fmt)
    print(f'percentage change: {perc_change_fmt}')

write_to_csv('perc_change_incidents_created_week_over_week.csv',
             ['week','perc_change'], PERC_CHANGE_DCT)

print('"perc_change_incidents_created_week_over_week.csv" exported succesfully')

print(RTN())
