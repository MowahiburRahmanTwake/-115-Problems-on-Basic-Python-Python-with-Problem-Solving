slide1 = float(input("Enter the slide1: "))
slide2 = float(input("Enter the slide2: "))
slide3 = float(input("Enter the slide3: "))

if slide1 == slide2 == slide3:
    print("Equilateral")
elif slide1 == slide2 or slide2 == slide3 or slide3 == slide1:
    print("Isosceles")
else:
    print("Scalene")