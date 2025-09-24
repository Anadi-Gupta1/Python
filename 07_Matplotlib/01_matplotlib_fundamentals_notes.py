"""
===============================================================================
MATPLOTLIB FUNDAMENTALS - STUDY NOTES
===============================================================================
📚 Learning Objective: Master the basic plotting techniques in Matplotlib
🎯 Key Concepts: Line plots, Bar charts, Histograms, Pie charts
📅 Last Updated: September 2025
===============================================================================
"""

import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# 📖 SECTION 1: LINE PLOTS - The Foundation of Data Visualization
# =============================================================================
print("🔹 LEARNING: Creating Basic Line Plots")
print("   ➤ Line plots show relationships between two continuous variables")
print("   ➤ Perfect for time series data and trend analysis")
print()

# Create sample data points
x_points = np.array([0, 0.6])    # X-coordinates (independent variable)
y_points = np.array([0, 250])    # Y-coordinates (dependent variable)

# 🎨 Create the line plot
plt.figure(figsize=(8, 6))       # Set figure size for better visibility
plt.plot(x_points, y_points, 'b-o', linewidth=2, markersize=8)
plt.title('📊 Basic Line Plot Example', fontsize=14, fontweight='bold')
plt.xlabel('X Values', fontsize=12)
plt.ylabel('Y Values', fontsize=12)
plt.grid(True, alpha=0.3)        # Add grid for better readability
plt.show()

print("✅ NOTE: Both x and y arrays must have the same number of points!")
print()

# =============================================================================
# 📖 SECTION 2: BAR CHARTS - Comparing Categories
# =============================================================================
print("🔹 LEARNING: Creating Bar Charts")
print("   ➤ Bar charts compare different categories or groups")
print("   ➤ Great for showing discrete data comparisons")
print()

# Sample data for bar chart
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = np.array([23, 45, 56, 78])

plt.figure(figsize=(10, 6))
bars = plt.bar(categories, values, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
plt.title('📊 Bar Chart - Category Comparison', fontsize=14, fontweight='bold')
plt.xlabel('Categories', fontsize=12)
plt.ylabel('Values', fontsize=12)

# Add value labels on top of bars
for i, v in enumerate(values):
    plt.text(i, v + 1, str(v), ha='center', fontweight='bold')

plt.show()

print("✅ NOTE: Use different colors to distinguish categories clearly!")
print()

# =============================================================================
# 📖 SECTION 3: HISTOGRAMS - Understanding Data Distribution
# =============================================================================
print("🔹 LEARNING: Creating Histograms")
print("   ➤ Histograms show the distribution of a dataset")
print("   ➤ Helpful for understanding data patterns and frequency")
print()

# Generate sample data for histogram
np.random.seed(42)  # For reproducible results
data = np.random.normal(100, 15, 1000)  # Normal distribution

plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='skyblue', alpha=0.7, edgecolor='black')
plt.title('📊 Histogram - Data Distribution Analysis', fontsize=14, fontweight='bold')
plt.xlabel('Data Values', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True, alpha=0.3, axis='y')

# Add statistical information
plt.axvline(data.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {data.mean():.1f}')
plt.legend()
plt.show()

print("✅ NOTE: The number of bins affects the visualization - experiment with different values!")
print()

# =============================================================================
# 📖 SECTION 4: PIE CHARTS - Showing Proportions
# =============================================================================
print("🔹 LEARNING: Creating Pie Charts")
print("   ➤ Pie charts show parts of a whole (percentages/proportions)")
print("   ➤ Best used when you have 5 or fewer categories")
print()

# Data for pie chart
labels = ['Python', 'JavaScript', 'Java', 'C++', 'Other']
sizes = np.array([35, 25, 20, 15, 5])
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57']
explode = (0.1, 0, 0, 0, 0)  # Explode the first slice

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', 
        startangle=90, explode=explode, shadow=True)
plt.title('📊 Programming Languages Usage', fontsize=14, fontweight='bold')
plt.axis('equal')  # Equal aspect ratio ensures circular pie
plt.show()

print("✅ NOTE: Use explode parameter to highlight important segments!")
print()

# =============================================================================
# 📖 SECTION 5: IMPROVED BAR CHART - Advanced Styling
# =============================================================================
print("🔹 LEARNING: Advanced Bar Chart Styling")
print("   ➤ Adding professional touches to make charts more appealing")
print()

# Enhanced bar chart with better styling
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = np.array([120, 135, 140, 125, 160, 145])

plt.figure(figsize=(12, 7))
bars = plt.bar(months, sales, 
               color=['#E74C3C', '#3498DB', '#2ECC71', '#F39C12', '#9B59B6', '#1ABC9C'],
               edgecolor='white', linewidth=1.5)

# Add value labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 2,
             f'${height}K', ha='center', va='bottom', fontweight='bold')

plt.title('📊 Monthly Sales Performance', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Months', fontsize=12, fontweight='bold')
plt.ylabel('Sales (in thousands)', fontsize=12, fontweight='bold')
plt.ylim(0, max(sales) * 1.1)  # Add some space at the top
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

print("✅ STUDY TIP: Always add labels, use consistent colors, and ensure readability!")

# =============================================================================
# 📚 KEY TAKEAWAYS FOR YOUR NOTES:
# =============================================================================
print("""
===============================================================================
📚 MATPLOTLIB FUNDAMENTALS - KEY TAKEAWAYS
===============================================================================
1. LINE PLOTS: Best for continuous data and trends
2. BAR CHARTS: Perfect for comparing categories
3. HISTOGRAMS: Excellent for showing data distributions  
4. PIE CHARTS: Ideal for showing proportions (use sparingly)

🎯 REMEMBER:
   • Always match array sizes for x and y coordinates
   • Use descriptive titles and labels
   • Add grids and legends for clarity
   • Choose appropriate colors and styling
   • Consider your audience when selecting chart types

📖 NEXT STEPS: Practice with your own datasets!
===============================================================================
""")


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()


import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()