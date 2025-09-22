"""
Matplotlib Subplot Examples
===========================
This file demonstrates how to create multiple plots in one figure
using matplotlib subplots with various layouts and configurations.
"""

import matplotlib.pyplot as plt
import numpy as np

print("=== Matplotlib Subplot Examples ===\n")

# Sample data for demonstrations
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([10, 20, 30, 40])

# 1. Basic subplots - side by side (1 row, 2 columns)
print("1. Basic subplots - side by side:")
plt.figure(figsize=(12, 5))

# Plot 1: Left side
plt.subplot(1, 2, 1)
plt.plot(x1, y1, 'b-o')
plt.title("Left Plot")
plt.xlabel("X values")
plt.ylabel("Y values")

# Plot 2: Right side
plt.subplot(1, 2, 2)
plt.plot(x2, y2, 'r-s')
plt.title("Right Plot")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.tight_layout()
plt.show()

# 2. Vertical subplots - top and bottom (2 rows, 1 column)
print("\n2. Vertical subplots - top and bottom:")
plt.figure(figsize=(8, 8))

# Plot 1: Top
plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'g-^')
plt.title("Top Plot")
plt.xlabel("X values")
plt.ylabel("Y values")

# Plot 2: Bottom
plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'm-D')
plt.title("Bottom Plot")
plt.xlabel("X values")
plt.ylabel("Y values")

plt.tight_layout()
plt.show()

# 3. Grid layout - 2x3 subplots (6 plots total)
print("\n3. Grid layout - 2x3 subplots:")
plt.figure(figsize=(15, 8))

# Different plot styles for each subplot
plot_styles = ['b-o', 'r-s', 'g-^', 'm-D', 'c-*', 'y-p']
plot_titles = ['Plot 1', 'Plot 2', 'Plot 3', 'Plot 4', 'Plot 5', 'Plot 6']

for i in range(6):
    plt.subplot(2, 3, i+1)
    if i % 2 == 0:
        plt.plot(x1, y1, plot_styles[i])
    else:
        plt.plot(x2, y2, plot_styles[i])
    plt.title(plot_titles[i])
    plt.xlabel("X values")
    plt.ylabel("Y values")

plt.tight_layout()
plt.show()

# 4. Subplots with individual titles
print("\n4. Subplots with individual titles:")
plt.figure(figsize=(12, 5))

# Sales plot
plt.subplot(1, 2, 1)
plt.plot(x1, y1, 'b-o', linewidth=2)
plt.title("SALES", fontsize=14, fontweight='bold')
plt.xlabel("Quarter")
plt.ylabel("Sales (in thousands)")
plt.grid(True, alpha=0.3)

# Income plot
plt.subplot(1, 2, 2)
plt.plot(x2, y2, 'g-s', linewidth=2)
plt.title("INCOME", fontsize=14, fontweight='bold')
plt.xlabel("Quarter")
plt.ylabel("Income (in thousands)")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 5. Subplots with super title
print("\n5. Subplots with super title:")
plt.figure(figsize=(12, 5))

# Sales plot
plt.subplot(1, 2, 1)
plt.plot(x1, y1, 'b-o', linewidth=2, markersize=8)
plt.title("SALES", fontsize=12)
plt.xlabel("Quarter")
plt.ylabel("Amount (in thousands)")
plt.grid(True, alpha=0.3)

# Income plot
plt.subplot(1, 2, 2)
plt.plot(x2, y2, 'g-s', linewidth=2, markersize=8)
plt.title("INCOME", fontsize=12)
plt.xlabel("Quarter")
plt.ylabel("Amount (in thousands)")
plt.grid(True, alpha=0.3)

# Add super title for the entire figure
plt.suptitle("MY SHOP - Financial Report", fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# 6. Different plot types in subplots
print("\n6. Different plot types in subplots:")
plt.figure(figsize=(15, 10))

# Line plot
plt.subplot(2, 3, 1)
plt.plot(x1, y1, 'b-o')
plt.title("Line Plot")
plt.grid(True, alpha=0.3)

# Bar plot
plt.subplot(2, 3, 2)
plt.bar(x1, y1, color='red', alpha=0.7)
plt.title("Bar Plot")

# Scatter plot
plt.subplot(2, 3, 3)
plt.scatter(x1, y1, color='green', s=100)
plt.title("Scatter Plot")

# Area plot
plt.subplot(2, 3, 4)
plt.fill_between(x1, y1, color='purple', alpha=0.5)
plt.plot(x1, y1, 'purple', linewidth=2)
plt.title("Area Plot")

# Step plot
plt.subplot(2, 3, 5)
plt.step(x1, y1, 'orange', linewidth=2, where='mid')
plt.title("Step Plot")

# Stem plot
plt.subplot(2, 3, 6)
plt.stem(x1, y1, basefmt=" ")
plt.title("Stem Plot")

plt.suptitle("Different Plot Types", fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# 7. Complex subplot with mathematical functions
print("\n7. Complex subplot with mathematical functions:")
plt.figure(figsize=(12, 8))

# Generate data for mathematical functions
x = np.linspace(0, 2*np.pi, 100)

# Sine function
plt.subplot(2, 2, 1)
plt.plot(x, np.sin(x), 'b-', linewidth=2)
plt.title("Sine Function")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True, alpha=0.3)

# Cosine function
plt.subplot(2, 2, 2)
plt.plot(x, np.cos(x), 'r-', linewidth=2)
plt.title("Cosine Function")
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.grid(True, alpha=0.3)

# Tangent function
plt.subplot(2, 2, 3)
plt.plot(x, np.tan(x), 'g-', linewidth=2)
plt.title("Tangent Function")
plt.xlabel("x")
plt.ylabel("tan(x)")
plt.ylim(-5, 5)  # Limit y-axis for better visualization
plt.grid(True, alpha=0.3)

# Combined functions
plt.subplot(2, 2, 4)
plt.plot(x, np.sin(x), 'b-', label='sin(x)', linewidth=2)
plt.plot(x, np.cos(x), 'r-', label='cos(x)', linewidth=2)
plt.title("Combined Functions")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True, alpha=0.3)

plt.suptitle("Trigonometric Functions", fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

print("\n=== Subplot Layout Reference ===")
print("""
Subplot Layout Syntax: plt.subplot(nrows, ncols, index)

Common Layouts:
- plt.subplot(1, 2, 1) : 1 row, 2 columns, plot 1 (left)
- plt.subplot(1, 2, 2) : 1 row, 2 columns, plot 2 (right)
- plt.subplot(2, 1, 1) : 2 rows, 1 column, plot 1 (top)
- plt.subplot(2, 1, 2) : 2 rows, 1 column, plot 2 (bottom)
- plt.subplot(2, 2, 1) : 2x2 grid, plot 1 (top-left)
- plt.subplot(2, 2, 2) : 2x2 grid, plot 2 (top-right)
- plt.subplot(2, 2, 3) : 2x2 grid, plot 3 (bottom-left)
- plt.subplot(2, 2, 4) : 2x2 grid, plot 4 (bottom-right)

Index numbering goes: left → right, top → bottom

Useful Functions:
- plt.title() : Add title to individual subplot
- plt.suptitle() : Add title to entire figure
- plt.tight_layout() : Automatically adjust spacing
- plt.figure(figsize=(width, height)) : Set figure size
""")

print("All subplot examples completed successfully!")