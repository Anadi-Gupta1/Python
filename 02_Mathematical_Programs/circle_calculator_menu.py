# write a program to create a menu to caluclutae are of a cirlce and perimeter of a circle
print("Menu:")
print("1. Calculate Area of Circle")
print("2. Calculate Perimeter of Circle")
choice = int(input("enter your choice 1 or 2:  "))
radius = float(input("Enter the radius of the circle: "))
if choice == 1:
    area = 3.14 * radius * radius
    print("The area of the circle is:", area)
elif choice == 2:
    perimeter = 2 * 3.14 * radius
    print("The perimeter of the circle is:", perimeter)