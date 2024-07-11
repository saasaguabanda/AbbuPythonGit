def addtwo(a,b): #a,b are called arguments of the function being defined
    if int(a) > 40:
        pay = (40 * int(b)) + ((int(a) - 40) * (int(b) + 5))
        return pay
    else:
        pay = (int(a)*int(b))
        return pay

a = input('Enter the number of hours you have worked: ')
b = input('Enter the hourly rate (regular): ')

x = addtwo(a,b)
print('Your pay is $',x,' since overtime is $5 more than the regular rate for hours above 40 hours')
