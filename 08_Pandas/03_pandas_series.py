"""
PANDAS SERIES - STUDY NOTES
============================

Author: Study Notes
Date: September 2025
Topic: Understanding Pandas Series

WHAT IS A SERIES?
-----------------
- A Pandas Series is like a single column in a table
- One-dimensional array that can hold data of any type
- Think of it as a list with labels (index)
- Building block of DataFrames
"""

import pandas as pd

# =============================================================================
# CREATING SERIES FROM LISTS
# =============================================================================

print("=== Creating Series from Lists ===")

# Basic Series creation
numbers = [1, 7, 2]
series_from_list = pd.Series(numbers)

print("Basic Series:")
print(series_from_list)
print(f"Data type: {type(series_from_list)}")

# Accessing values by index
print(f"\nFirst value (index 0): {series_from_list[0]}")
print(f"Second value (index 1): {series_from_list[1]}")

# =============================================================================
# CUSTOM LABELS (INDEX)
# =============================================================================

print("\n=== Series with Custom Labels ===")

# Create Series with custom index
custom_series = pd.Series(numbers, index=["x", "y", "z"])
print("Series with custom labels:")
print(custom_series)

# Access by custom label
print(f"\nValue at label 'y': {custom_series['y']}")
print(f"Value at label 'z': {custom_series['z']}")

# =============================================================================
# SERIES FROM DICTIONARIES
# =============================================================================

print("\n=== Series from Dictionary ===")

# Dictionary becomes Series (keys = index, values = data)
calories_data = {
    "Monday": 420, 
    "Tuesday": 380, 
    "Wednesday": 390,
    "Thursday": 450,
    "Friday": 320
}

calories_series = pd.Series(calories_data)
print("Calories Series:")
print(calories_series)

# =============================================================================
# SELECTIVE SERIES CREATION
# =============================================================================

print("\n=== Selective Series Creation ===")

# Create Series with only specific keys
selected_days = pd.Series(calories_data, index=["Monday", "Wednesday", "Friday"])
print("Selected days only:")
print(selected_days)

# =============================================================================
# SERIES VS DATAFRAMES
# =============================================================================

print("\n=== Series vs DataFrames ===")

# Series: Single column
print("Series (single column):")
duration_series = pd.Series([50, 40, 45], index=["Day1", "Day2", "Day3"])
print(duration_series)

# DataFrame: Multiple columns (table)
print("\nDataFrame (multiple columns - table):")
workout_data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45],
    "type": ["Running", "Cycling", "Swimming"]
}

workout_df = pd.DataFrame(workout_data)
print(workout_df)

# =============================================================================
# USEFUL SERIES METHODS
# =============================================================================

print("\n=== Useful Series Methods ===")
sample_series = pd.Series([10, 20, 30, 40, 50])

print(f"Sum: {sample_series.sum()}")
print(f"Mean: {sample_series.mean()}")
print(f"Max: {sample_series.max()}")
print(f"Min: {sample_series.min()}")
print(f"Standard Deviation: {sample_series.std():.2f}")

# =============================================================================
# KEY POINTS TO REMEMBER:
# =============================================================================
"""
IMPORTANT CONCEPTS:
1. Series = Single column of data with labels
2. DataFrame = Multiple Series combined (table)
3. Index can be default (0,1,2...) or custom labels
4. Dictionary keys automatically become index labels
5. Series support mathematical operations
6. Series are the building blocks of DataFrames
"""
