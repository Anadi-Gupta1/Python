"""
List Traversing and Iteration - Complete Python Guide
====================================================

Comprehensive guide to traversing, iterating, and accessing Python lists
using various methods, patterns, and advanced techniques. Master all
approaches to efficiently process list elements and extract information.

Author: Python Learning Notes
Date: September 2025
Topic: List Traversal, Iteration, Access Patterns, Advanced Techniques
"""

import time
import sys
from typing import List, Any, Union, Optional, Iterator, Tuple, Callable
from itertools import enumerate as builtin_enumerate, zip_longest, chain
from functools import reduce

# =============================================================================
# FUNDAMENTALS OF LIST TRAVERSAL
# =============================================================================

def list_traversal_fundamentals():
    """
    Understanding the fundamentals of list traversal and access
    """
    print("🚶 LIST TRAVERSAL FUNDAMENTALS")
    print("=" * 32)
    
    print("🎯 What is List Traversal?")
    print("   List traversal is the process of visiting each element in a list")
    print("   systematically. Python provides multiple approaches with different")
    print("   use cases, performance characteristics, and capabilities.")
    
    print(f"\n📋 Types of List Access and Traversal:")
    access_types = [
        ("Direct Indexing", "Access specific element by position", "list[index]", "O(1) time complexity"),
        ("Sequential Iteration", "Visit elements in order", "for item in list", "Simple and Pythonic"),
        ("Indexed Iteration", "Iterate with position info", "for i, item in enumerate(list)", "Access to both index and value"),
        ("Reverse Traversal", "Process elements backwards", "for item in reversed(list)", "Reverse order processing"),
        ("Conditional Traversal", "Process based on criteria", "if-conditions in loops", "Selective processing"),
        ("Parallel Traversal", "Multiple lists simultaneously", "for a, b in zip(list1, list2)", "Synchronized iteration"),
        ("Nested Traversal", "Process multi-dimensional lists", "Nested for loops", "Complex data structures")
    ]
    
    print("   Type                │ Description                  │ Syntax Example           │ Use Case")
    print("   ────────────────────┼──────────────────────────────┼──────────────────────────┼──────────────────")
    
    for access_type, desc, syntax, use_case in access_types:
        print(f"   {access_type:<19} │ {desc:<28} │ {syntax:<24} │ {use_case}")
    
    print(f"\n🔢 Indexing Fundamentals:")
    print("   • Positive indices: 0, 1, 2, ... (left to right)")
    print("   • Negative indices: -1, -2, -3, ... (right to left)")
    print("   • IndexError raised for out-of-bounds access")
    print("   • Length check with len() before accessing")
    
    return {'access_types': access_types}

def basic_access_methods():
    """
    Demonstrate basic list access methods
    """
    print("\n👆 BASIC ACCESS METHODS")
    print("=" * 25)
    
    # Sample list for demonstrations
    fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    numbers = [10, 20, 30, 40, 50]
    
    print(f"Sample lists:")
    print(f"   fruits = {fruits}")
    print(f"   numbers = {numbers}")
    
    # 1. DIRECT INDEXING ACCESS
    print(f"\n1️⃣ Direct Indexing Access:")
    
    # Positive indexing
    first = fruits[0]
    third = fruits[2]
    last = fruits[6]  # or fruits[-1]
    
    print(f"   fruits[0] (first) = '{first}'")
    print(f"   fruits[2] (third) = '{third}'")
    print(f"   fruits[6] (last) = '{last}'")
    
    # Negative indexing
    last_neg = fruits[-1]
    second_last = fruits[-2]
    third_last = fruits[-3]
    
    print(f"   fruits[-1] (last) = '{last_neg}'")
    print(f"   fruits[-2] (second last) = '{second_last}'")
    print(f"   fruits[-3] (third last) = '{third_last}'")
    
    # 2. SAFE ACCESS WITH BOUNDS CHECKING
    print(f"\n2️⃣ Safe Access with Bounds Checking:")
    
    def safe_access(lst: List[Any], index: int, default: Any = None) -> Any:
        """Safely access list element with bounds checking"""
        try:
            return lst[index]
        except IndexError:
            return default
    
    # Safe access examples
    valid_access = safe_access(fruits, 2)  # Valid index
    invalid_access = safe_access(fruits, 20, "Not Found")  # Invalid index
    negative_access = safe_access(fruits, -1)  # Valid negative
    
    print(f"   safe_access(fruits, 2) = '{valid_access}'")
    print(f"   safe_access(fruits, 20, 'Not Found') = '{invalid_access}'")
    print(f"   safe_access(fruits, -1) = '{negative_access}'")
    
    # Alternative safe access using conditional
    index_to_check = 15
    result = fruits[index_to_check] if 0 <= index_to_check < len(fruits) else "Index out of range"
    print(f"   Conditional access fruits[{index_to_check}] = '{result}'")
    
    # 3. MULTIPLE ELEMENT ACCESS
    print(f"\n3️⃣ Multiple Element Access:")
    
    # Access multiple elements by indices
    indices = [0, 2, 4, 6]
    selected_fruits = [fruits[i] for i in indices if i < len(fruits)]
    print(f"   Elements at indices {indices}: {selected_fruits}")
    
    # First and last elements
    first_last = [fruits[0], fruits[-1]]
    print(f"   First and last: {first_last}")
    
    # First n elements
    first_three = [fruits[i] for i in range(min(3, len(fruits)))]
    print(f"   First three elements: {first_three}")
    
    return {
        'basic_access': {
            'positive_indexing': [first, third, last],
            'negative_indexing': [last_neg, second_last, third_last]
        },
        'safe_access': {
            'valid': valid_access,
            'invalid': invalid_access,
            'method_demonstration': True
        },
        'multiple_access': {
            'selected_elements': selected_fruits,
            'first_last': first_last
        }
    }

def iteration_patterns():
    """
    Comprehensive demonstration of iteration patterns
    """
    print("\n🔄 ITERATION PATTERNS")
    print("=" * 22)
    
    # Sample data for iteration demonstrations
    colors = ["red", "green", "blue", "yellow", "orange", "purple"]
    scores = [85, 92, 78, 96, 88, 91]
    
    print(f"Sample data:")
    print(f"   colors = {colors}")
    print(f"   scores = {scores}")
    
    # 1. BASIC FOR LOOP ITERATION
    print(f"\n1️⃣ Basic For Loop Iteration:")
    
    print("   Basic iteration over colors:")
    for i, color in enumerate(colors[:3], 1):  # Show first 3 for brevity
        print(f"     {i}. {color}")
    
    # 2. ENUMERATE - GETTING INDEX AND VALUE
    print(f"\n2️⃣ Enumerate - Index and Value Access:")
    
    print("   Using enumerate() for indexed iteration:")
    result_enumerate = []
    for index, color in enumerate(colors):
        result_enumerate.append(f"Color {index}: {color}")
    
    for item in result_enumerate[:4]:  # Show first 4
        print(f"     {item}")
    
    # Custom start value for enumerate
    print("   Enumerate with custom start (starting from 1):")
    for position, color in enumerate(colors[:3], start=1):
        print(f"     Position {position}: {color}")
    
    # 3. REVERSE ITERATION
    print(f"\n3️⃣ Reverse Iteration:")
    
    # Using reversed()
    print("   Using reversed():")
    reversed_colors = list(reversed(colors))[:3]  # First 3 of reversed
    for color in reversed_colors:
        print(f"     {color}")
    
    # Using negative slicing
    print("   Using slice [::-1]:")
    for color in colors[::-1][:3]:  # First 3 of reversed slice
        print(f"     {color}")
    
    # Manual reverse with indices
    print("   Manual reverse with indices:")
    for i in range(len(colors) - 1, max(len(colors) - 4, -1), -1):  # Last 3
        print(f"     Index {i}: {colors[i]}")
    
    # 4. CONDITIONAL ITERATION
    print(f"\n4️⃣ Conditional Iteration:")
    
    # Filter during iteration
    print("   Processing only high scores (>= 90):")
    high_scores = [(i, score) for i, score in enumerate(scores) if score >= 90]
    for index, score in high_scores:
        print(f"     Student {index}: {score}")
    
    # Skip certain elements
    print("   Skipping colors containing 'r':")
    filtered_colors = [color for color in colors if 'r' not in color][:3]  # First 3
    for color in filtered_colors:
        print(f"     {color}")
    
    # 5. PARALLEL ITERATION WITH ZIP
    print(f"\n5️⃣ Parallel Iteration with zip():")
    
    # Zip two lists of same length
    print("   Combining colors and scores:")
    for color, score in zip(colors, scores)[:4]:  # First 4 pairs
        print(f"     {color}: {score}")
    
    # Zip lists of different lengths
    short_list = ["A", "B", "C"]
    print("   Zip with different lengths (shorter list determines result):")
    for color, letter in zip(colors, short_list):
        print(f"     {color} - {letter}")
    
    # Using zip_longest for unequal lengths
    print("   Using zip_longest for unequal lengths:")
    from itertools import zip_longest
    for color, letter in zip_longest(colors[:4], short_list, fillvalue="N/A"):
        print(f"     {color} - {letter}")
    
    # 6. NESTED ITERATION
    print(f"\n6️⃣ Nested Iteration (2D Lists):")
    
    # Create a 2D matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("   Matrix traversal:")
    for i, row in enumerate(matrix):
        print(f"     Row {i}: {row}")
        for j, element in enumerate(row):
            if j < 2:  # Show first 2 elements of each row for brevity
                print(f"       Element [{i}][{j}]: {element}")
    
    # Flatten nested list during iteration
    print("   Flattening during iteration:")
    flattened = [element for row in matrix for element in row][:6]  # First 6
    print(f"     Flattened: {flattened}")
    
    return {
        'iteration_results': {
            'enumerate_results': result_enumerate,
            'reversed_colors': reversed_colors,
            'high_scores': high_scores,
            'filtered_colors': filtered_colors
        },
        'parallel_iteration': {
            'color_score_pairs': list(zip(colors, scores))[:4],
            'zip_different_lengths': list(zip(colors, short_list))
        },
        'nested_structure': {
            'matrix': matrix,
            'flattened': flattened
        }
    }

def advanced_traversal_techniques():
    """
    Advanced list traversal techniques and patterns
    """
    print("\n🚀 ADVANCED TRAVERSAL TECHNIQUES")
    print("=" * 35)
    
    # Sample data for advanced techniques
    data = list(range(20))  # [0, 1, 2, ..., 19]
    nested_data = [[i, i+1, i+2] for i in range(0, 15, 3)]  # [[0,1,2], [3,4,5], ...]
    
    print(f"Sample data: {data[:10]}... (20 elements)")
    print(f"Nested data: {nested_data}")
    
    # 1. SLIDING WINDOW ITERATION
    print(f"\n1️⃣ Sliding Window Iteration:")
    
    def sliding_window_traverse(lst: List[Any], window_size: int, 
                              processor: Callable = None) -> List[Any]:
        """Traverse list using sliding window pattern"""
        results = []
        for i in range(len(lst) - window_size + 1):
            window = lst[i:i + window_size]
            if processor:
                results.append(processor(window))
            else:
                results.append(window)
        return results
    
    # Simple sliding window
    windows_3 = sliding_window_traverse(data[:8], 3)
    print(f"   Sliding windows (size 3) over data[:8]:")
    for i, window in enumerate(windows_3[:4]):  # Show first 4
        print(f"     Window {i}: {window}")
    
    # Sliding window with processing
    window_sums = sliding_window_traverse(data[:8], 3, sum)
    print(f"   Window sums: {window_sums}")
    
    # 2. BATCH PROCESSING ITERATION
    print(f"\n2️⃣ Batch Processing Iteration:")
    
    def batch_process(lst: List[Any], batch_size: int, 
                     processor: Callable = None) -> List[Any]:
        """Process list in batches"""
        results = []
        for i in range(0, len(lst), batch_size):
            batch = lst[i:i + batch_size]
            if processor:
                results.append(processor(batch))
            else:
                results.append(batch)
        return results
    
    # Simple batching
    batches = batch_process(data[:12], 4)
    print(f"   Batches (size 4) over data[:12]:")
    for i, batch in enumerate(batches):
        print(f"     Batch {i}: {batch}")
    
    # Batch processing with function
    batch_averages = batch_process(data[:12], 4, lambda batch: sum(batch) / len(batch))
    print(f"   Batch averages: {batch_averages}")
    
    # 3. CONDITIONAL TRAVERSAL WITH STATE
    print(f"\n3️⃣ Conditional Traversal with State:")
    
    def stateful_traversal(lst: List[int], condition: Callable) -> dict:
        """Traverse list maintaining state information"""
        state = {
            'processed': [],
            'skipped': [],
            'running_total': 0,
            'max_seen': float('-inf'),
            'min_seen': float('inf')
        }
        
        for i, item in enumerate(lst):
            if condition(item, i, state):
                state['processed'].append((i, item))
                state['running_total'] += item
                state['max_seen'] = max(state['max_seen'], item)
                state['min_seen'] = min(state['min_seen'], item)
            else:
                state['skipped'].append((i, item))
        
        return state
    
    # Process even numbers that are greater than 5
    condition = lambda x, i, state: x % 2 == 0 and x > 5
    state_result = stateful_traversal(data[:15], condition)
    
    print(f"   Condition: even numbers > 5")
    print(f"   Processed: {state_result['processed'][:5]}...")  # First 5
    print(f"   Skipped count: {len(state_result['skipped'])}")
    print(f"   Running total: {state_result['running_total']}")
    
    # 4. MULTI-LEVEL NESTED TRAVERSAL
    print(f"\n4️⃣ Multi-Level Nested Traversal:")
    
    def deep_traverse(structure: Any, path: List[str] = None) -> List[Tuple[List[str], Any]]:
        """Recursively traverse nested list structures"""
        if path is None:
            path = []
        
        results = []
        
        if isinstance(structure, list):
            for i, item in enumerate(structure):
                current_path = path + [f"[{i}]"]
                if isinstance(item, list):
                    results.extend(deep_traverse(item, current_path))
                else:
                    results.append((current_path, item))
        else:
            results.append((path, structure))
        
        return results
    
    # Create complex nested structure
    complex_nested = [
        [1, 2, [3, 4]],
        [5, 6],
        [7, [8, 9, [10, 11]]]
    ]
    
    deep_results = deep_traverse(complex_nested)
    print(f"   Complex nested structure: {complex_nested}")
    print(f"   Deep traversal results:")
    for path, value in deep_results[:6]:  # First 6 results
        print(f"     {''.join(path)}: {value}")
    
    # 5. PARALLEL MULTI-LIST TRAVERSAL
    print(f"\n5️⃣ Parallel Multi-List Traversal:")
    
    def parallel_traverse(*lists, processor: Callable = None) -> List[Any]:
        """Traverse multiple lists in parallel"""
        results = []
        
        # Use zip_longest to handle different lengths
        for items in zip_longest(*lists, fillvalue=None):
            if processor:
                results.append(processor(items))
            else:
                results.append(items)
        
        return results
    
    # Parallel traversal of three lists
    list_a = [1, 2, 3, 4, 5]
    list_b = ['a', 'b', 'c', 'd']
    list_c = [10, 20, 30, 40, 50, 60]
    
    parallel_results = parallel_traverse(list_a, list_b, list_c)[:5]  # First 5
    print(f"   Lists: {list_a}, {list_b[:4]}..., {list_c[:5]}...")
    print(f"   Parallel traversal:")
    for i, items in enumerate(parallel_results):
        print(f"     Position {i}: {items}")
    
    # Parallel traversal with processing
    def sum_numeric(items):
        """Sum only numeric items"""
        return sum(x for x in items if isinstance(x, (int, float)) and x is not None)
    
    parallel_sums = parallel_traverse(list_a, [10, 20, 30], [100, 200, 300, 400], 
                                    processor=sum_numeric)[:4]
    print(f"   Parallel sums: {parallel_sums}")
    
    # 6. GENERATOR-BASED TRAVERSAL
    print(f"\n6️⃣ Generator-Based Traversal:")
    
    def lazy_traverse(lst: List[Any], transformer: Callable = None) -> Iterator[Any]:
        """Lazy traversal using generator"""
        for item in lst:
            if transformer:
                yield transformer(item)
            else:
                yield item
    
    # Memory-efficient traversal
    lazy_squares = lazy_traverse(data[:10], lambda x: x**2)
    print(f"   Lazy squares generator created")
    print(f"   First 5 squares: {[next(lazy_squares) for _ in range(5)]}")
    
    return {
        'sliding_windows': {
            'windows': windows_3[:3],
            'window_sums': window_sums[:3]
        },
        'batch_processing': {
            'batches': batches,
            'averages': batch_averages
        },
        'stateful_traversal': {
            'processed_count': len(state_result['processed']),
            'running_total': state_result['running_total']
        },
        'deep_traversal': {
            'total_paths': len(deep_results),
            'first_paths': deep_results[:3]
        },
        'parallel_traversal': {
            'results_count': len(parallel_results),
            'parallel_sums': parallel_sums
        }
    }

def performance_analysis():
    """
    Performance analysis of different traversal methods
    """
    print("\n⚡ PERFORMANCE ANALYSIS OF TRAVERSAL METHODS")
    print("=" * 46)
    
    def time_traversal(func, data, iterations=1000):
        """Time a traversal operation"""
        start = time.perf_counter()
        for _ in range(iterations):
            result = func(data)
        end = time.perf_counter()
        return (end - start) * 1000 / iterations, result
    
    # Test data of different sizes
    small_list = list(range(100))
    medium_list = list(range(1000))
    large_list = list(range(10000))
    
    test_data = [
        ("Small (100)", small_list),
        ("Medium (1K)", medium_list),
        ("Large (10K)", large_list)
    ]
    
    print("📊 Traversal Method Performance Comparison:")
    print("   Method                   │ Small (100) │ Medium (1K) │ Large (10K) │ Notes")
    print("   ─────────────────────────┼─────────────┼─────────────┼─────────────┼─────────────────")
    
    # Different traversal methods
    methods = [
        ("Basic for loop", lambda lst: [x for x in lst], "Standard iteration"),
        ("List comprehension", lambda lst: [x*2 for x in lst], "With transformation"),
        ("enumerate()", lambda lst: [(i, x) for i, x in enumerate(lst)], "Index + value"),
        ("map() function", lambda lst: list(map(lambda x: x*2, lst)), "Functional approach"),
        ("Generator expression", lambda lst: list(x*2 for x in lst), "Lazy evaluation"),
        ("While loop (indexed)", lambda lst: [lst[i] for i in range(len(lst))], "Manual indexing")
    ]
    
    for method_name, method_func, notes in methods:
        times = []
        
        for size_name, test_list in test_data:
            if method_name == "While loop (indexed)" and len(test_list) > 1000:
                # Skip while loop for large data due to performance
                method_time = float('inf')
            else:
                method_time, _ = time_traversal(method_func, test_list, 
                                              iterations=100 if len(test_list) > 1000 else 1000)
            times.append(method_time)
        
        time_str = [f"{t:9.4f}" if t != float('inf') else "    N/A  " for t in times]
        print(f"   {method_name:<24} │ {time_str[0]} ms │ {time_str[1]} ms │ {time_str[2]} ms │ {notes}")
    
    # Memory analysis
    print(f"\n💾 Memory Usage Analysis:")
    
    def analyze_memory_patterns():
        """Analyze memory usage of different traversal patterns"""
        test_list = list(range(1000))
        
        # Different traversal results
        basic_copy = [x for x in test_list]
        transformed = [x*2 for x in test_list]
        enumerated = [(i, x) for i, x in enumerate(test_list)]
        generator_obj = (x*2 for x in test_list)  # Generator object
        
        return {
            'original': sys.getsizeof(test_list),
            'basic_copy': sys.getsizeof(basic_copy),
            'transformed': sys.getsizeof(transformed),
            'enumerated': sys.getsizeof(enumerated),
            'generator': sys.getsizeof(generator_obj)
        }
    
    memory_data = analyze_memory_patterns()
    
    print("   Pattern Type          │ Memory Usage │ Efficiency")
    print("   ──────────────────────┼──────────────┼─────────────────────")
    print(f"   Original list (1000)  │ {memory_data['original']:10,} B │ Baseline")
    print(f"   Basic copy            │ {memory_data['basic_copy']:10,} B │ Same as original")
    print(f"   Transformed list      │ {memory_data['transformed']:10,} B │ Same size, new data")
    print(f"   Enumerated tuples     │ {memory_data['enumerated']:10,} B │ Higher (tuples + indices)")
    print(f"   Generator object      │ {memory_data['generator']:10,} B │ Very efficient (lazy)")
    
    # Best practices
    print(f"\n💡 Traversal Performance Best Practices:")
    best_practices = [
        "Use basic for loops for simple iteration - they're highly optimized",
        "List comprehensions are faster than manual loops for transformations",
        "Generators save memory for large datasets you iterate once",
        "enumerate() has minimal overhead compared to manual indexing",
        "Avoid while loops with manual indexing for list traversal",
        "map() is efficient for simple transformations on large datasets",
        "Consider itertools for complex iteration patterns",
        "Profile your specific use case to choose optimal method"
    ]
    
    for i, practice in enumerate(best_practices, 1):
        print(f"   {i}. {practice}")
    
    return {
        'performance_methods': methods,
        'memory_analysis': memory_data,
        'best_practices': best_practices
    }

def practical_applications():
    """
    Practical applications of list traversal in real-world scenarios
    """
    print("\n🌍 PRACTICAL APPLICATIONS")
    print("=" * 27)
    
    print("🚀 Real-World Traversal Scenarios:")
    
    # 1. DATA VALIDATION AND CLEANING
    print(f"\n1️⃣ Data Validation and Cleaning:")
    
    # Sample messy data
    raw_data = [
        "  john@email.com  ",
        "JANE@EMAIL.COM",
        "invalid-email",
        "",
        "bob@domain.com",
        None,
        "alice@test.co.uk",
        "  ",
        "charlie@example.org"
    ]
    
    def clean_and_validate_emails(data: List[Any]) -> dict:
        """Clean and validate email list"""
        results = {
            'valid_emails': [],
            'invalid_entries': [],
            'cleaned_count': 0,
            'removed_count': 0
        }
        
        for i, entry in enumerate(data):
            # Skip None and empty entries
            if entry is None or (isinstance(entry, str) and not entry.strip()):
                results['invalid_entries'].append((i, entry, 'Empty or None'))
                results['removed_count'] += 1
                continue
            
            # Clean whitespace and normalize case
            cleaned = entry.strip().lower()
            
            # Simple email validation
            if '@' in cleaned and '.' in cleaned.split('@')[-1]:
                results['valid_emails'].append(cleaned)
                results['cleaned_count'] += 1
            else:
                results['invalid_entries'].append((i, entry, 'Invalid format'))
                results['removed_count'] += 1
        
        return results
    
    validation_result = clean_and_validate_emails(raw_data)
    
    print(f"   Raw data: {len(raw_data)} entries")
    print(f"   Valid emails: {validation_result['valid_emails']}")
    print(f"   Invalid entries: {validation_result['removed_count']}")
    print(f"   Cleaning efficiency: {validation_result['cleaned_count']/len(raw_data)*100:.1f}%")
    
    # 2. STATISTICAL ANALYSIS
    print(f"\n2️⃣ Statistical Analysis with Traversal:")
    
    # Sample sales data
    monthly_sales = [12500, 13200, 11800, 14100, 15300, 13900, 16200, 14700, 13500, 15800, 17200, 16400]
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    def analyze_sales_data(sales: List[float], months: List[str]) -> dict:
        """Comprehensive sales data analysis"""
        results = {
            'total_sales': sum(sales),
            'average_monthly': sum(sales) / len(sales),
            'best_month': None,
            'worst_month': None,
            'growth_trend': [],
            'quarterly_totals': [],
            'above_average_months': []
        }
        
        # Find best and worst months
        max_sales = max(sales)
        min_sales = min(sales)
        
        for i, (month, sale) in enumerate(zip(months, sales)):
            if sale == max_sales:
                results['best_month'] = (month, sale)
            if sale == min_sales:
                results['worst_month'] = (month, sale)
            
            # Track above-average months
            if sale > results['average_monthly']:
                results['above_average_months'].append((month, sale))
        
        # Calculate growth trend (month-over-month)
        for i in range(1, len(sales)):
            growth = ((sales[i] - sales[i-1]) / sales[i-1]) * 100
            results['growth_trend'].append((months[i], growth))
        
        # Quarterly totals
        for q in range(0, len(sales), 3):
            quarter_sales = sales[q:q+3]
            results['quarterly_totals'].append(sum(quarter_sales))
        
        return results
    
    sales_analysis = analyze_sales_data(monthly_sales, month_names)
    
    print(f"   Total annual sales: ${sales_analysis['total_sales']:,}")
    print(f"   Average monthly: ${sales_analysis['average_monthly']:,.0f}")
    print(f"   Best month: {sales_analysis['best_month'][0]} (${sales_analysis['best_month'][1]:,})")
    print(f"   Worst month: {sales_analysis['worst_month'][0]} (${sales_analysis['worst_month'][1]:,})")
    print(f"   Above average months: {len(sales_analysis['above_average_months'])}")
    
    # 3. TEXT PROCESSING AND ANALYSIS
    print(f"\n3️⃣ Text Processing and Analysis:")
    
    # Sample text data
    documents = [
        "Python is a powerful programming language for data science",
        "Machine learning algorithms require large datasets for training",
        "Data visualization helps in understanding complex patterns",
        "Programming skills are essential for software development",
        "Python libraries make data analysis more efficient"
    ]
    
    def analyze_documents(docs: List[str]) -> dict:
        """Analyze text documents for patterns"""
        results = {
            'word_frequency': {},
            'document_lengths': [],
            'common_words': [],
            'longest_words': [],
            'python_mentions': 0
        }
        
        all_words = []
        
        # Process each document
        for doc in docs:
            words = doc.lower().replace(',', '').split()
            results['document_lengths'].append(len(words))
            all_words.extend(words)
            
            # Count Python mentions
            if 'python' in doc.lower():
                results['python_mentions'] += 1
        
        # Calculate word frequency
        for word in all_words:
            results['word_frequency'][word] = results['word_frequency'].get(word, 0) + 1
        
        # Find common words (appearing more than once)
        results['common_words'] = [(word, count) for word, count in results['word_frequency'].items() 
                                  if count > 1]
        results['common_words'].sort(key=lambda x: x[1], reverse=True)
        
        # Find longest words
        results['longest_words'] = sorted(set(all_words), key=len, reverse=True)[:5]
        
        return results
    
    doc_analysis = analyze_documents(documents)
    
    print(f"   Documents analyzed: {len(documents)}")
    print(f"   Total unique words: {len(doc_analysis['word_frequency'])}")
    print(f"   Common words: {doc_analysis['common_words'][:5]}")  # Top 5
    print(f"   Longest words: {doc_analysis['longest_words']}")
    print(f"   Documents mentioning 'Python': {doc_analysis['python_mentions']}")
    
    # 4. LOG FILE PROCESSING
    print(f"\n4️⃣ Log File Processing:")
    
    # Sample log entries
    log_entries = [
        "2024-01-15 10:30:22 INFO User login: alice@example.com",
        "2024-01-15 10:31:15 DEBUG Database query executed successfully",
        "2024-01-15 10:32:01 INFO Processing order #12345",
        "2024-01-15 10:32:45 ERROR Payment gateway timeout",
        "2024-01-15 10:33:10 WARN Retry payment attempt",
        "2024-01-15 10:33:30 INFO Payment processed successfully",
        "2024-01-15 10:34:00 INFO Order completed: #12345",
        "2024-01-15 10:35:15 ERROR Database connection lost",
        "2024-01-15 10:36:00 INFO System recovery initiated"
    ]
    
    def process_log_entries(logs: List[str]) -> dict:
        """Process and analyze log entries"""
        results = {
            'log_levels': {'INFO': 0, 'DEBUG': 0, 'WARN': 0, 'ERROR': 0},
            'error_entries': [],
            'user_activities': [],
            'system_events': [],
            'time_range': {'first': None, 'last': None}
        }
        
        for i, log in enumerate(logs):
            parts = log.split(' ', 3)  # Split into date, time, level, message
            if len(parts) >= 4:
                date, time, level, message = parts
                datetime_str = f"{date} {time}"
                
                # Track time range
                if results['time_range']['first'] is None:
                    results['time_range']['first'] = datetime_str
                results['time_range']['last'] = datetime_str
                
                # Count log levels
                if level in results['log_levels']:
                    results['log_levels'][level] += 1
                
                # Categorize entries
                if level == 'ERROR':
                    results['error_entries'].append((i, datetime_str, message))
                
                if 'User' in message or 'login' in message.lower():
                    results['user_activities'].append((i, datetime_str, message))
                
                if 'System' in message or 'Database' in message:
                    results['system_events'].append((i, datetime_str, message))
        
        return results
    
    log_analysis = process_log_entries(log_entries)
    
    print(f"   Log entries processed: {len(log_entries)}")
    print(f"   Log level distribution: {log_analysis['log_levels']}")
    print(f"   Error entries: {len(log_analysis['error_entries'])}")
    print(f"   User activities: {len(log_analysis['user_activities'])}")
    print(f"   Time range: {log_analysis['time_range']['first']} to {log_analysis['time_range']['last']}")
    
    return {
        'data_validation': {
            'total_processed': len(raw_data),
            'valid_count': validation_result['cleaned_count'],
            'invalid_count': validation_result['removed_count']
        },
        'sales_analysis': {
            'total_sales': sales_analysis['total_sales'],
            'best_month': sales_analysis['best_month'],
            'above_average_count': len(sales_analysis['above_average_months'])
        },
        'text_analysis': {
            'document_count': len(documents),
            'unique_words': len(doc_analysis['word_frequency']),
            'python_mentions': doc_analysis['python_mentions']
        },
        'log_processing': {
            'total_logs': len(log_entries),
            'error_count': len(log_analysis['error_entries']),
            'log_levels': log_analysis['log_levels']
        }
    }

# =============================================================================
# MAIN EXECUTION AND COMPREHENSIVE DEMONSTRATION
# =============================================================================

def main():
    """
    Main function executing comprehensive list traversal guide
    """
    print(__doc__)
    
    # Core sections
    fundamentals = list_traversal_fundamentals()
    basic_access = basic_access_methods()
    iteration_patterns_demo = iteration_patterns()
    advanced_techniques = advanced_traversal_techniques()
    performance = performance_analysis()
    applications = practical_applications()
    
    return {
        'fundamentals': fundamentals,
        'basic_access': basic_access,
        'iteration_patterns': iteration_patterns_demo,
        'advanced_techniques': advanced_techniques,
        'performance_analysis': performance,
        'practical_applications': applications
    }

if __name__ == "__main__":
    """
    Execute comprehensive list traversal and access guide
    """
    results = main()
    
    print("\n" + "=" * 80)
    print("🎓 LIST TRAVERSAL & ITERATION MASTERY SUMMARY")
    print("=" * 80)
    print("✅ Complete understanding of basic and advanced list access methods")
    print("✅ Mastery of various iteration patterns and traversal techniques")
    print("✅ Advanced techniques including sliding windows and batch processing")
    print("✅ Performance analysis and optimization strategies")
    print("✅ Nested structure traversal and multi-dimensional access")
    print("✅ Real-world applications in data processing, validation, and analysis")
    print("✅ Best practices for efficient traversal operations")
    
    print("\n💡 List Traversal Mastery Key Points:")
    key_points = [
        "Basic for loops are highly optimized and should be preferred for simple iteration",
        "enumerate() provides both index and value access with minimal overhead",
        "List comprehensions offer superior performance for transformations",
        "Generators save memory for large datasets with one-time iteration",
        "zip() enables elegant parallel traversal of multiple lists",
        "Advanced patterns like sliding windows solve complex processing problems",
        "State-maintaining traversal enables sophisticated data analysis",
        "Understanding performance characteristics helps choose optimal methods"
    ]
    
    for point in key_points:
        print(f"   • {point}")
    
    print("\n🎯 Expert-Level Applications:")
    applications = [
        "Data validation and cleaning pipelines for ETL processes",
        "Statistical analysis and business intelligence reporting",
        "Text processing and natural language analysis systems",
        "Log file monitoring and anomaly detection systems",
        "Time series analysis and trend identification algorithms",
        "Machine learning data preprocessing and feature extraction",
        "Web scraping and content analysis applications",
        "Scientific computing and numerical data processing"
    ]
    
    for i, application in enumerate(applications, 1):
        print(f"   {i}. {application}")
    
    print(f"\n🚀 Master List Traversal for Efficient Data Processing!")
    print("Effective traversal patterns are the foundation of data manipulation!")

# =============================================================================
# ORIGINAL SIMPLE EXAMPLES (Enhanced with Context)
# =============================================================================

# Simple demonstrations of basic list access and traversal
print("\n" + "=" * 60)
print("BASIC EXAMPLES FROM ORIGINAL CODE")
print("=" * 60)

# Example of accessing elements in a list
example_list = [10, 20, 30, 40, 50]
first_element = example_list[0]  # Accessing the first element
second_element = example_list[1]  # Accessing the second element
third_element = example_list[2]  # Accessing the third element

print("List Access Examples:")
print(f"Example list: {example_list}")
print(f"First Element: {first_element}")
print(f"Second Element: {second_element}")
print(f"Third Element: {third_element}")

# Example of traversing a list using a for loop
lst = [1, 2, 3, 4, 5]  # Example of a simple list
print(f"\nList Traversal Example:")
print(f"List to traverse: {lst}")
print("Traversal with transformation (each element + 100):")
for e in lst:
    print(f"Element: {e + 100}")  # Printing each element in the list

print("\nThese basic patterns form the foundation for all advanced traversal techniques!")