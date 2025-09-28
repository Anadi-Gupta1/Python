"""
List Testing and Validation - Complete Python Guide
==================================================

Comprehensive guide to testing, validating, debugging, and quality assurance
for Python list operations. Master systematic approaches to ensure
robust list manipulations and data integrity.

Author: Python Learning Notes
Date: September 2025
Topic: List Testing, Validation, Quality Assurance, Debugging
"""

import unittest
import doctest
import time
import sys
import random
import traceback
from typing import List, Any, Union, Optional, Callable, Tuple, Dict
from collections import defaultdict
import copy
import json

# =============================================================================
# FUNDAMENTALS OF LIST TESTING AND VALIDATION
# =============================================================================

def list_testing_fundamentals():
    """
    Understanding the fundamentals of list testing and validation
    """
    print("🧪 LIST TESTING AND VALIDATION FUNDAMENTALS")
    print("=" * 45)
    
    print("🎯 What is List Testing?")
    print("   List testing involves verifying that list operations behave")
    print("   correctly under various conditions, handle edge cases properly,")
    print("   and maintain data integrity throughout manipulations.")
    
    print(f"\n📋 Types of List Testing:")
    testing_types = [
        ("Unit Testing", "Test individual list operations", "unittest.TestCase", "Isolated function testing"),
        ("Integration Testing", "Test list interactions", "Complex workflows", "Multi-operation sequences"),
        ("Property Testing", "Test invariant properties", "Hypothesis framework", "Random input generation"),
        ("Performance Testing", "Test operation speed", "timeit, benchmarking", "Scalability validation"),
        ("Boundary Testing", "Test edge cases", "Empty lists, single items", "Robustness validation"),
        ("Mutation Testing", "Test list modifications", "In-place operations", "State change validation"),
        ("Memory Testing", "Test memory usage", "Large datasets", "Resource management")
    ]
    
    print("   Type                │ Purpose                      │ Tools/Approach           │ Focus Area")
    print("   ────────────────────┼──────────────────────────────┼──────────────────────────┼─────────────────")
    
    for test_type, purpose, tools, focus in testing_types:
        print(f"   {test_type:<19} │ {purpose:<28} │ {tools:<24} │ {focus}")
    
    print(f"\n🔍 Key Testing Principles:")
    print("   • Test early and test often during development")
    print("   • Cover normal cases, edge cases, and error conditions")
    print("   • Validate both input and output constraints")
    print("   • Test performance characteristics and scalability")
    print("   • Ensure thread safety for concurrent operations")
    print("   • Validate memory management and resource cleanup")
    
    return {'testing_types': testing_types}

def validation_strategies():
    """
    Comprehensive validation strategies for list operations
    """
    print("\n✅ VALIDATION STRATEGIES FOR LIST OPERATIONS")
    print("=" * 44)
    
    # 1. TYPE VALIDATION
    print("1️⃣ Type Validation:")
    
    def validate_list_type(data: Any, expected_element_type: type = None) -> dict:
        """Comprehensive list type validation"""
        validation_result = {
            'is_list': isinstance(data, list),
            'is_empty': False,
            'length': 0,
            'element_types': set(),
            'homogeneous': True,
            'type_violations': [],
            'valid': True,
            'errors': []
        }
        
        # Basic list type check
        if not validation_result['is_list']:
            validation_result['valid'] = False
            validation_result['errors'].append(f"Expected list, got {type(data).__name__}")
            return validation_result
        
        # List properties
        validation_result['length'] = len(data)
        validation_result['is_empty'] = len(data) == 0
        
        if validation_result['is_empty']:
            return validation_result
        
        # Element type analysis
        for i, element in enumerate(data):
            element_type = type(element)
            validation_result['element_types'].add(element_type)
            
            # Check against expected type
            if expected_element_type and not isinstance(element, expected_element_type):
                validation_result['type_violations'].append((i, element, element_type))
                validation_result['valid'] = False
        
        # Homogeneity check
        validation_result['homogeneous'] = len(validation_result['element_types']) == 1
        
        if validation_result['type_violations']:
            validation_result['errors'].append(f"Found {len(validation_result['type_violations'])} type violations")
        
        return validation_result
    
    # Test type validation
    test_data = [
        ([1, 2, 3, 4, 5], int, "homogeneous integer list"),
        ([1, "hello", 3.14], None, "mixed type list"),
        ([], str, "empty list"),
        ("not a list", int, "invalid input type"),
        ([1, 2, "three", 4], int, "type violation case")
    ]
    
    print("   Type validation examples:")
    for data, expected_type, description in test_data[:3]:  # Show first 3
        result = validate_list_type(data, expected_type)
        print(f"     {description}: Valid={result['valid']}, Length={result['length']}")
        if result['errors']:
            print(f"       Errors: {result['errors']}")
    
    # 2. RANGE AND BOUNDARY VALIDATION
    print(f"\n2️⃣ Range and Boundary Validation:")
    
    def validate_list_ranges(data: List[Union[int, float]], 
                           min_val: Optional[float] = None,
                           max_val: Optional[float] = None,
                           min_length: int = 0,
                           max_length: Optional[int] = None) -> dict:
        """Validate list values are within acceptable ranges"""
        validation_result = {
            'valid': True,
            'length_valid': True,
            'value_violations': [],
            'length_violations': [],
            'statistics': {},
            'errors': []
        }
        
        # Length validation
        list_length = len(data)
        if list_length < min_length:
            validation_result['length_valid'] = False
            validation_result['length_violations'].append(f"Length {list_length} < minimum {min_length}")
            validation_result['valid'] = False
        
        if max_length is not None and list_length > max_length:
            validation_result['length_valid'] = False
            validation_result['length_violations'].append(f"Length {list_length} > maximum {max_length}")
            validation_result['valid'] = False
        
        # Value validation
        if data and all(isinstance(x, (int, float)) for x in data):
            validation_result['statistics'] = {
                'min': min(data),
                'max': max(data),
                'avg': sum(data) / len(data)
            }
            
            # Check value ranges
            for i, value in enumerate(data):
                if min_val is not None and value < min_val:
                    validation_result['value_violations'].append((i, value, f"< {min_val}"))
                    validation_result['valid'] = False
                
                if max_val is not None and value > max_val:
                    validation_result['value_violations'].append((i, value, f"> {max_val}"))
                    validation_result['valid'] = False
        
        return validation_result
    
    # Test range validation
    scores = [85, 92, 78, 96, 88, 91]
    temperature_readings = [-5.2, 23.7, 31.8, 29.3, 22.1]
    
    score_validation = validate_list_ranges(scores, min_val=0, max_val=100, min_length=1, max_length=50)
    temp_validation = validate_list_ranges(temperature_readings, min_val=-10, max_val=40)
    
    print("   Range validation examples:")
    print(f"     Scores validation: Valid={score_validation['valid']}")
    print(f"       Statistics: {score_validation['statistics']}")
    print(f"     Temperature validation: Valid={temp_validation['valid']}")
    print(f"       Statistics: {temp_validation['statistics']}")
    
    # 3. STRUCTURAL VALIDATION
    print(f"\n3️⃣ Structural Validation:")
    
    def validate_list_structure(data: List[Any], expected_structure: dict) -> dict:
        """Validate complex list structures"""
        validation_result = {
            'valid': True,
            'structure_violations': [],
            'pattern_matches': True,
            'errors': []
        }
        
        # Required keys validation
        required_keys = expected_structure.get('required_keys', [])
        if required_keys and data and isinstance(data[0], dict):
            for i, item in enumerate(data):
                if not isinstance(item, dict):
                    validation_result['structure_violations'].append(
                        (i, f"Expected dict, got {type(item).__name__}")
                    )
                    validation_result['valid'] = False
                    continue
                
                missing_keys = set(required_keys) - set(item.keys())
                if missing_keys:
                    validation_result['structure_violations'].append(
                        (i, f"Missing keys: {missing_keys}")
                    )
                    validation_result['valid'] = False
        
        # Pattern validation
        expected_pattern = expected_structure.get('pattern')
        if expected_pattern and data:
            pattern_length = len(expected_pattern)
            for i, item in enumerate(data):
                expected_type = expected_pattern[i % pattern_length]
                if not isinstance(item, expected_type):
                    validation_result['pattern_matches'] = False
                    validation_result['structure_violations'].append(
                        (i, f"Pattern violation: expected {expected_type.__name__}, got {type(item).__name__}")
                    )
                    validation_result['valid'] = False
        
        return validation_result
    
    # Test structural validation
    user_data = [
        {'name': 'Alice', 'age': 25, 'email': 'alice@example.com'},
        {'name': 'Bob', 'age': 30, 'email': 'bob@example.com'},
        {'name': 'Charlie', 'age': 35}  # Missing email
    ]
    
    structure_spec = {
        'required_keys': ['name', 'age', 'email'],
        'pattern': [dict]
    }
    
    struct_validation = validate_list_structure(user_data, structure_spec)
    print("   Structural validation example:")
    print(f"     User data validation: Valid={struct_validation['valid']}")
    if struct_validation['structure_violations']:
        print(f"     Violations: {len(struct_validation['structure_violations'])}")
    
    return {
        'type_validation': validate_list_type,
        'range_validation': validate_list_ranges,
        'structure_validation': validate_list_structure
    }

def unit_testing_framework():
    """
    Comprehensive unit testing framework for list operations
    """
    print("\n🧪 UNIT TESTING FRAMEWORK FOR LIST OPERATIONS")
    print("=" * 43)
    
    class ListOperationTests(unittest.TestCase):
        """Comprehensive unit tests for list operations"""
        
        def setUp(self):
            """Set up test fixtures"""
            self.sample_list = [1, 2, 3, 4, 5]
            self.empty_list = []
            self.string_list = ['apple', 'banana', 'cherry']
            self.mixed_list = [1, 'hello', 3.14, True]
            self.nested_list = [[1, 2], [3, 4], [5, 6]]
            
        def test_list_append(self):
            """Test list append operation"""
            original_length = len(self.sample_list)
            self.sample_list.append(6)
            
            self.assertEqual(len(self.sample_list), original_length + 1)
            self.assertEqual(self.sample_list[-1], 6)
            
        def test_list_extend(self):
            """Test list extend operation"""
            original_list = self.sample_list.copy()
            extension = [6, 7, 8]
            original_list.extend(extension)
            
            expected = self.sample_list + extension
            self.assertEqual(original_list, expected)
            
        def test_list_insert(self):
            """Test list insert operation"""
            test_list = self.sample_list.copy()
            test_list.insert(2, 99)
            
            self.assertEqual(test_list[2], 99)
            self.assertEqual(len(test_list), len(self.sample_list) + 1)
            
        def test_list_remove(self):
            """Test list remove operation"""
            test_list = self.sample_list.copy()
            test_list.remove(3)
            
            self.assertNotIn(3, test_list)
            self.assertEqual(len(test_list), len(self.sample_list) - 1)
            
        def test_list_pop(self):
            """Test list pop operation"""
            test_list = self.sample_list.copy()
            popped = test_list.pop()
            
            self.assertEqual(popped, 5)
            self.assertEqual(len(test_list), len(self.sample_list) - 1)
            
        def test_list_indexing(self):
            """Test list indexing operations"""
            # Positive indexing
            self.assertEqual(self.sample_list[0], 1)
            self.assertEqual(self.sample_list[2], 3)
            
            # Negative indexing
            self.assertEqual(self.sample_list[-1], 5)
            self.assertEqual(self.sample_list[-2], 4)
            
        def test_list_slicing(self):
            """Test list slicing operations"""
            # Basic slicing
            self.assertEqual(self.sample_list[1:4], [2, 3, 4])
            self.assertEqual(self.sample_list[:3], [1, 2, 3])
            self.assertEqual(self.sample_list[2:], [3, 4, 5])
            
            # Step slicing
            self.assertEqual(self.sample_list[::2], [1, 3, 5])
            self.assertEqual(self.sample_list[::-1], [5, 4, 3, 2, 1])
            
        def test_empty_list_operations(self):
            """Test operations on empty lists"""
            self.assertEqual(len(self.empty_list), 0)
            self.assertFalse(self.empty_list)
            
            # Test that operations on empty list work correctly
            self.empty_list.append(1)
            self.assertEqual(len(self.empty_list), 1)
            
        def test_list_membership(self):
            """Test membership operations"""
            self.assertIn(3, self.sample_list)
            self.assertNotIn(10, self.sample_list)
            
        def test_list_comprehensions(self):
            """Test list comprehension results"""
            squares = [x**2 for x in self.sample_list]
            expected_squares = [1, 4, 9, 16, 25]
            self.assertEqual(squares, expected_squares)
            
            # Filtered comprehension
            evens = [x for x in self.sample_list if x % 2 == 0]
            self.assertEqual(evens, [2, 4])
    
    # 2. PROPERTY-BASED TESTING
    print("1️⃣ Unit Testing Framework:")
    print("   Comprehensive TestCase class created with methods:")
    
    test_methods = [
        "test_list_append", "test_list_extend", "test_list_insert",
        "test_list_remove", "test_list_pop", "test_list_indexing",
        "test_list_slicing", "test_empty_list_operations",
        "test_list_membership", "test_list_comprehensions"
    ]
    
    for method in test_methods:
        print(f"     • {method}")
    
    # 3. CUSTOM TEST RUNNERS
    print(f"\n2️⃣ Custom Test Execution:")
    
    def run_list_tests():
        """Run comprehensive list operation tests"""
        # Create test suite
        test_suite = unittest.TestLoader().loadTestsFromTestCase(ListOperationTests)
        
        # Custom test runner with detailed output
        class DetailedTestResult(unittest.TextTestResult):
            def addSuccess(self, test):
                super().addSuccess(test)
                print(f"     ✅ {test._testMethodName}")
                
            def addError(self, test, err):
                super().addError(test, err)
                print(f"     ❌ {test._testMethodName} - ERROR")
                
            def addFailure(self, test, err):
                super().addFailure(test, err)
                print(f"     ❌ {test._testMethodName} - FAILED")
        
        # Run tests with custom result handler
        runner = unittest.TextTestRunner(resultclass=DetailedTestResult, verbosity=0)
        result = runner.run(test_suite)
        
        return {
            'tests_run': result.testsRun,
            'failures': len(result.failures),
            'errors': len(result.errors),
            'success_rate': ((result.testsRun - len(result.failures) - len(result.errors)) 
                           / result.testsRun * 100) if result.testsRun > 0 else 0
        }
    
    # Execute tests
    print("   Running comprehensive list operation tests:")
    test_results = run_list_tests()
    print(f"\n   Test Results Summary:")
    print(f"     Tests executed: {test_results['tests_run']}")
    print(f"     Failures: {test_results['failures']}")
    print(f"     Errors: {test_results['errors']}")
    print(f"     Success rate: {test_results['success_rate']:.1f}%")
    
    return {
        'test_case_class': ListOperationTests,
        'test_results': test_results,
        'test_methods': test_methods
    }

def error_handling_testing():
    """
    Comprehensive error handling and exception testing
    """
    print("\n🚨 ERROR HANDLING AND EXCEPTION TESTING")
    print("=" * 39)
    
    # 1. EXCEPTION TESTING FRAMEWORK
    print("1️⃣ Exception Testing Framework:")
    
    def test_list_exceptions():
        """Test various exception conditions with lists"""
        test_results = {
            'index_errors': [],
            'value_errors': [],
            'type_errors': [],
            'attribute_errors': [],
            'total_tests': 0,
            'passed_tests': 0
        }
        
        test_list = [1, 2, 3, 4, 5]
        
        # Test IndexError conditions
        index_error_tests = [
            (lambda: test_list[10], "Positive index out of range"),
            (lambda: test_list[-10], "Negative index out of range"),
            (lambda: [].pop(), "Pop from empty list"),
            (lambda: [][0], "Index empty list")
        ]
        
        for test_func, description in index_error_tests:
            test_results['total_tests'] += 1
            try:
                test_func()
                test_results['index_errors'].append((description, "FAILED - No exception raised"))
            except IndexError as e:
                test_results['index_errors'].append((description, f"PASSED - {str(e)}"))
                test_results['passed_tests'] += 1
            except Exception as e:
                test_results['index_errors'].append((description, f"FAILED - Wrong exception: {type(e).__name__}"))
        
        # Test ValueError conditions
        value_error_tests = [
            (lambda: test_list.remove(99), "Remove non-existent element"),
            (lambda: test_list.index(99), "Find index of non-existent element")
        ]
        
        for test_func, description in value_error_tests:
            test_results['total_tests'] += 1
            try:
                test_func()
                test_results['value_errors'].append((description, "FAILED - No exception raised"))
            except ValueError as e:
                test_results['value_errors'].append((description, f"PASSED - {str(e)}"))
                test_results['passed_tests'] += 1
            except Exception as e:
                test_results['value_errors'].append((description, f"FAILED - Wrong exception: {type(e).__name__}"))
        
        # Test TypeError conditions
        type_error_tests = [
            (lambda: test_list + "string", "Concatenate list with non-list"),
            (lambda: test_list[1.5], "Use float as index"),
            (lambda: [1, 2, 3].sort(key="invalid"), "Invalid sort key")
        ]
        
        for test_func, description in type_error_tests:
            test_results['total_tests'] += 1
            try:
                test_func()
                test_results['type_errors'].append((description, "FAILED - No exception raised"))
            except TypeError as e:
                test_results['type_errors'].append((description, f"PASSED - {str(e)[:50]}..."))
                test_results['passed_tests'] += 1
            except Exception as e:
                test_results['type_errors'].append((description, f"FAILED - Wrong exception: {type(e).__name__}"))
        
        return test_results
    
    exception_results = test_list_exceptions()
    
    print("   Exception test results:")
    print(f"     Total tests: {exception_results['total_tests']}")
    print(f"     Passed: {exception_results['passed_tests']}")
    print(f"     Success rate: {exception_results['passed_tests']/exception_results['total_tests']*100:.1f}%")
    
    print("   IndexError tests:")
    for description, result in exception_results['index_errors'][:2]:  # Show first 2
        print(f"     • {description}: {result}")
    
    # 2. DEFENSIVE PROGRAMMING PATTERNS
    print(f"\n2️⃣ Defensive Programming Patterns:")
    
    def safe_list_operations():
        """Demonstrate safe list operation patterns"""
        patterns = []
        
        # Safe indexing with bounds checking
        def safe_get(lst: List[Any], index: int, default: Any = None) -> Any:
            """Safely get list element with bounds checking"""
            try:
                return lst[index] if -len(lst) <= index < len(lst) else default
            except (IndexError, TypeError):
                return default
        
        # Safe list modification
        def safe_remove(lst: List[Any], item: Any) -> bool:
            """Safely remove item from list, return success status"""
            try:
                lst.remove(item)
                return True
            except ValueError:
                return False
        
        # Safe list extension
        def safe_extend(lst: List[Any], items: Any) -> bool:
            """Safely extend list with items"""
            try:
                if hasattr(items, '__iter__') and not isinstance(items, (str, bytes)):
                    lst.extend(items)
                    return True
                else:
                    return False
            except (TypeError, AttributeError):
                return False
        
        # Test safe operations
        test_list = [1, 2, 3, 4, 5]
        
        patterns.append(("Safe indexing", safe_get(test_list, 10, "Not found")))
        patterns.append(("Safe removal success", safe_remove(test_list.copy(), 3)))
        patterns.append(("Safe removal failure", safe_remove(test_list.copy(), 99)))
        patterns.append(("Safe extension", safe_extend(test_list.copy(), [6, 7, 8])))
        
        return patterns
    
    safe_patterns = safe_list_operations()
    
    print("   Safe operation patterns:")
    for pattern_name, result in safe_patterns:
        print(f"     • {pattern_name}: {result}")
    
    # 3. ERROR RECOVERY STRATEGIES
    print(f"\n3️⃣ Error Recovery Strategies:")
    
    def robust_list_processor(data: Any) -> dict:
        """Process data with comprehensive error recovery"""
        result = {
            'processed': [],
            'errors': [],
            'warnings': [],
            'success': False
        }
        
        # Input validation
        if not isinstance(data, list):
            try:
                data = list(data) if hasattr(data, '__iter__') else [data]
                result['warnings'].append("Input converted to list")
            except (TypeError, ValueError) as e:
                result['errors'].append(f"Cannot convert input to list: {e}")
                return result
        
        # Process each element with error handling
        for i, item in enumerate(data):
            try:
                # Attempt to process (example: convert to number and square)
                if isinstance(item, (int, float)):
                    processed_item = item ** 2
                elif isinstance(item, str) and item.isdigit():
                    processed_item = int(item) ** 2
                    result['warnings'].append(f"String '{item}' converted to number")
                else:
                    result['warnings'].append(f"Skipped non-numeric item at index {i}: {item}")
                    continue
                
                result['processed'].append(processed_item)
                
            except Exception as e:
                result['errors'].append(f"Error processing item {i}: {e}")
        
        result['success'] = len(result['processed']) > 0
        return result
    
    # Test error recovery
    test_inputs = [
        [1, 2, 3, 4, 5],  # Normal case
        [1, "2", 3.5, "invalid", 5],  # Mixed valid/invalid
        "12345",  # String that needs conversion
        None  # Invalid input
    ]
    
    print("   Error recovery examples:")
    for i, test_input in enumerate(test_inputs):
        result = robust_list_processor(test_input)
        print(f"     Test {i+1}: Success={result['success']}, "
              f"Processed={len(result['processed'])}, "
              f"Errors={len(result['errors'])}, "
              f"Warnings={len(result['warnings'])}")
    
    return {
        'exception_testing': exception_results,
        'safe_patterns': safe_patterns,
        'error_recovery': robust_list_processor
    }

def performance_testing_framework():
    """
    Performance testing and benchmarking framework for list operations
    """
    print("\n⚡ PERFORMANCE TESTING FRAMEWORK")
    print("=" * 33)
    
    # 1. OPERATION BENCHMARKING
    print("1️⃣ Operation Benchmarking:")
    
    def benchmark_list_operations():
        """Benchmark common list operations"""
        import timeit
        
        # Setup code for different list sizes
        sizes = [100, 1000, 10000]
        operations = {
            'append': 'lst.append(1)',
            'prepend': 'lst.insert(0, 1)',
            'extend': 'lst.extend([1, 2, 3])',
            'pop_end': 'lst.pop() if lst else None',
            'pop_start': 'lst.pop(0) if lst else None',
            'index_access': 'lst[len(lst)//2] if lst else None',
            'slice_copy': 'lst[:]',
            'list_comp': '[x*2 for x in lst]'
        }
        
        results = {}
        
        for size in sizes:
            results[size] = {}
            setup_code = f"lst = list(range({size}))"
            
            for op_name, op_code in operations.items():
                try:
                    # Use a fresh list for each operation
                    full_code = f"{setup_code}; {op_code}"
                    time_taken = timeit.timeit(full_code, number=1000)
                    results[size][op_name] = time_taken * 1000  # Convert to ms
                except Exception as e:
                    results[size][op_name] = float('inf')
        
        return results
    
    benchmark_results = benchmark_list_operations()
    
    print("   Performance benchmarks (average time in ms for 1000 operations):")
    print("   Operation        │    100 items │   1K items │  10K items")
    print("   ─────────────────┼──────────────┼────────────┼────────────")
    
    for op_name in ['append', 'prepend', 'extend', 'pop_end']:
        times = [f"{benchmark_results[size][op_name]:10.4f}" if benchmark_results[size][op_name] != float('inf') 
                else "       N/A" for size in [100, 1000, 10000]]
        print(f"   {op_name:<16} │ {times[0]} ms │ {times[1]} ms │ {times[2]} ms")
    
    # 2. MEMORY PROFILING
    print(f"\n2️⃣ Memory Usage Analysis:")
    
    def analyze_memory_usage():
        """Analyze memory usage patterns"""
        import sys
        
        memory_tests = []
        
        # Different list creation methods
        methods = [
            ("List literal", lambda n: [0] * n),
            ("List comprehension", lambda n: [0 for _ in range(n)]),
            ("List constructor", lambda n: list([0] * n)),
            ("Append loop", lambda n: [lst.append(0) for lst in [[]] for _ in range(n)][0])
        ]
        
        test_size = 1000
        
        for method_name, method_func in methods[:3]:  # Test first 3 methods
            try:
                test_list = method_func(test_size)
                memory_size = sys.getsizeof(test_list)
                memory_tests.append((method_name, memory_size, len(test_list)))
            except:
                memory_tests.append((method_name, 0, 0))
        
        return memory_tests
    
    memory_analysis = analyze_memory_usage()
    
    print("   Memory usage for 1000-element lists:")
    print("   Method               │ Memory (bytes) │ Elements")
    print("   ─────────────────────┼────────────────┼─────────")
    for method, memory, elements in memory_analysis:
        print(f"   {method:<20} │ {memory:12,} B │ {elements:7}")
    
    # 3. SCALABILITY TESTING
    print(f"\n3️⃣ Scalability Analysis:")
    
    def test_operation_scalability():
        """Test how operations scale with list size"""
        sizes = [10, 100, 1000, 10000]
        
        def time_operation(operation_func, size, iterations=100):
            """Time a specific operation"""
            start_time = time.perf_counter()
            for _ in range(iterations):
                test_list = list(range(size))
                operation_func(test_list)
            end_time = time.perf_counter()
            return (end_time - start_time) * 1000 / iterations  # ms per operation
        
        operations = {
            'linear_search': lambda lst: 999999 in lst,  # Worst case
            'list_reversal': lambda lst: lst[::-1],
            'list_sorting': lambda lst: sorted(lst),
            'list_copy': lambda lst: lst.copy()
        }
        
        scalability_results = {}
        for op_name, op_func in operations.items():
            scalability_results[op_name] = []
            for size in sizes:
                if size <= 1000 or op_name != 'list_sorting':  # Skip large sort tests
                    time_ms = time_operation(op_func, size)
                    scalability_results[op_name].append(time_ms)
                else:
                    scalability_results[op_name].append(None)
        
        return scalability_results
    
    scalability_data = test_operation_scalability()
    
    print("   Scalability analysis (time in ms):")
    print("   Operation      │    10 items │   100 items │  1K items │ 10K items")
    print("   ───────────────┼─────────────┼─────────────┼───────────┼──────────")
    
    for op_name, times in scalability_data.items():
        time_strs = []
        for time_val in times:
            if time_val is not None:
                time_strs.append(f"{time_val:9.4f}")
            else:
                time_strs.append("     N/A")
        
        print(f"   {op_name:<14} │ {time_strs[0]} ms │ {time_strs[1]} ms │ {time_strs[2]} ms │ {time_strs[3]} ms")
    
    return {
        'benchmark_results': benchmark_results,
        'memory_analysis': memory_analysis,
        'scalability_data': scalability_data
    }

def comprehensive_test_suite():
    """
    Comprehensive test suite combining all testing approaches
    """
    print("\n🎯 COMPREHENSIVE TEST SUITE EXECUTION")
    print("=" * 37)
    
    # 1. INTEGRATION TEST SCENARIOS
    print("1️⃣ Integration Test Scenarios:")
    
    def test_data_processing_pipeline():
        """Test complete data processing pipeline"""
        test_results = {
            'pipeline_tests': [],
            'total_tests': 0,
            'passed_tests': 0
        }
        
        # Test scenario 1: Data cleaning pipeline
        raw_data = [1, "2", 3.5, None, "invalid", 5, "", 7.2, "8"]
        expected_clean = [1, 2, 3.5, 5, 7.2, 8]
        
        def clean_data_pipeline(data):
            """Clean and process data pipeline"""
            cleaned = []
            for item in data:
                try:
                    if item is None or item == "":
                        continue
                    if isinstance(item, str):
                        if item.replace(".", "").isdigit():
                            cleaned.append(float(item) if "." in item else int(item))
                    elif isinstance(item, (int, float)):
                        cleaned.append(item)
                except:
                    continue
            return cleaned
        
        test_results['total_tests'] += 1
        try:
            result = clean_data_pipeline(raw_data)
            if result == expected_clean:
                test_results['passed_tests'] += 1
                test_results['pipeline_tests'].append(("Data cleaning", "PASSED"))
            else:
                test_results['pipeline_tests'].append(("Data cleaning", f"FAILED - Expected {expected_clean}, got {result}"))
        except Exception as e:
            test_results['pipeline_tests'].append(("Data cleaning", f"ERROR - {e}"))
        
        # Test scenario 2: Statistical processing
        test_results['total_tests'] += 1
        try:
            numbers = [10, 20, 30, 40, 50]
            stats = {
                'mean': sum(numbers) / len(numbers),
                'min': min(numbers),
                'max': max(numbers),
                'sorted': sorted(numbers)
            }
            expected_mean = 30.0
            if stats['mean'] == expected_mean:
                test_results['passed_tests'] += 1
                test_results['pipeline_tests'].append(("Statistical processing", "PASSED"))
            else:
                test_results['pipeline_tests'].append(("Statistical processing", "FAILED"))
        except Exception as e:
            test_results['pipeline_tests'].append(("Statistical processing", f"ERROR - {e}"))
        
        return test_results
    
    integration_results = test_data_processing_pipeline()
    
    print("   Integration test results:")
    for test_name, result in integration_results['pipeline_tests']:
        status_icon = "✅" if "PASSED" in result else "❌"
        print(f"     {status_icon} {test_name}: {result}")
    
    print(f"   Overall success rate: {integration_results['passed_tests']}/{integration_results['total_tests']} "
          f"({integration_results['passed_tests']/integration_results['total_tests']*100:.1f}%)")
    
    # 2. STRESS TESTING
    print(f"\n2️⃣ Stress Testing:")
    
    def stress_test_operations():
        """Perform stress tests on list operations"""
        stress_results = {
            'large_list_creation': False,
            'memory_intensive': False,
            'rapid_modifications': False,
            'deep_nesting': False
        }
        
        try:
            # Large list creation test
            large_list = list(range(100000))
            stress_results['large_list_creation'] = len(large_list) == 100000
            
            # Memory intensive operations
            doubled = [x * 2 for x in large_list[:10000]]  # Subset for performance
            stress_results['memory_intensive'] = len(doubled) == 10000
            
            # Rapid modifications test
            test_list = list(range(1000))
            for i in range(100):
                test_list.append(i)
                test_list.pop(0)
            stress_results['rapid_modifications'] = len(test_list) == 1000
            
            # Deep nesting test
            nested = [[i] * 3 for i in range(100)]
            flattened = [item for sublist in nested for item in sublist]
            stress_results['deep_nesting'] = len(flattened) == 300
            
        except Exception as e:
            print(f"     Stress test error: {e}")
        
        return stress_results
    
    stress_results = stress_test_operations()
    
    print("   Stress test results:")
    for test_name, passed in stress_results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"     {test_name}: {status}")
    
    # 3. COMPREHENSIVE VALIDATION
    print(f"\n3️⃣ Final Validation Summary:")
    
    # Count all test results
    total_integration = integration_results['total_tests']
    passed_integration = integration_results['passed_tests']
    total_stress = len(stress_results)
    passed_stress = sum(stress_results.values())
    
    overall_total = total_integration + total_stress
    overall_passed = passed_integration + passed_stress
    
    print(f"   Integration tests: {passed_integration}/{total_integration} passed")
    print(f"   Stress tests: {passed_stress}/{total_stress} passed")
    print(f"   Overall test success: {overall_passed}/{overall_total} "
          f"({overall_passed/overall_total*100:.1f}%)")
    
    # Quality metrics
    quality_score = overall_passed / overall_total if overall_total > 0 else 0
    quality_grade = (
        "A+" if quality_score >= 0.95 else
        "A" if quality_score >= 0.90 else
        "B+" if quality_score >= 0.85 else
        "B" if quality_score >= 0.80 else
        "C" if quality_score >= 0.70 else "F"
    )
    
    print(f"   Quality Grade: {quality_grade} ({quality_score*100:.1f}%)")
    
    return {
        'integration_results': integration_results,
        'stress_results': stress_results,
        'overall_quality': {
            'total_tests': overall_total,
            'passed_tests': overall_passed,
            'success_rate': quality_score,
            'grade': quality_grade
        }
    }

# =============================================================================
# MAIN EXECUTION AND COMPREHENSIVE DEMONSTRATION
# =============================================================================

def main():
    """
    Main function executing comprehensive list testing and validation guide
    """
    print(__doc__)
    
    # Core sections
    fundamentals = list_testing_fundamentals()
    validation = validation_strategies()
    unit_testing = unit_testing_framework()
    error_handling = error_handling_testing()
    performance = performance_testing_framework()
    comprehensive = comprehensive_test_suite()
    
    return {
        'fundamentals': fundamentals,
        'validation_strategies': validation,
        'unit_testing': unit_testing,
        'error_handling': error_handling,
        'performance_testing': performance,
        'comprehensive_suite': comprehensive
    }

if __name__ == "__main__":
    """
    Execute comprehensive list testing and validation guide
    """
    results = main()
    
    print("\n" + "=" * 80)
    print("🎓 LIST TESTING & VALIDATION MASTERY SUMMARY")
    print("=" * 80)
    print("✅ Complete understanding of testing methodologies and validation strategies")
    print("✅ Mastery of unit testing frameworks and custom test runners")
    print("✅ Advanced error handling and exception testing techniques")
    print("✅ Performance benchmarking and scalability analysis")
    print("✅ Integration testing and stress testing approaches")
    print("✅ Comprehensive quality assurance and validation pipelines")
    print("✅ Real-world testing scenarios and defensive programming patterns")
    
    print("\n💡 Testing Excellence Key Points:")
    key_points = [
        "Systematic testing covers normal cases, edge cases, and error conditions",
        "Unit tests provide fast feedback and regression detection",
        "Property-based testing finds edge cases through random generation",
        "Performance testing ensures scalability and efficiency requirements",
        "Error handling testing validates robustness and recovery capabilities",
        "Integration tests verify component interactions and workflows",
        "Stress testing identifies system limits and failure modes",
        "Comprehensive validation ensures data integrity and correctness"
    ]
    
    for point in key_points:
        print(f"   • {point}")
    
    print("\n🎯 Professional Testing Applications:")
    applications = [
        "Production code quality assurance and continuous integration",
        "Data pipeline validation and ETL process verification",
        "API testing and service reliability validation",
        "Performance optimization and bottleneck identification",
        "Security testing and input validation verification",
        "Regulatory compliance and audit trail documentation",
        "Machine learning model testing and validation pipelines",
        "Scientific computing accuracy and reproducibility verification"
    ]
    
    for i, application in enumerate(applications, 1):
        print(f"   {i}. {application}")
    
    print(f"\n🚀 Master List Testing for Bulletproof Applications!")
    print("Thorough testing is the foundation of reliable software systems!")

# =============================================================================
# ORIGINAL SIMPLE EXAMPLE (Enhanced with Context)
# =============================================================================

# Simple demonstration of basic list operations with testing context
print("\n" + "=" * 60)
print("BASIC EXAMPLES FROM ORIGINAL CODE (WITH TESTING CONTEXT)")
print("=" * 60)

# Original simple list example
lst = [1, 2, 3, 4, 5]  # Example of a simple list

print("Original Basic Example:")
print(f"List: {lst}")
print("Processing each element (adding 100):")

# Enhanced version with validation
def validated_list_processing(input_list):
    """Process list with validation and testing"""
    # Input validation
    if not isinstance(input_list, list):
        raise TypeError(f"Expected list, got {type(input_list).__name__}")
    
    if not input_list:
        return []
    
    # Validate elements are numeric
    for i, element in enumerate(input_list):
        if not isinstance(element, (int, float)):
            raise ValueError(f"Element at index {i} is not numeric: {element}")
    
    # Process with validation
    result = []
    for e in input_list:
        processed = e + 100
        result.append(processed)
        print(f"Element: {processed}")  # Original output
    
    return result

# Test the enhanced version
try:
    processed_result = validated_list_processing(lst)
    print(f"Processing successful! Result: {processed_result}")
    print("✅ All validations passed")
except Exception as e:
    print(f"❌ Processing failed: {e}")

print("\nThis demonstrates how simple operations can be enhanced with:")
print("• Input validation and type checking")
print("• Error handling and meaningful exceptions")
print("• Clear documentation and testing principles")
print("• Robust processing that handles edge cases")