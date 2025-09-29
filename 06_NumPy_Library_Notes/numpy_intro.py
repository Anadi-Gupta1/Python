"""
NumPy Introduction - Scientific Computing Foundation
=================================================

Comprehensive introduction to NumPy (Numerical Python), the fundamental
package for scientific computing in Python. This guide covers what NumPy is,
why it's important, and how it revolutionizes numerical computing.

Author: Python Learning Notes
Date: September 2025
Topic: NumPy Introduction, Scientific Computing, Arrays
"""

import numpy as np
import sys
import time

# =============================================================================
# WHAT IS NUMPY?
# =============================================================================

def introduction_to_numpy():
    """
    Introduction to NumPy and its significance in Python ecosystem
    """
    print("🔢 NUMPY INTRODUCTION")
    print("=" * 30)
    
    print("\n📚 What is NumPy?")
    print("NumPy (Numerical Python) is a powerful library for:")
    print("   • Working with multi-dimensional arrays")
    print("   • Mathematical and logical operations on arrays")
    print("   • Linear algebra, Fourier transforms, and random operations")
    print("   • Integration with C/C++ and Fortran code")
    print("   • Foundation for other scientific Python libraries")
    
    print(f"\n📊 Current NumPy Version: {np.__version__}")
    
    print("\n🎯 Key Features:")
    print("   ✅ N-dimensional array object (ndarray)")
    print("   ✅ Broadcasting functions")
    print("   ✅ Tools for integrating C/C++ and Fortran code")
    print("   ✅ Linear algebra and random number capabilities")
    print("   ✅ Fourier transform and signal processing")

def numpy_history_and_ecosystem():
    """
    Brief history of NumPy and its role in scientific Python ecosystem
    """
    print("\n📅 NUMPY HISTORY & ECOSYSTEM")
    print("=" * 35)
    
    print("🕰️  History:")
    print("   • Created in 2005 by Travis Oliphant")
    print("   • Built on earlier libraries (Numeric and Numarray)")
    print("   • Open source project with BSD license")
    print("   • Actively maintained by a global community")
    
    print("\n🌐 Scientific Python Ecosystem:")
    ecosystem = {
        "NumPy": "Foundation - arrays and mathematical functions",
        "Pandas": "Data analysis and manipulation",
        "Matplotlib": "Data visualization and plotting",
        "SciPy": "Scientific and technical computing",
        "Scikit-learn": "Machine learning library",
        "TensorFlow/PyTorch": "Deep learning frameworks"
    }
    
    for package, description in ecosystem.items():
        print(f"   📦 {package}: {description}")

# =============================================================================
# WHY USE NUMPY?
# =============================================================================

def why_use_numpy():
    """
    Demonstrate why NumPy is essential for numerical computing
    """
    print("\n⚡ WHY USE NUMPY?")
    print("=" * 20)
    
    print("🐌 Problems with Python Lists:")
    print("   • Slow for numerical operations")
    print("   • Memory inefficient")
    print("   • No built-in mathematical operations")
    print("   • Type checking overhead")
    print("   • No broadcasting capabilities")
    
    print("\n🚀 NumPy Advantages:")
    print("   • Up to 50x faster than Python lists")
    print("   • Memory efficient (homogeneous data)")
    print("   • Vectorized operations (no explicit loops)")
    print("   • Broadcasting for different sized arrays")
    print("   • Rich mathematical function library")
    
    # Performance comparison
    print("\n📈 PERFORMANCE COMPARISON:")
    demonstrate_performance()

def demonstrate_performance():
    """
    Practical demonstration of NumPy vs Python list performance
    """
    size = 1000000
    
    # Python list approach
    python_list = list(range(size))
    start_time = time.time()
    python_result = [x * 2 for x in python_list]
    python_time = time.time() - start_time
    
    # NumPy approach
    numpy_array = np.arange(size)
    start_time = time.time()
    numpy_result = numpy_array * 2
    numpy_time = time.time() - start_time
    
    # Memory usage
    python_memory = sys.getsizeof(python_list)
    numpy_memory = numpy_array.nbytes
    
    print(f"   📊 Performance Test (1M elements):")
    print(f"   Python List: {python_time:.4f} seconds")
    print(f"   NumPy Array: {numpy_time:.4f} seconds")
    print(f"   Speed improvement: {python_time/numpy_time:.1f}x faster")
    
    print(f"\n   💾 Memory Usage:")
    print(f"   Python List: {python_memory:,} bytes")
    print(f"   NumPy Array: {numpy_memory:,} bytes")
    print(f"   Memory efficiency: {python_memory/numpy_memory:.1f}x less memory")

# =============================================================================
# NUMPY NDARRAY FUNDAMENTALS
# =============================================================================

def introduce_ndarray():
    """
    Introduction to NumPy's core data structure - ndarray
    """
    print("\n🧮 NUMPY NDARRAY FUNDAMENTALS")
    print("=" * 35)
    
    print("📝 What is ndarray?")
    print("   • N-dimensional array object")
    print("   • Homogeneous data (same type)")
    print("   • Fixed size at creation")
    print("   • Elements accessed via indexing")
    print("   • Efficient storage and operations")
    
    # Create examples of different dimensional arrays
    print("\n🔍 Array Dimensions Examples:")
    
    # 0-D Array (scalar)
    scalar = np.array(42)
    print(f"   0-D Array (scalar): {scalar}")
    print(f"     Shape: {scalar.shape}, Dimensions: {scalar.ndim}")
    
    # 1-D Array (vector)
    vector = np.array([1, 2, 3, 4, 5])
    print(f"   1-D Array (vector): {vector}")
    print(f"     Shape: {vector.shape}, Dimensions: {vector.ndim}")
    
    # 2-D Array (matrix)
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"   2-D Array (matrix):")
    print(f"{matrix}")
    print(f"     Shape: {matrix.shape}, Dimensions: {matrix.ndim}")
    
    # 3-D Array (tensor)
    tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print(f"   3-D Array (tensor):")
    print(f"{tensor}")
    print(f"     Shape: {tensor.shape}, Dimensions: {tensor.ndim}")

def array_attributes_and_properties():
    """
    Explore important attributes and properties of NumPy arrays
    """
    print("\n🔍 ARRAY ATTRIBUTES & PROPERTIES")
    print("=" * 40)
    
    # Create sample array
    sample_array = np.array([[1, 2, 3, 4], 
                            [5, 6, 7, 8], 
                            [9, 10, 11, 12]], dtype=np.float64)
    
    print("Sample Array:")
    print(sample_array)
    
    print(f"\n📊 Key Attributes:")
    print(f"   • Shape: {sample_array.shape}")
    print(f"   • Size: {sample_array.size}")
    print(f"   • Dimensions: {sample_array.ndim}")
    print(f"   • Data type: {sample_array.dtype}")
    print(f"   • Item size: {sample_array.itemsize} bytes")
    print(f"   • Total bytes: {sample_array.nbytes} bytes")
    print(f"   • Memory layout: {'C' if sample_array.flags.c_contiguous else 'F'}-contiguous")

# =============================================================================
# DATA TYPES IN NUMPY
# =============================================================================

def numpy_data_types():
    """
    Explore NumPy data types and their importance
    """
    print("\n🏷️  NUMPY DATA TYPES")
    print("=" * 25)
    
    print("📝 Why Data Types Matter:")
    print("   • Memory efficiency")
    print("   • Computational speed")
    print("   • Numerical precision")
    print("   • Hardware optimization")
    
    # Common NumPy data types
    data_types = {
        'np.int8': 'Integer (-128 to 127)',
        'np.int16': 'Integer (-32,768 to 32,767)',
        'np.int32': 'Integer (-2^31 to 2^31-1)',
        'np.int64': 'Integer (64-bit)',
        'np.uint8': 'Unsigned integer (0 to 255)',
        'np.float16': 'Half precision float',
        'np.float32': 'Single precision float',
        'np.float64': 'Double precision float (default)',
        'np.complex64': 'Complex number (32-bit each part)',
        'np.complex128': 'Complex number (64-bit each part)',
        'np.bool_': 'Boolean (True/False)'
    }
    
    print("\n🎯 Common Data Types:")
    for dtype, description in data_types.items():
        print(f"   • {dtype:<15}: {description}")
    
    # Demonstrate data type usage
    print("\n💡 Data Type Examples:")
    
    # Different ways to specify data type
    int_array = np.array([1, 2, 3, 4], dtype=np.int32)
    float_array = np.array([1.1, 2.2, 3.3], dtype=np.float64)
    bool_array = np.array([True, False, True], dtype=np.bool_)
    
    print(f"   Integer array: {int_array} (dtype: {int_array.dtype})")
    print(f"   Float array: {float_array} (dtype: {float_array.dtype})")
    print(f"   Boolean array: {bool_array} (dtype: {bool_array.dtype})")
    
    # Type conversion
    print("\n🔄 Type Conversion:")
    original = np.array([1.7, 2.9, 3.1])
    converted = original.astype(np.int32)
    print(f"   Original: {original} ({original.dtype})")
    print(f"   Converted: {converted} ({converted.dtype})")

# =============================================================================
# DATA SCIENCE CONNECTION
# =============================================================================

def numpy_in_data_science():
    """
    Explain NumPy's role in data science
    """
    print("\n📊 NUMPY IN DATA SCIENCE")
    print("=" * 30)
    
    print("🔬 What is Data Science?")
    print("Data Science is an interdisciplinary field that:")
    print("   • Extracts insights from structured/unstructured data")
    print("   • Uses scientific methods, algorithms, and systems")
    print("   • Combines statistics, mathematics, and computer science")
    print("   • Enables data-driven decision making")
    
    print("\n🎯 NumPy's Role in Data Science Pipeline:")
    pipeline_steps = {
        "1. Data Collection": "Reading data from various sources",
        "2. Data Cleaning": "Handling missing values, outliers",
        "3. Data Transformation": "Reshaping, normalizing, encoding",
        "4. Exploratory Analysis": "Statistical analysis, pattern discovery",
        "5. Modeling": "Machine learning, statistical modeling",
        "6. Visualization": "Creating plots and charts"
    }
    
    for step, description in pipeline_steps.items():
        print(f"   {step}: {description}")
    
    print("\n🌟 Real-world Applications:")
    applications = [
        "🏥 Medical imaging and analysis",
        "📈 Financial modeling and risk analysis",
        "🌦️  Climate and weather prediction",
        "🤖 Machine learning and AI",
        "🔬 Scientific research and simulation",
        "📡 Signal and image processing"
    ]
    
    for app in applications:
        print(f"   {app}")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

def practical_numpy_examples():
    """
    Practical examples showing NumPy in action
    """
    print("\n🌟 PRACTICAL EXAMPLES")
    print("=" * 25)
    
    # Example 1: Simple mathematical operations
    print("\n📐 Example 1: Mathematical Operations")
    
    temperatures_celsius = np.array([0, 10, 20, 30, 40])
    temperatures_fahrenheit = temperatures_celsius * 9/5 + 32
    
    print(f"   Celsius: {temperatures_celsius}")
    print(f"   Fahrenheit: {temperatures_fahrenheit}")
    
    # Example 2: Statistical analysis
    print("\n📊 Example 2: Statistical Analysis")
    
    test_scores = np.array([85, 92, 78, 96, 88, 91, 84, 89, 95, 87])
    
    print(f"   Test Scores: {test_scores}")
    print(f"   Mean: {np.mean(test_scores):.1f}")
    print(f"   Median: {np.median(test_scores):.1f}")
    print(f"   Standard Deviation: {np.std(test_scores):.1f}")
    print(f"   Min: {np.min(test_scores)}, Max: {np.max(test_scores)}")
    
    # Example 3: Matrix operations
    print("\n🔢 Example 3: Matrix Operations")
    
    matrix_a = np.array([[1, 2], [3, 4]])
    matrix_b = np.array([[5, 6], [7, 8]])
    
    print("   Matrix A:")
    print(matrix_a)
    print("   Matrix B:")
    print(matrix_b)
    print("   Matrix Multiplication (A @ B):")
    print(matrix_a @ matrix_b)

if __name__ == "__main__":
    """
    Main execution demonstrating NumPy introduction concepts
    """
    print(__doc__)
    
    # Run all demonstrations
    introduction_to_numpy()
    numpy_history_and_ecosystem()
    why_use_numpy()
    introduce_ndarray()
    array_attributes_and_properties()
    numpy_data_types()
    numpy_in_data_science()
    practical_numpy_examples()
    
    print("\n" + "=" * 50)
    print("🎓 LEARNING SUMMARY")
    print("=" * 50)
    print("✅ Understanding of NumPy's purpose and importance")
    print("✅ Knowledge of performance benefits over Python lists")
    print("✅ Familiarity with ndarray structure and attributes")
    print("✅ Understanding of NumPy data types and their uses")
    print("✅ Awareness of NumPy's role in data science")
    print("✅ Practical examples of NumPy applications")
    
    print("\n💡 Key Takeaways:")
    print("• NumPy is the foundation of scientific Python computing")
    print("• Arrays are much faster and memory-efficient than lists")
    print("• Understanding data types is crucial for optimization")
    print("• NumPy enables vectorized operations and broadcasting")
    print("• Essential for data science, ML, and scientific computing")
    
    print("\n🎯 Next Steps:")
    print("• Learn array creation methods")
    print("• Practice array indexing and slicing")
    print("• Explore mathematical and statistical functions")
    print("• Study broadcasting and advanced operations")
    print("• Apply NumPy to real-world data problems")

Why is NumPy Faster Than Lists?
NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

This behavior is called locality of reference in computer science.

This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.

Which Language is NumPy written in?
NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.

Where is the NumPy Codebase?
The source code for NumPy is located at this github repository https://github.com/numpy/numpy