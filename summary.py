import codecs
import csv
import statistics
from collections import namedtuple
from datetime import datetime

def format_date(dates):
    """ """
    return datetime.strptime(dates, '%Y-%m-%d %H:%M:%S')


resolve_times = []
resolve_times_under_four_hours = []

with codecs.open('raw_data.csv', 'r', encoding='utf-8', errors='ignore') \
as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        if row.company != "" and row.state == "Closed":
            opened_at = format_date(row.opened_at)
            resolved_at = format_date(row.resolved_at)
            resolve_time = resolved_at - opened_at
            resolve_time_minutes = resolve_time.seconds / 60
            resolve_time_hours = resolve_time_minutes / 60
            resolve_time_days = resolve_time_hours / 1440
            total_resolve_time_days = resolve_time.days + resolve_time_days
            resolve_times.append(total_resolve_time_days)
            if total_resolve_time_days < 1.67:
                resolve_times_under_four_hours.append(row.number)
            else:
                pass

median_resolve_time = statistics.median(resolve_times)
avg_resolve_time = statistics.mean(resolve_times)
min = '{:.8f}'.format(min(resolve_times))
max = '{:.8f}'.format(max(resolve_times))
print('\n')
print('summary')
print(f'average resolve time: {avg_resolve_time}')
print(f'median resolve time: {median_resolve_time}')
print(f'range: {min} - {max}')
print(f'total number of incidents: {len(resolve_times)}')
print(f'number of incidents solved under four hours: '
      f'{len(resolve_times_under_four_hours)}')
perc = float(len(resolve_times_under_four_hours) / len(resolve_times)) * 100
perc_fmt = str('{0:.2f}'.format(perc)+'%')
print(f'percent solved quickly: {perc_fmt}')
print('\n')
