hours = input('How many hours did you work? ')
rate = input('What is the rate per hour you charge? ')
#int is used below to tell Python to treat the hours variable as an integer and not a string
pay = int(hours) * int(rate)
print('The amount you will get paid is', pay, 'since you worked', hours, 'hours and the rate you charge per hour is', rate)
print('All done')
