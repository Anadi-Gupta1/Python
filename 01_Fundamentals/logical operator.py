# what is logical operator ?
# Logical operators are used to combine conditional statements.
# They return a boolean value (True or False) based on the evaluation of the conditions.
# Common logical operators include:
# - and: Returns True if both conditions are True
# - or: Returns True if at least one condition is True
# - not: Returns True if the condition is False
# Example of logical operators in Python
a = True
b = False
# Using 'and' operator
if a and b:
    print("Both a and b are True")
else:
    print("Either a or b is False")
# Using 'or' operator
if a or b:
    print("At least one of a or b is True")
else:
    print("Both a and b are False")
# Using 'not' operator
if not a:
    print("a is False")
else:
    print("a is True")
# Example of logical operators with variables
x = 5
y = 10
# Check if x is greater than 0 and y is less than 20
if x > 0 and y < 20:
    print("x is greater than 0 and y is less than 20")
else:
    print("Either x is not greater than 0 or y is not less than 20")
# Check if x is less than 10 or y is greater than 5
if x < 10 or y > 5:
    print("Either x is less than 10 or y is greater than 5")
else:
    print("x is not less than 10 and y is not greater than 5")
# Check if x is not equal to 5
if not x == 5:
    print("x is not equal to 5")
    