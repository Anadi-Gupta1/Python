''' what is precedence of operator in python?
Precedence of operators in Python determines the order in which operations are evaluated in expressions.
Operators with higher precedence are evaluated before those with lower precedence.
Common operator precedence in Python (from highest to lowest):
1. Parentheses `()`
2. Exponentiation `**`  
3. Unary plus and minus `+`, `-`
4. Multiplication, Division, Floor Division, Modulus `*`, `/`, `//`, `%`
5. Addition and Subtraction `+`, `-`
6. Bitwise Shift `<<`, `>>`
7. Bitwise AND `&`
8. Bitwise XOR `^`
    9. Bitwise OR `|`
    10. Comparison Operators `==`, `!=`, `<`, `>`, `<=`, `>=`
    11. Assignment Operators `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=` etc.
    12. Logical Operators `and`, `or`, `not`
    Example of operator precedence in Python
        
        a = 10
        b = 5
        c = 2
        result = a + b * c  # Multiplication has higher precedence than addition
        print(result)  # Output: 20 (5 * 2 = 10, then 10 + 10 = 20)
        result = (a + b) * c  # Parentheses change the precedence
        print(result)  # Output: 30 ((10 + 5) * 2 = 30)
        # Example of operator precedence with different operators
        # Using exponentiation and multiplication
        # Exponentiation has higher precedence than multiplication
        # Example of operator precedence with different operators
        # Using exponentiation and multiplication
        # Exponentiation has higher precedence than multiplication
        # Example of operator precedence with different operators
        # Using exponentiation and multiplication
        # Exponentiation has higher precedence than multiplication
        # Example of operator precedence with different operators
        # Using exponentiation and multiplication
        # Exponentiation has higher precedence than multiplication
        # Example of operator precedence with different operators
        # '''


# what is expressions and statement in python?
# Expressions are combinations of values and operators that evaluate to a value.
# Statements are instructions that perform an action.
# Example of expressions and statements in Python

a = 10  # This is a statement
b = 20  # This is another statement
c = a + b  # This is an expression that evaluates to 30
print(c)  # This is a statement that prints the value of c
# Example of expressions and statements in Python
x = 5  # This is a statement
y = 10  # This is another statement
z = x * y  # This is an expression that evaluates to 50
print(z)  # This is a statement that prints the value of z
# Example of expressions and statements in Python
d = 15  # This is a statement
e = 25  # This is another statement
f = d - e  # This is an expression that evaluates to -10
print(f)  # This is a statement that prints the value of f
