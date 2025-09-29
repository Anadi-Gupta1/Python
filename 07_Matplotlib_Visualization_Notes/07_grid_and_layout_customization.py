"""
===============================================================================
GRID AND LAYOUT CUSTOMIZATION - STUDY NOTES
===============================================================================
📚 Learning Objective: Master grid customization and plot layout optimization
🎯 Key Concepts: Grid styling, axis customization, layout management
📅 Professional Plotting Guide - Make your charts publication-ready!
===============================================================================
"""

import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# 📖 UNDERSTANDING GRIDS
# =============================================================================
print("🔹 WHY USE GRIDS?")
print("   ➤ Grids help readers estimate values more accurately")
print("   ➤ Make data points easier to read and interpret")
print("   ➤ Add professional appearance to your visualizations")
print()

# Sample data for all examples
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2, 8, 4, 12, 7, 10])

# =============================================================================
# 📖 SECTION 1: BASIC GRID OPTIONS
# =============================================================================
print("🔹 SECTION 1: Basic Grid Examples")

plt.figure(figsize=(15, 10))

# No grid (default)
plt.subplot(2, 3, 1)
plt.plot(x, y, 'bo-', markersize=8, linewidth=2)
plt.title('No Grid (Default)', fontsize=12, fontweight='bold')

# Basic grid (both x and y)
plt.subplot(2, 3, 2)
plt.plot(x, y, 'ro-', markersize=8, linewidth=2)
plt.grid()  # Enables both x and y grid lines
plt.title('Basic Grid (Both Axes)', fontsize=12, fontweight='bold')

# X-axis grid only
plt.subplot(2, 3, 3)
plt.plot(x, y, 'go-', markersize=8, linewidth=2)
plt.grid(axis='x')  # Only vertical grid lines
plt.title('X-Axis Grid Only', fontsize=12, fontweight='bold')

# Y-axis grid only
plt.subplot(2, 3, 4)
plt.plot(x, y, 'mo-', markersize=8, linewidth=2)
plt.grid(axis='y')  # Only horizontal grid lines
plt.title('Y-Axis Grid Only', fontsize=12, fontweight='bold')

# Customized grid with transparency
plt.subplot(2, 3, 5)
plt.plot(x, y, 'co-', markersize=8, linewidth=2)
plt.grid(True, alpha=0.3)  # Semi-transparent grid
plt.title('Transparent Grid', fontsize=12, fontweight='bold')

# Grid with custom styling
plt.subplot(2, 3, 6)
plt.plot(x, y, 'ko-', markersize=8, linewidth=2)
plt.grid(True, linestyle='--', alpha=0.7, color='red')
plt.title('Custom Styled Grid', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.suptitle('📊 MATPLOTLIB GRID EXAMPLES', fontsize=16, fontweight='bold', y=0.98)
plt.show()

# =============================================================================
# 📖 SECTION 2: HORIZONTAL BAR CHART WITH GRID
# =============================================================================
print("🔹 SECTION 2: Grid with Horizontal Bar Chart")

categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
values = np.array([23, 45, 67, 34, 56])

plt.figure(figsize=(12, 8))

# Horizontal bar chart with customized height and grid
plt.barh(categories, values, height=0.6, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57'])
plt.grid(axis='x', alpha=0.7, linestyle='-', linewidth=0.5)  # Vertical grid for horizontal bars
plt.title('📊 Horizontal Bar Chart with Grid', fontsize=14, fontweight='bold')
plt.xlabel('Values', fontsize=12, fontweight='bold')
plt.ylabel('Categories', fontsize=12, fontweight='bold')

# Add value labels
for i, v in enumerate(values):
    plt.text(v + 1, i, str(v), va='center', fontweight='bold')

plt.tight_layout()
plt.show()

print("""
📝 KEY NOTES:
   • height=0.6 controls bar thickness (default is 0.8)
   • For horizontal bars, use axis='x' for grid lines
   • For vertical bars, use axis='y' for grid lines
""")

# =============================================================================
# 📖 SECTION 3: ADVANCED GRID CUSTOMIZATION
# =============================================================================
print("🔹 SECTION 3: Advanced Grid Styling Options")

plt.figure(figsize=(15, 10))

# Different linestyles
linestyles = ['-', '--', '-.', ':']
style_names = ['Solid', 'Dashed', 'Dash-dot', 'Dotted']

for i, (style, name) in enumerate(zip(linestyles, style_names)):
    plt.subplot(2, 2, i+1)
    plt.plot(x, y, 'o-', markersize=8, linewidth=2)
    plt.grid(True, linestyle=style, alpha=0.7, linewidth=1.5)
    plt.title(f'{name} Grid Lines', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.suptitle('📊 DIFFERENT GRID LINE STYLES', fontsize=16, fontweight='bold', y=0.98)
plt.show()

# =============================================================================
# 📖 SECTION 4: PROFESSIONAL GRID SETUP
# =============================================================================
print("🔹 SECTION 4: Professional Grid Configuration")

# Create a professional-looking plot
plt.figure(figsize=(12, 8))

plt.plot(x, y, 'o-', color='#2E86C1', markersize=10, linewidth=3, 
         markerfacecolor='white', markeredgewidth=2, markeredgecolor='#2E86C1')

# Major grid
plt.grid(True, which='major', linestyle='-', alpha=0.6, color='gray')

# Minor grid (requires setting minor ticks)
plt.minorticks_on()
plt.grid(True, which='minor', linestyle=':', alpha=0.3, color='gray')

plt.title('📊 Professional Chart with Major & Minor Grids', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Time Period', fontsize=14, fontweight='bold')
plt.ylabel('Performance Score', fontsize=14, fontweight='bold')

# Customize tick parameters
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.tight_layout()
plt.show()

# =============================================================================
# 📚 GRID CUSTOMIZATION - STUDY SUMMARY
# =============================================================================
print("""
===============================================================================
📚 GRID CUSTOMIZATION - STUDY SUMMARY
===============================================================================
🎯 BASIC GRID COMMANDS:
   • plt.grid()                    → Enable basic grid (both axes)
   • plt.grid(axis='x')           → Only vertical grid lines
   • plt.grid(axis='y')           → Only horizontal grid lines
   • plt.grid(False)              → Disable grid

🎨 STYLING OPTIONS:
   • alpha=0.3                    → Transparency (0=invisible, 1=opaque)
   • linestyle='--'               → Dashed lines ('-', '--', '-.', ':')
   • color='red'                  → Grid line color
   • linewidth=1.5                → Grid line thickness

💡 PROFESSIONAL TIPS:
   • Use alpha=0.3 to 0.7 for subtle grids
   • Match grid color to your theme
   • For horizontal bars: use axis='x' grid
   • For vertical bars: use axis='y' grid
   • Combine major and minor grids for precision

📖 REMEMBER: Grids should enhance readability, not distract from data!
===============================================================================
""")


