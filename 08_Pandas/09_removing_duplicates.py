"""
PANDAS REMOVING DUPLICATES - STUDY NOTES
=========================================

Author: Study Notes
Date: September 2025
Topic: Finding and Removing Duplicate Data

OVERVIEW:
---------
- Duplicate rows can skew analysis results
- drop_duplicates() method removes duplicate rows
- duplicated() method identifies duplicate rows
- Various options available for handling duplicates
"""

import pandas as pd

# =============================================================================
# CREATING SAMPLE DATA WITH DUPLICATES
# =============================================================================

print("=== Removing Duplicates - Study Examples ===")

# Create sample data with intentional duplicates
sample_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Diana', 'Bob', 'Eve'],
    'Age': [25, 30, 35, 25, 28, 30, 32],
    'City': ['NYC', 'London', 'Tokyo', 'NYC', 'Paris', 'London', 'Berlin'],
    'Salary': [50000, 60000, 55000, 50000, 52000, 60000, 58000]
}

df = pd.DataFrame(sample_data)
print("Original DataFrame with duplicates:")
print(df)
print(f"Shape: {df.shape}")

# =============================================================================
# IDENTIFYING DUPLICATES
# =============================================================================

print("\n=== Identifying Duplicates ===")

# Check for duplicate rows
duplicated_rows = df.duplicated()
print("Duplicate rows (True = duplicate):")
print(duplicated_rows)

# Count duplicates
print(f"\nNumber of duplicate rows: {duplicated_rows.sum()}")

# Show only duplicate rows
print("\nActual duplicate rows:")
print(df[duplicated_rows])

# =============================================================================
# REMOVING DUPLICATES
# =============================================================================

print("\n=== Removing Duplicates ===")

# Method 1: Create new DataFrame without duplicates
df_clean = df.drop_duplicates()
print("New DataFrame after removing duplicates:")
print(df_clean)
print(f"Shape: {df_clean.shape}")

# Method 2: Remove duplicates from original DataFrame
print("\n=== Remove from Original DataFrame ===")
df_copy = df.copy()
print(f"Before removal - Shape: {df_copy.shape}")

df_copy.drop_duplicates(inplace=True)
print(f"After removal - Shape: {df_copy.shape}")
print("DataFrame after inplace duplicate removal:")
print(df_copy)

# =============================================================================
# ADVANCED DUPLICATE HANDLING
# =============================================================================

print("\n=== Advanced Duplicate Handling ===")

# Keep different instances of duplicates
print("Keep first occurrence (default):")
df_keep_first = df.drop_duplicates(keep='first')
print(df_keep_first)

print("\nKeep last occurrence:")
df_keep_last = df.drop_duplicates(keep='last')
print(df_keep_last)

print("\nRemove all duplicates (keep none):")
df_keep_none = df.drop_duplicates(keep=False)
print(df_keep_none)

# =============================================================================
# DUPLICATES BASED ON SPECIFIC COLUMNS
# =============================================================================

print("\n=== Duplicates Based on Specific Columns ===")

# Remove duplicates based only on 'Name' column
df_name_duplicates = df.drop_duplicates(subset=['Name'])
print("Remove duplicates based on 'Name' column only:")
print(df_name_duplicates)

# Remove duplicates based on multiple columns
df_multi_col = df.drop_duplicates(subset=['Name', 'Age'])
print("\nRemove duplicates based on 'Name' and 'Age':")
print(df_multi_col)

# =============================================================================
# DUPLICATE ANALYSIS
# =============================================================================

print("\n=== Duplicate Analysis ===")

# Count duplicates by column
print("Duplicate analysis by Name:")
name_counts = df['Name'].value_counts()
print(name_counts)

# Find duplicates in specific columns
print(f"\nDuplicates in 'Name' column: {df['Name'].duplicated().sum()}")
print(f"Duplicates in 'Age' column: {df['Age'].duplicated().sum()}")

# Show all instances of duplicated names
duplicated_names = df['Name'].duplicated(keep=False)
print(f"\nAll rows with duplicated names:")
print(df[duplicated_names])

# =============================================================================
# PRACTICAL EXAMPLE
# =============================================================================

print("\n=== Practical Example ===")

# More realistic dataset
customer_data = {
    'CustomerID': [1, 2, 3, 1, 4, 2, 5],
    'Name': ['John', 'Jane', 'Bob', 'John', 'Alice', 'Jane', 'Charlie'],
    'Email': ['john@email.com', 'jane@email.com', 'bob@email.com', 
              'john@email.com', 'alice@email.com', 'jane@email.com', 'charlie@email.com'],
    'Purchase': [100, 200, 150, 300, 250, 180, 120]
}

customers_df = pd.DataFrame(customer_data)
print("Customer data with duplicates:")
print(customers_df)

# Remove duplicates based on CustomerID (keep latest purchase)
clean_customers = customers_df.drop_duplicates(subset=['CustomerID'], keep='last')
print(f"\nClean customer data (latest purchase per customer):")
print(clean_customers)

# =============================================================================
# KEY POINTS TO REMEMBER
# =============================================================================
"""
DUPLICATE HANDLING STRATEGIES:

1. IDENTIFICATION:
   - df.duplicated() - Boolean mask for duplicates
   - df.duplicated().sum() - Count of duplicates

2. REMOVAL METHODS:
   - drop_duplicates() - Remove duplicate rows
   - keep='first' - Keep first occurrence (default)
   - keep='last' - Keep last occurrence  
   - keep=False - Remove all duplicates
   - subset=['col'] - Check duplicates in specific columns

3. BEST PRACTICES:
   - Always check for duplicates before analysis
   - Decide which duplicate to keep based on business logic
   - Consider partial duplicates (same name, different data)
   - Document your duplicate removal strategy
   - Verify results after duplicate removal
"""