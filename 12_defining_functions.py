def guess():
    number = input('Guess which number between 0-10 I want you to enter: ')
    return int(number) #with the guess function, one has to use the return function to assign the number input by the user to the variable

number = guess()

while int(number) != 8:
    print ('Sorry, try again!')
    number = guess()
print('That is it! you guessed the correct number!')

#this has a traceback error if the user does not entere a number
