""" __doc__ """

RTN = lambda: '\n'

options = {
    'a': 'avg_res_time_days_dec.py',
    'b': 'companies_by_num_tasks_perc.py',
    'c': 'empty_account.py',
    'd': 'mult_short_desc.py',
    'e': 'search_for_term.py',
}

def switch_case(a, b):
    """ switch case statement """
    a
    return a.get(b, 'nothing')


def open_file(a):
    """ """
    exec(open(a).read())

print('a - average resolution time in days')
print('b - companies by number of incidents created')
print('c - find incidents where account is empty')
print('d - mult short descriptions')
print('e - search for term')

while True:
    usr_choice = input()
    open_file(switch_case(options, usr_choice))
    break
