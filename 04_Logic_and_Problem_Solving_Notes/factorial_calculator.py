"""
Factorial Calculator - Mathematical Operations and Algorithms
==========================================================

Comprehensive factorial calculation system with multiple implementations,
mathematical analysis, and practical applications. Demonstrates iterative
vs recursive approaches, optimization techniques, and mathematical concepts.

Author: Python Learning Notes
Date: September 2025
Topic: Factorials, Recursion, Mathematical Algorithms
"""

import math
import time
from typing import Optional, List, Tuple

# =============================================================================
# FACTORIAL THEORY AND MATHEMATICAL BACKGROUND
# =============================================================================

def explain_factorials():
    """
    Educational explanation of factorial concept and properties
    """
    print("🧮 FACTORIAL THEORY AND CONCEPTS")
    print("=" * 35)
    
    print("\n📚 What is a Factorial?")
    print("The factorial of a positive integer n (written as n!) is:")
    print("   • The product of all positive integers less than or equal to n")
    print("   • Defined as: n! = n × (n-1) × (n-2) × ... × 2 × 1")
    print("   • Special case: 0! = 1 (by definition)")
    print("   • Only defined for non-negative integers")
    
    print("\n🔢 Mathematical Examples:")
    examples = [
        (0, "0! = 1 (by definition)"),
        (1, "1! = 1"),
        (2, "2! = 2 × 1 = 2"),
        (3, "3! = 3 × 2 × 1 = 6"),
        (4, "4! = 4 × 3 × 2 × 1 = 24"),
        (5, "5! = 5 × 4 × 3 × 2 × 1 = 120")
    ]
    
    for n, explanation in examples:
        print(f"   {explanation}")
    
    print("\n📊 Factorial Growth Pattern:")
    print("   Factorials grow extremely rapidly!")
    for i in range(1, 11):
        result = math.factorial(i)
        print(f"   {i:2}! = {result:,}")
    
    print("\n🎯 Real-world Applications:")
    print("   • Permutations and Combinations")
    print("   • Probability calculations")
    print("   • Series expansions (Taylor series)")
    print("   • Counting arrangements")
    print("   • Statistical distributions")

# =============================================================================
# ITERATIVE FACTORIAL IMPLEMENTATIONS
# =============================================================================

def factorial_iterative_basic(n):
    """
    Basic iterative factorial calculation
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    print(f"\n🔄 Basic Iterative Method for {n}!")
    print("=" * 30)
    
    if n == 0 or n == 1:
        print(f"   Base case: {n}! = 1")
        return 1
    
    factorial = 1
    print(f"   Starting calculation:")
    print(f"   Initial value: factorial = {factorial}")
    
    for i in range(1, n + 1):
        factorial *= i
        print(f"   Step {i}: factorial = factorial × {i} = {factorial}")
    
    print(f"\n   ✅ Final result: {n}! = {factorial:,}")
    return factorial

def factorial_iterative_optimized(n):
    """
    Optimized iterative factorial with early termination and validation
    """
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers")
    if n == 0 or n == 1:
        return 1
    
    # For very large numbers, warn about computation time
    if n > 20:
        print(f"⚠️  Computing {n}! - This is a very large number!")
        print(f"   Result will have approximately {int(n * math.log10(n))} digits")
    
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    
    return factorial

# =============================================================================
# RECURSIVE FACTORIAL IMPLEMENTATIONS
# =============================================================================

def factorial_recursive_basic(n, depth=0):
    """
    Basic recursive factorial implementation with visualization
    
    Time Complexity: O(n)
    Space Complexity: O(n) - due to recursion stack
    """
    indent = "  " * depth
    
    if depth == 0:
        print(f"\n🔁 Recursive Method for {n}!")
        print("=" * 25)
        print("   Call stack visualization:")
    
    print(f"{indent}📞 factorial_recursive({n})")
    
    # Base case
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers")
    if n == 0 or n == 1:
        print(f"{indent}   Base case reached: {n}! = 1")
        return 1
    
    # Recursive case
    print(f"{indent}   Calculating: {n} × factorial({n-1})")
    result = n * factorial_recursive_basic(n - 1, depth + 1)
    
    print(f"{indent}   Returning: {n} × {result//n} = {result}")
    return result

def factorial_recursive_memoized(n, memo=None):
    """
    Memoized recursive factorial for efficiency
    
    Uses memoization to store previously calculated values
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        print(f"   📋 Using memoized value: {n}! = {memo[n]}")
        return memo[n]
    
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers")
    if n == 0 or n == 1:
        memo[n] = 1
        return 1
    
    result = n * factorial_recursive_memoized(n - 1, memo)
    memo[n] = result
    return result

# =============================================================================
# ADVANCED FACTORIAL METHODS
# =============================================================================

def factorial_builtin(n):
    """
    Using Python's built-in math.factorial function
    
    This is the fastest and most reliable method for production use
    """
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers")
    
    start_time = time.time()
    result = math.factorial(n)
    end_time = time.time()
    
    print(f"\n⚡ Built-in Method: math.factorial({n})")
    print(f"   Result: {result:,}")
    print(f"   Computation time: {(end_time - start_time)*1000:.4f} ms")
    
    return result

def factorial_stirling_approximation(n):
    """
    Stirling's approximation for very large factorials
    
    Formula: n! ≈ √(2πn) × (n/e)^n
    
    Useful when exact value isn't needed but magnitude estimation is required
    """
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers")
    if n == 0:
        return 1
    
    import math
    
    # Stirling's formula
    approximation = math.sqrt(2 * math.pi * n) * (n / math.e) ** n
    
    # Compare with exact value for demonstration
    exact = math.factorial(n) if n <= 20 else "Too large to compute exactly"
    
    print(f"\n🔬 Stirling's Approximation for {n}!")
    print("=" * 30)
    print(f"   Formula: √(2πn) × (n/e)^n")
    print(f"   Approximation: {approximation:,.0f}")
    
    if isinstance(exact, int):
        error_percent = abs(approximation - exact) / exact * 100
        print(f"   Exact value:   {exact:,}")
        print(f"   Error:         {error_percent:.2f}%")
    
    return approximation

# =============================================================================
# PERFORMANCE COMPARISON AND ANALYSIS
# =============================================================================

def compare_factorial_methods(n):
    """
    Compare performance of different factorial calculation methods
    """
    print(f"\n⏱️  PERFORMANCE COMPARISON for {n}!")
    print("=" * 40)
    
    methods = [
        ("Iterative Basic", lambda x: factorial_iterative_basic_silent(x)),
        ("Iterative Optimized", lambda x: factorial_iterative_optimized(x)),
        ("Recursive Basic", lambda x: factorial_recursive_silent(x)),
        ("Built-in math.factorial", lambda x: math.factorial(x))
    ]
    
    results = []
    
    for name, method in methods:
        try:
            print(f"\n🧪 Testing {name}:")
            
            start_time = time.time()
            result = method(n)
            end_time = time.time()
            
            execution_time = (end_time - start_time) * 1000
            results.append((name, result, execution_time, "Success"))
            
            print(f"   Time: {execution_time:.4f} ms")
            
        except RecursionError:
            results.append((name, None, None, "RecursionError"))
            print(f"   ❌ RecursionError - stack overflow")
        except Exception as e:
            results.append((name, None, None, f"Error: {str(e)}"))
            print(f"   ❌ {str(e)}")
    
    # Display results table
    print(f"\n📊 Performance Summary:")
    print("   ┌─────────────────────────┬─────────────┬──────────────┐")
    print("   │ Method                  │ Time (ms)   │ Status       │")
    print("   ├─────────────────────────┼─────────────┼──────────────┤")
    
    for name, result, time_ms, status in results:
        time_str = f"{time_ms:>9.4f}" if time_ms is not None else "    N/A"
        print(f"   │ {name:<23} │ {time_str} │ {status:<12} │")
    
    print("   └─────────────────────────┴─────────────┴──────────────┘")

# Helper functions for performance testing (silent versions)
def factorial_iterative_basic_silent(n):
    """Silent version for performance testing"""
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers")
    if n == 0 or n == 1:
        return 1
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def factorial_recursive_silent(n):
    """Silent version for performance testing"""
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive_silent(n - 1)

# =============================================================================
# PRACTICAL APPLICATIONS
# =============================================================================

def factorial_applications():
    """
    Demonstrate practical applications of factorials
    """
    print("\n🎯 PRACTICAL APPLICATIONS OF FACTORIALS")
    print("=" * 40)
    
    print("\n1️⃣ Permutations (Arrangements):")
    print("   How many ways can you arrange n distinct objects?")
    n = 5
    arrangements = math.factorial(n)
    print(f"   {n} people in a line: {n}! = {arrangements:,} ways")
    
    print("\n2️⃣ Combinations (Selections):")
    print("   Formula: C(n,r) = n! / (r!(n-r)!)")
    n, r = 10, 3
    combinations = math.factorial(n) // (math.factorial(r) * math.factorial(n-r))
    print(f"   Choose {r} from {n}: C({n},{r}) = {combinations} ways")
    
    print("\n3️⃣ Probability Calculations:")
    print("   Probability of specific arrangement:")
    total_arrangements = math.factorial(5)
    specific_probability = 1 / total_arrangements
    print(f"   P(specific order of 5 items) = 1/{total_arrangements} = {specific_probability:.6f}")
    
    print("\n4️⃣ Series Expansion:")
    print("   e^x = 1 + x + x²/2! + x³/3! + x⁴/4! + ...")
    x = 1
    e_approximation = sum(x**n / math.factorial(n) for n in range(10))
    print(f"   e^{x} ≈ {e_approximation:.6f} (using first 10 terms)")
    print(f"   Actual e^{x} = {math.e:.6f}")

def calculate_permutations_combinations(n, r):
    """
    Calculate permutations and combinations using factorials
    """
    print(f"\n🔢 PERMUTATIONS AND COMBINATIONS")
    print(f"   Given: n = {n}, r = {r}")
    print("=" * 30)
    
    if r > n:
        print("❌ Error: r cannot be greater than n")
        return None, None
    
    # Permutations: P(n,r) = n! / (n-r)!
    permutations = math.factorial(n) // math.factorial(n - r)
    print(f"   Permutations P({n},{r}) = {n}! / {n-r}! = {permutations:,}")
    
    # Combinations: C(n,r) = n! / (r!(n-r)!)
    combinations = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
    print(f"   Combinations C({n},{r}) = {n}! / ({r}!{n-r}!) = {combinations:,}")
    
    return permutations, combinations

# =============================================================================
# INTERACTIVE FACTORIAL CALCULATOR
# =============================================================================

def interactive_factorial_calculator():
    """
    Interactive factorial calculator with multiple options
    """
    print("\n🧮 INTERACTIVE FACTORIAL CALCULATOR")
    print("=" * 35)
    
    while True:
        try:
            print("\n🎯 Choose an option:")
            print("   1. Calculate factorial (basic iterative)")
            print("   2. Calculate factorial (recursive with visualization)")
            print("   3. Compare calculation methods")
            print("   4. Stirling's approximation")
            print("   5. Factorial applications")
            print("   6. Permutations and combinations")
            print("   7. Learn about factorials")
            print("   8. Exit")
            
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == "1":
                n = int(input("\nEnter a non-negative integer: "))
                result = factorial_iterative_basic(n)
                
            elif choice == "2":
                n = int(input("\nEnter a non-negative integer: "))
                if n > 10:
                    print("⚠️  Large recursion depth! Consider using iterative method.")
                    confirm = input("Continue anyway? (y/n): ").lower()
                    if confirm != 'y':
                        continue
                
                result = factorial_recursive_basic(n)
                
            elif choice == "3":
                n = int(input("\nEnter number for performance comparison: "))
                compare_factorial_methods(n)
                
            elif choice == "4":
                n = int(input("\nEnter number for Stirling's approximation: "))
                factorial_stirling_approximation(n)
                
            elif choice == "5":
                factorial_applications()
                
            elif choice == "6":
                n = int(input("Enter total items (n): "))
                r = int(input("Enter items to choose (r): "))
                calculate_permutations_combinations(n, r)
                
            elif choice == "7":
                explain_factorials()
                
            elif choice == "8":
                print("\n👋 Thanks for exploring factorials!")
                break
                
            else:
                print("❌ Invalid choice. Please choose 1-8.")
                
        except ValueError as e:
            print(f"❌ Invalid input: {e}")
        except RecursionError:
            print("❌ Number too large for recursive calculation!")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break

if __name__ == "__main__":
    """
    Main execution demonstrating factorial calculations and concepts
    """
    print(__doc__)
    
    # Educational content
    explain_factorials()
    
    # Demonstrate different methods
    print("\n🧪 ALGORITHM DEMONSTRATIONS:")
    test_numbers = [5, 6, 8, 10]
    
    for num in test_numbers:
        print(f"\n" + "="*50)
        print(f"Calculating {num}! using different methods:")
        
        # Iterative method
        result1 = factorial_iterative_basic(num)
        
        # Recursive method (only for smaller numbers)
        if num <= 8:
            result2 = factorial_recursive_basic(num)
        
        # Built-in method
        result3 = factorial_builtin(num)
    
    # Performance comparison
    print(f"\n" + "="*50)
    print("Performance Comparison:")
    compare_factorial_methods(12)
    
    # Applications demonstration
    factorial_applications()
    
    # Interactive session
    interactive_factorial_calculator()
    
    print("\n" + "=" * 50)
    print("🎓 LEARNING SUMMARY")
    print("=" * 50)
    print("✅ Understanding of factorial mathematical concept")
    print("✅ Implementation of iterative and recursive algorithms")
    print("✅ Performance analysis and optimization techniques")
    print("✅ Knowledge of practical applications")
    print("✅ Comparison of different computational approaches")
    
    print("\n💡 Key Concepts Learned:")
    print("• Factorial definition and mathematical properties")
    print("• Iterative vs recursive implementation trade-offs")
    print("• Time and space complexity analysis")
    print("• Real-world applications in combinatorics")
    print("• Approximation methods for large numbers")
    
    print("\n🎯 Next Steps:")
    print("• Study gamma function (generalization of factorials)")
    print("• Explore double factorials and superfactorials")
    print("• Learn about factorial in modular arithmetic")
    print("• Investigate Wilson's theorem and factorial properties")