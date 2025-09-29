"""
Advanced Data Structures and Algorithms - Trees, Graphs, Dynamic Programming
============================================================================

Educational guide to advanced DSA: binary trees, graphs, and dynamic programming.
Includes implementations, complexity analysis, and real-world applications.

Author: Python Learning Notes
Date: September 2025
Topic: DSA, Trees, Graphs, Dynamic Programming
"""

from collections import deque, defaultdict

# =============================================================================
# BINARY TREE IMPLEMENTATION
# =============================================================================

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []

def tree_demo():
    print("\n🌳 Binary Tree Demo")
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print("Inorder traversal:", inorder_traversal(root))

# =============================================================================
# GRAPH IMPLEMENTATION (ADJACENCY LIST)
# =============================================================================

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            queue.extend(graph[node])
    return order

def graph_demo():
    print("\n🔗 Graph BFS Demo")
    graph = defaultdict(list, {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    })
    print("BFS from A:", bfs(graph, 'A'))

# =============================================================================
# DYNAMIC PROGRAMMING EXAMPLE (FIBONACCI)
# =============================================================================

def fibonacci_dp(n):
    if n <= 1:
        return n
    dp = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

def dp_demo():
    print("\n⚡ Dynamic Programming Demo (Fibonacci)")
    n = 10
    print(f"Fibonacci({n}) = {fibonacci_dp(n)}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    print(__doc__)
    tree_demo()
    graph_demo()
    dp_demo()

if __name__ == "__main__":
    main()
