"""
Data Structures Implementation in Python - Comprehensive Guide
===============================================================

Educational guide to implementing fundamental data structures from scratch.
Includes stacks, queues, linked lists, hash tables with detailed explanations
and practical examples.

Author: Python Learning Notes
Date: September 2025
Topic: Data Structures, Algorithms, Implementation, OOP

Table of Contents:
1. Stack Implementation
2. Queue Implementation
3. Linked List Implementation
4. Hash Table Implementation
5. Performance Analysis
6. Best Practices
"""

import time
from collections import deque

print("Data Structures Implementation in Python - Comprehensive Guide")
print("=" * 70)
print()
print("Educational guide to implementing fundamental data structures from scratch.")
print("Includes stacks, queues, linked lists, hash tables with detailed explanations")
print("and practical examples.")
print()
print("Author: Python Learning Notes")
print("Date: September 2025")
print("Topic: Data Structures, Algorithms, Implementation, OOP")
print()

# =============================================================================
# 1. STACK IMPLEMENTATION
# =============================================================================

class Stack:
    """
    Stack implementation using Python list.
    LIFO (Last In, First Out) data structure.

    Time Complexity:
    - Push: O(1)
    - Pop: O(1)
    - Peek: O(1)
    - Search: O(n)
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0

    def push(self, item):
        """Add item to top of stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return item from top of stack"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        """Return item from top of stack without removing it"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def size(self):
        """Return number of items in stack"""
        return len(self.items)

    def __str__(self):
        """String representation of stack"""
        return f"Stack({self.items})"

def demonstrate_stack():
    """Demonstrate stack operations"""
    print("📚 Stack Implementation Demo:")
    stack = Stack()

    # Push elements
    for i in range(1, 6):
        stack.push(i)
        print(f"Pushed {i}: {stack}")

    # Peek
    print(f"Peek: {stack.peek()}")

    # Pop elements
    while not stack.is_empty():
        popped = stack.pop()
        print(f"Popped {popped}: {stack}")

    print()

# =============================================================================
# 2. QUEUE IMPLEMENTATION
# =============================================================================

class Queue:
    """
    Queue implementation using Python list.
    FIFO (First In, First Out) data structure.

    Time Complexity:
    - Enqueue: O(1)
    - Dequeue: O(1) amortized (O(n) worst case due to list shift)
    - Front: O(1)
    - Rear: O(1)
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0

    def enqueue(self, item):
        """Add item to rear of queue"""
        self.items.append(item)

    def dequeue(self):
        """Remove and return item from front of queue"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def front(self):
        """Return item from front of queue without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def rear(self):
        """Return item from rear of queue without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[-1]

    def size(self):
        """Return number of items in queue"""
        return len(self.items)

    def __str__(self):
        """String representation of queue"""
        return f"Queue({self.items})"

def demonstrate_queue():
    """Demonstrate queue operations"""
    print("🔄 Queue Implementation Demo:")
    queue = Queue()

    # Enqueue elements
    for i in range(1, 6):
        queue.enqueue(i)
        print(f"Enqueued {i}: {queue}")

    # Front and rear
    print(f"Front: {queue.front()}")
    print(f"Rear: {queue.rear()}")

    # Dequeue elements
    while not queue.is_empty():
        dequeued = queue.dequeue()
        print(f"Dequeued {dequeued}: {queue}")

    print()

# =============================================================================
# 3. LINKED LIST IMPLEMENTATION
# =============================================================================

class Node:
    """Node class for linked list"""

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    Singly linked list implementation.

    Time Complexity:
    - Insert at beginning: O(1)
    - Insert at end: O(n)
    - Delete: O(n)
    - Search: O(n)
    - Access by index: O(n)
    """

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        """Check if linked list is empty"""
        return self.head is None

    def insert_at_beginning(self, data):
        """Insert node at the beginning of linked list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        """Insert node at the end of linked list"""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def delete(self, data):
        """Delete first occurrence of data"""
        if self.is_empty():
            return False

        # Special case: delete head
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True

        # Find and delete node
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next

        return False

    def search(self, data):
        """Search for data in linked list"""
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    def get_size(self):
        """Return size of linked list"""
        return self.size

    def __str__(self):
        """String representation of linked list"""
        if self.is_empty():
            return "LinkedList([])"

        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next

        return f"LinkedList([{', '.join(elements)}])"

def demonstrate_linked_list():
    """Demonstrate linked list operations"""
    print("🔗 Linked List Implementation Demo:")
    linked_list = LinkedList()

    # Insert elements
    for i in range(1, 6):
        linked_list.insert_at_end(i)
        print(f"Inserted {i} at end: {linked_list}")

    # Insert at beginning
    linked_list.insert_at_beginning(0)
    print(f"Inserted 0 at beginning: {linked_list}")

    # Search
    print(f"Search for 3: position {linked_list.search(3)}")
    print(f"Search for 10: position {linked_list.search(10)}")

    # Delete
    linked_list.delete(3)
    print(f"Deleted 3: {linked_list}")

    print()

# =============================================================================
# 4. HASH TABLE IMPLEMENTATION
# =============================================================================

class HashTable:
    """
    Simple hash table implementation using separate chaining.
    Uses Python's built-in hash() function and lists for collision resolution.

    Time Complexity (average case):
    - Insert: O(1)
    - Search: O(1)
    - Delete: O(1)

    Time Complexity (worst case with many collisions):
    - All operations: O(n)
    """

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # List of lists for chaining
        self.count = 0

    def _hash(self, key):
        """Simple hash function"""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert key-value pair into hash table"""
        index = self._hash(key)

        # Check if key already exists
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update value
                return

        # Key doesn't exist, add new pair
        self.table[index].append((key, value))
        self.count += 1

    def search(self, key):
        """Search for value by key"""
        index = self._hash(key)

        for k, v in self.table[index]:
            if k == key:
                return v

        raise KeyError(f"Key '{key}' not found")

    def delete(self, key):
        """Delete key-value pair from hash table"""
        index = self._hash(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                self.count -= 1
                return

        raise KeyError(f"Key '{key}' not found")

    def __contains__(self, key):
        """Check if key exists in hash table"""
        try:
            self.search(key)
            return True
        except KeyError:
            return False

    def __len__(self):
        """Return number of key-value pairs"""
        return self.count

    def __str__(self):
        """String representation of hash table"""
        elements = []
        for bucket in self.table:
            if bucket:
                elements.extend([f"{k}:{v}" for k, v in bucket])

        return f"HashTable({{{', '.join(elements)}}})"

def demonstrate_hash_table():
    """Demonstrate hash table operations"""
    print("🔑 Hash Table Implementation Demo:")
    hash_table = HashTable()

    # Insert elements
    data = [("apple", 5), ("banana", 3), ("cherry", 8), ("date", 2), ("elderberry", 7)]
    for key, value in data:
        hash_table.insert(key, value)
        print(f"Inserted {key}:{value}: {hash_table}")

    # Search
    print(f"Search 'banana': {hash_table.search('banana')}")
    print(f"Search 'cherry': {hash_table.search('cherry')}")

    # Update
    hash_table.insert("banana", 10)
    print(f"Updated banana to 10: {hash_table}")

    # Delete
    hash_table.delete("date")
    print(f"Deleted 'date': {hash_table}")

    # Check membership
    print(f"'apple' in hash_table: {'apple' in hash_table}")
    print(f"'grape' in hash_table: {'grape' in hash_table}")

    print()

# =============================================================================
# 5. PERFORMANCE ANALYSIS
# =============================================================================

def performance_comparison():
    """Compare performance of custom data structures vs Python built-ins"""
    print("📊 Performance Comparison:")

    # Test data
    test_data = list(range(10000))

    # Stack comparison
    print("\nStack Performance:")
    custom_stack = Stack()
    builtin_list = []

    # Custom stack timing
    start = time.time()
    for item in test_data:
        custom_stack.push(item)
    for _ in test_data:
        custom_stack.pop()
    custom_time = time.time() - start

    # Built-in list timing
    start = time.time()
    for item in test_data:
        builtin_list.append(item)
    for _ in test_data:
        builtin_list.pop()
    builtin_time = time.time() - start

    print(".4f")
    print(".4f")

    # Queue comparison
    print("\nQueue Performance:")
    custom_queue = Queue()
    builtin_deque = deque()

    # Custom queue timing
    start = time.time()
    for item in test_data:
        custom_queue.enqueue(item)
    for _ in test_data:
        custom_queue.dequeue()
    custom_time = time.time() - start

    # Built-in deque timing
    start = time.time()
    for item in test_data:
        builtin_deque.append(item)
    for _ in test_data:
        builtin_deque.popleft()
    builtin_time = time.time() - start

    print(".4f")
    print(".4f")

    # Linked List vs List
    print("\nLinked List vs List (insert at end):")
    custom_ll = LinkedList()
    builtin_list = []

    # Custom linked list timing
    start = time.time()
    for item in test_data:
        custom_ll.insert_at_end(item)
    custom_time = time.time() - start

    # Built-in list timing
    start = time.time()
    for item in test_data:
        builtin_list.append(item)
    builtin_time = time.time() - start

    print(".4f")
    print(".4f")

    print()

# =============================================================================
# 6. BEST PRACTICES AND CONCLUSION
# =============================================================================

def best_practices():
    """Display best practices for data structures"""
    print("✅ Data Structures Best Practices:")
    print("1. Choose the right data structure for your use case")
    print("2. Consider time and space complexity trade-offs")
    print("3. Use Python's built-in data structures when possible")
    print("4. Implement custom structures only when necessary")
    print("5. Test your implementations thoroughly")
    print("6. Consider edge cases (empty structures, boundary conditions)")
    print("7. Document your code and complexity analysis")
    print("8. Use meaningful variable and method names")
    print()

# =============================================================================
# MAIN DEMONSTRATION
# =============================================================================

if __name__ == "__main__":
    # Run all demonstrations
    demonstrate_stack()
    demonstrate_queue()
    demonstrate_linked_list()
    demonstrate_hash_table()
    performance_comparison()
    best_practices()

    print("Data structures implementation guide completed!")
    print("All fundamental data structures demonstrated with practical examples.")