"""
Python List Functions and Methods - Complete Implementation Guide
================================================================

Comprehensive guide to Python list functions and methods covering built-in
functions, list methods, advanced operations, and practical applications.
Master all list manipulation techniques for effective data processing.

Author: Python Learning Notes
Date: September 2025
Topic: List Functions, Methods, Built-in Operations, Data Manipulation
"""

import sys
import time
import copy
from typing import List, Any, Optional, Callable, Union
from functools import reduce
from itertools import chain, accumulate

# =============================================================================
# BUILT-IN FUNCTIONS FOR LISTS
# =============================================================================

def builtin_functions_comprehensive():
    """
    Comprehensive guide to built-in functions that work with lists
    """
    print("🔧 BUILT-IN FUNCTIONS FOR LISTS")
    print("=" * 33)
    
    print("🎯 Essential Built-in Functions:")
    print("   Python provides many built-in functions that work efficiently")
    print("   with lists for common operations like length, sum, sorting, etc.")
    
    # Sample data for demonstrations
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    strings = ["apple", "banana", "cherry", "date"]
    mixed_data = [1, "hello", 3.14, True, [1, 2, 3]]
    empty_list = []
    
    print(f"\n📊 Sample Data:")
    print(f"   numbers = {numbers}")
    print(f"   strings = {strings}")
    print(f"   mixed_data = {mixed_data}")
    print(f"   empty_list = {empty_list}")
    
    # Demonstrate built-in functions
    builtin_functions = [
        ("len()", "Get length/size of list", "len(numbers)", len(numbers)),
        ("sum()", "Sum of numeric elements", "sum(numbers)", sum(numbers)),
        ("max()", "Maximum element", "max(numbers)", max(numbers)),
        ("min()", "Minimum element", "min(numbers)", min(numbers)),
        ("sorted()", "Return sorted copy", "sorted(numbers)", sorted(numbers)),
        ("reversed()", "Return reverse iterator", "list(reversed(numbers))", list(reversed(numbers))),
        ("enumerate()", "Add indices to elements", "list(enumerate(strings))", list(enumerate(strings))),
        ("zip()", "Combine multiple lists", "list(zip(numbers[:3], strings[:3]))", list(zip(numbers[:3], strings[:3]))),
        ("all()", "Check if all elements are True", "all([True, True, False])", all([True, True, False])),
        ("any()", "Check if any element is True", "any([True, False, False])", any([True, False, False]))
    ]
    
    print(f"\n🔨 Built-in Functions Demonstration:")
    print("   Function      │ Purpose                    │ Example                      │ Result")
    print("   ──────────────┼────────────────────────────┼──────────────────────────────┼─────────────────")
    
    for func_name, purpose, example, result in builtin_functions:
        result_str = str(result)[:25] + ("..." if len(str(result)) > 25 else "")
        print(f"   {func_name:<13} │ {purpose:<26} │ {example:<28} │ {result_str}")
    
    # Advanced built-in functions
    print(f"\n🚀 Advanced Built-in Functions:")
    
    # map() function
    squared = list(map(lambda x: x**2, numbers[:5]))
    print(f"   map() - Apply function to all elements:")
    print(f"     map(lambda x: x**2, {numbers[:5]}) → {squared}")
    
    # filter() function
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"   filter() - Filter elements based on condition:")
    print(f"     filter(lambda x: x%2==0, numbers) → {evens}")
    
    # reduce() function
    product = reduce(lambda x, y: x * y, numbers[:4], 1)
    print(f"   reduce() - Reduce list to single value:")
    print(f"     reduce(lambda x,y: x*y, {numbers[:4]}) → {product}")
    
    return {
        'builtin_functions': builtin_functions,
        'advanced_examples': {
            'map_result': squared,
            'filter_result': evens,
            'reduce_result': product
        }
    }

def list_methods_comprehensive():
    """
    Complete guide to all Python list methods
    """
    print("\n📋 PYTHON LIST METHODS COMPREHENSIVE")
    print("=" * 37)
    
    print("🎯 List Methods Categories:")
    print("   Modification: append, extend, insert, remove, pop, clear")
    print("   Information: index, count")
    print("   Reordering: sort, reverse")
    print("   Copying: copy")
    
    # Demonstrate each method with examples
    
    # 1. MODIFICATION METHODS
    print(f"\n🔧 Modification Methods:")
    
    # append() - Add single element to end
    demo_list = [1, 2, 3]
    print(f"   Original list: {demo_list}")
    demo_list.append(4)
    print(f"   After append(4): {demo_list}")
    
    # extend() - Add multiple elements to end
    demo_list.extend([5, 6, 7])
    print(f"   After extend([5, 6, 7]): {demo_list}")
    
    # insert() - Add element at specific position
    demo_list.insert(0, 0)
    print(f"   After insert(0, 0): {demo_list}")
    
    # remove() - Remove first occurrence of value
    demo_list.remove(3)
    print(f"   After remove(3): {demo_list}")
    
    # pop() - Remove and return element at index (default: last)
    popped = demo_list.pop()
    print(f"   After pop(): {demo_list} (popped: {popped})")
    
    popped_index = demo_list.pop(1)
    print(f"   After pop(1): {demo_list} (popped: {popped_index})")
    
    # clear() - Remove all elements
    clear_demo = demo_list.copy()
    clear_demo.clear()
    print(f"   After clear(): {clear_demo}")
    
    # 2. INFORMATION METHODS
    print(f"\n📊 Information Methods:")
    
    info_list = [1, 2, 3, 2, 4, 2, 5]
    print(f"   Sample list: {info_list}")
    
    # index() - Find index of first occurrence
    try:
        index_pos = info_list.index(2)
        print(f"   index(2): {index_pos}")
        
        # index() with start and end parameters
        index_pos_range = info_list.index(2, 2, 6)  # Search from index 2 to 6
        print(f"   index(2, 2, 6): {index_pos_range}")
    except ValueError as e:
        print(f"   index() error: {e}")
    
    # count() - Count occurrences of value
    count_2 = info_list.count(2)
    print(f"   count(2): {count_2}")
    
    # 3. REORDERING METHODS
    print(f"\n🔄 Reordering Methods:")
    
    sort_demo = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"   Original list: {sort_demo}")
    
    # sort() - Sort list in place
    sort_demo_copy = sort_demo.copy()
    sort_demo_copy.sort()
    print(f"   After sort(): {sort_demo_copy}")
    
    # sort() with reverse parameter
    sort_demo_copy.sort(reverse=True)
    print(f"   After sort(reverse=True): {sort_demo_copy}")
    
    # sort() with key function
    string_list = ["apple", "pie", "banana", "a"]
    string_copy = string_list.copy()
    string_copy.sort(key=len)
    print(f"   Strings by length: {string_list} → {string_copy}")
    
    # reverse() - Reverse list in place
    reverse_demo = [1, 2, 3, 4, 5]
    print(f"   Before reverse(): {reverse_demo}")
    reverse_demo.reverse()
    print(f"   After reverse(): {reverse_demo}")
    
    # 4. COPYING METHOD
    print(f"\n📄 Copying Method:")
    
    original = [1, [2, 3], 4]
    
    # Shallow copy
    shallow_copy = original.copy()
    print(f"   Original: {original}")
    print(f"   Shallow copy: {shallow_copy}")
    print(f"   Are they the same object? {original is shallow_copy}")
    print(f"   Do nested objects share references? {original[1] is shallow_copy[1]}")
    
    return {
        'modification_methods': ['append', 'extend', 'insert', 'remove', 'pop', 'clear'],
        'information_methods': ['index', 'count'],
        'reordering_methods': ['sort', 'reverse'],
        'copying_methods': ['copy'],
        'demonstration_results': {
            'final_demo_list': demo_list,
            'count_result': count_2,
            'sorted_strings': string_copy
        }
    }

def advanced_list_operations():
    """
    Advanced list operations and techniques
    """
    print("\n🚀 ADVANCED LIST OPERATIONS")
    print("=" * 29)
    
    print("🎯 List Comprehensions and Advanced Techniques:")
    
    # 1. LIST COMPREHENSIONS
    print(f"\n📝 List Comprehensions:")
    
    numbers = list(range(1, 11))
    print(f"   Base list: {numbers}")
    
    # Basic comprehension
    squares = [x**2 for x in numbers]
    print(f"   Squares: [x**2 for x in numbers] → {squares}")
    
    # With condition
    even_squares = [x**2 for x in numbers if x % 2 == 0]
    print(f"   Even squares: [x**2 for x in numbers if x%2==0] → {even_squares}")
    
    # Nested comprehension
    matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
    print(f"   Matrix: [[i*j for j in range(1,4)] for i in range(1,4)]")
    for row in matrix:
        print(f"     {row}")
    
    # 2. UNPACKING AND PACKING
    print(f"\n📦 Unpacking and Packing:")
    
    data = [1, 2, 3, 4, 5]
    
    # Basic unpacking
    first, *middle, last = data
    print(f"   first, *middle, last = {data}")
    print(f"   first: {first}, middle: {middle}, last: {last}")
    
    # Function with *args
    def sum_all(*args):
        return sum(args)
    
    result = sum_all(*data)
    print(f"   sum_all(*data): {result}")
    
    # 3. LIST MULTIPLICATION AND REPETITION
    print(f"\n🔢 List Multiplication and Repetition:")
    
    base_list = [1, 2, 3]
    multiplied = base_list * 3
    print(f"   {base_list} * 3 = {multiplied}")
    
    # Caution with mutable objects
    nested_caution = [[0] * 3] * 3  # All sublists share the same reference!
    print(f"   Caution - [[0] * 3] * 3: {nested_caution}")
    nested_caution[0][0] = 1
    print(f"   After modifying [0][0]: {nested_caution} (all rows affected!)")
    
    # Correct way
    nested_correct = [[0] * 3 for _ in range(3)]
    print(f"   Correct - [[0]*3 for _ in range(3)]: {nested_correct}")
    nested_correct[0][0] = 1
    print(f"   After modifying [0][0]: {nested_correct} (only first row affected)")
    
    # 4. CHAINING AND FLATTENING
    print(f"\n🔗 Chaining and Flattening:")
    
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = [7, 8, 9]
    
    # Chain multiple lists
    chained = list(chain(list1, list2, list3))
    print(f"   chain({list1}, {list2}, {list3}) → {chained}")
    
    # Flatten nested list
    nested = [[1, 2], [3, 4], [5, 6]]
    flattened = list(chain.from_iterable(nested))
    print(f"   Flatten {nested} → {flattened}")
    
    # Alternative flattening methods
    flattened_comp = [item for sublist in nested for item in sublist]
    print(f"   Using comprehension: {flattened_comp}")
    
    # 5. ACCUMULATION AND REDUCTION
    print(f"\n📈 Accumulation and Reduction:")
    
    values = [1, 2, 3, 4, 5]
    
    # Cumulative sums
    cumsum = list(accumulate(values))
    print(f"   Cumulative sum of {values}: {cumsum}")
    
    # Cumulative products
    cumproduct = list(accumulate(values, lambda x, y: x * y))
    print(f"   Cumulative product of {values}: {cumproduct}")
    
    return {
        'comprehension_examples': {
            'squares': squares,
            'even_squares': even_squares,
            'matrix': matrix
        },
        'unpacking_example': {'first': first, 'middle': middle, 'last': last},
        'chaining_results': {'chained': chained, 'flattened': flattened},
        'accumulation_results': {'cumsum': cumsum, 'cumproduct': cumproduct}
    }

def functional_programming_with_lists():
    """
    Functional programming techniques with lists
    """
    print("\n🧮 FUNCTIONAL PROGRAMMING WITH LISTS")
    print("=" * 37)
    
    print("🎯 Functional Programming Paradigms:")
    print("   Treat functions as first-class citizens")
    print("   Use higher-order functions for list processing")
    print("   Avoid side effects and mutation when possible")
    
    # Sample data
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print(f"\n📊 Sample Data: {numbers}")
    
    # 1. MAP, FILTER, REDUCE PATTERNS
    print(f"\n🔄 Map, Filter, Reduce Patterns:")
    
    # Map - transform each element
    def square(x):
        return x ** 2
    
    def double(x):
        return x * 2
    
    squares_func = list(map(square, numbers))
    doubled_func = list(map(double, numbers))
    
    print(f"   map(square, numbers): {squares_func}")
    print(f"   map(double, numbers): {doubled_func}")
    
    # Filter - select elements based on criteria
    def is_even(x):
        return x % 2 == 0
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    evens_func = list(filter(is_even, numbers))
    primes_func = list(filter(is_prime, numbers))
    
    print(f"   filter(is_even, numbers): {evens_func}")
    print(f"   filter(is_prime, numbers): {primes_func}")
    
    # Reduce - combine elements
    from functools import reduce
    
    def multiply(x, y):
        return x * y
    
    def find_max(x, y):
        return x if x > y else y
    
    product_func = reduce(multiply, numbers[:4])
    max_func = reduce(find_max, numbers)
    
    print(f"   reduce(multiply, {numbers[:4]}): {product_func}")
    print(f"   reduce(find_max, numbers): {max_func}")
    
    # 2. FUNCTION COMPOSITION
    print(f"\n🔗 Function Composition:")
    
    def compose(*functions):
        """Compose multiple functions into one"""
        return lambda x: reduce(lambda acc, f: f(acc), functions, x)
    
    # Compose functions: square then double
    square_then_double = compose(square, double)
    result_composition = square_then_double(5)
    print(f"   compose(square, double)(5): {result_composition}")
    
    # Apply composition to list
    composed_results = list(map(square_then_double, [1, 2, 3, 4]))
    print(f"   Applied to [1,2,3,4]: {composed_results}")
    
    # 3. CURRYING AND PARTIAL APPLICATION
    print(f"\n🍛 Currying and Partial Application:")
    
    def add(x):
        """Curried addition function"""
        return lambda y: x + y
    
    def multiply_by(multiplier):
        """Partial application for multiplication"""
        return lambda x: x * multiplier
    
    add_5 = add(5)
    multiply_by_3 = multiply_by(3)
    
    print(f"   add(5)(10): {add_5(10)}")
    print(f"   multiply_by(3) applied to [1,2,3,4]: {list(map(multiply_by_3, [1,2,3,4]))}")
    
    # 4. RECURSIVE LIST PROCESSING
    print(f"\n🔄 Recursive List Processing:")
    
    def recursive_sum(lst):
        """Calculate sum recursively"""
        if not lst:
            return 0
        return lst[0] + recursive_sum(lst[1:])
    
    def recursive_map(func, lst):
        """Map function recursively"""
        if not lst:
            return []
        return [func(lst[0])] + recursive_map(func, lst[1:])
    
    def recursive_filter(predicate, lst):
        """Filter list recursively"""
        if not lst:
            return []
        if predicate(lst[0]):
            return [lst[0]] + recursive_filter(predicate, lst[1:])
        return recursive_filter(predicate, lst[1:])
    
    rec_sum = recursive_sum([1, 2, 3, 4, 5])
    rec_squares = recursive_map(lambda x: x**2, [1, 2, 3, 4])
    rec_evens = recursive_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
    
    print(f"   recursive_sum([1,2,3,4,5]): {rec_sum}")
    print(f"   recursive_map(square, [1,2,3,4]): {rec_squares}")
    print(f"   recursive_filter(is_even, [1,2,3,4,5,6]): {rec_evens}")
    
    return {
        'map_results': {'squares': squares_func, 'doubled': doubled_func},
        'filter_results': {'evens': evens_func, 'primes': primes_func},
        'reduce_results': {'product': product_func, 'max': max_func},
        'composition_results': {'single': result_composition, 'list': composed_results},
        'recursive_results': {'sum': rec_sum, 'map': rec_squares, 'filter': rec_evens}
    }

def performance_optimization():
    """
    Performance optimization techniques for list operations
    """
    print("\n⚡ PERFORMANCE OPTIMIZATION FOR LISTS")
    print("=" * 38)
    
    print("🎯 Optimization Strategies:")
    print("   Choose appropriate data structures and algorithms")
    print("   Understand time complexities of operations")
    print("   Use built-in functions when possible")
    
    def time_operation(func, *args, iterations=1000):
        """Helper function to time operations"""
        start = time.perf_counter()
        for _ in range(iterations):
            result = func(*args)
        end = time.perf_counter()
        return (end - start) * 1000 / iterations, result
    
    # 1. LIST CREATION OPTIMIZATION
    print(f"\n🏗️ List Creation Optimization:")
    
    n = 1000
    
    # Different ways to create lists
    def create_with_loop():
        result = []
        for i in range(n):
            result.append(i)
        return result
    
    def create_with_comprehension():
        return [i for i in range(n)]
    
    def create_with_constructor():
        return list(range(n))
    
    loop_time, _ = time_operation(create_with_loop, iterations=100)
    comp_time, _ = time_operation(create_with_comprehension, iterations=100)
    constructor_time, _ = time_operation(create_with_constructor, iterations=100)
    
    print(f"   Method              │ Time (ms/op) │ Relative Speed")
    print(f"   ────────────────────┼──────────────┼───────────────")
    print(f"   Loop + append       │ {loop_time:10.4f}   │ {loop_time/constructor_time:.1f}x slower")
    print(f"   List comprehension  │ {comp_time:10.4f}   │ {comp_time/constructor_time:.1f}x")
    print(f"   list(range())       │ {constructor_time:10.4f}   │ 1.0x (fastest)")
    
    # 2. SEARCH OPTIMIZATION
    print(f"\n🔍 Search Optimization:")
    
    large_list = list(range(10000))
    target = 9999  # Worst case for linear search
    
    def linear_search(lst, target):
        for i, item in enumerate(lst):
            if item == target:
                return i
        return -1
    
    def using_index_method(lst, target):
        try:
            return lst.index(target)
        except ValueError:
            return -1
    
    def using_in_operator(lst, target):
        return target in lst
    
    linear_time, _ = time_operation(linear_search, large_list, target, iterations=10)
    index_time, _ = time_operation(using_index_method, large_list, target, iterations=10)
    in_time, _ = time_operation(using_in_operator, large_list, target, iterations=10)
    
    print(f"   Search Method       │ Time (ms/op) │ Use Case")
    print(f"   ────────────────────┼──────────────┼─────────────────────")
    print(f"   Manual linear       │ {linear_time:10.4f}   │ Custom logic needed")
    print(f"   list.index()        │ {index_time:10.4f}   │ Need index position")
    print(f"   'in' operator       │ {in_time:10.4f}   │ Just checking existence")
    
    # 3. MEMORY OPTIMIZATION
    print(f"\n💾 Memory Optimization:")
    
    # Generator vs list for large sequences
    def list_squares(n):
        return [x**2 for x in range(n)]
    
    def generator_squares(n):
        return (x**2 for x in range(n))
    
    n = 1000
    list_result = list_squares(n)
    gen_result = generator_squares(n)
    
    list_memory = sys.getsizeof(list_result)
    gen_memory = sys.getsizeof(gen_result)
    
    print(f"   Data Structure      │ Memory (bytes) │ Memory Ratio")
    print(f"   ────────────────────┼────────────────┼─────────────")
    print(f"   List (1000 items)   │ {list_memory:12,}   │ {list_memory/gen_memory:.1f}x larger")
    print(f"   Generator           │ {gen_memory:12,}   │ 1.0x (base)")
    
    print(f"\n   💡 Use generators for:")
    print(f"      • Large sequences that don't fit in memory")
    print(f"      • One-time iteration over data")
    print(f"      • Pipeline processing with multiple steps")
    
    return {
        'creation_times': {'loop': loop_time, 'comprehension': comp_time, 'constructor': constructor_time},
        'search_times': {'linear': linear_time, 'index': index_time, 'in_operator': in_time},
        'memory_usage': {'list': list_memory, 'generator': gen_memory}
    }

# =============================================================================
# MAIN EXECUTION AND COMPREHENSIVE DEMONSTRATION
# =============================================================================

def main():
    """
    Main function executing comprehensive list functions and methods guide
    """
    print(__doc__)
    
    # Core sections
    builtins = builtin_functions_comprehensive()
    methods = list_methods_comprehensive()
    advanced = advanced_list_operations()
    functional = functional_programming_with_lists()
    optimization = performance_optimization()
    
    return {
        'builtin_functions': builtins,
        'list_methods': methods,
        'advanced_operations': advanced,
        'functional_programming': functional,
        'performance_optimization': optimization
    }

if __name__ == "__main__":
    """
    Execute comprehensive list functions and methods guide
    """
    results = main()
    
    print("\n" + "=" * 80)
    print("🎓 PYTHON LIST FUNCTIONS & METHODS MASTERY SUMMARY")
    print("=" * 80)
    print("✅ Complete mastery of Python built-in functions for lists")
    print("✅ Comprehensive understanding of all list methods and their uses")
    print("✅ Advanced list operations including comprehensions and unpacking")
    print("✅ Functional programming techniques with lists")
    print("✅ Performance optimization strategies and best practices")
    print("✅ Memory-efficient approaches for large datasets")
    print("✅ Practical applications and real-world problem solving")
    
    print("\n💡 List Functions & Methods Mastery Key Points:")
    key_points = [
        "Built-in functions like len(), sum(), max() are optimized for performance",
        "List methods modify the original list (mutating operations)",
        "Use list comprehensions for readable and efficient transformations",
        "map(), filter(), reduce() enable functional programming paradigms",
        "Choose appropriate data structures based on use case requirements",
        "Generators save memory for large sequences and one-time iterations",
        "Understanding time complexity helps choose the right operation",
        "Composition and currying create reusable, modular code"
    ]
    
    for point in key_points:
        print(f"   • {point}")
    
    print("\n🎯 Expert-Level Applications:")
    applications = [
        "Data preprocessing pipelines with functional transformations",
        "Memory-efficient processing of large datasets with generators",
        "Custom data structures built on top of Python lists",
        "Algorithm implementation using appropriate list operations",
        "Performance-critical code optimization for list processing",
        "Functional programming patterns for complex data transformations",
        "Stream processing and real-time data analysis",
        "Machine learning data manipulation and feature engineering"
    ]
    
    for i, application in enumerate(applications, 1):
        print(f"   {i}. {application}")
    
    print(f"\n🚀 Master Python Lists - Foundation for Data Manipulation!")
    print("Efficient list operations are the backbone of effective Python programming!")