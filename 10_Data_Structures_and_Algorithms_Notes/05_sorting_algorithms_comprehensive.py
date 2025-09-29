"""
Sorting Algorithms Collection - Complete Implementation and Analysis Guide
========================================================================

Comprehensive guide to fundamental sorting algorithms in Python: implementation, 
analysis, comparison, and practical applications. Covers bubble sort, selection sort,
insertion sort, merge sort, quick sort, and heap sort with performance analysis.

Author: Python Learning Notes
Date: September 2025
Topic: Sorting Algorithms, Algorithm Analysis, Performance Comparison
"""

import time
import random
import sys
import matplotlib.pyplot as plt
from typing import List, Callable, Tuple, Dict, Any
import copy

# =============================================================================
# SORTING ALGORITHMS FUNDAMENTALS
# =============================================================================

def sorting_fundamentals():
    """
    Complete introduction to sorting algorithms and their importance
    """
    print("🔄 SORTING ALGORITHMS FUNDAMENTALS")
    print("=" * 36)
    
    print("🎯 What is Sorting?")
    print("   Sorting is the process of arranging elements in a specific order")
    print("   (typically ascending or descending). It's one of the most fundamental")
    print("   operations in computer science and forms the basis for many algorithms.")
    
    print(f"\n📊 Why Sorting is Important:")
    importance = [
        ("Search Efficiency", "Sorted data enables binary search O(log n)", "🔍 Fast searching"),
        ("Data Organization", "Makes data easier to understand and process", "📊 Better insights"),
        ("Algorithm Foundation", "Required for many advanced algorithms", "🏗️ Building blocks"),
        ("Database Operations", "Essential for indexing and queries", "💾 Data management"),
        ("User Experience", "Organized information is more usable", "👤 Better UX"),
        ("Duplicate Detection", "Easier to find duplicates in sorted data", "🔄 Data cleaning")
    ]
    
    print("   Aspect             │ Description                     │ Benefit")
    print("   ───────────────────┼─────────────────────────────────┼──────────────────")
    
    for aspect, desc, benefit in importance:
        print(f"   {aspect:<18} │ {desc:<31} │ {benefit}")
    
    print(f"\n⚡ Algorithm Complexity Overview:")
    algorithms = [
        ("Bubble Sort", "O(n²)", "O(n²)", "O(1)", "Simple but inefficient"),
        ("Selection Sort", "O(n²)", "O(n²)", "O(1)", "Minimal swaps"),
        ("Insertion Sort", "O(n)", "O(n²)", "O(1)", "Good for small/sorted data"),
        ("Merge Sort", "O(n log n)", "O(n log n)", "O(n)", "Stable, guaranteed performance"),
        ("Quick Sort", "O(n log n)", "O(n²)", "O(log n)", "Fast average case"),
        ("Heap Sort", "O(n log n)", "O(n log n)", "O(1)", "Guaranteed O(n log n)")
    ]
    
    print("   Algorithm      │ Best Case    │ Worst Case   │ Space    │ Notes")
    print("   ───────────────┼──────────────┼──────────────┼──────────┼─────────────────────")
    
    for name, best, worst, space, notes in algorithms:
        print(f"   {name:<14} │ {best:<12} │ {worst:<12} │ {space:<8} │ {notes}")
    
    return {
        'importance_factors': importance,
        'algorithm_complexities': algorithms
    }

# =============================================================================
# SIMPLE SORTING ALGORITHMS O(n²)
# =============================================================================

def bubble_sort(arr: List[int], verbose: bool = False) -> Tuple[List[int], Dict[str, int]]:
    """
    Bubble Sort: Repeatedly steps through list, compares adjacent elements
    and swaps them if they're in wrong order.
    
    Time Complexity: O(n²) average and worst case, O(n) best case
    Space Complexity: O(1)
    Stable: Yes
    
    Args:
        arr: List to sort
        verbose: Print step-by-step process
    
    Returns:
        Sorted list and statistics
    """
    arr = arr.copy()  # Don't modify original
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    if verbose:
        print(f"🫧 Bubble Sort Process:")
        print(f"   Initial array: {arr}")
    
    # Perform n-1 passes
    for i in range(n):
        swapped = False
        
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            comparisons += 1
            
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they're in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        
        if verbose:
            print(f"   Pass {i + 1}: {arr} ({'swapped' if swapped else 'no swaps'})")
        
        # If no swaps occurred, array is sorted
        if not swapped:
            break
    
    stats = {
        'comparisons': comparisons,
        'swaps': swaps,
        'passes': i + 1
    }
    
    return arr, stats

def selection_sort(arr: List[int], verbose: bool = False) -> Tuple[List[int], Dict[str, int]]:
    """
    Selection Sort: Finds minimum element and places it at beginning,
    then finds second minimum and places it at second position, etc.
    
    Time Complexity: O(n²) for all cases
    Space Complexity: O(1)
    Stable: No (can be made stable)
    
    Args:
        arr: List to sort
        verbose: Print step-by-step process
    
    Returns:
        Sorted list and statistics
    """
    arr = arr.copy()
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    if verbose:
        print(f"🎯 Selection Sort Process:")
        print(f"   Initial array: {arr}")
    
    # Find minimum element in remaining unsorted array
    for i in range(n):
        min_idx = i
        
        # Find minimum element in arr[i+1..n-1]
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap found minimum with first element
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
        
        if verbose:
            sorted_part = arr[:i+1]
            unsorted_part = arr[i+1:]
            print(f"   Step {i + 1}: {sorted_part} | {unsorted_part} (min: {arr[i]})")
    
    stats = {
        'comparisons': comparisons,
        'swaps': swaps,
        'passes': n
    }
    
    return arr, stats

def insertion_sort(arr: List[int], verbose: bool = False) -> Tuple[List[int], Dict[str, int]]:
    """
    Insertion Sort: Builds final sorted array one element at a time.
    Takes element from unsorted part and finds correct position in sorted part.
    
    Time Complexity: O(n) best case, O(n²) average and worst case
    Space Complexity: O(1)
    Stable: Yes
    
    Args:
        arr: List to sort
        verbose: Print step-by-step process
    
    Returns:
        Sorted list and statistics
    """
    arr = arr.copy()
    n = len(arr)
    comparisons = 0
    shifts = 0
    
    if verbose:
        print(f"📝 Insertion Sort Process:")
        print(f"   Initial array: {arr}")
        print(f"   Step 0: [{arr[0]}] | {arr[1:]} (sorted | unsorted)")
    
    # Start from second element (first is considered sorted)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
            shifts += 1
        
        if j >= 0:  # Made at least one comparison
            comparisons += 1
        
        # Place key in correct position
        arr[j + 1] = key
        
        if verbose:
            sorted_part = arr[:i+1]
            unsorted_part = arr[i+1:] if i+1 < n else []
            print(f"   Step {i}: {sorted_part} | {unsorted_part} (inserted: {key})")
    
    stats = {
        'comparisons': comparisons,
        'shifts': shifts,
        'passes': n - 1
    }
    
    return arr, stats

# =============================================================================
# EFFICIENT SORTING ALGORITHMS O(n log n)
# =============================================================================

def merge_sort(arr: List[int], verbose: bool = False, depth: int = 0) -> Tuple[List[int], Dict[str, int]]:
    """
    Merge Sort: Divide-and-conquer algorithm that divides array into halves,
    sorts them recursively, then merges sorted halves.
    
    Time Complexity: O(n log n) for all cases
    Space Complexity: O(n)
    Stable: Yes
    
    Args:
        arr: List to sort
        verbose: Print step-by-step process
        depth: Recursion depth for formatting
    
    Returns:
        Sorted list and statistics
    """
    # Initialize statistics on first call
    if depth == 0:
        merge_sort.comparisons = 0
        merge_sort.merges = 0
    
    if len(arr) <= 1:
        return arr, {'comparisons': merge_sort.comparisons, 'merges': merge_sort.merges}
    
    # Divide
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    if verbose:
        indent = "  " * depth
        print(f"{indent}🔪 Divide: {arr} → {left} | {right}")
    
    # Conquer (recursive calls)
    left_sorted, _ = merge_sort(left, verbose, depth + 1)
    right_sorted, _ = merge_sort(right, verbose, depth + 1)
    
    # Merge
    merged = merge(left_sorted, right_sorted, verbose, depth)
    merge_sort.merges += 1
    
    stats = {
        'comparisons': merge_sort.comparisons,
        'merges': merge_sort.merges
    }
    
    return merged, stats

def merge(left: List[int], right: List[int], verbose: bool = False, depth: int = 0) -> List[int]:
    """
    Merge two sorted arrays into one sorted array
    """
    result = []
    i = j = 0
    
    # Compare elements from both arrays
    while i < len(left) and j < len(right):
        merge_sort.comparisons += 1
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    if verbose:
        indent = "  " * depth
        print(f"{indent}🔗 Merge: {left} + {right} → {result}")
    
    return result

def quick_sort(arr: List[int], verbose: bool = False, depth: int = 0, 
               start: int = None, end: int = None) -> Tuple[List[int], Dict[str, int]]:
    """
    Quick Sort: Divide-and-conquer algorithm that picks pivot element,
    partitions array around pivot, then recursively sorts sub-arrays.
    
    Time Complexity: O(n log n) average, O(n²) worst case
    Space Complexity: O(log n) average
    Stable: No
    
    Args:
        arr: List to sort
        verbose: Print step-by-step process
        depth: Recursion depth for formatting
        start, end: Array bounds for in-place sorting
    
    Returns:
        Sorted list and statistics
    """
    # Initialize on first call
    if start is None:
        arr = arr.copy()
        start = 0
        end = len(arr) - 1
        quick_sort.comparisons = 0
        quick_sort.swaps = 0
        quick_sort.partitions = 0
    
    if start < end:
        # Partition array and get pivot index
        pivot_idx = partition(arr, start, end, verbose, depth)
        quick_sort.partitions += 1
        
        # Recursively sort elements before and after partition
        quick_sort(arr, verbose, depth + 1, start, pivot_idx - 1)
        quick_sort(arr, verbose, depth + 1, pivot_idx + 1, end)
    
    stats = {
        'comparisons': quick_sort.comparisons,
        'swaps': quick_sort.swaps,
        'partitions': quick_sort.partitions
    }
    
    return arr, stats

def partition(arr: List[int], start: int, end: int, verbose: bool = False, depth: int = 0) -> int:
    """
    Partition function for quick sort using last element as pivot
    """
    pivot = arr[end]
    i = start - 1  # Index of smaller element
    
    if verbose:
        indent = "  " * depth
        print(f"{indent}🎯 Partition {arr[start:end+1]} (pivot: {pivot})")
    
    for j in range(start, end):
        quick_sort.comparisons += 1
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            if arr[i] != arr[j]:  # Only count actual swaps
                quick_sort.swaps += 1
    
    # Place pivot in correct position
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    quick_sort.swaps += 1
    
    if verbose:
        indent = "  " * depth
        smaller = arr[start:i+1] if i >= start else []
        larger = arr[i+2:end+1] if i+2 <= end else []
        print(f"{indent}   Result: {smaller} [{pivot}] {larger}")
    
    return i + 1

# =============================================================================
# PERFORMANCE ANALYSIS AND COMPARISON
# =============================================================================

def performance_comparison():
    """
    Compare performance of different sorting algorithms
    """
    print("\n⚡ SORTING ALGORITHMS PERFORMANCE COMPARISON")
    print("=" * 47)
    
    # Test with different data sizes
    sizes = [10, 50, 100, 500, 1000]
    algorithms = {
        'Bubble Sort': bubble_sort,
        'Selection Sort': selection_sort,
        'Insertion Sort': insertion_sort,
        'Merge Sort': merge_sort,
        'Quick Sort': quick_sort
    }
    
    print(f"📊 Performance Test Results:")
    print("   Size    │ Bubble   │ Selection │ Insertion │ Merge     │ Quick")
    print("   ────────┼──────────┼───────────┼───────────┼───────────┼──────────")
    
    results = {}
    
    for size in sizes:
        # Generate random data
        data = [random.randint(1, 1000) for _ in range(size)]
        row_results = {}
        
        for name, algorithm in algorithms.items():
            # Measure execution time
            start_time = time.perf_counter()
            try:
                _, stats = algorithm(data)
                end_time = time.perf_counter()
                execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
                row_results[name] = execution_time
            except Exception as e:
                row_results[name] = float('inf')  # Algorithm failed
        
        results[size] = row_results
        
        # Display results for this size
        print(f"   {size:<7} │", end="")
        for name in algorithms.keys():
            time_ms = row_results[name]
            if time_ms == float('inf'):
                print(f" {'ERROR':<8} │", end="")
            else:
                print(f" {time_ms:<8.2f} │", end="")
        print()
    
    return results

def algorithm_demonstrations():
    """
    Demonstrate each sorting algorithm with step-by-step output
    """
    print(f"\n🎯 SORTING ALGORITHMS DEMONSTRATIONS")
    print("=" * 38)
    
    # Sample data for demonstrations
    demo_data = [64, 34, 25, 12, 22, 11, 90]
    
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort)
    ]
    
    for name, algorithm in algorithms:
        print(f"\n{'='*50}")
        print(f"🔄 {name.upper()} DEMONSTRATION")
        print(f"{'='*50}")
        print(f"Original array: {demo_data}")
        
        try:
            sorted_arr, stats = algorithm(demo_data, verbose=True)
            print(f"✅ Final sorted array: {sorted_arr}")
            print(f"📊 Statistics: {stats}")
            
            # Verify sorting
            is_sorted = all(sorted_arr[i] <= sorted_arr[i+1] for i in range(len(sorted_arr)-1))
            print(f"🔍 Verification: {'✅ Correctly sorted' if is_sorted else '❌ Sort failed'}")
            
        except Exception as e:
            print(f"❌ Algorithm failed: {e}")

def best_worst_case_analysis():
    """
    Analyze best and worst case scenarios for sorting algorithms
    """
    print(f"\n📈 BEST & WORST CASE ANALYSIS")
    print("=" * 31)
    
    # Test data scenarios
    size = 20
    test_data = {
        'Random': [random.randint(1, 100) for _ in range(size)],
        'Sorted': list(range(1, size + 1)),
        'Reverse Sorted': list(range(size, 0, -1)),
        'Nearly Sorted': list(range(1, size + 1)),
        'All Same': [42] * size
    }
    
    # Make nearly sorted data
    test_data['Nearly Sorted'][5], test_data['Nearly Sorted'][15] = test_data['Nearly Sorted'][15], test_data['Nearly Sorted'][5]
    
    algorithms = {
        'Bubble': bubble_sort,
        'Selection': selection_sort,
        'Insertion': insertion_sort
    }
    
    print("   Scenario      │ Bubble   │ Selection │ Insertion")
    print("   ──────────────┼──────────┼───────────┼──────────")
    
    for scenario, data in test_data.items():
        print(f"   {scenario:<13} │", end="")
        
        for name, algorithm in algorithms.items():
            start_time = time.perf_counter()
            _, stats = algorithm(data)
            end_time = time.perf_counter()
            execution_time = (end_time - start_time) * 1000
            
            print(f" {execution_time:<8.2f} │", end="")
        print()

# =============================================================================
# MAIN EXECUTION AND COMPREHENSIVE DEMONSTRATION
# =============================================================================

def main():
    """
    Main function executing comprehensive sorting algorithms guide
    """
    print(__doc__)
    
    # Fundamentals
    fundamentals = sorting_fundamentals()
    
    # Demonstrations
    algorithm_demonstrations()
    
    # Performance comparison
    performance_results = performance_comparison()
    
    # Best/worst case analysis
    best_worst_case_analysis()
    
    return {
        'fundamentals': fundamentals,
        'performance_results': performance_results
    }

if __name__ == "__main__":
    """
    Execute comprehensive sorting algorithms guide
    """
    results = main()
    
    print("\n" + "=" * 70)
    print("🎓 SORTING ALGORITHMS MASTERY SUMMARY")
    print("=" * 70)
    print("✅ Complete understanding of fundamental sorting algorithms")
    print("✅ Implementation of O(n²) algorithms: Bubble, Selection, Insertion")
    print("✅ Implementation of O(n log n) algorithms: Merge, Quick Sort")
    print("✅ Performance analysis and complexity comparison")
    print("✅ Best/worst case scenario analysis")
    print("✅ Step-by-step algorithm demonstrations")
    print("✅ Statistical analysis of algorithm behavior")
    
    print("\n💡 Sorting Algorithms Mastery Key Points:")
    key_points = [
        "Choose sorting algorithm based on data characteristics and requirements",
        "O(n²) algorithms are simple but inefficient for large datasets",
        "O(n log n) algorithms provide better scalability and performance",
        "Stable vs unstable sorting matters for complex data structures",
        "Space complexity trade-offs between in-place and auxiliary space",
        "Best/worst case analysis helps predict algorithm performance",
        "Insertion sort is efficient for small or nearly sorted arrays",
        "Merge sort guarantees O(n log n) performance in all cases"
    ]
    
    for point in key_points:
        print(f"   • {point}")
    
    print("\n🎯 Advanced Sorting Topics to Explore:")
    advanced_topics = [
        "Radix sort and counting sort for integer arrays",
        "Bucket sort for uniformly distributed data",
        "Tim sort (Python's built-in sorting algorithm)",
        "External sorting for data larger than memory",
        "Parallel sorting algorithms for multi-core systems",
        "Hybrid sorting algorithms combining multiple approaches",
        "Sorting stability and its applications",
        "Lower bound analysis for comparison-based sorting"
    ]
    
    for i, topic in enumerate(advanced_topics, 1):
        print(f"   {i}. {topic}")
    
    print(f"\n🚀 Master Sorting Algorithms - Foundation for Efficient Data Processing!")
    print("Understanding sorting unlocks advanced algorithms and data structures!")