"""
List Replication and Duplication - Complete Python Guide
======================================================

Comprehensive guide to replicating, duplicating, and repeating Python lists
using various methods including multiplication, copying, and advanced techniques.
Covers all approaches from basic repetition to complex duplication patterns.

Author: Python Learning Notes
Date: September 2025
Topic: List Replication, Duplication, Repetition, Copying, Memory Management
"""

import copy
import sys
import time
from typing import List, Any, Union, Optional

# =============================================================================
# FUNDAMENTALS OF LIST REPLICATION
# =============================================================================

def list_replication_fundamentals():
    """
    Understanding the basics of list replication in Python
    """
    print("🔄 LIST REPLICATION FUNDAMENTALS")
    print("=" * 34)
    
    print("🎯 What is List Replication?")
    print("   List replication creates multiple copies or repetitions of list")
    print("   elements or entire lists. Python offers several methods with")
    print("   different behaviors and memory implications.")
    
    print(f"\n📊 Types of List Replication:")
    replication_types = [
        ("Element Repetition", "Repeat list elements multiple times", "*", "[1, 2] * 3 → [1, 2, 1, 2, 1, 2]"),
        ("Shallow Copy", "Create independent list reference", ".copy(), [:]", "Changes don't affect original"),
        ("Deep Copy", "Create completely independent copy", "copy.deepcopy()", "Nested objects also copied"),
        ("Reference Copy", "Create new reference to same list", "=", "Changes affect both variables"),
        ("Conditional Replication", "Replicate based on conditions", "Comprehensions", "Selective duplication"),
        ("Pattern Replication", "Create structured patterns", "Custom functions", "Complex duplication logic")
    ]
    
    print("   Type                │ Description                    │ Method        │ Example")
    print("   ────────────────────┼────────────────────────────────┼───────────────┼──────────────────────────")
    
    for rep_type, desc, method, example in replication_types:
        print(f"   {rep_type:<19} │ {desc:<30} │ {method:<13} │ {example}")
    
    return {'replication_types': replication_types}

def basic_replication_methods():
    """
    Demonstrate basic list replication methods
    """
    print("\n✖️ BASIC REPLICATION METHODS")
    print("=" * 31)
    
    # Original list for demonstrations
    original = [1, 2, 3]
    print(f"Original list: {original}")
    
    # 1. MULTIPLICATION OPERATOR (*)
    print(f"\n1️⃣ Multiplication Operator (*):")
    
    # Basic multiplication
    replicated_2x = original * 2
    replicated_3x = original * 3
    replicated_5x = original * 5
    
    print(f"   original * 2 = {replicated_2x}")
    print(f"   original * 3 = {replicated_3x}")
    print(f"   original * 5 = {replicated_5x}")
    
    # Edge cases
    replicated_0 = original * 0
    replicated_1 = original * 1
    
    print(f"   original * 0 = {replicated_0}")  # Empty list
    print(f"   original * 1 = {replicated_1}")  # Same as original
    
    # 2. REVERSE MULTIPLICATION
    print(f"\n2️⃣ Reverse Multiplication:")
    
    reverse_mult = 3 * original  # Same as original * 3
    print(f"   3 * original = {reverse_mult}")
    print(f"   Equivalent to original * 3")
    
    # 3. IN-PLACE MULTIPLICATION (*=)
    print(f"\n3️⃣ In-Place Multiplication (*=):")
    
    in_place_list = [1, 2, 3]
    print(f"   Before: {in_place_list}")
    in_place_list *= 3
    print(f"   After *= 3: {in_place_list}")
    print(f"   Original list modified in-place")
    
    # 4. STRING LIST REPLICATION
    print(f"\n4️⃣ String List Replication:")
    
    words = ["hello", "world"]
    repeated_words = words * 4
    print(f"   {words} * 4 = {repeated_words}")
    
    # 5. MIXED TYPE LIST REPLICATION
    print(f"\n5️⃣ Mixed Type List Replication:")
    
    mixed = [1, "a", True, None]
    repeated_mixed = mixed * 2
    print(f"   {mixed} * 2 = {repeated_mixed}")
    
    return {
        'basic_examples': {
            'replicated_2x': replicated_2x,
            'replicated_3x': replicated_3x,
            'repeated_words': repeated_words,
            'repeated_mixed': repeated_mixed
        }
    }

def advanced_replication_techniques():
    """
    Advanced list replication and duplication techniques
    """
    print("\n🚀 ADVANCED REPLICATION TECHNIQUES")
    print("=" * 36)
    
    # 1. NESTED LIST REPLICATION PITFALLS
    print("1️⃣ Nested List Replication - Common Pitfalls:")
    
    # CAUTION: This creates references to the same nested list!
    nested_wrong = [[1, 2, 3]] * 3
    print(f"   [[1, 2, 3]] * 3 = {nested_wrong}")
    print(f"   ⚠️  All sublists are the SAME object!")
    
    # Demonstrate the problem
    nested_wrong[0][0] = 999
    print(f"   After nested_wrong[0][0] = 999: {nested_wrong}")
    print(f"   😱 All sublists changed because they share the same reference!")
    
    # CORRECT: Use list comprehension
    nested_correct = [[1, 2, 3] for _ in range(3)]
    print(f"   Correct way: [[1, 2, 3] for _ in range(3)] = {nested_correct}")
    
    nested_correct[0][0] = 888
    print(f"   After nested_correct[0][0] = 888: {nested_correct}")
    print(f"   ✅ Only first sublist changed - independent objects!")
    
    # 2. CONDITIONAL REPLICATION
    print(f"\n2️⃣ Conditional Replication:")
    
    def replicate_conditionally(lst: List[Any], condition: callable, times: int) -> List[Any]:
        """Replicate list elements based on condition"""
        result = []
        for item in lst:
            if condition(item):
                result.extend([item] * times)
            else:
                result.append(item)
        return result
    
    numbers = [1, 2, 3, 4, 5, 6]
    # Replicate even numbers 3 times, keep odd numbers as-is
    conditional_result = replicate_conditionally(numbers, lambda x: x % 2 == 0, 3)
    
    print(f"   Original: {numbers}")
    print(f"   Replicate even numbers 3x: {conditional_result}")
    
    # 3. PATTERN-BASED REPLICATION
    print(f"\n3️⃣ Pattern-Based Replication:")
    
    def create_pattern(base_list: List[Any], pattern: List[int]) -> List[Any]:
        """Create list based on replication pattern"""
        result = []
        for i, count in enumerate(pattern):
            if i < len(base_list):
                result.extend([base_list[i]] * count)
        return result
    
    base = ['A', 'B', 'C', 'D']
    pattern = [1, 3, 2, 4]  # A:1 time, B:3 times, C:2 times, D:4 times
    
    pattern_result = create_pattern(base, pattern)
    print(f"   Base list: {base}")
    print(f"   Pattern: {pattern}")
    print(f"   Result: {pattern_result}")
    
    # 4. INTERLEAVED REPLICATION
    print(f"\n4️⃣ Interleaved Replication:")
    
    def interleaved_replication(list1: List[Any], list2: List[Any], 
                               times: int) -> List[Any]:
        """Interleave two lists with replication"""
        result = []
        max_length = max(len(list1), len(list2))
        
        for i in range(max_length):
            if i < len(list1):
                result.extend([list1[i]] * times)
            if i < len(list2):
                result.extend([list2[i]] * times)
        
        return result
    
    list_a = [1, 3, 5]
    list_b = [2, 4, 6]
    interleaved = interleaved_replication(list_a, list_b, 2)
    
    print(f"   List A: {list_a}")
    print(f"   List B: {list_b}")
    print(f"   Interleaved (2x each): {interleaved}")
    
    # 5. FIBONACCI REPLICATION
    print(f"\n5️⃣ Fibonacci Replication Pattern:")
    
    def fibonacci_replication(lst: List[Any], n_terms: int) -> List[Any]:
        """Replicate list elements following Fibonacci pattern"""
        if n_terms <= 0:
            return []
        
        # Generate Fibonacci sequence
        fib = [1, 1]
        for i in range(2, n_terms):
            fib.append(fib[i-1] + fib[i-2])
        
        result = []
        for i, item in enumerate(lst):
            if i < len(fib):
                result.extend([item] * fib[i])
        
        return result
    
    elements = ['🍎', '🍌', '🍇', '🍓', '🍑']
    fib_replicated = fibonacci_replication(elements, 5)
    
    print(f"   Elements: {elements}")
    print(f"   Fibonacci replication: {fib_replicated}")
    print(f"   Pattern: 1, 1, 2, 3, 5 repetitions")
    
    return {
        'nested_demonstration': {'wrong': nested_wrong, 'correct': nested_correct},
        'conditional_result': conditional_result,
        'pattern_result': pattern_result,
        'interleaved_result': interleaved,
        'fibonacci_result': fib_replicated
    }

def memory_and_performance_analysis():
    """
    Analyze memory usage and performance of different replication methods
    """
    print("\n💾 MEMORY AND PERFORMANCE ANALYSIS")
    print("=" * 37)
    
    def time_operation(func, *args, iterations=1000):
        """Time a replication operation"""
        start = time.perf_counter()
        for _ in range(iterations):
            result = func(*args)
        end = time.perf_counter()
        return (end - start) * 1000 / iterations, result
    
    # Test data
    base_list = list(range(100))  # 100 element list
    
    print("📊 Performance Comparison of Replication Methods:")
    print("   Method                │ Time (ms/op) │ Memory (bytes) │ Notes")
    print("   ──────────────────────┼──────────────┼────────────────┼─────────────────")
    
    # Method 1: Multiplication operator
    mult_time, mult_result = time_operation(lambda lst, n: lst * n, base_list, 5, iterations=1000)
    mult_memory = sys.getsizeof(mult_result)
    
    # Method 2: List comprehension repetition
    comp_time, comp_result = time_operation(
        lambda lst, n: [item for item in lst for _ in range(n)], 
        base_list, 5, iterations=100
    )
    comp_memory = sys.getsizeof(comp_result)
    
    # Method 3: Extend in loop
    def extend_method(lst, n):
        result = []
        for _ in range(n):
            result.extend(lst)
        return result
    
    extend_time, extend_result = time_operation(extend_method, base_list, 5, iterations=100)
    extend_memory = sys.getsizeof(extend_result)
    
    print(f"   Multiplication (*)    │ {mult_time:10.4f}   │ {mult_memory:12,}   │ Fastest, most memory efficient")
    print(f"   List comprehension    │ {comp_time:10.4f}   │ {comp_memory:12,}   │ Flexible but slower")
    print(f"   Extend in loop        │ {extend_time:10.4f}   │ {extend_memory:12,}   │ Most readable but slowest")
    
    # Memory analysis for nested lists
    print(f"\n💡 Memory Behavior Analysis:")
    
    # Shallow replication (references shared)
    shallow_nested = [[1, 2, 3]] * 3
    shallow_memory = sys.getsizeof(shallow_nested) + sum(sys.getsizeof(sublist) for sublist in shallow_nested)
    
    # Deep replication (independent objects)
    deep_nested = [[1, 2, 3] for _ in range(3)]
    deep_memory = sys.getsizeof(deep_nested) + sum(sys.getsizeof(sublist) for sublist in deep_nested)
    
    print(f"   Replication Type      │ Memory Usage │ Object Independence")
    print(f"   ──────────────────────┼──────────────┼───────────────────────")
    print(f"   Shallow (references)  │ {shallow_memory:10,} B │ ❌ Shared references")
    print(f"   Deep (independent)    │ {deep_memory:10,} B │ ✅ Independent objects")
    
    return {
        'performance_data': {
            'multiplication': {'time': mult_time, 'memory': mult_memory},
            'comprehension': {'time': comp_time, 'memory': comp_memory},
            'extend_loop': {'time': extend_time, 'memory': extend_memory}
        },
        'memory_analysis': {
            'shallow_memory': shallow_memory,
            'deep_memory': deep_memory
        }
    }

def copying_vs_replication():
    """
    Understanding the difference between copying and replication
    """
    print("\n📋 COPYING VS REPLICATION")
    print("=" * 28)
    
    print("🔍 Understanding the Differences:")
    print("   Replication: Creating multiple instances of list elements")
    print("   Copying: Creating new list objects with same content")
    
    # Original list
    original = [1, 2, [3, 4], 5]
    print(f"\n📊 Original list: {original}")
    
    # 1. REFERENCE ASSIGNMENT (Not a copy!)
    print(f"\n1️⃣ Reference Assignment:")
    reference = original
    print(f"   reference = original")
    print(f"   Same object? {original is reference}")
    print(f"   Same ID? {id(original) == id(reference)}")
    
    reference[0] = 999
    print(f"   After reference[0] = 999:")
    print(f"   Original: {original}")
    print(f"   Reference: {reference}")
    print(f"   ⚠️  Both changed - same object!")
    
    # Reset for next examples
    original = [1, 2, [3, 4], 5]
    
    # 2. SHALLOW COPY
    print(f"\n2️⃣ Shallow Copy Methods:")
    
    shallow1 = original.copy()
    shallow2 = original[:]
    shallow3 = list(original)
    
    print(f"   Methods: .copy(), [:], list()")
    print(f"   Same object? {original is shallow1}")
    print(f"   Nested objects shared? {original[2] is shallow1[2]}")
    
    # Modify shallow copy
    shallow1[0] = 777
    shallow1[2][0] = 888  # This affects original too!
    
    print(f"   After shallow1[0] = 777 and shallow1[2][0] = 888:")
    print(f"   Original: {original}")
    print(f"   Shallow1: {shallow1}")
    print(f"   ⚠️  Nested list affected in both!")
    
    # Reset for deep copy
    original = [1, 2, [3, 4], 5]
    
    # 3. DEEP COPY
    print(f"\n3️⃣ Deep Copy:")
    
    deep = copy.deepcopy(original)
    
    print(f"   Method: copy.deepcopy()")
    print(f"   Same object? {original is deep}")
    print(f"   Nested objects shared? {original[2] is deep[2]}")
    
    # Modify deep copy
    deep[0] = 555
    deep[2][0] = 666
    
    print(f"   After deep[0] = 555 and deep[2][0] = 666:")
    print(f"   Original: {original}")
    print(f"   Deep: {deep}")
    print(f"   ✅ Completely independent!")
    
    # 4. REPLICATION WITH MULTIPLICATION
    print(f"\n4️⃣ Replication with Multiplication:")
    
    simple_list = [1, 2, 3]
    replicated = simple_list * 3
    
    print(f"   Original: {simple_list}")
    print(f"   Replicated: {replicated}")
    print(f"   Different purpose: repeating elements vs copying structure")
    
    return {
        'copy_types': {
            'reference': 'Same object, same memory',
            'shallow': 'New object, shared nested objects',
            'deep': 'Completely independent objects'
        },
        'replication_purpose': 'Repeat elements multiple times'
    }

def practical_applications():
    """
    Practical applications of list replication techniques
    """
    print("\n🌍 PRACTICAL APPLICATIONS")
    print("=" * 27)
    
    print("🚀 Real-World List Replication Scenarios:")
    
    # 1. CREATING GAME BOARDS
    print(f"\n1️⃣ Game Board Creation:")
    
    def create_game_board(rows: int, cols: int, default_value: str = "⬜") -> List[List[str]]:
        """Create a game board with proper independent cells"""
        return [[default_value for _ in range(cols)] for _ in range(rows)]
    
    # Tic-tac-toe board
    tic_tac_toe = create_game_board(3, 3, "⬜")
    tic_tac_toe[1][1] = "❌"  # Center move
    tic_tac_toe[0][0] = "⭕"  # Corner move
    
    print(f"   Tic-Tac-Toe Board:")
    for row in tic_tac_toe:
        print(f"     {' '.join(row)}")
    
    # 2. SURVEY RESPONSE INITIALIZATION
    print(f"\n2️⃣ Survey Response Initialization:")
    
    def initialize_survey_responses(num_questions: int, num_participants: int) -> List[List[Optional[int]]]:
        """Initialize survey response matrix"""
        return [[None for _ in range(num_questions)] for _ in range(num_participants)]
    
    survey = initialize_survey_responses(5, 3)  # 3 participants, 5 questions
    
    # Simulate some responses
    survey[0] = [5, 4, 3, 5, 4]  # Participant 1
    survey[1] = [3, 3, 4, 2, 5]  # Participant 2
    # Participant 3 hasn't responded yet
    
    print(f"   Survey Responses (5 questions, 3 participants):")
    for i, responses in enumerate(survey):
        print(f"     Participant {i+1}: {responses}")
    
    # 3. BATCH PROCESSING INITIALIZATION
    print(f"\n3️⃣ Batch Processing Initialization:")
    
    def create_processing_batches(data: List[Any], batch_size: int) -> List[List[Any]]:
        """Create batches for processing large datasets"""
        batches = []
        for i in range(0, len(data), batch_size):
            batch = data[i:i + batch_size]
            batches.append(batch)
        return batches
    
    large_dataset = list(range(1, 23))  # 22 items
    batches = create_processing_batches(large_dataset, 5)
    
    print(f"   Dataset: {large_dataset}")
    print(f"   Batches (size 5):")
    for i, batch in enumerate(batches):
        print(f"     Batch {i+1}: {batch}")
    
    # 4. PATTERN GENERATION FOR DESIGN
    print(f"\n4️⃣ Pattern Generation for Design:")
    
    def create_pattern(base_pattern: List[str], repetitions: int, 
                      separator: str = " ") -> str:
        """Create decorative patterns"""
        full_pattern = base_pattern * repetitions
        return separator.join(full_pattern)
    
    # Border pattern
    border_elements = ["*", "-", "*"]
    border_pattern = create_pattern(border_elements, 10, "")
    
    print(f"   Base pattern: {border_elements}")
    print(f"   Border: {border_pattern}")
    
    # Decorative pattern
    decorative = ["🌟", "🌙", "⭐"]
    decoration = create_pattern(decorative, 5, " ")
    print(f"   Decoration: {decoration}")
    
    # 5. TEST DATA GENERATION
    print(f"\n5️⃣ Test Data Generation:")
    
    def generate_test_data(template: dict, count: int) -> List[dict]:
        """Generate test data by replicating template with variations"""
        test_data = []
        for i in range(count):
            # Create a copy of template and modify
            test_item = template.copy()
            test_item['id'] = i + 1
            test_item['name'] = f"{template['name']}_{i+1}"
            test_data.append(test_item)
        return test_data
    
    user_template = {
        'id': None,
        'name': 'TestUser',
        'email': 'test@example.com',
        'active': True
    }
    
    test_users = generate_test_data(user_template, 3)
    
    print(f"   Template: {user_template}")
    print(f"   Generated test data:")
    for user in test_users:
        print(f"     {user}")
    
    return {
        'game_board': tic_tac_toe,
        'survey_responses': survey,
        'processing_batches': len(batches),
        'border_pattern': border_pattern,
        'test_users': len(test_users)
    }

# =============================================================================
# MAIN EXECUTION AND COMPREHENSIVE DEMONSTRATION
# =============================================================================

def main():
    """
    Main function executing comprehensive list replication guide
    """
    print(__doc__)
    
    # Core sections
    fundamentals = list_replication_fundamentals()
    basic_methods = basic_replication_methods()
    advanced_techniques = advanced_replication_techniques()
    memory_analysis = memory_and_performance_analysis()
    copying_comparison = copying_vs_replication()
    applications = practical_applications()
    
    return {
        'fundamentals': fundamentals,
        'basic_methods': basic_methods,
        'advanced_techniques': advanced_techniques,
        'memory_analysis': memory_analysis,
        'copying_comparison': copying_comparison,
        'applications': applications
    }

if __name__ == "__main__":
    """
    Execute comprehensive list replication and duplication guide
    """
    results = main()
    
    print("\n" + "=" * 80)
    print("🎓 LIST REPLICATION & DUPLICATION MASTERY SUMMARY")
    print("=" * 80)
    print("✅ Complete understanding of list replication methods and techniques")
    print("✅ Memory analysis and performance optimization strategies")
    print("✅ Advanced replication patterns and conditional duplication")
    print("✅ Distinction between copying and replication operations")
    print("✅ Memory-efficient approaches and pitfall avoidance")
    print("✅ Real-world applications in game development, data processing, and testing")
    print("✅ Best practices for choosing appropriate replication methods")
    
    print("\n💡 List Replication Mastery Key Points:")
    key_points = [
        "* operator is fastest and most memory-efficient for basic replication",
        "Nested list replication with * creates shared references (dangerous!)",
        "List comprehensions create independent objects for nested structures",
        "Shallow copy vs deep copy have different memory and behavior implications",
        "Pattern-based replication enables complex data structure initialization",
        "Conditional replication allows selective element duplication",
        "Performance varies significantly with replication method and data size",
        "Understanding memory behavior prevents common programming errors"
    ]
    
    for point in key_points:
        print(f"   • {point}")
    
    print("\n🎯 Expert-Level Applications:")
    applications = [
        "Game board and matrix initialization with independent cells",
        "Survey and form response data structure preparation",
        "Batch processing system setup for large dataset handling",
        "Test data generation and mock object creation",
        "Pattern generation for UI design and data visualization",
        "Memory-efficient data structure replication for performance optimization",
        "Distributed computing data distribution and replication",
        "Scientific computing array initialization and manipulation"
    ]
    
    for i, application in enumerate(applications, 1):
        print(f"   {i}. {application}")
    
    print(f"\n🚀 Master List Replication for Efficient Data Structure Creation!")
    print("Understanding replication patterns is essential for scalable system design!")

# =============================================================================
# ORIGINAL SIMPLE EXAMPLE (Enhanced with Context)
# =============================================================================

# Simple demonstration of basic list replication
list = [1, 2, 3, 4, 5]
cht = list * 2  # Replicate the list elements twice
print("Basic Example:")
print(f"Original list: {list}")
print(f"Replicated (list * 2): {cht}")
print("This creates a new list with elements repeated twice!")