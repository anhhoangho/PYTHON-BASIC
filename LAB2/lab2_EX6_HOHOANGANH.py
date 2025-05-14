seconds = int(input('enter the total number of seconds:'))

days =   int(seconds / 86400)
seconds %= 86400


hours =   int(seconds / 3600)
seconds %= 3600

minutes =  int(seconds / 60)
seconds %= 60

if days != 0:
    print('day(s):',days)
if hours != 0:
    print('hour(s):',hours)
if minutes != 0:
    print('minute(s):',minutes)
if seconds != 0:
    print('second(s):',seconds)