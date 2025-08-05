''' what is error and what are the types of errors which are found out"
# Error handling in Python is the process of responding to and managing errors that occur during program execution.
# It involves identifying, diagnosing, and resolving errors to ensure the program runs smoothly.
# Types of errors in Python:
# 1. Syntax Errors: These occur when the code is not written correctly, such as missing colons, parentheses, or indentation.
# 2. Runtime Errors: These occur during program execution, such as division by zero or accessing an undefined variable.
# 3. Logical Errors: These occur when the code runs without crashing but produces incorrect results.
# 4. Indentation Errors: These occur when the code is not properly indented, which is crucial in Python.
# 5. Import Errors: These occur when a module or package cannot be imported, often due to a missing or incorrect import statement.
# 6. Type Errors: These occur when an operation is performed on an object of an inappropriate type, such as trying to concatenate a string and an integer.  
# 7. Value Errors: These occur when a function receives an argument of the right type but an inappropriate value, such as passing a negative number to a function that expects a positive number.
# 8. Semantic Errors: These occur when the code is syntactically correct but does not do what the programmer intended, such as using the wrong variable or function.
#
#  Example of error handling in Python
# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     result = a / b
#     print("The result is:", result)
# except ZeroDivisionError:
#   print("Error: Division by zero is not allowed.")
# except ValueError:
#  print("Error: Invalid input. Please enter a valid number.")
# try:
#    a = int(input("Enter a number: "))
#   b = int(input("Enter another number: "))
#   result = a / b
# print("The result is:", result)
#'''


# what is debugging in Python?
# Debugging in Python is the process of identifying and fixing errors or bugs in the code.
# It involves using various tools and techniques to trace the execution of the program, inspect variables,
# and analyze the flow of control to find and resolve issues.
# Common debugging techniques in Python:
# 1. Print Statements: Inserting print statements in the code to display variable values and
# the flow of execution at different points.
# 2. Using a Debugger: Python provides built-in debuggers like pdb (Python Debugger) that allow you to step through the code,
# set breakpoints, and inspect variables interactively.
# 3. Logging: Using the logging module to log messages at different levels (debug, info, warning, error) to track the program's behavior.
# 4. Exception Handling: Using try-except blocks to catch and handle exceptions gracefully,
