""" __doc__ """

import csv
import functions
from collections import namedtuple

MINS_DAY = 24 * 60

DCT = {}

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
        total_days_formatted = '{0:.2f}'.format(total_days)
        DCT[row.company] = total_days_formatted

print(functions.RTN())

print('client, average resolution time in days ytd')
for client, average_resolution_time_ytd in DCT.items():
    print(f'{client} {average_resolution_time_ytd}')

print(functions.RTN())

with open('clients_average_resolution_times_in_days.csv', 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(['client', 'average resolution time in days ytd'])
    for client, average_resolution_time_ytd in DCT.items():
        keys_values = (client, average_resolution_time_ytd)
        out_csv.writerow(keys_values)

print('"clients_average_resolution_times_in_days.csv" exported successfully')

print(functions.RTN())
