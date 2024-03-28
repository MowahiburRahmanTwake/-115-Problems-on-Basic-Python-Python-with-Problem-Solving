mark = int(input("Enter your mark: "))
if (mark >= 90) & (mark <= 100):
    print("A+")
elif (mark >= 80) & (mark <= 89):
    print("A")
elif (mark >= 70) & (mark <= 79):
    print("B")
elif (mark >= 60) & (mark <= 69):
    print("C")
else:
    print("Fail")
