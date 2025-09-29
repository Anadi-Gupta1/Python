"""
Python Lists - Complete Operations Guide
======================================

Comprehensive guide to Python lists covering types, operations, methods,
and practical applications. Lists are one of the most versatile and
commonly used data structures in Python.

Author: Python Learning Notes
Date: September 2025
Topic: Lists, Data Structures, List Operations
"""

# =============================================================================
# UNDERSTANDING PYTHON LISTS
# =============================================================================

def introduction_to_lists():
    """
    Introduction to Python lists and their characteristics
    """
    print("📋 PYTHON LISTS - COMPLETE GUIDE")
    print("=" * 40)
    
    print("\n🔍 What is a List?")
    print("A list is a collection of items that are:")
    print("   ✅ Ordered - Items have a defined order")
    print("   ✅ Changeable (Mutable) - Items can be modified")
    print("   ✅ Allow duplicates - Same value can appear multiple times")
    print("   ✅ Indexed - Items can be accessed by position (0, 1, 2...)")
    
    print("\n📝 List Syntax:")
    print("   my_list = [item1, item2, item3, ...]")
    print("   my_list = []  # Empty list")

# =============================================================================
# TYPES OF LISTS IN PYTHON
# =============================================================================

def demonstrate_list_types():
    """
    Demonstrate different types of lists in Python
    """
    print("\n🗂️  TYPES OF LISTS IN PYTHON")
    print("=" * 35)
    
    # 1. HOMOGENEOUS LIST
    print("\n1️⃣ HOMOGENEOUS LIST (Same data type):")
    homogeneous_numbers = [1, 2, 3, 4, 5]
    homogeneous_strings = ["apple", "banana", "cherry"]
    homogeneous_booleans = [True, False, True, True]
    
    print(f"   Numbers: {homogeneous_numbers}")
    print(f"   Strings: {homogeneous_strings}")
    print(f"   Booleans: {homogeneous_booleans}")
    print(f"   All elements are {type(homogeneous_numbers[0]).__name__}s")
    
    # 2. HETEROGENEOUS LIST
    print("\n2️⃣ HETEROGENEOUS LIST (Mixed data types):")
    heterogeneous_list = [1, "two", 3.0, True, None]
    
    print(f"   Mixed list: {heterogeneous_list}")
    print("   Data types:")
    for i, item in enumerate(heterogeneous_list):
        print(f"     Index {i}: {item} ({type(item).__name__})")
    
    # 3. NESTED LIST
    print("\n3️⃣ NESTED LIST (Lists within lists):")
    nested_list = [[1, 2], [3, 4], [5, 6]]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    print(f"   Simple nested: {nested_list}")
    print(f"   3x3 Matrix: {matrix}")
    print(f"   Accessing nested item: matrix[1][2] = {matrix[1][2]}")
    
    # 4. MULTIDIMENSIONAL LIST
    print("\n4️⃣ MULTIDIMENSIONAL LIST (3D and beyond):")
    three_d_list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    
    print(f"   3D List: {three_d_list}")
    print(f"   Accessing 3D item: three_d_list[0][1][1] = {three_d_list[0][1][1]}")
    
    # 5. EMPTY LIST
    print("\n5️⃣ EMPTY LIST:")
    empty_list = []
    empty_list_alt = list()
    
    print(f"   Empty list: {empty_list}")
    print(f"   Length: {len(empty_list)}")
    print(f"   Alternative syntax: {empty_list_alt}")
    
    # 6. SPECIALIZED LISTS
    print("\n6️⃣ SPECIALIZED LISTS:")
    
    # List of tuples
    list_of_tuples = [(1, 2), (3, 4), (5, 6)]
    print(f"   List of tuples: {list_of_tuples}")
    
    # List of dictionaries
    list_of_dicts = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30},
        {"name": "Charlie", "age": 35}
    ]
    print(f"   List of dictionaries: {list_of_dicts}")
    
    # List of sets
    list_of_sets = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
    print(f"   List of sets: {list_of_sets}")

# =============================================================================
# BASIC LIST OPERATIONS
# =============================================================================

def basic_list_operations():
    """
    Demonstrate basic list operations
    """
    print("\n🛠️  BASIC LIST OPERATIONS")
    print("=" * 30)
    
    # Creating a sample list
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    print(f"Original list: {fruits}")
    
    # 1. ACCESSING ELEMENTS
    print("\n1️⃣ ACCESSING ELEMENTS:")
    print(f"   First element (index 0): {fruits[0]}")
    print(f"   Last element (index -1): {fruits[-1]}")
    print(f"   Second element (index 1): {fruits[1]}")
    print(f"   Second last (index -2): {fruits[-2]}")
    
    # 2. SLICING
    print("\n2️⃣ SLICING:")
    print(f"   First 3 elements: {fruits[:3]}")
    print(f"   Last 2 elements: {fruits[-2:]}")
    print(f"   Middle elements: {fruits[1:4]}")
    print(f"   Every 2nd element: {fruits[::2]}")
    print(f"   Reverse list: {fruits[::-1]}")
    
    # 3. CHECKING MEMBERSHIP
    print("\n3️⃣ CHECKING MEMBERSHIP:")
    print(f"   'apple' in list: {'apple' in fruits}")
    print(f"   'grape' in list: {'grape' in fruits}")
    print(f"   'banana' not in list: {'banana' not in fruits}")
    
    # 4. LIST LENGTH
    print(f"\n4️⃣ LIST LENGTH: {len(fruits)} elements")
    
    # 5. LIST CONCATENATION
    print("\n5️⃣ LIST CONCATENATION:")
    more_fruits = ["fig", "grape", "honeydew"]
    combined = fruits + more_fruits
    print(f"   Original: {fruits}")
    print(f"   Additional: {more_fruits}")
    print(f"   Combined: {combined}")
    
    # 6. LIST REPETITION
    print("\n6️⃣ LIST REPETITION:")
    repeated = ["ha"] * 3
    print(f"   ['ha'] * 3 = {repeated}")

# =============================================================================
# LIST METHODS AND MODIFICATIONS
# =============================================================================

def list_methods_demonstration():
    """
    Demonstrate various list methods
    """
    print("\n🔧 LIST METHODS DEMONSTRATION")
    print("=" * 35)
    
    # Working list
    numbers = [1, 3, 5, 7, 9]
    print(f"Starting list: {numbers}")
    
    # 1. ADDING ELEMENTS
    print("\n1️⃣ ADDING ELEMENTS:")
    
    # append() - add single element at end
    numbers.append(11)
    print(f"   After append(11): {numbers}")
    
    # insert() - add element at specific position
    numbers.insert(2, 4)
    print(f"   After insert(2, 4): {numbers}")
    
    # extend() - add multiple elements
    numbers.extend([13, 15])
    print(f"   After extend([13, 15]): {numbers}")
    
    # 2. REMOVING ELEMENTS
    print("\n2️⃣ REMOVING ELEMENTS:")
    
    # remove() - remove first occurrence of value
    numbers.remove(4)
    print(f"   After remove(4): {numbers}")
    
    # pop() - remove and return element at index
    popped = numbers.pop()  # removes last element
    print(f"   After pop(): {numbers} (popped: {popped})")
    
    popped_index = numbers.pop(2)  # removes element at index 2
    print(f"   After pop(2): {numbers} (popped: {popped_index})")
    
    # clear() - remove all elements
    temp_list = [1, 2, 3]
    temp_list.clear()
    print(f"   After clear(): {temp_list}")
    
    # 3. FINDING ELEMENTS
    print("\n3️⃣ FINDING ELEMENTS:")
    colors = ["red", "green", "blue", "red", "yellow"]
    print(f"   Colors list: {colors}")
    
    # index() - find first occurrence
    red_index = colors.index("red")
    print(f"   Index of 'red': {red_index}")
    
    # count() - count occurrences
    red_count = colors.count("red")
    print(f"   Count of 'red': {red_count}")
    
    # 4. SORTING AND REVERSING
    print("\n4️⃣ SORTING AND REVERSING:")
    mixed_numbers = [5, 2, 8, 1, 9, 3]
    print(f"   Original: {mixed_numbers}")
    
    # sort() - sort in place
    mixed_numbers.sort()
    print(f"   After sort(): {mixed_numbers}")
    
    # reverse() - reverse in place
    mixed_numbers.reverse()
    print(f"   After reverse(): {mixed_numbers}")
    
    # sorted() - return new sorted list (doesn't modify original)
    original = [5, 2, 8, 1, 9, 3]
    sorted_copy = sorted(original)
    print(f"   Original unchanged: {original}")
    print(f"   Sorted copy: {sorted_copy}")

# =============================================================================
# ADVANCED LIST OPERATIONS
# =============================================================================

def advanced_list_operations():
    """
    Demonstrate advanced list operations and techniques
    """
    print("\n⚡ ADVANCED LIST OPERATIONS")
    print("=" * 35)
    
    # 1. LIST COMPREHENSIONS
    print("\n1️⃣ LIST COMPREHENSIONS:")
    
    # Basic comprehension
    squares = [x**2 for x in range(1, 6)]
    print(f"   Squares [x**2 for x in range(1, 6)]: {squares}")
    
    # With condition
    even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
    print(f"   Even squares: {even_squares}")
    
    # String manipulation
    words = ["hello", "world", "python"]
    capitalized = [word.upper() for word in words]
    print(f"   Capitalized: {capitalized}")
    
    # 2. NESTED LIST OPERATIONS
    print("\n2️⃣ NESTED LIST OPERATIONS:")
    
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"   Matrix: {matrix}")
    
    # Flatten nested list
    flattened = [item for sublist in matrix for item in sublist]
    print(f"   Flattened: {flattened}")
    
    # Transpose matrix
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print(f"   Transposed: {transposed}")
    
    # 3. FILTERING AND MAPPING
    print("\n3️⃣ FILTERING AND MAPPING:")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Filter even numbers
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"   Even numbers: {evens}")
    
    # Map to squares
    squares = list(map(lambda x: x**2, numbers))
    print(f"   Squared: {squares}")
    
    # 4. LIST COPYING
    print("\n4️⃣ LIST COPYING:")
    
    original = [1, 2, 3, 4, 5]
    
    # Shallow copy methods
    copy1 = original.copy()
    copy2 = original[:]
    copy3 = list(original)
    
    print(f"   Original: {original}")
    print(f"   Copy methods produce same result:")
    print(f"     .copy(): {copy1}")
    print(f"     [:]: {copy2}")
    print(f"     list(): {copy3}")
    
    # Demonstrate independence
    copy1.append(6)
    print(f"   After copy1.append(6):")
    print(f"     Original: {original}")
    print(f"     Copy1: {copy1}")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

def practical_examples():
    """
    Real-world examples of list usage
    """
    print("\n🌟 PRACTICAL EXAMPLES")
    print("=" * 25)
    
    # Example 1: Shopping Cart
    print("\n🛒 Example 1: Shopping Cart Management")
    
    shopping_cart = []
    
    def add_to_cart(item, price):
        shopping_cart.append({"item": item, "price": price})
        print(f"   Added {item} (${price}) to cart")
    
    def display_cart():
        if not shopping_cart:
            print("   Cart is empty")
            return
        
        print("   Shopping Cart:")
        total = 0
        for i, item in enumerate(shopping_cart, 1):
            print(f"     {i}. {item['item']} - ${item['price']}")
            total += item['price']
        print(f"   Total: ${total:.2f}")
    
    # Simulate shopping
    add_to_cart("Laptop", 999.99)
    add_to_cart("Mouse", 29.99)
    add_to_cart("Keyboard", 79.99)
    display_cart()
    
    # Example 2: Grade Management
    print("\n📚 Example 2: Student Grade Management")
    
    students = [
        {"name": "Alice", "grades": [85, 90, 88]},
        {"name": "Bob", "grades": [78, 82, 80]},
        {"name": "Charlie", "grades": [92, 89, 94]}
    ]
    
    print("   Grade Report:")
    for student in students:
        grades = student["grades"]
        average = sum(grades) / len(grades)
        print(f"     {student['name']}: {grades} → Average: {average:.1f}")
    
    # Example 3: Data Processing
    print("\n📊 Example 3: Data Processing Pipeline")
    
    raw_data = ["  Alice  ", "BOB", "charlie", "", "  DAVID "]
    
    # Clean and process data
    cleaned_data = []
    for item in raw_data:
        cleaned = item.strip()  # Remove whitespace
        if cleaned:  # Remove empty strings
            cleaned_data.append(cleaned.title())  # Title case
    
    print(f"   Raw data: {raw_data}")
    print(f"   Cleaned data: {cleaned_data}")
    
    # Find items with specific criteria
    short_names = [name for name in cleaned_data if len(name) <= 5]
    print(f"   Names ≤ 5 characters: {short_names}")

if __name__ == "__main__":
    """
    Main execution demonstrating all list concepts
    """
    print(__doc__)
    
    # Run all demonstrations
    introduction_to_lists()
    demonstrate_list_types()
    basic_list_operations()
    list_methods_demonstration()
    advanced_list_operations()
    practical_examples()
    
    print("\n" + "=" * 50)
    print("🎓 LEARNING SUMMARY")
    print("=" * 50)
    print("✅ Understanding of list types and characteristics")
    print("✅ Mastery of basic list operations (access, slice, etc.)")
    print("✅ Knowledge of list methods (append, remove, sort, etc.)")
    print("✅ Advanced techniques (comprehensions, filtering, mapping)")
    print("✅ Practical applications in real-world scenarios")
    print("✅ List copying and memory management concepts")
    
    print("\n💡 Key Takeaways:")
    print("• Lists are versatile, ordered, and mutable collections")
    print("• Many built-in methods for efficient list manipulation")
    print("• List comprehensions provide powerful, readable syntax")
    print("• Understanding shallow vs deep copying is crucial")
    print("• Lists are fundamental to most Python applications")
    
    print("\n🎯 Next Steps:")
    print("• Learn about other data structures (tuples, sets, dicts)")
    print("• Practice with nested data structures")
    print("• Explore performance characteristics of list operations")
    print("• Study algorithms that work with lists")  
# Printing the lists
print("Homogeneous List:", homogeneous_list)
print("Heterogeneous List:", heterogeneous_list)
print("Nested List:", nested_list)
print("Multidimensional List:", multidimensional_list)
print("Empty List:", empty_list)



list = [1, 2, 3, 4, 5]  # Example of a simple list
print( list)

