hours = input('How many hours did you work? ')
try:
    ans1 = int(hours)
except:
    ans1 = -1
if ans1 > 0:
    rate = input('What is the rate per hour you charge? ')
    try:
        ans2 = int(rate)
    except:
        ans2 = -1
    if ans2 > 0:
        pay = int(hours) * int(rate)
        print('The amount you will get paid is', pay, 'since you worked', hours, 'hours and the rate you charge per hour is', rate) 
    else:
        print('one or more of your values werent numbers. All done')    
else:
    print('one or more of your values werent numbers. All done')
