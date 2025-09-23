"""
PANDAS FIXING WRONG FORMAT - STUDY NOTES
=========================================

Author: Study Notes
Date: September 2025
Topic: Converting and Fixing Data Types and Formats

OVERVIEW:
---------
- Data often comes in wrong formats (strings instead of dates, etc.)
- pandas provides methods to convert data types
- to_datetime() for date conversions
- astype() for general type conversions
- String methods for text data cleaning
"""

import pandas as pd
import numpy as np

# =============================================================================
# CREATING SAMPLE DATA WITH FORMAT ISSUES
# =============================================================================

print("=== Fixing Wrong Format - Study Examples ===")

# Create sample data with format issues
sample_data = {
    'Date': ['2023-01-01', '2023-01-02', '2023/01/03', 'January 4, 2023', '05-01-2023', '2023-01-06'],
    'Duration': ['60', '45', '30.5', '90', '120', '75'],  # Stored as strings
    'Pulse': [110, 117, 103, 109, 117, 102],
    'Temperature': ['98.6°F', '99.1°F', '97.8°F', '98.2°F', '99.5°F', '98.0°F'],  # With units
    'Active': ['Yes', 'No', 'True', 'False', '1', '0'],  # Mixed boolean formats
    'Price': ['$19.99', '$25.50', '$15.00', '$30.25', '$12.75', '$22.00']  # With currency symbols
}

df = pd.DataFrame(sample_data)
print("Original DataFrame with format issues:")
print(df)
print(f"\nData types:")
print(df.dtypes)

# =============================================================================
# FIXING DATE FORMATS
# =============================================================================

print("\n=== Fixing Date Formats ===")

# Convert Date column to datetime
try:
    df['Date_Fixed'] = pd.to_datetime(df['Date'], format='mixed')
    print("Dates after conversion:")
    print(df[['Date', 'Date_Fixed']])
    print(f"Date column type: {df['Date_Fixed'].dtype}")
except Exception as e:
    print(f"Date conversion error: {e}")
    # Alternative approach - try different formats
    df['Date_Fixed'] = pd.to_datetime(df['Date'], infer_datetime_format=True, errors='coerce')
    print("Dates after conversion (with error handling):")
    print(df[['Date', 'Date_Fixed']])

# =============================================================================
# FIXING NUMERIC FORMATS
# =============================================================================

print("\n=== Fixing Numeric Formats ===")

# Convert Duration from string to numeric
df['Duration_Fixed'] = pd.to_numeric(df['Duration'], errors='coerce')
print("Duration after conversion:")
print(df[['Duration', 'Duration_Fixed']])
print(f"Duration type: {df['Duration'].dtype} -> {df['Duration_Fixed'].dtype}")

# Fix Temperature (remove units and convert)
df['Temperature_Cleaned'] = df['Temperature'].str.replace('°F', '').str.replace('°C', '')
df['Temperature_Fixed'] = pd.to_numeric(df['Temperature_Cleaned'], errors='coerce')
print(f"\nTemperature conversion:")
print(df[['Temperature', 'Temperature_Fixed']])

# Fix Price (remove $ and convert)
df['Price_Cleaned'] = df['Price'].str.replace('$', '').str.replace(',', '')
df['Price_Fixed'] = pd.to_numeric(df['Price_Cleaned'], errors='coerce')
print(f"\nPrice conversion:")
print(df[['Price', 'Price_Fixed']])

# =============================================================================
# FIXING BOOLEAN FORMATS
# =============================================================================

print("\n=== Fixing Boolean Formats ===")

# Create a mapping for boolean conversion
boolean_map = {
    'Yes': True, 'No': False,
    'True': True, 'False': False,
    '1': True, '0': False
}

df['Active_Fixed'] = df['Active'].map(boolean_map)
print("Boolean conversion:")
print(df[['Active', 'Active_Fixed']])

# =============================================================================
# STRING CLEANING AND FORMATTING
# =============================================================================

print("\n=== String Cleaning Examples ===")

# Sample text data with issues
text_data = {
    'Names': ['  John Doe  ', 'JANE SMITH', 'bob johnson', 'Alice_Brown', 'charlie-wilson'],
    'Emails': ['John.Doe@email.com', 'JANE@EMAIL.COM', 'bob@email.com', 'alice@Email.Com', 'charlie@email.COM'],
    'Phone': ['(555) 123-4567', '555.123.4567', '555-123-4567', '5551234567', '+1-555-123-4567']
}

text_df = pd.DataFrame(text_data)
print("Original text data:")
print(text_df)

# Clean Names
text_df['Names_Clean'] = text_df['Names'].str.strip().str.title().str.replace('_', ' ').str.replace('-', ' ')
print(f"\nCleaned Names:")
print(text_df[['Names', 'Names_Clean']])

# Clean Emails  
text_df['Emails_Clean'] = text_df['Emails'].str.lower()
print(f"\nCleaned Emails:")
print(text_df[['Emails', 'Emails_Clean']])

# =============================================================================
# ADVANCED TYPE CONVERSIONS
# =============================================================================

print("\n=== Advanced Type Conversions ===")

# Create DataFrame with mixed types
mixed_data = {
    'ID': ['1', '2', '3', '4', '5'],
    'Score': ['85.5', '92.0', '78.5', '95.0', '88.5'],
    'Grade': ['B', 'A', 'C', 'A', 'B'],
    'Passed': ['True', 'True', 'False', 'True', 'True']
}

mixed_df = pd.DataFrame(mixed_data)
print("Original mixed data:")
print(mixed_df)
print(f"Original dtypes:\n{mixed_df.dtypes}")

# Convert multiple columns at once
conversions = {
    'ID': 'int64',
    'Score': 'float64',
    'Grade': 'category',  # Categorical data
    'Passed': 'bool'
}

# Apply conversions
for col, dtype in conversions.items():
    if dtype == 'bool':
        mixed_df[col] = mixed_df[col].map({'True': True, 'False': False})
    else:
        mixed_df[col] = mixed_df[col].astype(dtype)

print(f"\nAfter type conversions:")
print(mixed_df)
print(f"New dtypes:\n{mixed_df.dtypes}")

# =============================================================================
# ERROR HANDLING IN CONVERSIONS
# =============================================================================

print("\n=== Error Handling in Conversions ===")

# Data with conversion errors
error_data = {
    'Numbers': ['10', '20', 'invalid', '30', 'error', '40'],
    'Dates': ['2023-01-01', '2023-01-02', 'invalid-date', '2023-01-04', '2023-13-01', '2023-01-06']
}

error_df = pd.DataFrame(error_data)
print("Data with errors:")
print(error_df)

# Convert with error handling
error_df['Numbers_Fixed'] = pd.to_numeric(error_df['Numbers'], errors='coerce')  # NaN for errors
error_df['Dates_Fixed'] = pd.to_datetime(error_df['Dates'], errors='coerce')     # NaT for errors

print(f"\nAfter conversion with error handling:")
print(error_df)

# Count conversion errors
print(f"\nConversion errors:")
print(f"Numbers: {error_df['Numbers_Fixed'].isna().sum()} errors")
print(f"Dates: {error_df['Dates_Fixed'].isna().sum()} errors")

# =============================================================================
# KEY POINTS TO REMEMBER
# =============================================================================
"""
DATA FORMAT FIXING STRATEGIES:

1. DATE CONVERSIONS:
   - pd.to_datetime() for date parsing
   - format='mixed' for multiple date formats
   - errors='coerce' to handle invalid dates

2. NUMERIC CONVERSIONS:
   - pd.to_numeric() for string to number
   - Use str.replace() to clean text before conversion
   - Handle currency symbols, units, etc.

3. STRING CLEANING:
   - str.strip() - Remove whitespace
   - str.upper()/str.lower()/str.title() - Case conversion
   - str.replace() - Replace characters/patterns

4. TYPE CONVERSIONS:
   - astype() for general type conversion
   - map() for custom mappings (boolean, categorical)
   - errors='coerce' to handle conversion errors gracefully

5. BEST PRACTICES:
   - Always check data types after loading: df.dtypes
   - Handle errors gracefully with errors='coerce'
   - Clean data before conversion (remove units, symbols)
   - Validate results after conversion
   - Document your format assumptions
"""
