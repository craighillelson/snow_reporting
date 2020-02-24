""" __doc__ """

RTN = lambda: '\n'

options = {
    'a': 'avg_res_time_days_dec.py',
    'b': 'inc_cre_wk_ov_wk.py',
    'c': 'companies_by_num_tasks_perc.py',
    'd': 'empty_account.py',
    'e': 'mult_short_desc.py',
    'f': 'search_for_term.py',
}

def switch_case(a, b):
    """ switch case statement """
    a
    return a.get(b, 'nothing')


def open_file(a):
    """ """
    exec(open(a).read())


print(RTN())

print('a - calculate average resolution time in days')
print('b - % change in incidents created week over week')
print('c - companies by number of incidents created')
print('d - find incidents where account is empty')
print('e - mult short descriptions')
print('f - search for term')

while True:
    usr_choice = str(input())
    open_file(switch_case(options, usr_choice))
    break
