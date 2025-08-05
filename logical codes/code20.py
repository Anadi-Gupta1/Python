#write a program where the number is prime or not
n = int(input("Enter a number to check if it is prime: "))
f = 1
for i in range(2,n):
    if n % i == 0:
        f = 0
        break
if f == 1 :
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")