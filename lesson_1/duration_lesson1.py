duration = int(input(' enter duration in seconds: '))

if duration > 0:
    days = duration // 86400
    hours = duration // 3600 % 24
    minutes = duration // 60 % 60
    seconds = duration % 60
    print(days, 'day(-s)', hours, 'hour(-s)', minutes, 'minute(-s)', seconds, 'second(-s)')
else:
    print('the value = 0, please restart')



duration = [1258558, 85256, 88524, 856854, 85855]

for sec in duration:
    if sec > 0:
        days = sec // 86400
        hours = sec // 3600 % 24
        minutes = sec // 60 % 60
        seconds = sec % 60
        print(sec, 'seconds')
        print(days, 'day(-s)', hours, 'hour(-s)', minutes, 'minute(-s)', seconds, 'second(-s)')
    else:
        print('the value = 0, please restart')
