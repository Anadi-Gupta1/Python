# write a program to reverse a given number
n = int(input("Enter a number to reverse: "))
rev = 0
while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n //= 10
print(f"The reversed number is: {rev}")


