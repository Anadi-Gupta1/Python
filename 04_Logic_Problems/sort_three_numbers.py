# write a program of 3 integer and arrange in increasing ordder
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))
if a>=b and a>=c:
   if b>=c:
       print("The integers in increasing order are: a>b>c")
   else:
       print("The integers in increasing order are: a>c>b")
elif b>=a and b>=c:
   if a>=c:
       print("The integers in increasing order are: b>a>c")
   else:
       print("The integers in increasing order are: b>c>a")
elif c>=a and c>=b:
   if a>=b:
       print("The integers in increasing order are: c>a>b")
   else:
       print("The integers in increasing order are: c>b>a")