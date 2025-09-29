"""
PANDAS REMOVING WRONG DATA - STUDY NOTES
=========================================

Author: Study Notes
Date: September 2025
Topic: Identifying and Handling Wrong/Invalid Data

OVERVIEW:
---------
- Wrong data can be outliers, impossible values, or data entry errors
- Two main approaches: Replace wrong values or Remove rows
- Setting boundaries for valid data ranges
- Using conditions to filter and clean data
"""

import pandas as pd
import numpy as np

# =============================================================================
# CREATING SAMPLE DATA WITH WRONG VALUES
# =============================================================================

print("=== Removing Wrong Data - Study Examples ===")

# Create sample data with intentionally wrong values
sample_data = {
    'Duration': [60, 60, 60, 450, 45, 60, -10, 45, 45, 60, 999, 60],  # 450, -10, 999 are wrong
    'Pulse': [110, 117, 103, 109, 117, 102, 110, 104, 300, 98, 103, 45],  # 300, 45 are wrong
    'Maxpulse': [130, 145, 135, 175, 148, 127, 136, 134, 133, 400, 147, 50],  # 400, 50 are wrong  
    'Calories': [409, 479, 340, 282, 406, 300, 374, 253, 195, -50, 329, 1000]  # -50, 1000 are wrong
}

df = pd.DataFrame(sample_data)
print("Original DataFrame with wrong data:")
print(df)

# =============================================================================
# IDENTIFYING WRONG DATA
# =============================================================================

print("\n=== Identifying Wrong Data ===")

# Basic statistics to identify outliers
print("Basic statistics:")
print(df.describe())

# Set reasonable boundaries for each column
duration_bounds = (10, 120)  # 10-120 minutes reasonable
pulse_bounds = (50, 200)     # 50-200 bpm reasonable
maxpulse_bounds = (60, 250)  # 60-250 bpm reasonable
calories_bounds = (0, 1000)  # 0-1000 calories reasonable

print(f"\nValid ranges:")
print(f"Duration: {duration_bounds[0]}-{duration_bounds[1]} minutes")
print(f"Pulse: {pulse_bounds[0]}-{pulse_bounds[1]} bpm")
print(f"Maxpulse: {maxpulse_bounds[0]}-{maxpulse_bounds[1]} bpm")
print(f"Calories: {calories_bounds[0]}-{calories_bounds[1]} calories")

# Identify wrong data
wrong_duration = (df['Duration'] < duration_bounds[0]) | (df['Duration'] > duration_bounds[1])
wrong_pulse = (df['Pulse'] < pulse_bounds[0]) | (df['Pulse'] > pulse_bounds[1])
wrong_maxpulse = (df['Maxpulse'] < maxpulse_bounds[0]) | (df['Maxpulse'] > maxpulse_bounds[1])
wrong_calories = (df['Calories'] < calories_bounds[0]) | (df['Calories'] > calories_bounds[1])

print(f"\nRows with wrong data:")
print(f"Wrong Duration: {wrong_duration.sum()} rows")
print(f"Wrong Pulse: {wrong_pulse.sum()} rows")  
print(f"Wrong Maxpulse: {wrong_maxpulse.sum()} rows")
print(f"Wrong Calories: {wrong_calories.sum()} rows")

# =============================================================================
# METHOD 1: REPLACING WRONG VALUES
# =============================================================================

print("\n=== Method 1: Replace Wrong Values ===")

df_replace = df.copy()

# Replace with boundary values (capping)
print("Replace with boundary values:")

# Cap Duration values
df_replace.loc[df_replace['Duration'] > duration_bounds[1], 'Duration'] = duration_bounds[1]
df_replace.loc[df_replace['Duration'] < duration_bounds[0], 'Duration'] = duration_bounds[0]

# Cap Pulse values
df_replace.loc[df_replace['Pulse'] > pulse_bounds[1], 'Pulse'] = pulse_bounds[1]
df_replace.loc[df_replace['Pulse'] < pulse_bounds[0], 'Pulse'] = pulse_bounds[0]

print("After capping extreme values:")
print(df_replace)

# Replace with statistical measures
df_stats_replace = df.copy()
print(f"\n=== Replace with Statistical Values ===")

# Replace wrong values with median
duration_median = df[~wrong_duration]['Duration'].median()
pulse_median = df[~wrong_pulse]['Pulse'].median()
maxpulse_median = df[~wrong_maxpulse]['Maxpulse'].median()
calories_median = df[~wrong_calories]['Calories'].median()

df_stats_replace.loc[wrong_duration, 'Duration'] = duration_median
df_stats_replace.loc[wrong_pulse, 'Pulse'] = pulse_median
df_stats_replace.loc[wrong_maxpulse, 'Maxpulse'] = maxpulse_median
df_stats_replace.loc[wrong_calories, 'Calories'] = calories_median

print("After replacing with median values:")
print(df_stats_replace)

# =============================================================================
# METHOD 2: REMOVING ROWS WITH WRONG DATA
# =============================================================================

print("\n=== Method 2: Remove Rows with Wrong Data ===")

df_remove = df.copy()
print(f"Original shape: {df_remove.shape}")

# Method 2a: Remove rows with any wrong values
any_wrong = wrong_duration | wrong_pulse | wrong_maxpulse | wrong_calories
df_remove_any = df[~any_wrong]
print(f"After removing rows with ANY wrong values: {df_remove_any.shape}")
print(df_remove_any)

# Method 2b: Remove rows iteratively
df_iterative = df.copy()
print(f"\n=== Iterative Removal ===")

# Remove rows where Duration is wrong
mask_duration = (df_iterative['Duration'] >= duration_bounds[0]) & (df_iterative['Duration'] <= duration_bounds[1])
df_iterative = df_iterative[mask_duration]
print(f"After removing wrong Duration: {df_iterative.shape}")

# Remove rows where Pulse is wrong  
mask_pulse = (df_iterative['Pulse'] >= pulse_bounds[0]) & (df_iterative['Pulse'] <= pulse_bounds[1])
df_iterative = df_iterative[mask_pulse]
print(f"After removing wrong Pulse: {df_iterative.shape}")

print("Final clean DataFrame:")
print(df_iterative)

# =============================================================================
# ADVANCED TECHNIQUES (Optional - requires scipy)
# =============================================================================

print("\n=== Advanced Wrong Data Detection ===")

try:
    from scipy import stats
    # Calculate z-scores
    z_scores = np.abs(stats.zscore(df.select_dtypes(include=[np.number])))
    threshold = 3  # Values with z-score > 3 are outliers

    outliers = (z_scores > threshold).any(axis=1)
    print(f"Outliers detected using z-score (threshold={threshold}): {outliers.sum()} rows")
    print("Outlier rows:")
    print(df[outliers])
except ImportError:
    print("Scipy not available. Skipping z-score analysis.")

# Using IQR method (built-in pandas)
print(f"\n=== IQR Method for Outlier Detection ===")
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

# Define outliers as values outside Q1-1.5*IQR and Q3+1.5*IQR
outliers_iqr = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)
print(f"Outliers detected using IQR method: {outliers_iqr.sum()} rows")

# =============================================================================
# KEY POINTS TO REMEMBER
# =============================================================================
"""
WRONG DATA HANDLING STRATEGIES:

1. IDENTIFICATION METHODS:
   - Set logical boundaries for each column
   - Use statistical analysis (mean, median, std)
   - Z-score method for outlier detection
   - IQR (Interquartile Range) method
   - Domain knowledge for realistic ranges

2. HANDLING APPROACHES:
   - Replace with boundary values (capping)
   - Replace with statistical measures (mean/median)
   - Remove entire rows with wrong data
   - Replace with interpolated values

3. BEST PRACTICES:
   - Always investigate why data is wrong
   - Document your cleaning decisions
   - Keep a record of original data
   - Validate results after cleaning
   - Consider domain-specific constraints
   - Balance between data quality and quantity
"""



    