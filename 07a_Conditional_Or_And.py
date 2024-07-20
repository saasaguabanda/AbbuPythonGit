#example of AND
age = 25
has_license = True
if age >= 18 and has_license:
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")

# example of OR
weather = "rainy"
temperature = 75

if weather == "rainy" or temperature > 80:
    print("It's a good day for an umbrella.")
else:
    print("Enjoy the weather!")