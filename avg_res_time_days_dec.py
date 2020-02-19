""" __doc__ """

mins_hr = 60
mins_day = 24 * 60

client_res_time = {}

RTN = lambda: '\n'

print(RTN())

while True:
    print('client name (blank to quit)')
    client = input()
    if client == '':
        break
    print('how many days')
    days = int(input())
    print('how many hours')
    hrs = int(input())
    if hrs > 24:
        hrs = int(input('please enter a number less than 24\n'))
    else:
        pass
    print('how many minutes')
    mins = int(input())
    if mins > 60:
        mins = int(input('please enter a number less than 60\n'))
    else:
        pass
    tot_mins = hrs * mins_hr + mins
    mins_dec = (hrs * mins_hr + mins) / mins_day
    mins_dec_fmt = float('{0:.2f}'.format(mins_dec))
    days_dec = days + mins_dec_fmt
    client_res_time[client] = days_dec

print('client - resolve time (days)')
for client, res_time in client_res_time.items():
    print(f'{client} {res_time} days')

print(RTN())
