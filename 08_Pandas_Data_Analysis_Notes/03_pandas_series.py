"""
Pandas Series - Complete Guide to One-Dimensional Data Structures
===============================================================

Comprehensive guide to Pandas Series covering creation methods, indexing,
operations, methods, data types, and advanced techniques for mastering
one-dimensional labeled data structures in Python data analysis.

Author: Python Learning Notes
Date: September 2025
Topic: Pandas Series, Data Structures, Indexing, Data Analysis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Any, List, Dict, Union, Optional
import datetime
import warnings

# =============================================================================
# UNDERSTANDING PANDAS SERIES FUNDAMENTALS
# =============================================================================

def series_fundamentals():
    """
    Complete introduction to what a Pandas Series is and its core concepts
    """
    print("📊 PANDAS SERIES FUNDAMENTALS")
    print("=" * 31)
    
    print("🎯 What is a Pandas Series?")
    print("   A Series is a one-dimensional labeled array capable of holding")
    print("   any data type (integers, strings, floats, Python objects, etc.)")
    
    print(f"\n🏗️  Series Architecture:")
    print("   ┌─────────────┐")
    print("   │    Index    │  ←  Labels/Keys (like row names)")
    print("   │   (Labels)  │")  
    print("   ├─────────────┤")
    print("   │    Data     │  ←  Actual values")
    print("   │  (Values)   │")
    print("   └─────────────┘")
    
    print(f"\n🔍 Series vs Other Data Structures:")
    
    comparisons = [
        ("Python List", "No labels, position-based access only", "[1, 2, 3]"),
        ("NumPy Array", "No labels, homogeneous data types", "array([1, 2, 3])"),
        ("Dictionary", "Key-value pairs, not optimized for analysis", "{'a': 1, 'b': 2}"),
        ("Pandas Series", "Labeled + optimized for data analysis", "Series([1, 2, 3], index=['a', 'b', 'c'])")
    ]
    
    print("   ┌─────────────────┬───────────────────────────────┬─────────────────────────┐")
    print("   │ Structure       │ Characteristics               │ Example                 │")
    print("   ├─────────────────┼───────────────────────────────┼─────────────────────────┤")
    for structure, char, example in comparisons:
        print(f"   │ {structure:<15} │ {char:<29} │ {example:<23} │")
    print("   └─────────────────┴───────────────────────────────┴─────────────────────────┘")

def series_anatomy_deep_dive():
    """
    Deep dive into Series components and properties
    """
    print("\n🔬 SERIES ANATOMY - DEEP DIVE")
    print("=" * 32)
    
    # Create a comprehensive example Series
    sample_series = pd.Series(
        data=[85, 92, 78, 96, 89],
        index=['Math', 'Physics', 'Chemistry', 'Biology', 'English'],
        name='Test_Scores',
        dtype='int64'
    )
    
    print("📋 Example Series:")
    print(sample_series)
    
    print(f"\n🔍 Series Components:")
    components = [
        ('Values/Data', sample_series.values, 'The actual data array'),
        ('Index', sample_series.index, 'Labels for each data point'),
        ('Name', sample_series.name, 'Optional identifier for the Series'),
        ('Data Type', sample_series.dtype, 'Type of data stored'),
        ('Shape', sample_series.shape, 'Dimensions of the Series'),
        ('Size', sample_series.size, 'Number of elements'),
        ('Memory Usage', f"{sample_series.memory_usage()} bytes", 'Memory consumption')
    ]
    
    for component, value, description in components:
        print(f"   • {component:<12}: {value}")
        print(f"     {description}")
    
    return sample_series

# =============================================================================
# SERIES CREATION METHODS - COMPREHENSIVE GUIDE
# =============================================================================

def comprehensive_series_creation():
    """
    Complete guide to all Series creation methods
    """
    print("\n🏗️  SERIES CREATION METHODS - COMPLETE GUIDE")
    print("=" * 46)
    
    creation_methods = {}
    
    # Method 1: From Python Lists
    print("📝 Method 1: From Python Lists")
    list_series = pd.Series([10, 20, 30, 40, 50])
    creation_methods['from_list'] = list_series
    
    print("   Basic creation:")
    print(f"   pd.Series([10, 20, 30, 40, 50])")
    print(f"   Result: {list(list_series)}")
    
    # Method 2: From Lists with Custom Index
    custom_index_series = pd.Series([10, 20, 30], index=['A', 'B', 'C'])
    creation_methods['custom_index'] = custom_index_series
    
    print(f"\n   With custom index:")
    print(f"   pd.Series([10, 20, 30], index=['A', 'B', 'C'])")
    print(f"   Result:\n{custom_index_series}")
    
    # Method 3: From Dictionary
    print(f"\n📝 Method 3: From Dictionary")
    dict_data = {'Monday': 100, 'Tuesday': 120, 'Wednesday': 90, 'Thursday': 110}
    dict_series = pd.Series(dict_data)
    creation_methods['from_dict'] = dict_series
    
    print("   Dictionary to Series:")
    print(f"   data = {dict_data}")
    print(f"   pd.Series(data)")
    print(f"   Result:\n{dict_series}")
    
    # Method 4: From NumPy Arrays
    print(f"\n📝 Method 4: From NumPy Arrays")
    np_array = np.random.randn(5)
    np_series = pd.Series(np_array, index=[f'Point_{i}' for i in range(1, 6)])
    creation_methods['from_numpy'] = np_series
    
    print("   NumPy array to Series:")
    print(f"   np_array = np.random.randn(5)")
    print(f"   pd.Series(np_array, index=['Point_1', 'Point_2', ...])")
    print(f"   Result:\n{np_series.round(3)}")
    
    # Method 5: From Scalar Value
    print(f"\n📝 Method 5: From Scalar Value")
    scalar_series = pd.Series(42, index=['A', 'B', 'C', 'D'])
    creation_methods['from_scalar'] = scalar_series
    
    print("   Scalar to Series:")
    print(f"   pd.Series(42, index=['A', 'B', 'C', 'D'])")
    print(f"   Result:\n{scalar_series}")
    
    # Method 6: From Range
    print(f"\n📝 Method 6: From Range Objects")
    range_series = pd.Series(range(0, 15, 3), index=[f'Step_{i}' for i in range(5)])
    creation_methods['from_range'] = range_series
    
    print("   Range to Series:")
    print(f"   pd.Series(range(0, 15, 3), index=['Step_0', 'Step_1', ...])")
    print(f"   Result:\n{range_series}")
    
    # Method 7: From Date Range
    print(f"\n📝 Method 7: Date/Time Series")
    dates = pd.date_range('2024-01-01', periods=5, freq='D')
    temp_data = [22.5, 24.1, 21.8, 23.9, 25.2]
    date_series = pd.Series(temp_data, index=dates, name='Temperature')
    creation_methods['time_series'] = date_series
    
    print("   Time series creation:")
    print(f"   dates = pd.date_range('2024-01-01', periods=5, freq='D')")
    print(f"   pd.Series(temp_data, index=dates)")
    print(f"   Result:\n{date_series}")
    
    return creation_methods

def series_data_types_and_conversion():
    """
    Understanding data types in Series and conversion methods
    """
    print("\n🏷️  SERIES DATA TYPES AND CONVERSION")
    print("=" * 38)
    
    print("📊 Data Type Examples:")
    
    # Different data types
    type_examples = [
        ('Integer', pd.Series([1, 2, 3, 4, 5]), 'int64'),
        ('Float', pd.Series([1.1, 2.2, 3.3, 4.4]), 'float64'),
        ('String', pd.Series(['apple', 'banana', 'cherry']), 'object'),
        ('Boolean', pd.Series([True, False, True, False]), 'bool'),
        ('DateTime', pd.Series(pd.date_range('2024-01-01', periods=3)), 'datetime64[ns]'),
        ('Category', pd.Series(['A', 'B', 'A', 'C']).astype('category'), 'category')
    ]
    
    for type_name, series, expected_dtype in type_examples:
        print(f"\n   {type_name} Series:")
        print(f"   Data: {list(series) if type_name != 'DateTime' else [str(d.date()) for d in series]}")
        print(f"   Dtype: {series.dtype}")
        print(f"   Memory usage: {series.memory_usage()} bytes")
    
    # Type conversion examples
    print(f"\n🔄 Type Conversion Examples:")
    
    original = pd.Series(['1', '2', '3', '4', '5'])
    print(f"   Original (string): {list(original)} (dtype: {original.dtype})")
    
    conversions = [
        ('to_numeric', pd.to_numeric(original), 'String to integer'),
        ('astype(float)', original.astype(float), 'String to float'),
        ('astype(bool)', pd.Series([0, 1, 0, 1]).astype(bool), 'Integer to boolean')
    ]
    
    for method, result, description in conversions:
        print(f"   {method}: {list(result)} (dtype: {result.dtype})")
        print(f"   → {description}")

# =============================================================================
# INDEXING AND SELECTION MASTERY
# =============================================================================

def series_indexing_mastery():
    """
    Complete guide to Series indexing and selection methods
    """
    print("\n🎯 SERIES INDEXING AND SELECTION MASTERY")
    print("=" * 43)
    
    # Create sample data for demonstrations
    student_scores = pd.Series(
        [85, 92, 78, 96, 89, 94, 82, 88, 91, 87],
        index=['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
        name='Test_Scores'
    )
    
    print("📊 Sample Data - Student Test Scores:")
    print(student_scores)
    
    # Different indexing methods
    indexing_methods = [
        {
            "method": "Single Label Access",
            "code": "student_scores['Alice']",
            "result": student_scores['Alice'],
            "description": "Access single value by label"
        },
        {
            "method": "Multiple Labels Access",
            "code": "student_scores[['Alice', 'Diana', 'Frank']]",
            "result": student_scores[['Alice', 'Diana', 'Frank']],
            "description": "Access multiple values by labels"
        },
        {
            "method": "Position-based Access (iloc)",
            "code": "student_scores.iloc[0:3]",
            "result": student_scores.iloc[0:3],
            "description": "Access by position (first 3 elements)"
        },
        {
            "method": "Label-based Slicing (loc)",
            "code": "student_scores.loc['Charlie':'Frank']",
            "result": student_scores.loc['Charlie':'Frank'],
            "description": "Slice by labels (inclusive of end)"
        },
        {
            "method": "Boolean Indexing",
            "code": "student_scores[student_scores > 90]",
            "result": student_scores[student_scores > 90],
            "description": "Select values meeting condition"
        },
        {
            "method": "Query Method",
            "code": "student_scores.where(student_scores >= 85).dropna()",
            "result": student_scores.where(student_scores >= 85).dropna(),
            "description": "Conditional selection with where"
        }
    ]
    
    print(f"\n🎯 Indexing Methods:")
    for method_info in indexing_methods:
        print(f"\n   📌 {method_info['method']}:")
        print(f"   Code: {method_info['code']}")
        print(f"   Result:")
        if isinstance(method_info['result'], pd.Series):
            print(str(method_info['result']).replace('\n', '\n   '))
        else:
            print(f"   {method_info['result']}")
        print(f"   → {method_info['description']}")
    
    return student_scores

def advanced_series_selection():
    """
    Advanced selection techniques and best practices
    """
    print("\n🚀 ADVANCED SERIES SELECTION TECHNIQUES")
    print("=" * 41)
    
    # Create time series data for advanced examples
    dates = pd.date_range('2024-01-01', periods=30, freq='D')
    stock_prices = pd.Series(
        np.random.uniform(100, 200, 30).round(2),
        index=dates,
        name='Stock_Price'
    )
    
    print("📈 Sample Time Series - Stock Prices (30 days):")
    print(stock_prices.head())
    print(f"... (showing first 5 of {len(stock_prices)} values)")
    
    # Advanced selection techniques
    print(f"\n🎯 Advanced Selection Techniques:")
    
    # 1. Conditional selection with multiple conditions
    high_value_stocks = stock_prices[(stock_prices > 150) & (stock_prices < 180)]
    print(f"\n   📊 Stocks between $150-$180:")
    print(f"   Count: {len(high_value_stocks)} days")
    print(f"   Average: ${high_value_stocks.mean():.2f}")
    
    # 2. Top N values
    top_5_days = stock_prices.nlargest(5)
    print(f"\n   🔝 Top 5 highest prices:")
    for date, price in top_5_days.items():
        print(f"   {date.strftime('%Y-%m-%d')}: ${price}")
    
    # 3. Pattern-based selection
    weekend_prices = stock_prices[stock_prices.index.dayofweek >= 5]
    if len(weekend_prices) > 0:
        print(f"\n   📅 Weekend prices: {len(weekend_prices)} days")
    else:
        print(f"\n   📅 No weekend data (as expected for stock prices)")
    
    # 4. Rolling window selection
    high_volatility_days = stock_prices[stock_prices.rolling(3).std() > 10]
    print(f"\n   📊 High volatility days (rolling 3-day std > 10):")
    print(f"   Count: {len(high_volatility_days)} days")
    
    return stock_prices

# =============================================================================
# SERIES OPERATIONS AND METHODS
# =============================================================================

def series_operations_comprehensive():
    """
    Comprehensive guide to Series operations and methods
    """
    print("\n⚙️  SERIES OPERATIONS - COMPREHENSIVE GUIDE")
    print("=" * 44)
    
    # Create sample data
    sales_data = pd.Series([1200, 1500, 800, 2100, 1800, 900, 1600, 1400], 
                          index=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
                          name='Monthly_Sales')
    
    print("📊 Sample Data - Monthly Sales:")
    print(sales_data)
    
    # Mathematical operations
    print(f"\n🧮 Mathematical Operations:")
    
    math_ops = [
        ('Sum', sales_data.sum(), 'Total sales'),
        ('Mean', sales_data.mean(), 'Average sales'),
        ('Median', sales_data.median(), 'Middle value'),
        ('Standard Deviation', sales_data.std(), 'Variability measure'),
        ('Min/Max', f"{sales_data.min()} / {sales_data.max()}", 'Range'),
        ('Quantiles (25%, 75%)', f"{sales_data.quantile(0.25)} / {sales_data.quantile(0.75)}", 'Quartiles')
    ]
    
    for operation, result, description in math_ops:
        if isinstance(result, float):
            print(f"   • {operation:<20}: {result:>8.1f} ({description})")
        else:
            print(f"   • {operation:<20}: {result:>8} ({description})")
    
    # Element-wise operations
    print(f"\n🔄 Element-wise Operations:")
    
    print(f"   Original: {list(sales_data)}")
    print(f"   Add 200:  {list(sales_data + 200)}")
    print(f"   Multiply by 1.1: {list((sales_data * 1.1).round().astype(int))}")
    print(f"   Square root: {list(np.sqrt(sales_data).round(1))}")
    
    # String operations (if applicable)
    text_series = pd.Series(['Apple', 'Banana', 'Cherry', 'Date'])
    print(f"\n📝 String Operations:")
    print(f"   Original: {list(text_series)}")
    print(f"   Uppercase: {list(text_series.str.upper())}")
    print(f"   Length: {list(text_series.str.len())}")
    print(f"   Contains 'a': {list(text_series.str.contains('a'))}")
    
    # Sorting operations
    print(f"\n🔀 Sorting Operations:")
    print(f"   By values (ascending): {sales_data.sort_values().index.tolist()}")
    print(f"   By values (descending): {sales_data.sort_values(ascending=False).head(3).index.tolist()}")
    print(f"   By index: {sales_data.sort_index().index.tolist()}")
    
    return sales_data

def series_aggregation_and_grouping():
    """
    Series aggregation, transformation, and grouping operations
    """
    print("\n📈 SERIES AGGREGATION AND TRANSFORMATION")
    print("=" * 42)
    
    # Create sample data with categories
    np.random.seed(42)
    categories = ['A', 'B', 'C'] * 20
    values = np.random.randint(10, 100, 60)
    
    categorical_series = pd.Series(values, 
                                 index=[f"{cat}_{i//3+1}" for i, cat in enumerate(categories)],
                                 name='Performance_Scores')
    
    # Extract category for grouping
    categorical_series.index = pd.MultiIndex.from_tuples(
        [(idx.split('_')[0], idx.split('_')[1]) for idx in categorical_series.index],
        names=['Category', 'Item']
    )
    
    print("📊 Sample Categorical Data:")
    print(categorical_series.head(9))
    print(f"... (showing first 9 of {len(categorical_series)} values)")
    
    # Aggregation operations
    print(f"\n📊 Aggregation by Category:")
    
    group_stats = categorical_series.groupby(level='Category').agg([
        'count', 'mean', 'std', 'min', 'max'
    ]).round(2)
    
    print(group_stats)
    
    # Rolling operations
    print(f"\n📈 Rolling Window Operations (window=5):")
    rolling_ops = [
        ('Rolling Mean', categorical_series.rolling(5).mean()),
        ('Rolling Std', categorical_series.rolling(5).std()),
        ('Rolling Max', categorical_series.rolling(5).max())
    ]
    
    for op_name, result in rolling_ops:
        print(f"   {op_name}: {result.tail(3).round(2).tolist()}")
    
    # Transformation operations
    print(f"\n🔄 Transformation Operations:")
    transformations = [
        ('Normalize (0-1)', (categorical_series - categorical_series.min()) / 
         (categorical_series.max() - categorical_series.min())),
        ('Z-score', (categorical_series - categorical_series.mean()) / categorical_series.std()),
        ('Rank', categorical_series.rank()),
        ('Percent Change', categorical_series.pct_change())
    ]
    
    for transform_name, result in transformations:
        sample_values = result.dropna().head(3).round(3).tolist()
        print(f"   {transform_name}: {sample_values} (sample)")
    
    return categorical_series

# =============================================================================
# PRACTICAL APPLICATIONS AND REAL-WORLD EXAMPLES
# =============================================================================

def real_world_series_applications():
    """
    Real-world applications and practical examples of Series usage
    """
    print("\n🌍 REAL-WORLD SERIES APPLICATIONS")
    print("=" * 36)
    
    applications = {}
    
    # Application 1: Time Series Analysis
    print("📈 Application 1: Stock Market Analysis")
    
    # Simulate daily stock returns
    np.random.seed(42)
    trading_days = pd.date_range('2024-01-01', '2024-03-31', freq='B')  # Business days
    daily_returns = pd.Series(
        np.random.normal(0.001, 0.02, len(trading_days)),  # Mean 0.1%, std 2%
        index=trading_days,
        name='Daily_Returns'
    )
    
    applications['stock_analysis'] = daily_returns
    
    # Analysis
    print(f"   • Trading days analyzed: {len(daily_returns)}")
    print(f"   • Average daily return: {daily_returns.mean():.4f} ({daily_returns.mean()*252:.2%} annualized)")
    print(f"   • Volatility (std): {daily_returns.std():.4f} ({daily_returns.std()*np.sqrt(252):.2%} annualized)")
    print(f"   • Best day: {daily_returns.max():.4f} on {daily_returns.idxmax().strftime('%Y-%m-%d')}")
    print(f"   • Worst day: {daily_returns.min():.4f} on {daily_returns.idxmin().strftime('%Y-%m-%d')}")
    
    # Calculate cumulative returns
    cumulative_returns = (1 + daily_returns).cumprod() - 1
    print(f"   • Total return: {cumulative_returns.iloc[-1]:.2%}")
    
    # Application 2: Customer Analytics
    print(f"\n👥 Application 2: Customer Satisfaction Analysis")
    
    customer_ratings = pd.Series([4.2, 3.8, 4.5, 4.1, 3.9, 4.3, 4.0, 4.4, 3.7, 4.2,
                                4.1, 4.6, 3.8, 4.3, 4.0, 3.9, 4.4, 4.2, 4.1, 4.5],
                               index=[f'Customer_{i+1}' for i in range(20)],
                               name='Satisfaction_Rating')
    
    applications['customer_analytics'] = customer_ratings
    
    print(f"   • Average rating: {customer_ratings.mean():.2f}/5.0")
    print(f"   • Rating distribution:")
    
    rating_bins = pd.cut(customer_ratings, bins=[0, 3.5, 4.0, 4.5, 5.0], 
                        labels=['Poor', 'Fair', 'Good', 'Excellent'])
    rating_counts = rating_bins.value_counts()
    
    for rating, count in rating_counts.items():
        percentage = (count / len(customer_ratings)) * 100
        print(f"     {rating}: {count} customers ({percentage:.1f}%)")
    
    # Application 3: Sensor Data Processing
    print(f"\n🌡️  Application 3: IoT Temperature Monitoring")
    
    # Simulate hourly temperature readings
    hours = pd.date_range('2024-01-01', '2024-01-02', freq='H')[:-1]  # 24 hours
    temperature_data = pd.Series(
        20 + 10 * np.sin(np.linspace(0, 2*np.pi, 24)) + np.random.normal(0, 1, 24),
        index=hours,
        name='Temperature_Celsius'
    )
    
    applications['iot_sensors'] = temperature_data
    
    print(f"   • 24-hour monitoring period")
    print(f"   • Average temperature: {temperature_data.mean():.1f}°C")
    print(f"   • Temperature range: {temperature_data.min():.1f}°C to {temperature_data.max():.1f}°C")
    print(f"   • Hours above 25°C: {len(temperature_data[temperature_data > 25])}")
    
    # Detect anomalies (values outside 2 standard deviations)
    anomalies = temperature_data[np.abs(temperature_data - temperature_data.mean()) > 2 * temperature_data.std()]
    if len(anomalies) > 0:
        print(f"   • Temperature anomalies detected: {len(anomalies)}")
        for time, temp in anomalies.items():
            print(f"     {time.strftime('%H:%M')}: {temp:.1f}°C")
    else:
        print(f"   • No temperature anomalies detected")
    
    return applications

def series_performance_optimization():
    """
    Performance optimization techniques for Series operations
    """
    print("\n⚡ SERIES PERFORMANCE OPTIMIZATION")
    print("=" * 36)
    
    print("🎯 Performance Best Practices:")
    
    # Create large sample data for benchmarking
    large_series = pd.Series(np.random.randn(100000))
    
    # Benchmark different operations
    import time
    
    benchmarks = []
    
    # Test 1: Vectorized vs loop operations
    print(f"\n🏃‍♂️ Benchmark 1: Vectorized vs Loop Operations")
    
    # Vectorized operation
    start_time = time.time()
    result_vectorized = large_series * 2 + 1
    vectorized_time = time.time() - start_time
    
    # Loop operation (avoid in practice!)
    start_time = time.time()
    result_loop = pd.Series([x * 2 + 1 for x in large_series.iloc[:1000]])  # Only 1000 for demo
    loop_time = time.time() - start_time
    
    print(f"   Vectorized (100k elements): {vectorized_time:.4f} seconds")
    print(f"   Loop (1k elements): {loop_time:.4f} seconds") 
    print(f"   Estimated loop time for 100k: {loop_time * 100:.2f} seconds")
    print(f"   Speedup: ~{(loop_time * 100) / vectorized_time:.0f}x faster with vectorization")
    
    # Memory usage optimization
    print(f"\n💾 Memory Usage Optimization:")
    
    # Different data types and their memory impact
    memory_examples = [
        ('float64', pd.Series(np.random.randn(10000), dtype='float64')),
        ('float32', pd.Series(np.random.randn(10000), dtype='float32')),
        ('int64', pd.Series(np.random.randint(0, 1000, 10000), dtype='int64')),
        ('int32', pd.Series(np.random.randint(0, 1000, 10000), dtype='int32')),
        ('category', pd.Series(['A', 'B', 'C'] * 3334, dtype='category'))
    ]
    
    print("   Memory usage by data type (10k elements):")
    for dtype_name, series in memory_examples:
        memory_mb = series.memory_usage(deep=True) / 1024 / 1024
        print(f"   {dtype_name:<10}: {memory_mb:.2f} MB")
    
    # Performance tips
    print(f"\n💡 Performance Tips:")
    tips = [
        "Use vectorized operations instead of loops",
        "Choose appropriate data types (int32 vs int64, float32 vs float64)",
        "Use categorical data type for repeated string values",
        "Avoid chained operations that create intermediate Series",
        "Use .loc and .iloc for efficient indexing",
        "Consider using .eval() for complex expressions",
        "Use .query() for readable boolean indexing"
    ]
    
    for i, tip in enumerate(tips, 1):
        print(f"   {i}. {tip}")

# =============================================================================
# MAIN EXECUTION AND COMPREHENSIVE DEMONSTRATION
# =============================================================================

def main():
    """
    Main function executing comprehensive Series guide
    """
    print(__doc__)
    
    # Fundamentals
    series_fundamentals()
    sample_series = series_anatomy_deep_dive()
    
    # Creation methods
    creation_examples = comprehensive_series_creation()
    series_data_types_and_conversion()
    
    # Indexing and selection
    student_data = series_indexing_mastery()
    stock_data = advanced_series_selection()
    
    # Operations and methods
    sales_data = series_operations_comprehensive()
    categorical_data = series_aggregation_and_grouping()
    
    # Real-world applications
    applications = real_world_series_applications()
    
    # Performance optimization
    series_performance_optimization()
    
    return {
        'sample_series': sample_series,
        'creation_examples': creation_examples,
        'student_data': student_data,
        'stock_data': stock_data,
        'sales_data': sales_data,
        'categorical_data': categorical_data,
        'applications': applications
    }

if __name__ == "__main__":
    """
    Execute comprehensive Pandas Series guide and demonstrations
    """
    series_examples = main()
    
    print("\n" + "=" * 60)
    print("🎓 PANDAS SERIES MASTERY SUMMARY")
    print("=" * 60)
    print("✅ Series fundamentals and architecture understanding")
    print("✅ Comprehensive creation methods from all data sources")
    print("✅ Data types, conversion, and memory optimization")
    print("✅ Advanced indexing and selection techniques")
    print("✅ Complete operations, methods, and transformations")
    print("✅ Aggregation, grouping, and statistical analysis")
    print("✅ Real-world applications across multiple domains")
    print("✅ Performance optimization best practices")
    
    print("\n💡 Key Series Mastery Points:")
    mastery_points = [
        "Series = Labeled 1D array optimized for analysis",
        "Flexible creation from lists, dicts, arrays, scalars",
        "Powerful indexing with labels and positions",
        "Vectorized operations for performance",
        "Rich statistical and mathematical methods",
        "Time series and categorical data support",
        "Memory-efficient data type selection",
        "Foundation building block for DataFrames"
    ]
    
    for point in mastery_points:
        print(f"   • {point}")
    
    print("\n🎯 Next Steps in Series Mastery:")
    next_steps = [
        "Practice with real datasets in your domain",
        "Explore time series analysis techniques", 
        "Master advanced indexing patterns",
        "Learn Series integration with DataFrames",
        "Study performance profiling and optimization",
        "Build custom Series operations and methods"
    ]
    
    for i, step in enumerate(next_steps, 1):
        print(f"   {i}. {step}")
    
    print(f"\n🚀 Series Mastery Achieved!")
    print("You now have comprehensive knowledge of Pandas Series.")
    print("Ready to tackle complex data analysis tasks with confidence!")
    
    # Provide access to examples for further exploration
    print(f"\n📊 Explore the examples:")
    for key, value in series_examples.items():
        if isinstance(value, pd.Series):
            print(f"   • {key}: {value.name or 'Unnamed Series'} ({len(value)} elements)")
        elif isinstance(value, dict):
            print(f"   • {key}: {len(value)} example Series")
        else:
            print(f"   • {key}: Available for exploration")
