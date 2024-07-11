#user input, even if a number, is assumed to be a string by python
#as such, have to convert the user input to an integer before it can be used as a number by python
x = input("what is x? ")
y = input("what is y? ")
z = round((int(x)/int(y)),5)#round to 2 digits
print(z)

#add commas to 4+ digit numbers
print(f"{z}") #f tells python to look out for a {} that has a parameter (this line will do the same as print(z))
print(f"{z:,}") #f and a :, to tell it use a , for thousands

#using the f to round instead of the round function
z=int(x) / int(y)
print(f"{z:.2f}") #line 14 and 5 result in the same output (z = round((int(x)/int(y)),5)#round to 2 digits)
