''' It is iteration statement and what are the two kind of loop which are used in the python'''
# In Python, there are two main types of loops used for iteration:
# 1. **for loop**: Used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.
# 2. **while loop**: Repeats a block of code as long as a specified condition is true.      
## Example of a for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")    
## Example of a while loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1  # Increment the count to avoid an infinite loop 
# Example of a for loop with range
for i in range(5):
    print(f"Iteration {i}")
# Example of a while loop with a condition
n = 0
while n < 3:
    print(f"n is {n}")
    n += 1  # Increment n to avoid an infinite loop
# Example of a for loop with a string
for char in "hello":
    print(f"Character: {char}")
# Example of a while loop with user input
user
_input = ""
while user_input.lower() != "exit":
    user_input = input("Type 'exit' to stop: ")
    print(f"You typed: {user_input}")
# Example of a for loop with a list of numbers
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(f"Number: {number}")
# Example of a while loop with a countdown



# steps for looop execution
# 1. Initialize a variable (e.g., `i = 0`).
# 2. Check the loop condition (e.g., `i < 5`).
# 3. If the condition is true, execute the loop body (e.g., `print(i)`).
# 4. Increment the variable (e.g., `i += 1`).
# 5. Repeat steps 2-4 until the condition is false.
countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1  # Decrement countdown to avoid an infinite loop
# Example of a for loop with a range and step
for i in range(0, 10, 2):  # Step of 2
    print(f"Even number: {i}")


    #explain range function
# The `range()` function in Python generates a sequence of numbers. It can take one, two, or three arguments:
# 1. **`range(stop)`**: Generates numbers from 0 to `stop - 1`.
# 2. **`range(start, stop)`**: Generates numbers from `start` to `stop - 1`.
# 3. **`range(start, stop, step)`**: Generates numbers from `start` to `stop - 1`, incrementing by `step`.
# Example of range with one argument
for i in range(5):  # Generates 0, 1, 2, 3, 4
    print(f"Number: {i}")
# Example of range with two arguments
for i in range(2, 6):  # Generates 2, 3, 4, 5
    print(f"Number: {i}")

# Example of range with three arguments
for i in range(1, 10, 2):  # Generates 1, 3, 5, 7, 9
    print(f"Odd number: {i}")
    