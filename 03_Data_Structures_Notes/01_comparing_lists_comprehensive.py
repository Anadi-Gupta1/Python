"""
List Comparison and Analysis - Comprehensive Python Guide
========================================================

Complete guide to comparing, analyzing, and evaluating Python lists.
Covers equality checks, similarity measures, performance comparisons,
and advanced list analysis techniques for data processing.

Author: Python Learning Notes
Date: September 2025
Topic: List Comparison, Analysis, Performance Evaluation
"""

import time
import sys
import statistics
from typing import List, Any, Tuple, Dict, Optional
import operator
from collections import Counter

# =============================================================================
# FUNDAMENTALS OF LIST COMPARISON
# =============================================================================

def list_comparison_fundamentals():
    """
    Comprehensive guide to list comparison fundamentals
    """
    print("🔍 LIST COMPARISON FUNDAMENTALS")
    print("=" * 33)
    
    print("🎯 What is List Comparison?")
    print("   List comparison involves evaluating relationships between lists")
    print("   including equality, similarity, ordering, and structural analysis.")
    print("   Python provides multiple ways to compare lists effectively.")
    
    print(f"\n📊 Types of List Comparisons:")
    comparison_types = [
        ("Equality", "Check if two lists are identical", "==, !=", "list1 == list2"),
        ("Identity", "Check if two variables reference same list", "is, is not", "list1 is list2"),
        ("Membership", "Check if element exists in list", "in, not in", "item in list1"),
        ("Ordering", "Compare lists lexicographically", "<, >, <=, >=", "list1 < list2"),
        ("Similarity", "Measure how similar two lists are", "Custom functions", "jaccard_similarity()"),
        ("Performance", "Compare execution speed/memory", "Timing functions", "time.perf_counter()")
    ]
    
    print("   Type         │ Purpose                        │ Operators     │ Example")
    print("   ─────────────┼────────────────────────────────┼───────────────┼─────────────────")
    
    for comp_type, purpose, operators, example in comparison_types:
        print(f"   {comp_type:<12} │ {purpose:<30} │ {operators:<13} │ {example}")
    
    return {
        'comparison_types': comparison_types
    }

def equality_and_identity_comparison():
    """
    Detailed demonstration of equality vs identity comparison
    """
    print("\n⚖️ EQUALITY vs IDENTITY COMPARISON")
    print("=" * 36)
    
    # Create test lists
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 5]
    list3 = list1  # Same reference
    list4 = [1, 2, 3, 4, 6]  # Different content
    
    print("📋 Test Lists:")
    print(f"   list1 = {list1}")
    print(f"   list2 = {list2}")
    print(f"   list3 = list1  # Same reference")
    print(f"   list4 = {list4}")
    
    print(f"\n🔍 Equality Comparison (== operator):")
    equality_tests = [
        ("list1 == list2", list1 == list2, "Same content, different objects"),
        ("list1 == list3", list1 == list3, "Same content, same object"),
        ("list1 == list4", list1 == list4, "Different content")
    ]
    
    for test, result, explanation in equality_tests:
        status = "✅" if result else "❌"
        print(f"   {test:<15} → {status} {result:<5} │ {explanation}")
    
    print(f"\n🔗 Identity Comparison (is operator):")
    identity_tests = [
        ("list1 is list2", list1 is list2, "Different objects in memory"),
        ("list1 is list3", list1 is list3, "Same object reference"),
        ("list1 is list4", list1 is list4, "Different objects")
    ]
    
    for test, result, explanation in identity_tests:
        status = "✅" if result else "❌"
        print(f"   {test:<15} → {status} {result:<5} │ {explanation}")
    
    print(f"\n💡 Memory Addresses:")
    print(f"   id(list1) = {id(list1)}")
    print(f"   id(list2) = {id(list2)}")
    print(f"   id(list3) = {id(list3)}")
    
    return {
        'lists': {'list1': list1, 'list2': list2, 'list3': list3, 'list4': list4},
        'equality_results': [result for _, result, _ in equality_tests],
        'identity_results': [result for _, result, _ in identity_tests]
    }

def lexicographic_ordering_comparison():
    """
    Demonstrate lexicographic (dictionary) ordering of lists
    """
    print("\n📖 LEXICOGRAPHIC ORDERING COMPARISON")
    print("=" * 37)
    
    print("🔤 How Lexicographic Comparison Works:")
    print("   1. Compare elements from left to right")
    print("   2. First differing element determines the result")
    print("   3. Shorter list is considered 'less' if it's a prefix")
    
    # Test cases for lexicographic comparison
    test_cases = [
        ([1, 2, 3], [1, 2, 4], "First list < Second (3 < 4)"),
        ([1, 2], [1, 2, 3], "First list < Second (shorter)"),
        ([2, 1], [1, 2], "First list > Second (2 > 1)"),
        (['a', 'b'], ['a', 'c'], "First list < Second ('b' < 'c')"),
        ([1, 2, 3], [1, 2, 3], "Lists are equal"),
        ([1, 2, 3, 4], [1, 2, 3], "First list > Second (longer)")
    ]
    
    print(f"\n📊 Lexicographic Comparison Examples:")
    print("   List 1        │ Operator │ List 2        │ Result │ Explanation")
    print("   ──────────────┼──────────┼───────────────┼────────┼─────────────────────")
    
    for list1, list2, explanation in test_cases:
        # Perform all comparison operations
        results = {
            '<': list1 < list2,
            '<=': list1 <= list2,
            '>': list1 > list2,
            '>=': list1 >= list2,
            '==': list1 == list2,
            '!=': list1 != list2
        }
        
        # Find the primary relationship
        if results['<']:
            primary_op = '<'
        elif results['>']:
            primary_op = '>'
        else:
            primary_op = '=='
        
        list1_str = str(list1)[:12] + ("..." if len(str(list1)) > 12 else "")
        list2_str = str(list2)[:12] + ("..." if len(str(list2)) > 12 else "")
        
        print(f"   {list1_str:<13} │ {primary_op:<8} │ {list2_str:<13} │ {results[primary_op]!s:<6} │ {explanation}")
    
    return {
        'test_cases': test_cases,
        'comparison_rules': [
            "Elements compared left to right",
            "First difference determines result", 
            "Shorter list < longer if prefix"
        ]
    }

def membership_and_containment():
    """
    Demonstrate membership testing and containment operations
    """
    print("\n🎯 MEMBERSHIP AND CONTAINMENT OPERATIONS")
    print("=" * 42)
    
    # Sample data
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    nested_list = [[1, 2], [3, 4], [5, 6], [7, 8]]
    
    print("📋 Test Data:")
    print(f"   numbers = {numbers}")
    print(f"   fruits = {fruits}")
    print(f"   nested_list = {nested_list}")
    
    print(f"\n🔍 Membership Testing (in operator):")
    membership_tests = [
        ("5 in numbers", 5 in numbers),
        ("'apple' in fruits", 'apple' in fruits),
        ("'grape' in fruits", 'grape' in fruits),
        ("[1, 2] in nested_list", [1, 2] in nested_list),
        ("1 in nested_list", 1 in nested_list)  # 1 is not directly in nested_list
    ]
    
    for test_expr, result in membership_tests:
        status = "✅" if result else "❌"
        print(f"   {test_expr:<25} → {status} {result}")
    
    print(f"\n🚫 Negative Membership Testing (not in operator):")
    negative_tests = [
        ("11 not in numbers", 11 not in numbers),
        ("'grape' not in fruits", 'grape' not in fruits),
        ("[9, 10] not in nested_list", [9, 10] not in nested_list)
    ]
    
    for test_expr, result in negative_tests:
        status = "✅" if result else "❌"
        print(f"   {test_expr:<30} → {status} {result}")
    
    # Advanced containment checking
    print(f"\n🔬 Advanced Containment Analysis:")
    
    def check_all_elements_present(list1: List[Any], list2: List[Any]) -> bool:
        """Check if all elements of list1 are present in list2"""
        return all(item in list2 for item in list1)
    
    def check_any_elements_present(list1: List[Any], list2: List[Any]) -> bool:
        """Check if any elements of list1 are present in list2"""
        return any(item in list2 for item in list1)
    
    subset1 = [1, 3, 5]
    subset2 = [15, 20, 25]
    
    print(f"   subset1 = {subset1}")
    print(f"   subset2 = {subset2}")
    print(f"   All elements of subset1 in numbers: {check_all_elements_present(subset1, numbers)}")
    print(f"   Any elements of subset2 in numbers: {check_any_elements_present(subset2, numbers)}")
    
    return {
        'membership_results': membership_tests,
        'negative_results': negative_tests,
        'advanced_containment': {
            'all_present': check_all_elements_present(subset1, numbers),
            'any_present': check_any_elements_present(subset2, numbers)
        }
    }

# =============================================================================
# ADVANCED LIST COMPARISON TECHNIQUES
# =============================================================================

def similarity_measures():
    """
    Advanced similarity measures between lists
    """
    print("\n📊 ADVANCED LIST SIMILARITY MEASURES")
    print("=" * 38)
    
    def jaccard_similarity(list1: List[Any], list2: List[Any]) -> float:
        """Calculate Jaccard similarity coefficient"""
        set1, set2 = set(list1), set(list2)
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        return intersection / union if union > 0 else 0.0
    
    def cosine_similarity(list1: List[float], list2: List[float]) -> float:
        """Calculate cosine similarity for numeric lists"""
        if len(list1) != len(list2):
            return 0.0
        
        dot_product = sum(a * b for a, b in zip(list1, list2))
        norm1 = sum(a * a for a in list1) ** 0.5
        norm2 = sum(b * b for b in list2) ** 0.5
        
        return dot_product / (norm1 * norm2) if norm1 > 0 and norm2 > 0 else 0.0
    
    def overlap_coefficient(list1: List[Any], list2: List[Any]) -> float:
        """Calculate overlap coefficient"""
        set1, set2 = set(list1), set(list2)
        intersection = len(set1.intersection(set2))
        min_size = min(len(set1), len(set2))
        return intersection / min_size if min_size > 0 else 0.0
    
    def dice_coefficient(list1: List[Any], list2: List[Any]) -> float:
        """Calculate Dice coefficient"""
        set1, set2 = set(list1), set(list2)
        intersection = len(set1.intersection(set2))
        return (2 * intersection) / (len(set1) + len(set2)) if (len(set1) + len(set2)) > 0 else 0.0
    
    # Test data
    list_a = [1, 2, 3, 4, 5]
    list_b = [3, 4, 5, 6, 7]
    list_c = [1, 2, 3, 4, 5]  # Identical to list_a
    list_d = [10, 11, 12]     # No overlap
    
    vector1 = [1.0, 2.0, 3.0, 4.0]
    vector2 = [2.0, 3.0, 4.0, 5.0]
    
    print("📋 Test Lists:")
    print(f"   list_a = {list_a}")
    print(f"   list_b = {list_b}")
    print(f"   list_c = {list_c} (identical to list_a)")
    print(f"   list_d = {list_d} (no overlap)")
    print(f"   vector1 = {vector1}")
    print(f"   vector2 = {vector2}")
    
    print(f"\n📈 Similarity Measures:")
    
    similarity_tests = [
        ("Jaccard", jaccard_similarity, [(list_a, list_b), (list_a, list_c), (list_a, list_d)]),
        ("Overlap", overlap_coefficient, [(list_a, list_b), (list_a, list_c), (list_a, list_d)]),
        ("Dice", dice_coefficient, [(list_a, list_b), (list_a, list_c), (list_a, list_d)])
    ]
    
    print("   Measure  │ A vs B │ A vs C │ A vs D │ Interpretation")
    print("   ─────────┼────────┼────────┼────────┼─────────────────────────")
    
    for measure_name, measure_func, test_pairs in similarity_tests:
        results = [measure_func(pair[0], pair[1]) for pair in test_pairs]
        interpretation = f"Range [0,1]: 0=no similarity, 1=identical"
        print(f"   {measure_name:<8} │ {results[0]:.3f}  │ {results[1]:.3f}  │ {results[2]:.3f}  │ {interpretation}")
    
    # Cosine similarity for numeric vectors
    cosine_sim = cosine_similarity(vector1, vector2)
    print(f"\n🧮 Cosine Similarity (numeric vectors):")
    print(f"   vector1 vs vector2: {cosine_sim:.3f}")
    print(f"   Interpretation: {cosine_sim:.3f} indicates {'high' if cosine_sim > 0.8 else 'moderate' if cosine_sim > 0.5 else 'low'} similarity")
    
    return {
        'similarity_functions': [jaccard_similarity, overlap_coefficient, dice_coefficient, cosine_similarity],
        'test_results': {
            'jaccard': [jaccard_similarity(list_a, list_b), jaccard_similarity(list_a, list_c), jaccard_similarity(list_a, list_d)],
            'cosine': cosine_sim
        }
    }

def performance_comparison():
    """
    Performance comparison of different list operations
    """
    print("\n⚡ PERFORMANCE COMPARISON OF LIST OPERATIONS")
    print("=" * 45)
    
    def time_operation(operation_func, *args, iterations=1000):
        """Time a list operation"""
        start_time = time.perf_counter()
        for _ in range(iterations):
            result = operation_func(*args)
        end_time = time.perf_counter()
        return (end_time - start_time) * 1000 / iterations  # ms per operation
    
    # Test data of different sizes
    small_list = list(range(100))
    medium_list = list(range(1000))
    large_list = list(range(10000))
    
    test_lists = [
        ("Small (100)", small_list),
        ("Medium (1K)", medium_list), 
        ("Large (10K)", large_list)
    ]
    
    print("📊 Operation Performance Comparison:")
    print("   Operation      │ Small (100) │ Medium (1K) │ Large (10K) │ Complexity")
    print("   ───────────────┼─────────────┼─────────────┼─────────────┼───────────")
    
    # Define operations to test
    operations = [
        ("List Creation", lambda n: list(range(n)), "O(n)"),
        ("Append Item", lambda lst: lst + [999], "O(n)"),
        ("Index Access", lambda lst: lst[len(lst)//2], "O(1)"),
        ("Linear Search", lambda lst: 999 in lst, "O(n)"),
        ("List Copy", lambda lst: lst.copy(), "O(n)"),
        ("List Reverse", lambda lst: lst[::-1], "O(n)")
    ]
    
    for op_name, op_func, complexity in operations:
        times = []
        
        for size_name, test_list in test_lists:
            if op_name == "List Creation":
                # Special case for creation - pass size instead of list
                op_time = time_operation(op_func, len(test_list), iterations=100)
            else:
                op_time = time_operation(op_func, test_list.copy(), iterations=100)
            times.append(op_time)
        
        print(f"   {op_name:<14} │ {times[0]:9.4f} ms │ {times[1]:9.4f} ms │ {times[2]:9.4f} ms │ {complexity}")
    
    # Memory usage comparison
    print(f"\n💾 Memory Usage Analysis:")
    
    def get_list_memory_usage(lst):
        """Get approximate memory usage of a list"""
        return sys.getsizeof(lst) + sum(sys.getsizeof(item) for item in lst)
    
    for size_name, test_list in test_lists:
        memory_kb = get_list_memory_usage(test_list) / 1024
        print(f"   {size_name}: {memory_kb:.2f} KB")
    
    return {
        'performance_data': {
            'operations': operations,
            'test_sizes': [len(lst) for _, lst in test_lists]
        }
    }

def statistical_comparison():
    """
    Statistical analysis and comparison of lists
    """
    print("\n📈 STATISTICAL LIST COMPARISON")
    print("=" * 32)
    
    # Sample datasets for comparison
    dataset1 = [85, 90, 78, 92, 88, 75, 95, 82, 89, 91]  # Test scores class A
    dataset2 = [80, 85, 77, 87, 83, 79, 90, 84, 86, 88]  # Test scores class B
    dataset3 = [70, 95, 60, 100, 65, 85, 75, 90, 80, 85] # More varied scores
    
    print("📊 Sample Datasets (Test Scores):")
    print(f"   Class A: {dataset1}")
    print(f"   Class B: {dataset2}")
    print(f"   Class C: {dataset3}")
    
    def calculate_statistics(data: List[float]) -> Dict[str, float]:
        """Calculate comprehensive statistics for a dataset"""
        return {
            'mean': statistics.mean(data),
            'median': statistics.median(data),
            'mode': statistics.mode(data) if len(set(data)) < len(data) else None,
            'std_dev': statistics.stdev(data) if len(data) > 1 else 0,
            'variance': statistics.variance(data) if len(data) > 1 else 0,
            'min': min(data),
            'max': max(data),
            'range': max(data) - min(data)
        }
    
    # Calculate statistics for each dataset
    stats = {
        'Class A': calculate_statistics(dataset1),
        'Class B': calculate_statistics(dataset2),
        'Class C': calculate_statistics(dataset3)
    }
    
    print(f"\n📊 Statistical Summary:")
    print("   Statistic    │ Class A │ Class B │ Class C │ Interpretation")
    print("   ─────────────┼─────────┼─────────┼─────────┼──────────────────────")
    
    stat_names = ['mean', 'median', 'std_dev', 'variance', 'range']
    
    for stat in stat_names:
        a_val = stats['Class A'][stat]
        b_val = stats['Class B'][stat]
        c_val = stats['Class C'][stat]
        
        # Interpretation based on statistic
        if stat == 'mean':
            interpretation = f"A>B: Class A avg higher"
        elif stat == 'std_dev':
            interpretation = f"C highest: More variation"
        elif stat == 'range':
            interpretation = f"C widest: Most spread"
        else:
            interpretation = "Central tendency measure"
        
        print(f"   {stat.title():<12} │ {a_val:7.1f} │ {b_val:7.1f} │ {c_val:7.1f} │ {interpretation}")
    
    # Distribution analysis
    print(f"\n📊 Distribution Analysis:")
    
    def analyze_distribution(data: List[float], name: str) -> str:
        """Analyze the distribution characteristics"""
        mean_val = statistics.mean(data)
        median_val = statistics.median(data)
        std_val = statistics.stdev(data) if len(data) > 1 else 0
        
        # Check for skewness (simplified)
        if abs(mean_val - median_val) < std_val * 0.1:
            skewness = "Nearly Normal"
        elif mean_val > median_val:
            skewness = "Right-skewed"
        else:
            skewness = "Left-skewed"
        
        # Variability assessment
        cv = (std_val / mean_val) * 100 if mean_val != 0 else 0
        if cv < 10:
            variability = "Low variability"
        elif cv < 25:
            variability = "Moderate variability"
        else:
            variability = "High variability"
        
        return f"{skewness}, {variability} (CV: {cv:.1f}%)"
    
    for class_name, data in [('Class A', dataset1), ('Class B', dataset2), ('Class C', dataset3)]:
        analysis = analyze_distribution(data, class_name)
        print(f"   {class_name}: {analysis}")
    
    return {
        'datasets': {'A': dataset1, 'B': dataset2, 'C': dataset3},
        'statistics': stats,
        'distribution_analysis': [analyze_distribution(dataset1, 'A'), analyze_distribution(dataset2, 'B'), analyze_distribution(dataset3, 'C')]
    }

# =============================================================================
# MAIN EXECUTION AND COMPREHENSIVE DEMONSTRATION
# =============================================================================

def main():
    """
    Main function executing comprehensive list comparison guide
    """
    print(__doc__)
    
    # Core comparison fundamentals
    fundamentals = list_comparison_fundamentals()
    
    # Different types of comparisons
    equality_identity = equality_and_identity_comparison()
    lexicographic = lexicographic_ordering_comparison()
    membership = membership_and_containment()
    
    # Advanced techniques
    similarity = similarity_measures()
    performance = performance_comparison()
    statistics_analysis = statistical_comparison()
    
    return {
        'fundamentals': fundamentals,
        'equality_identity': equality_identity,
        'lexicographic': lexicographic,
        'membership': membership,
        'similarity': similarity,
        'performance': performance,
        'statistics': statistics_analysis
    }

if __name__ == "__main__":
    """
    Execute comprehensive list comparison and analysis guide
    """
    results = main()
    
    print("\n" + "=" * 70)
    print("🎓 LIST COMPARISON & ANALYSIS MASTERY SUMMARY")
    print("=" * 70)
    print("✅ Complete understanding of list comparison fundamentals")
    print("✅ Equality vs identity comparison mastery")
    print("✅ Lexicographic ordering and membership testing")
    print("✅ Advanced similarity measures and statistical analysis")
    print("✅ Performance comparison and optimization insights")
    print("✅ Real-world applications of list analysis techniques")
    print("✅ Statistical methods for data comparison and evaluation")
    
    print("\n💡 List Comparison Mastery Key Points:")
    key_points = [
        "Use == for content equality, 'is' for object identity",
        "Lexicographic comparison follows dictionary ordering rules",
        "Membership testing with 'in' is O(n) for lists, O(1) for sets",
        "Similarity measures quantify relationships between datasets",
        "Performance varies significantly with list size and operation type",
        "Statistical analysis reveals patterns and distributions in data",
        "Choose appropriate comparison method based on use case",
        "Consider converting to sets for faster membership testing"
    ]
    
    for point in key_points:
        print(f"   • {point}")
    
    print("\n🎯 Advanced Applications:")
    applications = [
        "Data deduplication and similarity detection",
        "Performance benchmarking and optimization",
        "Statistical analysis and data science applications",
        "Machine learning feature comparison",
        "Database query optimization",
        "Recommendation system similarity calculations",
        "Version control and difference analysis",
        "Quality assurance and testing frameworks"
    ]
    
    for i, application in enumerate(applications, 1):
        print(f"   {i}. {application}")
    
    print(f"\n🚀 Master List Comparison for Data Analysis Excellence!")
    print("Effective list comparison skills are essential for data processing and analysis!")