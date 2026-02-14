"""
DATAFRAME CREATION
========================================
"""

import pandas as pd
import numpy as np
from datetime import datetime

print("=" * 80)
print("PANDAS DATAFRAME CREATION - COMPLETE GUIDE")
print("=" * 80)

# ============================================================================
# WHAT IS A DATAFRAME?
# ============================================================================
"""
A DataFrame is a 2-dimensional labeled data structure with columns of 
potentially different types. Think of it like:
- A spreadsheet or SQL table
- A dictionary of Series objects
- A matrix with row and column labels

Key Components:
- Index: Row labels (can be numeric or text)
- Columns: Column labels
- Data: The actual values stored in cells
"""

# ============================================================================
# METHOD 1: FROM DICTIONARY
# ============================================================================
print("\n" + "=" * 80)
print("METHOD 1: CREATING DATAFRAME FROM DICTIONARY")
print("=" * 80)

"""
EXPLANATION:
- Most common and intuitive method
- Dictionary keys become column names
- Dictionary values become column data
- All lists must have the same length
- Automatically creates numeric index (0, 1, 2, ...)
"""

# Example 1: Simple dictionary with lists
print("\n--- Example 1: Basic Dictionary with Lists ---")
data_dict = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 28],
    'city': ['New York', 'London', 'Paris', 'Tokyo'],
    'salary': [50000, 60000, 75000, 55000]
}

df_dict = pd.DataFrame(data_dict)
print("\nDataFrame created from dictionary:")
print(df_dict)
print(f"\nShape: {df_dict.shape}")  # (rows, columns)
print(f"Columns: {df_dict.columns.tolist()}")
print(f"Index: {df_dict.index.tolist()}")

# Example 2: Dictionary with different data types
print("\n--- Example 2: Mixed Data Types ---")
"""
EXPLANATION:
DataFrames can hold different data types in different columns:
- int64: Integer numbers
- float64: Decimal numbers
- object: Strings, mixed types
- bool: True/False values
- datetime64: Date and time values
"""

mixed_data = {
    'product': ['Laptop', 'Mouse', 'Keyboard'],
    'price': [1200.50, 25.99, 75.00],  # float
    'quantity': [10, 100, 50],  # int
    'in_stock': [True, True, False],  # boolean
    'last_updated': [datetime(2024, 1, 1), datetime(2024, 1, 2), datetime(2024, 1, 3)]
}

df_mixed = pd.DataFrame(mixed_data)
print("\nDataFrame with mixed data types:")
print(df_mixed)
print("\nData types of each column:")
print(df_mixed.dtypes)

# Example 3: Dictionary with custom index
print("\n--- Example 3: Custom Index ---")
"""
EXPLANATION:
- You can specify custom row labels using the 'index' parameter
- Index can be strings, numbers, or dates
- Useful for identifying rows meaningfully
"""

data_with_index = {
    'temperature': [72, 68, 75, 70],
    'humidity': [45, 50, 42, 48]
}

df_custom_index = pd.DataFrame(data_with_index, 
                                index=['Monday', 'Tuesday', 'Wednesday', 'Thursday'])
print("\nDataFrame with custom index:")
print(df_custom_index)

# ============================================================================
# METHOD 2: FROM LIST OF LISTS
# ============================================================================
print("\n" + "=" * 80)
print("METHOD 2: CREATING DATAFRAME FROM LIST OF LISTS")
print("=" * 80)

"""
EXPLANATION:
- Each inner list becomes a row
- Must specify column names separately
- Good for data that comes in row format
- More memory efficient for large datasets
"""

# Example 1: Basic list of lists
print("\n--- Example 1: Basic List of Lists ---")
data_list = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'London'],
    ['Charlie', 35, 'Paris'],
    ['David', 28, 'Tokyo']
]

df_list = pd.DataFrame(data_list, columns=['name', 'age', 'city'])
print("\nDataFrame from list of lists:")
print(df_list)

# Example 2: With custom index
print("\n--- Example 2: List of Lists with Custom Index ---")
df_list_index = pd.DataFrame(data_list, 
                              columns=['name', 'age', 'city'],
                              index=['emp001', 'emp002', 'emp003', 'emp004'])
print("\nDataFrame with employee IDs as index:")
print(df_list_index)

# ============================================================================
# METHOD 3: FROM LIST OF DICTIONARIES
# ============================================================================
print("\n" + "=" * 80)
print("METHOD 3: CREATING DATAFRAME FROM LIST OF DICTIONARIES")
print("=" * 80)

"""
EXPLANATION:
- Each dictionary represents one row
- Dictionary keys become column names
- Useful for JSON-like data
- Missing keys automatically filled with NaN
- Common format from APIs and web scraping
"""

# Example 1: Complete data
print("\n--- Example 1: List of Complete Dictionaries ---")
data_list_dict = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'London'},
    {'name': 'Charlie', 'age': 35, 'city': 'Paris'}
]

df_list_dict = pd.DataFrame(data_list_dict)
print("\nDataFrame from list of dictionaries:")
print(df_list_dict)

# Example 2: Incomplete data (missing values)
print("\n--- Example 2: List of Dictionaries with Missing Values ---")
"""
EXPLANATION:
- If a dictionary is missing a key, Pandas fills with NaN (Not a Number)
- NaN represents missing or undefined data
- Useful for handling incomplete datasets
"""

incomplete_data = [
    {'name': 'Alice', 'age': 25, 'city': 'New York', 'salary': 50000},
    {'name': 'Bob', 'age': 30, 'city': 'London'},  # Missing salary
    {'name': 'Charlie', 'city': 'Paris', 'salary': 75000}  # Missing age
]

df_incomplete = pd.DataFrame(incomplete_data)
print("\nDataFrame with missing values:")
print(df_incomplete)
print("\nMissing values shown:")
print(df_incomplete.isnull())

# ============================================================================
# METHOD 4: FROM NUMPY ARRAY
# ============================================================================
print("\n" + "=" * 80)
print("METHOD 4: CREATING DATAFRAME FROM NUMPY ARRAY")
print("=" * 80)

"""
EXPLANATION:
- NumPy arrays are efficient for numerical operations
- Must specify column names
- Can optionally specify index
- Fast for mathematical computations
- All values must be the same data type
"""

# Example 1: Random data
print("\n--- Example 1: From Random NumPy Array ---")
random_data = np.random.rand(5, 3)  # 5 rows, 3 columns
df_numpy = pd.DataFrame(random_data, columns=['A', 'B', 'C'])
print("\nDataFrame from NumPy array (random values):")
print(df_numpy)
print(f"\nArray shape: {random_data.shape}")

# Example 2: Structured array
print("\n--- Example 2: From Structured NumPy Array ---")
structured_data = np.array([[1, 2, 3], 
                            [4, 5, 6], 
                            [7, 8, 9]])

df_structured = pd.DataFrame(structured_data, 
                             columns=['Column1', 'Column2', 'Column3'],
                             index=['Row1', 'Row2', 'Row3'])
print("\nDataFrame from structured array:")
print(df_structured)

# Example 3: Integer range
print("\n--- Example 3: Using NumPy arange ---")
"""
EXPLANATION:
- np.arange() creates arrays of sequential numbers
- reshape() converts 1D array to 2D
- Useful for creating test data or sequences
"""

sequential_data = np.arange(1, 13).reshape(4, 3)  # Numbers 1-12 in 4x3 grid
df_sequential = pd.DataFrame(sequential_data, 
                             columns=['Q1', 'Q2', 'Q3'])
print("\nDataFrame with sequential data:")
print(df_sequential)

# ============================================================================
# METHOD 5: FROM SERIES
# ============================================================================
print("\n" + "=" * 80)
print("METHOD 5: CREATING DATAFRAME FROM SERIES")
print("=" * 80)

"""
EXPLANATION:
- Series is a 1-dimensional labeled array (single column)
- Multiple Series can be combined into a DataFrame
- Each Series becomes one column
- Series must have the same length or compatible indices
"""

# Example 1: From single Series
print("\n--- Example 1: From Single Series ---")
series_data = pd.Series([10, 20, 30, 40, 50], name='values')
df_from_series = pd.DataFrame(series_data)
print("\nDataFrame from single Series:")
print(df_from_series)

# Example 2: From multiple Series
print("\n--- Example 2: From Multiple Series (Dictionary of Series) ---")
"""
EXPLANATION:
- Create separate Series for each column
- Combine using dictionary where keys are column names
- All Series should have the same index
"""

name_series = pd.Series(['Alice', 'Bob', 'Charlie', 'David'])
age_series = pd.Series([25, 30, 35, 28])
city_series = pd.Series(['New York', 'London', 'Paris', 'Tokyo'])

df_multi_series = pd.DataFrame({
    'name': name_series,
    'age': age_series,
    'city': city_series
})
print("\nDataFrame from multiple Series:")
print(df_multi_series)

# ============================================================================
# METHOD 6: EMPTY DATAFRAME
# ============================================================================
print("\n" + "=" * 80)
print("METHOD 6: CREATING EMPTY DATAFRAME")
print("=" * 80)

"""
EXPLANATION:
- Sometimes you need to start with an empty DataFrame
- Useful when building data incrementally
- Can specify columns upfront or add later
"""

# Example 1: Completely empty
print("\n--- Example 1: Completely Empty DataFrame ---")
df_empty = pd.DataFrame()
print("Empty DataFrame:")
print(df_empty)
print(f"Shape: {df_empty.shape}")

# Example 2: Empty with column names
print("\n--- Example 2: Empty DataFrame with Columns ---")
"""
EXPLANATION:
- Define column structure but no data yet
- Useful as a template to fill later
- Maintains data type consistency
"""

df_empty_cols = pd.DataFrame(columns=['name', 'age', 'city'])
print("\nEmpty DataFrame with columns:")
print(df_empty_cols)
print(f"Columns: {df_empty_cols.columns.tolist()}")
print(f"Shape: {df_empty_cols.shape}")

# Example 3: Adding data to empty DataFrame
print("\n--- Example 3: Adding Data to Empty DataFrame ---")
df_build = pd.DataFrame(columns=['name', 'age', 'city'])

# Method 1: Using loc
df_build.loc[0] = ['Alice', 25, 'New York']
df_build.loc[1] = ['Bob', 30, 'London']

# Method 2: Using concat (recommended for multiple rows)
new_rows = pd.DataFrame([
    {'name': 'Charlie', 'age': 35, 'city': 'Paris'},
    {'name': 'David', 'age': 28, 'city': 'Tokyo'}
])
df_build = pd.concat([df_build, new_rows], ignore_index=True)

print("\nDataFrame after adding data:")
print(df_build)

# ============================================================================
# METHOD 7: FROM CSV STRING
# ============================================================================
print("\n" + "=" * 80)
print("METHOD 7: CREATING DATAFRAME FROM CSV STRING")
print("=" * 80)

"""
EXPLANATION:
- Create DataFrame from CSV-formatted string
- Useful for testing or embedded data
- Uses StringIO to treat string as file
"""

from io import StringIO

csv_string = """name,age,city
Alice,25,New York
Bob,30,London
Charlie,35,Paris"""

df_csv_string = pd.read_csv(StringIO(csv_string))
print("\nDataFrame from CSV string:")
print(df_csv_string)

# ============================================================================
# METHOD 8: FROM RECORDS (TUPLES)
# ============================================================================
print("\n" + "=" * 80)
print("METHOD 8: CREATING DATAFRAME FROM RECORDS")
print("=" * 80)

"""
EXPLANATION:
- Similar to list of lists but using tuples
- from_records() is optimized for tuple data
- Common format from database queries
"""

records = [
    (1, 'Alice', 25, 'New York'),
    (2, 'Bob', 30, 'London'),
    (3, 'Charlie', 35, 'Paris')
]

df_records = pd.DataFrame.from_records(
    records, 
    columns=['id', 'name', 'age', 'city']
)
print("\nDataFrame from records (tuples):")
print(df_records)

# ============================================================================
# METHOD 9: FROM DICTIONARY OF LISTS (DIFFERENT LENGTHS)
# ============================================================================
print("\n" + "=" * 80)
print("METHOD 9: HANDLING DIFFERENT LENGTH LISTS")
print("=" * 80)

"""
EXPLANATION:
- Sometimes you have columns with different lengths
- Pandas automatically fills shorter columns with NaN
- Useful for ragged data
"""

ragged_data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30],  # Shorter list
    'C': [100, 200, 300, 400]  # Different length
}

df_ragged = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in ragged_data.items()]))
print("\nDataFrame with different length columns:")
print(df_ragged)

# ============================================================================
# METHOD 10: USING FROM_DICT() WITH ORIENT PARAMETER
# ============================================================================
print("\n" + "=" * 80)
print("METHOD 10: USING from_dict() WITH DIFFERENT ORIENTATIONS")
print("=" * 80)

"""
EXPLANATION:
- from_dict() offers more control over dictionary structure
- 'columns' orient: keys are column names (default)
- 'index' orient: keys are row labels
- 'tight' orient: for specific format
"""

# Example 1: Orient = 'columns' (default)
print("\n--- Example 1: Orient = 'columns' ---")
data_cols = {
    'name': ['Alice', 'Bob'],
    'age': [25, 30]
}
df_orient_cols = pd.DataFrame.from_dict(data_cols, orient='columns')
print("Orient='columns' (keys are column names):")
print(df_orient_cols)

# Example 2: Orient = 'index'
print("\n--- Example 2: Orient = 'index' ---")
"""
EXPLANATION:
- When orient='index', dictionary keys become row indices
- Dictionary values are row data
"""

data_index = {
    'row1': {'name': 'Alice', 'age': 25},
    'row2': {'name': 'Bob', 'age': 30}
}
df_orient_index = pd.DataFrame.from_dict(data_index, orient='index')
print("Orient='index' (keys are row labels):")
print(df_orient_index)

# ============================================================================
# EXAMPLES AND USE CASES
# ============================================================================
print("\n" + "=" * 80)
print("PRACTICAL EXAMPLES")
print("=" * 80)

# Example 1: Creating a gradebook
print("\n--- Example 1: Student Gradebook ---")
gradebook = pd.DataFrame({
    'student_id': [101, 102, 103, 104],
    'name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'David Wilson'],
    'math': [92, 85, 78, 95],
    'science': [88, 90, 85, 92],
    'english': [95, 87, 90, 88]
})
print(gradebook)
print(f"\nAverage scores:\n{gradebook[['math', 'science', 'english']].mean()}")

# Example 2: Creating a product inventory
print("\n--- Example 2: Product Inventory ---")
inventory = pd.DataFrame({
    'product_id': ['P001', 'P002', 'P003', 'P004'],
    'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'category': ['Electronics', 'Accessories', 'Accessories', 'Electronics'],
    'price': [1200.00, 25.99, 75.50, 350.00],
    'quantity': [15, 200, 75, 30],
    'supplier': ['TechCorp', 'GadgetInc', 'GadgetInc', 'TechCorp']
})
print(inventory)
inventory['total_value'] = inventory['price'] * inventory['quantity']
print(f"\nTotal inventory value: ${inventory['total_value'].sum():,.2f}")

# Example 3: Creating time series data
print("\n--- Example 3: Time Series Data ---")
dates = pd.date_range(start='2024-01-01', periods=7, freq='D')
time_series = pd.DataFrame({
    'date': dates,
    'temperature': [72, 68, 75, 70, 73, 71, 69],
    'humidity': [45, 50, 42, 48, 46, 49, 51],
    'rainfall': [0, 0.5, 0, 1.2, 0.8, 0, 0]
})
print(time_series)

