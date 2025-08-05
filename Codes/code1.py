#write a python to calculate the roots of a quadratic equation
import math
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

# Calculate discriminant
discriminant = b*b - 4*a*c

if discriminant > 0:
    r1 = ((-b + math.sqrt(discriminant))/(2*a))
    r2 = ((-b - math.sqrt(discriminant))/(2*a))
    print("The roots of the quadratic equation are: ", r1, "and", r2)
elif discriminant == 0:
    r = -b/(2*a)
    print("The quadratic equation has one repeated root: ", r)
else:
    print("The quadratic equation has no real roots (discriminant is negative)")
