"""
List Slicing - Complete Python Guide
===================================

Comprehensive guide to Python list slicing covering all syntax variations,
advanced techniques, performance optimization, and practical applications.
Master the art of extracting, modifying, and manipulating list segments.

Author: Python Learning Notes
Date: September 2025
Topic: List Slicing, Indexing, Sequence Manipulation, Advanced Techniques
"""

import time
import sys
from typing import List, Any, Union, Optional, Tuple

# =============================================================================
# FUNDAMENTALS OF LIST SLICING
# =============================================================================

def list_slicing_fundamentals():
    """
    Understanding the fundamentals of list slicing in Python
    """
    print("🔪 LIST SLICING FUNDAMENTALS")
    print("=" * 30)
    
    print("🎯 What is List Slicing?")
    print("   List slicing extracts a portion of a list using [start:stop:step]")
    print("   syntax. It creates a new list containing selected elements without")
    print("   modifying the original list (unless assigned back).")
    
    print(f"\n📝 Basic Slicing Syntax:")
    syntax_examples = [
        ("list[start:stop]", "Elements from start to stop-1", "[1,2,3,4,5][1:4] → [2,3,4]"),
        ("list[start:]", "Elements from start to end", "[1,2,3,4,5][2:] → [3,4,5]"),
        ("list[:stop]", "Elements from beginning to stop-1", "[1,2,3,4,5][:3] → [1,2,3]"),
        ("list[:]", "Complete copy of list", "[1,2,3,4,5][:] → [1,2,3,4,5]"),
        ("list[::step]", "Every step-th element", "[1,2,3,4,5][::2] → [1,3,5]"),
        ("list[start:stop:step]", "Full slicing syntax", "[1,2,3,4,5][1:4:2] → [2,4]")
    ]
    
    print("   Syntax              │ Description               │ Example")
    print("   ────────────────────┼───────────────────────────┼─────────────────────")
    
    for syntax, description, example in syntax_examples:
        print(f"   {syntax:<19} │ {description:<25} │ {example}")
    
    print(f"\n🔢 Index Rules:")
    print("   • Positive indices: 0, 1, 2, ... (left to right)")
    print("   • Negative indices: -1, -2, -3, ... (right to left)")
    print("   • start: inclusive (included in result)")
    print("   • stop: exclusive (not included in result)")
    print("   • step: increment/decrement between indices")
    
    return {'syntax_examples': syntax_examples}

def basic_slicing_operations():
    """
    Demonstrate basic list slicing operations
    """
    print("\n✂️ BASIC SLICING OPERATIONS")
    print("=" * 29)
    
    # Sample list for demonstrations
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Sample list: {numbers}")
    print(f"Indices:     {list(range(len(numbers)))}")
    print(f"Negative:    {list(range(-len(numbers), 0))}")
    
    # 1. BASIC FORWARD SLICING
    print(f"\n1️⃣ Basic Forward Slicing:")
    
    # Simple slicing examples
    slice1 = numbers[2:6]
    slice2 = numbers[1:8]
    slice3 = numbers[0:5]
    
    print(f"   numbers[2:6] = {slice1}  # Elements at indices 2, 3, 4, 5")
    print(f"   numbers[1:8] = {slice2}  # Elements at indices 1 through 7")
    print(f"   numbers[0:5] = {slice3}  # First 5 elements")
    
    # 2. OMITTING START OR STOP
    print(f"\n2️⃣ Omitting Start or Stop:")
    
    from_start = numbers[:4]    # From beginning to index 3
    to_end = numbers[6:]        # From index 6 to end
    entire_copy = numbers[:]    # Complete copy
    
    print(f"   numbers[:4]  = {from_start}   # From start to index 3")
    print(f"   numbers[6:]  = {to_end}    # From index 6 to end")
    print(f"   numbers[:]   = {entire_copy}  # Complete copy")
    
    # 3. NEGATIVE INDEXING
    print(f"\n3️⃣ Negative Indexing:")
    
    last_three = numbers[-3:]        # Last 3 elements
    except_last_two = numbers[:-2]   # All except last 2
    middle_section = numbers[-7:-2]  # Using both negative indices
    
    print(f"   numbers[-3:]   = {last_three}      # Last 3 elements")
    print(f"   numbers[:-2]   = {except_last_two}  # All except last 2")
    print(f"   numbers[-7:-2] = {middle_section}  # Elements -7 to -3")
    
    # 4. STEP PARAMETER
    print(f"\n4️⃣ Step Parameter:")
    
    every_second = numbers[::2]      # Every 2nd element
    every_third = numbers[::3]       # Every 3rd element
    every_second_from_1 = numbers[1::2]  # Every 2nd starting from index 1
    specific_step = numbers[2:8:2]   # Specific range with step
    
    print(f"   numbers[::2]   = {every_second}    # Every 2nd element")
    print(f"   numbers[::3]   = {every_third}       # Every 3rd element")
    print(f"   numbers[1::2]  = {every_second_from_1}  # Every 2nd from index 1")
    print(f"   numbers[2:8:2] = {specific_step}      # Range 2-7 with step 2")
    
    # 5. EDGE CASES AND SPECIAL BEHAVIORS
    print(f"\n5️⃣ Edge Cases and Special Behaviors:")
    
    # Out of bounds handling
    beyond_bounds = numbers[5:20]    # Stop beyond list length
    negative_beyond = numbers[-20:3] # Start beyond list length
    
    print(f"   numbers[5:20]  = {beyond_bounds}  # Stop beyond bounds (safe)")
    print(f"   numbers[-20:3] = {negative_beyond}  # Start beyond bounds (safe)")
    
    # Empty slices
    empty_slice1 = numbers[5:5]      # Same start and stop
    empty_slice2 = numbers[8:3]      # Start after stop
    
    print(f"   numbers[5:5]   = {empty_slice1}           # Same start/stop = empty")
    print(f"   numbers[8:3]   = {empty_slice2}           # Start after stop = empty")
    
    return {
        'basic_slices': {
            'slice1': slice1, 'slice2': slice2, 'slice3': slice3
        },
        'omitted_bounds': {
            'from_start': from_start, 'to_end': to_end, 'entire_copy': entire_copy
        },
        'negative_indices': {
            'last_three': last_three, 'except_last_two': except_last_two
        },
        'step_examples': {
            'every_second': every_second, 'every_third': every_third
        }
    }

def advanced_slicing_techniques():
    """
    Advanced list slicing techniques and patterns
    """
    print("\n🚀 ADVANCED SLICING TECHNIQUES")
    print("=" * 33)
    
    # Sample data for advanced operations
    data = list(range(20))  # [0, 1, 2, ..., 19]
    print(f"Data list: {data}")
    
    # 1. REVERSE SLICING
    print(f"\n1️⃣ Reverse Slicing with Negative Step:")
    
    # Complete reverse
    reversed_list = data[::-1]
    print(f"   data[::-1] = {reversed_list}")
    
    # Reverse a portion
    reverse_portion = data[10:5:-1]
    print(f"   data[10:5:-1] = {reverse_portion}  # Reverse from index 10 to 6")
    
    # Every 2nd element in reverse
    reverse_every_2nd = data[::-2]
    print(f"   data[::-2] = {reverse_every_2nd}  # Every 2nd element, reversed")
    
    # Reverse middle section
    reverse_middle = data[-5:-10:-1]
    print(f"   data[-5:-10:-1] = {reverse_middle}  # Reverse middle section")
    
    # 2. COMPLEX PATTERN EXTRACTION
    print(f"\n2️⃣ Complex Pattern Extraction:")
    
    # Extract elements at specific intervals
    def extract_pattern(lst: List[Any], start: int, interval: int, count: int) -> List[Any]:
        """Extract elements following a specific pattern"""
        return [lst[start + i * interval] for i in range(count) 
                if start + i * interval < len(lst)]
    
    pattern1 = extract_pattern(data, 2, 3, 5)  # Start at 2, every 3rd, 5 elements
    print(f"   Pattern (start=2, interval=3, count=5): {pattern1}")
    
    # Fibonacci-like extraction
    def fibonacci_slice(lst: List[Any], n_terms: int) -> List[Any]:
        """Extract elements at Fibonacci positions"""
        if n_terms <= 0:
            return []
        
        positions = [0, 1]
        for i in range(2, n_terms):
            next_pos = positions[i-1] + positions[i-2]
            if next_pos >= len(lst):
                break
            positions.append(next_pos)
        
        return [lst[pos] for pos in positions if pos < len(lst)]
    
    fib_elements = fibonacci_slice(data, 8)
    print(f"   Fibonacci positions: {fib_elements}")
    
    # 3. CONDITIONAL SLICING
    print(f"\n3️⃣ Conditional Slicing:")
    
    # Slice based on value conditions
    def conditional_slice(lst: List[int], condition: callable, 
                         max_elements: int = None) -> List[int]:
        """Extract elements meeting a condition"""
        result = [item for item in lst if condition(item)]
        if max_elements:
            result = result[:max_elements]
        return result
    
    evens_in_range = conditional_slice(data[5:15], lambda x: x % 2 == 0, 4)
    print(f"   Even numbers from data[5:15], max 4: {evens_in_range}")
    
    # Prime number extraction
    def is_prime(n: int) -> bool:
        """Check if number is prime"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    primes = conditional_slice(data[2:], is_prime, 6)
    print(f"   First 6 primes from data[2:]: {primes}")
    
    # 4. MULTI-DIMENSIONAL SLICING
    print(f"\n4️⃣ Multi-Dimensional Slicing:")
    
    # Create 2D matrix
    matrix = [[i * 4 + j for j in range(4)] for i in range(5)]
    print(f"   Matrix (5x4):")
    for row in matrix:
        print(f"     {row}")
    
    # Row slicing
    row_slice = matrix[1:4]
    print(f"   Rows 1-3: {row_slice}")
    
    # Column extraction using list comprehension with slicing
    column_2 = [row[2] for row in matrix]
    print(f"   Column 2: {column_2}")
    
    # Submatrix extraction
    submatrix = [row[1:3] for row in matrix[1:4]]
    print(f"   Submatrix (rows 1-3, cols 1-2): {submatrix}")
    
    # 5. SLIDING WINDOW TECHNIQUE
    print(f"\n5️⃣ Sliding Window Technique:")
    
    def sliding_window(lst: List[Any], window_size: int, step: int = 1) -> List[List[Any]]:
        """Generate sliding windows over a list"""
        windows = []
        for i in range(0, len(lst) - window_size + 1, step):
            windows.append(lst[i:i + window_size])
        return windows
    
    # Simple sliding window
    windows_3 = sliding_window(data[:10], 3)
    print(f"   Sliding windows (size=3) over data[:10]:")
    for i, window in enumerate(windows_3):
        print(f"     Window {i}: {window}")
    
    # Overlapping windows with step
    windows_step = sliding_window(data[:12], 4, 2)
    print(f"   Sliding windows (size=4, step=2) over data[:12]:")
    for i, window in enumerate(windows_step):
        print(f"     Window {i}: {window}")
    
    return {
        'reverse_operations': {
            'complete_reverse': reversed_list,
            'reverse_portion': reverse_portion
        },
        'pattern_extraction': {
            'custom_pattern': pattern1,
            'fibonacci_elements': fib_elements
        },
        'conditional_results': {
            'evens_in_range': evens_in_range,
            'primes': primes
        },
        'multidimensional': {
            'matrix': matrix,
            'submatrix': submatrix
        },
        'sliding_windows': {
            'simple_windows': windows_3,
            'stepped_windows': windows_step
        }
    }

def slicing_for_modification():
    """
    Using slicing for list modification and assignment
    """
    print("\n✏️ SLICING FOR MODIFICATION")
    print("=" * 28)
    
    print("🎯 Slice Assignment:")
    print("   Slicing can be used on the left side of assignment to modify lists")
    print("   This allows for insertion, deletion, and replacement operations")
    
    # 1. REPLACING ELEMENTS
    print(f"\n1️⃣ Replacing Elements with Slice Assignment:")
    
    numbers = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"   Original: {numbers}")
    
    # Replace a range
    numbers[2:5] = [20, 30, 40]
    print(f"   After numbers[2:5] = [20, 30, 40]: {numbers}")
    
    # Replace with different sized list
    numbers[1:3] = [100, 200, 300, 400]  # Replace 2 elements with 4
    print(f"   After numbers[1:3] = [100, 200, 300, 400]: {numbers}")
    
    # 2. INSERTING ELEMENTS
    print(f"\n2️⃣ Inserting Elements:")
    
    fruits = ['apple', 'cherry', 'elderberry']
    print(f"   Original fruits: {fruits}")
    
    # Insert using empty slice
    fruits[1:1] = ['banana']  # Insert at position 1
    print(f"   After fruits[1:1] = ['banana']: {fruits}")
    
    # Insert multiple elements
    fruits[3:3] = ['date', 'fig']  # Insert at position 3
    print(f"   After fruits[3:3] = ['date', 'fig']: {fruits}")
    
    # 3. DELETING ELEMENTS
    print(f"\n3️⃣ Deleting Elements:")
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    print(f"   Original letters: {letters}")
    
    # Delete a range
    del letters[2:5]  # Delete elements at indices 2, 3, 4
    print(f"   After del letters[2:5]: {letters}")
    
    # Delete using empty assignment
    letters[1:3] = []  # Delete elements at indices 1, 2
    print(f"   After letters[1:3] = []: {letters}")
    
    # 4. STEP-BASED MODIFICATION
    print(f"\n4️⃣ Step-Based Modification:")
    
    sequence = list(range(20))
    print(f"   Original sequence: {sequence}")
    
    # Replace every 3rd element in a range
    sequence[2:15:3] = [999] * len(sequence[2:15:3])
    print(f"   After sequence[2:15:3] = [999] * count: {sequence}")
    
    # Replace every 2nd element with step
    values = [10, 20, 30, 40, 50, 60]
    values[::2] = [100, 300, 500]  # Replace elements at indices 0, 2, 4
    print(f"   After values[::2] = [100, 300, 500]: {values}")
    
    # 5. ADVANCED MODIFICATION PATTERNS
    print(f"\n5️⃣ Advanced Modification Patterns:")
    
    # Rotate elements using slicing
    def rotate_left(lst: List[Any], positions: int) -> List[Any]:
        """Rotate list elements to the left"""
        n = len(lst)
        positions = positions % n  # Handle positions > length
        return lst[positions:] + lst[:positions]
    
    def rotate_right(lst: List[Any], positions: int) -> List[Any]:
        """Rotate list elements to the right"""
        n = len(lst)
        positions = positions % n
        return lst[-positions:] + lst[:-positions]
    
    original_rotate = [1, 2, 3, 4, 5, 6, 7, 8]
    rotated_left = rotate_left(original_rotate.copy(), 3)
    rotated_right = rotate_right(original_rotate.copy(), 2)
    
    print(f"   Original: {original_rotate}")
    print(f"   Rotated left 3 positions: {rotated_left}")
    print(f"   Rotated right 2 positions: {rotated_right}")
    
    # In-place reversal of portions
    def reverse_portion_inplace(lst: List[Any], start: int, end: int):
        """Reverse a portion of list in-place using slicing"""
        lst[start:end] = lst[start:end][::-1]
    
    reverse_demo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"   Before reversing middle portion: {reverse_demo}")
    reverse_portion_inplace(reverse_demo, 2, 7)
    print(f"   After reversing indices 2-6: {reverse_demo}")
    
    return {
        'replacement_examples': {
            'basic_replace': [20, 30, 40],
            'size_change': [100, 200, 300, 400]
        },
        'insertion_results': fruits,
        'deletion_results': letters,
        'rotation_examples': {
            'left_rotation': rotated_left,
            'right_rotation': rotated_right
        }
    }

def performance_analysis():
    """
    Performance analysis of different slicing operations
    """
    print("\n⚡ PERFORMANCE ANALYSIS OF SLICING")
    print("=" * 36)
    
    def time_operation(func, *args, iterations=10000):
        """Time a slicing operation"""
        start = time.perf_counter()
        for _ in range(iterations):
            result = func(*args)
        end = time.perf_counter()
        return (end - start) * 1000 / iterations, result
    
    # Test data of different sizes
    small_list = list(range(100))
    medium_list = list(range(1000))
    large_list = list(range(10000))
    
    print("📊 Slicing Performance Comparison:")
    print("   Operation                │ Small (100) │ Medium (1K) │ Large (10K) │ Notes")
    print("   ─────────────────────────┼─────────────┼─────────────┼─────────────┼─────────────────")
    
    # Different slicing operations
    operations = [
        ("Simple slice [10:50]", lambda lst: lst[10:50], "Basic range extraction"),
        ("Copy entire list [:]", lambda lst: lst[:], "Full list copy"),
        ("Every 2nd element [::2]", lambda lst: lst[::2], "Step-based extraction"),
        ("Reverse slice [::-1]", lambda lst: lst[::-1], "Complete reversal"),
        ("Negative indices [-50:-10]", lambda lst: lst[-50:-10] if len(lst) >= 50 else lst[-10:], "Negative indexing")
    ]
    
    for op_name, op_func, notes in operations:
        times = []
        for test_list in [small_list, medium_list, large_list]:
            op_time, _ = time_operation(op_func, test_list, iterations=1000)
            times.append(op_time)
        
        print(f"   {op_name:<24} │ {times[0]:9.4f} ms │ {times[1]:9.4f} ms │ {times[2]:9.4f} ms │ {notes}")
    
    # Memory analysis
    print(f"\n💾 Memory Usage Analysis:")
    
    def analyze_memory_usage():
        """Analyze memory usage of slicing operations"""
        original = list(range(1000))
        
        # Different slice sizes
        small_slice = original[10:20]  # 10 elements
        medium_slice = original[100:600]  # 500 elements
        large_slice = original[:]  # 1000 elements (copy)
        
        return {
            'original': sys.getsizeof(original),
            'small_slice': sys.getsizeof(small_slice),
            'medium_slice': sys.getsizeof(medium_slice),
            'large_slice': sys.getsizeof(large_slice)
        }
    
    memory_data = analyze_memory_usage()
    
    print("   Slice Type        │ Memory Usage │ Slice Size")
    print("   ──────────────────┼──────────────┼─────────────────")
    print(f"   Original (1000)   │ {memory_data['original']:10,} B │ 1000 elements")
    print(f"   Small slice (10)  │ {memory_data['small_slice']:10,} B │ 10 elements")
    print(f"   Medium slice (500)│ {memory_data['medium_slice']:10,} B │ 500 elements")
    print(f"   Large slice (1000)│ {memory_data['large_slice']:10,} B │ 1000 elements")
    
    # Best practices
    print(f"\n💡 Performance Best Practices:")
    best_practices = [
        "Use slicing for copying instead of loops - it's implemented in C",
        "Avoid creating unnecessary intermediate slices in long chains",
        "Consider generators for large datasets you'll only iterate once",
        "Use [:] for shallow copying instead of list() constructor",
        "Be aware that slicing creates new objects, not views",
        "Step-based slicing ([::n]) is efficient for regular patterns",
        "Negative indexing has same performance as positive indexing"
    ]
    
    for i, practice in enumerate(best_practices, 1):
        print(f"   {i}. {practice}")
    
    return {
        'performance_data': operations,
        'memory_analysis': memory_data,
        'best_practices': best_practices
    }

def practical_applications():
    """
    Practical applications of list slicing in real-world scenarios
    """
    print("\n🌍 PRACTICAL APPLICATIONS")
    print("=" * 27)
    
    print("🚀 Real-World Slicing Scenarios:")
    
    # 1. DATA PROCESSING - TIME SERIES
    print(f"\n1️⃣ Time Series Data Processing:")
    
    # Simulate temperature data over 30 days
    temperatures = [20 + (i * 0.5) + (i % 7) * 2 for i in range(30)]
    
    # Extract different time periods
    first_week = temperatures[:7]
    last_week = temperatures[-7:]
    middle_two_weeks = temperatures[7:21]
    every_other_day = temperatures[::2]
    
    print(f"   Full month temperatures (30 days): {[round(t, 1) for t in temperatures[:10]]}...")
    print(f"   First week: {[round(t, 1) for t in first_week]}")
    print(f"   Last week: {[round(t, 1) for t in last_week]}")
    print(f"   Every other day: {[round(t, 1) for t in every_other_day[:10]]}...")
    
    # Calculate weekly averages
    weekly_averages = []
    for week_start in range(0, len(temperatures), 7):
        week_data = temperatures[week_start:week_start + 7]
        weekly_averages.append(sum(week_data) / len(week_data))
    
    print(f"   Weekly averages: {[round(avg, 1) for avg in weekly_averages]}")
    
    # 2. TEXT PROCESSING
    print(f"\n2️⃣ Text Processing and Analysis:")
    
    text = "The quick brown fox jumps over the lazy dog multiple times"
    words = text.split()
    
    # Extract different portions of text
    first_half = words[:len(words)//2]
    last_three = words[-3:]
    every_second_word = words[::2]
    reverse_words = words[::-1]
    
    print(f"   Original text: '{text}'")
    print(f"   Words: {words}")
    print(f"   First half: {first_half}")
    print(f"   Last three words: {last_three}")
    print(f"   Every second word: {every_second_word}")
    print(f"   Words reversed: {reverse_words[:5]}...")  # Show first 5
    
    # 3. LOG FILE PROCESSING
    print(f"\n3️⃣ Log File Processing:")
    
    # Simulate log entries
    log_entries = [
        "2024-01-15 10:30:22 INFO User login successful",
        "2024-01-15 10:31:15 DEBUG Database connection established",
        "2024-01-15 10:32:01 INFO Processing request #12345",
        "2024-01-15 10:32:45 ERROR Database timeout occurred",
        "2024-01-15 10:33:10 WARN Retry attempt #1",
        "2024-01-15 10:33:30 INFO Request completed successfully",
        "2024-01-15 10:34:00 INFO User logout",
        "2024-01-15 10:35:15 ERROR Connection lost"
    ]
    
    # Extract recent logs (last 3 entries)
    recent_logs = log_entries[-3:]
    
    # Extract error logs only
    error_logs = [log for log in log_entries if 'ERROR' in log]
    
    # Get logs from specific time range (entries 2-5)
    time_range_logs = log_entries[2:6]
    
    print(f"   Total log entries: {len(log_entries)}")
    print(f"   Recent logs (last 3):")
    for log in recent_logs:
        print(f"     {log}")
    
    print(f"   Error logs: {len(error_logs)} found")
    for log in error_logs:
        print(f"     {log}")
    
    # 4. PAGINATION SYSTEM
    print(f"\n4️⃣ Pagination System Implementation:")
    
    def paginate(data: List[Any], page_number: int, items_per_page: int) -> dict:
        """Implement pagination using slicing"""
        total_items = len(data)
        total_pages = (total_items + items_per_page - 1) // items_per_page  # Ceiling division
        
        if page_number < 1 or page_number > total_pages:
            return {
                'data': [],
                'page_info': {
                    'current_page': page_number,
                    'total_pages': total_pages,
                    'items_per_page': items_per_page,
                    'total_items': total_items,
                    'error': 'Page number out of range'
                }
            }
        
        start_index = (page_number - 1) * items_per_page
        end_index = start_index + items_per_page
        page_data = data[start_index:end_index]
        
        return {
            'data': page_data,
            'page_info': {
                'current_page': page_number,
                'total_pages': total_pages,
                'items_per_page': items_per_page,
                'total_items': total_items,
                'has_previous': page_number > 1,
                'has_next': page_number < total_pages
            }
        }
    
    # Sample data - list of products
    products = [f"Product_{i:03d}" for i in range(1, 101)]  # 100 products
    
    # Get different pages
    page_1 = paginate(products, 1, 10)
    page_5 = paginate(products, 5, 10)
    last_page = paginate(products, 10, 10)
    
    print(f"   Total products: {len(products)}")
    print(f"   Page 1 (10 items): {page_1['data']}")
    print(f"   Page 5 (10 items): {page_5['data']}")
    print(f"   Page info for page 5: {page_5['page_info']}")
    
    # 5. DATA VALIDATION AND CLEANING
    print(f"\n5️⃣ Data Validation and Cleaning:")
    
    # Simulate sensor data with some invalid readings
    sensor_readings = [23.5, 24.1, -999, 25.3, 24.8, 0, 26.1, -999, 25.5, 24.9, 
                      26.3, -999, 25.1, 24.7, 25.8]
    
    print(f"   Raw sensor data: {sensor_readings}")
    
    # Find and remove invalid readings (-999 indicates sensor error)
    def clean_sensor_data(readings: List[float], invalid_value: float = -999) -> dict:
        """Clean sensor data by removing invalid readings"""
        valid_indices = [i for i, val in enumerate(readings) if val != invalid_value]
        clean_data = [readings[i] for i in valid_indices]
        
        # Use slicing to get data before and after gaps
        gaps = []
        for i, val in enumerate(readings):
            if val == invalid_value:
                before = readings[:i] if i > 0 else []
                after = readings[i+1:] if i < len(readings) - 1 else []
                gaps.append({
                    'position': i,
                    'before': before[-2:] if len(before) >= 2 else before,
                    'after': after[:2] if len(after) >= 2 else after
                })
        
        return {
            'cleaned_data': clean_data,
            'invalid_count': len(readings) - len(clean_data),
            'gaps_info': gaps[:3]  # Show first 3 gaps
        }
    
    cleaning_result = clean_sensor_data(sensor_readings)
    
    print(f"   Cleaned data: {cleaning_result['cleaned_data']}")
    print(f"   Invalid readings removed: {cleaning_result['invalid_count']}")
    print(f"   Data gaps detected at positions: {[gap['position'] for gap in cleaning_result['gaps_info']]}")
    
    return {
        'time_series': {
            'weekly_averages': weekly_averages,
            'temperature_ranges': {
                'first_week': first_week,
                'last_week': last_week
            }
        },
        'text_processing': {
            'word_analysis': {
                'total_words': len(words),
                'first_half_count': len(first_half)
            }
        },
        'log_processing': {
            'total_logs': len(log_entries),
            'error_count': len(error_logs),
            'recent_count': len(recent_logs)
        },
        'pagination': {
            'total_pages': page_1['page_info']['total_pages'],
            'items_per_page': 10
        },
        'data_cleaning': {
            'original_count': len(sensor_readings),
            'cleaned_count': len(cleaning_result['cleaned_data']),
            'invalid_removed': cleaning_result['invalid_count']
        }
    }

# =============================================================================
# MAIN EXECUTION AND COMPREHENSIVE DEMONSTRATION
# =============================================================================

def main():
    """
    Main function executing comprehensive list slicing guide
    """
    print(__doc__)
    
    # Core sections
    fundamentals = list_slicing_fundamentals()
    basic_operations = basic_slicing_operations()
    advanced_techniques = advanced_slicing_techniques()
    modification_ops = slicing_for_modification()
    performance = performance_analysis()
    applications = practical_applications()
    
    return {
        'fundamentals': fundamentals,
        'basic_operations': basic_operations,
        'advanced_techniques': advanced_techniques,
        'modification_operations': modification_ops,
        'performance_analysis': performance,
        'practical_applications': applications
    }

if __name__ == "__main__":
    """
    Execute comprehensive list slicing guide
    """
    results = main()
    
    print("\n" + "=" * 80)
    print("🎓 LIST SLICING MASTERY SUMMARY")
    print("=" * 80)
    print("✅ Complete understanding of basic and advanced slicing syntax")
    print("✅ Mastery of slice assignment for list modification")
    print("✅ Advanced pattern extraction and conditional slicing techniques")
    print("✅ Performance analysis and memory usage optimization")
    print("✅ Multi-dimensional and nested structure slicing")
    print("✅ Real-world applications in data processing, text analysis, and pagination")
    print("✅ Best practices for efficient slicing operations")
    
    print("\n💡 List Slicing Mastery Key Points:")
    key_points = [
        "Slicing syntax [start:stop:step] provides powerful sequence extraction",
        "Negative indices allow reverse direction access and slicing",
        "Slice assignment enables in-place modification without loops",
        "Step parameter creates patterns and enables efficient data sampling",
        "Slicing creates new objects - understand memory implications",
        "Advanced techniques enable complex data extraction patterns",
        "Performance is excellent due to C-level implementation",
        "Practical applications span data science, web development, and system administration"
    ]
    
    for point in key_points:
        print(f"   • {point}")
    
    print("\n🎯 Expert-Level Applications:")
    applications = [
        "Time series data analysis and windowing operations",
        "Text processing and natural language analysis pipelines",
        "Log file parsing and monitoring system data extraction",
        "Pagination systems for web applications and APIs",
        "Data cleaning and validation in scientific computing",
        "Image processing and computer vision array manipulation",
        "Machine learning data preprocessing and feature extraction",
        "Database query result processing and data transformation"
    ]
    
    for i, application in enumerate(applications, 1):
        print(f"   {i}. {application}")
    
    print(f"\n🚀 Master List Slicing for Powerful Data Manipulation!")
    print("Slicing is fundamental to efficient Pythonic data processing!")

# =============================================================================
# ORIGINAL SIMPLE EXAMPLE (Enhanced with Context)
# =============================================================================

# Simple demonstration of basic list slicing
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Example of a list
sliced_list = lst[2:5]  # Slicing the list from index 2 to index 5 (exclusive)
print("\nBasic Slicing Example:")
print(f"Original list: {lst}")
print(f"Sliced list lst[2:5]: {sliced_list}")  # Output: [3, 4, 5]
print("This extracts elements at indices 2, 3, and 4 (5 is exclusive)!")