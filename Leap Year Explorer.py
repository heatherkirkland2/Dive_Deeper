# Task 1: Leap Year Checker Write a Python program that prompts the user to input a year. The program should determine if the given year is a leap year or not and then display an appropriate message. Please note that this is the definition of a leap year: Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.

# Expected Outcome: If you test the year 1900, is should be False. The year 2000 should be True. The year 2024 should be True

def is_leap_year(year):
    # Check if the year is a leap year
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False

# Prompt the user to input a year
input_year = int(input("Enter a year to check if it's a leap year: "))

# Display an appropriate message
if is_leap_year(input_year):
    print(f"The year {input_year} is a leap year.")
else:
    print(f"The year {input_year} is not a leap year.")

# Test cases
# print(is_leap_year(1900))  # Expected Output: False
# print(is_leap_year(2000))  # Expected Output: True
# print(is_leap_year(2024))  # Expected Output: True
