"""
Pandas Getting Started - Comprehensive Data Analysis Foundation
===========================================================

Complete getting started guide for Pandas, covering installation, basic concepts,
DataFrame creation, essential operations, and practical examples to build a strong
foundation in Python data analysis and manipulation.

Author: Python Learning Notes
Date: September 2025
Topic: Pandas Introduction, DataFrames, Series, Data Analysis Fundamentals
"""

import pandas as pd
import numpy as np
import sys
import platform
from typing import Dict, List, Any
import warnings

# =============================================================================
# SYSTEM SETUP AND VERIFICATION
# =============================================================================

def check_pandas_environment():
    """
    Check Pandas installation and system compatibility
    """
    print("🔧 PANDAS ENVIRONMENT CHECK")
    print("=" * 30)
    
    # System information
    print(f"\n💻 System Information:")
    print(f"   Operating System: {platform.system()} {platform.release()}")
    print(f"   Python Version: {sys.version}")
    print(f"   Pandas Version: {pd.__version__}")
    
    # Check dependencies
    try:
        import numpy as np
        print(f"   NumPy Version: {np.__version__}")
    except ImportError:
        print("   ⚠️  NumPy not installed - required for Pandas")
    
    try:
        import matplotlib
        print(f"   Matplotlib Version: {matplotlib.__version__}")
    except ImportError:
        print("   ⚠️  Matplotlib not installed - optional for plotting")
    
    # Check pandas components
    print(f"\n🧰 Pandas Components Available:")
    components = [
        ("DataFrame", hasattr(pd, 'DataFrame')),
        ("Series", hasattr(pd, 'Series')),
        ("Index", hasattr(pd, 'Index')),
        ("read_csv", hasattr(pd, 'read_csv')),
        ("read_excel", hasattr(pd, 'read_excel')),
        ("to_datetime", hasattr(pd, 'to_datetime'))
    ]
    
    for component, available in components:
        status = "✅" if available else "❌"
        print(f"   {status} {component}")

def installation_guide():
    """
    Comprehensive installation guide for different environments
    """
    print("\n📦 PANDAS INSTALLATION GUIDE")
    print("=" * 32)
    
    installation_methods = [
        {
            "method": "pip (Standard)",
            "command": "pip install pandas",
            "description": "Standard Python package manager",
            "pros": ["Easy", "Quick", "Works everywhere"],
            "cons": ["May need additional dependencies"]
        },
        {
            "method": "conda",
            "command": "conda install pandas",
            "description": "Anaconda/Miniconda package manager",
            "pros": ["Handles dependencies", "Scientific stack"],
            "cons": ["Requires Anaconda/Miniconda"]
        },
        {
            "method": "pip with extras",
            "command": "pip install pandas[all]",
            "description": "Pandas with optional dependencies",
            "pros": ["Complete functionality", "All features"],
            "cons": ["Larger download size"]
        }
    ]
    
    print("🛠️  Installation Methods:")
    for method in installation_methods:
        print(f"\n   📋 {method['method']}:")
        print(f"      Command: {method['command']}")
        print(f"      Description: {method['description']}")
        print(f"      Pros: {', '.join(method['pros'])}")
        print(f"      Cons: {', '.join(method['cons'])}")
    
    print(f"\n🔍 Verify Installation:")
    print(f"   After installation, verify with:")
    print(f"   >>> import pandas as pd")
    print(f"   >>> print(pd.__version__)")

# =============================================================================
# PANDAS FUNDAMENTALS AND CONCEPTS
# =============================================================================

def pandas_overview():
    """
    Comprehensive overview of what Pandas is and why it's important
    """
    print("\n📊 WHAT IS PANDAS?")
    print("=" * 18)
    
    print("📚 Definition:")
    print("   Pandas (Python Data Analysis Library) is a powerful, open-source")
    print("   data manipulation and analysis library built on top of NumPy.")
    
    print(f"\n🏗️  Architecture:")
    print(f"   • Built on NumPy for performance")
    print(f"   • Provides high-level data structures")
    print(f"   • Integrates with entire Python ecosystem")
    print(f"   • Handles heterogeneous data types")
    print(f"   • Memory efficient operations")
    
    print(f"\n🎯 Core Data Structures:")
    
    structures = {
        "Series": {
            "description": "1D labeled array (like column in spreadsheet)",
            "use_cases": ["Time series data", "Single column operations", "Index-based data"],
            "example": "pd.Series([1, 2, 3], index=['a', 'b', 'c'])"
        },
        "DataFrame": {
            "description": "2D labeled data structure (like spreadsheet/table)",
            "use_cases": ["Tabular data", "Multiple columns", "Data analysis"],
            "example": "pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})"
        }
    }
    
    for structure, info in structures.items():
        print(f"\n   📋 {structure}:")
        print(f"      Description: {info['description']}")
        print(f"      Use Cases: {', '.join(info['use_cases'])}")
        print(f"      Example: {info['example']}")

def why_use_pandas():
    """
    Explain the benefits and advantages of using Pandas
    """
    print("\n⚡ WHY USE PANDAS?")
    print("=" * 17)
    
    advantages = {
        "🚀 Performance": [
            "Built on optimized NumPy arrays",
            "Vectorized operations for speed",
            "Efficient memory usage",
            "C-level performance for core operations"
        ],
        "🛠️  Functionality": [
            "Rich set of data manipulation tools",
            "Handles missing data gracefully", 
            "Flexible data input/output",
            "Powerful grouping and aggregation"
        ],
        "📈 Data Analysis": [
            "Statistical operations built-in",
            "Time series analysis capabilities",
            "Data cleaning and preparation tools",
            "Integration with visualization libraries"
        ],
        "🌐 Ecosystem": [
            "Works with NumPy, Matplotlib, Scikit-learn",
            "Reads from CSV, Excel, JSON, SQL databases",
            "Exports to multiple formats",
            "Large community and documentation"
        ]
    }
    
    for category, benefits in advantages.items():
        print(f"\n{category}:")
        for benefit in benefits:
            print(f"   • {benefit}")

# =============================================================================
# HANDS-ON DATAFRAME CREATION AND MANIPULATION
# =============================================================================

def basic_dataframe_creation():
    """
    Comprehensive guide to creating DataFrames from various sources
    """
    print("\n🏗️  DATAFRAME CREATION METHODS")
    print("=" * 31)
    
    print("📝 Method 1: From Dictionary")
    print("   Most common method for small datasets")
    
    # Basic dictionary to DataFrame
    student_data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'Age': [23, 25, 22, 24, 26],
        'Grade': ['A', 'B+', 'A-', 'A', 'B'],
        'Score': [95, 87, 92, 98, 85]
    }
    
    df_students = pd.DataFrame(student_data)
    print("\n   Student DataFrame:")
    print(df_students)
    
    # Add basic information
    print(f"\n   📊 DataFrame Info:")
    print(f"   Shape: {df_students.shape}")
    print(f"   Columns: {list(df_students.columns)}")
    print(f"   Data Types:\n{df_students.dtypes}")
    
    print("\n📝 Method 2: From Lists of Lists")
    print("   Useful when data comes in row format")
    
    # List of lists to DataFrame
    sales_data = [
        ['Q1', 'Product A', 1000, 50000],
        ['Q1', 'Product B', 800, 32000],
        ['Q2', 'Product A', 1200, 60000],
        ['Q2', 'Product B', 900, 36000]
    ]
    
    df_sales = pd.DataFrame(sales_data, columns=['Quarter', 'Product', 'Units', 'Revenue'])
    print("\n   Sales DataFrame:")
    print(df_sales)
    
    print("\n📝 Method 3: From NumPy Array")
    print("   Efficient for numerical data")
    
    # NumPy array to DataFrame
    np_data = np.random.randn(4, 3)  # 4 rows, 3 columns of random numbers
    df_numpy = pd.DataFrame(np_data, 
                           columns=['Feature_1', 'Feature_2', 'Feature_3'],
                           index=['Sample_1', 'Sample_2', 'Sample_3', 'Sample_4'])
    print("\n   NumPy-based DataFrame:")
    print(df_numpy.round(3))
    
    return df_students, df_sales, df_numpy

def dataframe_inspection_methods():
    """
    Essential methods for inspecting and understanding DataFrames
    """
    print("\n🔍 DATAFRAME INSPECTION METHODS")
    print("=" * 33)
    
    # Create sample data for inspection
    dates = pd.date_range('2024-01-01', periods=100, freq='D')
    df_sample = pd.DataFrame({
        'Date': dates,
        'Temperature': np.random.normal(20, 5, 100),
        'Humidity': np.random.uniform(30, 80, 100),
        'Pressure': np.random.normal(1013, 10, 100),
        'City': np.random.choice(['New York', 'London', 'Tokyo'], 100)
    })
    
    inspection_methods = [
        ('df.head()', 'First 5 rows', lambda: df_sample.head()),
        ('df.tail()', 'Last 5 rows', lambda: df_sample.tail()),
        ('df.info()', 'DataFrame summary', lambda: df_sample.info()),
        ('df.describe()', 'Statistical summary', lambda: df_sample.describe()),
        ('df.shape', 'Dimensions (rows, cols)', lambda: df_sample.shape),
        ('df.columns', 'Column names', lambda: list(df_sample.columns)),
        ('df.dtypes', 'Data types', lambda: df_sample.dtypes)
    ]
    
    print("📊 Sample Weather Dataset:")
    print(df_sample.head(3))
    
    for method, description, func in inspection_methods:
        print(f"\n🔎 {method} - {description}:")
        try:
            result = func()
            if hasattr(result, 'to_string'):
                print(str(result).replace('\n', '\n   '))
            else:
                print(f"   {result}")
        except Exception as e:
            print(f"   Result displayed separately due to formatting")
    
    return df_sample

def basic_dataframe_operations():
    """
    Essential DataFrame operations for data manipulation
    """
    print("\n⚙️  BASIC DATAFRAME OPERATIONS")
    print("=" * 32)
    
    # Create sample employee data
    employees = pd.DataFrame({
        'Employee_ID': range(1001, 1011),
        'Name': ['John Doe', 'Jane Smith', 'Mike Johnson', 'Sarah Williams', 
                'David Brown', 'Lisa Davis', 'Chris Wilson', 'Emma Garcia', 
                'Alex Martinez', 'Jessica Lee'],
        'Department': ['IT', 'HR', 'Finance', 'IT', 'Marketing', 
                      'Finance', 'IT', 'HR', 'Marketing', 'Finance'],
        'Salary': [75000, 65000, 70000, 80000, 60000, 
                  72000, 85000, 68000, 62000, 74000],
        'Years_Experience': [5, 3, 7, 6, 2, 8, 9, 4, 3, 6]
    })
    
    print("👥 Employee Dataset:")
    print(employees.head())
    
    print(f"\n🎯 Column Selection:")
    print("   Single column (returns Series):")
    print(employees['Name'].head(3))
    
    print(f"\n   Multiple columns (returns DataFrame):")
    print(employees[['Name', 'Department', 'Salary']].head(3))
    
    print(f"\n🎯 Row Selection:")
    print("   By index position (iloc):")
    print(employees.iloc[0:3])
    
    print(f"\n   By condition (boolean indexing):")
    high_salary = employees[employees['Salary'] > 70000]
    print(f"   Employees with salary > $70,000:")
    print(high_salary[['Name', 'Department', 'Salary']])
    
    print(f"\n🎯 Adding New Columns:")
    employees['Salary_Grade'] = employees['Salary'].apply(
        lambda x: 'Senior' if x >= 75000 else 'Junior'
    )
    print("   Added Salary_Grade column:")
    print(employees[['Name', 'Salary', 'Salary_Grade']].head(3))
    
    return employees

# =============================================================================
# PRACTICAL EXAMPLES AND USE CASES
# =============================================================================

def practical_data_analysis_example():
    """
    Real-world example of data analysis using Pandas
    """
    print("\n🌟 PRACTICAL DATA ANALYSIS EXAMPLE")
    print("=" * 35)
    
    print("📈 Scenario: Sales Performance Analysis")
    print("   Analyzing monthly sales data for different products and regions")
    
    # Generate realistic sales data
    np.random.seed(42)
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    products = ['Laptop', 'Desktop', 'Tablet', 'Phone']
    regions = ['North', 'South', 'East', 'West']
    
    sales_records = []
    for month in months:
        for product in products:
            for region in regions:
                units = np.random.randint(50, 200)
                price = {'Laptop': 1200, 'Desktop': 800, 'Tablet': 400, 'Phone': 600}[product]
                revenue = units * price + np.random.normal(0, price * 0.1)
                
                sales_records.append({
                    'Month': month,
                    'Product': product,
                    'Region': region,
                    'Units_Sold': units,
                    'Revenue': round(revenue, 2)
                })
    
    df_sales = pd.DataFrame(sales_records)
    
    print(f"\n📊 Sample Sales Data:")
    print(df_sales.head(8))
    
    print(f"\n📈 Analysis 1: Total Revenue by Product")
    revenue_by_product = df_sales.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
    print(revenue_by_product)
    
    print(f"\n📈 Analysis 2: Average Units Sold by Region")
    units_by_region = df_sales.groupby('Region')['Units_Sold'].mean().round(1)
    print(units_by_region)
    
    print(f"\n📈 Analysis 3: Monthly Revenue Trend")
    monthly_revenue = df_sales.groupby('Month')['Revenue'].sum()
    print(monthly_revenue)
    
    print(f"\n📈 Analysis 4: Top Performing Product-Region Combinations")
    top_combinations = (df_sales.groupby(['Product', 'Region'])['Revenue']
                       .sum().sort_values(ascending=False).head())
    print("Top 5 Product-Region combinations by revenue:")
    print(top_combinations)
    
    return df_sales

def common_pandas_patterns():
    """
    Common patterns and idioms in Pandas
    """
    print("\n🎨 COMMON PANDAS PATTERNS")
    print("=" * 27)
    
    # Create sample data for demonstrations
    data = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Diana'],
        'Subject': ['Math', 'Math', 'Science', 'Science', 'English', 'Math'],
        'Score': [95, 87, 92, 88, 94, 91],
        'Date': pd.to_datetime(['2024-01-15', '2024-01-16', '2024-01-17', 
                               '2024-01-18', '2024-01-19', '2024-01-20'])
    })
    
    print("📊 Sample Test Scores Data:")
    print(data)
    
    patterns = [
        {
            "name": "Filter and Select",
            "description": "Get high scores in Math",
            "code": "data[(data['Subject'] == 'Math') & (data['Score'] > 90)]",
            "result": data[(data['Subject'] == 'Math') & (data['Score'] > 90)]
        },
        {
            "name": "Group and Aggregate",
            "description": "Average score by student",
            "code": "data.groupby('Name')['Score'].mean()",
            "result": data.groupby('Name')['Score'].mean()
        },
        {
            "name": "Sort Values",
            "description": "Sort by score descending",
            "code": "data.sort_values('Score', ascending=False)",
            "result": data.sort_values('Score', ascending=False)
        }
    ]
    
    for pattern in patterns:
        print(f"\n🎯 Pattern: {pattern['name']}")
        print(f"   Description: {pattern['description']}")
        print(f"   Code: {pattern['code']}")
        print(f"   Result:")
        print(str(pattern['result']).replace('\n', '\n   '))

# =============================================================================
# MAIN EXECUTION AND LEARNING PATH
# =============================================================================

def main():
    """
    Main function to execute all Pandas getting started content
    """
    print(__doc__)
    
    # Environment setup
    check_pandas_environment()
    installation_guide()
    
    # Conceptual understanding
    pandas_overview()
    why_use_pandas()
    
    # Hands-on practice
    df_students, df_sales, df_numpy = basic_dataframe_creation()
    df_weather = dataframe_inspection_methods()
    df_employees = basic_dataframe_operations()
    
    # Real-world application
    df_sales_analysis = practical_data_analysis_example()
    common_pandas_patterns()
    
    return {
        'students': df_students,
        'sales': df_sales,
        'numpy_data': df_numpy,
        'weather': df_weather,
        'employees': df_employees,
        'sales_analysis': df_sales_analysis
    }

if __name__ == "__main__":
    """
    Execute the complete Pandas getting started guide
    """
    dataframes = main()
    
    print("\n" + "=" * 50)
    print("🎓 PANDAS GETTING STARTED SUMMARY")
    print("=" * 50)
    print("✅ Environment setup and verification completed")
    print("✅ Core concepts and data structures explained")
    print("✅ DataFrame creation methods demonstrated")
    print("✅ Essential inspection and manipulation operations")
    print("✅ Real-world data analysis examples provided")
    print("✅ Common patterns and best practices covered")
    
    print("\n💡 Key Learning Outcomes:")
    print("• Understanding of Pandas purpose and ecosystem")
    print("• Mastery of DataFrame and Series creation")
    print("• Essential data inspection and manipulation skills")
    print("• Practical data analysis techniques")
    print("• Foundation for advanced Pandas operations")
    
    print("\n🎯 Next Steps in Your Pandas Journey:")
    next_topics = [
        "Data cleaning and handling missing values",
        "Advanced indexing and selection methods",
        "Merging and joining datasets",
        "Time series analysis and date handling",
        "Data visualization with Pandas plotting",
        "Performance optimization techniques"
    ]
    
    for i, topic in enumerate(next_topics, 1):
        print(f"   {i}. {topic}")
    
    print("\n🚀 Ready to Dive Deeper into Data Analysis!")
    print("Continue with other files in this module to build expertise!")


