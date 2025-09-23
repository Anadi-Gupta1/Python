"""
PANDAS INTRODUCTION - STUDY NOTES
==================================

Author: Study Notes
Date: September 2025
Topic: What is Pandas and Why Use It

WHAT IS PANDAS?
---------------
Pandas is a powerful Python library designed for working with data sets.
- Created by Wes McKinney in 2008
- Name refers to both "Panel Data" and "Python Data Analysis"
- Essential tool for data science and analysis

KEY FUNCTIONS:
- Analyzing data
- Cleaning data
- Exploring data
- Manipulating data
"""

import pandas as pd

# =============================================================================
# WHY USE PANDAS?
# =============================================================================

print("=== Why Use Pandas? ===")
print("""
1. ANALYZE BIG DATA: Handle large datasets efficiently
2. STATISTICAL ANALYSIS: Make conclusions based on statistical theories
3. DATA CLEANING: Clean messy data sets and make them readable
4. DATA RELEVANCE: Filter and prepare relevant data for analysis
""")

# =============================================================================
# WHAT CAN PANDAS DO?
# =============================================================================

print("\n=== What Can Pandas Do? ===")
capabilities = [
    "Find correlations between columns",
    "Calculate average, max, min values", 
    "Delete irrelevant rows",
    "Handle missing data (NULL values)",
    "Clean messy data",
    "Transform data formats",
    "Merge and join datasets",
    "Group and aggregate data"
]

for i, capability in enumerate(capabilities, 1):
    print(f"{i}. {capability}")

# =============================================================================
# DATA SCIENCE CONNECTION
# =============================================================================

print(f"\n=== Data Science Overview ===")
print("""
DATA SCIENCE: A branch of computer science that studies how to:
- Store data efficiently
- Use data effectively  
- Analyze data for insights
- Derive meaningful information

Pandas is a fundamental tool in the data science workflow.
""")

# =============================================================================
# PANDAS ECOSYSTEM
# =============================================================================

print(f"\n=== Pandas Information ===")
print(f"Pandas Version: {pd.__version__}")
print("Official Repository: https://github.com/pandas-dev/pandas")
print("Documentation: https://pandas.pydata.org/docs/")

# =============================================================================
# KEY CONCEPTS TO REMEMBER:
# =============================================================================
"""
IMPORTANT POINTS:
1. Pandas is essential for data analysis in Python
2. It excels at cleaning and preparing messy data
3. Statistical analysis capabilities are built-in
4. Handles missing data gracefully
5. Perfect for exploring data before analysis
6. Industry standard for data manipulation in Python
"""