# what is decision making statement?
# Decision making statements in Python allow you to execute certain blocks of code based on specific conditions.
# The most common decision making statements are:
# 1. if statement
# 2. if-else statement
# 3. if-elif-else statement
# 4. nested if statement
# 5. switch-case statement (not natively supported in Python, but can be simulated using dictionaries or if-elif-else)
# Example of if statement
a = 10
if a > 5:
    print("a is greater than 5")
# Example of if-else statement
b = 3
if b > 5:
    print("b is greater than 5")
else:
    print("b is not greater than 5")
# Example of if-elif-else statement
c = 7
if c > 10:
    print("c is greater than 10")
elif c > 5:
    print("c is greater than 5 but less than or equal to 10")
elif c > 0:
    print("c is greater than 0 but less than or equal to 5")
elif c == 0:
    print("c is equal to 0")
else:
    print("c is negative")

# Example of nested if statement
d = 15
if d > 10:
    print("d is greater than 10")
    if d > 20:
        print("d is also greater than 20")
    else:
        print("d is not greater than 20")

# Note: Python does not have a built-in switch-case statement, but you can use dictionaries or if-elif-else statements to achieve similar functionality

