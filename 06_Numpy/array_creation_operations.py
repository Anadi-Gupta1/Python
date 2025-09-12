"""
NumPy Array Creation Operations
==============================

This module demonstrates various methods for creating NumPy arrays,
covering different dimensions and array creation techniques.

Author: Anadi Gupta
Date: September 2025
Purpose: Comprehensive guide to NumPy array creation methods
"""

import numpy as np

def demonstrate_basic_array_creation():
    """Demonstrate basic array creation from lists and tuples"""
    print("🔢 Basic Array Creation")
    print("=" * 40)
    
    # Create array from list
    list_array = np.array([1, 2, 3, 4, 5])
    print(f"📋 Array from list: {list_array}")
    print(f"   Type: {type(list_array)}")
    print(f"   Data type: {list_array.dtype}")
    
    # Create array from tuple
    tuple_array = np.array((10, 20, 30, 40, 50))
    print(f"\n📦 Array from tuple: {tuple_array}")
    print(f"   Type: {type(tuple_array)}")

def demonstrate_dimensional_arrays():
    """Demonstrate arrays of different dimensions"""
    print("\n📐 Arrays by Dimensions")
    print("=" * 30)
    
    # 0-D Array (Scalar)
    scalar_array = np.array(42)
    print(f"0️⃣ 0-D Array (Scalar): {scalar_array}")
    print(f"   Dimensions: {scalar_array.ndim}")
    print(f"   Shape: {scalar_array.shape}")
    
    # 1-D Array
    array_1d = np.array([1, 2, 3, 4, 5])
    print(f"\n1️⃣ 1-D Array: {array_1d}")
    print(f"   Dimensions: {array_1d.ndim}")
    print(f"   Shape: {array_1d.shape}")
    print(f"   Size: {array_1d.size}")
    
    # 2-D Array (Matrix)
    array_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"\n2️⃣ 2-D Array (Matrix):")
    print(array_2d)
    print(f"   Dimensions: {array_2d.ndim}")
    print(f"   Shape: {array_2d.shape}")
    print(f"   Size: {array_2d.size}")
    
    # 3-D Array (Tensor)
    array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print(f"\n3️⃣ 3-D Array (Tensor):")
    print(array_3d)
    print(f"   Dimensions: {array_3d.ndim}")
    print(f"   Shape: {array_3d.shape}")
    print(f"   Size: {array_3d.size}")

def demonstrate_array_creation_functions():
    """Demonstrate various NumPy array creation functions"""
    print("\n🛠️ Array Creation Functions")
    print("=" * 35)
    
    # Zeros array
    zeros_array = np.zeros((3, 4))
    print("🔘 Zeros array (3x4):")
    print(zeros_array)
    
    # Ones array
    ones_array = np.ones((2, 3))
    print(f"\n🔴 Ones array (2x3):")
    print(ones_array)
    
    # Identity matrix
    identity_matrix = np.eye(3)
    print(f"\n🆔 Identity matrix (3x3):")
    print(identity_matrix)
    
    # Array with range
    range_array = np.arange(0, 10, 2)
    print(f"\n📊 Range array (0 to 10, step 2): {range_array}")
    
    # Linearly spaced array
    linspace_array = np.linspace(0, 1, 5)
    print(f"📏 Linearly spaced array (0 to 1, 5 points): {linspace_array}")
    
    # Random array
    np.random.seed(42)  # For reproducible results
    random_array = np.random.random((2, 3))
    print(f"\n🎲 Random array (2x3):")
    print(random_array)

def demonstrate_custom_dimensions():
    """Demonstrate creating arrays with custom dimensions"""
    print("\n🎯 Custom Dimensional Arrays")
    print("=" * 35)
    
    # Create high-dimensional array
    high_dim_array = np.array([1, 2, 3, 4], ndmin=5)
    print(f"🚀 5-dimensional array: {high_dim_array}")
    print(f"   Shape: {high_dim_array.shape}")
    print(f"   Dimensions: {high_dim_array.ndim}")
    
    # Reshape existing array
    original = np.arange(12)
    reshaped = original.reshape(3, 4)
    print(f"\n🔄 Original array: {original}")
    print(f"   Reshaped to 3x4:")
    print(reshaped)

def demonstrate_data_types():
    """Demonstrate different data types in arrays"""
    print("\n📝 Array Data Types")
    print("=" * 25)
    
    # Integer array
    int_array = np.array([1, 2, 3, 4], dtype=np.int32)
    print(f"🔢 Integer array: {int_array}")
    print(f"   Data type: {int_array.dtype}")
    
    # Float array
    float_array = np.array([1.1, 2.2, 3.3, 4.4], dtype=np.float64)
    print(f"\n🔣 Float array: {float_array}")
    print(f"   Data type: {float_array.dtype}")
    
    # Boolean array
    bool_array = np.array([True, False, True, False])
    print(f"\n✅ Boolean array: {bool_array}")
    print(f"   Data type: {bool_array.dtype}")
    
    # String array
    string_array = np.array(['apple', 'banana', 'cherry'])
    print(f"\n📝 String array: {string_array}")
    print(f"   Data type: {string_array.dtype}")

def demonstrate_array_properties():
    """Demonstrate various array properties"""
    print("\n🔍 Array Properties Analysis")
    print("=" * 35)
    
    sample_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    
    print(f"📊 Sample array:")
    print(sample_array)
    print(f"\n📐 Properties:")
    print(f"   Shape: {sample_array.shape}")
    print(f"   Size: {sample_array.size}")
    print(f"   Dimensions: {sample_array.ndim}")
    print(f"   Data type: {sample_array.dtype}")
    print(f"   Item size: {sample_array.itemsize} bytes")
    print(f"   Total size: {sample_array.nbytes} bytes")

def main():
    """Main function to demonstrate all array creation operations"""
    try:
        print("🎯 NumPy Array Creation Operations Guide")
        print("=" * 50)
        
        demonstrate_basic_array_creation()
        demonstrate_dimensional_arrays()
        demonstrate_array_creation_functions()
        demonstrate_custom_dimensions()
        demonstrate_data_types()
        demonstrate_array_properties()
        
        print("\n✨ Array Creation Operations Complete!")
        print("\n📋 Key Learning Points:")
        print("• Arrays can be created from lists, tuples, and other sequences")
        print("• NumPy supports 0-D (scalar) to N-dimensional arrays")
        print("• Multiple creation functions: zeros, ones, arange, linspace, etc.")
        print("• Data types can be specified during array creation")
        print("• Array properties provide essential information about structure")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
