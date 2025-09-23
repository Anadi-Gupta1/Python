"""
PANDAS DATAFRAMES - STUDY NOTES
================================

Author: Study Notes  
Date: September 2025
Topic: Understanding Pandas DataFrames

WHAT IS A DATAFRAME?
--------------------
- 2-dimensional data structure (like a table)
- Has rows and columns (like Excel spreadsheet)
- Most commonly used pandas object
- Can store different data types in different columns
"""

import pandas as pd

# =============================================================================
# CREATING BASIC DATAFRAMES
# =============================================================================

print("=== Creating Basic DataFrames ===")

# Create DataFrame from dictionary
workout_data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45],
    "exercise": ["Running", "Cycling", "Swimming"]
}

df = pd.DataFrame(workout_data)
print("Basic DataFrame:")
print(df)
print(f"Shape: {df.shape}")  # (rows, columns)

# =============================================================================
# ACCESSING ROWS WITH LOC
# =============================================================================

print("\n=== Accessing Rows with .loc ===")

# Single row (returns Series)
print("Single row (index 0):")
print(df.loc[0])
print(f"Type: {type(df.loc[0])}")

# Multiple rows (returns DataFrame) 
print("\nMultiple rows (index 0 and 1):")
print(df.loc[[0, 1]])
print(f"Type: {type(df.loc[[0, 1]])}")

# =============================================================================
# CUSTOM INDEX LABELS
# =============================================================================

print("\n=== DataFrames with Custom Index ===")

# Create DataFrame with named indexes
df_named = pd.DataFrame(workout_data, index=["Monday", "Tuesday", "Wednesday"])
print("DataFrame with named index:")
print(df_named)

# Access by named index
print(f"\nTuesday's data:")
print(df_named.loc["Tuesday"])

# =============================================================================
# ACCESSING COLUMNS
# =============================================================================

print("\n=== Accessing Columns ===")

# Single column (returns Series)
print("Calories column:")
print(df_named["calories"])

# Multiple columns (returns DataFrame)
print("\nCalories and Duration columns:")
print(df_named[["calories", "duration"]])

# =============================================================================
# DATAFRAME METHODS AND PROPERTIES
# =============================================================================

print("\n=== DataFrame Methods ===")

print(f"DataFrame Info:")
print(f"Shape: {df_named.shape}")
print(f"Columns: {list(df_named.columns)}")
print(f"Index: {list(df_named.index)}")
print(f"Data types:\n{df_named.dtypes}")

print(f"\nBasic statistics:")
print(df_named.describe())

# =============================================================================
# LOADING DATA FROM FILES
# =============================================================================

print("\n=== Loading Data from Files ===")

# Example of reading CSV (commented out as file may not exist)
"""
# Read from CSV file
df_from_csv = pd.read_csv('data.csv')
print(df_from_csv)

# Other file formats pandas can read:
# df = pd.read_excel('file.xlsx')    # Excel files
# df = pd.read_json('file.json')     # JSON files
# df = pd.read_sql(query, connection) # SQL databases
"""

# =============================================================================
# DATAFRAME CREATION EXAMPLES
# =============================================================================

print("\n=== More DataFrame Examples ===")

# From list of lists
list_data = [
    ["Alice", 25, "Engineer"],
    ["Bob", 30, "Doctor"], 
    ["Charlie", 35, "Teacher"]
]

df_from_lists = pd.DataFrame(list_data, 
                           columns=["Name", "Age", "Profession"],
                           index=["Person1", "Person2", "Person3"])
print("DataFrame from list of lists:")
print(df_from_lists)

# =============================================================================
# KEY POINTS TO REMEMBER:
# =============================================================================
"""
IMPORTANT CONCEPTS:
1. DataFrame = 2D table with rows and columns
2. .loc[] is used to access rows by label/index
3. Column access: df["column"] or df[["col1", "col2"]]
4. Custom index makes data more readable
5. DataFrames can be created from various sources
6. Each column can have different data types
7. Use .shape, .dtypes, .describe() for quick info
""" 