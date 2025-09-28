"""
Queue Data Structure - Complete Implementation and Applications Guide
===================================================================

Comprehensive guide to queues in Python: implementation, applications, algorithms,
and real-world problem solving. Covers FIFO principles, operations, complexity
analysis, and practical applications in computer science.

Author: Python Learning Notes
Date: September 2025
Topic: Queue Data Structure, FIFO, Algorithm Implementation, BFS, Scheduling
"""

import time
import sys
from typing import List, Optional, Any, Deque, Generator
from collections import deque
import threading
import queue as threading_queue
from abc import ABC, abstractmethod

# =============================================================================
# QUEUE FUNDAMENTALS AND THEORY
# =============================================================================

def queue_fundamentals_comprehensive():
    """
    Complete introduction to queue data structure and FIFO principle
    """
    print("🚀 QUEUE DATA STRUCTURE FUNDAMENTALS")
    print("=" * 37)
    
    print("🎯 What is a Queue?")
    print("   A queue is a linear data structure that follows the")
    print("   First-In-First-Out (FIFO) principle. Think of it like")
    print("   people standing in line - first person to join is first to be served.")
    
    print(f"\n📊 Queue Characteristics:")
    characteristics = [
        ("FIFO Order", "First element added is first to be removed", "🚶 Like a line"),
        ("Linear Structure", "Elements arranged in sequential order", "📐 Ordered access"),
        ("Two-End Access", "Add at rear, remove from front", "⚡ Efficient operations"),
        ("Dynamic Size", "Can grow and shrink during runtime", "📈 Flexible capacity"),
        ("Fair Processing", "Elements processed in arrival order", "⚖️ Fair scheduling"),
        ("Memory Efficient", "Optimal for sequential processing", "🔄 Streaming data")
    ]
    
    print("   Property          │ Description                     │ Real-World Analogy")
    print("   ──────────────────┼─────────────────────────────────┼───────────────────")
    
    for prop, desc, analogy in characteristics:
        print(f"   {prop:<17} │ {desc:<31} │ {analogy}")
    
    print(f"\n🔧 Core Queue Operations:")
    operations = [
        ("Enqueue", "Add element to rear", "O(1)", "queue.append(item)"),
        ("Dequeue", "Remove and return front element", "O(1)*", "queue.popleft()"),
        ("Front/Peek", "View front element without removal", "O(1)", "queue[0]"),
        ("Rear", "View rear element without removal", "O(1)", "queue[-1]"),
        ("Is Empty", "Check if queue has no elements", "O(1)", "len(queue) == 0"),
        ("Size", "Get number of elements", "O(1)", "len(queue)")
    ]
    
    print("   Operation │ Description                  │ Time     │ Python Implementation")
    print("   ──────────┼──────────────────────────────┼──────────┼──────────────────────")
    
    for op, desc, complexity, implementation in operations:
        print(f"   {op:<9} │ {desc:<28} │ {complexity:<8} │ {implementation}")
    
    print("   * O(1) with deque, O(n) with list")
    
    # Visual representation
    print(f"\n🎨 Visual Queue Representation:")
    print("   Queue Operations (FIFO - First In, First Out):")
    print("   ")
    print("   Enqueue(D)           Dequeue()             Front/Peek()")
    print("   ┌─────┬─────┬─────┐  ┌─────┬─────┬─────┐   ┌─────┬─────┬─────┐")
    print("   │  A  │  B  │  C  │  │  B  │  C  │     │   │  A  │  B  │  C  │")
    print("   └─────┴─────┴─────┘  └─────┴─────┴─────┘   └─────┴─────┴─────┘")
    print("   Front       Rear     Front   Rear          Front ↑      Rear")
    print("        ↑         ↑          ↑      ↑              Peek")
    print("      Add D    Remove A     Process in order")
    
    return {
        'characteristics': characteristics,
        'operations': operations
    }

# =============================================================================
# QUEUE IMPLEMENTATION CLASSES
# =============================================================================

class QueueInterface(ABC):
    """Abstract base class defining queue interface"""
    
    @abstractmethod
    def enqueue(self, item: Any) -> None:
        """Add item to rear of queue"""
        pass
    
    @abstractmethod
    def dequeue(self) -> Any:
        """Remove and return front item"""
        pass
    
    @abstractmethod
    def front(self) -> Any:
        """Return front item without removing"""
        pass
    
    @abstractmethod
    def is_empty(self) -> bool:
        """Check if queue is empty"""
        pass
    
    @abstractmethod
    def size(self) -> int:
        """Return number of items in queue"""
        pass

class ListQueue(QueueInterface):
    """
    Queue implementation using Python list
    Pros: Simple, familiar interface
    Cons: O(n) dequeue operation due to shifting
    """
    
    def __init__(self):
        """Initialize empty queue using list"""
        self._queue = []
        self._operations_count = 0
    
    def enqueue(self, item: Any) -> None:
        """Add item to rear of queue - O(1)"""
        self._queue.append(item)
        self._operations_count += 1
    
    def dequeue(self) -> Any:
        """Remove and return front item - O(n) due to shifting"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        self._operations_count += 1
        return self._queue.pop(0)
    
    def front(self) -> Any:
        """Return front item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._queue[0]
    
    def rear(self) -> Any:
        """Return rear item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("rear from empty queue")
        return self._queue[-1]
    
    def is_empty(self) -> bool:
        """Check if queue is empty - O(1)"""
        return len(self._queue) == 0
    
    def size(self) -> int:
        """Return number of items in queue - O(1)"""
        return len(self._queue)
    
    def clear(self) -> None:
        """Remove all items from queue - O(1)"""
        self._queue.clear()
        self._operations_count += 1
    
    def __str__(self) -> str:
        """String representation of queue"""
        return f"ListQueue(front -> {' -> '.join(map(str, self._queue))} <- rear)"
    
    def __len__(self) -> int:
        """Support len() function"""
        return len(self._queue)

class DequeQueue(QueueInterface):
    """
    Queue implementation using collections.deque
    Pros: O(1) operations on both ends, optimized for queues
    Cons: Slightly more memory overhead than list
    """
    
    def __init__(self, maxlen: Optional[int] = None):
        """Initialize empty queue using deque"""
        self._queue = deque(maxlen=maxlen)
        self._maxlen = maxlen
    
    def enqueue(self, item: Any) -> None:
        """Add item to rear of queue - O(1)"""
        if self._maxlen and len(self._queue) >= self._maxlen:
            raise OverflowError("Queue is full")
        self._queue.append(item)
    
    def dequeue(self) -> Any:
        """Remove and return front item - O(1)"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._queue.popleft()
    
    def front(self) -> Any:
        """Return front item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._queue[0]
    
    def rear(self) -> Any:
        """Return rear item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("rear from empty queue")
        return self._queue[-1]
    
    def is_empty(self) -> bool:
        """Check if queue is empty - O(1)"""
        return len(self._queue) == 0
    
    def size(self) -> int:
        """Return number of items in queue - O(1)"""
        return len(self._queue)
    
    def is_full(self) -> bool:
        """Check if bounded queue is full - O(1)"""
        return self._maxlen is not None and len(self._queue) >= self._maxlen
    
    def __str__(self) -> str:
        """String representation of queue"""
        return f"DequeQueue(front -> {' -> '.join(map(str, self._queue))} <- rear)"

class CircularQueue:
    """
    Circular queue implementation using fixed-size array
    Pros: Memory efficient, no shifting required, fixed memory usage
    Cons: Fixed capacity, more complex implementation
    """
    
    def __init__(self, capacity: int):
        """Initialize circular queue with fixed capacity"""
        self._capacity = capacity
        self._queue = [None] * capacity
        self._front = 0
        self._rear = -1
        self._size = 0
    
    def enqueue(self, item: Any) -> None:
        """Add item to queue - O(1)"""
        if self.is_full():
            raise OverflowError(f"Queue overflow: maximum capacity {self._capacity} reached")
        self._rear = (self._rear + 1) % self._capacity
        self._queue[self._rear] = item
        self._size += 1
    
    def dequeue(self) -> Any:
        """Remove and return front item - O(1)"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self._queue[self._front]
        self._queue[self._front] = None  # Help garbage collection
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return item
    
    def front(self) -> Any:
        """Return front item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._queue[self._front]
    
    def rear(self) -> Any:
        """Return rear item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("rear from empty queue")
        return self._queue[self._rear]
    
    def is_empty(self) -> bool:
        """Check if queue is empty - O(1)"""
        return self._size == 0
    
    def is_full(self) -> bool:
        """Check if queue is full - O(1)"""
        return self._size == self._capacity
    
    def size(self) -> int:
        """Return number of items in queue - O(1)"""
        return self._size
    
    def capacity(self) -> int:
        """Return maximum capacity - O(1)"""
        return self._capacity
    
    def __str__(self) -> str:
        """String representation of circular queue"""
        if self.is_empty():
            return f"CircularQueue(empty, capacity={self._capacity})"
        
        items = []
        index = self._front
        for _ in range(self._size):
            items.append(str(self._queue[index]))
            index = (index + 1) % self._capacity
        
        return f"CircularQueue(front -> {' -> '.join(items)} <- rear, {self._size}/{self._capacity})"

class PriorityQueue:
    """
    Priority queue implementation using heap
    Elements with higher priority are dequeued first
    """
    
    def __init__(self, reverse: bool = False):
        """
        Initialize priority queue
        reverse: If True, higher values have higher priority (max-heap)
                If False, lower values have higher priority (min-heap)
        """
        self._heap = []
        self._reverse = reverse
        self._counter = 0  # For stable sorting when priorities are equal
    
    def enqueue(self, item: Any, priority: float) -> None:
        """Add item with priority - O(log n)"""
        import heapq
        # Use counter for stable ordering and handle reverse priority
        priority_tuple = (-priority, self._counter) if self._reverse else (priority, self._counter)
        heapq.heappush(self._heap, (priority_tuple, item))
        self._counter += 1
    
    def dequeue(self) -> Any:
        """Remove and return highest priority item - O(log n)"""
        import heapq
        if self.is_empty():
            raise IndexError("dequeue from empty priority queue")
        _, item = heapq.heappop(self._heap)
        return item
    
    def front(self) -> Any:
        """Return highest priority item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("front from empty priority queue")
        return self._heap[0][1]
    
    def is_empty(self) -> bool:
        """Check if priority queue is empty - O(1)"""
        return len(self._heap) == 0
    
    def size(self) -> int:
        """Return number of items in priority queue - O(1)"""
        return len(self._heap)
    
    def __str__(self) -> str:
        """String representation of priority queue"""
        if self.is_empty():
            return "PriorityQueue(empty)"
        items = [f"{item}(p:{-prio[0] if self._reverse else prio[0]})" 
                for prio, item in sorted(self._heap)]
        return f"PriorityQueue([{', '.join(items)}])"

# =============================================================================
# QUEUE ALGORITHMS AND APPLICATIONS
# =============================================================================

def breadth_first_search(graph: dict, start: str) -> List[str]:
    """
    Perform BFS traversal using queue
    Time Complexity: O(V + E), Space Complexity: O(V)
    """
    visited = set()
    queue = DequeQueue()
    result = []
    
    queue.enqueue(start)
    visited.add(start)
    
    while not queue.is_empty():
        vertex = queue.dequeue()
        result.append(vertex)
        
        if vertex in graph:
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)
    
    return result

def level_order_traversal(tree: dict, root: str) -> List[List[str]]:
    """
    Level-order (breadth-first) traversal of binary tree
    Returns list of lists, where each inner list contains nodes at same level
    """
    if not root:
        return []
    
    result = []
    queue = DequeQueue()
    queue.enqueue((root, 0))  # (node, level)
    
    current_level = -1
    current_level_nodes = []
    
    while not queue.is_empty():
        node, level = queue.dequeue()
        
        if level > current_level:
            if current_level_nodes:
                result.append(current_level_nodes)
            current_level_nodes = []
            current_level = level
        
        current_level_nodes.append(node)
        
        # Add children if they exist
        if node in tree:
            for child in tree[node]:
                queue.enqueue((child, level + 1))
    
    if current_level_nodes:
        result.append(current_level_nodes)
    
    return result

def sliding_window_maximum(nums: List[int], k: int) -> List[int]:
    """
    Find maximum in each sliding window of size k using deque
    Time Complexity: O(n), Space Complexity: O(k)
    """
    if not nums or k == 0:
        return []
    
    from collections import deque
    dq = deque()  # Store indices
    result = []
    
    for i in range(len(nums)):
        # Remove indices that are out of current window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove indices of elements smaller than current element
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # Add maximum of current window to result
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

def task_scheduler_simulation(tasks: List[tuple], cpu_cores: int = 1) -> List[tuple]:
    """
    Simulate task scheduling using priority queue
    tasks: List of (task_name, arrival_time, execution_time, priority)
    Returns: List of (task_name, start_time, end_time)
    """
    # Sort tasks by arrival time
    tasks.sort(key=lambda x: x[1])
    
    # Priority queue for ready tasks (higher priority first)
    ready_queue = PriorityQueue(reverse=True)
    
    # Results
    results = []
    current_time = 0
    task_index = 0
    
    while task_index < len(tasks) or not ready_queue.is_empty():
        # Add newly arrived tasks to ready queue
        while task_index < len(tasks) and tasks[task_index][1] <= current_time:
            task_name, arrival_time, execution_time, priority = tasks[task_index]
            ready_queue.enqueue((task_name, execution_time), priority)
            task_index += 1
        
        if not ready_queue.is_empty():
            # Execute highest priority task
            task_name, execution_time = ready_queue.dequeue()
            start_time = current_time
            end_time = current_time + execution_time
            
            results.append((task_name, start_time, end_time))
            current_time = end_time
        elif task_index < len(tasks):
            # Jump to next task arrival time if no tasks ready
            current_time = tasks[task_index][1]
    
    return results

def producer_consumer_simulation(buffer_size: int, num_items: int) -> dict:
    """
    Simulate producer-consumer pattern using queue
    """
    buffer = DequeQueue(maxlen=buffer_size)
    produced_items = []
    consumed_items = []
    
    # Simulate production and consumption
    for i in range(num_items):
        item = f"item_{i}"
        
        # Producer
        try:
            buffer.enqueue(item)
            produced_items.append((item, i))
        except OverflowError:
            # Buffer full - in real scenario, producer would wait
            pass
        
        # Consumer (consume every other iteration to simulate different speeds)
        if i % 2 == 1 and not buffer.is_empty():
            consumed_item = buffer.dequeue()
            consumed_items.append((consumed_item, i))
    
    # Consume remaining items
    while not buffer.is_empty():
        consumed_item = buffer.dequeue()
        consumed_items.append((consumed_item, num_items))
    
    return {
        'produced': produced_items,
        'consumed': consumed_items,
        'buffer_size': buffer_size,
        'efficiency': len(consumed_items) / len(produced_items) if produced_items else 0
    }

# =============================================================================
# PRACTICAL DEMONSTRATIONS AND BENCHMARKING
# =============================================================================

def queue_implementation_benchmark():
    """
    Benchmark different queue implementations
    """
    print("\n⚡ QUEUE IMPLEMENTATION BENCHMARK")
    print("=" * 36)
    
    implementations = {
        'ListQueue': ListQueue,
        'DequeQueue': DequeQueue,
        'CircularQueue': lambda: CircularQueue(10000)
    }
    
    operations_count = 5000
    
    print(f"   Benchmarking {operations_count} operations for each implementation:")
    print("   Implementation │ Enqueue Time │ Dequeue Time │ Total Time")
    print("   ───────────────┼──────────────┼──────────────┼───────────")
    
    for name, queue_class in implementations.items():
        queue = queue_class()
        
        # Benchmark enqueue operations
        start_time = time.perf_counter()
        for i in range(operations_count):
            queue.enqueue(i)
        enqueue_time = (time.perf_counter() - start_time) * 1000
        
        # Benchmark dequeue operations
        start_time = time.perf_counter()
        for _ in range(operations_count):
            queue.dequeue()
        dequeue_time = (time.perf_counter() - start_time) * 1000
        
        total_time = enqueue_time + dequeue_time
        
        print(f"   {name:<14} │ {enqueue_time:10.2f} ms │ {dequeue_time:10.2f} ms │ {total_time:8.2f} ms")
    
    return {
        'operations_count': operations_count,
        'implementations': list(implementations.keys())
    }

def practical_applications_demo():
    """
    Demonstrate practical queue applications
    """
    print("\n🚀 PRACTICAL QUEUE APPLICATIONS DEMO")
    print("=" * 37)
    
    # 1. Breadth-First Search
    print("1️⃣  Breadth-First Search:")
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    bfs_result = breadth_first_search(graph, 'A')
    print(f"     Graph: {graph}")
    print(f"     BFS traversal from 'A': {' → '.join(bfs_result)}")
    
    # 2. Level Order Traversal
    print(f"\n2️⃣  Binary Tree Level Order Traversal:")
    tree = {
        '1': ['2', '3'],
        '2': ['4', '5'],
        '3': ['6', '7'],
        '4': [], '5': [], '6': [], '7': []
    }
    
    levels = level_order_traversal(tree, '1')
    print(f"     Tree: {tree}")
    for i, level in enumerate(levels):
        print(f"     Level {i}: {level}")
    
    # 3. Sliding Window Maximum
    print(f"\n3️⃣  Sliding Window Maximum:")
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    max_values = sliding_window_maximum(nums, k)
    print(f"     Array: {nums}")
    print(f"     Window size: {k}")
    print(f"     Sliding window maximums: {max_values}")
    
    # 4. Task Scheduling
    print(f"\n4️⃣  Task Scheduling Simulation:")
    tasks = [
        ("TaskA", 0, 3, 2),  # (name, arrival, execution, priority)
        ("TaskB", 1, 2, 1),
        ("TaskC", 2, 4, 3),
        ("TaskD", 3, 1, 2)
    ]
    
    schedule = task_scheduler_simulation(tasks)
    print(f"     Tasks: {tasks}")
    print(f"     Schedule (name, start, end):")
    for task_name, start, end in schedule:
        print(f"       {task_name}: {start} → {end}")
    
    # 5. Producer-Consumer
    print(f"\n5️⃣  Producer-Consumer Simulation:")
    simulation = producer_consumer_simulation(buffer_size=3, num_items=8)
    print(f"     Buffer size: {simulation['buffer_size']}")
    print(f"     Produced: {len(simulation['produced'])} items")
    print(f"     Consumed: {len(simulation['consumed'])} items")
    print(f"     Efficiency: {simulation['efficiency']:.1%}")
    
    return {
        'bfs_result': bfs_result,
        'tree_levels': levels,
        'sliding_window': max_values,
        'task_schedule': schedule,
        'producer_consumer': simulation
    }

# =============================================================================
# MAIN EXECUTION AND COMPREHENSIVE DEMONSTRATION
# =============================================================================

def main():
    """
    Main function executing comprehensive queue data structure guide
    """
    print(__doc__)
    
    # Fundamentals
    fundamentals = queue_fundamentals_comprehensive()
    
    # Benchmarking
    benchmark_results = queue_implementation_benchmark()
    
    # Practical applications
    applications = practical_applications_demo()
    
    return {
        'fundamentals': fundamentals,
        'benchmark': benchmark_results,
        'applications': applications
    }

if __name__ == "__main__":
    """
    Execute comprehensive queue data structure guide
    """
    results = main()
    
    print("\n" + "=" * 70)
    print("🎓 QUEUE DATA STRUCTURE MASTERY SUMMARY")
    print("=" * 70)
    print("✅ Complete queue fundamentals and FIFO principle understanding")
    print("✅ Multiple implementation approaches (List, Deque, Circular, Priority)")
    print("✅ Time and space complexity analysis for all operations")
    print("✅ Practical algorithms: BFS, level-order traversal, sliding window")
    print("✅ Advanced applications: task scheduling, producer-consumer patterns")
    print("✅ Performance benchmarking and implementation comparison")
    print("✅ Real-world problem solving with queue-based solutions")
    
    print("\n💡 Queue Mastery Key Points:")
    key_points = [
        "FIFO principle ensures fair and ordered processing",
        "Deque implementation provides O(1) operations on both ends",
        "Circular queues are memory-efficient for fixed-size scenarios",
        "Priority queues enable importance-based processing",
        "BFS algorithms rely on queue structure for level-by-level exploration",
        "Producer-consumer patterns use queues for buffering",
        "Task scheduling systems utilize priority queues",
        "Sliding window problems often employ deque for efficiency"
    ]
    
    for point in key_points:
        print(f"   • {point}")
    
    print("\n🎯 Advanced Queue Topics to Explore:")
    advanced_topics = [
        "Multi-threaded and concurrent queue implementations",
        "Lock-free and wait-free queue algorithms",
        "Distributed queue systems and message brokers",
        "Network packet scheduling and Quality of Service",
        "Graph algorithms: shortest path with priority queues",
        "Operating system process scheduling algorithms",
        "Real-time systems and deadline-aware scheduling",
        "Stream processing and event-driven architectures"
    ]
    
    for i, topic in enumerate(advanced_topics, 1):
        print(f"   {i}. {topic}")
    
    print(f"\n🚀 Master the Queue - Foundation for System Design!")
    print("Understanding queues unlocks scheduling, networking, and distributed systems!")