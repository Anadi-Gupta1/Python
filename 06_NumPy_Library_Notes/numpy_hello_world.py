"""
NumPy Hello World - Introduction to NumPy Scientific Computing
============================================================

Complete introduction to NumPy (Numerical Python) library covering installation,
basic concepts, array creation, fundamental operations, and practical examples
for scientific computing and data analysis applications.

Author: Python Learning Notes
Date: September 2025
Topic: NumPy Introduction, Scientific Computing, Array Operations
"""

import numpy as np
import sys
import time
from typing import List, Tuple, Any, Optional
import matplotlib.pyplot as plt

# =============================================================================
# NUMPY INTRODUCTION AND CONCEPTS
# =============================================================================

def introduce_numpy():
    """
    Educational introduction to NumPy and its importance
    """
    print("🚀 WELCOME TO NUMPY!")
    print("=" * 20)
    
    print("\n🔬 What is NumPy?")
    print("NumPy (Numerical Python) is the fundamental package for:")
    print("   • Scientific computing with Python")
    print("   • Large, multi-dimensional arrays and matrices")
    print("   • Mathematical functions to operate on arrays")
    print("   • Tools for integrating C/C++ and Fortran code")
    print("   • Linear algebra, Fourier transform, and random number capabilities")
    
    print(f"\n📦 NumPy Installation Check:")
    print(f"   NumPy Version: {np.__version__}")
    print(f"   Python Version: {sys.version}")
    print(f"   NumPy Location: {np.__file__}")
    
    print(f"\n⚡ Why Choose NumPy?")
    advantages = [
        ("Speed", "50-100x faster than pure Python"),
        ("Memory", "Much more memory efficient"),
        ("Vectorization", "Apply operations to entire arrays"),
        ("Broadcasting", "Operations on different shaped arrays"),
        ("Ecosystem", "Foundation for pandas, scikit-learn, matplotlib"),
        ("C Integration", "Easy integration with C/C++ libraries")
    ]
    
    print("   ┌─────────────────┬─────────────────────────────────┐")
    print("   │ Feature         │ Advantage                       │")
    print("   ├─────────────────┼─────────────────────────────────┤")
    for feature, advantage in advantages:
        print(f"   │ {feature:<15} │ {advantage:<31} │")
    print("   └─────────────────┴─────────────────────────────────┘")

def compare_python_vs_numpy():
    """
    Demonstrate performance differences between Python lists and NumPy arrays
    """
    print("\n⚡ PERFORMANCE COMPARISON: Python Lists vs NumPy Arrays")
    print("=" * 55)
    
    # Test data size
    size = 1000000
    
    print(f"Testing with {size:,} elements...")
    
    # Python lists
    print("\n🐍 Python Lists:")
    python_list1 = list(range(size))
    python_list2 = list(range(size, 2 * size))
    
    start_time = time.time()
    python_result = [x + y for x, y in zip(python_list1, python_list2)]
    python_time = (time.time() - start_time) * 1000
    
    print(f"   Creation and addition: {python_time:.2f} ms")
    print(f"   Memory usage: {sys.getsizeof(python_result):,} bytes")
    
    # NumPy arrays
    print("\n🔢 NumPy Arrays:")
    numpy_array1 = np.arange(size)
    numpy_array2 = np.arange(size, 2 * size)
    
    start_time = time.time()
    numpy_result = numpy_array1 + numpy_array2
    numpy_time = (time.time() - start_time) * 1000
    
    print(f"   Creation and addition: {numpy_time:.2f} ms")
    print(f"   Memory usage: {numpy_result.nbytes:,} bytes")
    
    # Performance comparison
    speedup = python_time / numpy_time if numpy_time > 0 else float('inf')
    memory_ratio = sys.getsizeof(python_result) / numpy_result.nbytes
    
    print(f"\n📊 Performance Results:")
    print(f"   Speed improvement: {speedup:.1f}x faster with NumPy")
    print(f"   Memory efficiency: {memory_ratio:.1f}x less memory with NumPy")
    
    # Verify results are identical
    verification = all(p == n for p, n in zip(python_result[:10], numpy_result[:10]))
    print(f"   Results identical: {'✅ Yes' if verification else '❌ No'}")

# =============================================================================
# BASIC NUMPY ARRAY OPERATIONS
# =============================================================================

def demonstrate_array_creation():
    """
    Demonstrate various ways to create NumPy arrays
    """
    print("\n🎨 ARRAY CREATION METHODS")
    print("=" * 25)
    
    # From Python lists
    print("\n1️⃣  From Python Lists:")
    list_1d = [1, 2, 3, 4, 5]
    array_1d = np.array(list_1d)
    print(f"   List: {list_1d}")
    print(f"   Array: {array_1d}")
    print(f"   Shape: {array_1d.shape}, Dtype: {array_1d.dtype}")
    
    # 2D array from nested lists
    list_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    array_2d = np.array(list_2d)
    print(f"\n   2D List: {list_2d}")
    print(f"   2D Array:\n{array_2d}")
    print(f"   Shape: {array_2d.shape}, Dtype: {array_2d.dtype}")
    
    # Built-in creation functions
    print("\n2️⃣  Built-in Creation Functions:")
    
    # Zeros, ones, and empty arrays
    zeros = np.zeros((2, 3))
    ones = np.ones((2, 3))
    empty = np.empty((2, 3))
    
    print(f"   Zeros (2x3):\n{zeros}")
    print(f"   Ones (2x3):\n{ones}")
    print(f"   Empty (2x3):\n{empty}")
    
    # Range-based arrays
    print("\n3️⃣  Range-based Arrays:")
    
    arange_array = np.arange(0, 10, 2)
    linspace_array = np.linspace(0, 1, 5)
    
    print(f"   arange(0, 10, 2): {arange_array}")
    print(f"   linspace(0, 1, 5): {linspace_array}")
    
    # Special arrays
    print("\n4️⃣  Special Arrays:")
    
    identity = np.eye(3)
    full = np.full((2, 3), 7)
    
    print(f"   Identity (3x3):\n{identity}")
    print(f"   Full (2x3, value=7):\n{full}")

def demonstrate_array_properties():
    """
    Demonstrate NumPy array properties and attributes
    """
    print("\n📏 ARRAY PROPERTIES AND ATTRIBUTES")
    print("=" * 35)
    
    # Create sample arrays
    array_1d = np.array([1, 2, 3, 4, 5])
    array_2d = np.array([[1, 2, 3], [4, 5, 6]])
    array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    
    arrays = [
        ("1D Array", array_1d),
        ("2D Array", array_2d),
        ("3D Array", array_3d)
    ]
    
    for name, arr in arrays:
        print(f"\n🔍 {name}: {arr.flatten()}")
        print(f"   Shape: {arr.shape}")
        print(f"   Size: {arr.size}")
        print(f"   Dimensions: {arr.ndim}")
        print(f"   Data type: {arr.dtype}")
        print(f"   Item size: {arr.itemsize} bytes")
        print(f"   Total bytes: {arr.nbytes} bytes")
        print(f"   Memory layout: {'C-contiguous' if arr.flags['C_CONTIGUOUS'] else 'Not C-contiguous'}")

def demonstrate_basic_operations():
    """
    Demonstrate basic mathematical operations with NumPy arrays
    """
    print("\n🧮 BASIC MATHEMATICAL OPERATIONS")
    print("=" * 32)
    
    # Create sample arrays
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([10, 20, 30, 40, 50])
    
    print(f"Array a: {a}")
    print(f"Array b: {b}")
    
    # Basic arithmetic operations
    print(f"\n➕ Addition (a + b): {a + b}")
    print(f"➖ Subtraction (a - b): {a - b}")
    print(f"✖️  Multiplication (a * b): {a * b}")
    print(f"➗ Division (a / b): {a / b}")
    print(f"⚡ Power (a ** 2): {a ** 2}")
    print(f"📐 Square root (√a): {np.sqrt(a)}")
    
    # Scalar operations
    print(f"\n🔢 Scalar Operations:")
    print(f"   a + 10: {a + 10}")
    print(f"   a * 3: {a * 3}")
    print(f"   a / 2: {a / 2}")
    
    # Statistical operations
    print(f"\n📊 Statistical Operations:")
    print(f"   Sum: {np.sum(a)}")
    print(f"   Mean: {np.mean(a):.2f}")
    print(f"   Standard deviation: {np.std(a):.2f}")
    print(f"   Minimum: {np.min(a)}")
    print(f"   Maximum: {np.max(a)}")
    print(f"   Median: {np.median(a):.2f}")

def demonstrate_array_indexing():
    """
    Demonstrate array indexing and slicing operations
    """
    print("\n🎯 ARRAY INDEXING AND SLICING")
    print("=" * 30)
    
    # 1D array indexing
    arr_1d = np.array([10, 20, 30, 40, 50])
    print(f"1D Array: {arr_1d}")
    print(f"   First element [0]: {arr_1d[0]}")
    print(f"   Last element [-1]: {arr_1d[-1]}")
    print(f"   Slice [1:4]: {arr_1d[1:4]}")
    print(f"   Every 2nd element [::2]: {arr_1d[::2]}")
    
    # 2D array indexing
    arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"\n2D Array:\n{arr_2d}")
    print(f"   Element [1,2]: {arr_2d[1, 2]}")
    print(f"   First row [0,:]: {arr_2d[0, :]}")
    print(f"   Last column [:,-1]: {arr_2d[:, -1]}")
    print(f"   Sub-array [0:2, 1:3]:\n{arr_2d[0:2, 1:3]}")
    
    # Boolean indexing
    print(f"\n🔍 Boolean Indexing:")
    condition = arr_1d > 25
    print(f"   Condition (arr_1d > 25): {condition}")
    print(f"   Filtered values: {arr_1d[condition]}")
    
    # Fancy indexing
    indices = [0, 2, 4]
    print(f"   Fancy indexing [0,2,4]: {arr_1d[indices]}")

# =============================================================================
# PRACTICAL NUMPY EXAMPLES
# =============================================================================

def demonstrate_practical_examples():
    """
    Demonstrate practical NumPy applications
    """
    print("\n🛠️  PRACTICAL NUMPY APPLICATIONS")
    print("=" * 32)
    
    # Example 1: Grade analysis
    print("\n📚 Example 1: Student Grade Analysis")
    print("-" * 35)
    
    # Student scores in different subjects
    students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    subjects = ["Math", "Physics", "Chemistry", "Biology"]
    
    # Random grades (for demonstration)
    np.random.seed(42)  # For reproducible results
    grades = np.random.randint(60, 100, (5, 4))
    
    print("Grade Matrix (Students × Subjects):")
    print(f"Students: {students}")
    print(f"Subjects: {subjects}")
    print(grades)
    
    # Analysis
    student_averages = np.mean(grades, axis=1)
    subject_averages = np.mean(grades, axis=0)
    
    print(f"\n📊 Analysis Results:")
    for i, (student, avg) in enumerate(zip(students, student_averages)):
        print(f"   {student}: {avg:.1f} average")
    
    print(f"\n   Subject averages:")
    for subject, avg in zip(subjects, subject_averages):
        print(f"   {subject}: {avg:.1f}")
    
    print(f"   Highest grade: {np.max(grades)}")
    print(f"   Lowest grade: {np.min(grades)}")
    print(f"   Overall average: {np.mean(grades):.1f}")
    
    # Example 2: Temperature conversion
    print("\n🌡️  Example 2: Temperature Conversion")
    print("-" * 36)
    
    # Fahrenheit temperatures
    fahrenheit = np.array([32, 68, 86, 104, 122])
    
    # Convert to Celsius using vectorized operation
    celsius = (fahrenheit - 32) * 5/9
    
    print("Temperature Conversion (Fahrenheit → Celsius):")
    for f, c in zip(fahrenheit, celsius):
        print(f"   {f}°F = {c:.1f}°C")
    
    # Example 3: Matrix operations
    print("\n🔢 Example 3: Matrix Operations")
    print("-" * 30)
    
    # Create matrices
    matrix_a = np.array([[1, 2], [3, 4]])
    matrix_b = np.array([[5, 6], [7, 8]])
    
    print(f"Matrix A:\n{matrix_a}")
    print(f"Matrix B:\n{matrix_b}")
    
    # Matrix operations
    print(f"\nMatrix Addition:\n{matrix_a + matrix_b}")
    print(f"\nMatrix Multiplication:\n{np.dot(matrix_a, matrix_b)}")
    print(f"\nMatrix A Transpose:\n{matrix_a.T}")
    print(f"\nMatrix A Determinant: {np.linalg.det(matrix_a):.2f}")

def create_visualization_example():
    """
    Create a simple visualization using NumPy and matplotlib
    """
    print("\n📈 VISUALIZATION EXAMPLE")
    print("=" * 23)
    
    # Generate data
    x = np.linspace(0, 2 * np.pi, 100)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    y_tan = np.tan(x)
    
    print("Generated trigonometric data:")
    print(f"   X values: {len(x)} points from 0 to 2π")
    print(f"   Functions: sin(x), cos(x), tan(x)")
    
    # Display sample values
    sample_indices = [0, 25, 50, 75, 99]
    print(f"\n   Sample values:")
    print("   ┌─────────┬─────────┬─────────┬─────────┐")
    print("   │ x       │ sin(x)  │ cos(x)  │ tan(x)  │")
    print("   ├─────────┼─────────┼─────────┼─────────┤")
    
    for i in sample_indices:
        # Clip tan values for display
        tan_val = np.clip(y_tan[i], -10, 10)
        print(f"   │ {x[i]:7.2f} │ {y_sin[i]:7.2f} │ {y_cos[i]:7.2f} │ {tan_val:7.2f} │")
    
    print("   └─────────┴─────────┴─────────┴─────────┘")
    
    # Statistics
    print(f"\n   📊 Statistics:")
    print(f"   Sin - Min: {np.min(y_sin):.2f}, Max: {np.max(y_sin):.2f}")
    print(f"   Cos - Min: {np.min(y_cos):.2f}, Max: {np.max(y_cos):.2f}")
    
    print(f"   💡 Note: Run with matplotlib to create actual plots!")

# =============================================================================
# INTERACTIVE LEARNING TOOLS
# =============================================================================

def numpy_quiz():
    """
    Interactive NumPy knowledge quiz
    """
    print("\n🎓 NUMPY KNOWLEDGE QUIZ")
    print("=" * 23)
    
    questions = [
        {
            "question": "What does NumPy stand for?",
            "options": ["Number Python", "Numerical Python", "New Python", "Numeric Python"],
            "correct": 1,
            "explanation": "NumPy stands for 'Numerical Python' - it's the fundamental package for scientific computing."
        },
        {
            "question": "Which function creates an array of zeros?",
            "options": ["np.empty()", "np.zeros()", "np.null()", "np.void()"],
            "correct": 1,
            "explanation": "np.zeros() creates an array filled with zeros."
        },
        {
            "question": "What is the main advantage of NumPy arrays over Python lists?",
            "options": ["Easier syntax", "Better speed and memory efficiency", "More functions", "Prettier output"],
            "correct": 1,
            "explanation": "NumPy arrays are much faster and more memory efficient than Python lists."
        }
    ]
    
    score = 0
    
    for i, q in enumerate(questions, 1):
        print(f"\n❓ Question {i}: {q['question']}")
        
        for j, option in enumerate(q['options']):
            print(f"   {j + 1}. {option}")
        
        try:
            answer = int(input("   Your answer (1-4): ")) - 1
            
            if answer == q['correct']:
                print("   ✅ Correct!")
                score += 1
            else:
                correct_answer = q['options'][q['correct']]
                print(f"   ❌ Incorrect. The correct answer is: {correct_answer}")
            
            print(f"   💡 Explanation: {q['explanation']}")
            
        except (ValueError, IndexError):
            print("   ❌ Invalid input. Skipping question.")
    
    print(f"\n🏆 Final Score: {score}/{len(questions)}")
    
    if score == len(questions):
        print("   🎉 Perfect score! You're a NumPy master!")
    elif score >= len(questions) * 0.7:
        print("   👏 Great job! You have a good understanding of NumPy!")
    else:
        print("   📚 Keep learning! Review the concepts and try again.")

def interactive_numpy_playground():
    """
    Interactive playground for experimenting with NumPy
    """
    print("\n🎮 NUMPY INTERACTIVE PLAYGROUND")
    print("=" * 30)
    
    while True:
        try:
            print("\n🎯 Choose an operation:")
            print("   1. Create arrays")
            print("   2. Array operations")
            print("   3. Array properties")
            print("   4. Mathematical functions")
            print("   5. Random arrays")
            print("   6. Take the quiz")
            print("   7. Exit playground")
            
            choice = input("\nEnter your choice (1-7): ").strip()
            
            if choice == "1":
                print("\n🎨 Array Creation:")
                shape = input("Enter shape (e.g., '3,4' for 3x4): ").strip()
                try:
                    shape_tuple = tuple(map(int, shape.split(',')))
                    array = np.random.randint(1, 10, shape_tuple)
                    print(f"Created array:\n{array}")
                    print(f"Shape: {array.shape}, Type: {array.dtype}")
                except ValueError:
                    print("Invalid shape format. Use comma-separated integers.")
            
            elif choice == "2":
                print("\n🧮 Array Operations:")
                a = np.array([1, 2, 3, 4, 5])
                b = np.array([6, 7, 8, 9, 10])
                
                operations = {
                    "Addition": a + b,
                    "Multiplication": a * b,
                    "Power": a ** 2,
                    "Square root": np.sqrt(a)
                }
                
                for op_name, result in operations.items():
                    print(f"   {op_name}: {result}")
            
            elif choice == "3":
                print("\n📏 Array Properties:")
                array = np.random.randint(1, 100, (3, 4, 2))
                print(f"Sample array shape: {array.shape}")
                print(f"Size: {array.size}")
                print(f"Dimensions: {array.ndim}")
                print(f"Data type: {array.dtype}")
            
            elif choice == "4":
                print("\n📊 Mathematical Functions:")
                x = np.array([1, 4, 9, 16, 25])
                functions = {
                    "Square root": np.sqrt(x),
                    "Natural log": np.log(x),
                    "Exponential": np.exp([1, 2, 3]),
                    "Sine": np.sin([0, np.pi/2, np.pi])
                }
                
                for func_name, result in functions.items():
                    print(f"   {func_name}: {result}")
            
            elif choice == "5":
                print("\n🎲 Random Arrays:")
                size = int(input("Enter size: "))
                
                arrays = {
                    "Random integers (1-10)": np.random.randint(1, 11, size),
                    "Random floats (0-1)": np.random.random(size),
                    "Normal distribution": np.random.normal(0, 1, size)
                }
                
                for array_name, array in arrays.items():
                    print(f"   {array_name}: {array}")
            
            elif choice == "6":
                numpy_quiz()
            
            elif choice == "7":
                print("\n👋 Thanks for exploring NumPy! Keep practicing!")
                break
            
            else:
                print("❌ Invalid choice. Please choose 1-7.")
                
        except ValueError:
            print("❌ Please enter valid numbers!")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

# =============================================================================
# MAIN EXECUTION AND DEMONSTRATION
# =============================================================================

def main():
    """
    Main function demonstrating all NumPy concepts
    """
    print(__doc__)
    
    # Introduction and concepts
    introduce_numpy()
    
    # Performance comparison
    compare_python_vs_numpy()
    
    # Basic operations
    demonstrate_array_creation()
    demonstrate_array_properties()
    demonstrate_basic_operations()
    demonstrate_array_indexing()
    
    # Practical examples
    demonstrate_practical_examples()
    create_visualization_example()
    
    # Interactive components
    interactive_numpy_playground()

if __name__ == "__main__":
    """
    Execute the complete NumPy Hello World tutorial
    """
    main()
    
    print("\n" + "=" * 50)
    print("🎓 NUMPY LEARNING SUMMARY")
    print("=" * 50)
    print("✅ NumPy installation and setup verification")
    print("✅ Performance advantages over pure Python")
    print("✅ Array creation methods and techniques")
    print("✅ Array properties and attributes mastery")
    print("✅ Mathematical operations and functions")
    print("✅ Indexing, slicing, and array manipulation")
    print("✅ Practical applications and real-world examples")
    print("✅ Interactive learning and knowledge assessment")
    
    print("\n💡 Key Concepts Mastered:")
    print("• NumPy array fundamentals and advantages")
    print("• Vectorized operations for performance")
    print("• Multi-dimensional array handling")
    print("• Mathematical and statistical functions")
    print("• Array creation and manipulation techniques")
    print("• Memory efficiency and optimization")
    
    print("\n🎯 Next Steps in NumPy Learning:")
    print("• Advanced indexing and broadcasting")
    print("• Linear algebra operations")
    print("• File I/O with NumPy")
    print("• Integration with other scientific libraries")
    print("• Performance optimization techniques")
    print("• Custom ufuncs and advanced operations")