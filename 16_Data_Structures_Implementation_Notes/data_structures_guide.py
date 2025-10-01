"""
Data Structures Implementation in Python - Comprehensive Guide
=============================================================

Educational guide to implementing custom data structures: stacks, queues, linked lists, hash tables.
Includes educational explanations, use cases, and performance analysis.

Author: Python Learning Notes
Date: September 2025
Topic: Data Structures, Stack, Queue, Linked List, Hash Table
"""

from typing import Optional, Any, List
from collections import deque

# =============================================================================
# STACK IMPLEMENTATION
# =============================================================================

class Stack:
    """Stack implementation using list"""
    
    def __init__(self):
        self._items = []
    
    def push(self, item: Any) -> None:
        """Add item to top of stack"""
        self._items.append(item)
    
    def pop(self) -> Any:
        """Remove and return top item"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items.pop()
    
    def peek(self) -> Any:
        """Return top item without removing"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """Check if stack is empty"""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Return stack size"""
        return len(self._items)

def stack_demo():
    """Demonstrate stack operations"""
    print("\n📚 Stack Demo:")
    stack = Stack()
    
    # Push items
    for item in [1, 2, 3, 4, 5]:
        stack.push(item)
        print(f"Pushed {item}, stack size: {stack.size()}")
    
    # Pop items
    while not stack.is_empty():
        item = stack.pop()
        print(f"Popped {item}, remaining size: {stack.size()}")

# =============================================================================
# QUEUE IMPLEMENTATION
# =============================================================================

class Queue:
    """Queue implementation using deque for efficiency"""
    
    def __init__(self):
        self._items = deque()
    
    def enqueue(self, item: Any) -> None:
        """Add item to rear of queue"""
        self._items.append(item)
    
    def dequeue(self) -> Any:
        """Remove and return front item"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items.popleft()
    
    def front(self) -> Any:
        """Return front item without removing"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items[0]
    
    def is_empty(self) -> bool:
        """Check if queue is empty"""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Return queue size"""
        return len(self._items)

def queue_demo():
    """Demonstrate queue operations"""
    print("\n🚶 Queue Demo:")
    queue = Queue()
    
    # Enqueue items
    for item in ['A', 'B', 'C', 'D']:
        queue.enqueue(item)
        print(f"Enqueued {item}, front: {queue.front()}, size: {queue.size()}")
    
    # Dequeue items
    while not queue.is_empty():
        item = queue.dequeue()
        front = queue.front() if not queue.is_empty() else "None"
        print(f"Dequeued {item}, new front: {front}, size: {queue.size()}")

# =============================================================================
# LINKED LIST IMPLEMENTATION
# =============================================================================

class ListNode:
    """Node for linked list"""
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional['ListNode'] = None

class LinkedList:
    """Singly linked list implementation"""
    
    def __init__(self):
        self.head: Optional[ListNode] = None
        self._size = 0
    
    def append(self, data: Any) -> None:
        """Add node to end of list"""
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1
    
    def prepend(self, data: Any) -> None:
        """Add node to beginning of list"""
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
    
    def delete(self, data: Any) -> bool:
        """Delete first occurrence of data"""
        if not self.head:
            return False
        
        if self.head.data == data:
            self.head = self.head.next
            self._size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        return False
    
    def find(self, data: Any) -> bool:
        """Check if data exists in list"""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def size(self) -> int:
        """Return list size"""
        return self._size
    
    def to_list(self) -> List[Any]:
        """Convert to Python list for display"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

def linked_list_demo():
    """Demonstrate linked list operations"""
    print("\n🔗 Linked List Demo:")
    ll = LinkedList()
    
    # Append items
    for item in [10, 20, 30]:
        ll.append(item)
        print(f"Appended {item}, list: {ll.to_list()}")
    
    # Prepend item
    ll.prepend(5)
    print(f"Prepended 5, list: {ll.to_list()}")
    
    # Find items
    for item in [20, 99]:
        found = ll.find(item)
        print(f"Find {item}: {'Found' if found else 'Not found'}")
    
    # Delete items
    ll.delete(20)
    print(f"Deleted 20, list: {ll.to_list()}")

# =============================================================================
# HASH TABLE IMPLEMENTATION
# =============================================================================

class HashTable:
    """Hash table implementation with chaining for collision resolution"""
    
    def __init__(self, initial_capacity: int = 8):
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]
    
    def _hash(self, key: str) -> int:
        """Simple hash function"""
        return hash(key) % self.capacity
    
    def put(self, key: str, value: Any) -> None:
        """Insert or update key-value pair"""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # Check if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing
                return
        
        # Add new key-value pair
        bucket.append((key, value))
        self.size += 1
        
        # Resize if load factor > 0.75
        if self.size > self.capacity * 0.75:
            self._resize()
    
    def get(self, key: str) -> Any:
        """Get value by key"""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError(f"Key '{key}' not found")
    
    def delete(self, key: str) -> bool:
        """Delete key-value pair"""
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        
        return False
    
    def _resize(self) -> None:
        """Resize hash table when load factor is high"""
        old_buckets = self.buckets
        self.capacity *= 2
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]
        
        # Rehash all items
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)
    
    def keys(self) -> List[str]:
        """Return all keys"""
        keys = []
        for bucket in self.buckets:
            for key, _ in bucket:
                keys.append(key)
        return keys
    
    def load_factor(self) -> float:
        """Return current load factor"""
        return self.size / self.capacity

def hash_table_demo():
    """Demonstrate hash table operations"""
    print("\n🔑 Hash Table Demo:")
    ht = HashTable(4)  # Small initial capacity to show resizing
    
    # Insert items
    items = [("name", "Alice"), ("age", 25), ("city", "Boston"), ("job", "Engineer")]
    for key, value in items:
        ht.put(key, value)
        print(f"Put {key}={value}, load factor: {ht.load_factor():.2f}")
    
    # Get items
    for key in ["name", "age"]:
        try:
            value = ht.get(key)
            print(f"Get {key}: {value}")
        except KeyError as e:
            print(f"Get {key}: {e}")
    
    # Update item
    ht.put("age", 26)
    print(f"Updated age to {ht.get('age')}")
    
    # Delete item
    deleted = ht.delete("city")
    print(f"Deleted 'city': {deleted}")
    print(f"Remaining keys: {ht.keys()}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    print(__doc__)
    
    stack_demo()
    queue_demo()
    linked_list_demo()
    hash_table_demo()
    
    print("\nData structures implementation guide completed!")

if __name__ == "__main__":
    main()