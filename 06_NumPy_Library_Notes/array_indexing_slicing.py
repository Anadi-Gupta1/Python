"""
NumPy Array Indexing and Slicing - Complete Mastery Guide
=========================================================

Comprehensive guide to NumPy array indexing and slicing operations including
basic indexing, advanced slicing, boolean indexing, fancy indexing, and
performance optimization techniques for efficient array manipulation.

Author: Python Learning Notes
Date: September 2025
Topic: Array Indexing, Slicing, Boolean Indexing, Fancy Indexing
"""

import numpy as np
import time
import warnings
from typing import List, Tuple, Union, Optional, Any

# =============================================================================
# INDEXING AND SLICING CONCEPTS
# =============================================================================

def explain_indexing_concepts():
    """
    Educational explanation of NumPy indexing and slicing concepts
    """
    print("🎯 NUMPY INDEXING AND SLICING CONCEPTS")
    print("=" * 40)
    
    print("\n📚 Why Master Array Indexing?")
    print("Array indexing and slicing are crucial for:")
    print("   • Data extraction and selection")
    print("   • Efficient array manipulation")
    print("   • Conditional data filtering")
    print("   • Memory-efficient operations")
    print("   • Complex data analysis workflows")
    print("   • Scientific computing algorithms")
    
    print("\n🔄 Indexing Methods Overview:")
    methods = [
        ("Basic Indexing", "[i, j, k]", "Single elements", "arr[1, 2]"),
        ("Slicing", "[start:stop:step]", "Array segments", "arr[1:5:2]"),
        ("Boolean Indexing", "[condition]", "Conditional selection", "arr[arr > 5]"),
        ("Fancy Indexing", "[array_of_indices]", "Multiple elements", "arr[[1, 3, 5]]"),
        ("Mixed Indexing", "Combine methods", "Complex selection", "arr[1:3, [0, 2]]")
    ]
    
    print("   ┌──────────────────┬─────────────────┬─────────────────┬─────────────────┐")
    print("   │ Method           │ Syntax          │ Purpose         │ Example         │")
    print("   ├──────────────────┼─────────────────┼─────────────────┼─────────────────┤")
    for method, syntax, purpose, example in methods:
        print(f"   │ {method:<16} │ {syntax:<15} │ {purpose:<15} │ {example:<15} │")
    print("   └──────────────────┴─────────────────┴─────────────────┴─────────────────┘")
    
    print("\n⚡ Performance Considerations:")
    print("   • Views vs Copies: Understanding memory implications")
    print("   • Contiguous memory access for cache efficiency")
    print("   • Boolean indexing creates copies")
    print("   • Fancy indexing performance characteristics")
    print("   • Broadcasting in advanced indexing")

# =============================================================================
# BASIC INDEXING AND SLICING
# =============================================================================

class IndexingSlicingMaster:
    """
    Comprehensive utility for demonstrating indexing and slicing operations
    """
    
    def __init__(self):
        """Initialize with sample arrays for demonstrations"""
        # 1D sample array
        self.arr_1d = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
        
        # 2D sample array
        self.arr_2d = np.array([
            [1,  2,  3,  4,  5],
            [6,  7,  8,  9,  10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]
        ])
        
        # 3D sample array
        self.arr_3d = np.arange(24).reshape(2, 3, 4)
        
        # String array for mixed type demonstrations
        self.str_arr = np.array(['apple', 'banana', 'cherry', 'date', 'elderberry'])
        
        print("🔧 Sample arrays initialized for demonstrations")
    
    def demonstrate_basic_indexing(self):
        """
        Demonstrate basic single-element indexing
        """
        print("\n📍 BASIC INDEXING - SINGLE ELEMENTS")
        print("=" * 35)
        
        # 1D array indexing
        print("\n1️⃣  1D Array Indexing:")
        print(f"   Array: {self.arr_1d}")
        print(f"   Length: {len(self.arr_1d)}")
        
        indexing_examples = [
            ("First element", 0),
            ("Second element", 1),
            ("Last element", -1),
            ("Second to last", -2),
            ("Middle element", 4)
        ]
        
        for description, index in indexing_examples:
            try:
                value = self.arr_1d[index]
                print(f"   {description} [{index}]: {value}")
            except IndexError as e:
                print(f"   {description} [{index}]: ❌ {e}")
        
        # 2D array indexing
        print(f"\n2️⃣  2D Array Indexing:")
        print(f"   Array shape: {self.arr_2d.shape}")
        print(f"   Array:\n{self.arr_2d}")
        
        indexing_2d_examples = [
            ("Top-left element", (0, 0)),
            ("Top-right element", (0, -1)),
            ("Bottom-left element", (-1, 0)),
            ("Bottom-right element", (-1, -1)),
            ("Center element", (1, 2)),
            ("Element at [2, 3]", (2, 3))
        ]
        
        for description, indices in indexing_2d_examples:
            try:
                value = self.arr_2d[indices]
                print(f"   {description} {indices}: {value}")
            except IndexError as e:
                print(f"   {description} {indices}: ❌ {e}")
        
        # 3D array indexing
        print(f"\n3️⃣  3D Array Indexing:")
        print(f"   Array shape: {self.arr_3d.shape}")
        print(f"   Array:\n{self.arr_3d}")
        
        indexing_3d_examples = [
            ("First element of first matrix", (0, 0, 0)),
            ("Last element of last matrix", (-1, -1, -1)),
            ("Element at [1, 1, 2]", (1, 1, 2)),
        ]
        
        for description, indices in indexing_3d_examples:
            try:
                value = self.arr_3d[indices]
                print(f"   {description} {indices}: {value}")
            except IndexError as e:
                print(f"   {description} {indices}: ❌ {e}")
        
        # Alternative indexing syntax
        print(f"\n4️⃣  Alternative Indexing Syntax:")
        print(f"   arr[0, 1] is equivalent to arr[0][1]")
        
        element_method1 = self.arr_2d[1, 2]
        element_method2 = self.arr_2d[1][2]
        
        print(f"   Method 1 - arr[1, 2]: {element_method1}")
        print(f"   Method 2 - arr[1][2]: {element_method2}")
        print(f"   Are equal: {element_method1 == element_method2}")
        print(f"   💡 Prefer arr[1, 2] for better performance")
    
    def demonstrate_slicing_operations(self):
        """
        Demonstrate array slicing operations
        """
        print("\n🔪 ARRAY SLICING OPERATIONS")
        print("=" * 28)
        
        # 1D array slicing
        print("\n1️⃣  1D Array Slicing:")
        print(f"   Array: {self.arr_1d}")
        
        slicing_examples = [
            ("First 5 elements", slice(0, 5)),
            ("Last 3 elements", slice(-3, None)),
            ("Elements 2 to 6", slice(2, 7)),
            ("Every 2nd element", slice(None, None, 2)),
            ("Every 2nd from index 1", slice(1, None, 2)),
            ("Reverse array", slice(None, None, -1)),
            ("Middle section reverse", slice(7, 2, -1))
        ]
        
        for description, slice_obj in slicing_examples:
            try:
                result = self.arr_1d[slice_obj]
                # Convert slice to readable format
                start, stop, step = slice_obj.indices(len(self.arr_1d))
                slice_notation = f"[{start if start != 0 else ''}:{stop if stop != len(self.arr_1d) else ''}{':', step if step != 1 else ''}]".replace('::', ':')
                print(f"   {description} {slice_notation}: {result}")
            except Exception as e:
                print(f"   {description}: ❌ {e}")
        
        # 2D array slicing
        print(f"\n2️⃣  2D Array Slicing:")
        print(f"   Array:\n{self.arr_2d}")
        
        print(f"\n   Row Operations:")
        print(f"   First row [0, :]: {self.arr_2d[0, :]}")
        print(f"   Last row [-1, :]: {self.arr_2d[-1, :]}")
        print(f"   First two rows [0:2, :]: \n{self.arr_2d[0:2, :]}")
        
        print(f"\n   Column Operations:")
        print(f"   First column [:, 0]: {self.arr_2d[:, 0]}")
        print(f"   Last column [:, -1]: {self.arr_2d[:, -1]}")
        print(f"   Columns 1-3 [:, 1:4]: \n{self.arr_2d[:, 1:4]}")
        
        print(f"\n   Subarray Operations:")
        print(f"   Top-left 2x2 [0:2, 0:2]: \n{self.arr_2d[0:2, 0:2]}")
        print(f"   Bottom-right 2x2 [-2:, -2:]: \n{self.arr_2d[-2:, -2:]}")
        print(f"   Every other element [::2, ::2]: \n{self.arr_2d[::2, ::2]}")
        
        # Views vs copies demonstration
        print(f"\n3️⃣  Views vs Copies:")
        
        # Create a view
        view = self.arr_2d[1:3, 1:4]
        print(f"   Original array:\n{self.arr_2d}")
        print(f"   View [1:3, 1:4]:\n{view}")
        
        # Modify the view
        original_value = view[0, 0]
        view[0, 0] = 999
        
        print(f"   After modifying view[0, 0] from {original_value} to 999:")
        print(f"   Modified view:\n{view}")
        print(f"   Original array (note the change):\n{self.arr_2d}")
        
        # Restore original value
        view[0, 0] = original_value
        
        print(f"   💡 Slicing creates views, not copies!")
        print(f"   💡 Changes to views affect the original array!")
    
    def demonstrate_boolean_indexing(self):
        """
        Demonstrate boolean indexing for conditional selection
        """
        print("\n🔍 BOOLEAN INDEXING - CONDITIONAL SELECTION")
        print("=" * 45)
        
        # Simple boolean conditions
        print("\n1️⃣  Simple Boolean Conditions:")
        print(f"   Array: {self.arr_1d}")
        
        conditions = [
            ("Greater than 50", self.arr_1d > 50),
            ("Less than or equal to 30", self.arr_1d <= 30),
            ("Equal to 40", self.arr_1d == 40),
            ("Not equal to 60", self.arr_1d != 60)
        ]
        
        for description, condition in conditions:
            result = self.arr_1d[condition]
            print(f"   {description}:")
            print(f"     Condition: {condition}")
            print(f"     Selected elements: {result}")
        
        # Complex boolean conditions
        print("\n2️⃣  Complex Boolean Conditions:")
        
        # Logical AND
        and_condition = (self.arr_1d > 30) & (self.arr_1d < 80)
        and_result = self.arr_1d[and_condition]
        print(f"   Between 30 and 80 (AND):")
        print(f"     Condition: {and_condition}")
        print(f"     Selected: {and_result}")
        
        # Logical OR
        or_condition = (self.arr_1d < 30) | (self.arr_1d > 80)
        or_result = self.arr_1d[or_condition]
        print(f"   Less than 30 OR greater than 80:")
        print(f"     Condition: {or_condition}")
        print(f"     Selected: {or_result}")
        
        # Logical NOT
        not_condition = ~(self.arr_1d == 50)
        not_result = self.arr_1d[not_condition]
        print(f"   Not equal to 50:")
        print(f"     Selected: {not_result}")
        
        # 2D boolean indexing
        print("\n3️⃣  2D Boolean Indexing:")
        print(f"   Array:\n{self.arr_2d}")
        
        # Condition on 2D array
        condition_2d = self.arr_2d > 10
        result_2d = self.arr_2d[condition_2d]
        
        print(f"   Elements greater than 10:")
        print(f"     Condition mask:\n{condition_2d}")
        print(f"     Selected elements (flattened): {result_2d}")
        
        # Row-wise conditions
        row_sums = np.sum(self.arr_2d, axis=1)
        high_sum_rows = row_sums > 40
        selected_rows = self.arr_2d[high_sum_rows]
        
        print(f"   Rows with sum > 40:")
        print(f"     Row sums: {row_sums}")
        print(f"     High sum rows condition: {high_sum_rows}")
        print(f"     Selected rows:\n{selected_rows}")
        
        # Boolean indexing with assignment
        print("\n4️⃣  Boolean Indexing with Assignment:")
        
        # Create a copy to modify
        temp_arr = self.arr_1d.copy()
        print(f"   Original: {temp_arr}")
        
        # Set all values > 60 to 999
        temp_arr[temp_arr > 60] = 999
        print(f"   After setting values > 60 to 999: {temp_arr}")
        
        # Conditional replacement
        temp_arr_2d = self.arr_2d.copy()
        temp_arr_2d[temp_arr_2d % 2 == 0] = -1  # Replace even numbers with -1
        print(f"   2D array with even numbers replaced by -1:\n{temp_arr_2d}")
    
    def demonstrate_fancy_indexing(self):
        """
        Demonstrate fancy indexing using arrays of indices
        """
        print("\n✨ FANCY INDEXING - ARRAY-BASED SELECTION")
        print("=" * 42)
        
        # 1D fancy indexing
        print("\n1️⃣  1D Fancy Indexing:")
        print(f"   Array: {self.arr_1d}")
        
        # Integer array indexing
        indices = [1, 3, 5, 7]
        fancy_result = self.arr_1d[indices]
        print(f"   Indices {indices}: {fancy_result}")
        
        # Negative indices
        neg_indices = [-1, -3, -5]
        neg_result = self.arr_1d[neg_indices]
        print(f"   Negative indices {neg_indices}: {neg_result}")
        
        # Repeated indices
        repeat_indices = [0, 2, 2, 4, 0]
        repeat_result = self.arr_1d[repeat_indices]
        print(f"   Repeated indices {repeat_indices}: {repeat_result}")
        
        # Random selection
        np.random.seed(42)
        random_indices = np.random.choice(len(self.arr_1d), 5, replace=False)
        random_result = self.arr_1d[random_indices]
        print(f"   Random indices {random_indices}: {random_result}")
        
        # 2D fancy indexing
        print("\n2️⃣  2D Fancy Indexing:")
        print(f"   Array:\n{self.arr_2d}")
        
        # Row selection
        row_indices = [0, 2, 3]
        selected_rows = self.arr_2d[row_indices]
        print(f"   Rows {row_indices}:\n{selected_rows}")
        
        # Column selection (requires transpose or advanced indexing)
        col_indices = [1, 3, 4]
        selected_cols = self.arr_2d[:, col_indices]
        print(f"   Columns {col_indices}:\n{selected_cols}")
        
        # Element selection with row and column indices
        row_idx = [0, 1, 2]
        col_idx = [1, 2, 3]
        elements = self.arr_2d[row_idx, col_idx]
        print(f"   Elements at positions {list(zip(row_idx, col_idx))}: {elements}")
        
        # 3D fancy indexing
        print("\n3️⃣  3D Fancy Indexing:")
        print(f"   3D Array shape: {self.arr_3d.shape}")
        print(f"   3D Array:\n{self.arr_3d}")
        
        # Select specific matrices
        matrix_indices = [0, 1, 0]
        selected_matrices = self.arr_3d[matrix_indices]
        print(f"   Selected matrices {matrix_indices}:\n{selected_matrices}")
        
        # Mixed indexing combinations
        print("\n4️⃣  Mixed Indexing:")
        
        # Combine slicing and fancy indexing
        mixed_result = self.arr_2d[1:3, [0, 2, 4]]
        print(f"   Rows 1-2, columns [0, 2, 4]:\n{mixed_result}")
        
        # Boolean + fancy indexing
        mask = self.arr_1d > 50
        high_values = self.arr_1d[mask]
        if len(high_values) >= 3:
            selected_high = high_values[[0, 2]]  # First and third high values
            print(f"   First and third values > 50: {selected_high}")
        
        # Fancy indexing with assignment
        print("\n5️⃣  Fancy Indexing with Assignment:")
        
        temp_arr = self.arr_1d.copy()
        print(f"   Original: {temp_arr}")
        
        # Assign to specific indices
        assign_indices = [1, 3, 5]
        temp_arr[assign_indices] = [999, 888, 777]
        print(f"   After assigning to indices {assign_indices}: {temp_arr}")
        
        # Increment specific elements
        temp_arr[[0, 2, 4]] += 100
        print(f"   After incrementing indices [0, 2, 4] by 100: {temp_arr}")
    
    def demonstrate_advanced_indexing(self):
        """
        Demonstrate advanced indexing techniques and edge cases
        """
        print("\n🚀 ADVANCED INDEXING TECHNIQUES")
        print("=" * 31)
        
        # Ellipsis indexing
        print("\n1️⃣  Ellipsis (...) Indexing:")
        print(f"   3D Array shape: {self.arr_3d.shape}")
        
        # These are equivalent for 3D arrays
        methods = [
            ("Full specification", self.arr_3d[:, :, 0]),
            ("Ellipsis at end", self.arr_3d[..., 0]),
            ("Ellipsis at start", self.arr_3d[0, ...]),
            ("Middle ellipsis", self.arr_3d[:, ..., 0])
        ]
        
        for description, result in methods:
            print(f"   {description}: shape {result.shape}")
        
        # None/np.newaxis indexing
        print("\n2️⃣  Adding New Axes:")
        
        arr_1d_sample = np.array([1, 2, 3])
        print(f"   Original 1D array: {arr_1d_sample} (shape: {arr_1d_sample.shape})")
        
        # Add dimension at different positions
        new_axis_examples = [
            ("Add axis at start", arr_1d_sample[np.newaxis, :]),
            ("Add axis at end", arr_1d_sample[:, np.newaxis]),
            ("Add axis with None", arr_1d_sample[None, :]),
            ("Multiple new axes", arr_1d_sample[np.newaxis, :, np.newaxis])
        ]
        
        for description, result in new_axis_examples:
            print(f"   {description}: shape {result.shape}")
        
        # Advanced boolean indexing
        print("\n3️⃣  Advanced Boolean Indexing:")
        
        # Multiple conditions with different arrays
        arr_a = np.array([1, 2, 3, 4, 5])
        arr_b = np.array([5, 4, 3, 2, 1])
        
        print(f"   Array A: {arr_a}")
        print(f"   Array B: {arr_b}")
        
        # Cross-array conditions
        condition = arr_a > arr_b
        result_a = arr_a[condition]
        result_b = arr_b[condition]
        
        print(f"   Where A > B: A={result_a}, B={result_b}")
        
        # np.where for conditional selection
        where_result = np.where(arr_a > 3, arr_a, arr_b)
        print(f"   np.where(A > 3, A, B): {where_result}")
        
        # Advanced fancy indexing
        print("\n4️⃣  Advanced Fancy Indexing:")
        
        # Index array broadcasting
        row_idx = np.array([[0, 1], [2, 3]])
        col_idx = np.array([[1, 2], [3, 4]])
        
        if self.arr_2d.shape[0] > 3 and self.arr_2d.shape[1] > 4:
            broadcast_result = self.arr_2d[row_idx, col_idx]
            print(f"   Broadcasting index arrays:")
            print(f"   Row indices:\n{row_idx}")
            print(f"   Col indices:\n{col_idx}")
            print(f"   Result:\n{broadcast_result}")
        
        # Performance comparison
        print("\n5️⃣  Performance Comparison:")
        
        large_arr = np.random.randint(0, 100, 100000)
        
        # Boolean indexing performance
        start_time = time.time()
        bool_result = large_arr[large_arr > 50]
        bool_time = (time.time() - start_time) * 1000
        
        # Fancy indexing performance
        indices = np.where(large_arr > 50)[0]
        start_time = time.time()
        fancy_result = large_arr[indices]
        fancy_time = (time.time() - start_time) * 1000
        
        print(f"   Boolean indexing: {bool_time:.3f} ms ({len(bool_result)} elements)")
        print(f"   Fancy indexing: {fancy_time:.3f} ms ({len(fancy_result)} elements)")
        print(f"   Results identical: {np.array_equal(bool_result, fancy_result)}")

# =============================================================================
# PRACTICAL APPLICATIONS AND EXAMPLES
# =============================================================================

def practical_indexing_examples():
    """
    Demonstrate practical applications of indexing and slicing
    """
    print("\n🛠️  PRACTICAL INDEXING APPLICATIONS")
    print("=" * 35)
    
    # Example 1: Data filtering and analysis
    print("\n📊 Example 1: Student Grade Analysis")
    print("-" * 35)
    
    # Simulated student data
    np.random.seed(42)
    students = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry"]
    subjects = ["Math", "Physics", "Chemistry", "Biology"]
    grades = np.random.randint(50, 100, (len(students), len(subjects)))
    
    print("Student Grades Matrix:")
    print(f"Students: {students}")
    print(f"Subjects: {subjects}")
    print(grades)
    
    # Find students with high performance
    avg_grades = np.mean(grades, axis=1)
    high_performers = grades[avg_grades > 75]
    high_performer_names = [students[i] for i, avg in enumerate(avg_grades) if avg > 75]
    
    print(f"\nHigh Performers (avg > 75): {high_performer_names}")
    print(f"Their grades:\n{high_performers}")
    
    # Find subjects where all students scored > 60
    all_pass_subjects = np.all(grades > 60, axis=0)
    passing_subjects = [subjects[i] for i, passed in enumerate(all_pass_subjects) if passed]
    
    print(f"Subjects with all students > 60: {passing_subjects}")
    
    # Find students who failed (< 60) in any subject
    failed_any = np.any(grades < 60, axis=1)
    failed_students = [students[i] for i, failed in enumerate(failed_any) if failed]
    
    print(f"Students who failed any subject: {failed_students}")
    
    # Example 2: Image processing simulation
    print("\n🖼️  Example 2: Image Processing")
    print("-" * 30)
    
    # Simulate a small grayscale image
    image = np.random.randint(0, 256, (8, 8))
    print(f"Original 8x8 'image':\n{image}")
    
    # Extract regions of interest
    top_left = image[:4, :4]
    center = image[2:6, 2:6]
    
    print(f"Top-left quadrant:\n{top_left}")
    print(f"Center 4x4 region:\n{center}")
    
    # Thresholding (convert to binary)
    threshold = 128
    binary = image > threshold
    
    print(f"Binary image (threshold={threshold}):\n{binary.astype(int)}")
    
    # Find bright pixels
    bright_pixels = np.where(image > 200)
    print(f"Bright pixel coordinates (value > 200): {list(zip(bright_pixels[0], bright_pixels[1]))}")
    
    # Example 3: Time series data analysis
    print("\n📈 Example 3: Time Series Analysis")
    print("-" * 32)
    
    # Simulate daily temperature data for a year
    days = np.arange(365)
    temperature = 20 + 10 * np.sin(2 * np.pi * days / 365) + np.random.normal(0, 2, 365)
    
    print(f"Temperature data shape: {temperature.shape}")
    print(f"Sample temperatures (first 10 days): {temperature[:10]}")
    
    # Find hot days
    hot_threshold = 25
    hot_days = days[temperature > hot_threshold]
    hot_temps = temperature[temperature > hot_threshold]
    
    print(f"Hot days (> {hot_threshold}°C): {len(hot_days)} days")
    print(f"Hottest day: Day {days[np.argmax(temperature)]} ({np.max(temperature):.1f}°C)")
    
    # Monthly averages (assuming 30 days per month)
    monthly_temps = []
    for month in range(12):
        start_day = month * 30
        end_day = min((month + 1) * 30, 365)
        monthly_avg = np.mean(temperature[start_day:end_day])
        monthly_temps.append(monthly_avg)
    
    monthly_temps = np.array(monthly_temps)
    print(f"Monthly averages: {monthly_temps}")
    print(f"Hottest month: Month {np.argmax(monthly_temps) + 1} ({np.max(monthly_temps):.1f}°C)")

def interactive_indexing_playground():
    """
    Interactive playground for experimenting with indexing
    """
    print("\n🎮 INTERACTIVE INDEXING PLAYGROUND")
    print("=" * 33)
    
    # Create sample data
    master = IndexingSlicingMaster()
    
    while True:
        try:
            print("\n🎯 Choose indexing operation:")
            print("   1. Basic indexing practice")
            print("   2. Slicing operations")
            print("   3. Boolean indexing experiments")
            print("   4. Fancy indexing trials")
            print("   5. Mixed indexing challenges")
            print("   6. Create custom array for practice")
            print("   7. Performance comparison")
            print("   8. Exit playground")
            
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == "1":
                master.demonstrate_basic_indexing()
            elif choice == "2":
                master.demonstrate_slicing_operations()
            elif choice == "3":
                master.demonstrate_boolean_indexing()
            elif choice == "4":
                master.demonstrate_fancy_indexing()
            elif choice == "5":
                master.demonstrate_advanced_indexing()
            elif choice == "6":
                create_custom_indexing_practice()
            elif choice == "7":
                indexing_performance_comparison()
            elif choice == "8":
                print("\n👋 Thanks for exploring NumPy indexing!")
                break
            else:
                print("❌ Invalid choice. Please choose 1-8.")
                
        except ValueError:
            print("❌ Please enter valid numbers!")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def create_custom_indexing_practice():
    """
    Create custom arrays for indexing practice
    """
    print("\n🛠️  Custom Array Creator for Indexing Practice")
    print("=" * 45)
    
    try:
        # Get array specifications
        dimensions = input("Number of dimensions (1, 2, or 3): ").strip()
        
        if dimensions == "1":
            size = int(input("Array size: "))
            array = np.random.randint(1, 100, size)
            
        elif dimensions == "2":
            rows = int(input("Number of rows: "))
            cols = int(input("Number of columns: "))
            array = np.random.randint(1, 100, (rows, cols))
            
        elif dimensions == "3":
            depth = int(input("Depth: "))
            rows = int(input("Number of rows: "))
            cols = int(input("Number of columns: "))
            array = np.random.randint(1, 100, (depth, rows, cols))
            
        else:
            print("❌ Invalid dimensions. Using default 2D array.")
            array = np.random.randint(1, 100, (4, 5))
        
        print(f"\n✅ Created array:")
        print(f"Shape: {array.shape}")
        print(f"Array:")
        print(array)
        
        # Interactive indexing practice
        print(f"\n🎯 Try some indexing operations:")
        print(f"   Examples to try:")
        
        if array.ndim == 1:
            print(f"   • array[0] - first element")
            print(f"   • array[-1] - last element")
            print(f"   • array[::2] - every second element")
            print(f"   • array[array > 50] - elements > 50")
        elif array.ndim == 2:
            print(f"   • array[0, 0] - top-left element")
            print(f"   • array[:, 0] - first column")
            print(f"   • array[0, :] - first row")
            print(f"   • array[array > 50] - elements > 50")
            print(f"   • array[[0, 2], :] - rows 0 and 2")
        
        # Let user try operations
        while True:
            try:
                expression = input("\nEnter indexing expression (or 'quit'): ").strip()
                
                if expression.lower() == 'quit':
                    break
                
                # Safely evaluate the expression
                if expression.startswith('array'):
                    try:
                        result = eval(expression, {"array": array, "np": np})
                        print(f"Result: {result}")
                        if hasattr(result, 'shape'):
                            print(f"Shape: {result.shape}")
                    except Exception as e:
                        print(f"❌ Error: {e}")
                else:
                    print("❌ Expression must start with 'array'")
                    
            except KeyboardInterrupt:
                break
        
    except ValueError:
        print("❌ Please enter valid numbers!")
    except Exception as e:
        print(f"❌ Error creating array: {e}")

def indexing_performance_comparison():
    """
    Compare performance of different indexing methods
    """
    print("\n⏱️  INDEXING PERFORMANCE COMPARISON")
    print("=" * 35)
    
    # Create large test array
    size = 1000000
    large_array = np.random.randint(0, 1000, size)
    
    print(f"Testing with array of {size:,} elements")
    
    # Test different selection methods
    methods = [
        ("Boolean indexing (> 500)", lambda: large_array[large_array > 500]),
        ("np.where + fancy indexing", lambda: large_array[np.where(large_array > 500)[0]]),
        ("List comprehension", lambda: np.array([x for x in large_array if x > 500])),
        ("Fancy indexing (first 1000)", lambda: large_array[np.arange(1000)]),
        ("Slicing (first 1000)", lambda: large_array[:1000])
    ]
    
    print(f"\n📊 Performance Results:")
    print("   ┌─────────────────────────────┬─────────────┬─────────────┐")
    print("   │ Method                      │ Time (ms)   │ Elements    │")
    print("   ├─────────────────────────────┼─────────────┼─────────────┤")
    
    for method_name, method_func in methods:
        # Warm up
        _ = method_func()
        
        # Measure performance
        start_time = time.time()
        result = method_func()
        elapsed = (time.time() - start_time) * 1000
        
        result_size = len(result) if hasattr(result, '__len__') else 1
        
        print(f"   │ {method_name:<27} │ {elapsed:>9.2f} │ {result_size:>9,} │")
    
    print("   └─────────────────────────────┴─────────────┴─────────────┘")
    
    print(f"\n💡 Performance Tips:")
    print("   • Boolean indexing is generally fastest for conditions")
    print("   • Slicing creates views (no copying) when possible")
    print("   • Fancy indexing always creates copies")
    print("   • Avoid Python list comprehensions for large arrays")

# =============================================================================
# MAIN EXECUTION AND DEMONSTRATION
# =============================================================================

def demonstrate_all_indexing():
    """
    Comprehensive demonstration of all indexing and slicing techniques
    """
    print("\n" + "="*60)
    print("COMPREHENSIVE INDEXING AND SLICING DEMONSTRATION")
    print("="*60)
    
    master = IndexingSlicingMaster()
    
    # Demonstrate all techniques
    techniques = [
        ("Basic Indexing", master.demonstrate_basic_indexing),
        ("Slicing Operations", master.demonstrate_slicing_operations),
        ("Boolean Indexing", master.demonstrate_boolean_indexing),
        ("Fancy Indexing", master.demonstrate_fancy_indexing),
        ("Advanced Indexing", master.demonstrate_advanced_indexing)
    ]
    
    for technique_name, technique_func in techniques:
        print(f"\n{'='*50}")
        print(f"DEMONSTRATING: {technique_name.upper()}")
        print('='*50)
        
        try:
            technique_func()
            print("✅ Technique demonstrated successfully")
        except Exception as e:
            print(f"❌ Error in {technique_name}: {e}")

if __name__ == "__main__":
    """
    Main execution demonstrating NumPy indexing and slicing concepts
    """
    print(__doc__)
    
    # Educational content
    explain_indexing_concepts()
    
    # Comprehensive demonstration
    demonstrate_all_indexing()
    
    # Practical examples
    practical_indexing_examples()
    
    # Interactive playground
    interactive_indexing_playground()
    
    print("\n" + "=" * 50)
    print("🎓 INDEXING AND SLICING MASTERY SUMMARY")
    print("=" * 50)
    print("✅ All indexing and slicing techniques mastered")
    print("✅ Boolean and fancy indexing expertise")
    print("✅ Views vs copies understanding")
    print("✅ Performance optimization knowledge")
    print("✅ Practical application skills")
    print("✅ Advanced indexing techniques")
    
    print("\n💡 Key Concepts Mastered:")
    print("• Complete indexing methodology and syntax")
    print("• Memory-efficient operations with views")
    print("• Conditional data selection and filtering")
    print("• Multi-dimensional array manipulation")
    print("• Performance characteristics of different methods")
    print("• Real-world application patterns")
    
    print("\n🎯 Next Steps in NumPy:")
    print("• Array broadcasting and vectorization")
    print("• Mathematical operations and functions")
    print("• Array reshaping and manipulation")
    print("• Linear algebra operations")
    print("• Advanced array processing techniques")
    print("• Integration with scientific computing workflows")
