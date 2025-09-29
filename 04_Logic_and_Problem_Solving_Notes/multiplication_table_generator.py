"""
Multiplication Table Generator - Loops and Mathematical Patterns
=============================================================

Comprehensive multiplication table generation system with various formatting
styles, customizable ranges, and mathematical pattern analysis. Demonstrates
loop structures, string formatting, and mathematical relationships.

Author: Python Learning Notes
Date: September 2025
Topic: Loops, Mathematical Tables, String Formatting, Patterns
"""

import math
from typing import List, Tuple, Optional

# =============================================================================
# MATHEMATICAL CONCEPTS AND THEORY
# =============================================================================

def explain_multiplication_concepts():
    """
    Educational explanation of multiplication and table concepts
    """
    print("✖️  MULTIPLICATION AND TABLE CONCEPTS")
    print("=" * 38)
    
    print("\n📚 What is Multiplication?")
    print("Multiplication is:")
    print("   • Repeated addition of the same number")
    print("   • A fundamental arithmetic operation")
    print("   • The basis for many mathematical concepts")
    print("   • Essential for understanding patterns and relationships")
    
    print("\n🔢 Understanding Multiplication Tables:")
    print("A multiplication table shows:")
    print("   • Products of a number with consecutive integers")
    print("   • Mathematical patterns and relationships")
    print("   • Foundation for mental math skills")
    print("   • Building blocks for advanced mathematics")
    
    print("\n📊 Example - Table of 3:")
    print("   3 × 1 = 3   (3)")
    print("   3 × 2 = 6   (3 + 3)")
    print("   3 × 3 = 9   (3 + 3 + 3)")
    print("   3 × 4 = 12  (3 + 3 + 3 + 3)")
    print("   Pattern: Each result increases by 3")
    
    print("\n🎯 Properties of Multiplication:")
    properties = [
        ("Commutative", "a × b = b × a", "3 × 4 = 4 × 3 = 12"),
        ("Associative", "(a × b) × c = a × (b × c)", "(2 × 3) × 4 = 2 × (3 × 4) = 24"),
        ("Identity", "a × 1 = a", "7 × 1 = 7"),
        ("Zero Property", "a × 0 = 0", "9 × 0 = 0"),
        ("Distributive", "a × (b + c) = a×b + a×c", "3 × (4 + 5) = 3×4 + 3×5 = 27")
    ]
    
    print("   ┌─────────────┬─────────────────────┬─────────────────┐")
    print("   │ Property    │ Rule                │ Example         │")
    print("   ├─────────────┼─────────────────────┼─────────────────┤")
    for prop, rule, example in properties:
        print(f"   │ {prop:<11} │ {rule:<19} │ {example:<15} │")
    print("   └─────────────┴─────────────────────┴─────────────────┘")

# =============================================================================
# BASIC MULTIPLICATION TABLE GENERATION
# =============================================================================

def generate_basic_table(number, start=1, end=10):
    """
    Generate basic multiplication table with step-by-step explanation
    
    Args:
        number (int): Number for which to generate table
        start (int): Starting multiplier (default: 1)
        end (int): Ending multiplier (default: 10)
    """
    print(f"\n📋 Basic Multiplication Table for {number}")
    print("=" * 35)
    print(f"   Range: {start} to {end}")
    print("   Format: {number} × multiplier = result")
    print()
    
    results = []
    
    for i in range(start, end + 1):
        result = number * i
        results.append((i, result))
        
        # Show calculation process for first few
        if i <= start + 2:
            print(f"   Step {i}: {number} × {i} = {result}")
        else:
            print(f"   {number} × {i:2} = {result:3}")
    
    print(f"\n   ✅ Generated {len(results)} multiplication facts")
    return results

def generate_formatted_table(number, start=1, end=10, width=3):
    """
    Generate beautifully formatted multiplication table
    """
    print(f"\n🎨 Formatted Table for {number}")
    print("=" * 25)
    
    # Table header
    print(f"   ┌─────────────┬──────────┐")
    print(f"   │ Expression  │  Result  │")
    print(f"   ├─────────────┼──────────┤")
    
    # Table rows
    for i in range(start, end + 1):
        result = number * i
        expression = f"{number} × {i:2}"
        print(f"   │ {expression:<11} │ {result:>8} │")
    
    print(f"   └─────────────┴──────────┘")
    
    # Summary statistics
    total = sum(number * i for i in range(start, end + 1))
    average = total / (end - start + 1)
    
    print(f"\n   📊 Statistics:")
    print(f"   • Sum of all results: {total:,}")
    print(f"   • Average result: {average:.2f}")
    print(f"   • Smallest result: {number * start}")
    print(f"   • Largest result: {number * end}")

# =============================================================================
# ADVANCED TABLE FORMATS
# =============================================================================

def generate_horizontal_table(number, start=1, end=10):
    """
    Generate horizontal multiplication table layout
    """
    print(f"\n↔️  Horizontal Table for {number}")
    print("=" * 27)
    
    # Multipliers row
    multipliers = "×  │ " + " │ ".join(f"{i:2}" for i in range(start, end + 1)) + " │"
    print(f"   {multipliers}")
    
    # Separator
    separator = "───┼" + "┼".join("────" for _ in range(start, end + 1)) + "┼"
    print(f"   {separator}")
    
    # Results row
    results = f"{number:2} │ " + " │ ".join(f"{number * i:2}" for i in range(start, end + 1)) + " │"
    print(f"   {results}")
    
    print(f"\n   Reading: {number} × column_number = cell_value")

def generate_grid_table(max_number=10):
    """
    Generate complete multiplication grid (times table chart)
    """
    print(f"\n📊 Complete Multiplication Grid (1 to {max_number})")
    print("=" * 40)
    
    # Header row with multipliers
    print("    ×", end="")
    for i in range(1, max_number + 1):
        print(f"{i:4}", end="")
    print()
    
    # Separator line
    print("  " + "─" * (4 * max_number + 3))
    
    # Table rows
    for i in range(1, max_number + 1):
        print(f"{i:3} │", end="")
        for j in range(1, max_number + 1):
            result = i * j
            print(f"{result:4}", end="")
        print()
    
    print(f"\n   📖 How to read: Row × Column = Cell value")
    print(f"   Example: Row 4 × Column 7 = 28")

def generate_visual_table(number, start=1, end=10):
    """
    Generate visually enhanced table with bars and patterns
    """
    print(f"\n🎯 Visual Multiplication Table for {number}")
    print("=" * 35)
    
    max_result = number * end
    max_bar_length = 30
    
    for i in range(start, end + 1):
        result = number * i
        
        # Calculate bar length proportional to result
        bar_length = int((result / max_result) * max_bar_length)
        bar = "█" * bar_length
        
        # Format the display
        expression = f"{number} × {i:2} = {result:3}"
        print(f"   {expression} │{bar}")
    
    print(f"\n   📏 Bar length represents result magnitude")
    print(f"   Longest bar = {max_result} (largest result)")

# =============================================================================
# PATTERN ANALYSIS AND EXPLORATION
# =============================================================================

def analyze_multiplication_patterns(number, end=20):
    """
    Analyze mathematical patterns in multiplication tables
    """
    print(f"\n🔍 Pattern Analysis for Table of {number}")
    print("=" * 35)
    
    results = [number * i for i in range(1, end + 1)]
    
    print(f"   First {end} multiples: {results[:10]}...")
    
    # Pattern 1: Difference between consecutive terms
    differences = [results[i] - results[i-1] for i in range(1, len(results))]
    print(f"\n   🔢 Consecutive differences: {set(differences)}")
    print(f"   Pattern: All differences are {number} (constant)")
    
    # Pattern 2: Sum of digits patterns
    print(f"\n   🧮 Sum of digits patterns:")
    digit_sums = []
    for i, result in enumerate(results[:10], 1):
        digit_sum = sum(int(digit) for digit in str(result))
        digit_sums.append(digit_sum)
        print(f"   {number} × {i:2} = {result:3} → digit sum = {digit_sum}")
    
    # Pattern 3: Even/Odd analysis
    even_count = sum(1 for r in results[:10] if r % 2 == 0)
    odd_count = 10 - even_count
    
    print(f"\n   ⚖️  Even/Odd distribution:")
    print(f"   Even results: {even_count}/10")
    print(f"   Odd results: {odd_count}/10")
    
    if number % 2 == 0:
        print(f"   Pattern: Since {number} is even, all results are even")
    else:
        print(f"   Pattern: Since {number} is odd, results alternate even/odd")
    
    # Pattern 4: Divisibility patterns
    print(f"\n   🔄 Divisibility patterns:")
    for divisor in [2, 3, 5, 9]:
        divisible_count = sum(1 for r in results[:10] if r % divisor == 0)
        print(f"   Divisible by {divisor}: {divisible_count}/10 results")

def find_multiplication_relationships(number):
    """
    Find interesting mathematical relationships
    """
    print(f"\n🔗 Mathematical Relationships for {number}")
    print("=" * 35)
    
    # Square and cube
    square = number ** 2
    cube = number ** 3
    print(f"   {number}² = {square}")
    print(f"   {number}³ = {cube}")
    
    # Factors
    factors = [i for i in range(1, number + 1) if number % i == 0]
    print(f"   Factors of {number}: {factors}")
    
    # Prime factorization
    def prime_factors(n):
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors
    
    if number > 1:
        pf = prime_factors(number)
        print(f"   Prime factorization: {' × '.join(map(str, pf))}")
    
    # Special properties
    if number == sum(factors[:-1]):  # Perfect number check
        print(f"   🌟 {number} is a perfect number!")
    
    if len(str(number)) > 1:
        digit_sum = sum(int(d) for d in str(number))
        print(f"   Sum of digits: {digit_sum}")

# =============================================================================
# INTERACTIVE TABLE GENERATOR
# =============================================================================

def interactive_table_generator():
    """
    Interactive multiplication table generator with multiple options
    """
    print(f"\n🎮 INTERACTIVE TABLE GENERATOR")
    print("=" * 30)
    
    while True:
        try:
            print(f"\n🎯 Choose an option:")
            print("   1. Generate basic table")
            print("   2. Generate formatted table")
            print("   3. Generate horizontal table")
            print("   4. Generate complete multiplication grid")
            print("   5. Generate visual table with bars")
            print("   6. Analyze patterns")
            print("   7. Custom range table")
            print("   8. Multiple tables comparison")
            print("   9. Learn about multiplication")
            print("   10. Exit")
            
            choice = input("\nEnter your choice (1-10): ").strip()
            
            if choice == "1":
                number = int(input("Enter number for table: "))
                generate_basic_table(number)
                
            elif choice == "2":
                number = int(input("Enter number for table: "))
                generate_formatted_table(number)
                
            elif choice == "3":
                number = int(input("Enter number for table: "))
                generate_horizontal_table(number)
                
            elif choice == "4":
                size = int(input("Enter grid size (e.g., 12 for 12×12): "))
                generate_grid_table(size)
                
            elif choice == "5":
                number = int(input("Enter number for visual table: "))
                generate_visual_table(number)
                
            elif choice == "6":
                number = int(input("Enter number for pattern analysis: "))
                analyze_multiplication_patterns(number)
                find_multiplication_relationships(number)
                
            elif choice == "7":
                number = int(input("Enter number for table: "))
                start = int(input("Enter starting multiplier: "))
                end = int(input("Enter ending multiplier: "))
                generate_basic_table(number, start, end)
                
            elif choice == "8":
                numbers = input("Enter numbers separated by commas: ")
                numbers = [int(x.strip()) for x in numbers.split(',')]
                compare_multiple_tables(numbers)
                
            elif choice == "9":
                explain_multiplication_concepts()
                
            elif choice == "10":
                print("\n👋 Thanks for exploring multiplication tables!")
                break
                
            else:
                print("❌ Invalid choice. Please choose 1-10.")
                
        except ValueError:
            print("❌ Please enter valid numbers!")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break

def compare_multiple_tables(numbers, range_end=10):
    """
    Compare multiplication tables for multiple numbers side by side
    """
    print(f"\n📊 Comparing Tables: {', '.join(map(str, numbers))}")
    print("=" * 40)
    
    # Header
    header = "  × │"
    for num in numbers:
        header += f" {num:>4} │"
    print(header)
    
    # Separator
    separator = "────┼" + "──────┼" * len(numbers)
    print(separator)
    
    # Rows
    for i in range(1, range_end + 1):
        row = f" {i:2} │"
        for num in numbers:
            result = num * i
            row += f" {result:>4} │"
        print(row)
    
    print(f"\n   📝 Reading: Multiplier × Table_Number = Result")

# =============================================================================
# PRACTICAL APPLICATIONS
# =============================================================================

def practical_applications():
    """
    Show real-world applications of multiplication tables
    """
    print(f"\n🎯 PRACTICAL APPLICATIONS")
    print("=" * 25)
    
    print("\n1️⃣ Shopping and Pricing:")
    item_price = 12
    quantities = [1, 2, 3, 4, 5]
    print(f"   Item price: ${item_price}")
    print("   Quantity pricing:")
    for qty in quantities:
        total = item_price * qty
        print(f"   {qty} items × ${item_price} = ${total}")
    
    print("\n2️⃣ Time Calculations:")
    hours_per_day = 8
    print(f"   Working {hours_per_day} hours per day:")
    for days in range(1, 8):
        total_hours = hours_per_day * days
        print(f"   {days} day{'s' if days > 1 else ''}: {total_hours} hours")
    
    print("\n3️⃣ Area Calculations:")
    width = 7
    print(f"   Rectangle with width {width} units:")
    for length in range(1, 11):
        area = width * length
        print(f"   {width} × {length} = {area} square units")
    
    print("\n4️⃣ Scaling Recipes:")
    base_servings = 4
    ingredient_amount = 2  # cups
    print(f"   Recipe for {base_servings} people uses {ingredient_amount} cups:")
    for people in [2, 6, 8, 10, 12]:
        multiplier = people / base_servings
        needed = ingredient_amount * multiplier
        print(f"   For {people} people: {needed} cups")

def multiplication_games():
    """
    Interactive multiplication games and exercises
    """
    import random
    
    print(f"\n🎮 MULTIPLICATION GAMES")
    print("=" * 22)
    
    print("\n🎯 Quick Quiz Game:")
    score = 0
    questions = 5
    
    for i in range(questions):
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        correct_answer = a * b
        
        try:
            user_answer = int(input(f"   Question {i+1}: {a} × {b} = "))
            
            if user_answer == correct_answer:
                print("   ✅ Correct!")
                score += 1
            else:
                print(f"   ❌ Wrong! The answer is {correct_answer}")
                
        except ValueError:
            print(f"   ❌ Invalid input! The answer was {correct_answer}")
    
    print(f"\n   🏆 Final Score: {score}/{questions}")
    percentage = (score / questions) * 100
    print(f"   Percentage: {percentage:.1f}%")
    
    if percentage >= 80:
        print("   🌟 Excellent work!")
    elif percentage >= 60:
        print("   👍 Good job!")
    else:
        print("   📚 Keep practicing!")

if __name__ == "__main__":
    """
    Main execution demonstrating multiplication table concepts
    """
    print(__doc__)
    
    # Educational content
    explain_multiplication_concepts()
    
    # Demonstrate different table formats
    sample_numbers = [3, 7, 9, 12]
    
    for number in sample_numbers:
        print(f"\n" + "="*60)
        print(f"DEMONSTRATION: Multiplication Table for {number}")
        print("="*60)
        
        # Show different formats
        generate_basic_table(number, 1, 8)
        generate_formatted_table(number, 1, 8)
        generate_visual_table(number, 1, 8)
        
        # Pattern analysis
        analyze_multiplication_patterns(number, 15)
        find_multiplication_relationships(number)
    
    # Show grid table
    print(f"\n" + "="*60)
    print("COMPLETE MULTIPLICATION GRID")
    print("="*60)
    generate_grid_table(8)
    
    # Show practical applications
    practical_applications()
    
    # Interactive games
    play_games = input("\n🎮 Would you like to play multiplication games? (y/n): ").lower()
    if play_games == 'y':
        multiplication_games()
    
    # Interactive session
    interactive_table_generator()
    
    print("\n" + "=" * 50)
    print("🎓 LEARNING SUMMARY")
    print("=" * 50)
    print("✅ Understanding of multiplication concepts and properties")
    print("✅ Multiple table generation and formatting techniques")
    print("✅ Pattern recognition in mathematical sequences")
    print("✅ Loop structures and iteration concepts")
    print("✅ Real-world applications of multiplication")
    
    print("\n💡 Key Concepts Learned:")
    print("• Multiplication as repeated addition")
    print("• Loop structures for pattern generation")
    print("• String formatting and table presentation")
    print("• Mathematical pattern analysis")
    print("• Practical problem-solving applications")
    
    print("\n🎯 Next Steps:")
    print("• Explore division tables and inverse operations")
    print("• Study modular arithmetic and remainders")
    print("• Learn about prime factorization")
    print("• Investigate mathematical sequences and series")
