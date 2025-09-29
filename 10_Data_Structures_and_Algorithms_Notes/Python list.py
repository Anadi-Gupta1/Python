"""
Python Lists and Data Structures - Complete DSA Foundation Guide
==============================================================

Comprehensive guide to Python lists as dynamic arrays and fundamental data structures
for algorithm implementation. Covers creation, operations, complexity analysis, and
practical applications in data structures and algorithms.

Author: Python Learning Notes
Date: September 2025
Topic: Lists, Arrays, Data Structures, Algorithm Foundations
"""

import time
import random
import sys
from typing import List, Any, Optional, Tuple
import matplotlib.pyplot as plt
from collections import deque
import heapq

# =============================================================================
# PYTHON LISTS FUNDAMENTALS
# =============================================================================

def list_fundamentals_comprehensive():
    """
    Complete introduction to Python lists as dynamic arrays
    """
    print("📋 PYTHON LISTS FUNDAMENTALS COMPREHENSIVE")
    print("=" * 44)
    
    print("🎯 What are Python Lists?")
    print("   Python lists are dynamic arrays - ordered, mutable collections")
    print("   that can store elements of any type. They are the foundation")
    print("   for implementing many data structures and algorithms.")
    
    print(f"\n📊 List Characteristics:")
    characteristics = [
        ("Ordered", "Elements maintain their insertion order", "✅ Indexed access"),
        ("Mutable", "Can be modified after creation", "✅ Add/remove/change"),
        ("Dynamic", "Size can grow or shrink at runtime", "✅ Flexible capacity"),
        ("Heterogeneous", "Can store different data types", "✅ Mixed elements"),
        ("Iterable", "Can be traversed with loops", "✅ for/while loops"),
        ("Indexable", "Access elements by position", "✅ list[index]")
    ]
    
    print("   Property      │ Description                    │ Benefit")
    print("   ──────────────┼────────────────────────────────┼─────────────────")
    
    for prop, desc, benefit in characteristics:
        print(f"   {prop:<13} │ {desc:<30} │ {benefit}")
    
    # List Creation Methods
    print(f"\n🔧 List Creation Methods:")
    
    # Method 1: Literal syntax
    empty_list = []
    numbers = [1, 2, 3, 4, 5]
    mixed_types = [1, "hello", 3.14, True, [1, 2, 3]]
    
    print(f"   1. Literal syntax:")
    print(f"      empty_list = []                    → {empty_list}")
    print(f"      numbers = [1, 2, 3, 4, 5]         → {numbers}")
    print(f"      mixed = [1, 'hello', 3.14, True]  → {mixed_types[:4]}")
    
    # Method 2: list() constructor
    from_string = list("hello")
    from_range = list(range(1, 6))
    from_tuple = list((1, 2, 3, 4, 5))
    
    print(f"\n   2. list() constructor:")
    print(f"      list('hello')     → {from_string}")
    print(f"      list(range(1, 6)) → {from_range}")
    print(f"      list((1,2,3,4,5)) → {from_tuple}")
    
    # Method 3: List comprehensions
    squares = [x**2 for x in range(1, 6)]
    evens = [x for x in range(1, 11) if x % 2 == 0]
    matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
    
    print(f"\n   3. List comprehensions:")
    print(f"      [x**2 for x in range(1, 6)]       → {squares}")
    print(f"      [x for x in range(1, 11) if x%2==0] → {evens}")
    print(f"      [[i*j for j in range(1,4)] for i in range(1,4)] → {matrix}")
    
    # Method 4: Repetition and multiplication
    zeros = [0] * 5
    pattern = [1, 2] * 3
    
    print(f"\n   4. Repetition:")
    print(f"      [0] * 5   → {zeros}")
    print(f"      [1, 2] * 3 → {pattern}")
    
    return {
        'examples': {
            'empty': empty_list,
            'numbers': numbers,
            'mixed': mixed_types,
            'squares': squares,
            'matrix': matrix
        }
    }

def list_operations_comprehensive():
    """
    Comprehensive coverage of list operations and methods
    """
    print("\n🔧 LIST OPERATIONS COMPREHENSIVE")
    print("=" * 33)
    
    # Initialize sample list
    sample_list = [10, 20, 30, 40, 50]
    original = sample_list.copy()
    
    print(f"📊 Core List Operations:")
    print(f"   Starting list: {original}")
    
    # Access operations
    print(f"\n   1. Access Operations:")
    print(f"      list[0]     → {sample_list[0]} (first element)")
    print(f"      list[-1]    → {sample_list[-1]} (last element)")
    print(f"      list[1:4]   → {sample_list[1:4]} (slice)")
    print(f"      len(list)   → {len(sample_list)} (length)")
    
    # Modification operations
    print(f"\n   2. Modification Operations:")
    
    # Append (add to end)
    sample_list.append(60)
    print(f"      append(60)       → {sample_list}")
    
    # Insert (add at position)
    sample_list.insert(2, 25)
    print(f"      insert(2, 25)    → {sample_list}")
    
    # Extend (add multiple elements)
    sample_list.extend([70, 80])
    print(f"      extend([70, 80]) → {sample_list}")
    
    # Remove operations
    sample_list.remove(25)  # Remove first occurrence
    print(f"      remove(25)       → {sample_list}")
    
    popped = sample_list.pop(3)  # Remove and return element at index
    print(f"      pop(3)           → {sample_list} (removed {popped})")
    
    # Sorting and reversing
    unsorted = [30, 10, 50, 20, 40]
    unsorted.sort()
    print(f"      sort()           → {unsorted}")
    
    unsorted.reverse()
    print(f"      reverse()        → {unsorted}")
    
    # List Methods Summary
    print(f"\n📋 Complete List Methods:")
    methods_info = [
        ("append(x)", "Add x to end", "O(1)", "Amortized constant"),
        ("insert(i, x)", "Insert x at position i", "O(n)", "Linear shift required"),
        ("remove(x)", "Remove first x", "O(n)", "Search + shift required"),
        ("pop(i)", "Remove and return item at i", "O(n)", "Shift required"),
        ("index(x)", "Find index of first x", "O(n)", "Linear search"),
        ("count(x)", "Count occurrences of x", "O(n)", "Full scan required"),
        ("sort()", "Sort list in-place", "O(n log n)", "Timsort algorithm"),
        ("reverse()", "Reverse list in-place", "O(n)", "Swap elements"),
        ("clear()", "Remove all elements", "O(n)", "Deallocate memory"),
        ("copy()", "Shallow copy of list", "O(n)", "Copy references")
    ]
    
    print("   Method         │ Description           │ Time      │ Notes")
    print("   ───────────────┼───────────────────────┼───────────┼────────────────────")
    
    for method, desc, time_comp, notes in methods_info:
        print(f"   {method:<14} │ {desc:<21} │ {time_comp:<9} │ {notes}")
    
    return {
        'final_list': sample_list,
        'operations_performed': ['append', 'insert', 'extend', 'remove', 'pop', 'sort', 'reverse']
    }

# =============================================================================
# ALGORITHM IMPLEMENTATION AND COMPLEXITY ANALYSIS
# =============================================================================

def algorithm_implementation_guide():
    """
    Comprehensive guide to implementing algorithms with lists
    """
    print("\n⚙️ ALGORITHM IMPLEMENTATION GUIDE")
    print("=" * 34)
    
    print("🎯 Common Algorithm Patterns with Lists:")
    
    # Pattern 1: Linear Search
    def linear_search(arr: List[int], target: int) -> int:
        """
        Find the index of target in array, return -1 if not found
        Time Complexity: O(n), Space Complexity: O(1)
        """
        comparisons = 0
        for i in range(len(arr)):
            comparisons += 1
            if arr[i] == target:
                return i, comparisons
        return -1, comparisons
    
    # Pattern 2: Binary Search (requires sorted array)
    def binary_search(arr: List[int], target: int) -> Tuple[int, int]:
        """
        Find target in sorted array using binary search
        Time Complexity: O(log n), Space Complexity: O(1)
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
    
    # Pattern 3: Finding minimum/maximum
    def find_min_max(arr: List[int]) -> Tuple[Tuple[int, int], Tuple[int, int], int]:
        """
        Find minimum and maximum values with their indices
        Time Complexity: O(n), Space Complexity: O(1)
        """
        if not arr:
            return None, None, 0
            
        min_val, min_idx = arr[0], 0
        max_val, max_idx = arr[0], 0
        comparisons = 0
        
        for i in range(1, len(arr)):
            comparisons += 2  # Two comparisons per iteration
            if arr[i] < min_val:
                min_val, min_idx = arr[i], i
            if arr[i] > max_val:
                max_val, max_idx = arr[i], i
                
        return (min_val, min_idx), (max_val, max_idx), comparisons
    
    # Demonstration with sample data
    sample_data = [64, 25, 12, 22, 11, 90, 88, 76, 50, 42]
    sorted_data = sorted(sample_data)
    
    print(f"\n📊 Algorithm Demonstrations:")
    print(f"   Sample data: {sample_data}")
    print(f"   Sorted data: {sorted_data}")
    
    # Linear search demonstration
    target = 22
    index, linear_comps = linear_search(sample_data, target)
    print(f"\n   Linear Search for {target}:")
    print(f"     Found at index: {index}")
    print(f"     Comparisons: {linear_comps}")
    
    # Binary search demonstration
    index, binary_comps = binary_search(sorted_data, target)
    print(f"\n   Binary Search for {target}:")
    print(f"     Found at index: {index}")
    print(f"     Comparisons: {binary_comps}")
    print(f"     Efficiency gain: {linear_comps/binary_comps:.1f}x faster")
    
    # Min/max finding
    min_result, max_result, minmax_comps = find_min_max(sample_data)
    print(f"\n   Min/Max Finding:")
    print(f"     Minimum: {min_result[0]} at index {min_result[1]}")
    print(f"     Maximum: {max_result[0]} at index {max_result[1]}")
    print(f"     Comparisons: {minmax_comps}")
    
    return {
        'sample_data': sample_data,
        'search_results': {
            'linear': (index, linear_comps),
            'binary': (index, binary_comps)
        },
        'minmax': (min_result, max_result, minmax_comps)
    }

def time_complexity_analysis():
    """
    Comprehensive time complexity analysis and benchmarking
    """
    print("\n⏱️ TIME COMPLEXITY ANALYSIS")
    print("=" * 28)
    
    print("📊 Big O Notation Overview:")
    
    complexity_classes = [
        ("O(1)", "Constant", "Array access, append", "Excellent"),
        ("O(log n)", "Logarithmic", "Binary search", "Very Good"),
        ("O(n)", "Linear", "Linear search, traversal", "Good"),
        ("O(n log n)", "Linearithmic", "Efficient sorting", "Acceptable"),
        ("O(n²)", "Quadratic", "Bubble sort, nested loops", "Poor"),
        ("O(2^n)", "Exponential", "Recursive fibonacci", "Very Poor"),
        ("O(n!)", "Factorial", "Traveling salesman brute force", "Terrible")
    ]
    
    print("   Notation   │ Name          │ Example Operations        │ Performance")
    print("   ───────────┼───────────────┼───────────────────────────┼────────────")
    
    for notation, name, example, performance in complexity_classes:
        print(f"   {notation:<10} │ {name:<13} │ {example:<25} │ {performance}")
    
    # Practical benchmarking
    print(f"\n🔬 Practical Performance Benchmarking:")
    
    def benchmark_operation(operation_func, data_sizes, operation_name):
        """Benchmark an operation across different data sizes"""
        results = []
        
        for size in data_sizes:
            # Create test data
            test_data = list(range(size))
            random.shuffle(test_data)
            
            # Measure execution time
            start_time = time.time()
            operation_func(test_data)
            end_time = time.time()
            
            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
            results.append(execution_time)
        
        return results
    
    # Define operations to benchmark
    def linear_search_benchmark(data):
        target = data[-1]  # Search for last element (worst case)
        for item in data:
            if item == target:
                return True
        return False
    
    def list_sort_benchmark(data):
        data_copy = data.copy()
        data_copy.sort()
        return data_copy
    
    def list_reverse_benchmark(data):
        data_copy = data.copy()
        data_copy.reverse()
        return data_copy
    
    # Run benchmarks
    data_sizes = [100, 500, 1000, 2000, 5000]
    
    print(f"   Benchmarking operations on different data sizes:")
    print("   Size     │ Linear Search │ List Sort    │ List Reverse")
    print("   ─────────┼───────────────┼──────────────┼─────────────")
    
    for size in data_sizes:
        # Create test data
        test_data = list(range(size))
        random.shuffle(test_data)
        
        # Benchmark linear search
        start = time.perf_counter()
        linear_search_benchmark(test_data)
        linear_time = (time.perf_counter() - start) * 1000
        
        # Benchmark sorting
        start = time.perf_counter()
        list_sort_benchmark(test_data)
        sort_time = (time.perf_counter() - start) * 1000
        
        # Benchmark reverse
        start = time.perf_counter()
        list_reverse_benchmark(test_data)
        reverse_time = (time.perf_counter() - start) * 1000
        
        print(f"   {size:<8} │ {linear_time:11.3f} ms │ {sort_time:10.3f} ms │ {reverse_time:9.3f} ms")
    
    # Growth analysis
    print(f"\n📈 Complexity Growth Analysis:")
    print(f"   As data size increases from 100 to 5000 (50x increase):")
    
    # Calculate growth ratios for largest vs smallest dataset
    test_100 = list(range(100))
    test_5000 = list(range(5000))
    random.shuffle(test_100)
    random.shuffle(test_5000)
    
    # Time operations
    start = time.perf_counter()
    linear_search_benchmark(test_100)
    linear_100 = time.perf_counter() - start
    
    start = time.perf_counter()
    linear_search_benchmark(test_5000)
    linear_5000 = time.perf_counter() - start
    
    linear_growth = linear_5000 / linear_100 if linear_100 > 0 else 0
    
    print(f"     Linear search: ~{linear_growth:.1f}x slower (expected ~50x for O(n))")
    print(f"     List sort: Expected ~{50 * np.log2(50)/np.log2(1):.1f}x slower for O(n log n)")
    print(f"     List reverse: Expected ~50x slower for O(n)")
    
    return {
        'data_sizes': data_sizes,
        'complexity_classes': complexity_classes,
        'benchmark_results': 'completed'
    }

# =============================================================================
# PRACTICAL DSA APPLICATIONS
# =============================================================================

def practical_dsa_applications():
    """
    Practical applications of data structures and algorithms
    """
    print("\n🚀 PRACTICAL DSA APPLICATIONS")
    print("=" * 31)
    
    print("🎯 Real-World Algorithm Applications:")
    
    # Application 1: Frequency Counter
    def frequency_counter(text: str) -> dict:
        """Count character frequencies in text - O(n) time"""
        frequencies = {}
        for char in text:
            frequencies[char] = frequencies.get(char, 0) + 1
        return frequencies
    
    # Application 2: Two Sum Problem
    def two_sum(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
        """Find two numbers that sum to target - O(n) time with hash map"""
        seen = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in seen:
                return (seen[complement], i)
            seen[num] = i
        return None
    
    # Application 3: Palindrome Checker
    def is_palindrome(s: str) -> bool:
        """Check if string is palindrome - O(n) time"""
        s = s.lower().replace(' ', '')
        return s == s[::-1]
    
    # Application 4: Anagram Detector
    def are_anagrams(str1: str, str2: str) -> bool:
        """Check if two strings are anagrams - O(n log n) time"""
        return sorted(str1.lower()) == sorted(str2.lower())
    
    # Application 5: Moving Average
    class MovingAverage:
        """Sliding window moving average calculator"""
        def __init__(self, window_size: int):
            self.window_size = window_size
            self.window = deque()
            self.sum = 0
        
        def next(self, val: float) -> float:
            if len(self.window) >= self.window_size:
                old_val = self.window.popleft()
                self.sum -= old_val
            
            self.window.append(val)
            self.sum += val
            return self.sum / len(self.window)
    
    print(f"\n📊 Algorithm Demonstrations:")
    
    # Demonstrate frequency counter
    sample_text = "hello world"
    frequencies = frequency_counter(sample_text)
    print(f"   Frequency Counter:")
    print(f"     Text: '{sample_text}'")
    print(f"     Frequencies: {frequencies}")
    
    # Demonstrate two sum
    numbers = [2, 7, 11, 15, 3, 8]
    target = 9
    result = two_sum(numbers, target)
    print(f"\n   Two Sum Problem:")
    print(f"     Numbers: {numbers}")
    print(f"     Target: {target}")
    print(f"     Indices: {result} (values: {numbers[result[0]]}, {numbers[result[1]]})")
    
    # Demonstrate palindrome
    test_strings = ["racecar", "hello", "A man a plan a canal Panama"]
    print(f"\n   Palindrome Checker:")
    for s in test_strings:
        result = is_palindrome(s)
        print(f"     '{s}' → {result}")
    
    # Demonstrate anagrams
    anagram_pairs = [("listen", "silent"), ("hello", "world"), ("evil", "vile")]
    print(f"\n   Anagram Detector:")
    for str1, str2 in anagram_pairs:
        result = are_anagrams(str1, str2)
        print(f"     '{str1}' & '{str2}' → {result}")
    
    # Demonstrate moving average
    print(f"\n   Moving Average (window=3):")
    ma = MovingAverage(3)
    values = [1, 10, 3, 5, 7, 6, 8]
    print(f"     Values: {values}")
    print(f"     Averages: ", end="")
    averages = []
    for val in values:
        avg = ma.next(val)
        averages.append(round(avg, 2))
    print(averages)
    
    return {
        'frequency_result': frequencies,
        'two_sum_result': result,
        'palindrome_results': [(s, is_palindrome(s)) for s in test_strings],
        'anagram_results': [(pair, are_anagrams(pair[0], pair[1])) for pair in anagram_pairs],
        'moving_averages': averages
    }

# =============================================================================
# MAIN EXECUTION AND COMPREHENSIVE DEMONSTRATION
# =============================================================================

def main():
    """
    Main function executing comprehensive Python lists and DSA guide
    """
    print(__doc__)
    
    # Fundamentals
    list_basics = list_fundamentals_comprehensive()
    list_ops = list_operations_comprehensive()
    
    # Algorithm implementation
    algorithm_results = algorithm_implementation_guide()
    complexity_analysis = time_complexity_analysis()
    
    # Practical applications
    practical_results = practical_dsa_applications()
    
    return {
        'list_fundamentals': list_basics,
        'list_operations': list_ops,
        'algorithms': algorithm_results,
        'complexity': complexity_analysis,
        'practical_applications': practical_results
    }

if __name__ == "__main__":
    """
    Execute comprehensive Python lists and DSA foundation guide
    """
    results = main()
    
    print("\n" + "=" * 60)
    print("🎓 PYTHON LISTS AND DSA FOUNDATION SUMMARY")
    print("=" * 60)
    print("✅ Comprehensive Python lists fundamentals and characteristics")
    print("✅ Complete list operations and methods with complexity analysis")
    print("✅ Algorithm implementation patterns and best practices")
    print("✅ Time complexity analysis and Big O notation mastery")
    print("✅ Practical benchmarking and performance measurement")
    print("✅ Real-world DSA applications and problem-solving patterns")
    print("✅ Search algorithms (linear and binary search)")
    print("✅ Sorting and optimization techniques")
    print("✅ Data structure foundations for advanced algorithms")
    
    print("\n💡 Python Lists and DSA Mastery Key Points:")
    key_points = [
        "Lists are dynamic arrays - the foundation of Python DSA",
        "Understand time complexity to choose optimal algorithms",
        "Master common patterns: search, sort, frequency counting",
        "Use appropriate data structures for specific problems",
        "Benchmark and profile code for performance optimization",
        "Apply algorithmic thinking to real-world problems",
        "Combine multiple algorithms for complex solutions",
        "Consider space-time tradeoffs in algorithm design"
    ]
    
    for point in key_points:
        print(f"   • {point}")
    
    print("\n🎯 Next Steps in DSA Learning:")
    next_steps = [
        "Advanced data structures (trees, graphs, hash tables)",
        "Sorting algorithms (quicksort, mergesort, heapsort)",
        "Dynamic programming and memoization techniques",
        "Graph algorithms (BFS, DFS, shortest path)",
        "Advanced string algorithms and pattern matching",
        "Competitive programming and algorithmic contests",
        "System design and scalable algorithm implementation",
        "Mathematical algorithms and number theory applications"
    ]
    
    for i, step in enumerate(next_steps, 1):
        print(f"   {i}. {step}")
    
    print(f"\n🚀 Ready for Advanced Data Structures and Algorithms!")
    print("Master the art of efficient problem-solving with Python!")