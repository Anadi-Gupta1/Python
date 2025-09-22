
"""
Matplotlib Labels and Titles Examples
=====================================
This file demonstrates how to add titles, labels, and format them
with different font properties and positions.
"""

import numpy as np
import matplotlib.pyplot as plt

print("=== Matplotlib Labels and Titles Examples ===\n")

# Sample data for all examples
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# 1. Basic plot with labels
print("1. Basic plot with labels:")
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.title("Sports Watch Data")
plt.show()

# 2. Font properties examples
print("\n2. Font properties for titles and labels:")
plt.figure(figsize=(12, 8))

# Define font dictionaries
font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}
font3 = {'family': 'sans-serif', 'color': 'green', 'size': 18}
font4 = {'family': 'monospace', 'color': 'purple', 'size': 14}

plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title("Sports Watch Data", fontdict=font1)
plt.xlabel("Average Pulse", fontdict=font2)
plt.ylabel("Calorie Burnage", fontdict=font2)

plt.subplot(2, 2, 2)
plt.plot(x, y, 'g--')
plt.title("Green Dashed Line", fontdict=font3)
plt.xlabel("Average Pulse", fontdict=font4)
plt.ylabel("Calorie Burnage", fontdict=font4)

plt.subplot(2, 2, 3)
plt.plot(x, y, 'ro-')
plt.title("Red Circle Markers", fontdict={'family': 'serif', 'color': 'red', 'size': 16})
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.subplot(2, 2, 4)
plt.plot(x, y, 'bs:')
plt.title("Blue Square Dotted", fontdict={'family': 'serif', 'color': 'blue', 'size': 16})
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.tight_layout()
plt.show()

# 3. Title positioning
print("\n3. Title positioning examples:")
plt.figure(figsize=(15, 4))

plt.subplot(1, 3, 1)
plt.plot(x, y)
plt.title("Sports Watch Data", loc='left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.subplot(1, 3, 2)
plt.plot(x, y, 'g-')
plt.title("Sports Watch Data", loc='center')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.subplot(1, 3, 3)
plt.plot(x, y, 'r-')
plt.title("Sports Watch Data", loc='right')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.tight_layout()
plt.show()

# 4. Advanced styling
print("\n4. Advanced styling examples:")
plt.figure(figsize=(12, 8))

# Different font families
plt.subplot(2, 2, 1)
plt.plot(x, y, 'b-o')
plt.title("Serif Font Family", fontdict={'family': 'serif', 'size': 16, 'weight': 'bold'})
plt.xlabel("Average Pulse", fontsize=12, style='italic')
plt.ylabel("Calorie Burnage", fontsize=12, style='italic')

plt.subplot(2, 2, 2)
plt.plot(x, y, 'g-s')
plt.title("Sans-serif Font", fontdict={'family': 'sans-serif', 'size': 16, 'weight': 'bold'})
plt.xlabel("Average Pulse", fontsize=12, weight='bold')
plt.ylabel("Calorie Burnage", fontsize=12, weight='bold')

plt.subplot(2, 2, 3)
plt.plot(x, y, 'r-^')
plt.title("Monospace Font", fontdict={'family': 'monospace', 'size': 16, 'weight': 'bold'})
plt.xlabel("Average Pulse", fontsize=12)
plt.ylabel("Calorie Burnage", fontsize=12)

plt.subplot(2, 2, 4)
plt.plot(x, y, 'm-D')
plt.title("Custom Styled Title", fontdict={'family': 'serif', 'color': 'darkblue', 'size': 18, 'weight': 'bold'})
plt.xlabel("Average Pulse", fontdict={'family': 'serif', 'color': 'darkgreen', 'size': 14})
plt.ylabel("Calorie Burnage", fontdict={'family': 'serif', 'color': 'darkred', 'size': 14})

plt.tight_layout()
plt.show()

# 5. Multiple plots with different styles
print("\n5. Comprehensive example with different datasets:")
plt.figure(figsize=(12, 6))

# Create multiple datasets
x1 = np.linspace(0, 10, 100)
y1 = np.sin(x1)
y2 = np.cos(x1)

plt.plot(x1, y1, 'b-', label='sin(x)', linewidth=2)
plt.plot(x1, y2, 'r--', label='cos(x)', linewidth=2)

plt.title("Trigonometric Functions", 
          fontdict={'family': 'serif', 'color': 'navy', 'size': 20, 'weight': 'bold'},
          loc='center')
plt.xlabel("X values", fontdict={'family': 'serif', 'color': 'darkgreen', 'size': 14})
plt.ylabel("Y values", fontdict={'family': 'serif', 'color': 'darkred', 'size': 14})
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print("\n=== Font Property Reference ===")
print("""
Font Families:
- 'serif': Times New Roman style
- 'sans-serif': Arial style  
- 'monospace': Courier style
- 'cursive': Script style
- 'fantasy': Decorative style

Font Properties:
- family: Font family name
- size: Font size in points
- color: Font color (name or hex)
- weight: 'normal', 'bold', 'light', 'heavy'
- style: 'normal', 'italic', 'oblique'

Title Positions:
- 'left': Left-aligned title
- 'center': Center-aligned (default)
- 'right': Right-aligned title

Common Colors:
'blue', 'red', 'green', 'black', 'white', 'purple',
'orange', 'brown', 'pink', 'gray', 'cyan', 'magenta'
""")

print("All label and title examples completed successfully!")


