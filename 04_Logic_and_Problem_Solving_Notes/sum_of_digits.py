"""
Sum of Digits Calculator - Digit Manipulation and Mathematical Analysis
====================================================================

Comprehensive digit summation system with multiple algorithms, mathematical
properties analysis, and practical applications. Demonstrates digit extraction,
accumulation patterns, and number theory concepts.

Author: Python Learning Notes
Date: September 2025
Topic: Digit Manipulation, Mathematical Properties, Number Theory
"""

import math
from typing import List, Tuple, Union

# =============================================================================
# MATHEMATICAL CONCEPTS AND DIGIT THEORY
# =============================================================================

def explain_digit_sum_concepts():
    """
    Educational explanation of digit summation and related concepts
    """
    print("🔢 DIGIT SUMMATION CONCEPTS")
    print("=" * 27)
    
    print("\n📚 What is Sum of Digits?")
    print("Sum of digits is:")
    print("   • Adding all individual digits in a number")
    print("   • A fundamental operation in number theory")
    print("   • Used in divisibility tests and mathematical proofs")
    print("   • Foundation for digital root calculations")
    
    print("\n🧮 Mathematical Foundation:")
    print("For a number like 1234:")
    print("   • Individual digits: 1, 2, 3, 4")
    print("   • Sum process: 1 + 2 + 3 + 4 = 10")
    print("   • Each digit contributes to the total")
    
    print("\n🔍 Step-by-Step Process:")
    number = 1234
    print(f"   Original number: {number}")
    
    temp = number
    digit_sum = 0
    digits = []
    
    print("   Digit extraction:")
    while temp > 0:
        digit = temp % 10
        digits.append(digit)
        digit_sum += digit
        temp //= 10
        print(f"   Extract {digit}, running sum = {digit_sum}")
    
    digits.reverse()  # Show in original order
    print(f"   Digits (left to right): {digits}")
    print(f"   Final sum: {' + '.join(map(str, digits))} = {digit_sum}")
    
    print("\n📊 Applications and Properties:")
    applications = [
        ("Divisibility by 3", "Sum divisible by 3 → number divisible by 3"),
        ("Divisibility by 9", "Sum divisible by 9 → number divisible by 9"),
        ("Digital Root", "Repeatedly sum until single digit"),
        ("Check Digits", "Validation in credit cards, ISBN"),
        ("Hash Functions", "Simple checksum calculations")
    ]
    
    print("   ┌─────────────────┬─────────────────────────────────────┐")
    print("   │ Application     │ Description                         │")
    print("   ├─────────────────┼─────────────────────────────────────┤")
    for app, desc in applications:
        print(f"   │ {app:<15} │ {desc:<35} │")
    print("   └─────────────────┴─────────────────────────────────────┘")

# =============================================================================
# BASIC DIGIT SUM ALGORITHMS
# =============================================================================

def sum_digits_iterative(n):
    """
    Basic iterative approach to sum digits
    
    Time Complexity: O(log n) - where n is the input number
    Space Complexity: O(1)
    
    Args:
        n (int): Number whose digits to sum
        
    Returns:
        int: Sum of digits
    """
    original = n
    print(f"\n🔄 Iterative Method for {original}")
    print("=" * 25)
    
    if n == 0:
        print("   Special case: 0 has digit sum 0")
        return 0
    
    # Handle negative numbers
    if n < 0:
        n = abs(n)
        print(f"   Negative number: working with absolute value {n}")
    
    digit_sum = 0
    step = 1
    digits_found = []
    
    print("   Step-by-step extraction:")
    print(f"   Initial: number = {n}, sum = {digit_sum}")
    
    while n > 0:
        # Extract the last digit
        digit = n % 10
        digits_found.append(digit)
        
        # Add to sum
        digit_sum += digit
        
        # Remove the last digit
        n = n // 10
        
        print(f"   Step {step}: Extract {digit} → sum = {digit_sum}, remaining = {n}")
        step += 1
    
    # Show digits in original order
    digits_found.reverse()
    print(f"\n   📊 Analysis:")
    print(f"   • Digits (left to right): {digits_found}")
    print(f"   • Number of digits: {len(digits_found)}")
    print(f"   • Sum calculation: {' + '.join(map(str, digits_found))} = {digit_sum}")
    print(f"   ✅ Final result: {digit_sum}")
    
    return digit_sum

def sum_digits_string_method(n):
    """
    String-based approach to sum digits
    
    Method: Convert to string, iterate through characters
    """
    original = n
    print(f"\n📝 String Method for {original}")
    print("=" * 20)
    
    # Handle negative numbers
    if n < 0:
        n = abs(n)
        print(f"   Negative number: working with {n}")
    
    # Convert to string
    str_number = str(n)
    print(f"   String representation: '{str_number}'")
    
    digit_sum = 0
    calculations = []
    
    print("   Character-by-character processing:")
    for i, char in enumerate(str_number):
        digit = int(char)
        digit_sum += digit
        calculations.append(str(digit))
        print(f"   Position {i}: '{char}' → {digit}, running sum = {digit_sum}")
    
    print(f"\n   📊 Summary:")
    print(f"   • Calculation: {' + '.join(calculations)} = {digit_sum}")
    print(f"   ✅ Result: {digit_sum}")
    
    return digit_sum

def sum_digits_recursive(n, digit_sum=0):
    """
    Recursive approach to sum digits
    """
    if n == 0:
        return digit_sum
    
    digit = n % 10
    return sum_digits_recursive(n // 10, digit_sum + digit)

def sum_digits_recursive_verbose(n, digit_sum=0, depth=0):
    """
    Verbose recursive approach with call stack visualization
    """
    indent = "  " * depth
    
    if depth == 0:
        print(f"\n🔁 Recursive Method for {n}")
        print("=" * 20)
        print("   Call stack visualization:")
    
    print(f"{indent}📞 sum_digits({n}, {digit_sum})")
    
    # Base case
    if n == 0:
        print(f"{indent}   Base case reached, returning {digit_sum}")
        return digit_sum
    
    # Extract digit and make recursive call
    digit = n % 10
    remaining = n // 10
    new_sum = digit_sum + digit
    
    print(f"{indent}   Extract digit {digit}, new sum = {new_sum}")
    
    result = sum_digits_recursive_verbose(remaining, new_sum, depth + 1)
    
    print(f"{indent}   Returning {result}")
    return result

# =============================================================================
# ADVANCED DIGIT SUM FEATURES
# =============================================================================

def sum_digits_with_analysis(n):
    """
    Comprehensive digit sum with detailed analysis
    """
    original = n
    print(f"\n🔬 Comprehensive Analysis for {original}")
    print("=" * 30)
    
    if n == 0:
        print("   Special case: Zero")
        return 0, {"digits": [0], "properties": ["zero"]}
    
    # Handle negative numbers
    is_negative = n < 0
    if is_negative:
        n = abs(n)
        print(f"   Negative number: analyzing {n}")
    
    # Extract all digits
    digits = []
    temp = n
    while temp > 0:
        digits.append(temp % 10)
        temp //= 10
    
    digits.reverse()  # Original order
    
    # Calculate sum
    digit_sum = sum(digits)
    
    # Analyze properties
    properties = []
    
    # Even/odd analysis
    even_digits = [d for d in digits if d % 2 == 0]
    odd_digits = [d for d in digits if d % 2 == 1]
    
    print(f"   📊 Digit Analysis:")
    print(f"   • All digits: {digits}")
    print(f"   • Even digits: {even_digits} (count: {len(even_digits)})")
    print(f"   • Odd digits: {odd_digits} (count: {len(odd_digits)})")
    print(f"   • Digit sum: {digit_sum}")
    
    # Mathematical properties
    print(f"\n   🧮 Mathematical Properties:")
    
    if digit_sum % 3 == 0:
        properties.append("divisible_by_3")
        print(f"   ✓ Original number {original} is divisible by 3 (sum = {digit_sum})")
    
    if digit_sum % 9 == 0:
        properties.append("divisible_by_9")
        print(f"   ✓ Original number {original} is divisible by 9 (sum = {digit_sum})")
    
    # Check if palindromic sum
    digit_sum_str = str(digit_sum)
    if digit_sum_str == digit_sum_str[::-1]:
        properties.append("palindromic_sum")
        print(f"   ✓ Digit sum {digit_sum} is palindromic")
    
    # Digit patterns
    if len(set(digits)) == 1:
        properties.append("all_same_digits")
        print(f"   ✓ All digits are the same: {digits[0]}")
    
    if digits == sorted(digits):
        properties.append("ascending_digits")
        print(f"   ✓ Digits are in ascending order")
    elif digits == sorted(digits, reverse=True):
        properties.append("descending_digits")
        print(f"   ✓ Digits are in descending order")
    
    return digit_sum, {
        "digits": digits,
        "properties": properties,
        "even_count": len(even_digits),
        "odd_count": len(odd_digits),
        "is_negative": is_negative
    }

def calculate_digital_root(n):
    """
    Calculate digital root (repeated digit sum until single digit)
    """
    original = n
    print(f"\n🌳 Digital Root Calculation for {original}")
    print("=" * 30)
    
    if n == 0:
        print("   Digital root of 0 is 0")
        return 0
    
    # Handle negative numbers
    if n < 0:
        n = abs(n)
        print(f"   Working with absolute value: {n}")
    
    step = 1
    while n >= 10:
        # Calculate sum of digits
        digit_sum = sum_digits_iterative_silent(n)
        print(f"   Step {step}: {n} → sum of digits = {digit_sum}")
        n = digit_sum
        step += 1
    
    print(f"\n   ✅ Digital root: {n}")
    
    # Mathematical formula for digital root
    # Digital root = 1 + (n-1) % 9 for n > 0, and 0 for n = 0
    if original != 0:
        formula_result = 1 + (abs(original) - 1) % 9
        print(f"   🧮 Formula verification: 1 + ({abs(original)}-1) % 9 = {formula_result}")
        if formula_result == n:
            print("   ✓ Formula matches iterative result")
    
    return n

def sum_digits_iterative_silent(n):
    """Silent version for internal use"""
    n = abs(n)
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    return digit_sum

# =============================================================================
# MATHEMATICAL PATTERNS AND PROPERTIES
# =============================================================================

def explore_digit_sum_patterns():
    """
    Explore mathematical patterns in digit sums
    """
    print(f"\n🎨 DIGIT SUM PATTERNS")
    print("=" * 20)
    
    print("\n1️⃣ Perfect Powers and Their Digit Sums:")
    print("   Squares (n²):")
    for i in range(1, 11):
        square = i ** 2
        digit_sum = sum_digits_iterative_silent(square)
        print(f"   {i}² = {square:3} → digit sum = {digit_sum}")
    
    print("\n   Cubes (n³):")
    for i in range(1, 8):
        cube = i ** 3
        digit_sum = sum_digits_iterative_silent(cube)
        print(f"   {i}³ = {cube:3} → digit sum = {digit_sum}")
    
    print("\n2️⃣ Fibonacci Sequence Digit Sums:")
    print("   First 10 Fibonacci numbers:")
    fib_a, fib_b = 0, 1
    for i in range(10):
        if i == 0:
            fib_current = 0
        elif i == 1:
            fib_current = 1
        else:
            fib_current = fib_a + fib_b
            fib_a, fib_b = fib_b, fib_current
        
        digit_sum = sum_digits_iterative_silent(fib_current)
        print(f"   F({i:2}) = {fib_current:3} → digit sum = {digit_sum}")
    
    print("\n3️⃣ Prime Numbers and Digit Sums:")
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    print("   First 15 primes:")
    for prime in primes:
        digit_sum = sum_digits_iterative_silent(prime)
        print(f"   {prime:2} → digit sum = {digit_sum}")

def analyze_digit_sum_frequency(start, end):
    """
    Analyze frequency of digit sums in a range
    """
    print(f"\n📊 Digit Sum Frequency Analysis [{start}, {end}]")
    print("=" * 40)
    
    frequency = {}
    
    for num in range(start, end + 1):
        digit_sum = sum_digits_iterative_silent(num)
        if digit_sum not in frequency:
            frequency[digit_sum] = 0
        frequency[digit_sum] += 1
    
    # Display frequency table
    print("   Digit Sum Frequency Distribution:")
    print("   ┌─────────────┬───────────┬─────────────┐")
    print("   │ Digit Sum   │ Count     │ Percentage  │")
    print("   ├─────────────┼───────────┼─────────────┤")
    
    total_numbers = end - start + 1
    
    for digit_sum in sorted(frequency.keys()):
        count = frequency[digit_sum]
        percentage = (count / total_numbers) * 100
        print(f"   │ {digit_sum:>9}   │ {count:>7}   │ {percentage:>8.1f}%   │")
    
    print("   └─────────────┴───────────┴─────────────┘")
    
    # Find most common
    most_common = max(frequency.items(), key=lambda x: x[1])
    print(f"\n   📈 Most common digit sum: {most_common[0]} ({most_common[1]} occurrences)")
    
    return frequency

def divisibility_tests_using_digit_sums():
    """
    Demonstrate divisibility tests using digit sums
    """
    print(f"\n🎯 DIVISIBILITY TESTS WITH DIGIT SUMS")
    print("=" * 35)
    
    test_numbers = [123, 456, 789, 1011, 2025, 3333]
    
    print("   Testing divisibility by 3 and 9:")
    print("   ┌──────────┬─────────────┬──────────────┬──────────────┐")
    print("   │ Number   │ Digit Sum   │ Div by 3?    │ Div by 9?    │")
    print("   ├──────────┼─────────────┼──────────────┼──────────────┤")
    
    for num in test_numbers:
        digit_sum = sum_digits_iterative_silent(num)
        
        div_by_3_sum = (digit_sum % 3 == 0)
        div_by_3_actual = (num % 3 == 0)
        div_by_9_sum = (digit_sum % 9 == 0)
        div_by_9_actual = (num % 9 == 0)
        
        div3_result = "Yes" if div_by_3_sum else "No"
        div9_result = "Yes" if div_by_9_sum else "No"
        
        # Verify accuracy
        div3_check = "✓" if div_by_3_sum == div_by_3_actual else "✗"
        div9_check = "✓" if div_by_9_sum == div_by_9_actual else "✗"
        
        print(f"   │ {num:>6}   │ {digit_sum:>9}   │ {div3_result:<8}{div3_check:>4} │ {div9_result:<8}{div9_check:>4} │")
    
    print("   └──────────┴─────────────┴──────────────┴──────────────┘")
    
    print(f"\n   📚 Rules:")
    print("   • Divisible by 3: Sum of digits divisible by 3")
    print("   • Divisible by 9: Sum of digits divisible by 9")
    print("   • ✓ = Test matches actual divisibility")

# =============================================================================
# PRACTICAL APPLICATIONS
# =============================================================================

def practical_applications():
    """
    Show practical applications of digit summation
    """
    print(f"\n🎯 PRACTICAL APPLICATIONS")
    print("=" * 25)
    
    print("\n1️⃣ Credit Card Validation (Luhn Algorithm Simplified):")
    card_number = "4532123456789012"
    print(f"   Card number: {card_number}")
    
    # Simple digit sum for demonstration
    digit_sum = sum(int(d) for d in card_number)
    print(f"   Sum of digits: {digit_sum}")
    print("   (Real Luhn algorithm uses weighted sums)")
    
    print("\n2️⃣ ISBN Check Digit:")
    isbn_partial = "978014312"
    print(f"   Partial ISBN: {isbn_partial}")
    
    digit_sum = sum(int(d) for d in isbn_partial)
    print(f"   Sum of digits: {digit_sum}")
    print("   Check digit calculation based on this sum")
    
    print("\n3️⃣ Digital Signature/Checksum:")
    data = "20250315"  # Date format YYYYMMDD
    checksum = sum_digits_iterative_silent(int(data))
    print(f"   Data: {data}")
    print(f"   Simple checksum: {checksum}")
    
    print("\n4️⃣ Game Score Validation:")
    player_scores = [1247, 856, 3392]
    print("   Player scores and their digit sums:")
    
    for i, score in enumerate(player_scores, 1):
        digit_sum = sum_digits_iterative_silent(score)
        print(f"   Player {i}: {score:4} → sum = {digit_sum:2}")

def number_games_with_digit_sums():
    """
    Interactive games involving digit sums
    """
    import random
    
    print(f"\n🎮 DIGIT SUM GAMES")
    print("=" * 17)
    
    print("\n🎯 Quick Calculation Challenge:")
    score = 0
    rounds = 5
    
    for round_num in range(rounds):
        # Generate random number
        number = random.randint(100, 9999)
        correct_sum = sum_digits_iterative_silent(number)
        
        try:
            print(f"\n   Round {round_num + 1}: Find sum of digits of {number}")
            user_answer = int(input("   Your answer: "))
            
            if user_answer == correct_sum:
                print("   ✅ Correct!")
                score += 1
            else:
                print(f"   ❌ Wrong! Correct answer: {correct_sum}")
                
        except ValueError:
            print(f"   ❌ Invalid input! Correct answer: {correct_sum}")
    
    print(f"\n   🏆 Final Score: {score}/{rounds}")
    percentage = (score / rounds) * 100
    
    if percentage == 100:
        print("   🌟 Perfect! You're a digit sum master!")
    elif percentage >= 80:
        print("   👍 Excellent work!")
    elif percentage >= 60:
        print("   👌 Good job! Keep practicing!")
    else:
        print("   📚 Keep working on your mental math!")

# =============================================================================
# INTERACTIVE DIGIT SUM CALCULATOR
# =============================================================================

def interactive_digit_sum_calculator():
    """
    Interactive calculator with multiple features
    """
    print(f"\n🎮 INTERACTIVE DIGIT SUM CALCULATOR")
    print("=" * 35)
    
    while True:
        try:
            print(f"\n🎯 Choose an option:")
            print("   1. Calculate digit sum (iterative)")
            print("   2. Calculate digit sum (recursive)")
            print("   3. Calculate with string method")
            print("   4. Comprehensive analysis")
            print("   5. Calculate digital root")
            print("   6. Analyze patterns in range")
            print("   7. Test divisibility rules")
            print("   8. Frequency analysis")
            print("   9. Play digit sum games")
            print("   10. Learn about digit sums")
            print("   11. Exit")
            
            choice = input("\nEnter your choice (1-11): ").strip()
            
            if choice == "1":
                num = int(input("Enter a number: "))
                sum_digits_iterative(num)
                
            elif choice == "2":
                num = int(input("Enter a number: "))
                result = sum_digits_recursive_verbose(num)
                print(f"   🎯 Final result: {result}")
                
            elif choice == "3":
                num = int(input("Enter a number: "))
                sum_digits_string_method(num)
                
            elif choice == "4":
                num = int(input("Enter a number: "))
                digit_sum, analysis = sum_digits_with_analysis(num)
                print(f"\n   📋 Summary: Digit sum = {digit_sum}")
                
            elif choice == "5":
                num = int(input("Enter a number: "))
                calculate_digital_root(num)
                
            elif choice == "6":
                explore_digit_sum_patterns()
                
            elif choice == "7":
                divisibility_tests_using_digit_sums()
                
            elif choice == "8":
                start = int(input("Enter start of range: "))
                end = int(input("Enter end of range: "))
                analyze_digit_sum_frequency(start, end)
                
            elif choice == "9":
                number_games_with_digit_sums()
                
            elif choice == "10":
                explain_digit_sum_concepts()
                
            elif choice == "11":
                print("\n👋 Thanks for exploring digit sums!")
                break
                
            else:
                print("❌ Invalid choice. Please choose 1-11.")
                
        except ValueError:
            print("❌ Please enter valid numbers!")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break

if __name__ == "__main__":
    """
    Main execution demonstrating digit sum concepts and applications
    """
    print(__doc__)
    
    # Educational content
    explain_digit_sum_concepts()
    
    # Demonstrate different methods with sample numbers
    sample_numbers = [1234, 5678, 999, 12321, 0, -456]
    
    for number in sample_numbers:
        print(f"\n" + "="*60)
        print(f"DEMONSTRATION: Sum of digits for {number}")
        print("="*60)
        
        # Show different approaches
        sum_digits_iterative(number)
        sum_digits_string_method(number)
        
        # Show recursive method for reasonable numbers
        if abs(number) < 100000:
            result = sum_digits_recursive_verbose(abs(number))
        
        # Comprehensive analysis
        digit_sum, analysis = sum_digits_with_analysis(number)
        
        # Digital root
        if number != 0:
            calculate_digital_root(abs(number))
    
    # Pattern exploration
    print(f"\n" + "="*60)
    print("PATTERN ANALYSIS")
    print("="*60)
    explore_digit_sum_patterns()
    
    # Frequency analysis
    analyze_digit_sum_frequency(1, 100)
    
    # Divisibility tests
    divisibility_tests_using_digit_sums()
    
    # Practical applications
    practical_applications()
    
    # Interactive games
    play_games = input("\n🎮 Would you like to play digit sum games? (y/n): ").lower()
    if play_games == 'y':
        number_games_with_digit_sums()
    
    # Interactive calculator
    interactive_digit_sum_calculator()
    
    print("\n" + "=" * 50)
    print("🎓 LEARNING SUMMARY")
    print("=" * 50)
    print("✅ Understanding of digit extraction and summation")
    print("✅ Multiple algorithmic approaches to digit sum calculation")
    print("✅ Mathematical properties and pattern recognition")
    print("✅ Digital root concept and calculation methods")
    print("✅ Practical applications in validation and checksums")
    
    print("\n💡 Key Concepts Learned:")
    print("• Digit extraction using modulo and integer division")
    print("• Iterative vs recursive vs string-based approaches")
    print("• Mathematical properties (divisibility by 3 and 9)")
    print("• Digital root calculation and significance")
    print("• Pattern analysis in number sequences")
    
    print("\n🎯 Next Steps:")
    print("• Study advanced number theory concepts")
    print("• Explore weighted digit sum algorithms (Luhn, etc.)")
    print("• Learn about digital signatures and cryptography")
    print("• Investigate mathematical sequences and their properties")