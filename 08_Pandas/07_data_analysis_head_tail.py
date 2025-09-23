"""
PANDAS DATA ANALYSIS - HEAD & TAIL - STUDY NOTES
================================================

Author: Study Notes
Date: September 2025
Topic: Data Analysis with head() and tail() methods

OVERVIEW:
---------
- head() and tail() are essential for quick data overview
- Perfect for exploring large datasets
- Help understand data structure before analysis
"""

import pandas as pd

# =============================================================================
# DATA ANALYSIS METHODS
# =============================================================================

print("=== Data Analysis with head() and tail() ===")

# Create sample data for demonstration
sample_data = {
    'Duration': [60, 60, 60, 45, 45, 60, 60, 45, 45, 60, 60, 60, 60],
    'Pulse': [110, 117, 103, 109, 117, 102, 110, 104, 109, 98, 103, 100, 106],
    'Maxpulse': [130, 145, 135, 175, 148, 127, 136, 134, 133, 124, 147, 120, 128],
    'Calories': [409, 479, 340, 282, 406, 300, 374, 253, 195, 269, 329, 250, 345]
}

df = pd.DataFrame(sample_data)

# =============================================================================
# HEAD() METHOD - VIEW FIRST ROWS
# =============================================================================

print("\n=== Using head() method ===")

# Default head() - shows first 5 rows
print("First 5 rows (default):")
print(df.head())

# Specify number of rows
print("\nFirst 3 rows:")
print(df.head(3))

print("\nFirst 10 rows:")
print(df.head(10))

# =============================================================================
# TAIL() METHOD - VIEW LAST ROWS
# =============================================================================

print("\n=== Using tail() method ===")

# Default tail() - shows last 5 rows
print("Last 5 rows (default):")
print(df.tail())

# Specify number of rows
print("\nLast 3 rows:")
print(df.tail(3))

# =============================================================================
# INFO() METHOD - DATASET INFORMATION
# =============================================================================

print("\n=== Dataset Information with info() ===")
print("Complete dataset information:")
print(df.info())

print("\n=== Understanding info() output ===")
info_explanation = """
INFO() METHOD EXPLAINS:
1. DataFrame class and memory usage
2. RangeIndex: Number of entries (rows)
3. Data columns: Column count and names
4. Non-Null Count: Missing values per column
5. Dtype: Data type of each column
6. Memory usage: Space consumed by DataFrame
"""
print(info_explanation)

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

print("\n=== Practical Data Exploration ===")

# Combine multiple methods for comprehensive overview
print("Dataset shape:", df.shape)
print("\nColumn names:", list(df.columns))
print("\nData types:")
print(df.dtypes)

print("\nFirst and last rows comparison:")
print("FIRST 2 ROWS:")
print(df.head(2))
print("\nLAST 2 ROWS:")
print(df.tail(2))

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Basic statistics
print("\nBasic statistics:")
print(df.describe())

# =============================================================================
# BEST PRACTICES
# =============================================================================

print("\n=== Best Practices ===")
best_practices = """
DATA EXPLORATION WORKFLOW:
1. df.head() - Quick look at first few rows
2. df.tail() - Check last few rows
3. df.info() - Get dataset overview
4. df.describe() - Statistical summary
5. df.shape - Dimensions (rows, columns)
6. df.columns - Column names
7. df.isnull().sum() - Check missing values
"""
print(best_practices)

# =============================================================================
# KEY POINTS TO REMEMBER:
# =============================================================================
"""
IMPORTANT CONCEPTS:
1. head() shows first n rows (default: 5)
2. tail() shows last n rows (default: 5)
3. info() provides comprehensive dataset information
4. Always explore data before analysis
5. Check for missing values and data types
6. Use describe() for statistical overview
7. These methods are essential for data quality assessment
"""