year = raw_input()
month = raw_input()
date = raw_input()

if year % 400 ==0:
    leap_year=True
elif year % 100 ==0:
    leap_year = False
elif year % 4 == 0:
    leap_year = True
else:
    leap_year = False
month

