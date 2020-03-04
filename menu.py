""" __doc__ """

RTN = lambda: '\n'

options = {
    'a': 'average_resolution_time_in_days.py',
    'b': 'incidents_created_week_over_week.py',
    'c': 'companies_by_number_of_tasks_and_percentage.py',
    'd': 'empty_account.py',
    'e': 'group_incidents_by_company_count_unique_short_descriptions.py',
    'f': 'search_for_term.py',
    'g': 'filter_out_incidents_not_created_by_humans.py'
}

def switch_case(a, b):
    """ switch case statement """
    a
    return a.get(b, 'nothing')


def open_file(a):
    """ open a Python script """
    exec(open(a).read())


print('a - average resolution time in days')
print('b - % change in incidents created week over week')
print('c - companies by number of incidents created')
print('d - find incidents where company is empty')
print('e - group incidents by company count unique short descriptions')
print('f - search for number of occurances of a term')
print('g - filter out incidents not created by humans')

while True:
    usr_choice = input()
    open_file(switch_case(options, usr_choice))
    break
