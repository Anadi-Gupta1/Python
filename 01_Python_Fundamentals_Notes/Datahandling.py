"""
Python Data Handling Fundamentals - Learning Notes
===============================================

This module covers the fundamental concepts of data handling in Python,
including data types, data structures, and basic operations.

Author: Python Learning Notes
Date: September 2025
Topic: Data Types, Data Structures, Data Handling
"""

# =============================================================================
# WHAT IS DATA HANDLING?
# =============================================================================

def introduction_to_data_handling():
    """
    Data handling refers to the process of collecting, storing, managing, 
    and processing data in a structured manner.
    """
    print("🗃️  DATA HANDLING IN PYTHON")
    print("=" * 50)
    
    print("\n📋 What is Data Handling?")
    print("Data handling involves various operations:")
    print("• 📥 Data Input - Getting data into the program")
    print("• ✅ Data Validation - Ensuring data is correct")
    print("• 🔄 Data Transformation - Converting data formats")
    print("• 📤 Data Output - Presenting or storing results")
    print("• 💾 Data Storage - Saving data for later use")
    
    print("\n🎯 Why is Data Handling Important?")
    print("• Ensures data accuracy and reliability")
    print("• Improves program efficiency and performance")
    print("• Enables complex data analysis and processing")
    print("• Forms the foundation of all programming applications")

# =============================================================================
# UNDERSTANDING DATA
# =============================================================================

def what_is_data():
    """
    Data is a collection of facts, statistics, or information that can be 
    processed, analyzed, and used to make decisions.
    """
    print("\n📊 WHAT IS DATA?")
    print("=" * 30)
    
    print("Data is raw information that can be:")
    print("• 🔢 Numbers (age, price, quantity)")
    print("• 🔤 Text (names, descriptions, messages)")
    print("• ✅ Boolean values (true/false, yes/no)")
    print("• 📅 Dates and times")
    print("• 🖼️  Images, sounds, and other media")
    
    # Examples of different types of data
    examples = {
        "Personal Info": ["John Doe", 25, True, "engineer"],
        "Sales Data": [1250.75, "2024-09-28", "Product A"],
        "Survey Results": [True, False, True, "Maybe", 4.5]
    }
    
    print("\n📋 Data Examples:")
    for category, data_list in examples.items():
        print(f"   {category}: {data_list}")

# =============================================================================
# PYTHON DATA TYPES
# =============================================================================

def demonstrate_data_types():
    """
    Python has several built-in data types for handling different kinds of data
    """
    print("\n🐍 PYTHON DATA TYPES")
    print("=" * 40)
    
    # 1. NUMERIC DATA TYPES
    print("\n1️⃣ NUMERIC DATA TYPES:")
    
    # Integer
    age = 25
    print(f"   Integer: {age} (type: {type(age).__name__})")
    
    # Float
    price = 19.99
    print(f"   Float: {price} (type: {type(price).__name__})")
    
    # Complex
    complex_num = 3 + 4j
    print(f"   Complex: {complex_num} (type: {type(complex_num).__name__})")
    
    # 2. STRING DATA TYPE
    print("\n2️⃣ STRING DATA TYPE:")
    
    name = "Python Programming"
    message = 'Learning is fun!'
    multiline = """This is a
    multiline string"""
    
    print(f"   String: '{name}' (type: {type(name).__name__})")
    print(f"   Length: {len(name)} characters")
    print(f"   First char: '{name[0]}', Last char: '{name[-1]}'")
    
    # 3. BOOLEAN DATA TYPE
    print("\n3️⃣ BOOLEAN DATA TYPE:")
    
    is_student = True
    is_employed = False
    
    print(f"   Boolean True: {is_student} (type: {type(is_student).__name__})")
    print(f"   Boolean False: {is_employed} (type: {type(is_employed).__name__})")
    
    # Boolean operations
    print(f"   AND operation: {is_student and is_employed}")
    print(f"   OR operation: {is_student or is_employed}")
    print(f"   NOT operation: {not is_student}")

# =============================================================================
# PYTHON DATA STRUCTURES
# =============================================================================

def demonstrate_data_structures():
    """
    Python provides several built-in data structures for organizing data
    """
    print("\n🏗️  PYTHON DATA STRUCTURES")
    print("=" * 45)
    
    # 1. LIST DATA STRUCTURE
    print("\n1️⃣ LIST (Ordered, Mutable):")
    
    fruits = ["apple", "banana", "orange", "grape"]
    mixed_list = [1, "hello", 3.14, True, None]
    
    print(f"   Fruits list: {fruits}")
    print(f"   Mixed list: {mixed_list}")
    print(f"   List length: {len(fruits)}")
    print(f"   First fruit: {fruits[0]}")
    print(f"   Last fruit: {fruits[-1]}")
    
    # List operations
    fruits.append("mango")
    print(f"   After adding mango: {fruits}")
    
    # 2. TUPLE DATA STRUCTURE
    print("\n2️⃣ TUPLE (Ordered, Immutable):")
    
    coordinates = (10, 20)
    colors = ("red", "green", "blue")
    mixed_tuple = (1, "Python", 3.14, True)
    
    print(f"   Coordinates: {coordinates}")
    print(f"   Colors: {colors}")
    print(f"   Mixed tuple: {mixed_tuple}")
    print(f"   X coordinate: {coordinates[0]}")
    print(f"   Y coordinate: {coordinates[1]}")
    
    # 3. DICTIONARY DATA STRUCTURE
    print("\n3️⃣ DICTIONARY (Key-Value Pairs, Mutable):")
    
    student = {
        "name": "Alice Johnson",
        "age": 20,
        "grade": "A",
        "subjects": ["Math", "Science", "English"]
    }
    
    print(f"   Student info: {student}")
    print(f"   Student name: {student['name']}")
    print(f"   Student age: {student['age']}")
    print(f"   Dictionary keys: {list(student.keys())}")
    
    # 4. SET DATA STRUCTURE
    print("\n4️⃣ SET (Unordered, Unique Items):")
    
    unique_numbers = {1, 2, 3, 4, 5}
    unique_colors = {"red", "green", "blue", "red", "green"}  # Duplicates removed
    
    print(f"   Numbers set: {unique_numbers}")
    print(f"   Colors set: {unique_colors}")  # Notice duplicates are removed
    print(f"   Set length: {len(unique_colors)}")

# =============================================================================
# SEQUENCES IN PYTHON
# =============================================================================

def understand_sequences():
    """
    A sequence is an ordered collection of items that can be indexed and iterated over.
    In memory, sequence data is stored in a linear manner with continuous allocation.
    """
    print("\n🔗 UNDERSTANDING SEQUENCES")
    print("=" * 40)
    
    print("📝 What is a Sequence?")
    print("• An ordered collection of items")
    print("• Items can be accessed by index (position)")
    print("• Items are stored in memory in linear arrangement")
    print("• Support iteration (looping through items)")
    
    # Examples of sequences
    print("\n🐍 Python Sequence Types:")
    
    # String (sequence of characters)
    text = "Python"
    print(f"   String: '{text}' → {[char for char in text]}")
    
    # List (sequence of any items)
    numbers = [10, 20, 30, 40, 50]
    print(f"   List: {numbers}")
    
    # Tuple (immutable sequence)
    weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")
    print(f"   Tuple: {weekdays}")
    
    # Range (sequence of numbers)
    number_range = range(1, 6)
    print(f"   Range: range(1, 6) → {list(number_range)}")
    
    # Common sequence operations
    print("\n🛠️  Common Sequence Operations:")
    print(f"   Length: len({text}) = {len(text)}")
    print(f"   Indexing: {text}[0] = '{text[0]}'")
    print(f"   Slicing: {text}[1:4] = '{text[1:4]}'")
    print(f"   Contains: 'Py' in '{text}' = {'Py' in text}")
    print(f"   Concatenation: '{text}' + ' Rocks' = '{text + ' Rocks'}'")

# =============================================================================
# PRACTICAL DATA HANDLING EXAMPLES
# =============================================================================

def practical_examples():
    """
    Real-world examples of data handling in Python
    """
    print("\n🌟 PRACTICAL DATA HANDLING EXAMPLES")
    print("=" * 50)
    
    # Example 1: Student Grade Management
    print("\n📚 Example 1: Student Grade Management")
    
    student_grades = {
        "Alice": [85, 90, 88],
        "Bob": [78, 82, 80],
        "Charlie": [92, 89, 94]
    }
    
    for student, grades in student_grades.items():
        average = sum(grades) / len(grades)
        print(f"   {student}: Grades {grades}, Average: {average:.1f}")
    
    # Example 2: Shopping Cart
    print("\n🛒 Example 2: Shopping Cart")
    
    cart_items = [
        {"name": "Laptop", "price": 999.99, "quantity": 1},
        {"name": "Mouse", "price": 29.99, "quantity": 2},
        {"name": "Keyboard", "price": 79.99, "quantity": 1}
    ]
    
    total_cost = 0
    for item in cart_items:
        item_total = item["price"] * item["quantity"]
        total_cost += item_total
        print(f"   {item['name']}: ${item['price']} × {item['quantity']} = ${item_total}")
    
    print(f"   Total Cart Value: ${total_cost:.2f}")
    
    # Example 3: Data Validation
    print("\n✅ Example 3: Data Validation")
    
    def validate_email(email):
        """Simple email validation"""
        return "@" in email and "." in email.split("@")[1]
    
    emails = ["user@example.com", "invalid-email", "test@domain.org", "bad@"]
    
    for email in emails:
        status = "✅ Valid" if validate_email(email) else "❌ Invalid"
        print(f"   {email}: {status}")

if __name__ == "__main__":
    """
    Main execution block demonstrating all data handling concepts
    """
    print(__doc__)
    
    # Run all demonstrations
    introduction_to_data_handling()
    what_is_data()
    demonstrate_data_types()
    demonstrate_data_structures()
    understand_sequences()
    practical_examples()
    
    print("\n" + "=" * 50)
    print("🎓 LEARNING SUMMARY")
    print("=" * 50)
    print("✅ Understanding of data handling importance")
    print("✅ Knowledge of Python data types:")
    print("   • Numeric (int, float, complex)")
    print("   • String (text data)")
    print("   • Boolean (True/False)")
    print("✅ Familiarity with data structures:")
    print("   • List (ordered, mutable)")
    print("   • Tuple (ordered, immutable)")
    print("   • Dictionary (key-value pairs)")
    print("   • Set (unique items)")
    print("✅ Understanding of sequences and their properties")
    
    print("\n🎯 Next Steps:")
    print("• Practice with different data types")
    print("• Learn advanced data structure operations")
    print("• Explore data validation techniques")
    print("• Study data persistence (file handling)")
