""""""

==============================================================================================================================================================

PIE CHARTS - DETAILED EXAMPLES AND STUDY NOTESPIE CHARTS - DETAILED EXAMPLES AND STUDY NOTES

==============================================================================================================================================================

📚 Learning Objective: Master pie chart creation and customization in Matplotlib📚 Learning Objective: Master pie chart creation and customization in Matplotlib

🎯 Key Concepts: Data visualization, proportions, styling, and best practices🎯 Key Concepts: Data visualization, proportions, styling, and best practices

📅 Comprehensive Guide - Perfect for understanding data proportions!📅 Comprehensive Guide - Perfect for understanding data proportions!

==============================================================================================================================================================

""""""



import matplotlib.pyplot as pltimport matplotlib.pyplot as plt

import numpy as npimport numpy as np



# =============================================================================

# 📖 UNDERSTANDING PIE CHARTS

# =============================================================================# =============================================================================# =============================================================================

print("🔹 WHAT ARE PIE CHARTS?")

print("   ➤ Pie charts show parts of a whole (proportions/percentages)")# 📖 UNDERSTANDING PIE CHARTS# 📖 UNDERSTANDING PIE CHARTS

print("   ➤ Best for showing composition of categorical data")

print("   ➤ Use when you have 3-7 categories maximum")# =============================================================================# =============================================================================

print("   ➤ Each slice represents a proportion of the total")

print()print("🔹 WHAT ARE PIE CHARTS?")

print("🔹 WHAT ARE PIE CHARTS?")

# =============================================================================

# 📖 SECTION 1: BASIC PIE CHARTprint("   ➤ Pie charts show parts of a whole (proportions/percentages)")

# =============================================================================print("   ➤ Pie charts show parts of a whole (proportions/percentages)")

print("🔹 SECTION 1: Creating Your First Pie Chart")

print("   ➤ Best for showing composition of categorical data")

# 📊 Sample data - fruit sales for the monthprint("   ➤ Best for showing composition of categorical data")

y = np.array([35, 25, 25, 15])  # Values for each slice

mylabels = ["Apples", "Bananas", "Cherries", "Dates"]  # Names for each sliceprint("   ➤ Use when you have 3-7 categories maximum")

print("   ➤ Use when you have 3-7 categories maximum")

plt.figure(figsize=(8, 8))

plt.pie(y, labels=mylabels)

plt.title("🍎 Basic Pie Chart - Monthly Fruit Sales", fontsize=14, fontweight='bold')print("   ➤ Each slice represents a proportion of the total")

plt.axis('equal')  # Ensures the pie chart is circularprint("   ➤ Each slice represents a proportion of the total")

plt.show()

print()

print("""print()

📝 UNDERSTANDING THE DATA:

   • Apples: 35 units (largest slice)

   • Bananas: 25 units# =============================================================================# =============================================================================

   • Cherries: 25 units  

   • Dates: 15 units (smallest slice)# 📖 SECTION 1: BASIC PIE CHART# 📖 SECTION 1: BASIC PIE CHART

   

✅ TIP: The pie chart automatically calculates percentages!# =============================================================================# =============================================================================

""")

print("🔹 SECTION 1: Creating Your First Pie Chart")

# =============================================================================print("🔹 SECTION 1: Creating Your First Pie Chart")

# 📖 SECTION 2: EXPLODED PIE CHART

# =============================================================================

print("🔹 SECTION 2: Exploded Pie Chart - Highlighting Important Data")

# 📊 Sample data - fruit sales for the month# 📊 Sample data - fruit sales for the month

# Same data with explode parameter

myexplode = [0.2, 0, 0, 0]  # Only explode the first slice (Apples)y = np.array([35, 25, 25, 15])  # Values for each slicey = np.array([35, 25, 25, 15])  # Values for each slice



plt.figure(figsize=(8, 8))mylabels = ["Apples", "Bananas", "Cherries", "Dates"]  # Names for each slicemylabels = ["Apples", "Bananas", "Cherries", "Dates"]  # Names for each slice

plt.pie(y, labels=mylabels, explode=myexplode)

plt.title("🍎 Exploded Pie Chart - Highlighting Best Seller", fontsize=14, fontweight='bold')

plt.axis('equal')

plt.show()plt.figure(figsize=(8, 8))

plt.figure(figsize=(8, 8))

print("""

📝 EXPLODE PARAMETER EXPLAINED:plt.pie(y, labels=mylabels)plt.pie(y, labels=mylabels)

   • myexplode = [0.2, 0, 0, 0] means:

     - Apples slice: moves out by 0.2 (20% of radius)plt.title("🍎 Basic Pie Chart - Monthly Fruit Sales", fontsize=14, fontweight='bold')plt.title("🍎 Basic Pie Chart - Monthly Fruit Sales", fontsize=14, fontweight='bold')

     - Bananas, Cherries, Dates: stay in place (0)

   plt.axis('equal')  # Ensures the pie chart is circularplt.axis('equal')  # Ensures the pie chart is circular

✅ TIP: Use explode to draw attention to important categories!

""")plt.show()plt.show()



# =============================================================================

# 📖 SECTION 3: PIE CHART WITH PERCENTAGES AND START ANGLE

# =============================================================================print("""print("""

print("🔹 SECTION 3: Professional Pie Chart with Percentages")

📝 UNDERSTANDING THE DATA:📝 UNDERSTANDING THE DATA:

# Enhanced pie chart with percentages and custom start angle

plt.figure(figsize=(10, 8))   • Apples: 35 units (largest slice)   • Apples: 35 units (largest slice)

plt.pie(y, labels=mylabels, explode=myexplode, autopct='%1.1f%%', 

         startangle=90, shadow=True)   • Bananas: 25 units   • Bananas: 25 units

plt.title("🍎 Professional Pie Chart - Sales Distribution", fontsize=16, fontweight='bold')

plt.axis('equal')   • Cherries: 25 units     • Cherries: 25 units  

plt.show()

   • Dates: 15 units (smallest slice)   • Dates: 15 units (smallest slice)

print("""

📝 ENHANCED FEATURES:      

   • autopct='%1.1f%%': Shows percentages on each slice

   • startangle=90: Starts first slice at top (90 degrees)✅ TIP: The pie chart automatically calculates percentages!✅ TIP: The pie chart automatically calculates percentages!

   • shadow=True: Adds depth with shadow effect

   """)""")

✅ MATH NOTE: Each slice size = value ÷ sum of all values × 100%

""")



# =============================================================================# =============================================================================# =============================================================================

# 📖 SECTION 4: CUSTOM COLORS AND PROFESSIONAL STYLING

# =============================================================================# 📖 SECTION 2: EXPLODED PIE CHART# 📖 SECTION 2: EXPLODED PIE CHART

print("🔹 SECTION 4: Custom Colors and Professional Styling")

# =============================================================================# =============================================================================

# Define custom colors for each slice

mycolors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4"]  # Modern color paletteprint("🔹 SECTION 2: Exploded Pie Chart - Highlighting Important Data")print("🔹 SECTION 2: Exploded Pie Chart - Highlighting Important Data")



plt.figure(figsize=(10, 8))

plt.pie(y, labels=mylabels, colors=mycolors, autopct='%1.1f%%', 

         startangle=45, explode=myexplode, shadow=True,# Same data with explode parameter# Same data with explode parameter

         textprops={'fontsize': 12, 'fontweight': 'bold'})

plt.title("🎨 Custom Colored Pie Chart", fontsize=16, fontweight='bold')myexplode = [0.2, 0, 0, 0]  # Only explode the first slice (Apples)myexplode = [0.2, 0, 0, 0]  # Only explode the first slice (Apples)

plt.axis('equal')

plt.show()



print("""plt.figure(figsize=(8, 8))plt.figure(figsize=(8, 8))

📝 COLOR CUSTOMIZATION OPTIONS:

   • Hexadecimal values: "#FF6B6B" (red-pink)plt.pie(y, labels=mylabels, explode=myexplode)plt.pie(y, labels=mylabels, explode=myexplode)

   • Named colors: "red", "blue", "green"

   • Color shortcuts: 'r', 'g', 'b', 'c', 'm', 'y', 'k', 'w'plt.title("🍎 Exploded Pie Chart - Highlighting Best Seller", fontsize=14, fontweight='bold')plt.title("🍎 Exploded Pie Chart - Highlighting Best Seller", fontsize=14, fontweight='bold')

   • textprops: Customize text appearance

""")plt.axis('equal')plt.axis('equal')



# =============================================================================plt.show()plt.show()

# 📖 SECTION 5: PIE CHART WITH LEGEND

# =============================================================================

print("🔹 SECTION 5: Adding Legends for Better Understanding")

print("""print("""

# Create pie chart with comprehensive legend

plt.figure(figsize=(12, 8))📝 EXPLODE PARAMETER EXPLAINED:📝 EXPLODE PARAMETER EXPLAINED:

wedges, texts, autotexts = plt.pie(y, labels=mylabels, colors=mycolors, 

                                   autopct='%1.1f%%', startangle=90,   • myexplode = [0.2, 0, 0, 0] means:   • myexplode = [0.2, 0, 0, 0] means:

                                   explode=myexplode, shadow=True)

plt.title("📊 Pie Chart with Professional Legend", fontsize=16, fontweight='bold')     - Apples slice: moves out by 0.2 (20% of radius)     - Apples slice: moves out by 0.2 (20% of radius)



# Add legend with custom positioning     - Bananas, Cherries, Dates: stay in place (0)     - Bananas, Cherries, Dates: stay in place (0)

plt.legend(wedges, mylabels, title="Fruit Types", loc="center left", 

           bbox_to_anchor=(1, 0, 0.5, 1))      

plt.axis('equal')

plt.show()✅ TIP: Use explode to draw attention to important categories!✅ TIP: Use explode to draw attention to important categories!



print("""""")""")

📝 LEGEND FEATURES:

   • plt.legend(): Adds explanation list

   • title="Fruit Types": Legend header

   • loc="center left": Position control# =============================================================================# =============================================================================

   • bbox_to_anchor: Fine positioning

""")# 📖 SECTION 3: PIE CHART WITH PERCENTAGES AND START ANGLE# 📖 SECTION 3: PIE CHART WITH PERCENTAGES AND START ANGLE



# =============================================================================# =============================================================================# =============================================================================

# 📖 SECTION 6: ADVANCED PIE CHART TECHNIQUES

# =============================================================================print("🔹 SECTION 3: Professional Pie Chart with Percentages")print("🔹 SECTION 3: Professional Pie Chart with Percentages")

print("🔹 SECTION 6: Advanced Techniques and Best Practices")



# Multi-feature advanced pie chart

sales_data = np.array([450, 320, 280, 150, 100])# Enhanced pie chart with percentages and custom start angle# Enhanced pie chart with percentages and custom start angle

products = ['Smartphones', 'Laptops', 'Tablets', 'Accessories', 'Others']

colors_advanced = ['#E74C3C', '#3498DB', '#2ECC71', '#F39C12', '#9B59B6']plt.figure(figsize=(10, 8))plt.figure(figsize=(10, 8))

explode_advanced = (0.05, 0.05, 0.05, 0.05, 0.1)  # Slightly separate all slices

plt.pie(y, labels=mylabels, explode=myexplode, autopct='%1.1f%%', plt.pie(y, labels=mylabels, explode=myexplode, autopct='%1.1f%%', 

plt.figure(figsize=(14, 10))

         startangle=90, shadow=True)         startangle=90, shadow=True)

# Create the pie chart

wedges, texts, autotexts = plt.pie(sales_data, labels=products, plt.title("🍎 Professional Pie Chart - Sales Distribution", fontsize=16, fontweight='bold')plt.title("🍎 Professional Pie Chart - Sales Distribution", fontsize=16, fontweight='bold')

                                   colors=colors_advanced, autopct='%1.1f%%',

                                   startangle=140, explode=explode_advanced,plt.axis('equal')plt.axis('equal')

                                   shadow=True, textprops={'fontsize': 11})

plt.show()plt.show()

# Enhance text appearance

for autotext in autotexts:

    autotext.set_color('white')

    autotext.set_fontweight('bold')print("""print("""



plt.title("💼 Q3 Sales Performance by Product Category", 📝 ENHANCED FEATURES:📝 ENHANCED FEATURES:

          fontsize=18, fontweight='bold', pad=30)

   • autopct='%1.1f%%': Shows percentages on each slice   • autopct='%1.1f%%': Shows percentages on each slice

# Add detailed legend

plt.legend(wedges, [f'{product}: ${value}K' for product, value in zip(products, sales_data)],   • startangle=90: Starts first slice at top (90 degrees)   • startangle=90: Starts first slice at top (90 degrees)

          title="Sales Revenue", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1),

          fontsize=12)   • shadow=True: Adds depth with shadow effect   • shadow=True: Adds depth with shadow effect



plt.axis('equal')      

plt.tight_layout()

plt.show()✅ MATH NOTE: Each slice size = value ÷ sum of all values × 100%✅ MATH NOTE: Each slice size = value ÷ sum of all values × 100%



print("""""")""")

📝 ADVANCED TECHNIQUES USED:

   • Multiple explode values for separation

   • White text on colored slices for contrast

   • Detailed legend with values# =============================================================================# =============================================================================

   • Professional title with padding

   • tight_layout() for optimal spacing# 📖 SECTION 4: CUSTOM COLORS AND PROFESSIONAL STYLING# 📖 SECTION 4: CUSTOM COLORS AND PROFESSIONAL STYLING

""")

# =============================================================================# =============================================================================

# =============================================================================

# 📚 STUDY SUMMARY AND REFERENCEprint("🔹 SECTION 4: Custom Colors and Professional Styling")print("🔹 SECTION 4: Custom Colors and Professional Styling")

# =============================================================================

print("""

===============================================================================

📚 PIE CHARTS - QUICK REFERENCE SUMMARY# Define custom colors for each slice# Define custom colors for each slice

===============================================================================

mycolors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4"]  # Modern color palettemycolors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4"]  # Modern color palette

🔧 ESSENTIAL PARAMETERS:

   • labels: Array of category names

   • autopct: Format string for percentages ('%1.1f%%')

   • colors: Array of colors (hex, named, or shortcuts)plt.figure(figsize=(10, 8))plt.figure(figsize=(10, 8))

   • explode: Array of separation distances (0 = no separation)

   • startangle: Rotation angle in degrees (90 = start at top)plt.pie(y, labels=mylabels, colors=mycolors, autopct='%1.1f%%', plt.pie(y, labels=mylabels, colors=mycolors, autopct='%1.1f%%', 

   • shadow: Boolean for shadow effect

   • textprops: Dictionary for text styling         startangle=45, explode=myexplode, shadow=True,         startangle=45, explode=myexplode, shadow=True,



🎨 COLOR OPTIONS:         textprops={'fontsize': 12, 'fontweight': 'bold'})         textprops={'fontsize': 12, 'fontweight': 'bold'})

   • Named: 'red', 'blue', 'green', 'orange', etc.

   • Shortcuts: 'r', 'g', 'b', 'c', 'm', 'y', 'k', 'w'plt.title("🎨 Custom Colored Pie Chart", fontsize=16, fontweight='bold')plt.title("🎨 Custom Colored Pie Chart", fontsize=16, fontweight='bold')

   • Hex codes: '#FF6B6B', '#4ECDC4', etc.

plt.axis('equal')plt.axis('equal')

📊 BEST PRACTICES:

   • Use for 3-7 categories maximumplt.show()plt.show()

   • Start largest slice at 12 o'clock (startangle=90)

   • Include percentages with autopct

   • Choose contrasting colors

   • Use plt.axis('equal') for circular shapeprint("""print("""



✅ DO's:📝 COLOR CUSTOMIZATION OPTIONS:📝 COLOR CUSTOMIZATION OPTIONS:

   ✓ Order slices by size (largest to smallest)

   ✓ Use explode sparingly to highlight key data   • Hexadecimal values: "#FF6B6B" (red-pink)   • Hexadecimal values: "#FF6B6B" (red-pink)

   ✓ Add legends when labels might be cluttered

   ✓ Test colors for accessibility   • Named colors: "red", "blue", "green"   • Named colors: "red", "blue", "green"



❌ DON'Ts:   • Color shortcuts: 'r', 'g', 'b', 'c', 'm', 'y', 'k', 'w'   • Color shortcuts: 'r', 'g', 'b', 'c', 'm', 'y', 'k', 'w'

   ✗ Don't use for more than 7 categories

   ✗ Don't use 3D effects (misleading)   • textprops: Customize text appearance   • textprops: Customize text appearance

   ✗ Don't explode too many slices

   ✗ Don't use similar colors for adjacent slices""")""")



🚀 REMEMBER: Pie charts tell stories about proportions - make them clear!

===============================================================================

""")# =============================================================================# =============================================================================

# 📖 SECTION 5: PIE CHART WITH LEGEND# 📖 SECTION 5: PIE CHART WITH LEGEND

# =============================================================================# =============================================================================

print("🔹 SECTION 5: Adding Legends for Better Understanding")print("🔹 SECTION 5: Adding Legends for Better Understanding")



# Create pie chart with comprehensive legend# Create pie chart with comprehensive legend

plt.figure(figsize=(12, 8))plt.figure(figsize=(12, 8))

wedges, texts, autotexts = plt.pie(y, labels=mylabels, colors=mycolors, wedges, texts, autotexts = plt.pie(y, labels=mylabels, colors=mycolors, 

                                   autopct='%1.1f%%', startangle=90,                                   autopct='%1.1f%%', startangle=90,

                                   explode=myexplode, shadow=True)                                   explode=myexplode, shadow=True)

plt.title("📊 Pie Chart with Professional Legend", fontsize=16, fontweight='bold')plt.title("📊 Pie Chart with Professional Legend", fontsize=16, fontweight='bold')



# Add legend with custom positioning# Add legend with custom positioning

plt.legend(wedges, mylabels, title="Fruit Types", loc="center left", plt.legend(wedges, mylabels, title="Fruit Types", loc="center left", 

           bbox_to_anchor=(1, 0, 0.5, 1))           bbox_to_anchor=(1, 0, 0.5, 1))

plt.axis('equal')plt.axis('equal')

plt.show()plt.show()



print("""print("""

📝 LEGEND FEATURES:📝 LEGEND FEATURES:

   • plt.legend(): Adds explanation list   • plt.legend(): Adds explanation list

   • title="Fruit Types": Legend header   • title="Fruit Types": Legend header

   • loc="center left": Position control   • loc="center left": Position control

   • bbox_to_anchor: Fine positioning   • bbox_to_anchor: Fine positioning

""")""")



# =============================================================================# =============================================================================

# 📖 SECTION 6: ADVANCED PIE CHART TECHNIQUES# 📖 SECTION 6: ADVANCED PIE CHART TECHNIQUES

# =============================================================================# =============================================================================

print("🔹 SECTION 6: Advanced Techniques and Best Practices")print("🔹 SECTION 6: Advanced Techniques and Best Practices")



# Multi-feature advanced pie chart# Multi-feature advanced pie chart

sales_data = np.array([450, 320, 280, 150, 100])sales_data = np.array([450, 320, 280, 150, 100])

products = ['Smartphones', 'Laptops', 'Tablets', 'Accessories', 'Others']products = ['Smartphones', 'Laptops', 'Tablets', 'Accessories', 'Others']

colors_advanced = ['#E74C3C', '#3498DB', '#2ECC71', '#F39C12', '#9B59B6']colors_advanced = ['#E74C3C', '#3498DB', '#2ECC71', '#F39C12', '#9B59B6']

explode_advanced = (0.05, 0.05, 0.05, 0.05, 0.1)  # Slightly separate all slicesexplode_advanced = (0.05, 0.05, 0.05, 0.05, 0.1)  # Slightly separate all slices



plt.figure(figsize=(14, 10))plt.figure(figsize=(14, 10))



# Create the pie chart# Create the pie chart

wedges, texts, autotexts = plt.pie(sales_data, labels=products, wedges, texts, autotexts = plt.pie(sales_data, labels=products, 

                                   colors=colors_advanced, autopct='%1.1f%%',                                   colors=colors_advanced, autopct='%1.1f%%',

                                   startangle=140, explode=explode_advanced,                                   startangle=140, explode=explode_advanced,

                                   shadow=True, textprops={'fontsize': 11})                                   shadow=True, textprops={'fontsize': 11})



# Enhance text appearance# Enhance text appearance

for autotext in autotexts:for autotext in autotexts:

    autotext.set_color('white')    autotext.set_color('white')

    autotext.set_fontweight('bold')    autotext.set_fontweight('bold')



plt.title("💼 Q3 Sales Performance by Product Category", plt.title("💼 Q3 Sales Performance by Product Category", 

          fontsize=18, fontweight='bold', pad=30)          fontsize=18, fontweight='bold', pad=30)



# Add detailed legend# Add detailed legend

plt.legend(wedges, [f'{product}: ${value}K' for product, value in zip(products, sales_data)],plt.legend(wedges, [f'{product}: ${value}K' for product, value in zip(products, sales_data)],

          title="Sales Revenue", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1),          title="Sales Revenue", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1),

          fontsize=12)          fontsize=12)



plt.axis('equal')plt.axis('equal')

plt.tight_layout()plt.tight_layout()

plt.show()plt.show()



print("""print("""

📝 ADVANCED TECHNIQUES USED:📝 ADVANCED TECHNIQUES USED:

   • Multiple explode values for separation   • Multiple explode values for separation

   • White text on colored slices for contrast   • White text on colored slices for contrast

   • Detailed legend with values   • Detailed legend with values

   • Professional title with padding   • Professional title with padding

   • tight_layout() for optimal spacing   • tight_layout() for optimal spacing

""")""")



# =============================================================================# =============================================================================

# 📚 STUDY SUMMARY AND REFERENCE# 📚 STUDY SUMMARY AND REFERENCE

# =============================================================================# =============================================================================

print("""print("""

==============================================================================================================================================================

📚 PIE CHARTS - QUICK REFERENCE SUMMARY📚 PIE CHARTS - QUICK REFERENCE SUMMARY

==============================================================================================================================================================



🔧 ESSENTIAL PARAMETERS:🔧 ESSENTIAL PARAMETERS:

   • labels: Array of category names   • labels: Array of category names

   • autopct: Format string for percentages ('%1.1f%%')   • autopct: Format string for percentages ('%1.1f%%')

   • colors: Array of colors (hex, named, or shortcuts)   • colors: Array of colors (hex, named, or shortcuts)

   • explode: Array of separation distances (0 = no separation)   • explode: Array of separation distances (0 = no separation)

   • startangle: Rotation angle in degrees (90 = start at top)   • startangle: Rotation angle in degrees (90 = start at top)

   • shadow: Boolean for shadow effect   • shadow: Boolean for shadow effect

   • textprops: Dictionary for text styling   • textprops: Dictionary for text styling



🎨 COLOR OPTIONS:🎨 COLOR OPTIONS:

   • Named: 'red', 'blue', 'green', 'orange', etc.   • Named: 'red', 'blue', 'green', 'orange', etc.

   • Shortcuts: 'r', 'g', 'b', 'c', 'm', 'y', 'k', 'w'   • Shortcuts: 'r', 'g', 'b', 'c', 'm', 'y', 'k', 'w'

   • Hex codes: '#FF6B6B', '#4ECDC4', etc.   • Hex codes: '#FF6B6B', '#4ECDC4', etc.



📊 BEST PRACTICES:📊 BEST PRACTICES:

   • Use for 3-7 categories maximum   • Use for 3-7 categories maximum

   • Start largest slice at 12 o'clock (startangle=90)   • Start largest slice at 12 o'clock (startangle=90)

   • Include percentages with autopct   • Include percentages with autopct

   • Choose contrasting colors   • Choose contrasting colors

   • Use plt.axis('equal') for circular shape   • Use plt.axis('equal') for circular shape



✅ DO's:✅ DO's:

   ✓ Order slices by size (largest to smallest)   ✓ Order slices by size (largest to smallest)

   ✓ Use explode sparingly to highlight key data   ✓ Use explode sparingly to highlight key data

   ✓ Add legends when labels might be cluttered   ✓ Add legends when labels might be cluttered

   ✓ Test colors for accessibility   ✓ Test colors for accessibility



❌ DON'Ts:❌ DON'Ts:

   ✗ Don't use for more than 7 categories   ✗ Don't use for more than 7 categories

   ✗ Don't use 3D effects (misleading)   ✗ Don't use 3D effects (misleading)

   ✗ Don't explode too many slices   ✗ Don't explode too many slices

   ✗ Don't use similar colors for adjacent slices   ✗ Don't use similar colors for adjacent slices



🚀 REMEMBER: Pie charts tell stories about proportions - make them clear!🚀 REMEMBER: Pie charts tell stories about proportions - make them clear!

==============================================================================================================================================================

""")""")