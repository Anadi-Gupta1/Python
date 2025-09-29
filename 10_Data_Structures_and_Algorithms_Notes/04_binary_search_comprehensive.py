"""
Binary Search Algorithm - Complete Implementation and Analysis Guide
==================================================================

Comprehensive guide to binary search algorithm in Python: implementation, analysis,
variations, and practical applications. Covers iterative and recursive approaches,
complexity analysis, and real-world problem solving.

Author: Python Learning Notes
Date: September 2025
Topic: Binary Search, Algorithm Analysis, Search Algorithms
"""

import time
import random
import matplotlib.pyplot as plt
from typing import List, Optional, Tuple, Any
import math

# =============================================================================
# BINARY SEARCH FUNDAMENTALS
# =============================================================================

def binary_search_fundamentals():
    """
    Complete introduction to binary search algorithm and its principles
    """
    print("🔍 BINARY SEARCH ALGORITHM FUNDAMENTALS")
    print("=" * 41)
    
    print("🎯 What is Binary Search?")
    print("   Binary search is an efficient algorithm for finding a target value")
    print("   in a sorted array by repeatedly dividing the search space in half.")
    print("   It follows the divide-and-conquer paradigm.")
    
    print(f"\n📊 Binary Search Characteristics:")
    characteristics = [
        ("Prerequisite", "Array must be sorted", "🔄 Sorting required"),
        ("Time Complexity", "O(log n)", "⚡ Very efficient"),
        ("Space Complexity", "O(1) iterative, O(log n) recursive", "📦 Memory efficient"),
        ("Approach", "Divide and conquer", "🔪 Split search space"),
        ("Comparison", "Faster than linear search", "🏃 Logarithmic growth"),
        ("Applications", "Database indexing, autocomplete", "🌐 Wide usage")
    ]
    
    print("   Property          │ Description                     │ Advantage")
    print("   ──────────────────┼─────────────────────────────────┼──────────────────")
    
    for prop, desc, advantage in characteristics:
        print(f"   {prop:<17} │ {desc:<31} │ {advantage}")
    
    # Algorithm visualization
    print(f"\n🎨 Binary Search Process Visualization:")
    print("   Example: Searching for target = 7 in [1, 3, 5, 7, 9, 11, 13]")
    print("   ")
    print("   Step 1: [1, 3, 5, |7|, 9, 11, 13]  mid=7, target=7 → Found!")
    print("           ↑         ↑              ↑")
    print("         left      mid           right")
    print("   ")
    print("   Example: Searching for target = 3 in [1, 3, 5, 7, 9, 11, 13]")
    print("   ")
    print("   Step 1: [1, 3, 5, |7|, 9, 11, 13]  mid=7, target=3 → go left")
    print("           ↑         ↑              ↑")
    print("         left      mid           right")
    print("   ")
    print("   Step 2: [1, |3|, 5]                mid=3, target=3 → Found!")
    print("           ↑  ↑     ↑")
    print("         left mid right")
    
    return {
        'characteristics': characteristics
    }

# =============================================================================
# BINARY SEARCH IMPLEMENTATIONS
# =============================================================================

def binary_search_iterative(arr: List[int], target: int) -> Tuple[int, int]:
    """
    Iterative binary search implementation
    
    Args:
        arr: Sorted list of integers
        target: Value to search for
    
    Returns:
        Tuple of (index, comparisons) where index is -1 if not found
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    comparisons = 0
    
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, comparisons

def binary_search_recursive(arr: List[int], target: int, left: int = 0, right: int = None) -> Tuple[int, int]:
    """
    Recursive binary search implementation
    
    Args:
        arr: Sorted list of integers
        target: Value to search for
        left: Left boundary index
        right: Right boundary index
    
    Returns:
        Tuple of (index, comparisons)
    
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion stack
    """
    if right is None:
        right = len(arr) - 1
    
    # Base case: element not found
    if left > right:
        return -1, 1
    
    mid = (left + right) // 2
    
    # Element found
    if arr[mid] == target:
        return mid, 1
    
    # Recursive calls
    if arr[mid] < target:
        result, comp = binary_search_recursive(arr, target, mid + 1, right)
        return result, comp + 1
    else:
        result, comp = binary_search_recursive(arr, target, left, mid - 1)
        return result, comp + 1

def binary_search_leftmost(arr: List[int], target: int) -> int:
    """
    Find the leftmost (first) occurrence of target in sorted array
    
    Args:
        arr: Sorted list that may contain duplicates
        target: Value to search for
    
    Returns:
        Index of leftmost occurrence, or -1 if not found
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def binary_search_rightmost(arr: List[int], target: int) -> int:
    """
    Find the rightmost (last) occurrence of target in sorted array
    
    Args:
        arr: Sorted list that may contain duplicates
        target: Value to search for
    
    Returns:
        Index of rightmost occurrence, or -1 if not found
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def binary_search_range(arr: List[int], target: int) -> Tuple[int, int]:
    """
    Find the range [start, end] of target values in sorted array
    
    Args:
        arr: Sorted list that may contain duplicates
        target: Value to search for
    
    Returns:
        Tuple of (start_index, end_index), or (-1, -1) if not found
    """
    start = binary_search_leftmost(arr, target)
    if start == -1:
        return (-1, -1)
    
    end = binary_search_rightmost(arr, target)
    return (start, end)

# =============================================================================
# BINARY SEARCH VARIATIONS AND APPLICATIONS
# =============================================================================

def search_insert_position(arr: List[int], target: int) -> int:
    """
    Find the position where target should be inserted to maintain sorted order
    
    Args:
        arr: Sorted list of integers
        target: Value to insert
    
    Returns:
        Index where target should be inserted
    
    LeetCode Problem: Search Insert Position
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left

def find_peak_element(arr: List[int]) -> int:
    """
    Find a peak element in array (element greater than its neighbors)
    
    Args:
        arr: List of integers
    
    Returns:
        Index of a peak element
    
    Note: Array boundaries are considered as negative infinity
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return left

def search_rotated_array(arr: List[int], target: int) -> int:
    """
    Search in rotated sorted array
    
    Args:
        arr: Rotated sorted array (e.g., [4,5,6,7,0,1,2])
        target: Value to search for
    
    Returns:
        Index of target, or -1 if not found
    
    LeetCode Problem: Search in Rotated Sorted Array
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        # Check which part is sorted
        if arr[left] <= arr[mid]:  # Left part is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right part is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

def find_sqrt(n: int) -> int:
    """
    Find integer square root using binary search
    
    Args:
        n: Non-negative integer
    
    Returns:
        Floor of square root of n
    """
    if n < 2:
        return n
    
    left, right = 1, n // 2
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == n:
            return mid
        elif square < n:
            left = mid + 1
        else:
            right = mid - 1
    
    return right  # Floor of square root

# =============================================================================
# PERFORMANCE ANALYSIS AND COMPARISON
# =============================================================================

def linear_search(arr: List[int], target: int) -> Tuple[int, int]:
    """
    Linear search for comparison with binary search
    
    Returns:
        Tuple of (index, comparisons)
    """
    comparisons = 0
    for i, val in enumerate(arr):
        comparisons += 1
        if val == target:
            return i, comparisons
    return -1, comparisons

def performance_comparison():
    """
    Compare binary search vs linear search performance
    """
    print("\n⚡ PERFORMANCE COMPARISON")
    print("=" * 26)
    
    # Test different array sizes
    sizes = [100, 1000, 10000, 100000]
    
    print(f"📊 Binary Search vs Linear Search Performance:")
    print("   Array Size │ Binary Comparisons │ Linear Comparisons │ Speed Up")
    print("   ───────────┼────────────────────┼────────────────────┼─────────")
    
    for size in sizes:
        # Create sorted array
        arr = list(range(1, size + 1))
        target = size  # Worst case for linear search
        
        # Binary search
        _, binary_comps = binary_search_iterative(arr, target)
        
        # Linear search
        _, linear_comps = linear_search(arr, target)
        
        # Calculate speedup
        speedup = linear_comps / binary_comps if binary_comps > 0 else 0
        
        print(f"   {size:<10} │ {binary_comps:<18} │ {linear_comps:<18} │ {speedup:.1f}x")
    
    return {
        'test_sizes': sizes
    }

def complexity_visualization():
    """
    Visualize the complexity difference between O(log n) and O(n)
    """
    print(f"\n📈 Complexity Growth Analysis:")
    
    sizes = [2**i for i in range(1, 21)]  # Powers of 2 from 2 to 1M
    
    print("   Input Size │ log₂(n) │  n     │ Efficiency Ratio")
    print("   ───────────┼─────────┼────────┼────────────────")
    
    for n in [16, 256, 4096, 65536, 1048576]:
        log_n = math.log2(n)
        ratio = n / log_n
        
        print(f"   {n:<10} │ {log_n:<7.0f} │ {n:<6} │ {ratio:.0f}x")
    
    print(f"\n💡 Key Insight:")
    print("   As input size grows, binary search becomes exponentially")
    print("   more efficient compared to linear search!")

# =============================================================================
# PRACTICAL DEMONSTRATIONS
# =============================================================================

def practical_demonstrations():
    """
    Demonstrate various binary search applications
    """
    print("\n🚀 PRACTICAL BINARY SEARCH DEMONSTRATIONS")
    print("=" * 43)
    
    # Demo 1: Basic binary search
    print("1️⃣  Basic Binary Search:")
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    
    index_iter, comps_iter = binary_search_iterative(arr, target)
    index_rec, comps_rec = binary_search_recursive(arr, target)
    
    print(f"     Array: {arr}")
    print(f"     Target: {target}")
    print(f"     Iterative: Found at index {index_iter} with {comps_iter} comparisons")
    print(f"     Recursive: Found at index {index_rec} with {comps_rec} comparisons")
    
    # Demo 2: Finding range of duplicates
    print(f"\n2️⃣  Finding Range in Array with Duplicates:")
    arr_dup = [1, 2, 3, 3, 3, 3, 4, 5, 6]
    target_dup = 3
    
    start, end = binary_search_range(arr_dup, target_dup)
    print(f"     Array: {arr_dup}")
    print(f"     Target: {target_dup}")
    print(f"     Range: [{start}, {end}] (indices {start} to {end})")
    
    # Demo 3: Search insert position
    print(f"\n3️⃣  Search Insert Position:")
    arr_insert = [1, 3, 5, 6]
    targets_insert = [5, 2, 7, 0]
    
    for target in targets_insert:
        pos = search_insert_position(arr_insert, target)
        print(f"     Insert {target} at position {pos} in {arr_insert}")
    
    # Demo 4: Peak element
    print(f"\n4️⃣  Find Peak Element:")
    arr_peak = [1, 2, 3, 1]
    peak_idx = find_peak_element(arr_peak)
    print(f"     Array: {arr_peak}")
    print(f"     Peak element {arr_peak[peak_idx]} found at index {peak_idx}")
    
    # Demo 5: Rotated array search
    print(f"\n5️⃣  Search in Rotated Sorted Array:")
    arr_rotated = [4, 5, 6, 7, 0, 1, 2]
    target_rot = 0
    
    index_rot = search_rotated_array(arr_rotated, target_rot)
    print(f"     Array: {arr_rotated}")
    print(f"     Target: {target_rot}")
    print(f"     Found at index: {index_rot}")
    
    # Demo 6: Integer square root
    print(f"\n6️⃣  Integer Square Root:")
    numbers = [4, 8, 15, 25, 100]
    
    for num in numbers:
        sqrt_result = find_sqrt(num)
        print(f"     √{num} = {sqrt_result} (exact: {math.sqrt(num):.2f})")
    
    return {
        'basic_search': (index_iter, comps_iter),
        'range_search': (start, end),
        'peak_index': peak_idx,
        'rotated_search': index_rot
    }

# =============================================================================
# MAIN EXECUTION AND COMPREHENSIVE DEMONSTRATION
# =============================================================================

def main():
    """
    Main function executing comprehensive binary search guide
    """
    print(__doc__)
    
    # Fundamentals
    fundamentals = binary_search_fundamentals()
    
    # Performance comparison
    performance = performance_comparison()
    complexity_visualization()
    
    # Practical demonstrations
    demos = practical_demonstrations()
    
    return {
        'fundamentals': fundamentals,
        'performance': performance,
        'demonstrations': demos
    }

if __name__ == "__main__":
    """
    Execute comprehensive binary search algorithm guide
    """
    results = main()
    
    print("\n" + "=" * 70)
    print("🎓 BINARY SEARCH ALGORITHM MASTERY SUMMARY")
    print("=" * 70)
    print("✅ Complete binary search fundamentals and principles")
    print("✅ Iterative and recursive implementations")
    print("✅ Advanced variations: leftmost, rightmost, range search")
    print("✅ Practical applications: insert position, peak finding")
    print("✅ Complex scenarios: rotated arrays, square root")
    print("✅ Performance analysis and complexity comparison")
    print("✅ Real-world problem solving demonstrations")
    
    print("\n💡 Binary Search Mastery Key Points:")
    key_points = [
        "Binary search requires sorted input - O(log n) time complexity",
        "Divide and conquer approach halves search space each iteration",
        "Iterative implementation uses O(1) space, recursive uses O(log n)",
        "Variations handle duplicates, insertion points, and rotated arrays",
        "Essential for efficient searching in large datasets",
        "Foundation for many advanced algorithms and data structures",
        "Performance advantage grows exponentially with input size",
        "Understanding binary search improves algorithmic thinking"
    ]
    
    for point in key_points:
        print(f"   • {point}")
    
    print("\n🎯 Advanced Binary Search Topics to Explore:")
    advanced_topics = [
        "Binary search on answer (optimization problems)",
        "2D matrix binary search techniques",
        "Binary indexed trees and segment trees",
        "Ternary search for unimodal functions",
        "Exponential search for unbounded arrays",
        "Interpolation search for uniformly distributed data",
        "Fractional cascading for multiple searches",
        "Binary search in database indexing systems"
    ]
    
    for i, topic in enumerate(advanced_topics, 1):
        print(f"   {i}. {topic}")
    
    print(f"\n🚀 Master Binary Search - The Gateway to Efficient Algorithms!")
    print("Understanding binary search opens doors to advanced algorithmic techniques!")