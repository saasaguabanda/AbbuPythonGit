# is opeator means 'is the same as'
# is operator is similar to, but stronger than ==
# 'is not' is the opposite of 'is'

smallest = None #signals the absence of a meaningful value; used as a default placeholder
for value in (3,54,67,2,1,55):
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print (smallest,value)
print('After',smallest)
