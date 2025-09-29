"""
Sort Three Numbers - Sorting Algorithms and Comparison Logic
=========================================================

Comprehensive exploration of sorting three numbers using various approaches
including manual sorting, built-in functions, and algorithmic methods.
Demonstrates sorting concepts, comparison logic, and algorithm efficiency.

Author: Python Learning Notes
Date: September 2025
Topic: Sorting Algorithms, Comparison Logic, Data Arrangement
"""

from typing import List, Tuple, Union
import time
import random

# =============================================================================
# SORTING CONCEPTS AND THEORY
# =============================================================================

def explain_sorting_concepts():
    """
    Educational explanation of sorting algorithms and concepts
    """
    print("📊 SORTING CONCEPTS AND THEORY")
    print("=" * 30)
    
    print("\n📚 What is Sorting?")
    print("Sorting is the process of:")
    print("   • Arranging data in a specific order (ascending/descending)")
    print("   • Organizing information for efficient access")
    print("   • Implementing fundamental computer science algorithms")
    print("   • Preparing data for search and analysis operations")
    
    print("\n🔄 Common Sorting Orders:")
    print("   • Ascending: Smallest to largest (1, 2, 3, 4, 5)")
    print("   • Descending: Largest to smallest (5, 4, 3, 2, 1)")
    print("   • Alphabetical: Dictionary order (A, B, C...)")
    print("   • Reverse Alphabetical: Reverse dictionary order (Z, Y, X...)")
    
    print("\n⚖️  Comparison Operations:")
    print("   Sorting relies on comparison operators:")
    print("   • Less than (<): 3 < 5 → True")
    print("   • Greater than (>): 7 > 4 → True")
    print("   • Equal to (==): 5 == 5 → True")
    print("   • Less than or equal (<=): 3 <= 3 → True")
    print("   • Greater than or equal (>=): 6 >= 2 → True")
    
    print("\n🎯 Why Learn Sorting?")
    print("   • Foundation for algorithm design")
    print("   • Improves search efficiency")
    print("   • Essential for data analysis")
    print("   • Required for many advanced algorithms")
    
    print("\n📈 Algorithm Complexity Preview:")
    algorithms = [
        ("Manual (3 numbers)", "O(1)", "Fixed comparisons"),
        ("Bubble Sort", "O(n²)", "Simple but slow"),
        ("Quick Sort", "O(n log n)", "Fast average case"),
        ("Built-in sort()", "O(n log n)", "Optimized implementation")
    ]
    
    print("   ┌─────────────────┬──────────────┬─────────────────────┐")
    print("   │ Algorithm       │ Complexity   │ Description         │")
    print("   ├─────────────────┼──────────────┼─────────────────────┤")
    for alg, comp, desc in algorithms:
        print(f"   │ {alg:<15} │ {comp:<12} │ {desc:<19} │")
    print("   └─────────────────┴──────────────┴─────────────────────┘")

# =============================================================================
# MANUAL SORTING METHODS FOR THREE NUMBERS
# =============================================================================

def sort_three_manual_nested_if(a, b, c):
    """
    Manual sorting using nested if-else statements
    
    Method: Explicit comparison of all possible arrangements
    Time Complexity: O(1) - constant number of comparisons
    """
    print(f"\n🔍 Manual Nested If-Else Method")
    print("=" * 30)
    print(f"   Input: a={a}, b={b}, c={c}")
    print("\n   Decision tree analysis:")
    
    # Find all possible orderings
    if a <= b <= c:
        result = [a, b, c]
        print(f"   ✓ a ≤ b ≤ c: {result}")
    elif a <= c <= b:
        result = [a, c, b]
        print(f"   ✓ a ≤ c ≤ b: {result}")
    elif b <= a <= c:
        result = [b, a, c]
        print(f"   ✓ b ≤ a ≤ c: {result}")
    elif b <= c <= a:
        result = [b, c, a]
        print(f"   ✓ b ≤ c ≤ a: {result}")
    elif c <= a <= b:
        result = [c, a, b]
        print(f"   ✓ c ≤ a ≤ b: {result}")
    else:  # c <= b <= a
        result = [c, b, a]
        print(f"   ✓ c ≤ b ≤ a: {result}")
    
    print(f"\n   📊 Result (ascending): {result}")
    print(f"   📊 Result (descending): {result[::-1]}")
    
    return result

def sort_three_sequential_swaps(a, b, c):
    """
    Sequential comparison and swapping approach
    
    Method: Compare pairs and swap if needed
    Similar to bubble sort approach
    """
    print(f"\n🔄 Sequential Swap Method")
    print("=" * 25)
    print(f"   Input: a={a}, b={b}, c={c}")
    
    numbers = [a, b, c]
    print(f"   Initial array: {numbers}")
    
    # First pass: compare adjacent pairs
    print("\n   Pass 1: Compare adjacent elements")
    
    if numbers[0] > numbers[1]:
        numbers[0], numbers[1] = numbers[1], numbers[0]
        print(f"   Swapped positions 0,1: {numbers}")
    else:
        print(f"   No swap needed for positions 0,1: {numbers}")
    
    if numbers[1] > numbers[2]:
        numbers[1], numbers[2] = numbers[2], numbers[1]
        print(f"   Swapped positions 1,2: {numbers}")
    else:
        print(f"   No swap needed for positions 1,2: {numbers}")
    
    # Second pass: check first two again
    print("\n   Pass 2: Final check")
    
    if numbers[0] > numbers[1]:
        numbers[0], numbers[1] = numbers[1], numbers[0]
        print(f"   Final swap positions 0,1: {numbers}")
    else:
        print(f"   No additional swap needed: {numbers}")
    
    print(f"\n   ✅ Sorted result: {numbers}")
    return numbers

def sort_three_min_max_approach(a, b, c):
    """
    Using min/max approach to find positions
    
    Method: Find minimum, maximum, and middle value
    """
    print(f"\n⚡ Min-Max Approach")
    print("=" * 18)
    print(f"   Input: a={a}, b={b}, c={c}")
    
    numbers = [a, b, c]
    
    # Find min and max
    minimum = min(numbers)
    maximum = max(numbers)
    
    print(f"   Minimum value: {minimum}")
    print(f"   Maximum value: {maximum}")
    
    # Find middle value (sum - min - max)
    total = sum(numbers)
    middle = total - minimum - maximum
    
    print(f"   Middle value: {total} - {minimum} - {maximum} = {middle}")
    
    result = [minimum, middle, maximum]
    print(f"\n   ✅ Sorted result: {result}")
    
    return result

# =============================================================================
# BUILT-IN SORTING METHODS
# =============================================================================

def sort_three_builtin_methods(a, b, c):
    """
    Demonstrate various built-in sorting methods in Python
    """
    print(f"\n🐍 Python Built-in Methods")
    print("=" * 25)
    print(f"   Input: a={a}, b={b}, c={c}")
    
    numbers = [a, b, c]
    print(f"   Original list: {numbers}")
    
    # Method 1: Using sorted() function
    sorted_asc = sorted(numbers)
    sorted_desc = sorted(numbers, reverse=True)
    
    print(f"\n   Method 1: sorted() function")
    print(f"   • Ascending: sorted({numbers}) = {sorted_asc}")
    print(f"   • Descending: sorted({numbers}, reverse=True) = {sorted_desc}")
    
    # Method 2: Using list.sort() method
    numbers_copy = numbers.copy()
    numbers_copy.sort()
    
    print(f"\n   Method 2: list.sort() method")
    print(f"   • In-place sort: {numbers_copy}")
    
    # Method 3: Using tuple sorting
    numbers_tuple = tuple(numbers)
    sorted_tuple = tuple(sorted(numbers_tuple))
    
    print(f"\n   Method 3: Tuple sorting")
    print(f"   • Tuple input: {numbers_tuple}")
    print(f"   • Sorted tuple: {sorted_tuple}")
    
    return sorted_asc

def sort_with_custom_key(a, b, c):
    """
    Sorting with custom comparison keys
    """
    print(f"\n🎛️  Custom Key Sorting")
    print("=" * 20)
    print(f"   Input: a={a}, b={b}, c={c}")
    
    numbers = [a, b, c]
    
    # Sort by absolute value
    abs_sorted = sorted(numbers, key=abs)
    print(f"   By absolute value: {abs_sorted}")
    
    # Sort by distance from zero
    dist_sorted = sorted(numbers, key=lambda x: abs(x))
    print(f"   By distance from 0: {dist_sorted}")
    
    # Sort by digit sum (for positive numbers)
    if all(n >= 0 for n in numbers):
        digit_sum_sorted = sorted(numbers, key=lambda x: sum(int(d) for d in str(x)))
        print(f"   By digit sum: {digit_sum_sorted}")
    
    return abs_sorted

# =============================================================================
# ADVANCED SORTING DEMONSTRATIONS
# =============================================================================

def demonstrate_stability():
    """
    Demonstrate stable vs unstable sorting concepts
    """
    print(f"\n🔒 Sorting Stability Demonstration")
    print("=" * 30)
    
    # Create tuples with same values but different identifiers
    items = [(5, 'first'), (3, 'second'), (5, 'third'), (1, 'fourth')]
    
    print(f"   Original items: {items}")
    print("   (number, identifier)")
    
    # Stable sort - maintains relative order of equal elements
    stable_sorted = sorted(items, key=lambda x: x[0])
    
    print(f"\n   Stable sort by number:")
    print(f"   Result: {stable_sorted}")
    print("   Notice: 'first' comes before 'third' (both have value 5)")
    
    return stable_sorted

def sorting_performance_comparison():
    """
    Compare performance of different sorting methods
    """
    print(f"\n⏱️  Performance Comparison")
    print("=" * 25)
    
    # Generate test data
    test_size = 100000
    test_cases = [(random.randint(-1000, 1000),
                   random.randint(-1000, 1000),
                   random.randint(-1000, 1000)) for _ in range(test_size)]
    
    methods = [
        ("Manual Nested If", lambda nums: sort_three_manual_silent(nums[0], nums[1], nums[2])),
        ("Sequential Swaps", lambda nums: sort_three_swaps_silent(nums[0], nums[1], nums[2])),
        ("Min-Max Approach", lambda nums: sort_three_minmax_silent(nums[0], nums[1], nums[2])),
        ("Built-in sorted()", lambda nums: sorted(nums))
    ]
    
    print(f"   Testing with {test_size:,} random triplets...")
    
    results = []
    
    for name, method in methods:
        start_time = time.time()
        
        for test_case in test_cases:
            result = method(test_case)
        
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000
        
        results.append((name, execution_time))
        print(f"   {name}: {execution_time:.2f} ms")
    
    # Find fastest
    fastest = min(results, key=lambda x: x[1])
    print(f"\n   🏆 Fastest: {fastest[0]} ({fastest[1]:.2f} ms)")
    
    return results

# Silent helper functions for performance testing
def sort_three_manual_silent(a, b, c):
    """Silent version of manual sort for performance testing"""
    if a <= b <= c: return [a, b, c]
    elif a <= c <= b: return [a, c, b]
    elif b <= a <= c: return [b, a, c]
    elif b <= c <= a: return [b, c, a]
    elif c <= a <= b: return [c, a, b]
    else: return [c, b, a]

def sort_three_swaps_silent(a, b, c):
    """Silent version of swap sort for performance testing"""
    nums = [a, b, c]
    if nums[0] > nums[1]: nums[0], nums[1] = nums[1], nums[0]
    if nums[1] > nums[2]: nums[1], nums[2] = nums[2], nums[1]
    if nums[0] > nums[1]: nums[0], nums[1] = nums[1], nums[0]
    return nums

def sort_three_minmax_silent(a, b, c):
    """Silent version of min-max sort for performance testing"""
    nums = [a, b, c]
    minimum = min(nums)
    maximum = max(nums)
    middle = sum(nums) - minimum - maximum
    return [minimum, middle, maximum]

# =============================================================================
# EDGE CASES AND SPECIAL SCENARIOS
# =============================================================================

def handle_sorting_edge_cases():
    """
    Demonstrate handling of edge cases in sorting
    """
    print(f"\n🛡️  Edge Case Handling")
    print("=" * 20)
    
    edge_cases = [
        (5, 5, 5, "All equal"),
        (1, 2, 2, "Two equal (last two)"),
        (2, 1, 2, "Two equal (first and last)"),
        (2, 2, 1, "Two equal (first two)"),
        (-3, 0, 5, "Mixed signs"),
        (-10, -5, -1, "All negative"),
        (0, 0, 0, "All zeros"),
        (100, -100, 0, "Large range")
    ]
    
    print("   Testing various edge cases:")
    print("   ┌─────────────────┬─────────────────┬─────────────────┐")
    print("   │ Input           │ Sorted          │ Description     │")
    print("   ├─────────────────┼─────────────────┼─────────────────┤")
    
    for a, b, c, description in edge_cases:
        sorted_result = sorted([a, b, c])
        input_str = f"({a}, {b}, {c})"
        result_str = f"{sorted_result}"
        print(f"   │ {input_str:<15} │ {result_str:<15} │ {description:<15} │")
    
    print("   └─────────────────┴─────────────────┴─────────────────┘")

def sort_with_analysis(a, b, c):
    """
    Comprehensive sorting with detailed analysis
    """
    print(f"\n🔬 Comprehensive Analysis")
    print("=" * 25)
    print(f"   Input numbers: a={a}, b={b}, c={c}")
    
    numbers = [a, b, c]
    
    # Pre-sorting analysis
    print(f"\n   📊 Pre-sorting Analysis:")
    print(f"   • Sum: {sum(numbers)}")
    print(f"   • Average: {sum(numbers)/3:.2f}")
    print(f"   • Range: {max(numbers) - min(numbers)}")
    print(f"   • Unique values: {len(set(numbers))}")
    
    # Perform sorting
    sorted_numbers = sorted(numbers)
    
    # Post-sorting analysis
    print(f"\n   📈 Sorting Results:")
    print(f"   • Original order: {numbers}")
    print(f"   • Sorted (ascending): {sorted_numbers}")
    print(f"   • Sorted (descending): {sorted_numbers[::-1]}")
    
    # Check if sorting was needed
    if numbers == sorted_numbers:
        print("   ✅ Input was already sorted!")
    else:
        print("   🔄 Sorting was necessary")
    
    # Position changes
    print(f"\n   📍 Position Changes:")
    for i, original_val in enumerate(numbers):
        new_pos = sorted_numbers.index(original_val)
        if i != new_pos:
            print(f"   • Value {original_val}: position {i} → {new_pos}")
        else:
            print(f"   • Value {original_val}: stayed at position {i}")
    
    return sorted_numbers

# =============================================================================
# INTERACTIVE SORTING TOOL
# =============================================================================

def interactive_sorting_tool():
    """
    Interactive tool for exploring sorting concepts
    """
    print(f"\n🎮 INTERACTIVE SORTING TOOL")
    print("=" * 27)
    
    while True:
        try:
            print(f"\n🎯 Choose an option:")
            print("   1. Sort three numbers manually (nested if)")
            print("   2. Sort with sequential swaps")
            print("   3. Sort using min-max approach")
            print("   4. Sort with built-in methods")
            print("   5. Sort with custom keys")
            print("   6. Comprehensive analysis")
            print("   7. Test edge cases")
            print("   8. Performance comparison")
            print("   9. Generate random numbers to sort")
            print("   10. Learn about sorting concepts")
            print("   11. Exit")
            
            choice = input("\nEnter your choice (1-11): ").strip()
            
            if choice in ["1", "2", "3", "4", "5", "6"]:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                c = float(input("Enter third number: "))
                
                if choice == "1":
                    sort_three_manual_nested_if(a, b, c)
                elif choice == "2":
                    sort_three_sequential_swaps(a, b, c)
                elif choice == "3":
                    sort_three_min_max_approach(a, b, c)
                elif choice == "4":
                    sort_three_builtin_methods(a, b, c)
                elif choice == "5":
                    sort_with_custom_key(a, b, c)
                elif choice == "6":
                    sort_with_analysis(a, b, c)
                    
            elif choice == "7":
                handle_sorting_edge_cases()
                
            elif choice == "8":
                sorting_performance_comparison()
                
            elif choice == "9":
                a = random.randint(-100, 100)
                b = random.randint(-100, 100)
                c = random.randint(-100, 100)
                
                print(f"\n🎲 Generated numbers: {a}, {b}, {c}")
                
                # Quick sort demonstration
                result = sort_three_builtin_methods(a, b, c)
                
            elif choice == "10":
                explain_sorting_concepts()
                
            elif choice == "11":
                print("\n👋 Thanks for exploring sorting algorithms!")
                break
                
            else:
                print("❌ Invalid choice. Please choose 1-11.")
                
        except ValueError:
            print("❌ Please enter valid numbers!")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break

# =============================================================================
# PRACTICAL APPLICATIONS
# =============================================================================

def practical_sorting_applications():
    """
    Show practical applications of sorting
    """
    print(f"\n🎯 PRACTICAL APPLICATIONS")
    print("=" * 25)
    
    print("\n1️⃣ Grade Ranking:")
    student_grades = [85.5, 92.0, 78.5]
    sorted_grades = sorted(student_grades, reverse=True)
    print(f"   Original grades: {student_grades}")
    print(f"   Ranked (highest first): {sorted_grades}")
    
    print("\n2️⃣ Price Comparison:")
    prices = [29.99, 19.99, 35.00]
    sorted_prices = sorted(prices)
    print(f"   Product prices: {prices}")
    print(f"   Cheapest to expensive: {sorted_prices}")
    print(f"   Best deal: ${min(prices)}")
    
    print("\n3️⃣ Time Scheduling:")
    meeting_times = [14.5, 9.0, 11.25]  # Hours in 24-hour format
    sorted_times = sorted(meeting_times)
    print(f"   Meeting times: {meeting_times}")
    print(f"   Chronological order: {sorted_times}")
    
    print("\n4️⃣ Sports Scores:")
    scores = [7, 3, 10]
    sorted_scores = sorted(scores, reverse=True)
    print(f"   Team scores: {scores}")
    print(f"   Leaderboard: {sorted_scores}")
    print(f"   Winner: {max(scores)} points")

def sorting_games():
    """
    Interactive sorting games and challenges
    """
    import random
    
    print(f"\n🎮 SORTING GAMES")
    print("=" * 15)
    
    print("\n🎯 Sorting Challenge:")
    print("   I'll give you three numbers - sort them mentally!")
    
    score = 0
    rounds = 3
    
    for round_num in range(rounds):
        # Generate random numbers
        numbers = [random.randint(1, 100) for _ in range(3)]
        correct_answer = sorted(numbers)
        
        print(f"\n   Round {round_num + 1}: Sort these numbers: {numbers}")
        
        try:
            user_input = input("   Enter sorted numbers (comma-separated): ")
            user_answer = [int(x.strip()) for x in user_input.split(',')]
            
            if user_answer == correct_answer:
                print("   ✅ Correct!")
                score += 1
            else:
                print(f"   ❌ Wrong! Correct answer: {correct_answer}")
                
        except ValueError:
            print(f"   ❌ Invalid input! Correct answer: {correct_answer}")
    
    print(f"\n   🏆 Final Score: {score}/{rounds}")
    percentage = (score / rounds) * 100
    print(f"   Accuracy: {percentage:.1f}%")
    
    if percentage == 100:
        print("   🌟 Perfect score! You're a sorting master!")
    elif percentage >= 66:
        print("   👍 Great job! You understand sorting well!")
    else:
        print("   📚 Keep practicing - sorting takes time to master!")

if __name__ == "__main__":
    """
    Main execution demonstrating sorting concepts and algorithms
    """
    print(__doc__)
    
    # Educational content
    explain_sorting_concepts()
    
    # Demonstrate different sorting methods
    test_cases = [
        (15, 8, 23),
        (7, 7, 12),
        (-5, 0, 3),
        (100, 1, 50),
        (42, 42, 42)
    ]
    
    for a, b, c in test_cases:
        print(f"\n" + "="*60)
        print(f"DEMONSTRATION: Sorting {a}, {b}, {c}")
        print("="*60)
        
        # Show different approaches
        sort_three_manual_nested_if(a, b, c)
        sort_three_sequential_swaps(a, b, c)
        sort_three_min_max_approach(a, b, c)
        sort_three_builtin_methods(a, b, c)
        
        # Comprehensive analysis
        sort_with_analysis(a, b, c)
    
    # Edge case demonstration
    print(f"\n" + "="*60)
    print("EDGE CASES DEMONSTRATION")
    print("="*60)
    handle_sorting_edge_cases()
    
    # Performance comparison
    print(f"\n" + "="*60)
    print("PERFORMANCE ANALYSIS")
    print("="*60)
    sorting_performance_comparison()
    
    # Stability demonstration
    demonstrate_stability()
    
    # Practical applications
    practical_sorting_applications()
    
    # Interactive games
    play_games = input("\n🎮 Would you like to play sorting games? (y/n): ").lower()
    if play_games == 'y':
        sorting_games()
    
    # Interactive tool
    interactive_sorting_tool()
    
    print("\n" + "=" * 50)
    print("🎓 LEARNING SUMMARY")
    print("=" * 50)
    print("✅ Understanding of sorting algorithms and concepts")
    print("✅ Multiple approaches to sorting three numbers")
    print("✅ Comparison logic and decision-making structures")
    print("✅ Performance analysis and algorithm efficiency")
    print("✅ Edge case handling and robust programming")
    
    print("\n💡 Key Concepts Learned:")
    print("• Manual sorting with conditional logic")
    print("• Built-in sorting functions and methods")
    print("• Algorithm complexity and performance analysis")
    print("• Stable vs unstable sorting concepts")
    print("• Practical applications in real-world scenarios")
    
    print("\n🎯 Next Steps:")
    print("• Study advanced sorting algorithms (QuickSort, MergeSort)")
    print("• Explore sorting larger datasets")
    print("• Learn about custom comparison functions")
    print("• Investigate parallel and distributed sorting")