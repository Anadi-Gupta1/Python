"""
READING CSV FILES WITH PANDAS - STUDY NOTES
============================================

Author: Study Notes
Date: September 2025  
Topic: Reading and Loading CSV Files

WHAT ARE CSV FILES?
-------------------
- CSV = Comma Separated Values
- Plain text format for storing tabular data
- Widely supported format (Excel, Google Sheets, databases)
- Perfect for data exchange between systems
- Pandas can easily read and write CSV files
"""

import pandas as pd

# =============================================================================
# BASIC CSV READING
# =============================================================================

print("=== Reading CSV Files ===")

# Note: These examples assume CSV files exist
# In practice, you would have actual CSV files to read

# Basic CSV reading syntax
"""
df = pd.read_csv('filename.csv')
"""

# Create a sample DataFrame to demonstrate
sample_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'London', 'Tokyo', 'Paris', 'Berlin'],
    'Salary': [50000, 60000, 55000, 52000, 58000]
}

df_sample = pd.DataFrame(sample_data)
print("Sample DataFrame (simulating CSV data):")
print(df_sample)

# =============================================================================
# DISPLAY OPTIONS
# =============================================================================

print("\n=== Display Options ===")

# Check default max rows setting
print(f"Default max rows displayed: {pd.options.display.max_rows}")

# Using to_string() to show entire DataFrame
print("\nUsing .to_string() method:")
print(df_sample.to_string())

# =============================================================================
# CUSTOMIZING DISPLAY SETTINGS
# =============================================================================

print("\n=== Customizing Display ===")

# Change maximum rows display
original_max_rows = pd.options.display.max_rows
pd.options.display.max_rows = 20
print(f"Changed max rows to: {pd.options.display.max_rows}")

# Reset to original
pd.options.display.max_rows = original_max_rows

# =============================================================================
# CSV READING PARAMETERS
# =============================================================================

print("\n=== CSV Reading Parameters ===")

# Common pd.read_csv() parameters:
csv_parameters = """
Important pd.read_csv() parameters:

1. filepath_or_buffer: Path to the CSV file
2. sep or delimiter: Separator character (default: ',')
3. header: Row to use as column names (default: 0)
4. index_col: Column to use as row labels
5. usecols: Subset of columns to read
6. skiprows: Rows to skip at the beginning
7. nrows: Number of rows to read
8. encoding: Character encoding (e.g., 'utf-8')
9. na_values: Additional strings to recognize as NaN
"""

print(csv_parameters)

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

print("\n=== Practical CSV Examples ===")

# Save sample data to demonstrate
df_sample.to_csv('sample_data.csv', index=False)
print("Created sample_data.csv file")

# Read it back
df_from_csv = pd.read_csv('sample_data.csv')
print("\nReading back from CSV:")
print(df_from_csv.head())

# Read with custom parameters
"""
Examples of reading with parameters:

# Read specific columns only
df = pd.read_csv('file.csv', usecols=['Name', 'Age'])

# Read with custom separator
df = pd.read_csv('file.txt', sep='\t')  # Tab-separated

# Skip header and provide own column names
df = pd.read_csv('file.csv', header=None, names=['Col1', 'Col2'])

# Set a column as index
df = pd.read_csv('file.csv', index_col='Name')

# Read only first 100 rows
df = pd.read_csv('file.csv', nrows=100)
"""

# =============================================================================
# FILE INFO AND EXPLORATION
# =============================================================================

print("\n=== File Exploration ===")
print(f"DataFrame shape: {df_from_csv.shape}")
print(f"Data types:\n{df_from_csv.dtypes}")
print(f"\nFirst 3 rows:\n{df_from_csv.head(3)}")
print(f"\nBasic statistics:\n{df_from_csv.describe()}")

# =============================================================================
# KEY POINTS TO REMEMBER:
# =============================================================================
"""
IMPORTANT CONCEPTS:
1. pd.read_csv() is the main function for reading CSV files
2. Use .to_string() to display entire DataFrame
3. Display options can be customized with pd.options
4. Many parameters available for flexible CSV reading
5. Always check data after loading (.head(), .info(), .describe())
6. CSV is the most common format for data exchange
7. Handle encoding issues with encoding parameter
""" 