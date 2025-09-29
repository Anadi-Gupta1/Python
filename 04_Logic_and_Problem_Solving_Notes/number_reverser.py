"""
Number Reverser - Digit Manipulation and Algorithm Design
=======================================================

Comprehensive number reversal system with multiple algorithms, mathematical
analysis, and practical applications. Demonstrates digit extraction, number
reconstruction, and algorithmic thinking for numeric operations.

Author: Python Learning Notes
Date: September 2025
Topic: Number Manipulation, Algorithms, Mathematical Operations, Loops
"""

import math
from typing import List, Tuple, Union

# =============================================================================
# MATHEMATICAL CONCEPTS AND NUMBER THEORY
# =============================================================================

def explain_number_reversal_concepts():
    """
    Educational explanation of number reversal and digit manipulation
    """
    print("🔢 NUMBER REVERSAL CONCEPTS")
    print("=" * 28)
    
    print("\n📚 What is Number Reversal?")
    print("Number reversal involves:")
    print("   • Extracting individual digits from a number")
    print("   • Rearranging digits in reverse order")
    print("   • Reconstructing the number from reversed digits")
    print("   • Understanding positional value systems")
    
    print("\n🧮 Mathematical Foundation:")
    print("For a number like 1234:")
    print("   • Position values: 1×1000 + 2×100 + 3×10 + 4×1")
    print("   • Digit extraction: Use modulo (%) and division (/)")
    print("   • Reversal process: 4×1000 + 3×100 + 2×10 + 1×1")
    print("   • Result: 4321")
    
    print("\n🔍 Step-by-Step Process:")
    number = 1234
    print(f"   Original number: {number}")
    
    steps = []
    temp = number
    reversed_num = 0
    step = 1
    
    print("   Extraction process:")
    while temp > 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10
        print(f"   Step {step}: Extract {digit}, build {reversed_num}")
        step += 1
    
    print(f"   Final result: {reversed_num}")
    
    print("\n📊 Key Operations:")
    operations = [
        ("Modulo (%)", "Extract last digit", "1234 % 10 = 4"),
        ("Integer Division (//)", "Remove last digit", "1234 // 10 = 123"),
        ("Multiplication (*)", "Shift digits left", "42 * 10 = 420"),
        ("Addition (+)", "Append new digit", "420 + 1 = 421")
    ]
    
    print("   ┌─────────────────┬──────────────────┬─────────────────┐")
    print("   │ Operation       │ Purpose          │ Example         │")
    print("   ├─────────────────┼──────────────────┼─────────────────┤")
    for op, purpose, example in operations:
        print(f"   │ {op:<15} │ {purpose:<16} │ {example:<15} │")
    print("   └─────────────────┴──────────────────┴─────────────────┘")

# =============================================================================
# BASIC NUMBER REVERSAL ALGORITHMS
# =============================================================================

def reverse_number_iterative(n):
    """
    Basic iterative approach to reverse a number
    
    Time Complexity: O(log n) - where n is the input number
    Space Complexity: O(1)
    
    Args:
        n (int): Number to reverse
        
    Returns:
        int: Reversed number
    """
    original = n
    print(f"\n🔄 Iterative Method for {original}")
    print("=" * 25)
    
    if n == 0:
        print("   Special case: 0 reversed is 0")
        return 0
    
    # Handle negative numbers
    is_negative = n < 0
    if is_negative:
        n = abs(n)
        print(f"   Negative number detected: working with {n}")
    
    reversed_num = 0
    step = 1
    
    print("   Step-by-step process:")
    print(f"   Initial: number = {n}, reversed = {reversed_num}")
    
    while n > 0:
        # Extract the last digit
        digit = n % 10
        
        # Build reversed number
        reversed_num = reversed_num * 10 + digit
        
        # Remove the last digit from original
        n = n // 10
        
        print(f"   Step {step}: Extract {digit} → reversed = {reversed_num}, remaining = {n}")
        step += 1
    
    # Apply negative sign if needed
    if is_negative:
        reversed_num = -reversed_num
        print(f"   Applied negative sign: {reversed_num}")
    
    print(f"\n   ✅ Final result: {original} → {reversed_num}")
    return reversed_num

def reverse_number_string_method(n):
    """
    String-based approach to reverse a number
    
    Method: Convert to string, reverse, convert back
    Simpler but less educational for mathematical understanding
    """
    original = n
    print(f"\n📝 String Method for {original}")
    print("=" * 20)
    
    # Handle negative numbers
    is_negative = n < 0
    if is_negative:
        n = abs(n)
        print(f"   Negative number: working with {n}")
    
    # Convert to string and reverse
    str_number = str(n)
    reversed_str = str_number[::-1]
    
    print(f"   String representation: '{str_number}'")
    print(f"   Reversed string: '{reversed_str}'")
    
    # Convert back to integer
    reversed_num = int(reversed_str)
    
    # Apply negative sign if needed
    if is_negative:
        reversed_num = -reversed_num
        print(f"   Applied negative sign: {reversed_num}")
    
    print(f"\n   ✅ Result: {original} → {reversed_num}")
    return reversed_num

def reverse_number_recursive(n, reversed_num=0):
    """
    Recursive approach to reverse a number
    
    Method: Use recursion to build reversed number
    """
    if n == 0:
        return reversed_num
    
    # Extract last digit and recursively process remaining
    digit = n % 10
    return reverse_number_recursive(n // 10, reversed_num * 10 + digit)

def reverse_number_recursive_verbose(n, reversed_num=0, depth=0):
    """
    Verbose recursive approach with step visualization
    """
    indent = "  " * depth
    
    if depth == 0:
        print(f"\n🔁 Recursive Method for {n}")
        print("=" * 20)
        print("   Call stack visualization:")
    
    print(f"{indent}📞 reverse({n}, {reversed_num})")
    
    # Base case
    if n == 0:
        print(f"{indent}   Base case reached, returning {reversed_num}")
        return reversed_num
    
    # Extract digit and make recursive call
    digit = n % 10
    remaining = n // 10
    new_reversed = reversed_num * 10 + digit
    
    print(f"{indent}   Extract digit {digit}, new_reversed = {new_reversed}")
    
    result = reverse_number_recursive_verbose(remaining, new_reversed, depth + 1)
    
    print(f"{indent}   Returning {result}")
    return result

# =============================================================================
# ADVANCED NUMBER REVERSAL FEATURES
# =============================================================================

def reverse_with_validation(n):
    """
    Number reversal with comprehensive input validation and analysis
    """
    original = n
    print(f"\n🛡️  Validated Reversal for {original}")
    print("=" * 25)
    
    # Input validation
    if not isinstance(n, int):
        print("   ❌ Error: Input must be an integer")
        return None
    
    # Special cases
    if n == 0:
        print("   ⚠️  Special case: Zero")
        return 0
    
    # Check for single digit
    if -9 <= n <= 9:
        print("   ℹ️  Single digit number")
        return n
    
    # Analyze number properties before reversal
    digit_count = len(str(abs(n)))
    is_palindrome_before = str(abs(n)) == str(abs(n))[::-1]
    
    print(f"   📊 Analysis:")
    print(f"   • Digit count: {digit_count}")
    print(f"   • Is negative: {n < 0}")
    print(f"   • Is palindrome: {is_palindrome_before}")
    
    # Perform reversal
    reversed_num = reverse_number_iterative_silent(n)
    
    # Post-reversal analysis
    is_palindrome_after = (n == reversed_num)
    
    print(f"\n   📈 Results:")
    print(f"   • Original: {original}")
    print(f"   • Reversed: {reversed_num}")
    print(f"   • Forms palindrome: {is_palindrome_after}")
    
    # Check for leading zeros (would be lost in integer conversion)
    original_str = str(abs(original))
    if original_str.endswith('0'):
        zeros_lost = len(original_str) - len(original_str.rstrip('0'))
        print(f"   ⚠️  {zeros_lost} trailing zero(s) lost in reversal")
    
    return reversed_num

def reverse_number_iterative_silent(n):
    """Silent version for internal use"""
    is_negative = n < 0
    n = abs(n)
    reversed_num = 0
    
    while n > 0:
        reversed_num = reversed_num * 10 + (n % 10)
        n //= 10
    
    return -reversed_num if is_negative else reversed_num

def reverse_preserve_leading_zeros(number_str):
    """
    Reverse number while preserving leading zeros as string
    
    Useful when working with number strings where leading zeros matter
    """
    print(f"\n🔐 Preserving Leading Zeros: '{number_str}'")
    print("=" * 30)
    
    if not number_str.isdigit() and not (number_str.startswith('-') and number_str[1:].isdigit()):
        print("   ❌ Invalid number string")
        return None
    
    # Handle negative sign
    if number_str.startswith('-'):
        sign = '-'
        digits = number_str[1:]
    else:
        sign = ''
        digits = number_str
    
    # Reverse the digits
    reversed_digits = digits[::-1]
    result = sign + reversed_digits
    
    print(f"   Original digits: '{digits}'")
    print(f"   Reversed digits: '{reversed_digits}'")
    print(f"   Final result: '{result}'")
    
    return result

# =============================================================================
# MATHEMATICAL PROPERTIES AND ANALYSIS
# =============================================================================

def analyze_reversal_properties(numbers):
    """
    Analyze mathematical properties of number reversal
    """
    print(f"\n🔬 REVERSAL PROPERTIES ANALYSIS")
    print("=" * 30)
    
    properties = {
        'palindromes': [],
        'increased': [],
        'decreased': [],
        'same_digits': [],
        'different_digits': []
    }
    
    for num in numbers:
        reversed_num = reverse_number_iterative_silent(num)
        
        # Check if palindrome
        if num == reversed_num:
            properties['palindromes'].append(num)
        
        # Check if increased/decreased
        if reversed_num > num:
            properties['increased'].append((num, reversed_num))
        elif reversed_num < num:
            properties['decreased'].append((num, reversed_num))
        
        # Check digit count
        if len(str(abs(num))) == len(str(abs(reversed_num))):
            properties['same_digits'].append(num)
        else:
            properties['different_digits'].append(num)
    
    # Display analysis
    print(f"   📊 Analysis of {len(numbers)} numbers:")
    print(f"   • Palindromes: {len(properties['palindromes'])}")
    if properties['palindromes']:
        print(f"     Examples: {properties['palindromes'][:5]}")
    
    print(f"   • Value increased after reversal: {len(properties['increased'])}")
    if properties['increased']:
        print(f"     Examples: {properties['increased'][:3]}")
    
    print(f"   • Value decreased after reversal: {len(properties['decreased'])}")
    if properties['decreased']:
        print(f"     Examples: {properties['decreased'][:3]}")
    
    print(f"   • Same digit count: {len(properties['same_digits'])}")
    print(f"   • Different digit count: {len(properties['different_digits'])}")

def find_palindromic_numbers(start, end):
    """
    Find all palindromic numbers in a given range
    """
    print(f"\n🔄 Palindromic Numbers in Range [{start}, {end}]")
    print("=" * 40)
    
    palindromes = []
    
    for num in range(start, end + 1):
        reversed_num = reverse_number_iterative_silent(num)
        if num == reversed_num:
            palindromes.append(num)
    
    print(f"   Found {len(palindromes)} palindromic numbers:")
    
    # Group by digit count for better display
    by_digits = {}
    for p in palindromes:
        digits = len(str(p))
        if digits not in by_digits:
            by_digits[digits] = []
        by_digits[digits].append(p)
    
    for digits in sorted(by_digits.keys()):
        numbers = by_digits[digits]
        print(f"   {digits}-digit: {numbers}")
    
    return palindromes

def number_reversal_patterns():
    """
    Explore interesting patterns in number reversal
    """
    print(f"\n🎨 NUMBER REVERSAL PATTERNS")
    print("=" * 27)
    
    print("\n1️⃣ Palindromic Squares:")
    palindromic_squares = []
    for i in range(1, 32):  # Check first 31 squares
        square = i ** 2
        if square == reverse_number_iterative_silent(square):
            palindromic_squares.append((i, square))
    
    print("   Numbers whose squares are palindromes:")
    for num, square in palindromic_squares[:10]:
        print(f"   {num}² = {square}")
    
    print("\n2️⃣ Sum with Reverse:")
    print("   Numbers where n + reverse(n) gives interesting results:")
    for n in [19, 47, 58, 89, 169]:
        rev_n = reverse_number_iterative_silent(n)
        sum_result = n + rev_n
        print(f"   {n} + {rev_n} = {sum_result}")
    
    print("\n3️⃣ Kaprekar-like Process:")
    print("   Example: Start with 1234")
    num = 1234
    for step in range(5):
        rev_num = reverse_number_iterative_silent(num)
        if num > rev_num:
            diff = num - rev_num
            print(f"   Step {step + 1}: {num} - {rev_num} = {diff}")
            num = diff
        else:
            diff = rev_num - num
            print(f"   Step {step + 1}: {rev_num} - {num} = {diff}")
            num = diff
        
        if num == 0 or num == reverse_number_iterative_silent(num):
            print(f"   Process terminates at palindrome: {num}")
            break

# =============================================================================
# PRACTICAL APPLICATIONS
# =============================================================================

def practical_applications():
    """
    Show practical applications of number reversal
    """
    print(f"\n🎯 PRACTICAL APPLICATIONS")
    print("=" * 25)
    
    print("\n1️⃣ Data Validation:")
    print("   Check if a number is the same when reversed (palindrome)")
    test_ids = [12321, 45654, 12345]
    for id_num in test_ids:
        rev_id = reverse_number_iterative_silent(id_num)
        is_valid = (id_num == rev_id)
        print(f"   ID {id_num}: {'Valid' if is_valid else 'Invalid'} palindrome")
    
    print("\n2️⃣ Cryptography - Simple Encoding:")
    print("   Reverse digits as basic encoding step")
    original_code = 98765
    encoded = reverse_number_iterative_silent(original_code)
    decoded = reverse_number_iterative_silent(encoded)
    print(f"   Original: {original_code}")
    print(f"   Encoded:  {encoded}")
    print(f"   Decoded:  {decoded}")
    
    print("\n3️⃣ Number Games and Puzzles:")
    print("   Create challenging number puzzles")
    puzzle_nums = [142, 263, 487]
    print("   Find the pattern:")
    for num in puzzle_nums:
        rev_num = reverse_number_iterative_silent(num)
        sum_digits = sum(int(d) for d in str(num))
        print(f"   {num} → reverse: {rev_num}, digit sum: {sum_digits}")
    
    print("\n4️⃣ Algorithm Analysis:")
    print("   Test sorting algorithms with reversed data")
    original_list = [123, 456, 789]
    reversed_list = [reverse_number_iterative_silent(x) for x in original_list]
    print(f"   Original: {original_list}")
    print(f"   Reversed: {reversed_list}")
    print(f"   Sorted:   {sorted(reversed_list)}")

# =============================================================================
# INTERACTIVE NUMBER REVERSER
# =============================================================================

def interactive_number_reverser():
    """
    Interactive number reversal tool with multiple options
    """
    print(f"\n🎮 INTERACTIVE NUMBER REVERSER")
    print("=" * 30)
    
    while True:
        try:
            print(f"\n🎯 Choose an option:")
            print("   1. Reverse single number (iterative)")
            print("   2. Reverse single number (recursive)")
            print("   3. Reverse with string method")
            print("   4. Reverse with validation and analysis")
            print("   5. Find palindromic numbers in range")
            print("   6. Analyze reversal properties")
            print("   7. Explore number patterns")
            print("   8. Batch reverse multiple numbers")
            print("   9. Learn about number reversal")
            print("   10. Exit")
            
            choice = input("\nEnter your choice (1-10): ").strip()
            
            if choice == "1":
                num = int(input("Enter a number to reverse: "))
                reverse_number_iterative(num)
                
            elif choice == "2":
                num = int(input("Enter a number to reverse: "))
                result = reverse_number_recursive_verbose(num)
                print(f"   🎯 Final result: {result}")
                
            elif choice == "3":
                num = int(input("Enter a number to reverse: "))
                reverse_number_string_method(num)
                
            elif choice == "4":
                num = int(input("Enter a number for analysis: "))
                reverse_with_validation(num)
                
            elif choice == "5":
                start = int(input("Enter start of range: "))
                end = int(input("Enter end of range: "))
                find_palindromic_numbers(start, end)
                
            elif choice == "6":
                numbers_input = input("Enter numbers separated by commas: ")
                numbers = [int(x.strip()) for x in numbers_input.split(',')]
                analyze_reversal_properties(numbers)
                
            elif choice == "7":
                number_reversal_patterns()
                
            elif choice == "8":
                numbers_input = input("Enter numbers separated by commas: ")
                numbers = [int(x.strip()) for x in numbers_input.split(',')]
                
                print(f"\n📊 Batch Reversal Results:")
                print("   ┌──────────┬──────────┬─────────────┐")
                print("   │ Original │ Reversed │ Palindrome? │")
                print("   ├──────────┼──────────┼─────────────┤")
                
                for num in numbers:
                    rev_num = reverse_number_iterative_silent(num)
                    is_palindrome = (num == rev_num)
                    palindrome_str = "Yes" if is_palindrome else "No"
                    print(f"   │ {num:>8} │ {rev_num:>8} │ {palindrome_str:>11} │")
                
                print("   └──────────┴──────────┴─────────────┘")
                
            elif choice == "9":
                explain_number_reversal_concepts()
                
            elif choice == "10":
                print("\n👋 Thanks for exploring number reversal!")
                break
                
            else:
                print("❌ Invalid choice. Please choose 1-10.")
                
        except ValueError:
            print("❌ Please enter valid numbers!")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break

if __name__ == "__main__":
    """
    Main execution demonstrating number reversal concepts and applications
    """
    print(__doc__)
    
    # Educational content
    explain_number_reversal_concepts()
    
    # Demonstrate different methods with sample numbers
    sample_numbers = [1234, 5670, -789, 12321, 100]
    
    for number in sample_numbers:
        print(f"\n" + "="*60)
        print(f"DEMONSTRATION: Reversing {number}")
        print("="*60)
        
        # Show different approaches
        reverse_number_iterative(number)
        reverse_number_string_method(number)
        
        # Show recursive method for smaller numbers
        if abs(number) < 10000:
            result = reverse_number_recursive_verbose(number)
        
        # Comprehensive analysis
        reverse_with_validation(number)
    
    # Pattern analysis
    print(f"\n" + "="*60)
    print("PATTERN ANALYSIS")
    print("="*60)
    number_reversal_patterns()
    
    # Properties analysis
    test_numbers = [123, 456, 121, 1001, 12321, 9876]
    analyze_reversal_properties(test_numbers)
    
    # Find palindromes
    find_palindromic_numbers(1, 1000)
    
    # Show practical applications
    practical_applications()
    
    # Interactive session
    interactive_number_reverser()
    
    print("\n" + "=" * 50)
    print("🎓 LEARNING SUMMARY")
    print("=" * 50)
    print("✅ Understanding of digit extraction and number manipulation")
    print("✅ Multiple algorithmic approaches to number reversal")
    print("✅ Mathematical properties and pattern recognition")
    print("✅ Loop structures and recursive thinking")
    print("✅ Practical applications in programming and mathematics")
    
    print("\n💡 Key Concepts Learned:")
    print("• Modulo and integer division for digit manipulation")
    print("• Iterative vs recursive algorithm design")
    print("• String manipulation as alternative approach")
    print("• Mathematical properties of palindromic numbers")
    print("• Input validation and edge case handling")
    
    print("\n🎯 Next Steps:")
    print("• Study advanced digit manipulation algorithms")
    print("• Explore number theory and palindromic sequences")
    print("• Learn about big integer handling for large numbers")
    print("• Investigate cryptographic applications of number operations")


