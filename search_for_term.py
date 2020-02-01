""" __doc__ """

# imports
import csv
import functions
import list
import re

# for term in list.terms:
#     print(term)

print(functions.RTN())

# data stores
results_dct = {}
tasks = {}
companies = []
results_lst = []
incs_reqs = []
terms = []

functions.open_csv(companies, tasks)
num_tasks = functions.total_tasks(companies)

# prompt user
# while True:
print('Enter the term you\'d like to search for ') #+
         # '(Or enter nothing to stop.):')
term = input()
term_dct = term.lower() + '_dct'
term_dct = {}
term_csv = term.lower() + '.csv'
# if term == '':
#     break
terms = terms + [term]

print(functions.RTN())

# for term in search_terms:
print(f'results for: {term}')
for num, details in tasks.items():
    co = details[0]
    short_desc = details[1]
    if term in short_desc.lower():
        results_lst.append(term)
        term_dct[num] = [co, short_desc]

if len(results_lst) > 0:
    (f'{len(results_lst)} results found')
    print(functions.RTN())
    for i, (inc, details) in enumerate(term_dct.items(), 1):
        co = details[0]
        short_desc = details[1]
        incs_reqs.append(co)
else:
    print('no results found')

# print(functions.RTN())

# output results
print(f'tasks total: {num_tasks}')
total_incs_reqs = len(incs_reqs)
perc_of_total = total_incs_reqs / num_tasks * 100
perc_of_total_fmt = '{0:.2f}'.format(perc_of_total)+'%'
print(f'percentage of total: {perc_of_total_fmt}')
print(functions.RTN())
print(f'total incidents and requests containing {term}: {total_incs_reqs}')
# print(functions.RTN())

print(f'percentage of incidents containing search term "{term}" by company')
for co in set(incs_reqs):
    num_incs_reqs = incs_reqs.count(co)
    per_fmt = functions.format_percentage(num_incs_reqs, total_incs_reqs)
    # print(f'{co} - {num_incs_reqs} - {per_fmt}')
    results_dct[co] = num_incs_reqs, per_fmt

for co, stat in sorted(results_dct.items(), key=lambda x: x[1],
                           reverse=True):
    print(co, stat[1])

print(functions.RTN())

# write results to csv
HEADERS = '','company','number','short_description'

with open(term_csv, 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(HEADERS)
    for i, (k, v) in enumerate(term_dct.items(), 1):
        keys_values = (i, v[0], k, v[1])
        out_csv.writerow(keys_values)

# update user
print(f'"{term_csv}" exported successfully')

print(functions.RTN())
