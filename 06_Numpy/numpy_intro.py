"""
NumPy Introduction and Fundamentals
==================================

This module provides a comprehensive introduction to NumPy (Numerical Python),
the fundamental package for scientific computing in Python.

Author: Anadi Gupta
Date: September 2025
Purpose: Educational introduction to NumPy concepts and usage
"""

import numpy as np
import sys

def display_numpy_info():
    """Display basic information about NumPy installation and capabilities"""
    print("🔢 NumPy Introduction")
    print("=" * 50)
    
    print("\n📚 What is NumPy?")
    print("NumPy is a Python library used for working with arrays and mathematical operations.")
    print("It provides:")
    print("• Fast array operations")
    print("• Linear algebra functions")
    print("• Fourier transform capabilities")
    print("• Matrix operations")
    print("• Broadcasting capabilities")
    
    print(f"\n📊 Current NumPy Version: {np.__version__}")
    print(f"🐍 Python Version: {sys.version}")
    
    print("\n🚀 Why Use NumPy?")
    print("• Performance: Up to 50x faster than Python lists")
    print("• Memory Efficient: Optimized storage for large datasets")
    print("• Vectorization: Perform operations on entire arrays")
    print("• Scientific Computing: Foundation for data science libraries")
    print("• Broadcasting: Operations between arrays of different shapes")

def demonstrate_speed_comparison():
    """Demonstrate speed difference between Python lists and NumPy arrays"""
    print("\n⚡ Performance Comparison")
    print("-" * 30)
    
    import time
    
    # Create large datasets
    size = 1000000
    python_list = list(range(size))
    numpy_array = np.arange(size)
    
    # Time Python list operation
    start_time = time.time()
    python_result = [x * 2 for x in python_list]
    python_time = time.time() - start_time
    
    # Time NumPy array operation
    start_time = time.time()
    numpy_result = numpy_array * 2
    numpy_time = time.time() - start_time
    
    print(f"📋 Python List Time: {python_time:.4f} seconds")
    print(f"🔢 NumPy Array Time: {numpy_time:.4f} seconds")
    print(f"🏆 Speed Improvement: {python_time/numpy_time:.1f}x faster")

def demonstrate_basic_concepts():
    """Demonstrate basic NumPy concepts"""
    print("\n🎯 Basic NumPy Concepts")
    print("-" * 25)
    
    # Create arrays
    print("1. Creating Arrays:")
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    
    print(f"   1D Array: {arr1}")
    print(f"   2D Array:\n{arr2}")
    
    # Array properties
    print(f"\n2. Array Properties:")
    print(f"   Shape: {arr2.shape}")
    print(f"   Size: {arr2.size}")
    print(f"   Data type: {arr2.dtype}")
    print(f"   Dimensions: {arr2.ndim}")
    
    # Basic operations
    print(f"\n3. Basic Operations:")
    print(f"   Array + 10: {arr1 + 10}")
    print(f"   Array * 2: {arr1 * 2}")
    print(f"   Sum: {np.sum(arr1)}")
    print(f"   Mean: {np.mean(arr1)}")

def main():
    """Main function to run NumPy introduction"""
    try:
        display_numpy_info()
        demonstrate_speed_comparison()
        demonstrate_basic_concepts()
        
        print("\n✨ NumPy Introduction Complete!")
        print("\n📋 Key Takeaways:")
        print("• NumPy is essential for scientific computing in Python")
        print("• Arrays are much faster than Python lists")
        print("• NumPy provides powerful mathematical functions")
        print("• It's the foundation for data science in Python")
        
    except ImportError:
        print("❌ NumPy is not installed. Install it using: pip install numpy")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()