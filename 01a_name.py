#more on the print function
# In Python, both single quotes (') and double quotes (") can be used to define string literals (text data). However, there are a few subtle differences and use cases where one might be preferred over the other
# Double quotes allow embedding of both single quotes (') and double quotes (") within the string without needing to escape them. This can improve readability when your string contains these characters naturally
# the \ tells python to not consider the immediately following " as a close or open " operation
# Many Python programmers favor using single quotes for strings unless they need to embed double quotes within the string itself
print("Those are Bob's tools")

#using the \ backslash parameter tells python that the character following it should not be considered the end of the "
print('Those are Bob\'s tools')
print("You are not my \"friend\"")
print('You are not my "friend"')#alternate to using \

#, vs +
name = input('Tell me your name: ')
print("hello,",name) #with a , a space is auto added after the ,
print("hello, " + name) #using concatinate so space has to be added prior to "

#end- to override a line break at the end of the print funcation
print("How")#without the end="" (see below) the print function 
print("d")
print("how ", end="")#adding the end="" results in overriding the default next line feature of print
print("d")

# strip off spaces from the input (just before the first character) and capitalize using string functions .strip .capitalize .title
name = name.strip().capitalize() #.strips to remove spaces and .capitalize to capitalize
print("Hello,",name)
name = name.title()# capitalize not just the first word but all words
print("Hello,",name)

#another way to use a variable in the print function
name = input('Tell me your name: ').strip().title()# can add the .strip and .title string funcations into this line itself
print(f"Hello, {name}") #adding f string at the start and then {variable} useful when putting additional constraints (see in subsequent files)

#if the user enters both first and last name and you want to greet using just first name
first, last = name.split(" ")
print("Hello,",first)