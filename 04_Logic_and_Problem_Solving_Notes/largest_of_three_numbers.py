"""
Largest of Three Numbers - Comparison Logic and Decision Making
============================================================

Comprehensive exploration of finding the maximum among three numbers using
various approaches including conditional logic, built-in functions, and
algorithmic methods. Demonstrates decision-making structures and optimization.

Author: Python Learning Notes
Date: September 2025
Topic: Conditional Statements, Comparison Operations, Decision Making
"""

from typing import List, Union, Tuple
import random

# =============================================================================
# FUNDAMENTAL CONCEPTS AND THEORY
# =============================================================================

def explain_comparison_concepts():
    """
    Educational explanation of comparison operations and decision making
    """
    print("🔍 COMPARISON AND DECISION MAKING CONCEPTS")
    print("=" * 45)
    
    print("\n📚 What is Comparison?")
    print("Comparison operations allow us to:")
    print("   • Determine relationships between values")
    print("   • Make decisions based on conditions")
    print("   • Control program flow with logic")
    print("   • Implement sorting and selection algorithms")
    
    print("\n🔢 Comparison Operators in Python:")
    operators = [
        ("==", "Equal to", "5 == 5 → True"),
        ("!=", "Not equal to", "5 != 3 → True"), 
        (">", "Greater than", "7 > 4 → True"),
        ("<", "Less than", "2 < 6 → True"),
        (">=", "Greater than or equal", "5 >= 5 → True"),
        ("<=", "Less than or equal", "3 <= 8 → True")
    ]
    
    print("   ┌──────┬─────────────────────┬─────────────────┐")
    print("   │ Op.  │ Description         │ Example         │")
    print("   ├──────┼─────────────────────┼─────────────────┤")
    for op, desc, example in operators:
        print(f"   │ {op:<4} │ {desc:<19} │ {example:<15} │")
    print("   └──────┴─────────────────────┴─────────────────┘")
    
    print("\n🧠 Logical Operators:")
    print("   • AND (and): Both conditions must be True")
    print("   • OR (or): At least one condition must be True") 
    print("   • NOT (not): Reverses the boolean value")
    
    print("\n📊 Truth Table for AND operation:")
    print("   A     │ B     │ A and B")
    print("   ──────┼───────┼────────")
    print("   True  │ True  │ True")
    print("   True  │ False │ False")
    print("   False │ True  │ False")
    print("   False │ False │ False")

# =============================================================================
# BASIC APPROACHES TO FIND MAXIMUM
# =============================================================================

def find_largest_basic_if_else(a, b, c):
    """
    Basic approach using nested if-else statements
    
    Method: Sequential comparison with explicit conditions
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    print(f"\n🔍 Basic If-Else Method")
    print("=" * 25)
    print(f"   Numbers: a={a}, b={b}, c={c}")
    print("\n   Step-by-step comparison:")
    
    if a > b and a > c:
        print(f"   ✓ a ({a}) > b ({b}) AND a ({a}) > c ({c})")
        print(f"   Result: {a} is the largest")
        return a
    elif b > a and b > c:
        print(f"   ✓ b ({b}) > a ({a}) AND b ({b}) > c ({c})")
        print(f"   Result: {b} is the largest")
        return b
    else:
        print(f"   ✓ c ({c}) is largest (or equal to largest)")
        print(f"   Result: {c} is the largest")
        return c

def find_largest_sequential(a, b, c):
    """
    Sequential comparison approach
    
    Method: Compare pairs step by step
    """
    print(f"\n🔄 Sequential Comparison Method")
    print("=" * 30)
    print(f"   Numbers: a={a}, b={b}, c={c}")
    
    # Start with first number as largest
    largest = a
    print(f"   Step 1: Assume a={a} is largest")
    
    # Compare with second number
    if b > largest:
        largest = b
        print(f"   Step 2: b={b} > {a}, so largest = {b}")
    else:
        print(f"   Step 2: b={b} ≤ {largest}, largest remains {largest}")
    
    # Compare with third number
    if c > largest:
        previous = largest
        largest = c
        print(f"   Step 3: c={c} > {previous}, so largest = {c}")
    else:
        print(f"   Step 3: c={c} ≤ {largest}, largest remains {largest}")
    
    print(f"\n   ✅ Final result: {largest}")
    return largest

def find_largest_builtin(a, b, c):
    """
    Using Python's built-in max() function
    
    Method: Leverages optimized built-in function
    Most efficient and readable approach
    """
    print(f"\n⚡ Built-in max() Function")
    print("=" * 25)
    print(f"   Numbers: {a}, {b}, {c}")
    
    result = max(a, b, c)
    print(f"   Using max({a}, {b}, {c}) = {result}")
    print(f"   ✅ Result: {result}")
    
    return result

# =============================================================================
# ADVANCED COMPARISON METHODS
# =============================================================================

def find_largest_ternary(a, b, c):
    """
    Using ternary (conditional) operators for compact code
    
    Method: Nested ternary operations
    """
    print(f"\n🎯 Ternary Operator Method")
    print("=" * 25)
    print(f"   Numbers: a={a}, b={b}, c={c}")
    
    # Nested ternary: (a if a > b else b) if (a if a > b else b) > c else c
    result = (a if a > b else b) if (a if a > b else b) > c else c
    
    print("   Ternary expression breakdown:")
    temp = a if a > b else b
    print(f"   • First comparison: a if a > b else b = {temp}")
    print(f"   • Second comparison: {temp} if {temp} > c else c = {result}")
    print(f"   ✅ Result: {result}")
    
    return result

def find_largest_mathematical(a, b, c):
    """
    Mathematical approach without explicit comparisons
    
    Method: Using mathematical properties and functions
    """
    print(f"\n🧮 Mathematical Approach")
    print("=" * 25)
    print(f"   Numbers: a={a}, b={b}, c={c}")
    
    # Method 1: Using sum and abs
    print("\n   Method 1: Using mathematical properties")
    
    # Find max of two numbers: (a + b + |a - b|) / 2
    def max_two(x, y):
        return (x + y + abs(x - y)) // 2
    
    step1 = max_two(a, b)
    result = max_two(step1, c)
    
    print(f"   Step 1: max({a}, {b}) = ({a} + {b} + |{a} - {b}|) / 2 = {step1}")
    print(f"   Step 2: max({step1}, {c}) = {result}")
    print(f"   ✅ Result: {result}")
    
    return result

def find_largest_list_approach(a, b, c):
    """
    Using list and list methods
    
    Method: Convert to list and use list operations
    """
    print(f"\n📋 List-Based Approach")
    print("=" * 22)
    
    numbers = [a, b, c]
    print(f"   Numbers list: {numbers}")
    
    # Method 1: Using max() on list
    result1 = max(numbers)
    print(f"   Using max(list): {result1}")
    
    # Method 2: Using sorted() and taking last element
    sorted_numbers = sorted(numbers)
    result2 = sorted_numbers[-1]
    print(f"   Using sorted()[-1]: {sorted_numbers} → {result2}")
    
    # Method 3: Using list.sort() and indexing
    numbers_copy = numbers.copy()
    numbers_copy.sort()
    result3 = numbers_copy[-1]
    print(f"   Using sort()[-1]: {result3}")
    
    print(f"   ✅ All methods give: {result1}")
    return result1

# =============================================================================
# HANDLING EDGE CASES
# =============================================================================

def find_largest_with_edge_cases(a, b, c):
    """
    Comprehensive solution handling various edge cases
    """
    print(f"\n🛡️  Edge Case Handling")
    print("=" * 22)
    print(f"   Numbers: a={a}, b={b}, c={c}")
    
    # Check for equal values
    if a == b == c:
        print("   📍 All numbers are equal")
        return a, "All numbers are equal"
    
    elif a == b and a > c:
        print("   📍 Two numbers tied for largest (a and b)")
        return a, "a and b are tied for largest"
    
    elif a == c and a > b:
        print("   📍 Two numbers tied for largest (a and c)")
        return a, "a and c are tied for largest"
    
    elif b == c and b > a:
        print("   📍 Two numbers tied for largest (b and c)")
        return b, "b and c are tied for largest"
    
    else:
        # Standard case - all numbers different
        largest = max(a, b, c)
        which = 'a' if largest == a else ('b' if largest == b else 'c')
        print(f"   📍 Standard case: {which} is uniquely largest")
        return largest, f"{which} is the largest"

def handle_special_inputs():
    """
    Demonstrate handling of special numeric inputs
    """
    print(f"\n🔬 Special Input Cases")
    print("=" * 22)
    
    test_cases = [
        (0, 0, 0, "All zeros"),
        (-5, -2, -8, "All negative"),
        (5, -3, 0, "Mixed signs"),
        (3.14, 2.71, 3.14159, "Floating point"),
        (float('inf'), 100, 200, "Infinity value"),
        (float('-inf'), -100, -50, "Negative infinity")
    ]
    
    for a, b, c, description in test_cases:
        print(f"\n   Case: {description}")
        print(f"   Values: {a}, {b}, {c}")
        
        try:
            result = max(a, b, c)
            print(f"   Result: {result}")
        except Exception as e:
            print(f"   Error: {e}")

# =============================================================================
# PERFORMANCE COMPARISON
# =============================================================================

def compare_methods_performance():
    """
    Compare performance of different maximum-finding methods
    """
    import time
    import random
    
    print(f"\n⏱️  PERFORMANCE COMPARISON")
    print("=" * 30)
    
    # Generate test data
    test_size = 100000
    test_data = [(random.randint(-1000, 1000), 
                  random.randint(-1000, 1000), 
                  random.randint(-1000, 1000)) for _ in range(test_size)]
    
    methods = [
        ("If-Else Method", lambda a,b,c: a if a > b and a > c else (b if b > a and b > c else c)),
        ("Sequential Method", lambda a,b,c: max(max(a, b), c)),
        ("Built-in max()", lambda a,b,c: max(a, b, c)),
        ("Ternary Operator", lambda a,b,c: (a if a > b else b) if (a if a > b else b) > c else c)
    ]
    
    print(f"   Testing with {test_size:,} random number triplets...")
    
    results = []
    
    for name, method in methods:
        start_time = time.time()
        
        for a, b, c in test_data:
            result = method(a, b, c)
        
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convert to ms
        
        results.append((name, execution_time))
        print(f"   {name}: {execution_time:.2f} ms")
    
    # Find fastest method
    fastest = min(results, key=lambda x: x[1])
    print(f"\n   🏆 Fastest method: {fastest[0]} ({fastest[1]:.2f} ms)")
    
    return results

# =============================================================================
# INTERACTIVE DEMONSTRATIONS
# =============================================================================

def interactive_comparison_demo():
    """
    Interactive demonstration of different comparison methods
    """
    print(f"\n🎮 INTERACTIVE COMPARISON DEMO")
    print("=" * 30)
    
    while True:
        try:
            print(f"\n🎯 Choose an option:")
            print("   1. Enter three numbers manually")
            print("   2. Generate random numbers")
            print("   3. Test edge cases")
            print("   4. Performance comparison")
            print("   5. Learn about comparisons")
            print("   6. Exit")
            
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == "1":
                print("\nEnter three numbers:")
                a = float(input("First number: "))
                b = float(input("Second number: "))
                c = float(input("Third number: "))
                
                print(f"\n🔍 Finding largest of {a}, {b}, {c}:")
                
                # Demonstrate all methods
                find_largest_basic_if_else(a, b, c)
                find_largest_sequential(a, b, c)
                find_largest_builtin(a, b, c)
                find_largest_ternary(a, b, c)
                
                # Handle edge cases
                result, message = find_largest_with_edge_cases(a, b, c)
                print(f"\n📋 Summary: {message}")
                
            elif choice == "2":
                # Generate random numbers
                import random
                a = random.randint(-50, 50)
                b = random.randint(-50, 50)
                c = random.randint(-50, 50)
                
                print(f"\n🎲 Random numbers generated: {a}, {b}, {c}")
                
                # Quick comparison
                result = find_largest_builtin(a, b, c)
                
            elif choice == "3":
                print("\n🧪 Testing Edge Cases:")
                handle_special_inputs()
                
            elif choice == "4":
                compare_methods_performance()
                
            elif choice == "5":
                explain_comparison_concepts()
                
            elif choice == "6":
                print("\n👋 Thanks for exploring comparisons!")
                break
                
            else:
                print("❌ Invalid choice. Please choose 1-6.")
                
        except ValueError:
            print("❌ Please enter valid numbers!")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break

# =============================================================================
# PRACTICAL APPLICATIONS
# =============================================================================

def practical_applications():
    """
    Show practical applications of maximum finding
    """
    print(f"\n🎯 PRACTICAL APPLICATIONS")
    print("=" * 25)
    
    print("\n1️⃣ Grade Analysis:")
    grades = [85, 92, 78]
    highest_grade = max(grades)
    print(f"   Student grades: {grades}")
    print(f"   Highest grade: {highest_grade}")
    
    print("\n2️⃣ Temperature Monitoring:")
    temperatures = [23.5, 25.8, 21.2]  # Celsius
    max_temp = max(temperatures)
    print(f"   Daily temperatures: {temperatures}°C")
    print(f"   Maximum temperature: {max_temp}°C")
    
    print("\n3️⃣ Sales Performance:")
    sales_q1, sales_q2, sales_q3 = 15000, 18500, 16200
    best_quarter = max(sales_q1, sales_q2, sales_q3)
    quarter = "Q1" if best_quarter == sales_q1 else ("Q2" if best_quarter == sales_q2 else "Q3")
    print(f"   Quarterly sales: Q1=${sales_q1:,}, Q2=${sales_q2:,}, Q3=${sales_q3:,}")
    print(f"   Best performing quarter: {quarter} with ${best_quarter:,}")
    
    print("\n4️⃣ Resource Allocation:")
    cpu_usage = [75.2, 82.1, 69.8]  # Percentage
    peak_usage = max(cpu_usage)
    print(f"   CPU usage over time: {cpu_usage}%")
    print(f"   Peak CPU usage: {peak_usage}%")

if __name__ == "__main__":
    """
    Main execution demonstrating various approaches to find the largest number
    """
    print(__doc__)
    
    # Educational content
    explain_comparison_concepts()
    
    # Demonstrate different methods with sample data
    sample_numbers = [(15, 8, 23), (7, 12, 7), (-5, -2, -8), (10, 10, 10)]
    
    for a, b, c in sample_numbers:
        print(f"\n" + "="*60)
        print(f"DEMONSTRATION: Finding largest of {a}, {b}, {c}")
        print("="*60)
        
        # Show different approaches
        find_largest_basic_if_else(a, b, c)
        find_largest_sequential(a, b, c)
        find_largest_builtin(a, b, c)
        find_largest_ternary(a, b, c)
        find_largest_mathematical(a, b, c)
        find_largest_list_approach(a, b, c)
        
        # Handle edge cases
        result, message = find_largest_with_edge_cases(a, b, c)
        print(f"\n📋 Analysis: {message}")
    
    # Show practical applications
    practical_applications()
    
    # Performance comparison
    compare_methods_performance()
    
    # Interactive demonstration
    interactive_comparison_demo()
    
    print("\n" + "=" * 50)
    print("🎓 LEARNING SUMMARY")
    print("=" * 50)
    print("✅ Understanding of comparison operators and logic")
    print("✅ Multiple approaches to find maximum values")
    print("✅ Edge case handling and robust programming")
    print("✅ Performance analysis and method comparison")
    print("✅ Real-world applications of comparison logic")
    
    print("\n💡 Key Concepts Learned:")
    print("• Conditional statements and logical operators")
    print("• Multiple algorithmic approaches to same problem")
    print("• Built-in functions vs custom implementations")
    print("• Edge case identification and handling")
    print("• Performance considerations in algorithm choice")
    
    print("\n🎯 Next Steps:")
    print("• Explore sorting algorithms for multiple values")
    print("• Study advanced comparison techniques")
    print("• Learn about custom comparison functions")
    print("• Investigate min-max algorithms for arrays")
    