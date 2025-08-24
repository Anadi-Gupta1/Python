# write a program to calculate the sum of digits of a given number
n = int(input("Enter a number to calculate the sum of its digits: "))
sum = 0
while n > 0:
    r = n % 10
    sum += r
    n = n // 10
    print(f"The sum of the digits is: {sum}")