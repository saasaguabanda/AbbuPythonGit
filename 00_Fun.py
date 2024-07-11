
name = input('Tell me your name: ')
print('Hello',name)

def guess():
    number = input('Guess which number between 0-10 I want you to enter: ')
    try:
        return int(number) #with the guess function, seems like one has to use the return function to assign the number input by the user to the variable
    except:
        return -1 #with the guess function, seems like one has to use the return function to assign a number to a variable and cannot use number = -1 over here

number = guess()

while number != 8 and number >0:
    print ('Sorry, try again!')
    number = guess()

if number == 8: #need an if here because the while function is checking for both non-8 and non-numbers
    print('That is it! you guessed the correct number!')
else:
    print('What you entered is not a number. Try again')