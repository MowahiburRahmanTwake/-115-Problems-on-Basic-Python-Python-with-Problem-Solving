# Leap Year Checker: Write a Python program that takes a year as input and
# determines if it is a leap year or not.

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 100 != 0) or (year % 4 == 0):
    print(year,"is a leap year")
else:
    print(year, "isn't' leap year")
