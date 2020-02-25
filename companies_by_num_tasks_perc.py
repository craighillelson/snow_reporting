""" __doc__ """

# imports
import csv
import functions
import re

# data stores
co_per = {}
co_tasks = {}
tasks = {}
companies = []

# open csv
functions.open_csv(companies, tasks)

print(functions.RTN())

# count tasks and populate co_tasks dictionary with results
total_tasks = len(companies)
for company in set(companies):
    num_tasks = companies.count(company)
    co_tasks[company] = num_tasks

# output results
print('companies by percentage of tasks')
for co, num_tasks in sorted(co_tasks.items(), key=lambda x: x[1], reverse=True):
    co_tasks[company] = num_tasks
    per_fmt = functions.format_percentage(num_tasks, total_tasks)
    print(co, num_tasks, per_fmt)
    co_per[co] = per_fmt

print(functions.RTN())

HEADERS = 'company','percentage of all tasks'

with open('companies_by_num_tasks_perc.csv', 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(HEADERS)
    for co, per_fmt in co_per.items():
        keys_values = (co, per_fmt)
        out_csv.writerow(keys_values)

# update user
print('"companies_by_num_tasks_perc.csv" exported successfully')

print(functions.RTN())
