def guess():
    number = input('Guess which number between 0-10 I want you to enter: ')
    try:
        return int(number) #with the guess function, seems like one has to use the return function to assign the number input by the user to the variable
    except:
        return -1 #with the guess function, seems like one has to use the return function to assign a number to a variable and cannot use number = -1 over here

number = guess()

if number > 0:
    while number != 8:
        print ('Sorry, try again!')
        number = guess()
    print('That is it! you guessed the correct number!')
else:
    print('What you entered is not a number. Bye')

#this does not capture the post-first round error of the user entering a non-number as the if function runs only the first time
#this happens because, given that the defined function is called within the while function, the if function does not trigger/ gets bypassed after the while function is triggered
