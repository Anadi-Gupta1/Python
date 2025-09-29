"""
Advanced NumPy Operations - Matrix, Statistics, Broadcasting, Linear Algebra
============================================================================

Comprehensive guide to advanced NumPy operations for scientific computing and data analysis.
Includes matrix manipulations, statistical functions, broadcasting, and linear algebra examples.

Author: Python Learning Notes
Date: September 2025
Topic: NumPy, Matrix Operations, Statistics, Linear Algebra
"""

import numpy as np

# =============================================================================
# MATRIX OPERATIONS
# =============================================================================

def matrix_operations_demo():
    print("\n🔢 Matrix Operations Demo")
    # Create matrices
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print(f"A:\n{A}\nB:\n{B}")
    # Matrix addition
    print(f"A + B:\n{A + B}")
    # Matrix multiplication
    print(f"A * B (element-wise):\n{A * B}")
    print(f"A @ B (matrix product):\n{A @ B}")
    # Transpose
    print(f"A.T:\n{A.T}")
    # Inverse
    print(f"np.linalg.inv(A):\n{np.linalg.inv(A)}")
    # Determinant
    print(f"np.linalg.det(A): {np.linalg.det(A):.2f}")

# =============================================================================
# STATISTICAL FUNCTIONS
# =============================================================================

def statistics_demo():
    print("\n📊 Statistics Demo")
    data = np.random.normal(loc=10, scale=2, size=100)
    print(f"Mean: {np.mean(data):.2f}")
    print(f"Median: {np.median(data):.2f}")
    print(f"Std Dev: {np.std(data):.2f}")
    print(f"Variance: {np.var(data):.2f}")
    print(f"Min: {np.min(data):.2f}, Max: {np.max(data):.2f}")
    print(f"25th percentile: {np.percentile(data, 25):.2f}")
    print(f"75th percentile: {np.percentile(data, 75):.2f}")

# =============================================================================
# BROADCASTING
# =============================================================================

def broadcasting_demo():
    print("\n📡 Broadcasting Demo")
    a = np.array([1, 2, 3])
    b = 10
    print(f"a: {a}, b: {b}")
    print(f"a + b: {a + b}")
    M = np.ones((3, 3))
    v = np.array([1, 2, 3])
    print(f"M:\n{M}\nv: {v}")
    print(f"M + v (broadcasted):\n{M + v}")

# =============================================================================
# LINEAR ALGEBRA
# =============================================================================

def linear_algebra_demo():
    print("\n📐 Linear Algebra Demo")
    # Solve Ax = b
    A = np.array([[3, 1], [1, 2]])
    b = np.array([9, 8])
    x = np.linalg.solve(A, b)
    print(f"Solving Ax = b for x:\nA = {A}\nb = {b}\nx = {x}")
    # Eigenvalues and eigenvectors
    eigvals, eigvecs = np.linalg.eig(A)
    print(f"Eigenvalues: {eigvals}")
    print(f"Eigenvectors:\n{eigvecs}")
    # Singular Value Decomposition
    U, S, Vt = np.linalg.svd(A)
    print(f"SVD: U =\n{U}\nS = {S}\nVt =\n{Vt}")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    print(__doc__)
    matrix_operations_demo()
    statistics_demo()
    broadcasting_demo()
    linear_algebra_demo()

if __name__ == "__main__":
    main()
