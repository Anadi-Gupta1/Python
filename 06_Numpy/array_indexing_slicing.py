"""
NumPy Array Indexing and Slicing Operations
==========================================

This module demonstrates comprehensive array indexing and slicing techniques
in NumPy, covering 1D, 2D, and multi-dimensional arrays.

Author: Anadi Gupta
Date: September 2025
Purpose: Complete guide to NumPy array indexing, slicing, and advanced selection
"""

import numpy as np

def demonstrate_1d_indexing():
    """Demonstrate indexing operations on 1-dimensional arrays"""
    print("🎯 1-D Array Indexing")
    print("=" * 30)
    
    arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
    print(f"📊 Original array: {arr}")
    print(f"   Array length: {len(arr)}")
    
    # Basic indexing
    print(f"\n🔍 Basic Indexing:")
    print(f"   First element [0]: {arr[0]}")
    print(f"   Second element [1]: {arr[1]}")
    print(f"   Last element [-1]: {arr[-1]}")
    print(f"   Second last [-2]: {arr[-2]}")
    
    # Multiple elements
    print(f"\n📋 Multiple Element Access:")
    print(f"   Elements at indices [0, 2, 4]: {arr[[0, 2, 4]]}")
    print(f"   Elements at indices [1, 3, 5]: {arr[[1, 3, 5]]}")

def demonstrate_1d_slicing():
    """Demonstrate slicing operations on 1-dimensional arrays"""
    print("\n✂️ 1-D Array Slicing")
    print("=" * 30)
    
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"📊 Original array: {arr}")
    
    # Basic slicing
    print(f"\n🔪 Basic Slicing:")
    print(f"   First 5 elements [0:5]: {arr[0:5]}")
    print(f"   Elements 3 to 7 [3:8]: {arr[3:8]}")
    print(f"   Last 3 elements [-3:]: {arr[-3:]}")
    print(f"   All except last 2 [:-2]: {arr[:-2]}")
    
    # Step slicing
    print(f"\n👣 Step Slicing:")
    print(f"   Every 2nd element [::2]: {arr[::2]}")
    print(f"   Every 3rd element [::3]: {arr[::3]}")
    print(f"   Reverse array [::-1]: {arr[::-1]}")
    print(f"   Every 2nd in reverse [::-2]: {arr[::-2]}")

def demonstrate_2d_indexing():
    """Demonstrate indexing operations on 2-dimensional arrays"""
    print("\n🎯 2-D Array Indexing")
    print("=" * 30)
    
    arr = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12]])
    
    print(f"📊 Original 2D array:")
    print(arr)
    print(f"   Shape: {arr.shape}")
    
    # Element access
    print(f"\n🔍 Element Access:")
    print(f"   Element at [0, 0]: {arr[0, 0]}")
    print(f"   Element at [1, 2]: {arr[1, 2]}")
    print(f"   Element at [2, 3]: {arr[2, 3]}")
    print(f"   Element at [-1, -1]: {arr[-1, -1]}")
    
    # Row and column access
    print(f"\n📏 Row and Column Access:")
    print(f"   First row [0, :]: {arr[0, :]}")
    print(f"   Second row [1]: {arr[1]}")  # Shorthand
    print(f"   Last row [-1, :]: {arr[-1, :]}")
    print(f"   First column [:, 0]: {arr[:, 0]}")
    print(f"   Last column [:, -1]: {arr[:, -1]}")

def demonstrate_2d_slicing():
    """Demonstrate slicing operations on 2-dimensional arrays"""
    print("\n✂️ 2-D Array Slicing")
    print("=" * 30)
    
    arr = np.array([[1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10],
                    [11, 12, 13, 14, 15],
                    [16, 17, 18, 19, 20]])
    
    print(f"📊 Original 4x5 array:")
    print(arr)
    
    # Row slicing
    print(f"\n📏 Row Slicing:")
    print(f"   First 2 rows [0:2, :]:")
    print(arr[0:2, :])
    print(f"   Last 2 rows [-2:, :]:")
    print(arr[-2:, :])
    
    # Column slicing
    print(f"\n📐 Column Slicing:")
    print(f"   First 3 columns [:, 0:3]:")
    print(arr[:, 0:3])
    print(f"   Last 2 columns [:, -2:]:")
    print(arr[:, -2:])
    
    # Subarray slicing
    print(f"\n🔲 Subarray Slicing:")
    print(f"   Middle 2x3 subarray [1:3, 1:4]:")
    print(arr[1:3, 1:4])

def demonstrate_boolean_indexing():
    """Demonstrate boolean indexing for conditional selection"""
    print("\n✅ Boolean Indexing")
    print("=" * 25)
    
    arr = np.array([1, 5, 3, 8, 2, 9, 4, 7, 6])
    print(f"📊 Original array: {arr}")
    
    # Boolean conditions
    print(f"\n🔍 Boolean Conditions:")
    greater_than_5 = arr > 5
    print(f"   Condition (arr > 5): {greater_than_5}")
    print(f"   Elements > 5: {arr[greater_than_5]}")
    
    even_numbers = arr % 2 == 0
    print(f"   Even numbers: {arr[even_numbers]}")
    
    # Complex conditions
    print(f"\n🧮 Complex Conditions:")
    between_3_and_7 = (arr >= 3) & (arr <= 7)
    print(f"   Between 3 and 7: {arr[between_3_and_7]}")
    
    not_equal_5 = arr != 5
    print(f"   Not equal to 5: {arr[not_equal_5]}")

def demonstrate_fancy_indexing():
    """Demonstrate fancy indexing with integer arrays"""
    print("\n🎭 Fancy Indexing")
    print("=" * 25)
    
    arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
    print(f"📊 Original array: {arr}")
    
    # Index arrays
    indices = np.array([0, 2, 4, 6])
    print(f"\n📋 Index array: {indices}")
    print(f"   Selected elements: {arr[indices]}")
    
    # 2D fancy indexing
    arr_2d = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
    
    print(f"\n📊 2D Array for fancy indexing:")
    print(arr_2d)
    
    row_indices = np.array([0, 1, 2])
    col_indices = np.array([2, 1, 0])
    print(f"   Row indices: {row_indices}")
    print(f"   Col indices: {col_indices}")
    print(f"   Diagonal elements: {arr_2d[row_indices, col_indices]}")

def demonstrate_advanced_slicing():
    """Demonstrate advanced slicing techniques"""
    print("\n🚀 Advanced Slicing Techniques")
    print("=" * 40)
    
    # 3D array
    arr_3d = np.arange(24).reshape(2, 3, 4)
    print(f"📊 3D Array (2x3x4):")
    print(arr_3d)
    
    # 3D slicing
    print(f"\n🎯 3D Slicing Examples:")
    print(f"   First matrix [0, :, :]:")
    print(arr_3d[0, :, :])
    
    print(f"   Middle column of all matrices [:, 1, :]:")
    print(arr_3d[:, 1, :])
    
    print(f"   Corner elements [0, 0, 0] and [1, 2, 3]: {arr_3d[0, 0, 0]}, {arr_3d[1, 2, 3]}")

def demonstrate_array_modification():
    """Demonstrate modifying arrays through indexing"""
    print("\n✏️ Array Modification via Indexing")
    print("=" * 40)
    
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(f"📊 Original array: {arr}")
    
    # Single element modification
    arr[0] = 99
    print(f"   After arr[0] = 99: {arr}")
    
    # Slice modification
    arr[1:4] = [88, 77, 66]
    print(f"   After slice modification: {arr}")
    
    # Boolean indexing modification
    arr[arr > 50] = 0
    print(f"   After setting >50 to 0: {arr}")
    
    # 2D modification
    arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"\n📊 2D Array modification:")
    print(f"   Original: \n{arr_2d}")
    
    arr_2d[1, :] = [10, 11, 12]
    print(f"   After row modification: \n{arr_2d}")

def demonstrate_performance_tips():
    """Demonstrate performance considerations for indexing"""
    print("\n⚡ Performance Tips")
    print("=" * 25)
    
    import time
    
    large_array = np.random.random(1000000)
    
    # View vs Copy
    print("📊 View vs Copy Performance:")
    
    # Slicing creates a view (fast)
    start_time = time.time()
    slice_view = large_array[100:200]
    slice_time = time.time() - start_time
    
    # Fancy indexing creates a copy (slower)
    start_time = time.time()
    fancy_copy = large_array[[i for i in range(100, 200)]]
    fancy_time = time.time() - start_time
    
    print(f"   Slicing (view): {slice_time:.6f} seconds")
    print(f"   Fancy indexing (copy): {fancy_time:.6f} seconds")
    if slice_time > 0:
        print(f"   🏆 Slicing is {fancy_time/slice_time:.1f}x faster")
    else:
        print(f"   🏆 Slicing is significantly faster (near-instantaneous)")

def main():
    """Main function to demonstrate all indexing and slicing operations"""
    try:
        print("🎯 NumPy Array Indexing and Slicing Guide")
        print("=" * 50)
        
        demonstrate_1d_indexing()
        demonstrate_1d_slicing()
        demonstrate_2d_indexing()
        demonstrate_2d_slicing()
        demonstrate_boolean_indexing()
        demonstrate_fancy_indexing()
        demonstrate_advanced_slicing()
        demonstrate_array_modification()
        demonstrate_performance_tips()
        
        print("\n✨ Array Indexing and Slicing Complete!")
        print("\n📋 Key Learning Points:")
        print("• Basic indexing uses square brackets with integer indices")
        print("• Slicing uses start:stop:step syntax for ranges")
        print("• Boolean indexing enables conditional element selection")
        print("• Fancy indexing uses arrays of indices for complex selection")
        print("• Slicing creates views (fast), fancy indexing creates copies")
        print("• 2D and 3D arrays support multi-dimensional indexing")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
