"""
PANDAS GETTING STARTED - STUDY NOTES
=====================================

Author: Study Notes
Date: September 2025
Topic: Introduction to Pandas Library

OVERVIEW:
---------
Pandas is a powerful data manipulation and analysis library for Python.
It provides data structures and operations for manipulating numerical tables and time series.

INSTALLATION:
------------
# Install Pandas using pip
# Command: pip install pandas
# Alternative: Use Anaconda distribution which includes Pandas
"""

# =============================================================================
# IMPORTING PANDAS
# =============================================================================

# Standard import method
import pandas

# Recommended: Import with alias 'pd' (standard convention)
import pandas as pd

print("Pandas version:", pd.__version__)

# =============================================================================
# BASIC DATAFRAME CREATION
# =============================================================================

# Example 1: Creating a simple DataFrame from dictionary
print("\n=== Example 1: Basic DataFrame ===")
mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

# Create DataFrame using pandas.DataFrame()
myvar = pd.DataFrame(mydataset)
print("DataFrame using dictionary:")
print(myvar)

# =============================================================================
# DATAFRAME WITH DIFFERENT DATA
# =============================================================================

# Example 2: Another DataFrame example
print("\n=== Example 2: Fruits DataFrame ===")
fruits_data = {
    "FRUITS": ["apples", "bananas", "cherries"], 
    "COUNT": [5, 3, 8]
}

fruits_df = pd.DataFrame(fruits_data)
print("Fruits DataFrame:")
print(fruits_df)

# =============================================================================
# KEY POINTS TO REMEMBER:
# =============================================================================
"""
1. Always import pandas as 'pd' - it's the standard convention
2. DataFrame is the primary data structure in pandas
3. DataFrames can be created from dictionaries, lists, CSV files, etc.
4. Use pd.__version__ to check the installed version
5. DataFrames are similar to Excel spreadsheets or SQL tables
"""


