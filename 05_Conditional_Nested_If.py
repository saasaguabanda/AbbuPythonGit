x= input('Enter a number: ')
#indending after the : is critical in Python for conditional (if-then) code
if int(x)<10:
    print('The number you chose is smaller than 10.')
    if int(x)<5:
        print('And it is also less than 5.')
if int(x)>20:
    print('The number you chose is bigger than 20')
    if int(x)>99:
        print('And it is also a tripple digit number')
print('All done')
        
