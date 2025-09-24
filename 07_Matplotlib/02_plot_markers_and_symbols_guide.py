"""
===============================================================================
PLOT MARKERS AND SYMBOLS - COMPLETE REFERENCE GUIDE
===============================================================================
📚 Learning Objective: Master all matplotlib marker types and styling options
🎯 Key Concepts: Marker shapes, sizes, colors, and customization
📅 Reference Guide - Keep this handy while plotting!
===============================================================================
"""

import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# 📖 UNDERSTANDING MARKERS
# =============================================================================
print("🔹 WHAT ARE MARKERS?")
print("   ➤ Markers emphasize individual data points on plots")
print("   ➤ Use the 'marker' keyword argument to specify marker type")
print("   ➤ Essential for scatter plots and highlighting trends")
print()

# Sample data for demonstrations
xpoints = np.array([1, 2, 3, 4, 5, 6])
ypoints = np.array([2, 4, 1, 5, 3, 6])

# =============================================================================
# 📖 SECTION 1: BASIC MARKER EXAMPLES
# =============================================================================
print("🔹 BASIC MARKER DEMONSTRATIONS:")

plt.figure(figsize=(15, 10))

# Circle marker example
plt.subplot(2, 3, 1)
plt.plot(xpoints, ypoints, marker='o', linestyle='-', markersize=8, linewidth=2)
plt.title("Circle Marker 'o'", fontsize=12, fontweight='bold')
plt.grid(True, alpha=0.3)

# Star marker example  
plt.subplot(2, 3, 2)
plt.plot(xpoints, ypoints, marker='*', linestyle='-', markersize=10, linewidth=2)
plt.title("Star Marker '*'", fontsize=12, fontweight='bold')
plt.grid(True, alpha=0.3)

# Square marker example
plt.subplot(2, 3, 3)
plt.plot(xpoints, ypoints, marker='s', linestyle='-', markersize=8, linewidth=2)
plt.title("Square Marker 's'", fontsize=12, fontweight='bold')
plt.grid(True, alpha=0.3)

# Triangle up marker example
plt.subplot(2, 3, 4)
plt.plot(xpoints, ypoints, marker='^', linestyle='-', markersize=8, linewidth=2)
plt.title("Triangle Up '^'", fontsize=12, fontweight='bold')
plt.grid(True, alpha=0.3)

# Diamond marker example
plt.subplot(2, 3, 5)
plt.plot(xpoints, ypoints, marker='D', linestyle='-', markersize=8, linewidth=2)
plt.title("Diamond Marker 'D'", fontsize=12, fontweight='bold')
plt.grid(True, alpha=0.3)

# X marker example
plt.subplot(2, 3, 6)
plt.plot(xpoints, ypoints, marker='x', linestyle='-', markersize=8, linewidth=2)
plt.title("X Marker 'x'", fontsize=12, fontweight='bold')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.suptitle('📊 MATPLOTLIB MARKER EXAMPLES', fontsize=16, fontweight='bold', y=0.98)
plt.show()

print("✅ TIP: Combine markers with different line styles for variety!")
print()

# =============================================================================
# 📖 SECTION 2: COMPLETE MARKER REFERENCE TABLE
# =============================================================================
print("🔹 COMPLETE MARKER REFERENCE:")
print("""
===============================================================================
MARKER SYMBOLS REFERENCE TABLE
===============================================================================
BASIC SHAPES:
   'o'  →  Circle (most common)
   '*'  →  Star (eye-catching)
   '.'  →  Point (small dot)
   ','  →  Pixel (tiny point)
   's'  →  Square
   'D'  →  Diamond (filled)
   'd'  →  Diamond (thin)
   
LINES AND CROSSES:
   'x'  →  X mark
   'X'  →  X (filled/bold)
   '+'  →  Plus sign
   'P'  →  Plus (filled)
   '|'  →  Vertical line
   '_'  →  Horizontal line
   
TRIANGLES:
   '^'  →  Triangle pointing up
   'v'  →  Triangle pointing down
   '<'  →  Triangle pointing left
   '>'  →  Triangle pointing right
   '1'  →  Tri down (different style)
   '2'  →  Tri up (different style)
   '3'  →  Tri left (different style)
   '4'  →  Tri right (different style)
   
POLYGONS:
   'p'  →  Pentagon (5-sided)
   'H'  →  Hexagon (large)
   'h'  →  Hexagon (small)
===============================================================================
""")

# =============================================================================
# 📖 SECTION 3: COLOR REFERENCE
# =============================================================================
print("🔹 COLOR ABBREVIATIONS:")
print("""
===============================================================================
BASIC COLOR CODES
===============================================================================
   'r'  →  Red
   'g'  →  Green  
   'b'  →  Blue
   'c'  →  Cyan (light blue)
   'm'  →  Magenta (purple-pink)
   'y'  →  Yellow
   'k'  →  Black
   'w'  →  White
===============================================================================
""")

# =============================================================================
# 📖 SECTION 4: PRACTICAL EXAMPLES WITH COLORS
# =============================================================================
print("🔹 MARKER + COLOR COMBINATIONS:")

plt.figure(figsize=(15, 8))

# Create different colored marker examples
colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
markers = ['o', '*', 's', '^', 'D', 'x', '+']
color_names = ['Red', 'Green', 'Blue', 'Cyan', 'Magenta', 'Yellow', 'Black']

for i in range(len(colors)):
    plt.subplot(2, 4, i+1)
    plt.plot(xpoints, ypoints, marker=markers[i], color=colors[i], 
             linestyle='-', markersize=10, linewidth=2)
    plt.title(f"{color_names[i]} {markers[i]}", fontsize=12, fontweight='bold')
    plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.suptitle('📊 MARKER + COLOR COMBINATIONS', fontsize=16, fontweight='bold', y=0.98)
plt.show()

# =============================================================================
# 📖 SECTION 5: ADVANCED MARKER CUSTOMIZATION
# =============================================================================
print("🔹 ADVANCED MARKER CUSTOMIZATION:")

plt.figure(figsize=(12, 8))

# Size variations
plt.subplot(2, 2, 1)
sizes = [5, 10, 15, 20, 25, 30]
plt.plot(xpoints, ypoints, marker='o', markersize=sizes[0], label=f'Size {sizes[0]}')
for i, size in enumerate(sizes[1:], 1):
    plt.scatter(xpoints[i-1], ypoints[i-1], marker='o', s=size*10, alpha=0.7)
plt.title('Variable Marker Sizes', fontsize=12, fontweight='bold')
plt.grid(True, alpha=0.3)

# Edge and face colors
plt.subplot(2, 2, 2)
plt.plot(xpoints, ypoints, marker='o', markersize=12, 
         markerfacecolor='yellow', markeredgecolor='red', markeredgewidth=2)
plt.title('Custom Edge/Face Colors', fontsize=12, fontweight='bold')
plt.grid(True, alpha=0.3)

# Multiple marker styles
plt.subplot(2, 2, 3)
plt.plot(xpoints[:3], ypoints[:3], 'ro-', markersize=10, label='Red circles')
plt.plot(xpoints[2:], ypoints[2:], 'g^-', markersize=10, label='Green triangles')
plt.title('Multiple Marker Styles', fontsize=12, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)

# Transparency effects
plt.subplot(2, 2, 4)
plt.plot(xpoints, ypoints, marker='o', markersize=15, alpha=0.5, linewidth=3)
plt.title('Semi-transparent Markers', fontsize=12, fontweight='bold')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# =============================================================================
# 📚 STUDY NOTES & QUICK TIPS
# =============================================================================
print("""
===============================================================================
📚 MARKERS - STUDY NOTES & QUICK TIPS
===============================================================================
🎯 KEY REMINDERS:
   • Use 'marker' parameter to specify marker type
   • Combine with 'markersize' to control size
   • Use 'markerfacecolor' and 'markeredgecolor' for custom colors
   • 'alpha' parameter controls transparency (0=invisible, 1=opaque)
   
💡 BEST PRACTICES:
   • Circle 'o' - Most versatile and readable
   • Star '*' - Great for highlighting important points
   • Square 's' - Good for categorical data
   • Triangles '^,v,<,>' - Useful for directional data
   
🚀 PRO TIPS:
   • Combine markers: plt.plot(x, y, 'ro-') = red circles with line
   • Format string order: [color][marker][line] (e.g., 'ro-', 'g*--')
   • Use larger markers for small datasets
   • Consider color-blind friendly palettes for presentations
   
📖 REMEMBER: The right marker makes your data story clearer!
===============================================================================
""")	
'w'	White