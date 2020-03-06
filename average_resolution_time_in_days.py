""" __doc__ """

import csv
import functions
from collections import namedtuple

MINS_DAY = 24 * 60

COMPANIES_RESOLUTION_TIMES = {}

with open('clients_resolution_times.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        days = int(row.days)
        hours = int(row.hours)
        minutes = int(row.minutes)
        hours_in_minutes = hours * 60
        days_fraction = (hours_in_minutes + minutes) / MINS_DAY
        total_days = days + days_fraction
        total_days_formatted = functions.format_days(total_days,
                                                     'total_days_formatted')
        COMPANIES_RESOLUTION_TIMES[row.company] = float(total_days_formatted)

print(functions.RTN())

print('client, average resolution time in days ytd')
for client, average_resolution_time_ytd in COMPANIES_RESOLUTION_TIMES.items():
    if average_resolution_time_ytd > 3:
        above_goal = average_resolution_time_ytd - 3
        above_goal_formatted = functions.format_days(above_goal,
                                                     'above_goal_formatted')
        print(f'{client} {average_resolution_time_ytd} - '
              f'{above_goal_formatted} days above goal')
    elif average_resolution_time_ytd == 3:
        print(f'{client} {average_resolution_time_ytd} - at goal')
    else:
        print(f'{client} {average_resolution_time_ytd} - under goal')

print(functions.RTN())

with open('clients_average_resolution_times_in_days.csv', 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(['client', 'average resolution time in days ytd'])
    for client, average_resolution_time_ytd in \
    COMPANIES_RESOLUTION_TIMES.items():
        keys_values = (client, average_resolution_time_ytd)
        out_csv.writerow(keys_values)

print('"clients_average_resolution_times_in_days.csv" exported successfully')

print(functions.RTN())
