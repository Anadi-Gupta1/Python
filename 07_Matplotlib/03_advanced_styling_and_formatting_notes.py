"""
===============================================================================
ADVANCED STYLING AND FORMATTING - COMPREHENSIVE NOTES
===============================================================================
📚 Learning Objective: Master advanced matplotlib styling techniques
🎯 Key Concepts: Markers, line styles, colors, and professional formatting
📅 Advanced Guide - Transform basic plots into professional visualizations!
===============================================================================
"""

import matplotlib.pyplot as plt
import numpy as np

# Sample data for demonstrations
ypoints = np.array([3, 8, 1, 10])      # Y-coordinates for plotting
xpoints = np.array([1, 2, 3, 4])       # X-coordinates for plotting

print("=== 🎨 ADVANCED MATPLOTLIB STYLING AND FORMATTING ===\n")

# =============================================================================
# 📖 UNDERSTANDING MATPLOTLIB STYLING COMPONENTS
# =============================================================================
print("🔹 MATPLOTLIB STYLING HAS THREE MAIN COMPONENTS:")
print("   ➤ MARKERS: Shapes that mark individual data points")
print("   ➤ LINES: Connecting lines between data points")  
print("   ➤ COLORS: Visual distinction and aesthetic appeal")
print("   ➤ FORMAT STRINGS: Compact way to combine all three!")
print()

# 1. Basic markers
print("1. Different marker examples:")
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.plot(ypoints, marker='*')
plt.title("Star Marker")

plt.subplot(2, 3, 2)
plt.plot(ypoints, marker='o')
plt.title("Circle Marker")

plt.subplot(2, 3, 3)
plt.plot(ypoints, marker='s')
plt.title("Square Marker")

plt.subplot(2, 3, 4)
plt.plot(ypoints, marker='^')
plt.title("Triangle Up Marker")

plt.subplot(2, 3, 5)
plt.plot(ypoints, marker='D')
plt.title("Diamond Marker")

plt.subplot(2, 3, 6)
plt.plot(ypoints, marker='x')
plt.title("X Marker")

plt.tight_layout()
plt.show()

# 2. Format strings (marker|line|color)
print("\n2. Format string examples:")
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(ypoints, 'o:r')  # Circle marker, dotted line, red color
plt.title("Circle, Dotted, Red")

plt.subplot(1, 3, 2)
plt.plot(ypoints, 's--g')  # Square marker, dashed line, green color
plt.title("Square, Dashed, Green")

plt.subplot(1, 3, 3)
plt.plot(ypoints, '^-b')  # Triangle marker, solid line, blue color
plt.title("Triangle, Solid, Blue")

plt.tight_layout()
plt.show()

# 3. Marker sizes
print("\n3. Different marker sizes:")
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(ypoints, marker='o', ms=5)
plt.title("Small Markers (ms=5)")

plt.subplot(1, 3, 2)
plt.plot(ypoints, marker='o', ms=15)
plt.title("Medium Markers (ms=15)")

plt.subplot(1, 3, 3)
plt.plot(ypoints, marker='o', ms=25)
plt.title("Large Markers (ms=25)")

plt.tight_layout()
plt.show()

# 4. Marker colors
print("\n4. Marker color examples:")
plt.figure(figsize=(15, 4))

plt.subplot(1, 4, 1)
plt.plot(ypoints, marker='o', ms=15, mec='r')
plt.title("Red Edge Color")

plt.subplot(1, 4, 2)
plt.plot(ypoints, marker='o', ms=15, mfc='g')
plt.title("Green Face Color")

plt.subplot(1, 4, 3)
plt.plot(ypoints, marker='o', ms=15, mec='r', mfc='b')
plt.title("Red Edge, Blue Face")

plt.subplot(1, 4, 4)
plt.plot(ypoints, marker='o', ms=15, mec='#4CAF50', mfc='#4CAF50')
plt.title("Hexadecimal Green")

plt.tight_layout()
plt.show()

# 5. Line styles
print("\n5. Different line styles:")
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(xpoints, ypoints, '-', marker='o')
plt.title("Solid Line")

plt.subplot(2, 2, 2)
plt.plot(xpoints, ypoints, '--', marker='s')
plt.title("Dashed Line")

plt.subplot(2, 2, 3)
plt.plot(xpoints, ypoints, ':', marker='^')
plt.title("Dotted Line")

plt.subplot(2, 2, 4)
plt.plot(xpoints, ypoints, '-.', marker='D')
plt.title("Dash-Dot Line")

plt.tight_layout()
plt.show()

# 6. Comprehensive example
print("\n6. Comprehensive styling example:")
plt.figure(figsize=(10, 6))

# Multiple lines with different styles
x = np.linspace(0, 10, 20)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

plt.plot(x, y1, 'o-r', label='sin(x)', ms=8, linewidth=2)
plt.plot(x, y2, 's--g', label='cos(x)', ms=6, linewidth=2)
plt.plot(x, y3, '^:b', label='sin(x)*cos(x)', ms=10, linewidth=2)

plt.title('Multiple Functions with Different Styles')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print("\n=== Reference Information ===")
print("""
Available Markers:
'o' - Circle        '*' - Star         '.' - Point
',' - Pixel         'x' - X            'X' - X (filled)
'+' - Plus          'P' - Plus (filled) 's' - Square
'D' - Diamond       'd' - Diamond (thin) 'p' - Pentagon
'H' - Hexagon       'h' - Hexagon      'v' - Triangle Down
'^' - Triangle Up   '<' - Triangle Left '>' - Triangle Right
'1' - Tri Down      '2' - Tri Up       '3' - Tri Left
'4' - Tri Right     '|' - Vline        '_' - Hline

Line Styles:
'-' - Solid line    '--' - Dashed line
':' - Dotted line   '-.' - Dash-dot line

Colors:
'r' - Red           'g' - Green         'b' - Blue
'c' - Cyan          'm' - Magenta       'y' - Yellow
'k' - Black         'w' - White

Parameters:
ms/markersize - Marker size
mec/markeredgecolor - Marker edge color
mfc/markerfacecolor - Marker face color
linewidth/lw - Line width
alpha - Transparency (0-1)
""")

# 7. Line width examples
print("\n7. Line width examples:")
plt.figure(figsize=(12, 4))

# Sample data for line width demonstration
xpoints = np.array([10.20, 30.40, 50.60])
ypoints = np.array([20.30, 40.50, 60.70])

plt.subplot(1, 3, 1)
plt.plot(xpoints, ypoints, linewidth=1)
plt.title("Thin Line (linewidth=1)")

plt.subplot(1, 3, 2)
plt.plot(xpoints, ypoints, linewidth=5)
plt.title("Medium Line (linewidth=5)")

plt.subplot(1, 3, 3)
plt.plot(xpoints, ypoints, linewidth=20.5)
plt.title("Thick Line (linewidth=20.5)")

plt.tight_layout()
plt.show()

print("All examples completed successfully!")
