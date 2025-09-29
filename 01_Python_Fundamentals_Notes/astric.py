"""
Python Operators and Shortcut Functions - Learning Notes
======================================================

This module demonstrates various Python operators, especially the asterisk (*) 
operator and its multiple uses, along with shortcut assignment operations.

Author: Python Learning Notes
Date: September 2025
Topic: Python Operators, Shortcut Functions, Asterisk Usage
"""

# =============================================================================
# UNDERSTANDING THE ASTERISK (*) OPERATOR IN PYTHON
# =============================================================================

def introduce_asterisk_operator():
    """
    The asterisk (*) is a versatile operator in Python with multiple uses
    """
    print("⭐ THE ASTERISK (*) OPERATOR IN PYTHON")
    print("=" * 40)
    
    print("\n🔍 Multiple Uses of Asterisk (*):")
    print("   1️⃣ Multiplication operator")
    print("   2️⃣ Exponentiation (**) - power operator")
    print("   3️⃣ Repetition operator (for sequences)")
    print("   4️⃣ Unpacking operator (advanced)")
    print("   5️⃣ Variable-length arguments (*args)")

def basic_arithmetic_operations():
    """
    Demonstrate basic arithmetic with asterisk operators
    """
    print("\n🧮 BASIC ARITHMETIC OPERATIONS")
    print("=" * 35)
    
    # Basic multiplication
    x = 2
    y = 3
    multiplication = x * y
    
    print(f"\n1️⃣ MULTIPLICATION:")
    print(f"   {x} * {y} = {multiplication}")
    
    # Exponentiation (power operation)
    base = 3
    exponent = 2
    power_result = base ** exponent
    
    print(f"\n2️⃣ EXPONENTIATION (**):")
    print(f"   {base} ** {exponent} = {power_result}")
    print(f"   (Read as: '{base} to the power of {exponent}')")
    
    # More power examples
    examples = [
        (2, 3),   # 2^3 = 8
        (5, 2),   # 5^2 = 25
        (10, 0),  # 10^0 = 1
        (4, 0.5)  # 4^0.5 = 2 (square root)
    ]
    
    print(f"\n   📊 More Power Examples:")
    for base, exp in examples:
        result = base ** exp
        print(f"     {base} ** {exp} = {result}")

def sequence_repetition():
    """
    Demonstrate asterisk for sequence repetition
    """
    print("\n🔄 SEQUENCE REPETITION WITH *")
    print("=" * 35)
    
    # String repetition
    char = "A"
    repeated_char = char * 5
    print(f"1️⃣ STRING REPETITION:")
    print(f"   '{char}' * 5 = '{repeated_char}'")
    
    # List repetition
    item = [1, 2]
    repeated_list = item * 3
    print(f"\n2️⃣ LIST REPETITION:")
    print(f"   {item} * 3 = {repeated_list}")
    
    # Creating patterns
    print(f"\n3️⃣ CREATING PATTERNS:")
    patterns = {
        "Stars": "*" * 10,
        "Dashes": "-" * 15,
        "Hearts": "♥ " * 5,
        "Zeros": [0] * 8
    }
    
    for name, pattern in patterns.items():
        print(f"   {name}: {pattern}")

def shortcut_assignment_operators():
    """
    Demonstrate shortcut assignment operators
    """
    print("\n⚡ SHORTCUT ASSIGNMENT OPERATORS")
    print("=" * 40)
    
    print("📝 What are Shortcut Functions?")
    print("   Shortcut operators perform an operation and assignment in one step")
    print("   They make code more concise and readable")
    
    # Starting value
    x = 10
    print(f"\n🔢 Starting with x = {x}")
    
    # Multiplication assignment (*=)
    print(f"\n1️⃣ MULTIPLICATION ASSIGNMENT (*=):")
    x_copy = x
    x_copy *= 2  # Same as: x_copy = x_copy * 2
    print(f"   x *= 2  →  x = {x_copy}")
    print(f"   (Equivalent to: x = x * 2)")
    
    # Power assignment (**=)
    print(f"\n2️⃣ POWER ASSIGNMENT (**=):")
    x_copy = 3
    print(f"   Starting: x = {x_copy}")
    x_copy **= 2  # Same as: x_copy = x_copy ** 2
    print(f"   x **= 2  →  x = {x_copy}")
    print(f"   (Equivalent to: x = x ** 2)")
    
    # All shortcut operators
    print(f"\n📋 ALL SHORTCUT OPERATORS:")
    shortcuts = {
        "+=": "Addition assignment (x += 5)",
        "-=": "Subtraction assignment (x -= 3)",
        "*=": "Multiplication assignment (x *= 2)",
        "/=": "Division assignment (x /= 4)",
        "**=": "Power assignment (x **= 2)",
        "//=": "Floor division assignment (x //= 3)",
        "%=": "Modulus assignment (x %= 7)"
    }
    
    for op, description in shortcuts.items():
        print(f"     {op:<3}: {description}")

def demonstrate_all_operations():
    """
    Comprehensive demonstration of asterisk operations
    """
    print(f"\n🌟 COMPREHENSIVE DEMONSTRATION")
    print("=" * 40)
    
    # Starting values
    a = 5
    b = 3
    
    print(f"Starting values: a = {a}, b = {b}")
    
    # Basic operations
    print(f"\n🧮 ARITHMETIC OPERATIONS:")
    print(f"   a * b = {a * b}")
    print(f"   a ** b = {a ** b}")
    
    # Conditional logic example
    print(f"\n🤔 CONDITIONAL LOGIC EXAMPLE:")
    if a == 5:
        print(f"   ✅ a is equal to 5")
        result = a ** 2
        print(f"   a squared = {result}")
    else:
        print(f"   ❌ a is not equal to 5")
    
    # Shortcut operations
    print(f"\n⚡ SHORTCUT OPERATIONS:")
    a_copy = a
    a_copy *= 2
    print(f"   After a *= 2: a = {a_copy}")
    
    b_copy = b
    b_copy **= 2
    print(f"   After b **= 2: b = {b_copy}")
    
    # String operations
    print(f"\n🔤 STRING OPERATIONS:")
    message = "Hi! "
    repeated_message = message * 3
    print(f"   '{message}' * 3 = '{repeated_message}'")

def practical_examples():
    """
    Practical examples using asterisk operations
    """
    print(f"\n🎯 PRACTICAL EXAMPLES")
    print("=" * 25)
    
    # Example 1: Creating a separator line
    print("1️⃣ Creating separator lines:")
    separator = "=" * 50
    print(f"   separator = '=' * 50")
    print(f"   Result: {separator}")
    
    # Example 2: Calculating compound interest
    print(f"\n2️⃣ Compound interest calculation:")
    principal = 1000
    rate = 1.05  # 5% interest
    years = 3
    
    final_amount = principal * (rate ** years)
    print(f"   Principal: ${principal}")
    print(f"   Rate: {rate} (5% annually)")
    print(f"   Years: {years}")
    print(f"   Final amount: ${final_amount:.2f}")
    
    # Example 3: Creating grid patterns
    print(f"\n3️⃣ Creating grid patterns:")
    rows = 3
    cols = 5
    
    print("   Creating a 3x5 grid of stars:")
    for i in range(rows):
        row = "* " * cols
        print(f"   {row}")
    
    # Example 4: Data initialization
    print(f"\n4️⃣ Data structure initialization:")
    empty_scores = [0] * 5
    print(f"   Initialize 5 scores to zero: {empty_scores}")
    
    matrix_row = [1, 2, 3]
    matrix = [matrix_row[:] for _ in range(3)]  # Create 3x3 matrix
    print(f"   3x3 matrix: {matrix}")

if __name__ == "__main__":
    """
    Main execution demonstrating all asterisk operations
    """
    print(__doc__)
    
    # Run all demonstrations
    introduce_asterisk_operator()
    basic_arithmetic_operations()
    sequence_repetition()
    shortcut_assignment_operators()
    demonstrate_all_operations()
    practical_examples()
    
    print("\n" + "=" * 50)
    print("🎓 LEARNING SUMMARY")
    print("=" * 50)
    print("✅ Understanding of asterisk (*) operator multiple uses")
    print("✅ Knowledge of exponentiation (**) operator")
    print("✅ Mastery of shortcut assignment operators")
    print("✅ Sequence repetition techniques")
    print("✅ Practical applications in real scenarios")
    
    print("\n💡 Key Takeaways:")
    print("• * operator has multiple contexts in Python")
    print("• ** is used for exponentiation (power operations)")
    print("• Shortcut operators make code more concise")
    print("• Sequence repetition is useful for patterns and initialization")
    print("• Understanding operator precedence is important")
    
    print("\n🎯 Next Steps:")
    print("• Learn about operator precedence and associativity")
    print("• Explore advanced uses of * (unpacking)")
    print("• Practice with more complex mathematical operations")
    print("• Study other Python operators in detail")
