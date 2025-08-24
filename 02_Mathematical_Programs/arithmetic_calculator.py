# write a program reads two nbmer and arithmetic oopertor and isplay the ocmputed result
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operator = input("Enter the arithmetic operator (+, -, *, /): ")
if operator == "+":
    result = a + b
    print(" the result of addition is ", result)
elif operator == "-":
    result = a - b
    print(" the result of subtraction is ", result)
elif operator == "*":
    result = a * b
    print(" the result of multiplication is ", result)
elif operator == "/":
    result = a/b
    print(" the result of division is ", result)
else:
    print("Invalid operator. Please use +, -, *, or /.")
    