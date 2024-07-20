#counting in a loop
#if function in a loop; in this eg to compute largest number
#summing in a loop
#finding the average

largest_so_far = 0
count = 0
sum = 0

print('Starting',largest_so_far)

for number in (4,2,123,15,634,66,7):
    count = count + 1
    sum = sum + number
    if number > largest_so_far:
        largest_so_far = number
    print(count,':',largest_so_far,number,number + largest_so_far)
print('End','Largest is:',largest_so_far,'Average is:',int(sum/count))

print('')
print('New section below')
for value in (341,143,666,77,23432):
    if value >500:
        print ('Numbers >500 are: ',value)
        

#search using a Boolean Variable
print('')
print('New section below')
found = False
print('before',found)
for value in (5,7,6,8,1,2):
    if value == 8:
        found = True
    print(found,value)
print('After',found)


print('')
print('New section below')

