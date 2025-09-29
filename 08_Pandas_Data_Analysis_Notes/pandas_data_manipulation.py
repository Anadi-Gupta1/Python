"""
Pandas Data Manipulation - Comprehensive Guide
=============================================

Educational guide to pandas DataFrame operations, data cleaning, merging, grouping, and time series analysis.
Includes practical examples and best practices for data analysis.

Author: Python Learning Notes
Date: September 2025
Topic: Pandas, DataFrame, Data Cleaning, Grouping, Time Series
"""

import pandas as pd
import numpy as np

# =============================================================================
# DATAFRAME CREATION AND BASIC OPERATIONS
# =============================================================================

def dataframe_creation_demo():
    print("\n🗂️ DataFrame Creation Demo")
    data = {
        'Name': ['Alice', 'Bob', 'Carol', 'David'],
        'Age': [25, 30, 22, 35],
        'Score': [88, 92, 79, 85]
    }
    df = pd.DataFrame(data)
    print(df)
    print("Describe:\n", df.describe())

# =============================================================================
# DATA CLEANING
# =============================================================================

def data_cleaning_demo():
    print("\n🧹 Data Cleaning Demo")
    df = pd.DataFrame({
        'A': [1, 2, np.nan, 4],
        'B': ['x', np.nan, 'y', 'z']
    })
    print("Original:\n", df)
    print("Drop NA rows:\n", df.dropna())
    print("Fill NA with 0/empty:\n", df.fillna({'A': 0, 'B': ''}))

# =============================================================================
# MERGING AND GROUPING
# =============================================================================

def merging_grouping_demo():
    print("\n🔗 Merging and Grouping Demo")
    df1 = pd.DataFrame({'ID': [1, 2, 3], 'Score': [88, 92, 79]})
    df2 = pd.DataFrame({'ID': [2, 3, 4], 'Age': [30, 22, 35]})
    merged = pd.merge(df1, df2, on='ID', how='outer')
    print("Merged:\n", merged)
    # Grouping
    df = pd.DataFrame({
        'Team': ['A', 'A', 'B', 'B', 'C'],
        'Points': [10, 15, 20, 25, 30]
    })
    grouped = df.groupby('Team').sum()
    print("Grouped by Team:\n", grouped)

# =============================================================================
# TIME SERIES ANALYSIS
# =============================================================================

def time_series_demo():
    print("\n⏳ Time Series Demo")
    dates = pd.date_range('2025-09-01', periods=5)
    df = pd.DataFrame({'Date': dates, 'Value': np.random.randint(10, 100, 5)})
    df.set_index('Date', inplace=True)
    print(df)
    print("Rolling mean:\n", df['Value'].rolling(window=2).mean())

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    print(__doc__)
    dataframe_creation_demo()
    data_cleaning_demo()
    merging_grouping_demo()
    time_series_demo()

if __name__ == "__main__":
    main()
