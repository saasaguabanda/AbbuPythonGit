number = input('Guess which number between 0-10 I want you to enter: ')
try:
    ans1 = int(number)
except:
    ans1 = -1
if ans1 > 0:
    while int(number) != 8:
        print ('Sorry, try again!')
        number = input('Guess which number between 0-10 I want you to enter: ')
    print('That it is! 8 is the number!')
else:
    print('What you entered is not a number. Bye')

