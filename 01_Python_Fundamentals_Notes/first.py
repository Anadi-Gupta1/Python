"""
Python Fundamentals - First Program and Language Tokens
=====================================================

This is your first Python program! It demonstrates the basic structure of Python
code and introduces the fundamental tokens that make up the Python language.

Author: Python Learning Notes
Date: September 2025
Topic: Python Basics, Language Tokens, First Program
"""

# =============================================================================
# FIRST PYTHON PROGRAM
# =============================================================================

def first_python_program():
    """
    Traditional first program in any programming language
    Demonstrates basic output using print() function
    """
    print("🐍 Hello World from Python!")
    print("This is my first Python script in the Fundamentals directory.")
    print("Welcome to the amazing world of Python programming! 🚀")

# =============================================================================
# PYTHON LANGUAGE TOKENS
# =============================================================================

def demonstrate_python_tokens():
    """
    Python consists of various tokens - the smallest elements of a program.
    Understanding these tokens is crucial for writing Python code.
    """
    
    print("\n" + "=" * 50)
    print("🔤 PYTHON LANGUAGE TOKENS OVERVIEW")
    print("=" * 50)
    
    # 1. KEYWORDS (Reserved words with special meaning)
    print("\n1️⃣ KEYWORDS (Reserved Words):")
    keywords = [
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
        'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
        'except', 'finally', 'for', 'from', 'global', 'if', 'import',
        'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
        'raise', 'return', 'try', 'while', 'with', 'yield'
    ]
    
    print(f"📝 Total Keywords: {len(keywords)}")
    print("Examples of commonly used keywords:")
    common_keywords = ['if', 'else', 'for', 'while', 'def', 'class', 'import', 'return']
    for keyword in common_keywords:
        print(f"   • {keyword}")
    
    # 2. IDENTIFIERS (Names for variables, functions, classes)
    print("\n2️⃣ IDENTIFIERS (Variable/Function Names):")
    identifiers = ['a', 'b', 'c', 'my_variable', 'anotherVariable', 'user_name', 'calculate_sum']
    print("Examples of valid identifiers:")
    for identifier in identifiers:
        print(f"   • {identifier}")
    
    print("\n📋 Identifier Rules:")
    print("   ✅ Must start with letter (a-z, A-Z) or underscore (_)")
    print("   ✅ Can contain letters, digits (0-9), and underscores")
    print("   ❌ Cannot start with a digit")
    print("   ❌ Cannot be a Python keyword")
    print("   ❌ Cannot contain spaces or special characters")
    
    # 3. LITERALS (Fixed values in code)
    print("\n3️⃣ LITERALS (Fixed Values):")
    
    # Numeric literals
    integer_literal = 42
    float_literal = 3.14159
    complex_literal = 2 + 3j
    
    # String literals
    string_literal_single = 'Hello'
    string_literal_double = "World"
    string_literal_triple = """This is a
    multiline string"""
    
    # Boolean literals
    bool_literal_true = True
    bool_literal_false = False
    
    # None literal
    none_literal = None
    
    print(f"   📊 Integer: {integer_literal} (type: {type(integer_literal).__name__})")
    print(f"   🔢 Float: {float_literal} (type: {type(float_literal).__name__})")
    print(f"   🔤 String: '{string_literal_single}' (type: {type(string_literal_single).__name__})")
    print(f"   ✅ Boolean: {bool_literal_true} (type: {type(bool_literal_true).__name__})")
    print(f"   ❌ None: {none_literal} (type: {type(none_literal).__name__})")
    
    # 4. OPERATORS (Symbols for operations)
    print("\n4️⃣ OPERATORS (Operation Symbols):")
    
    arithmetic_ops = ['+', '-', '*', '/', '%', '**', '//']
    comparison_ops = ['==', '!=', '<', '>', '<=', '>=']
    logical_ops = ['and', 'or', 'not']
    assignment_ops = ['=', '+=', '-=', '*=', '/=']
    
    print("   🔢 Arithmetic:", ', '.join(arithmetic_ops))
    print("   ⚖️  Comparison:", ', '.join(comparison_ops))
    print("   🧠 Logical:", ', '.join(logical_ops))
    print("   📝 Assignment:", ', '.join(assignment_ops))
    
    # 5. DELIMITERS (Symbols for grouping and separation)
    print("\n5️⃣ DELIMITERS (Grouping & Separation):")
    delimiters = {
        'Parentheses': '( )',
        'Square brackets': '[ ]',
        'Curly braces': '{ }',
        'Comma': ',',
        'Colon': ':',
        'Semicolon': ';',
        'Period/Dot': '.',
        'At symbol': '@'
    }
    
    for name, symbol in delimiters.items():
        print(f"   • {name}: {symbol}")

def demonstrate_token_usage():
    """
    Practical demonstration of using different tokens in Python code
    """
    print("\n" + "=" * 50)
    print("🛠️  PRACTICAL TOKEN USAGE EXAMPLES")
    print("=" * 50)
    
    # Using identifiers and assignment
    student_name = "Alice"  # identifier + string literal
    student_age = 20        # identifier + integer literal
    is_enrolled = True      # identifier + boolean literal
    
    # Using operators and delimiters
    if student_age >= 18 and is_enrolled:  # keywords, operators, identifiers
        print(f"Student {student_name} is an adult and enrolled.")
    else:
        print(f"Student {student_name} is either minor or not enrolled.")
    
    # Using various delimiters
    subjects = ['Math', 'Science', 'History']  # list with square brackets
    student_info = {                           # dictionary with curly braces
        'name': student_name,
        'age': student_age,
        'subjects': subjects
    }
    
    print(f"\n📋 Student Information:")
    for key, value in student_info.items():   # keywords, identifiers, delimiters
        print(f"   {key}: {value}")

if __name__ == "__main__":
    """
    Main execution block - runs when script is executed directly
    """
    print(__doc__)
    
    # Run the first program
    first_python_program()
    
    # Demonstrate Python tokens
    demonstrate_python_tokens()
    
    # Show practical usage
    demonstrate_token_usage()
    
    print("\n" + "=" * 50)
    print("🎓 LEARNING SUMMARY")
    print("=" * 50)
    print("✅ You've learned about Python's basic structure")
    print("✅ You understand the 5 types of Python tokens:")
    print("   1. Keywords (reserved words)")
    print("   2. Identifiers (names)")
    print("   3. Literals (fixed values)")
    print("   4. Operators (operation symbols)")
    print("   5. Delimiters (grouping symbols)")
    
    print("\n🎯 Next Steps:")
    print("• Learn about Python data types in detail")
    print("• Practice writing variables with good identifiers")
    print("• Explore different types of operators")
    print("• Understand Python syntax and indentation")
