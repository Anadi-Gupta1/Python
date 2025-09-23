"""
JSON DATA HANDLING WITH PANDAS - STUDY NOTES
=============================================

Author: Study Notes
Date: September 2025
Topic: Reading and Working with JSON Data

JSON OVERVIEW:
--------------
- JSON = JavaScript Object Notation
- Lightweight data-interchange format
- Human readable and widely used
- Perfect for APIs and web services
- Similar format to Python dictionaries
"""

import pandas as pd

# =============================================================================
# READING JSON FROM FILES
# =============================================================================

print("=== Reading JSON Files ===")

# Basic JSON reading (commented as file may not exist)
"""
df = pd.read_json('data.json')
print(df.to_string())  # Display entire DataFrame
"""

# =============================================================================
# CREATING DATAFRAME FROM DICTIONARY (JSON-LIKE)
# =============================================================================

print("=== DataFrame from Dictionary (JSON format) ===")

# Dictionary with JSON-like structure
json_data = {
    "Duration": {
        "0": 60,
        "1": 60, 
        "2": 60,
        "3": 45,
        "4": 45,
        "5": 60
    },
    "Pulse": {
        "0": 110,
        "1": 117,
        "2": 103,
        "3": 109,
        "4": 117,
        "5": 102
    },
    "Maxpulse": {
        "0": 130,
        "1": 145,
        "2": 135,
        "3": 175,
        "4": 148,
        "5": 127
    },
    "Calories": {
        "0": 409,
        "1": 479,
        "2": 340,
        "3": 282,
        "4": 406,
        "5": 300
    }
}

# Create DataFrame from dictionary
df_from_dict = pd.DataFrame(json_data)
print("DataFrame from JSON-like dictionary:")
print(df_from_dict)

# =============================================================================
# KEY POINTS TO REMEMBER:
# =============================================================================
"""
IMPORTANT CONCEPTS:
1. pd.read_json() reads JSON files into DataFrames
2. JSON and Python dictionaries have similar structure
3. Use .to_json() to save DataFrames to JSON format
4. JSON is ideal for web APIs and data exchange
""" 