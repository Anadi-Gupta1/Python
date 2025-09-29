"""
PANDAS DATA CLEANING - STUDY NOTES
===================================

Author: Study Notes
Date: September 2025
Topic: Cleaning Empty Cells and Missing Data

OVERVIEW:
---------
- Empty cells can give wrong results in data analysis
- Two main approaches: Remove rows or Replace values
- dropna() removes rows with missing values
- fillna() replaces missing values with specified values
"""

import pandas as pd
import numpy as np

# =============================================================================
# CREATING SAMPLE DATA WITH MISSING VALUES
# =============================================================================

print("=== Data Cleaning - Handling Missing Values ===")

# Create sample data with missing values (NaN)
sample_data = {
    'Duration': [60, 60, np.nan, 45, 45, 60, np.nan, 45, 45, 60],
    'Pulse': [110, 117, 103, np.nan, 117, 102, 110, 104, 109, 98],
    'Maxpulse': [130, 145, 135, 175, np.nan, 127, 136, 134, 133, 124],
    'Calories': [409, 479, np.nan, 282, 406, np.nan, 374, 253, 195, 269]
}

df = pd.DataFrame(sample_data)
print("Original DataFrame with missing values:")
print(df)

# Check missing values
print(f"\nMissing values per column:")
print(df.isnull().sum())

# =============================================================================
# REMOVING ROWS WITH MISSING VALUES
# =============================================================================

print("\n=== Method 1: Remove Rows with Missing Values ===")

# Create new DataFrame without missing values (default behavior)
df_clean = df.dropna()
print("New DataFrame after removing rows with NaN:")
print(df_clean)
print(f"Shape before: {df.shape}, Shape after: {df_clean.shape}")

# Remove missing values from original DataFrame (inplace=True)
print("\n=== Remove from Original DataFrame ===")
df_copy = df.copy()  # Make a copy to demonstrate inplace
print("Before inplace removal:")
print(f"Shape: {df_copy.shape}")

df_copy.dropna(inplace=True)
print("\nAfter inplace removal:")
print(df_copy)
print(f"Shape: {df_copy.shape}")

# =============================================================================
# REPLACING MISSING VALUES
# =============================================================================

print("\n=== Method 2: Replace Missing Values ===")

# Replace with a specific value
df_filled = df.fillna(0)
print("Replace all NaN with 0:")
print(df_filled)

# Replace with different values per column
df_custom_fill = df.copy()
df_custom_fill['Duration'].fillna(50, inplace=True)     # Replace Duration NaN with 50
df_custom_fill['Pulse'].fillna(df['Pulse'].mean(), inplace=True)  # Replace with mean
df_custom_fill['Maxpulse'].fillna(df['Maxpulse'].median(), inplace=True)  # Replace with median
df_custom_fill['Calories'].fillna(df['Calories'].mean(), inplace=True)  # Replace with mean

print("\nCustom replacement (Duration=50, others=mean/median):")
print(df_custom_fill)

# =============================================================================
# ADVANCED REPLACEMENT STRATEGIES
# =============================================================================

print("\n=== Advanced Replacement Strategies ===")

# Replace with specific value for specific column
df_specific = df.copy()
df_specific.fillna({"Calories": 300}, inplace=True)  # Only replace Calories column
print("Replace only Calories column with 300:")
print(df_specific)

# Replace using statistical measures
print("\n=== Statistical Replacements ===")
df_stats = df.copy()

# Calculate statistics
duration_mean = df['Duration'].mean()
pulse_median = df['Pulse'].median() 
maxpulse_mode = df['Maxpulse'].mode()[0] if not df['Maxpulse'].mode().empty else df['Maxpulse'].mean()

print(f"Duration mean: {duration_mean:.2f}")
print(f"Pulse median: {pulse_median:.2f}")
print(f"Maxpulse mode: {maxpulse_mode:.2f}")

# Apply statistical replacements
df_stats['Duration'].fillna(duration_mean, inplace=True)
df_stats['Pulse'].fillna(pulse_median, inplace=True)
df_stats['Maxpulse'].fillna(maxpulse_mode, inplace=True)
df_stats['Calories'].fillna(df['Calories'].mean(), inplace=True)

print("\nDataFrame after statistical replacement:")
print(df_stats)

# =============================================================================
# FORWARD FILL AND BACKWARD FILL
# =============================================================================

print("\n=== Forward Fill and Backward Fill ===")

# Forward fill (use previous value)
df_ffill = df.fillna(method='ffill')
print("Forward fill (use previous value):")
print(df_ffill)

# Backward fill (use next value)
df_bfill = df.fillna(method='bfill')
print("\nBackward fill (use next value):")
print(df_bfill)

# =============================================================================
# KEY POINTS TO REMEMBER
# =============================================================================
"""
DATA CLEANING STRATEGIES:

1. REMOVAL METHODS:
   - dropna() - Remove rows with missing values
   - Use inplace=True to modify original DataFrame

2. REPLACEMENT METHODS:
   - fillna(value) - Replace with specific value
   - fillna(dict) - Replace specific columns
   - Statistical replacement: mean(), median(), mode()
   - Forward fill: method='ffill'
   - Backward fill: method='bfill'

3. BEST PRACTICES:
   - Always check missing values first: df.isnull().sum()
   - Consider the impact of removal vs replacement
   - Statistical measures often work better than fixed values
   - Document your cleaning decisions
"""