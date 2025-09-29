"""
Testing and Debugging in Python - Comprehensive Guide
====================================================

Educational guide to unit testing with unittest/pytest, debugging techniques, code profiling, and quality assurance.
Includes best practices for testing and debugging Python applications.

Author: Python Learning Notes
Date: September 2025
Topic: Testing, Debugging, Unit Tests, Profiling, Quality Assurance
"""

import unittest
import time
import cProfile
import pstats
from functools import wraps
import logging

# =============================================================================
# UNIT TESTING WITH UNITTEST
# =============================================================================

class Calculator:
    """Simple calculator class for testing"""
    
    def add(self, a, b):
        return a + b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if n == 0:
            return 1
        return n * self.factorial(n - 1)

class TestCalculator(unittest.TestCase):
    """Unit tests for Calculator class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition functionality"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_divide(self):
        """Test division functionality"""
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
    
    def test_factorial(self):
        """Test factorial functionality"""
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(5), 120)
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)

# =============================================================================
# DEBUGGING TECHNIQUES
# =============================================================================

def debug_function(func):
    """Decorator for debugging function calls"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned: {result}")
            return result
        except Exception as e:
            print(f"{func.__name__} raised: {type(e).__name__}: {e}")
            raise
    return wrapper

@debug_function
def problematic_function(x, y):
    """Function with potential issues for debugging"""
    if x == 0:
        raise ValueError("x cannot be zero")
    result = x / y
    return result * 2

# =============================================================================
# CODE PROFILING
# =============================================================================

def fibonacci_recursive(n):
    """Inefficient recursive Fibonacci for profiling"""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    """Efficient iterative Fibonacci"""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def profile_fibonacci():
    """Profile Fibonacci implementations"""
    print("\nProfiling Fibonacci implementations:")
    
    # Profile recursive version
    print("Recursive Fibonacci (n=30):")
    profiler = cProfile.Profile()
    profiler.enable()
    result1 = fibonacci_recursive(30)
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative').print_stats(5)
    print(f"Result: {result1}")
    
    # Profile iterative version
    print("\nIterative Fibonacci (n=30):")
    profiler = cProfile.Profile()
    profiler.enable()
    result2 = fibonacci_iterative(30)
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative').print_stats(5)
    print(f"Result: {result2}")

# =============================================================================
# LOGGING FOR DEBUGGING
# =============================================================================

def setup_debug_logging():
    """Configure logging for debugging"""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
    )

def function_with_logging():
    """Function demonstrating logging for debugging"""
    logger = logging.getLogger(__name__)
    logger.debug("Entering function_with_logging")
    
    try:
        logger.info("Performing calculation")
        result = 10 / 2
        logger.debug(f"Calculation result: {result}")
        return result
    except Exception as e:
        logger.error(f"Error in calculation: {e}")
        raise
    finally:
        logger.debug("Exiting function_with_logging")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    print(__doc__)
    
    # Run unit tests
    print("Running Unit Tests:")
    unittest.main(argv=[''], exit=False, verbosity=2)
    
    # Demonstrate debugging
    print("\nDebugging Demo:")
    try:
        result = problematic_function(5, 2)
        print(f"Success: {result}")
    except ValueError as e:
        print(f"Caught error: {e}")
    
    # Profile code
    profile_fibonacci()
    
    # Logging demo
    print("\nLogging Demo:")
    setup_debug_logging()
    function_with_logging()
    
    print("\nTesting and debugging guide completed!")

if __name__ == "__main__":
    main()
