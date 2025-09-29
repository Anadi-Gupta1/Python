"""
Threading and Concurrency in Python - Comprehensive Guide
========================================================

Educational guide to multi-threading, multiprocessing, async programming, and performance comparisons.
Includes best practices for concurrent programming in Python.

Author: Python Learning Notes
Date: September 2025
Topic: Threading, Multiprocessing, Async, Concurrency, Performance
"""

import threading
import multiprocessing
import asyncio
import time
import concurrent.futures
from typing import List
import math

# =============================================================================
# MULTI-THREADING BASICS
# =============================================================================

def worker_thread(thread_id: int, results: List[int]):
    """Worker function for threading demo"""
    print(f"Thread {thread_id} starting")
    time.sleep(1)  # Simulate work
    result = thread_id * 2
    results.append(result)
    print(f"Thread {thread_id} finished with result: {result}")

def threading_demo():
    """Demonstrate basic multi-threading"""
    print("\n🧵 Multi-threading Demo:")
    results = []
    threads = []
    
    # Create and start threads
    for i in range(3):
        thread = threading.Thread(target=worker_thread, args=(i, results))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    print(f"Final results: {results}")

# =============================================================================
# THREAD SYNCHRONIZATION
# =============================================================================

class Counter:
    """Thread-safe counter using Lock"""
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
    
    def increment(self):
        with self.lock:
            self.value += 1
            time.sleep(0.01)  # Simulate some work

def synchronization_demo():
    """Demonstrate thread synchronization"""
    print("\n🔒 Thread Synchronization Demo:")
    counter = Counter()
    
    def increment_worker():
        for _ in range(100):
            counter.increment()
    
    threads = []
    for _ in range(5):
        thread = threading.Thread(target=increment_worker)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(f"Final counter value: {counter.value} (expected: 500)")

# =============================================================================
# MULTI-PROCESSING
# =============================================================================

def cpu_intensive_task(n: int) -> int:
    """CPU-intensive task for multiprocessing demo"""
    return sum(i * i for i in range(n))

def multiprocessing_demo():
    """Demonstrate multiprocessing for CPU-bound tasks"""
    print("\n⚙️ Multi-processing Demo:")
    numbers = [100000, 200000, 300000]
    
    start_time = time.time()
    with multiprocessing.Pool(processes=3) as pool:
        results = pool.map(cpu_intensive_task, numbers)
    mp_time = time.time() - start_time
    
    start_time = time.time()
    results_sequential = [cpu_intensive_task(n) for n in numbers]
    seq_time = time.time() - start_time
    
    print(f"Multiprocessing results: {results} (time: {mp_time:.2f}s)")
    print(f"Sequential results: {results_sequential} (time: {seq_time:.2f}s)")
    print(f"Speedup: {seq_time/mp_time:.2f}x")

# =============================================================================
# ASYNC/AWAIT PROGRAMMING
# =============================================================================

async def async_task(task_id: int, delay: float) -> str:
    """Async task that simulates I/O operation"""
    print(f"Async task {task_id} starting")
    await asyncio.sleep(delay)  # Non-blocking sleep
    result = f"Task {task_id} completed after {delay}s"
    print(result)
    return result

async def async_demo():
    """Demonstrate async/await programming"""
    print("\n🔄 Async/Await Demo:")
    
    # Run tasks concurrently
    tasks = [
        async_task(1, 1.0),
        async_task(2, 0.5),
        async_task(3, 1.5)
    ]
    
    start_time = time.time()
    results = await asyncio.gather(*tasks)
    total_time = time.time() - start_time
    
    print(f"All async tasks completed in {total_time:.2f}s")
    print(f"Results: {results}")

# =============================================================================
# CONCURRENT.FUTURES
# =============================================================================

def futures_demo():
    """Demonstrate concurrent.futures for both threads and processes"""
    print("\n🔧 Concurrent.Futures Demo:")
    
    def io_task(url: str) -> str:
        """Simulate I/O task"""
        time.sleep(0.5)  # Simulate network delay
        return f"Downloaded {url}"
    
    urls = [f"http://example.com/page{i}" for i in range(5)]
    
    # ThreadPoolExecutor for I/O-bound tasks
    print("ThreadPoolExecutor (I/O-bound):")
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(io_task, urls))
    thread_time = time.time() - start_time
    print(f"Results: {len(results)} tasks completed in {thread_time:.2f}s")
    
    # ProcessPoolExecutor for CPU-bound tasks
    print("\nProcessPoolExecutor (CPU-bound):")
    numbers = [50000, 75000, 100000]
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(cpu_intensive_task, numbers))
    process_time = time.time() - start_time
    print(f"Results: {results} completed in {process_time:.2f}s")

def calculate_pi_approximation(iterations: int) -> float:
    """Approximate pi using Leibniz formula"""
    pi_approx = 0
    for i in range(iterations):
        pi_approx += (-1) ** i / (2 * i + 1)
    return 4 * pi_approx

# =============================================================================
# PERFORMANCE COMPARISON
# =============================================================================

def performance_comparison():
    """Compare different concurrency approaches"""
    print("\n📊 Performance Comparison:")
    
    iterations = 1000000
    
    # Sequential
    print("Sequential execution:")
    start_time = time.time()
    result_seq = calculate_pi_approximation(iterations)
    seq_time = time.time() - start_time
    print(f"Result: {result_seq:.10f} (time: {seq_time:.2f}s)")
    
    # Multiprocessing
    print("\nMultiprocessing:")
    start_time = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        # Split work among processes
        chunk_size = iterations // 4
        chunks = [chunk_size] * 4
        results = pool.map(calculate_pi_approximation, chunks)
        result_mp = sum(results)
    mp_time = time.time() - start_time
    print(f"Result: {result_mp:.10f} (time: {mp_time:.2f}s)")
    
    print(f"\nSpeedup: {seq_time/mp_time:.2f}x")

# =============================================================================
# BEST PRACTICES
# =============================================================================

def best_practices_demo():
    """Demonstrate concurrency best practices"""
    print("\n✅ Concurrency Best Practices:")
    
    # 1. Use ThreadPoolExecutor for I/O-bound tasks
    print("1. ThreadPoolExecutor for I/O-bound tasks")
    
    # 2. Use ProcessPoolExecutor for CPU-bound tasks
    print("2. ProcessPoolExecutor for CPU-bound tasks")
    
    # 3. Use asyncio for cooperative multitasking
    print("3. Asyncio for cooperative multitasking")
    
    # 4. Avoid shared state in threads
    print("4. Avoid shared state in threads (use locks if necessary)")
    
    # 5. Use concurrent.futures for simple cases
    print("5. Use concurrent.futures for simple concurrency needs")
    
    # 6. Consider GIL limitations
    print("6. Consider GIL limitations for CPU-bound multi-threading")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    print(__doc__)
    
    threading_demo()
    synchronization_demo()
    multiprocessing_demo()
    
    # Run async demo
    asyncio.run(async_demo())
    
    futures_demo()
    performance_comparison()
    best_practices_demo()
    
    print("\nThreading and concurrency guide completed!")

if __name__ == "__main__":
    main()
