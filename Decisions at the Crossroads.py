# Task 1: Code Correction You are provided with a Python script that uses conditional statements to tell if a number is positive, negative, or zero, but it has some errors. Identify and fix them.

# Buggy Code:

# number = input("Enter a number: ")

# if number > 0:
#    print("The number is positive.")
# elif number = 0:
#    print("The number is zero.")
# else number < 0:
#    print("The number is negative.")

# Convert input to a floating-point number
number = float(input("Enter a number: ")) 

if number > 0:
    print("The number is positive.")

# Use double equals for equality comparison
elif number == 0: 
    print("The number is zero.")

# Correct the syntax for the negative case
else: 
    print("The number is negative.")
