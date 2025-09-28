"""
List Joining and Concatenation - Complete Python Guide
=====================================================

Comprehensive guide to joining, concatenating, and merging Python lists
using various methods, techniques, and performance optimizations.
Covers all approaches from basic concatenation to advanced merging strategies.

Author: Python Learning Notes
Date: September 2025
Topic: List Joining, Concatenation, Merging, Performance Optimization
"""

import time
import sys
from typing import List, Any, Union, Iterator
from itertools import chain
import operator
from functools import reduce

# =============================================================================
# FUNDAMENTALS OF LIST JOINING
# =============================================================================

def list_joining_fundamentals():
    """
    Comprehensive guide to list joining fundamentals
    """
    print("🔗 LIST JOINING FUNDAMENTALS")
    print("=" * 30)
    
    print("🎯 What is List Joining?")
    print("   List joining (concatenation) combines multiple lists into one")
    print("   continuous sequence. Python offers several methods with different")
    print("   performance characteristics and use cases.")
    
    print(f"\n📊 Types of List Joining:")
    joining_types = [
        ("Concatenation", "Combine lists end-to-end", "+, extend()", "[1,2] + [3,4] → [1,2,3,4]"),
        ("Merging", "Combine with specific ordering", "Custom functions", "Merge sorted lists"),
        ("Interleaving", "Alternate elements from lists", "zip(), custom", "[1,3] + [2,4] → [1,2,3,4]"),
        ("Flattening", "Join nested lists into flat list", "chain(), comprehension", "[[1,2],[3,4]] → [1,2,3,4]"),
        ("Union", "Join with duplicates removed", "set operations", "[1,2] ∪ [2,3] → [1,2,3]"),
        ("Cartesian", "All combinations of elements", "itertools.product", "[1,2] × [a,b] → [(1,a),(1,b)...]")
    ]
    
    print("   Type          │ Description              │ Methods           │ Example")
    print("   ──────────────┼──────────────────────────┼───────────────────┼─────────────────────")
    
    for join_type, desc, methods, example in joining_types:
        print(f"   {join_type:<13} │ {desc:<24} │ {methods:<17} │ {example}")
    
    return {
        'joining_types': joining_types
    }

def basic_concatenation_methods():
    """
    Demonstrate all basic list concatenation methods
    """
    print("\n➕ BASIC CONCATENATION METHODS")
    print("=" * 32)
    
    # Sample lists for demonstration
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = [7, 8, 9]
    
    print("📋 Sample Lists:")
    print(f"   list1 = {list1}")
    print(f"   list2 = {list2}")
    print(f"   list3 = {list3}")
    
    print(f"\n🔧 Concatenation Methods:")
    
    # Method 1: Plus operator (+)
    result1 = list1 + list2
    print(f"1️⃣ Plus Operator (+):")
    print(f"   list1 + list2 = {result1}")
    print(f"   Creates new list, original lists unchanged")
    print(f"   Original list1: {list1}")
    
    # Method 2: Augmented assignment (+=)
    list1_copy = list1.copy()
    list1_copy += list2
    print(f"\n2️⃣ Augmented Assignment (+=):")
    print(f"   list1 += list2 = {list1_copy}")
    print(f"   Modifies original list in-place")
    
    # Method 3: extend() method
    list1_extend = list1.copy()
    list1_extend.extend(list2)
    print(f"\n3️⃣ extend() Method:")
    print(f"   list1.extend(list2) = {list1_extend}")
    print(f"   Modifies original list, returns None")
    
    # Method 4: Unpacking with *
    result4 = [*list1, *list2]
    print(f"\n4️⃣ Unpacking with * operator:")
    print(f"   [*list1, *list2] = {result4}")
    print(f"   Modern Python syntax, creates new list")
    
    # Method 5: List comprehension
    result5 = [item for sublist in [list1, list2] for item in sublist]
    print(f"\n5️⃣ List Comprehension:")
    print(f"   [item for sublist in [list1, list2] for item in sublist] = {result5}")
    print(f"   Flexible but more verbose")
    
    # Method 6: itertools.chain()
    result6 = list(chain(list1, list2))
    print(f"\n6️⃣ itertools.chain():")
    print(f"   list(chain(list1, list2)) = {result6}")
    print(f"   Memory efficient for large lists")
    
    # Multiple list concatenation
    print(f"\n🔄 Multiple List Concatenation:")
    
    # Multiple lists with +
    result_multi1 = list1 + list2 + list3
    print(f"   list1 + list2 + list3 = {result_multi1}")
    
    # Multiple lists with chain
    result_multi2 = list(chain(list1, list2, list3))
    print(f"   chain(list1, list2, list3) = {result_multi2}")
    
    # Multiple lists with unpacking
    result_multi3 = [*list1, *list2, *list3]
    print(f"   [*list1, *list2, *list3] = {result_multi3}")
    
    return {
        'methods': ['plus_operator', 'augmented_assignment', 'extend', 'unpacking', 'comprehension', 'chain'],
        'results': {
            'plus': result1,
            'extend': list1_extend,
            'unpacking': result4,
            'chain': result6,
            'multiple': result_multi1
        }
    }

def advanced_joining_techniques():
    """
    Advanced list joining and merging techniques
    """
    print("\n🚀 ADVANCED JOINING TECHNIQUES")
    print("=" * 32)
    
    # 1. MERGING SORTED LISTS
    print("1️⃣ Merging Sorted Lists:")
    
    def merge_sorted_lists(list1: List[int], list2: List[int]) -> List[int]:
        """Merge two sorted lists maintaining order - O(n + m)"""
        result = []
        i = j = 0
        
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        
        # Add remaining elements
        result.extend(list1[i:])
        result.extend(list2[j:])
        return result
    
    sorted1 = [1, 3, 5, 7, 9]
    sorted2 = [2, 4, 6, 8, 10]
    merged_sorted = merge_sorted_lists(sorted1, sorted2)
    
    print(f"   Sorted list 1: {sorted1}")
    print(f"   Sorted list 2: {sorted2}")
    print(f"   Merged result: {merged_sorted}")
    
    # 2. INTERLEAVING LISTS
    print(f"\n2️⃣ Interleaving Lists:")
    
    def interleave_lists(*lists):
        """Interleave elements from multiple lists"""
        max_length = max(len(lst) for lst in lists) if lists else 0
        result = []
        
        for i in range(max_length):
            for lst in lists:
                if i < len(lst):
                    result.append(lst[i])
        
        return result
    
    list_a = [1, 4, 7]
    list_b = [2, 5, 8]
    list_c = [3, 6, 9, 10]
    
    interleaved = interleave_lists(list_a, list_b, list_c)
    print(f"   List A: {list_a}")
    print(f"   List B: {list_b}")
    print(f"   List C: {list_c}")
    print(f"   Interleaved: {interleaved}")
    
    # Alternative using zip_longest
    from itertools import zip_longest
    interleaved_zip = [item for items in zip_longest(list_a, list_b, list_c, fillvalue=None) 
                      for item in items if item is not None]
    print(f"   Using zip_longest: {interleaved_zip}")
    
    # 3. FLATTENING NESTED LISTS
    print(f"\n3️⃣ Flattening Nested Lists:")
    
    nested_list = [[1, 2], [3, 4, 5], [6], [7, 8, 9]]
    
    # Method 1: List comprehension
    flat1 = [item for sublist in nested_list for item in sublist]
    print(f"   Nested list: {nested_list}")
    print(f"   Flattened (comprehension): {flat1}")
    
    # Method 2: itertools.chain.from_iterable
    flat2 = list(chain.from_iterable(nested_list))
    print(f"   Flattened (chain.from_iterable): {flat2}")
    
    # Method 3: Recursive flattening for deeply nested
    def recursive_flatten(lst):
        """Recursively flatten arbitrarily nested lists"""
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(recursive_flatten(item))
            else:
                result.append(item)
        return result
    
    deeply_nested = [1, [2, 3], [4, [5, 6]], [[7, 8], 9]]
    flat_recursive = recursive_flatten(deeply_nested)
    print(f"   Deeply nested: {deeply_nested}")
    print(f"   Recursively flattened: {flat_recursive}")
    
    # 4. CONDITIONAL JOINING
    print(f"\n4️⃣ Conditional Joining:")
    
    def conditional_join(list1: List[int], list2: List[int], 
                        condition: callable = lambda x, y: x + y < 10) -> List[int]:
        """Join lists based on condition"""
        result = []
        
        for item1 in list1:
            for item2 in list2:
                if condition(item1, item2):
                    result.append((item1, item2))
        
        return result
    
    nums1 = [1, 2, 3, 4]
    nums2 = [3, 4, 5, 6]
    
    conditional_result = conditional_join(nums1, nums2, lambda x, y: x + y < 8)
    print(f"   List 1: {nums1}")
    print(f"   List 2: {nums2}")
    print(f"   Condition: x + y < 8")
    print(f"   Result: {conditional_result}")
    
    return {
        'merge_sorted': merged_sorted,
        'interleaved': interleaved,
        'flattened': flat1,
        'recursive_flat': flat_recursive,
        'conditional': conditional_result
    }

def set_operations_and_joining():
    """
    Set-based joining operations for unique combinations
    """
    print("\n🎭 SET OPERATIONS AND JOINING")
    print("=" * 31)
    
    print("🎯 Set-Based List Operations:")
    print("   When you need to join lists while handling duplicates")
    print("   or performing mathematical set operations")
    
    # Sample data with duplicates
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    list3 = [1, 3, 5, 7, 9]
    
    print(f"\n📊 Sample Data:")
    print(f"   list1 = {list1}")
    print(f"   list2 = {list2}")
    print(f"   list3 = {list3}")
    
    # 1. UNION (combine with no duplicates)
    print(f"\n🔗 Union Operations:")
    
    # Method 1: Convert to set and back
    union_set = list(set(list1) | set(list2))
    print(f"   Union (set method): {sorted(union_set)}")
    
    # Method 2: Preserve order with dict.fromkeys()
    union_ordered = list(dict.fromkeys(list1 + list2))
    print(f"   Union (order preserved): {union_ordered}")
    
    # Method 3: Multiple list union
    union_multiple = list(set(list1) | set(list2) | set(list3))
    print(f"   Union of three lists: {sorted(union_multiple)}")
    
    # 2. INTERSECTION (common elements)
    print(f"\n🔄 Intersection Operations:")
    
    intersection = list(set(list1) & set(list2))
    print(f"   Intersection list1 ∩ list2: {sorted(intersection)}")
    
    intersection_multiple = list(set(list1) & set(list2) & set(list3))
    print(f"   Intersection of three lists: {sorted(intersection_multiple)}")
    
    # 3. DIFFERENCE (elements in first but not second)
    print(f"\n➖ Difference Operations:")
    
    difference = list(set(list1) - set(list2))
    print(f"   Difference list1 - list2: {sorted(difference)}")
    
    symmetric_diff = list(set(list1) ^ set(list2))
    print(f"   Symmetric difference: {sorted(symmetric_diff)}")
    
    # 4. CUSTOM JOINING WITH PREDICATES
    print(f"\n🎯 Custom Joining with Predicates:")
    
    def join_with_predicate(list1: List[Any], list2: List[Any], 
                           predicate: callable) -> List[Any]:
        """Join lists based on custom predicate"""
        result = []
        for item1 in list1:
            for item2 in list2:
                if predicate(item1, item2):
                    result.append((item1, item2))
        return result
    
    # Join numbers where first is less than second
    less_than_pairs = join_with_predicate(
        [1, 2, 3], [2, 3, 4], 
        lambda x, y: x < y
    )
    print(f"   Pairs where first < second: {less_than_pairs}")
    
    # Join strings by length compatibility
    words1 = ["cat", "dog", "bird"]
    words2 = ["house", "car", "tree"]
    
    length_compatible = join_with_predicate(
        words1, words2,
        lambda x, y: abs(len(x) - len(y)) <= 1
    )
    print(f"   Words with similar length: {length_compatible}")
    
    return {
        'union_ordered': union_ordered,
        'intersection': sorted(intersection),
        'difference': sorted(difference),
        'symmetric_difference': sorted(symmetric_diff),
        'custom_joins': {
            'less_than': less_than_pairs,
            'length_compatible': length_compatible
        }
    }

def performance_analysis():
    """
    Performance analysis of different joining methods
    """
    print("\n⚡ PERFORMANCE ANALYSIS OF JOINING METHODS")
    print("=" * 44)
    
    def time_operation(func, *args, iterations=1000):
        """Time a joining operation"""
        start = time.perf_counter()
        for _ in range(iterations):
            result = func(*args)
        end = time.perf_counter()
        return (end - start) * 1000 / iterations, result
    
    # Create test data of different sizes
    small_lists = ([1] * 100, [2] * 100)
    medium_lists = ([1] * 1000, [2] * 1000)
    large_lists = ([1] * 5000, [2] * 5000)
    
    test_cases = [
        ("Small (200)", small_lists),
        ("Medium (2K)", medium_lists),
        ("Large (10K)", large_lists)
    ]
    
    print("📊 Joining Method Performance Comparison:")
    print("   Method            │ Small (200) │ Medium (2K) │ Large (10K) │ Notes")
    print("   ──────────────────┼─────────────┼─────────────┼─────────────┼─────────────────")
    
    # Define joining methods to test
    methods = [
        ("Plus operator", lambda l1, l2: l1 + l2, "Creates new list"),
        ("extend()", lambda l1, l2: l1.copy().extend(l2) or (l1 + l2), "Modifies original"),
        ("Unpacking", lambda l1, l2: [*l1, *l2], "Modern Python"),
        ("itertools.chain", lambda l1, l2: list(chain(l1, l2)), "Memory efficient"),
        ("List comprehension", lambda l1, l2: [x for lst in [l1, l2] for x in lst], "Flexible syntax")
    ]
    
    for method_name, method_func, notes in methods:
        times = []
        
        for size_name, (list1, list2) in test_cases:
            method_time, _ = time_operation(method_func, list1, list2, iterations=100)
            times.append(method_time)
        
        print(f"   {method_name:<17} │ {times[0]:9.4f} ms │ {times[1]:9.4f} ms │ {times[2]:9.4f} ms │ {notes}")
    
    # Memory usage analysis
    print(f"\n💾 Memory Usage Analysis:")
    
    def analyze_memory_usage():
        """Analyze memory usage of different approaches"""
        test_list1 = list(range(1000))
        test_list2 = list(range(1000, 2000))
        
        # Method 1: Plus operator (creates new list)
        result_plus = test_list1 + test_list2
        memory_plus = sys.getsizeof(result_plus)
        
        # Method 2: extend (modifies existing)
        result_extend = test_list1.copy()
        result_extend.extend(test_list2)
        memory_extend = sys.getsizeof(result_extend)
        
        # Method 3: itertools.chain (lazy evaluation)
        chain_obj = chain(test_list1, test_list2)
        memory_chain = sys.getsizeof(chain_obj)
        
        return {
            'plus': memory_plus,
            'extend': memory_extend,
            'chain': memory_chain
        }
    
    memory_results = analyze_memory_usage()
    
    print("   Method          │ Memory Usage │ Memory Efficiency")
    print("   ────────────────┼──────────────┼─────────────────────────")
    print(f"   Plus operator   │ {memory_results['plus']:10,} B │ Full list in memory")
    print(f"   extend()        │ {memory_results['extend']:10,} B │ Full list in memory")
    print(f"   itertools.chain │ {memory_results['chain']:10,} B │ Lazy evaluation (best)")
    
    # Best practices recommendations
    print(f"\n💡 Performance Best Practices:")
    recommendations = [
        "Use + operator for simple, small list concatenations",
        "Use extend() when modifying existing list in-place",
        "Use itertools.chain() for memory-efficient large list joining",
        "Use unpacking [*list1, *list2] for readable modern Python",
        "Convert to sets first if duplicates need to be removed",
        "Consider generators for one-time iteration over joined data",
        "Profile your specific use case for optimal method selection"
    ]
    
    for i, recommendation in enumerate(recommendations, 1):
        print(f"   {i}. {recommendation}")
    
    return {
        'performance_data': test_cases,
        'memory_analysis': memory_results,
        'best_practices': recommendations
    }

def practical_applications():
    """
    Practical applications of list joining techniques
    """
    print("\n🌍 PRACTICAL APPLICATIONS")
    print("=" * 27)
    
    print("🚀 Real-World List Joining Scenarios:")
    
    # 1. DATA PROCESSING PIPELINE
    print(f"\n1️⃣ Data Processing Pipeline:")
    
    # Simulate processing data from multiple sources
    sales_q1 = [1000, 1200, 1100, 1300]
    sales_q2 = [1400, 1350, 1500, 1250]
    sales_q3 = [1600, 1550, 1700, 1450]
    sales_q4 = [1800, 1750, 1900, 1650]
    
    # Combine quarterly data
    yearly_sales = list(chain(sales_q1, sales_q2, sales_q3, sales_q4))
    print(f"   Q1 Sales: {sales_q1}")
    print(f"   Q2 Sales: {sales_q2}")
    print(f"   Q3 Sales: {sales_q3}")
    print(f"   Q4 Sales: {sales_q4}")
    print(f"   Yearly Sales: {yearly_sales}")
    print(f"   Total Revenue: ${sum(yearly_sales):,}")
    
    # 2. LOG FILE AGGREGATION
    print(f"\n2️⃣ Log File Aggregation:")
    
    # Simulate log entries from multiple servers
    server1_logs = ["ERROR: Connection failed", "INFO: User login", "WARN: High CPU"]
    server2_logs = ["INFO: Database updated", "ERROR: Disk space low"]
    server3_logs = ["INFO: Backup completed", "WARN: Memory usage high", "INFO: User logout"]
    
    # Aggregate with timestamps
    def add_timestamps(logs, server_id):
        return [f"[Server-{server_id}] {log}" for log in logs]
    
    all_logs = (add_timestamps(server1_logs, 1) + 
               add_timestamps(server2_logs, 2) + 
               add_timestamps(server3_logs, 3))
    
    print(f"   Aggregated Logs:")
    for log in all_logs:
        print(f"     {log}")
    
    # 3. FEATURE ENGINEERING
    print(f"\n3️⃣ Machine Learning Feature Engineering:")
    
    # Combine different feature types
    numerical_features = [25, 50000, 3.5, 1200]  # age, salary, rating, experience
    categorical_features = [1, 0, 1]  # encoded: is_manager, is_remote, has_degree
    text_features = [0.2, 0.8, 0.1]  # sentiment scores from text analysis
    
    # Combine all features for ML model
    combined_features = [*numerical_features, *categorical_features, *text_features]
    
    print(f"   Numerical features: {numerical_features}")
    print(f"   Categorical features: {categorical_features}")
    print(f"   Text features: {text_features}")
    print(f"   Combined feature vector: {combined_features}")
    print(f"   Total feature count: {len(combined_features)}")
    
    # 4. BATCH PROCESSING
    print(f"\n4️⃣ Batch Processing System:")
    
    def process_batches(*batches, batch_size=5):
        """Process multiple batches and combine results"""
        all_items = list(chain(*batches))
        
        # Process in chunks
        results = []
        for i in range(0, len(all_items), batch_size):
            batch = all_items[i:i + batch_size]
            # Simulate processing (e.g., square each number)
            processed_batch = [x**2 for x in batch]
            results.extend(processed_batch)
        
        return results
    
    batch1 = [1, 2, 3, 4]
    batch2 = [5, 6, 7, 8, 9]
    batch3 = [10, 11, 12]
    
    processed_results = process_batches(batch1, batch2, batch3)
    
    print(f"   Batch 1: {batch1}")
    print(f"   Batch 2: {batch2}")
    print(f"   Batch 3: {batch3}")
    print(f"   Processed results: {processed_results}")
    
    # 5. CONFIGURATION MERGING
    print(f"\n5️⃣ Configuration Merging:")
    
    # Simulate merging configuration from multiple sources
    default_config = ["debug=false", "timeout=30", "retries=3"]
    user_config = ["debug=true", "theme=dark"]
    env_config = ["timeout=60", "database_url=prod"]
    
    # Merge configurations (later values override earlier ones)
    def merge_configs(*config_lists):
        """Merge configuration lists, with later configs overriding earlier ones"""
        config_dict = {}
        
        for config_list in config_lists:
            for item in config_list:
                key, value = item.split('=')
                config_dict[key] = value
        
        return [f"{k}={v}" for k, v in config_dict.items()]
    
    final_config = merge_configs(default_config, user_config, env_config)
    
    print(f"   Default config: {default_config}")
    print(f"   User config: {user_config}")
    print(f"   Environment config: {env_config}")
    print(f"   Final merged config: {final_config}")
    
    return {
        'sales_aggregation': {'yearly_total': sum(yearly_sales)},
        'log_aggregation': {'total_logs': len(all_logs)},
        'feature_engineering': {'feature_count': len(combined_features)},
        'batch_processing': {'processed_count': len(processed_results)},
        'config_merging': {'final_config': final_config}
    }

# =============================================================================
# MAIN EXECUTION AND COMPREHENSIVE DEMONSTRATION
# =============================================================================

def main():
    """
    Main function executing comprehensive list joining guide
    """
    print(__doc__)
    
    # Core sections
    fundamentals = list_joining_fundamentals()
    basic_methods = basic_concatenation_methods()
    advanced_techniques = advanced_joining_techniques()
    set_operations = set_operations_and_joining()
    performance = performance_analysis()
    applications = practical_applications()
    
    return {
        'fundamentals': fundamentals,
        'basic_methods': basic_methods,
        'advanced_techniques': advanced_techniques,
        'set_operations': set_operations,
        'performance': performance,
        'applications': applications
    }

if __name__ == "__main__":
    """
    Execute comprehensive list joining and concatenation guide
    """
    results = main()
    
    print("\n" + "=" * 80)
    print("🎓 LIST JOINING & CONCATENATION MASTERY SUMMARY")
    print("=" * 80)
    print("✅ Complete understanding of all list joining methods and techniques")
    print("✅ Performance analysis and optimization strategies")
    print("✅ Advanced joining techniques including merging and interleaving")
    print("✅ Set-based operations for handling duplicates and unions")
    print("✅ Memory-efficient approaches for large-scale data processing")
    print("✅ Real-world applications in data processing and system design")
    print("✅ Best practices for choosing appropriate joining methods")
    
    print("\n💡 List Joining Mastery Key Points:")
    key_points = [
        "+ operator creates new lists, extend() modifies existing lists",
        "itertools.chain() provides memory-efficient lazy evaluation",
        "Unpacking syntax [*list1, *list2] is readable and modern",
        "Set operations handle duplicates and mathematical relationships",
        "Merge algorithms maintain sorted order efficiently",
        "Performance varies significantly with list size and method choice",
        "Consider memory usage for large-scale data processing",
        "Choose method based on mutability, performance, and readability needs"
    ]
    
    for point in key_points:
        print(f"   • {point}")
    
    print("\n🎯 Expert-Level Applications:")
    applications = [
        "ETL pipelines for data warehouse processing",
        "Stream processing and real-time data aggregation",
        "Machine learning feature engineering and data preparation",
        "Log aggregation and monitoring system data collection",
        "Distributed computing batch processing systems",
        "Configuration management and environment merging",
        "Graph algorithms and network data processing",
        "Scientific computing and numerical data analysis"
    ]
    
    for i, application in enumerate(applications, 1):
        print(f"   {i}. {application}")
    
    print(f"\n🚀 Master List Joining for Efficient Data Processing!")
    print("Effective list joining is fundamental to data manipulation and system integration!")