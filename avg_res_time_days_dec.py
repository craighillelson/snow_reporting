""" __doc__ """

print('how many days')
days = int(input())

print('how many hours')
hrs = int(input())

print('how many minutes')
mins = int(input())

print('\n')

print(f'{days} days {hrs} hours {mins} minutes')

mins_hr = 60
mins_day = 24 * 60
print(f'minutes per day: {mins_day}')
tot_mins = hrs * mins_hr + mins
print(f'total minutes: {tot_mins}')
print('\n')

mins_dec = (hrs * mins_hr + mins) / mins_day
mins_dec_fmt = float('{0:.2f}'.format(mins_dec))
print(f'percentage of a day: {mins_dec_fmt}')
print('\n')

days_dec = days + mins_dec_fmt
print(f'days plus minutes as percentage of a day {days_dec}')

print('\n')
