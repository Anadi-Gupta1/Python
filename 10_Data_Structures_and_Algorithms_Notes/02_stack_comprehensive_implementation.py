"""
Stack Data Structure - Complete Implementation and Applications Guide
===================================================================

Comprehensive guide to stacks in Python: implementation, applications, algorithms,
and real-world problem solving. Covers LIFO principles, operations, complexity
analysis, and practical applications in computer science.

Author: Python Learning Notes
Date: September 2025
Topic: Stack Data Structure, LIFO, Algorithm Implementation, Problem Solving
"""

import time
import sys
from typing import List, Optional, Any, Union
from collections import deque
import matplotlib.pyplot as plt

# =============================================================================
# STACK FUNDAMENTALS AND THEORY
# =============================================================================

def stack_fundamentals_comprehensive():
    """
    Complete introduction to stack data structure and LIFO principle
    """
    print("📚 STACK DATA STRUCTURE FUNDAMENTALS")
    print("=" * 38)
    
    print("🎯 What is a Stack?")
    print("   A stack is a linear data structure that follows the")
    print("   Last-In-First-Out (LIFO) principle. Think of it like")
    print("   a stack of plates - you can only add or remove from the top.")
    
    print(f"\n📊 Stack Characteristics:")
    characteristics = [
        ("LIFO Order", "Last element added is first to be removed", "🥞 Like pancakes"),
        ("Linear Structure", "Elements arranged in sequential order", "📐 Ordered access"),
        ("Restricted Access", "Can only access the top element", "🔒 Controlled operations"),
        ("Dynamic Size", "Can grow and shrink during runtime", "📈 Flexible capacity"),
        ("Homogeneous/Heterogeneous", "Can store same or different types", "🎭 Type flexibility"),
        ("Memory Efficient", "Minimal overhead for operations", "⚡ Fast operations")
    ]
    
    print("   Property          │ Description                     │ Analogy")
    print("   ──────────────────┼─────────────────────────────────┼──────────────────")
    
    for prop, desc, analogy in characteristics:
        print(f"   {prop:<17} │ {desc:<31} │ {analogy}")
    
    print(f"\n🔧 Core Stack Operations:")
    operations = [
        ("Push", "Add element to top", "O(1)", "stack.append(item)"),
        ("Pop", "Remove and return top element", "O(1)", "stack.pop()"),
        ("Peek/Top", "View top element without removal", "O(1)", "stack[-1]"),
        ("Is Empty", "Check if stack has no elements", "O(1)", "len(stack) == 0"),
        ("Size", "Get number of elements", "O(1)", "len(stack)")
    ]
    
    print("   Operation │ Description                  │ Time     │ Python Implementation")
    print("   ──────────┼──────────────────────────────┼──────────┼──────────────────────")
    
    for op, desc, complexity, implementation in operations:
        print(f"   {op:<9} │ {desc:<28} │ {complexity:<8} │ {implementation}")
    
    # Visual representation
    print(f"\n🎨 Visual Stack Representation:")
    print("   Stack Operations:")
    print("   ")
    print("   Push(D)    Pop()      Peek()")
    print("   ┌─────┐    ┌─────┐    ┌─────┐")
    print("   │  D  │ ←  │  C  │ ←  │  C  │ ← Top")
    print("   ├─────┤    ├─────┤    ├─────┤")
    print("   │  C  │    │  B  │    │  B  │")
    print("   ├─────┤    ├─────┤    ├─────┤")
    print("   │  B  │    │  A  │    │  A  │")
    print("   ├─────┤    └─────┘    └─────┘")
    print("   │  A  │")
    print("   └─────┘")
    
    return {
        'characteristics': characteristics,
        'operations': operations
    }

# =============================================================================
# STACK IMPLEMENTATION CLASSES
# =============================================================================

class ListStack:
    """
    Stack implementation using Python list
    Pros: Simple, built-in support, dynamic sizing
    Cons: Potential memory reallocation on growth
    """
    
    def __init__(self):
        """Initialize empty stack using list"""
        self._stack = []
        self._operations_count = 0
    
    def push(self, item: Any) -> None:
        """Add item to top of stack - O(1) amortized"""
        self._stack.append(item)
        self._operations_count += 1
    
    def pop(self) -> Any:
        """Remove and return top item - O(1)"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        self._operations_count += 1
        return self._stack.pop()
    
    def peek(self) -> Any:
        """Return top item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._stack[-1]
    
    def is_empty(self) -> bool:
        """Check if stack is empty - O(1)"""
        return len(self._stack) == 0
    
    def size(self) -> int:
        """Return number of items in stack - O(1)"""
        return len(self._stack)
    
    def clear(self) -> None:
        """Remove all items from stack - O(1)"""
        self._stack.clear()
        self._operations_count += 1
    
    def __str__(self) -> str:
        """String representation of stack"""
        return f"Stack(top -> {' -> '.join(map(str, reversed(self._stack)))} <- bottom)"
    
    def __len__(self) -> int:
        """Support len() function"""
        return len(self._stack)

class DequeStack:
    """
    Stack implementation using collections.deque
    Pros: Optimized for both ends, thread-safe operations
    Cons: Slightly more overhead than list for simple operations
    """
    
    def __init__(self):
        """Initialize empty stack using deque"""
        self._stack = deque()
        self._max_size = None
    
    def push(self, item: Any) -> None:
        """Add item to top of stack - O(1)"""
        if self._max_size and len(self._stack) >= self._max_size:
            raise OverflowError("Stack overflow")
        self._stack.append(item)
    
    def pop(self) -> Any:
        """Remove and return top item - O(1)"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._stack.pop()
    
    def peek(self) -> Any:
        """Return top item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._stack[-1]
    
    def is_empty(self) -> bool:
        """Check if stack is empty - O(1)"""
        return len(self._stack) == 0
    
    def size(self) -> int:
        """Return number of items in stack - O(1)"""
        return len(self._stack)
    
    def set_max_size(self, max_size: int) -> None:
        """Set maximum stack size"""
        self._max_size = max_size
    
    def __str__(self) -> str:
        """String representation of stack"""
        return f"DequeStack(top -> {' -> '.join(map(str, reversed(self._stack)))} <- bottom)"

class BoundedStack:
    """
    Fixed-size stack implementation with overflow protection
    Pros: Memory efficient, prevents overflow
    Cons: Fixed capacity, needs pre-allocation planning
    """
    
    def __init__(self, max_size: int):
        """Initialize bounded stack with maximum size"""
        self._max_size = max_size
        self._stack = [None] * max_size
        self._top = -1
    
    def push(self, item: Any) -> None:
        """Add item to stack - O(1)"""
        if self.is_full():
            raise OverflowError(f"Stack overflow: maximum size {self._max_size} reached")
        self._top += 1
        self._stack[self._top] = item
    
    def pop(self) -> Any:
        """Remove and return top item - O(1)"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        item = self._stack[self._top]
        self._stack[self._top] = None  # Help garbage collection
        self._top -= 1
        return item
    
    def peek(self) -> Any:
        """Return top item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._stack[self._top]
    
    def is_empty(self) -> bool:
        """Check if stack is empty - O(1)"""
        return self._top == -1
    
    def is_full(self) -> bool:
        """Check if stack is full - O(1)"""
        return self._top == self._max_size - 1
    
    def size(self) -> int:
        """Return number of items in stack - O(1)"""
        return self._top + 1
    
    def capacity(self) -> int:
        """Return maximum capacity - O(1)"""
        return self._max_size
    
    def __str__(self) -> str:
        """String representation of stack"""
        items = [str(self._stack[i]) for i in range(self._top, -1, -1)]
        return f"BoundedStack({self.size()}/{self._max_size}): top -> {' -> '.join(items)} <- bottom"

# =============================================================================
# STACK ALGORITHMS AND APPLICATIONS
# =============================================================================

def balanced_parentheses_checker(expression: str) -> tuple[bool, str]:
    """
    Check if parentheses are balanced using stack
    Time Complexity: O(n), Space Complexity: O(n)
    """
    stack = ListStack()
    pairs = {'(': ')', '[': ']', '{': '}'}
    opening = set(pairs.keys())
    closing = set(pairs.values())
    
    for i, char in enumerate(expression):
        if char in opening:
            stack.push((char, i))
        elif char in closing:
            if stack.is_empty():
                return False, f"Unmatched closing '{char}' at position {i}"
            
            open_char, open_pos = stack.pop()
            if pairs[open_char] != char:
                return False, f"Mismatched pair: '{open_char}' at {open_pos} and '{char}' at {i}"
    
    if not stack.is_empty():
        open_char, open_pos = stack.peek()
        return False, f"Unmatched opening '{open_char}' at position {open_pos}"
    
    return True, "All parentheses are balanced"

def evaluate_postfix_expression(expression: str) -> float:
    """
    Evaluate postfix (RPN) expression using stack
    Time Complexity: O(n), Space Complexity: O(n)
    """
    stack = ListStack()
    operators = {'+', '-', '*', '/', '//', '%', '**'}
    
    tokens = expression.split()
    
    for token in tokens:
        if token in operators:
            if stack.size() < 2:
                raise ValueError(f"Insufficient operands for operator '{token}'")
            
            # Pop operands (note the order!)
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            # Perform operation
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            elif token == '//':
                result = operand1 // operand2
            elif token == '%':
                result = operand1 % operand2
            elif token == '**':
                result = operand1 ** operand2
            
            stack.push(result)
        else:
            # Convert to number and push
            try:
                number = float(token) if '.' in token else int(token)
                stack.push(number)
            except ValueError:
                raise ValueError(f"Invalid token: '{token}'")
    
    if stack.size() != 1:
        raise ValueError("Invalid expression: too many operands")
    
    return stack.pop()

def infix_to_postfix_converter(expression: str) -> str:
    """
    Convert infix expression to postfix using stack
    Time Complexity: O(n), Space Complexity: O(n)
    """
    stack = ListStack()
    result = []
    
    # Define operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '//': 2, '%': 2, '**': 3}
    right_associative = {'**'}
    
    # Tokenize expression
    tokens = []
    current_token = ""
    
    for char in expression:
        if char.isalnum() or char == '.':
            current_token += char
        else:
            if current_token:
                tokens.append(current_token)
                current_token = ""
            if not char.isspace():
                tokens.append(char)
    
    if current_token:
        tokens.append(current_token)
    
    for token in tokens:
        if token.replace('.', '').isdigit():
            # Operand
            result.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            # Pop until opening parenthesis
            while not stack.is_empty() and stack.peek() != '(':
                result.append(stack.pop())
            if stack.is_empty():
                raise ValueError("Mismatched parentheses")
            stack.pop()  # Remove the '('
        elif token in precedence:
            # Operator
            while (not stack.is_empty() and 
                   stack.peek() != '(' and
                   (precedence.get(stack.peek(), 0) > precedence[token] or
                    (precedence.get(stack.peek(), 0) == precedence[token] and 
                     token not in right_associative))):
                result.append(stack.pop())
            stack.push(token)
        else:
            raise ValueError(f"Invalid token: '{token}'")
    
    # Pop remaining operators
    while not stack.is_empty():
        op = stack.pop()
        if op in '()':
            raise ValueError("Mismatched parentheses")
        result.append(op)
    
    return ' '.join(result)

def tower_of_hanoi_solver(n: int, source: str, destination: str, auxiliary: str) -> List[str]:
    """
    Solve Tower of Hanoi puzzle using recursive stack approach
    Time Complexity: O(2^n), Space Complexity: O(n)
    """
    moves = []
    
    def hanoi(n, src, dest, aux):
        if n == 1:
            moves.append(f"Move disk 1 from {src} to {dest}")
            return
        
        # Move n-1 disks from source to auxiliary
        hanoi(n-1, src, aux, dest)
        
        # Move largest disk from source to destination
        moves.append(f"Move disk {n} from {src} to {dest}")
        
        # Move n-1 disks from auxiliary to destination
        hanoi(n-1, aux, dest, src)
    
    hanoi(n, source, destination, auxiliary)
    return moves

def depth_first_search_iterative(graph: dict, start: str) -> List[str]:
    """
    Perform DFS traversal using explicit stack
    Time Complexity: O(V + E), Space Complexity: O(V)
    """
    visited = set()
    stack = ListStack()
    result = []
    
    stack.push(start)
    
    while not stack.is_empty():
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # Add neighbors to stack (in reverse order for consistent traversal)
            if vertex in graph:
                for neighbor in reversed(graph[vertex]):
                    if neighbor not in visited:
                        stack.push(neighbor)
    
    return result

# =============================================================================
# PRACTICAL DEMONSTRATIONS AND BENCHMARKING
# =============================================================================

def stack_implementation_benchmark():
    """
    Benchmark different stack implementations
    """
    print("\n⚡ STACK IMPLEMENTATION BENCHMARK")
    print("=" * 35)
    
    implementations = {
        'ListStack': ListStack,
        'DequeStack': DequeStack,
        'BoundedStack': lambda: BoundedStack(10000)
    }
    
    operations_count = 5000
    
    print(f"   Benchmarking {operations_count} operations for each implementation:")
    print("   Implementation │ Push Time │ Pop Time  │ Total Time")
    print("   ───────────────┼───────────┼───────────┼───────────")
    
    for name, stack_class in implementations.items():
        stack = stack_class()
        
        # Benchmark push operations
        start_time = time.perf_counter()
        for i in range(operations_count):
            stack.push(i)
        push_time = (time.perf_counter() - start_time) * 1000
        
        # Benchmark pop operations
        start_time = time.perf_counter()
        for _ in range(operations_count):
            stack.pop()
        pop_time = (time.perf_counter() - start_time) * 1000
        
        total_time = push_time + pop_time
        
        print(f"   {name:<14} │ {push_time:7.2f} ms │ {pop_time:7.2f} ms │ {total_time:7.2f} ms")
    
    return {
        'operations_count': operations_count,
        'implementations': list(implementations.keys())
    }

def practical_applications_demo():
    """
    Demonstrate practical stack applications
    """
    print("\n🚀 PRACTICAL STACK APPLICATIONS DEMO")
    print("=" * 37)
    
    # 1. Balanced Parentheses
    print("1️⃣  Balanced Parentheses Checker:")
    test_expressions = [
        "((()))",
        "([{}])",
        "(()",
        "()[]{}",
        "([)]",
        "{[()()]}"
    ]
    
    for expr in test_expressions:
        is_balanced, message = balanced_parentheses_checker(expr)
        status = "✅" if is_balanced else "❌"
        print(f"     '{expr}' → {status} {message}")
    
    # 2. Postfix Evaluation
    print(f"\n2️⃣  Postfix Expression Evaluation:")
    postfix_expressions = [
        "3 4 + 2 *",
        "15 7 1 1 + - / 3 * 2 1 1 + + -",
        "5 1 2 + 4 * + 3 -"
    ]
    
    for expr in postfix_expressions:
        try:
            result = evaluate_postfix_expression(expr)
            print(f"     '{expr}' = {result}")
        except Exception as e:
            print(f"     '{expr}' → Error: {e}")
    
    # 3. Infix to Postfix Conversion
    print(f"\n3️⃣  Infix to Postfix Conversion:")
    infix_expressions = [
        "3 + 4 * 2",
        "(3 + 4) * 2",
        "A + B * C + D",
        "(A + B) * (C + D)"
    ]
    
    for expr in infix_expressions:
        try:
            postfix = infix_to_postfix_converter(expr)
            print(f"     '{expr}' → '{postfix}'")
        except Exception as e:
            print(f"     '{expr}' → Error: {e}")
    
    # 4. Tower of Hanoi
    print(f"\n4️⃣  Tower of Hanoi (3 disks):")
    moves = tower_of_hanoi_solver(3, "A", "C", "B")
    for i, move in enumerate(moves, 1):
        print(f"     Step {i}: {move}")
    print(f"     Total moves: {len(moves)}")
    
    # 5. Depth-First Search
    print(f"\n5️⃣  Depth-First Search:")
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    dfs_result = depth_first_search_iterative(graph, 'A')
    print(f"     Graph: {graph}")
    print(f"     DFS traversal from 'A': {' → '.join(dfs_result)}")
    
    return {
        'parentheses_tests': len(test_expressions),
        'postfix_tests': len(postfix_expressions),
        'infix_tests': len(infix_expressions),
        'hanoi_moves': len(moves),
        'dfs_result': dfs_result
    }

# =============================================================================
# MAIN EXECUTION AND COMPREHENSIVE DEMONSTRATION
# =============================================================================

def main():
    """
    Main function executing comprehensive stack data structure guide
    """
    print(__doc__)
    
    # Fundamentals
    fundamentals = stack_fundamentals_comprehensive()
    
    # Benchmarking
    benchmark_results = stack_implementation_benchmark()
    
    # Practical applications
    applications = practical_applications_demo()
    
    return {
        'fundamentals': fundamentals,
        'benchmark': benchmark_results,
        'applications': applications
    }

if __name__ == "__main__":
    """
    Execute comprehensive stack data structure guide
    """
    results = main()
    
    print("\n" + "=" * 70)
    print("🎓 STACK DATA STRUCTURE MASTERY SUMMARY")
    print("=" * 70)
    print("✅ Complete stack fundamentals and LIFO principle understanding")
    print("✅ Multiple implementation approaches (List, Deque, Bounded)")
    print("✅ Time and space complexity analysis for all operations")
    print("✅ Practical algorithms: parentheses, postfix, infix conversion")
    print("✅ Advanced applications: Tower of Hanoi, DFS traversal")
    print("✅ Performance benchmarking and implementation comparison")
    print("✅ Error handling and edge case management")
    
    print("\n💡 Stack Mastery Key Points:")
    key_points = [
        "LIFO principle is fundamental to stack operations",
        "Stack operations are O(1) - constant time complexity",
        "Choose implementation based on specific requirements",
        "Stacks are essential for recursive algorithm simulation",
        "Expression evaluation and syntax parsing use stacks",
        "DFS and backtracking algorithms rely on stack structure",
        "Memory management and function calls use system stacks",
        "Balanced parentheses checking is a classic stack application"
    ]
    
    for point in key_points:
        print(f"   • {point}")
    
    print("\n🎯 Advanced Stack Topics to Explore:")
    advanced_topics = [
        "Function call stack and recursion depth management",
        "Expression parsing and compiler design applications",
        "Backtracking algorithms and puzzle solving",
        "Undo/Redo mechanisms in software applications",
        "Browser history and navigation stack implementation",
        "Memory management and garbage collection stacks",
        "Concurrent and thread-safe stack implementations",
        "Stack-based virtual machines and interpreters"
    ]
    
    for i, topic in enumerate(advanced_topics, 1):
        print(f"   {i}. {topic}")
    
    print(f"\n🚀 Master the Stack - Foundation for Advanced Algorithms!")
    print("Understanding stacks opens doors to recursion, parsing, and beyond!")