"""
Pandas DataFrames - Complete Mastery Guide for Tabular Data
========================================================

Comprehensive guide to Pandas DataFrames covering creation, manipulation,
indexing, operations, and advanced techniques for mastering two-dimensional
labeled data structures essential for data analysis and manipulation.

Author: Python Learning Notes
Date: September 2025
Topic: DataFrames, Tabular Data, Data Manipulation, Analysis Fundamentals
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Any, List, Dict, Union, Optional, Tuple
import datetime
from io import StringIO
import warnings

# =============================================================================
# DATAFRAME FUNDAMENTALS AND ARCHITECTURE
# =============================================================================

def dataframe_fundamentals():
    """
    Complete introduction to DataFrames and their architecture
    """
    print("📋 PANDAS DATAFRAMES FUNDAMENTALS")
    print("=" * 35)
    
    print("🎯 What is a DataFrame?")
    print("   A DataFrame is a 2-dimensional labeled data structure with columns")
    print("   that can be of different types. Think of it as:")
    print("   • Excel spreadsheet or SQL table")
    print("   • Collection of Series with shared index")
    print("   • Primary data structure for data analysis")
    
    print(f"\n🏗️  DataFrame Architecture:")
    print("   ┌─────────────┬─────────────┬─────────────┬─────────────┐")
    print("   │             │   Column 1  │   Column 2  │   Column 3  │  ← Column Names")
    print("   │             │    (Series) │    (Series) │    (Series) │")
    print("   ├─────────────┼─────────────┼─────────────┼─────────────┤")
    print("   │  Index 0    │    Value    │    Value    │    Value    │  ← Row (Index + Data)")
    print("   │  Index 1    │    Value    │    Value    │    Value    │")
    print("   │  Index 2    │    Value    │    Value    │    Value    │")
    print("   └─────────────┴─────────────┴─────────────┴─────────────┘")
    print("     ↑")
    print("   Row Index")
    
    print(f"\n📊 Key DataFrame Characteristics:")
    characteristics = {
        "Two-Dimensional": "Rows and columns like a spreadsheet",
        "Heterogeneous Data": "Different columns can have different data types",
        "Labeled Axes": "Both rows (index) and columns have labels",
        "Size Mutable": "Can add/remove rows and columns",
        "Data Alignment": "Automatic alignment by index and column labels",
        "Integrated Statistics": "Built-in statistical and analytical methods"
    }
    
    for characteristic, description in characteristics.items():
        print(f"   • {characteristic}: {description}")

def dataframe_vs_other_structures():
    """
    Compare DataFrames with other data structures
    """
    print("\n⚖️  DATAFRAMES VS OTHER DATA STRUCTURES")
    print("=" * 41)
    
    comparisons = [
        {
            "structure": "Python List of Lists",
            "example": "[[1, 'A'], [2, 'B']]",
            "advantages": ["Simple", "Built-in"],
            "disadvantages": ["No labels", "No data alignment", "Limited operations"]
        },
        {
            "structure": "NumPy 2D Array", 
            "example": "np.array([[1, 2], [3, 4]])",
            "advantages": ["Fast", "Memory efficient"],
            "disadvantages": ["No labels", "Homogeneous data only", "Limited data analysis tools"]
        },
        {
            "structure": "Dictionary of Lists",
            "example": "{'col1': [1, 2], 'col2': ['A', 'B']}",
            "advantages": ["Column labels", "Heterogeneous data"],
            "disadvantages": ["No row labels", "Manual data alignment", "Limited operations"]
        },
        {
            "structure": "Pandas DataFrame",
            "example": "pd.DataFrame({'col1': [1, 2], 'col2': ['A', 'B']})",
            "advantages": ["Row & column labels", "Data alignment", "Rich operations", "Statistical methods"],
            "disadvantages": ["Memory overhead", "Learning curve"]
        }
    ]
    
    print("📊 Comparison Table:")
    print("   ┌──────────────────────┬─────────────────────────┬──────────────────────────┐")
    print("   │ Data Structure       │ Advantages              │ Disadvantages            │")
    print("   ├──────────────────────┼─────────────────────────┼──────────────────────────┤")
    
    for comp in comparisons:
        advantages_str = ", ".join(comp["advantages"])[:23]
        disadvantages_str = ", ".join(comp["disadvantages"])[:24]
        print(f"   │ {comp['structure']:<20} │ {advantages_str:<23} │ {disadvantages_str:<24} │")
    
    print("   └──────────────────────┴─────────────────────────┴──────────────────────────┘")

# =============================================================================
# COMPREHENSIVE DATAFRAME CREATION METHODS
# =============================================================================

def comprehensive_dataframe_creation():
    """
    Complete guide to all DataFrame creation methods
    """
    print("\n🏗️  DATAFRAME CREATION - COMPLETE METHODS GUIDE")
    print("=" * 50)
    
    creation_examples = {}
    
    # Method 1: From Dictionary of Lists/Arrays
    print("📝 Method 1: From Dictionary of Lists")
    
    employee_data = {
        'Name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'Diana Prince'],
        'Age': [28, 34, 29, 31],
        'Department': ['Engineering', 'Marketing', 'Engineering', 'Sales'],
        'Salary': [85000, 72000, 88000, 79000],
        'Years_Experience': [5, 8, 6, 7]
    }
    
    df_from_dict = pd.DataFrame(employee_data)
    creation_examples['from_dictionary'] = df_from_dict
    
    print("   Dictionary to DataFrame:")
    print(df_from_dict)
    print(f"   Shape: {df_from_dict.shape}")
    
    # Method 2: From List of Dictionaries
    print(f"\n📝 Method 2: From List of Dictionaries")
    
    product_records = [
        {'Product': 'Laptop', 'Price': 1200, 'Category': 'Electronics', 'In_Stock': True},
        {'Product': 'Desk Chair', 'Price': 350, 'Category': 'Furniture', 'In_Stock': False},
        {'Product': 'Monitor', 'Price': 400, 'Category': 'Electronics', 'In_Stock': True},
        {'Product': 'Coffee Maker', 'Price': 150, 'Category': 'Appliance', 'In_Stock': True}
    ]
    
    df_from_records = pd.DataFrame(product_records)
    creation_examples['from_records'] = df_from_records
    
    print("   List of dictionaries to DataFrame:")
    print(df_from_records)
    
    # Method 3: From NumPy Arrays
    print(f"\n📝 Method 3: From NumPy Arrays")
    
    np.random.seed(42)
    numerical_data = np.random.randn(5, 4)
    
    df_from_numpy = pd.DataFrame(
        numerical_data,
        columns=['Feature_A', 'Feature_B', 'Feature_C', 'Feature_D'],
        index=[f'Sample_{i+1}' for i in range(5)]
    )
    creation_examples['from_numpy'] = df_from_numpy
    
    print("   NumPy array to DataFrame:")
    print(df_from_numpy.round(3))
    
    # Method 4: From Series
    print(f"\n📝 Method 4: From Multiple Series")
    
    dates = pd.date_range('2024-01-01', periods=6, freq='D')
    temperatures = pd.Series([22.5, 24.1, 21.8, 23.9, 25.2, 20.7], index=dates, name='Temperature')
    humidity = pd.Series([65, 70, 68, 72, 75, 63], index=dates, name='Humidity') 
    pressure = pd.Series([1013, 1015, 1012, 1016, 1018, 1010], index=dates, name='Pressure')
    
    df_from_series = pd.DataFrame({'Temperature': temperatures, 'Humidity': humidity, 'Pressure': pressure})
    creation_examples['from_series'] = df_from_series
    
    print("   Multiple Series to DataFrame:")
    print(df_from_series.head(3))
    
    # Method 5: From CSV String (simulated)
    print(f"\n📝 Method 5: From CSV Data")
    
    csv_data = """Name,Age,City,Score
    John,25,New York,85
    Jane,30,Los Angeles,92
    Mike,28,Chicago,78
    Sarah,26,Houston,88"""
    
    df_from_csv = pd.read_csv(StringIO(csv_data))
    creation_examples['from_csv'] = df_from_csv
    
    print("   CSV string to DataFrame:")
    print(df_from_csv)
    
    # Method 6: Empty DataFrame with Structure
    print(f"\n📝 Method 6: Empty DataFrame with Predefined Structure")
    
    df_empty = pd.DataFrame(
        columns=['Transaction_ID', 'Amount', 'Date', 'Category', 'Description'],
        index=range(3)
    )
    creation_examples['empty_structure'] = df_empty
    
    print("   Empty DataFrame with structure:")
    print(df_empty)
    print(f"   Data types: {df_empty.dtypes.tolist()}")
    
    return creation_examples

def dataframe_properties_and_attributes():
    """
    Comprehensive exploration of DataFrame properties and attributes
    """
    print("\n🔍 DATAFRAME PROPERTIES AND ATTRIBUTES")
    print("=" * 40)
    
    # Create comprehensive sample DataFrame
    np.random.seed(42)
    sample_df = pd.DataFrame({
        'Product_ID': range(1001, 1021),
        'Product_Name': [f'Product_{i}' for i in range(1, 21)],
        'Category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home'], 20),
        'Price': np.random.uniform(10, 500, 20).round(2),
        'Quantity': np.random.randint(1, 100, 20),
        'Rating': np.random.uniform(1, 5, 20).round(1),
        'Launch_Date': pd.date_range('2023-01-01', periods=20, freq='2W'),
        'Is_Active': np.random.choice([True, False], 20, p=[0.8, 0.2])
    })
    
    print("📊 Sample E-commerce DataFrame:")
    print(sample_df.head())
    
    print(f"\n🔍 Essential Properties:")
    
    properties = [
        ('Shape', sample_df.shape, 'Dimensions (rows, columns)'),
        ('Size', sample_df.size, 'Total number of elements'),
        ('Memory Usage', f"{sample_df.memory_usage(deep=True).sum() / 1024:.1f} KB", 'Memory consumption'),
        ('Column Count', len(sample_df.columns), 'Number of columns'),
        ('Row Count', len(sample_df.index), 'Number of rows'),
        ('Data Types Count', sample_df.dtypes.value_counts().to_dict(), 'Distribution of data types')
    ]
    
    for prop_name, value, description in properties:
        print(f"   • {prop_name:<15}: {value}")
        print(f"     {description}")
    
    print(f"\n📋 Column Information:")
    print("   ┌─────────────────┬──────────────┬─────────────┬──────────────────┐")
    print("   │ Column          │ Data Type    │ Non-Null    │ Memory Usage     │")
    print("   ├─────────────────┼──────────────┼─────────────┼──────────────────┤")
    
    for col in sample_df.columns:
        dtype = str(sample_df[col].dtype)
        non_null = sample_df[col].count()
        memory = sample_df[col].memory_usage(deep=True)
        print(f"   │ {col:<15} │ {dtype:<12} │ {non_null:<11} │ {memory:<16} │")
    
    print("   └─────────────────┴──────────────┴─────────────┴──────────────────┘")
    
    # Statistical summary
    print(f"\n📈 Statistical Summary:")
    numeric_cols = sample_df.select_dtypes(include=[np.number]).columns
    print(f"   Numerical columns: {list(numeric_cols)}")
    print(sample_df[numeric_cols].describe().round(2))
    
    return sample_df

# =============================================================================
# INDEXING AND SELECTION MASTERY
# =============================================================================

def dataframe_indexing_mastery():
    """
    Complete guide to DataFrame indexing and selection methods
    """
    print("\n🎯 DATAFRAME INDEXING AND SELECTION MASTERY")
    print("=" * 45)
    
    # Create sample DataFrame for demonstrations
    sales_data = pd.DataFrame({
        'Date': pd.date_range('2024-01-01', periods=10, freq='D'),
        'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South'],
        'Salesperson': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
        'Product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Tablet', 'Laptop'],
        'Units_Sold': [5, 8, 3, 7, 6, 4, 9, 5, 2, 8],
        'Revenue': [6000, 4800, 1200, 8400, 3600, 1600, 10800, 3000, 800, 9600]
    })
    
    print("📊 Sample Sales DataFrame:")
    print(sales_data)
    
    # Column selection methods
    print(f"\n🔍 Column Selection Methods:")
    
    selection_methods = [
        {
            "method": "Single Column (Series)",
            "code": "df['Region']",
            "result": sales_data['Region'].head(3),
            "returns": "Series"
        },
        {
            "method": "Multiple Columns (DataFrame)",
            "code": "df[['Region', 'Revenue']]",
            "result": sales_data[['Region', 'Revenue']].head(3),
            "returns": "DataFrame"
        },
        {
            "method": "Dot notation",
            "code": "df.Salesperson",
            "result": sales_data.Salesperson.head(3),
            "returns": "Series"
        }
    ]
    
    for method_info in selection_methods:
        print(f"\n   📌 {method_info['method']}:")
        print(f"   Code: {method_info['code']}")
        print(f"   Returns: {method_info['returns']}")
        print(f"   Result:")
        print(str(method_info['result']).replace('\n', '\n   '))
    
    # Row selection methods
    print(f"\n🔍 Row Selection Methods:")
    
    row_selection_methods = [
        {
            "method": "iloc - Position-based",
            "code": "df.iloc[0:3]",
            "result": sales_data.iloc[0:3],
            "description": "Select rows by position"
        },
        {
            "method": "loc - Label-based", 
            "code": "df.loc[0:2]",
            "result": sales_data.loc[0:2],
            "description": "Select rows by index label"
        },
        {
            "method": "Boolean indexing",
            "code": "df[df['Revenue'] > 5000]",
            "result": sales_data[sales_data['Revenue'] > 5000],
            "description": "Select rows meeting condition"
        },
        {
            "method": "Query method",
            "code": "df.query('Units_Sold > 6')",
            "result": sales_data.query('Units_Sold > 6'),
            "description": "SQL-like conditional selection"
        }
    ]
    
    for method_info in row_selection_methods:
        print(f"\n   📌 {method_info['method']}:")
        print(f"   Code: {method_info['code']}")
        print(f"   Description: {method_info['description']}")
        print(f"   Result: {len(method_info['result'])} rows selected")
        if len(method_info['result']) <= 3:
            print(str(method_info['result']).replace('\n', '\n   '))
    
    # Advanced selection combinations
    print(f"\n🚀 Advanced Selection Combinations:")
    
    advanced_examples = [
        {
            "description": "Specific rows and columns",
            "code": "df.loc[df['Product'] == 'Laptop', ['Salesperson', 'Revenue']]",
            "result": sales_data.loc[sales_data['Product'] == 'Laptop', ['Salesperson', 'Revenue']]
        },
        {
            "description": "Top N values",
            "code": "df.nlargest(3, 'Revenue')",
            "result": sales_data.nlargest(3, 'Revenue')[['Salesperson', 'Product', 'Revenue']]
        },
        {
            "description": "Multiple conditions",
            "code": "df[(df['Region'] == 'North') & (df['Revenue'] > 3000)]", 
            "result": sales_data[(sales_data['Region'] == 'North') & (sales_data['Revenue'] > 3000)]
        }
    ]
    
    for example in advanced_examples:
        print(f"\n   🎯 {example['description']}:")
        print(f"   Code: {example['code']}")
        print(f"   Result:")
        print(str(example['result']).replace('\n', '\n   '))
    
    return sales_data

# =============================================================================
# DATAFRAME OPERATIONS AND MANIPULATIONS
# =============================================================================

def dataframe_operations_comprehensive():
    """
    Comprehensive guide to DataFrame operations and manipulations
    """
    print("\n⚙️  DATAFRAME OPERATIONS - COMPREHENSIVE GUIDE")
    print("=" * 48)
    
    # Create sample data for operations
    np.random.seed(42)
    operations_df = pd.DataFrame({
        'Store_ID': ['S001', 'S002', 'S003', 'S004', 'S005'],
        'Store_Name': ['Downtown', 'Mall Plaza', 'Suburb Center', 'City Square', 'Market Street'],
        'Manager': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'Daily_Sales': [15000, 22000, 18000, 25000, 19000],
        'Employees': [15, 25, 20, 30, 22],
        'Area_SqFt': [2500, 4000, 3200, 5000, 3500],
        'Opening_Year': [2018, 2015, 2020, 2012, 2017],
        'Has_Parking': [True, True, False, True, True]
    })
    
    print("📊 Sample Store Data:")
    print(operations_df)
    
    # Adding new columns
    print(f"\n➕ Adding New Columns:")
    
    # Simple calculation
    operations_df['Sales_Per_Employee'] = operations_df['Daily_Sales'] / operations_df['Employees']
    print(f"   Added calculated column 'Sales_Per_Employee':")
    print(f"   {operations_df[['Store_Name', 'Sales_Per_Employee']].round(0)}")
    
    # Conditional column
    operations_df['Performance_Category'] = operations_df['Daily_Sales'].apply(
        lambda x: 'High' if x > 20000 else ('Medium' if x > 17000 else 'Low')
    )
    print(f"\n   Added categorical column 'Performance_Category':")
    print(f"   {operations_df[['Store_Name', 'Daily_Sales', 'Performance_Category']]}")
    
    # Date-based column
    operations_df['Store_Age'] = 2024 - operations_df['Opening_Year']
    
    # Modifying existing columns
    print(f"\n🔄 Modifying Existing Columns:")
    
    # Update values conditionally
    operations_df.loc[operations_df['Store_Age'] > 10, 'Status'] = 'Established'
    operations_df.loc[operations_df['Store_Age'] <= 10, 'Status'] = 'New'
    
    print(f"   Added 'Status' based on store age:")
    print(f"   {operations_df[['Store_Name', 'Store_Age', 'Status']]}")
    
    # Sorting operations
    print(f"\n🔀 Sorting Operations:")
    
    # Sort by single column
    sorted_by_sales = operations_df.sort_values('Daily_Sales', ascending=False)
    print(f"   Stores sorted by Daily_Sales (descending):")
    print(f"   {sorted_by_sales[['Store_Name', 'Daily_Sales']].head(3)}")
    
    # Sort by multiple columns
    multi_sort = operations_df.sort_values(['Performance_Category', 'Daily_Sales'], 
                                         ascending=[True, False])
    print(f"\n   Multi-column sort (Performance_Category asc, Daily_Sales desc):")
    print(f"   {multi_sort[['Store_Name', 'Performance_Category', 'Daily_Sales']]}")
    
    # Grouping and aggregation
    print(f"\n📊 Grouping and Aggregation:")
    
    # Group by categorical variable
    performance_stats = operations_df.groupby('Performance_Category').agg({
        'Daily_Sales': ['mean', 'sum', 'count'],
        'Employees': ['mean', 'sum'],
        'Area_SqFt': 'mean'
    }).round(0)
    
    print(f"   Statistics by Performance Category:")
    print(performance_stats)
    
    # Filtering operations
    print(f"\n🎯 Advanced Filtering:")
    
    # Multiple condition filtering
    high_performing_stores = operations_df[
        (operations_df['Daily_Sales'] > 20000) & 
        (operations_df['Has_Parking'] == True) &
        (operations_df['Employees'] > 20)
    ]
    
    print(f"   High-performing stores with parking and >20 employees:")
    print(f"   {high_performing_stores[['Store_Name', 'Daily_Sales', 'Employees']]}")
    
    # String operations
    print(f"\n📝 String Operations on Text Columns:")
    
    operations_df['Store_Name_Upper'] = operations_df['Store_Name'].str.upper()
    operations_df['Name_Length'] = operations_df['Store_Name'].str.len()
    operations_df['Contains_Center'] = operations_df['Store_Name'].str.contains('Center')
    
    print(f"   String manipulations:")
    print(f"   {operations_df[['Store_Name', 'Store_Name_Upper', 'Name_Length', 'Contains_Center']]}")
    
    return operations_df

def dataframe_statistical_analysis():
    """
    Statistical analysis capabilities of DataFrames
    """
    print("\n📈 DATAFRAME STATISTICAL ANALYSIS")
    print("=" * 35)
    
    # Generate sample dataset for analysis
    np.random.seed(42)
    n_samples = 100
    
    analysis_df = pd.DataFrame({
        'Customer_Age': np.random.normal(40, 12, n_samples).round().astype(int),
        'Income': np.random.normal(60000, 15000, n_samples).round().astype(int),
        'Purchase_Amount': np.random.exponential(200, n_samples).round(2),
        'Satisfaction_Score': np.random.uniform(1, 5, n_samples).round(1),
        'Days_Since_Last_Purchase': np.random.poisson(30, n_samples),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], n_samples),
        'Customer_Type': np.random.choice(['New', 'Returning', 'VIP'], n_samples, p=[0.3, 0.6, 0.1])
    })
    
    print("📊 Customer Analytics Dataset (100 samples):")
    print(analysis_df.head())
    
    # Basic statistics
    print(f"\n📊 Basic Statistical Summary:")
    numeric_stats = analysis_df.describe()
    print(numeric_stats.round(2))
    
    # Correlation analysis
    print(f"\n🔗 Correlation Analysis:")
    numeric_cols = ['Customer_Age', 'Income', 'Purchase_Amount', 'Satisfaction_Score']
    correlation_matrix = analysis_df[numeric_cols].corr()
    print(correlation_matrix.round(3))
    
    # Group statistics
    print(f"\n👥 Group Statistics by Customer Type:")
    group_stats = analysis_df.groupby('Customer_Type').agg({
        'Purchase_Amount': ['count', 'mean', 'std'],
        'Satisfaction_Score': ['mean', 'min', 'max'],
        'Income': 'mean'
    }).round(2)
    
    print(group_stats)
    
    # Cross-tabulation
    print(f"\n📊 Cross-tabulation: Customer Type vs Region:")
    crosstab = pd.crosstab(analysis_df['Customer_Type'], analysis_df['Region'], margins=True)
    print(crosstab)
    
    # Percentile analysis
    print(f"\n📊 Percentile Analysis for Purchase Amount:")
    percentiles = [10, 25, 50, 75, 90, 95, 99]
    percentile_values = analysis_df['Purchase_Amount'].quantile([p/100 for p in percentiles])
    
    for p, value in zip(percentiles, percentile_values):
        print(f"   {p:2d}th percentile: ${value:7.2f}")
    
    return analysis_df

# =============================================================================
# ADVANCED DATAFRAME TECHNIQUES
# =============================================================================

def advanced_dataframe_techniques():
    """
    Advanced DataFrame techniques and operations
    """
    print("\n🚀 ADVANCED DATAFRAME TECHNIQUES")
    print("=" * 35)
    
    # Create sample data for advanced operations
    sales_df = pd.DataFrame({
        'Date': pd.date_range('2024-01-01', periods=90, freq='D'),
        'Product': np.random.choice(['A', 'B', 'C'], 90),
        'Sales': np.random.poisson(50, 90),
        'Price': np.random.uniform(10, 100, 90).round(2),
        'Promotion': np.random.choice([True, False], 90, p=[0.3, 0.7])
    })
    
    sales_df['Revenue'] = sales_df['Sales'] * sales_df['Price']
    sales_df['Month'] = sales_df['Date'].dt.month
    sales_df['Weekday'] = sales_df['Date'].dt.day_name()
    
    print("📊 Sample Sales Data (90 days):")
    print(sales_df.head())
    
    # Pivot Tables
    print(f"\n🔄 Pivot Table Analysis:")
    
    pivot_table = sales_df.pivot_table(
        values='Revenue',
        index='Product',
        columns='Month',
        aggfunc=['sum', 'mean', 'count'],
        fill_value=0
    )
    
    print(f"   Revenue pivot by Product and Month:")
    print(pivot_table.round(0))
    
    # Rolling operations  
    print(f"\n📈 Rolling Window Analysis:")
    
    # Sort by date for time series operations
    sales_df_sorted = sales_df.sort_values('Date').set_index('Date')
    
    # Calculate rolling statistics
    sales_df_sorted['Revenue_MA_7'] = sales_df_sorted['Revenue'].rolling(7).mean()
    sales_df_sorted['Revenue_MA_30'] = sales_df_sorted['Revenue'].rolling(30).mean()
    sales_df_sorted['Revenue_Std_7'] = sales_df_sorted['Revenue'].rolling(7).std()
    
    print(f"   Sample rolling analysis (last 5 days):")
    rolling_sample = sales_df_sorted[['Revenue', 'Revenue_MA_7', 'Revenue_MA_30']].tail()
    print(rolling_sample.round(2))
    
    # Resampling and time-based aggregation
    print(f"\n📅 Time-based Aggregation:")
    
    weekly_stats = sales_df_sorted.resample('W').agg({
        'Sales': 'sum',
        'Revenue': ['sum', 'mean'],
        'Promotion': 'sum'
    })
    
    print(f"   Weekly aggregation (first 4 weeks):")
    print(weekly_stats.head(4).round(0))
    
    # Advanced filtering with query
    print(f"\n🎯 Advanced Query Operations:")
    
    # Complex queries
    complex_query = sales_df.query(
        'Revenue > @sales_df.Revenue.quantile(0.75) and Promotion == True'
    )
    
    print(f"   High-revenue promotional sales (top 25% revenue + promotion):")
    print(f"   Found {len(complex_query)} records out of {len(sales_df)}")
    print(complex_query[['Date', 'Product', 'Revenue', 'Promotion']].head(3))
    
    # Transform operations
    print(f"\n🔄 Transform Operations:")
    
    # Rank within groups
    sales_df['Revenue_Rank_by_Product'] = sales_df.groupby('Product')['Revenue'].rank(
        method='dense', ascending=False
    )
    
    # Normalize within groups
    sales_df['Revenue_Normalized'] = sales_df.groupby('Product')['Revenue'].transform(
        lambda x: (x - x.mean()) / x.std()
    )
    
    print(f"   Transform examples:")
    sample_transform = sales_df[['Product', 'Revenue', 'Revenue_Rank_by_Product', 'Revenue_Normalized']].head()
    print(sample_transform.round(3))
    
    return sales_df

# =============================================================================
# MAIN EXECUTION AND COMPREHENSIVE DEMONSTRATION
# =============================================================================

def main():
    """
    Main function executing comprehensive DataFrame guide
    """
    print(__doc__)
    
    # Fundamentals and concepts
    dataframe_fundamentals()
    dataframe_vs_other_structures()
    
    # Creation and properties
    creation_examples = comprehensive_dataframe_creation()
    sample_df = dataframe_properties_and_attributes()
    
    # Indexing and selection
    sales_data = dataframe_indexing_mastery()
    
    # Operations and analysis
    operations_df = dataframe_operations_comprehensive()
    analysis_df = dataframe_statistical_analysis()
    
    # Advanced techniques
    advanced_df = advanced_dataframe_techniques()
    
    return {
        'creation_examples': creation_examples,
        'sample_properties': sample_df,
        'sales_data': sales_data,
        'operations_data': operations_df,
        'analysis_data': analysis_df,
        'advanced_data': advanced_df
    }

if __name__ == "__main__":
    """
    Execute comprehensive Pandas DataFrame guide and demonstrations
    """
    dataframe_examples = main()
    
    print("\n" + "=" * 60)
    print("🎓 PANDAS DATAFRAME MASTERY SUMMARY")
    print("=" * 60)
    print("✅ DataFrame fundamentals and architecture mastered")
    print("✅ Comprehensive creation methods from all sources")
    print("✅ Properties, attributes, and metadata understanding")
    print("✅ Advanced indexing and selection techniques")
    print("✅ Complete operations and manipulation methods")
    print("✅ Statistical analysis and aggregation capabilities")
    print("✅ Advanced techniques for complex data workflows")
    print("✅ Real-world applications and best practices")
    
    print("\n💡 DataFrame Mastery Key Points:")
    mastery_points = [
        "DataFrames = Labeled 2D structures for tabular data",
        "Multiple creation methods for different data sources",
        "Powerful indexing with loc, iloc, and boolean selection",
        "Rich operations for data manipulation and analysis",
        "Built-in statistical functions and aggregations",
        "Time series and grouping capabilities",
        "Integration with visualization and ML libraries",
        "Performance optimization for large datasets"
    ]
    
    for point in mastery_points:
        print(f"   • {point}")
    
    print("\n🎯 Advanced DataFrame Skills Achieved:")
    skills = [
        "Create DataFrames from any data source efficiently",
        "Master all indexing and selection patterns",
        "Perform complex data manipulations and transformations",
        "Execute statistical analysis and aggregations",
        "Handle time series and categorical data",
        "Optimize performance for large datasets",
        "Build complete data analysis workflows",
        "Integrate with the broader Python data ecosystem"
    ]
    
    for i, skill in enumerate(skills, 1):
        print(f"   {i}. {skill}")
    
    print(f"\n🚀 DataFrame Mastery Complete!")
    print("You now possess comprehensive DataFrame knowledge and skills")
    print("Ready to handle any tabular data analysis challenge!")
    
    # Provide access to examples
    print(f"\n📊 Available Examples for Further Exploration:")
    for key, value in dataframe_examples.items():
        if isinstance(value, pd.DataFrame):
            print(f"   • {key}: DataFrame {value.shape} - {value.columns.tolist()[:3]}...")
        elif isinstance(value, dict):
            print(f"   • {key}: {len(value)} DataFrame examples")
    
    print(f"\n🎯 Next Steps: Continue with advanced Pandas topics")
    print("   • Data cleaning and preprocessing")
    print("   • Merging and joining datasets") 
    print("   • Time series analysis")
    print("   • Performance optimization") 