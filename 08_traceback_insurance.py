#try-except framework to avoid a traceback error if the user enteres an inappropriate response like a word instead of a number
#use traceback only for the specific line at risk due to the potential bad response by the user. Do not use it for other parts of the code otherwise bugs will remain in the code

number=input('enter a number')
try:
    answr=int(number)
except:
    #will be applicable only if there is a traceback error 
    answr=-1
if answr>0:
    print('nice work')
else:
    print('not a number')
