"""
Queue Data Structure Implementation in Python

A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.

Think of a queue as people standing in line in a supermarket.
The first person to stand in line is also the first who can pay and leave the supermarket.

Basic operations we can do on a queue are:
- Enqueue: Adds a new element to the queue
- Dequeue: Removes and returns the first (front) element from the queue
- Peek: Returns the first element in the queue
- isEmpty: Checks if the queue is empty
- Size: Finds the number of elements in the queue

Queues can be implemented by using arrays or linked lists.

Queues can be used to implement:
- Job scheduling for an office printer
- Order processing for e-tickets
- Algorithms for breadth-first search in graphs

Queues are often mentioned together with Stacks, which is a similar data structure.
"""

# ============================================================================
# Queue Implementation using Python Lists
# ============================================================================

print("=== Queue Implementation using Python Lists ===")
print("Basic queue operations with Python lists:")

# Using a Python list as a queue:
queue = []

# Enqueue operations
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue after enqueues: ", queue)

# Peek operation
front_element = queue[0]
print("Peek (front element): ", front_element)

# Dequeue operation
popped_element = queue.pop(0)
print("Dequeue: ", popped_element)

print("Queue after dequeue: ", queue)

# isEmpty check
is_empty = not bool(queue)
print("isEmpty: ", is_empty)

# Size operation
print("Size: ", len(queue))
print()

# Note: While using a list is simple, removing elements from the beginning (dequeue operation) 
# requires shifting all remaining elements, making it less efficient for large queues.

# ============================================================================
# Queue Class Implementation
# ============================================================================

print("=== Queue Class Implementation ===")

class Queue:
    """A Queue class implementation using Python lists"""
    
    def __init__(self):
        """Initialize an empty queue"""
        self.queue = []
    
    def enqueue(self, element):
        """Add an element to the rear of the queue"""
        self.queue.append(element)
    
    def dequeue(self):
        """Remove and return the front element from the queue"""
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        """Return the front element without removing it"""
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.queue) == 0
    
    def size(self):
        """Return the number of elements in the queue"""
        return len(self.queue)
    
    def display(self):
        """Display the current queue"""
        return self.queue


# Demonstrating Queue class usage
my_queue = Queue()

my_queue.enqueue('A')
my_queue.enqueue('B')
my_queue.enqueue('C')

print("Queue: ", my_queue.display())
print("Peek: ", my_queue.peek())
print("Dequeue: ", my_queue.dequeue())
print("Queue after dequeue: ", my_queue.display())
print("isEmpty: ", my_queue.is_empty())
print("Size: ", my_queue.size())
print()

# ============================================================================
# Queue Implementation using Linked Lists
# ============================================================================

print("=== Queue Implementation using Linked Lists ===")

class Node:
    """Node class for linked list implementation"""
    
    def __init__(self, data):
        """Initialize a node with data"""
        self.data = data
        self.next = None


class LinkedListQueue:
    """Queue implementation using linked lists for better efficiency"""
    
    def __init__(self):
        """Initialize an empty queue"""
        self.front = None
        self.rear = None
        self.length = 0
    
    def enqueue(self, element):
        """Add an element to the rear of the queue"""
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1
    
    def dequeue(self):
        """Remove and return the front element from the queue"""
        if self.is_empty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data
    
    def peek(self):
        """Return the front element without removing it"""
        if self.is_empty():
            return "Queue is empty"
        return self.front.data
    
    def is_empty(self):
        """Check if the queue is empty"""
        return self.length == 0
    
    def size(self):
        """Return the number of elements in the queue"""
        return self.length
    
    def display(self):
        """Display the queue elements"""
        elements = []
        temp = self.front
        while temp:
            elements.append(temp.data)
            temp = temp.next
        return elements


# Demonstrating LinkedListQueue usage
linked_queue = LinkedListQueue()

linked_queue.enqueue('A')
linked_queue.enqueue('B')
linked_queue.enqueue('C')

print("Linked List Queue: ", linked_queue.display())
print("Peek: ", linked_queue.peek())
print("Dequeue: ", linked_queue.dequeue())
print("Queue after dequeue: ", linked_queue.display())
print("isEmpty: ", linked_queue.is_empty())
print("Size: ", linked_queue.size())
print()

# ============================================================================
# Queue Applications and Benefits
# ============================================================================

print("=== Queue Applications ===")
print("""
Common Queue Applications:
1. Task scheduling in operating systems
2. Breadth-first search in graphs
3. Message queues in distributed systems
4. Print job scheduling
5. CPU task scheduling
6. Handling requests in web servers

Benefits of Linked List Implementation:
- Dynamic size: The queue can grow and shrink dynamically
- No shifting: Front element removal doesn't require shifting other elements
- Memory efficient: Only allocates memory as needed

Drawbacks of Linked List Implementation:
- Extra memory: Each element needs memory for the next pointer
- More complex: Code is longer and more complex than array implementation
""")

# ============================================================================
# Performance Comparison
# ============================================================================

print("=== Performance Comparison ===")
print("""
Array-based Queue (Python List):
- Enqueue: O(1) - amortized
- Dequeue: O(n) - requires shifting elements
- Space: O(n)

Linked List-based Queue:
- Enqueue: O(1)
- Dequeue: O(1) - no shifting required
- Space: O(n) + pointer overhead
""")

if __name__ == "__main__":
    print("\n=== Queue Implementation Demo Complete ===")
    print("All queue operations demonstrated successfully!")