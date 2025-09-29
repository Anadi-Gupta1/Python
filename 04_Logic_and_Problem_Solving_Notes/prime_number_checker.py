"""
Prime Number Checker - Advanced Algorithm Implementation
=====================================================

Comprehensive prime number detection system with multiple algorithms,
optimization techniques, and mathematical analysis. Demonstrates
algorithmic thinking, optimization strategies, and number theory.

Author: Python Learning Notes
Date: September 2025
Topic: Prime Numbers, Algorithm Optimization, Number Theory
"""

import math
import time
from typing import List, Tuple

# =============================================================================
# PRIME NUMBER THEORY AND CONCEPTS
# =============================================================================

def explain_prime_numbers():
    """
    Educational explanation of prime numbers and their properties
    """
    print("🔢 PRIME NUMBER THEORY")
    print("=" * 30)
    
    print("\n📚 What are Prime Numbers?")
    print("A prime number is a natural number greater than 1 that:")
    print("   • Has exactly two positive divisors: 1 and itself")
    print("   • Cannot be formed by multiplying two smaller numbers")
    print("   • Is the building block of all positive integers")
    
    print("\n🎯 Key Properties:")
    print("   • 2 is the only even prime number")
    print("   • All other primes are odd numbers")
    print("   • There are infinitely many prime numbers")
    print("   • Prime numbers become less frequent as numbers get larger")
    
    print("\n📊 First 20 Prime Numbers:")
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    print(f"   {primes}")
    
    print("\n🔍 Examples:")
    print("   • 2 is prime: divisors are 1, 2")
    print("   • 4 is NOT prime: divisors are 1, 2, 4")
    print("   • 17 is prime: divisors are 1, 17")
    print("   • 21 is NOT prime: divisors are 1, 3, 7, 21")

# =============================================================================
# BASIC PRIME CHECKING ALGORITHM
# =============================================================================

def is_prime_basic(n):
    """
    Basic prime checking algorithm - checks all numbers from 2 to n-1
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        n (int): Number to check for primality
    
    Returns:
        bool: True if prime, False otherwise
    """
    if n < 2:
        return False
    
    print(f"\n🔍 Basic Algorithm for {n}:")
    print(f"   Checking divisors from 2 to {n-1}...")
    
    for i in range(2, n):
        print(f"   Checking {n} ÷ {i} = {n/i:.2f} (remainder: {n%i})")
        if n % i == 0:
            print(f"   ❌ Found divisor: {i}")
            return False
    
    print(f"   ✅ No divisors found - {n} is prime!")
    return True

# =============================================================================
# OPTIMIZED PRIME CHECKING ALGORITHMS
# =============================================================================

def is_prime_optimized(n):
    """
    Optimized prime checking - only check up to sqrt(n)
    
    Time Complexity: O(√n)
    Space Complexity: O(1)
    
    Mathematical insight: If n has a divisor greater than √n,
    it must also have a divisor smaller than √n.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Only check odd numbers up to sqrt(n)
    limit = int(math.sqrt(n)) + 1
    
    print(f"\n⚡ Optimized Algorithm for {n}:")
    print(f"   Only checking odd divisors from 3 to {limit-1}...")
    print(f"   Mathematical insight: √{n} ≈ {math.sqrt(n):.2f}")
    
    for i in range(3, limit, 2):
        print(f"   Checking {n} ÷ {i} = {n/i:.2f} (remainder: {n%i})")
        if n % i == 0:
            print(f"   ❌ Found divisor: {i}")
            return False
    
    print(f"   ✅ No divisors found - {n} is prime!")
    return True

def is_prime_advanced(n):
    """
    Advanced prime checking with multiple optimizations
    
    Optimizations:
    - Handle special cases (2, 3, multiples of 2 and 3)
    - Check only numbers of form 6k±1
    - Use square root limit
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check for divisors of form 6k±1 up to √n
    i = 5
    limit = int(math.sqrt(n)) + 1
    
    print(f"\n🚀 Advanced Algorithm for {n}:")
    print(f"   Checking numbers of form 6k±1 up to {limit}...")
    
    while i <= limit:
        if n % i == 0 or n % (i + 2) == 0:
            print(f"   ❌ Found divisor: {i if n % i == 0 else i + 2}")
            return False
        print(f"   Checked {i} and {i+2}")
        i += 6
    
    print(f"   ✅ No divisors found - {n} is prime!")
    return True

# =============================================================================
# PERFORMANCE COMPARISON
# =============================================================================

def compare_algorithms(n):
    """
    Compare performance of different prime checking algorithms
    """
    print(f"\n⏱️  PERFORMANCE COMPARISON for {n}")
    print("=" * 40)
    
    algorithms = [
        ("Basic Algorithm O(n)", lambda x: is_prime_simple(x)),
        ("Optimized Algorithm O(√n)", lambda x: is_prime_sqrt(x)),
        ("Advanced Algorithm", lambda x: is_prime_advanced_simple(x))
    ]
    
    results = []
    
    for name, func in algorithms:
        print(f"\n🧪 Testing {name}:")
        
        start_time = time.time()
        result = func(n)
        end_time = time.time()
        
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        results.append((name, result, execution_time))
        
        print(f"   Result: {'Prime' if result else 'Not Prime'}")
        print(f"   Time: {execution_time:.4f} ms")
    
    print(f"\n📊 Performance Summary:")
    print("   ┌─────────────────────────┬──────────┬─────────────┐")
    print("   │ Algorithm               │ Result   │ Time (ms)   │")
    print("   ├─────────────────────────┼──────────┼─────────────┤")
    
    for name, result, time_ms in results:
        status = "Prime" if result else "Not Prime"
        print(f"   │ {name:<23} │ {status:<8} │ {time_ms:>9.4f} │")
    
    print("   └─────────────────────────┴──────────┴─────────────┘")

# Helper functions for performance comparison (simplified versions)
def is_prime_simple(n):
    """Simplified basic algorithm for performance testing"""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime_sqrt(n):
    """Simplified sqrt algorithm for performance testing"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_prime_advanced_simple(n):
    """Simplified advanced algorithm for performance testing"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# =============================================================================
# PRIME NUMBER GENERATORS
# =============================================================================

def generate_primes_sieve(limit):
    """
    Generate all prime numbers up to limit using Sieve of Eratosthenes
    
    Time Complexity: O(n log log n)
    Space Complexity: O(n)
    """
    print(f"\n🧮 SIEVE OF ERATOSTHENES (up to {limit})")
    print("=" * 40)
    
    if limit < 2:
        return []
    
    # Initialize sieve array
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    print(f"Step 1: Initialize array of size {limit + 1}")
    
    # Sieve algorithm
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            print(f"Step {i}: Marking multiples of {i}")
            # Mark all multiples of i as not prime
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    
    # Collect prime numbers
    primes = [i for i in range(2, limit + 1) if sieve[i]]
    
    print(f"\n✅ Found {len(primes)} prime numbers:")
    print(f"   {primes[:20]}{'...' if len(primes) > 20 else ''}")
    
    return primes

def find_primes_in_range(start, end):
    """
    Find all prime numbers in a given range
    """
    print(f"\n🎯 PRIMES IN RANGE [{start}, {end}]")
    print("=" * 35)
    
    primes = []
    
    for num in range(max(2, start), end + 1):
        if is_prime_sqrt(num):
            primes.append(num)
    
    print(f"Prime numbers found: {primes}")
    print(f"Total count: {len(primes)}")
    
    return primes

# =============================================================================
# INTERACTIVE PRIME CHECKER
# =============================================================================

def interactive_prime_checker():
    """
    Interactive prime number checker with multiple options
    """
    print("\n🔢 INTERACTIVE PRIME NUMBER CHECKER")
    print("=" * 40)
    
    while True:
        try:
            print("\n🎯 Choose an option:")
            print("   1. Check if a number is prime")
            print("   2. Generate primes up to a limit")
            print("   3. Find primes in a range")
            print("   4. Compare algorithm performance")
            print("   5. View prime number theory")
            print("   6. Exit")
            
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == "1":
                n = int(input("\nEnter a number to check: "))
                
                print("\n🔍 Choose algorithm:")
                print("   1. Basic algorithm (educational)")
                print("   2. Optimized algorithm (recommended)")
                print("   3. Advanced algorithm (fastest)")
                
                algo_choice = input("Choose algorithm (1-3): ").strip()
                
                if algo_choice == "1":
                    result = is_prime_basic(n)
                elif algo_choice == "2":
                    result = is_prime_optimized(n)
                else:
                    result = is_prime_advanced(n)
                
                print(f"\n🎯 Final Result: {n} is {'PRIME' if result else 'NOT PRIME'}")
                
            elif choice == "2":
                limit = int(input("\nEnter upper limit: "))
                generate_primes_sieve(limit)
                
            elif choice == "3":
                start = int(input("Enter start of range: "))
                end = int(input("Enter end of range: "))
                find_primes_in_range(start, end)
                
            elif choice == "4":
                n = int(input("\nEnter number for performance test: "))
                compare_algorithms(n)
                
            elif choice == "5":
                explain_prime_numbers()
                
            elif choice == "6":
                print("\n👋 Thanks for exploring prime numbers!")
                break
                
            else:
                print("❌ Invalid choice. Please choose 1-6.")
                
        except ValueError:
            print("❌ Please enter a valid number!")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break

# =============================================================================
# MATHEMATICAL EXAMPLES AND PATTERNS
# =============================================================================

def explore_prime_patterns():
    """
    Explore interesting patterns and properties of prime numbers
    """
    print("\n🔍 PRIME NUMBER PATTERNS AND PROPERTIES")
    print("=" * 45)
    
    # Twin primes
    print("\n1️⃣ Twin Primes (differ by 2):")
    twin_primes = [(3,5), (5,7), (11,13), (17,19), (29,31), (41,43)]
    for p1, p2 in twin_primes:
        print(f"   ({p1}, {p2})")
    
    # Prime gaps
    print("\n2️⃣ Prime Gaps (distance between consecutive primes):")
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    gaps = [primes[i+1] - primes[i] for i in range(len(primes)-1)]
    
    for i in range(len(gaps)):
        print(f"   Gap between {primes[i]} and {primes[i+1]}: {gaps[i]}")
    
    # Mersenne primes (2^p - 1 where p is prime)
    print("\n3️⃣ Mersenne Primes (2^p - 1):")
    mersenne_primes = []
    for p in [2, 3, 5, 7, 13, 17, 19]:
        mersenne = 2**p - 1
        if is_prime_sqrt(mersenne):
            mersenne_primes.append((p, mersenne))
            print(f"   2^{p} - 1 = {mersenne} (prime)")
    
    # Prime factorization example
    print("\n4️⃣ Prime Factorization Examples:")
    numbers = [12, 24, 36, 60, 100]
    
    for num in numbers:
        factors = prime_factorization(num)
        factor_str = " × ".join([f"{p}^{e}" if e > 1 else str(p) for p, e in factors])
        print(f"   {num} = {factor_str}")

def prime_factorization(n):
    """
    Find prime factorization of a number
    """
    factors = []
    d = 2
    
    while d * d <= n:
        while n % d == 0:
            # Count occurrences of this prime factor
            count = 0
            while n % d == 0:
                n //= d
                count += 1
            factors.append((d, count))
        d += 1
    
    if n > 1:
        factors.append((n, 1))
    
    return factors

if __name__ == "__main__":
    """
    Main execution demonstrating prime number concepts
    """
    print(__doc__)
    
    # Educational content
    explain_prime_numbers()
    
    # Demonstrate algorithms with examples
    print("\n🧪 ALGORITHM DEMONSTRATIONS:")
    test_numbers = [17, 25, 97, 100]
    
    for num in test_numbers:
        print(f"\n" + "="*50)
        print(f"Testing {num}:")
        is_prime_optimized(num)
    
    # Show patterns
    explore_prime_patterns()
    
    # Interactive session
    interactive_prime_checker()
    
    print("\n" + "=" * 50)
    print("🎓 LEARNING SUMMARY")
    print("=" * 50)
    print("✅ Understanding of prime number theory and properties")
    print("✅ Implementation of multiple prime checking algorithms")
    print("✅ Knowledge of algorithm optimization techniques")
    print("✅ Performance analysis and comparison skills")
    print("✅ Pattern recognition in number theory")
    
    print("\n💡 Key Concepts Learned:")
    print("• Prime number definition and properties")
    print("• Algorithm optimization from O(n) to O(√n)")
    print("• Sieve of Eratosthenes for bulk prime generation")
    print("• Mathematical patterns and special prime types")
    print("• Performance measurement and analysis")
    
    print("\n🎯 Next Steps:")
    print("• Study advanced primality tests (Miller-Rabin)")
    print("• Explore cryptographic applications of primes")
    print("• Learn about prime number theorems")
    print("• Implement probabilistic primality tests")