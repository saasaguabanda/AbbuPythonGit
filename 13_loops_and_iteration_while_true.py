#while vs while True
#The while loop executes a block of code repeatedly as long as a specified condition remains True. When the condition becomes False, the loop terminates.
#The while True loop creates an infinite loop. Since the condition True is always met, the code block within the loop keeps executing repeatedly unless terminated by other means.

while True:
    line = input('Enter the magic word or "done" if you want to end ')
    if line[0] == '#':
        continue #this ends the current iteration of the loop and jumps to the top of the loop - to the while
    if line == 'done':
        break #this ends the current loop and jumps to the statement immediately following the loop
    print('Try again ',line,' is not the magic word')
print('Done!')
