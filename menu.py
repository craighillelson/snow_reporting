""" __doc__ """

from datetime import datetime
from datetime import timedelta

RTN = lambda: '\n'

# weekdays = [
#     'Monday',
#     'Tuesday',
#     'Wednesday',
#     'Thursday',
#     'Friday',
#     'Saturday',
#     'Sunday',
# ]

options = {
    'a': 'avg_res_time_days_dec.py', # works off user input
    'b': 'deltas_weekly.py', # works off incs_cre_wkly.csv
    'c': 'deltas_spec_dates.py', # works off incs_cre_wkly.csv
    'd': 'num_perc_incs_by_co.py', # works off raw_data.csv
    'e': 'mult_short_desc.py',
    # 'f': 'empty_account.py',
    # 'g': 'mult_short_desc.py',
    # 'h': 'search_for_term.py',
    # 'i': 'next_fri.py',
}

def switch_case(a, b):
    """ switch case statement """
    a
    return a.get(b, 'nothing')


def open_file(a):
    """ """
    exec(open(a).read())


print(RTN())

print('please make a selection from the options below or \'enter\' to quit')
print('a - calculate average resolution time in days')
print('b - % change in incidents created week over week')
print('c - % change in incidents created between two dates')
print('d - companies by number and percentage of incidents created')
print('e - occurances of short descriptions by account ytd')
# print('f - find incidents where account is empty')
# print('g - mult short descriptions')
# print('h - search for term')
# print('i - assemble report')

usr_choice = str(input())

while True:
    if usr_choice == '':
        break
    else:
        open_file(switch_case(options, usr_choice))
        break
