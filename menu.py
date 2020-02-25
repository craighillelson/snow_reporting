""" __doc__ """

from datetime import datetime
from datetime import timedelta

RTN = lambda: '\n'

weekdays = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
]

options = {
    'a': 'avg_res_time_days_dec.py',
    'b': 'deltas_weekly.py',
    'c': 'deltas_spec_dates.py',
    'd': 'companies_by_num_tasks_perc.py',
    # 'd': 'empty_account.py',
    # 'e': 'mult_short_desc.py',
    # 'f': 'search_for_term.py',
    # 'g': 'next_fri.py',
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
print('d - companies by number of incidents created')
# print('e - find incidents where account is empty')
# print('f - mult short descriptions')
# print('g - search for term')

usr_choice = str(input())

while True:
    if usr_choice == '':
        break
    else:
        open_file(switch_case(options, usr_choice))
        break
