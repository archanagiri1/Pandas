"""
Filter DataFrame (Where, Query)
==================================================
filtering DataFrames using various methods
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("=" * 80)
print("PANDAS DATAFRAME FILTERING")
print("=" * 80)

# ============================================================================
# WHAT IS FILTERING?
# ============================================================================
"""
Filtering (also called subsetting or selecting):
================================================

Definition:
- Selecting rows that meet specific conditions
- Creating a subset of data based on criteria
- Boolean indexing to find matching records

Methods Covered:
1. Boolean indexing (most common)
2. loc[] with conditions
3. query() method (SQL-like)
4. where() method
5. isin() for lists
6. between() for ranges
7. String methods for text filtering
"""

# Create comprehensive sample data
np.random.seed(42)
df = pd.DataFrame({
    'employee_id': range(101, 121),
    'name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'David Wilson', 
             'Eve Davis', 'Frank Miller', 'Grace Lee', 'Henry Garcia',
             'Iris Martinez', 'Jack Robinson', 'Kate Taylor', 'Leo Anderson',
             'Mia Thomas', 'Noah Jackson', 'Olivia White', 'Paul Harris',
             'Quinn Martin', 'Rachel Thompson', 'Sam Garcia', 'Tina Moore'],
    'age': [25, 30, 35, 28, 32, 45, 29, 38, 27, 41, 33, 36, 26, 39, 31, 42, 28, 34, 37, 40],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR',
                   'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT',
                   'HR', 'Finance', 'IT', 'HR'],
    'city': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney', 'Berlin',
             'Toronto', 'Mumbai', 'Singapore', 'Dubai', 'San Francisco', 'Madrid',
             'Chicago', 'Amsterdam', 'Seoul', 'Boston', 'Austin', 'Melbourne',
             'Seattle', 'Barcelona'],
    'salary': [50000, 60000, 75000, 55000, 70000, 85000, 58000, 65000,
               52000, 78000, 62000, 80000, 56000, 68000, 72000, 82000,
               54000, 76000, 79000, 67000],
    'experience_years': [2, 5, 10, 3, 7, 15, 4, 8, 2, 12, 6, 11, 3, 9, 5, 13, 3, 8, 10, 7],
    'performance_score': [8.5, 9.2, 7.8, 9.0, 8.8, 9.5, 8.3, 7.5, 8.9, 9.1,
                         8.7, 8.0, 9.3, 7.9, 8.4, 9.4, 8.1, 8.6, 9.0, 8.2],
    'active': [True, True, False, True, True, True, True, False, True, True,
               True, True, True, False, True, True, True, True, False, True],
    'join_date': pd.date_range('2020-01-01', periods=20, freq='2M')
})

print("\nSample Employee Dataset:")
print(df.head(10))
print(f"\nShape: {df.shape}")
print(f"\nData types:\n{df.dtypes}")
print(f"\nBasic statistics:\n{df[['age', 'salary', 'experience_years']].describe()}")

# ============================================================================
# METHOD 1: BOOLEAN INDEXING (MOST COMMON)
# ============================================================================
print("\n" + "=" * 80)
print("METHOD 1: BOOLEAN INDEXING")
print("=" * 80)

"""
EXPLANATION:
- Most intuitive and commonly used method
- Create boolean mask (True/False for each row)
- Use mask to select rows
- Syntax: df[condition]
- Returns DataFrame with matching rows
"""

print("\n--- Single Condition Filtering ---")

# Example 1: Age greater than 30
print("\n1. Employees older than 30:")
age_filter = df['age'] > 30
print(f"Boolean mask (first 5): {age_filter.head().tolist()}")
result = df[df['age'] > 30]
print(f"\nFiltered result ({len(result)} rows):")
print(result[['name', 'age', 'department']].head())

# Example 2: Exact match
print("\n2. Employees in IT department:")
it_employees = df[df['department'] == 'IT']
print(f"Found {len(it_employees)} IT employees:")
print(it_employees[['name', 'department', 'salary']].head())

# Example 3: Not equal
print("\n3. Employees NOT in HR:")
not_hr = df[df['department'] != 'HR']
print(f"Found {len(not_hr)} non-HR employees:")
print(not_hr[['name', 'department']].head())

# Example 4: Greater than or equal
print("\n4. Salary >= $70,000:")
high_salary = df[df['salary'] >= 70000]
print(f"Found {len(high_salary)} employees:")
print(high_salary[['name', 'salary']].head())

# Example 5: Less than
print("\n5. Experience < 5 years:")
junior = df[df['experience_years'] < 5]
print(f"Found {len(junior)} junior employees:")
print(junior[['name', 'experience_years']].head())

print("\n--- Multiple Conditions (AND, OR, NOT) ---")

"""
EXPLANATION:
Operators for combining conditions:
- & (AND): Both conditions must be True
- | (OR): At least one condition must be True
- ~ (NOT): Negates the condition
- Use parentheses () to group conditions!
"""

# Example 1: AND condition (&)
print("\n6. IT employees with salary > $60,000:")
it_and_high_salary = df[(df['department'] == 'IT') & (df['salary'] > 60000)]
print(f"Found {len(it_and_high_salary)} employees:")
print(it_and_high_salary[['name', 'department', 'salary']])

# Example 2: OR condition (|)
print("\n7. Employees in HR OR Finance:")
hr_or_finance = df[(df['department'] == 'HR') | (df['department'] == 'Finance')]
print(f"Found {len(hr_or_finance)} employees:")
print(hr_or_finance[['name', 'department']].head())

# Example 3: NOT condition (~)
print("\n8. NOT active employees:")
inactive = df[~df['active']]
print(f"Found {len(inactive)} inactive employees:")
print(inactive[['name', 'active']])

# Example 4: Complex combination
print("\n9. Complex: (Age > 30 AND Salary > $65,000) OR Department = Finance:")
complex_filter = df[((df['age'] > 30) & (df['salary'] > 65000)) | (df['department'] == 'Finance')]
print(f"Found {len(complex_filter)} employees:")
print(complex_filter[['name', 'age', 'salary', 'department']].head())

# Example 5: Multiple AND conditions
print("\n10. Age 25-35, Salary > $55,000, Active:")
multi_and = df[(df['age'] >= 25) & (df['age'] <= 35) & 
               (df['salary'] > 55000) & (df['active'] == True)]
print(f"Found {len(multi_and)} employees:")
print(multi_and[['name', 'age', 'salary', 'active']].head())

print("\n--- Common Boolean Operations ---")

# Greater than
print("\n11. Greater than (>):")
print(df[df['performance_score'] > 9.0][['name', 'performance_score']].head())

# Less than
print("\n12. Less than (<):")
print(df[df['age'] < 30][['name', 'age']].head())

# Equal to
print("\n13. Equal to (==):")
print(df[df['city'] == 'London'][['name', 'city']])

# Not equal to
print("\n14. Not equal to (!=):")
print(df[df['department'] != 'IT'][['name', 'department']].head())

# Greater than or equal
print("\n15. Greater than or equal (>=):")
print(df[df['salary'] >= 75000][['name', 'salary']].head())

# Less than or equal
print("\n16. Less than or equal (<=):")
print(df[df['experience_years'] <= 3][['name', 'experience_years']])

# ============================================================================
# METHOD 2: USING .loc[] WITH CONDITIONS
# ============================================================================
print("\n" + "=" * 80)
print("METHOD 2: USING .loc[] WITH CONDITIONS")
print("=" * 80)

"""
EXPLANATION:
- loc[] is label-based indexing
- Can filter rows AND select specific columns
- Syntax: df.loc[row_condition, columns]
- More flexible than simple boolean indexing
"""

print("\n--- Filter Rows and Select Columns ---")

# Example 1: Filter rows, select specific columns
print("\n1. IT employees - show only name and salary:")
result = df.loc[df['department'] == 'IT', ['name', 'salary']]
print(result.head())

# Example 2: Multiple conditions with column selection
print("\n2. Age > 30 and Salary > $60,000 - show name, age, salary:")
result = df.loc[(df['age'] > 30) & (df['salary'] > 60000), 
                ['name', 'age', 'salary']]
print(result)

# Example 3: All columns for filtered rows
print("\n3. High performers (score > 9.0) - all columns:")
result = df.loc[df['performance_score'] > 9.0]
print(result[['name', 'performance_score']].head())

# Example 4: Filter and modify
print("\n4. Give 10% raise to IT employees with experience > 5:")
# Create a copy to avoid modifying original
df_copy = df.copy()
it_experienced = (df_copy['department'] == 'IT') & (df_copy['experience_years'] > 5)
df_copy.loc[it_experienced, 'salary'] = df_copy.loc[it_experienced, 'salary'] * 1.10
print("Before and After comparison:")
comparison = pd.DataFrame({
    'name': df.loc[it_experienced, 'name'].values,
    'old_salary': df.loc[it_experienced, 'salary'].values,
    'new_salary': df_copy.loc[it_experienced, 'salary'].values
})
print(comparison)

# ============================================================================
# METHOD 3: .query() METHOD (SQL-LIKE)
# ============================================================================
print("\n" + "=" * 80)
print("METHOD 3: .query() METHOD")
print("=" * 80)

"""
EXPLANATION:
- SQL-like query syntax
- More readable for complex conditions
- String-based expressions
- Column names used directly (no df['column'])
- Supports variables with @
- Cleaner syntax for multiple conditions
"""

print("\n--- Basic Query Usage ---")

# Example 1: Simple condition
print("\n1. Age > 30 using query:")
result = df.query('age > 30')
print(f"Found {len(result)} employees:")
print(result[['name', 'age']].head())

# Example 2: Multiple conditions with 'and'
print("\n2. Age > 30 AND salary > 60000:")
result = df.query('age > 30 and salary > 60000')
print(result[['name', 'age', 'salary']])

# Example 3: Multiple conditions with 'or'
print("\n3. Department = HR OR department = Finance:")
result = df.query('department == "HR" or department == "Finance"')
print(f"Found {len(result)} employees:")
print(result[['name', 'department']].head())

# Example 4: Using 'not'
print("\n4. NOT active employees:")
result = df.query('not active')
print(result[['name', 'active']])

# Example 5: Complex query
print("\n5. Complex query with parentheses:")
result = df.query('(age > 30 and salary > 65000) or department == "Finance"')
print(f"Found {len(result)} employees:")
print(result[['name', 'age', 'salary', 'department']].head())

print("\n--- Query with Variables (using @) ---")

"""
EXPLANATION:
- Use @ to reference variables
- Useful for dynamic filtering
- Makes queries more flexible
"""

# Example 6: Using variables
print("\n6. Query with variables:")
min_age = 30
max_age = 40
min_salary = 60000

result = df.query('age >= @min_age and age <= @max_age and salary >= @min_salary')
print(f"Age {min_age}-{max_age}, Salary >= ${min_salary}:")
print(result[['name', 'age', 'salary']])

# Example 7: Variables from list
print("\n7. Filter by list of departments:")
target_departments = ['IT', 'Finance']
result = df.query('department in @target_departments')
print(f"Found {len(result)} employees in {target_departments}:")
print(result[['name', 'department']].head())

print("\n--- Advanced Query Features ---")

# Example 8: String contains
print("\n8. Names containing 'son' (case-insensitive):")
result = df.query('name.str.contains("son", case=False)', engine='python')
print(result[['name']])

# Example 9: Between values
print("\n9. Salary between 60000 and 75000:")
result = df.query('60000 <= salary <= 75000')
print(result[['name', 'salary']])

# Example 10: Not in list
print("\n10. Not in specific cities:")
excluded_cities = ['London', 'Paris', 'Tokyo']
result = df.query('city not in @excluded_cities')
print(f"Employees NOT in {excluded_cities}:")
print(result[['name', 'city']].head())

# Example 11: Index-based query
print("\n11. Query by index:")
result = df.query('index < 5')
print("First 5 rows using query:")
print(result[['name', 'age']])

# ============================================================================
# METHOD 4: .isin() FOR LIST MATCHING
# ============================================================================
print("\n" + "=" * 80)
print("METHOD 4: .isin() METHOD")
print("=" * 80)

"""
EXPLANATION:
- Check if values are in a list
- Returns boolean mask
- Cleaner than multiple OR conditions
- Case-sensitive for strings
- Works with any iterable
"""

print("\n--- Basic isin() Usage ---")

# Example 1: Filter by list of values
print("\n1. Employees in specific departments:")
departments_list = ['IT', 'Finance']
result = df[df['department'].isin(departments_list)]
print(f"Departments {departments_list} ({len(result)} employees):")
print(result[['name', 'department']].head())

# Example 2: Filter by multiple values
print("\n2. Employees in specific cities:")
cities = ['London', 'Tokyo', 'Sydney', 'Berlin']
result = df[df['city'].isin(cities)]
print(f"Cities {cities}:")
print(result[['name', 'city']].head())

# Example 3: NOT in list (using ~)
print("\n3. Employees NOT in HR or Finance:")
excluded_depts = ['HR', 'Finance']
result = df[~df['department'].isin(excluded_depts)]
print(f"NOT in {excluded_depts}:")
print(result[['name', 'department']])

# Example 4: Multiple columns with isin
print("\n4. Specific ages OR specific departments:")
target_ages = [25, 30, 35]
target_depts = ['IT']
result = df[df['age'].isin(target_ages) & df['department'].isin(target_depts)]
print(f"Ages {target_ages} in {target_depts}:")
print(result[['name', 'age', 'department']])

# Example 5: isin with range
print("\n5. Experience years in specific set:")
target_years = [2, 5, 10, 15]
result = df[df['experience_years'].isin(target_years)]
print(f"Experience in {target_years} years:")
print(result[['name', 'experience_years']])

# ============================================================================
# METHOD 5: .between() FOR RANGE FILTERING
# ============================================================================
print("\n" + "=" * 80)
print("METHOD 5: .between() METHOD")
print("=" * 80)

"""
EXPLANATION:
- Filter values within a range
- Inclusive by default (includes boundaries)
- Cleaner than (value >= x) & (value <= y)
- Works with numbers, dates, strings
"""

print("\n--- Basic between() Usage ---")

# Example 1: Age between range
print("\n1. Age between 28 and 35 (inclusive):")
result = df[df['age'].between(28, 35)]
print(f"Found {len(result)} employees:")
print(result[['name', 'age']].head())

# Example 2: Salary range
print("\n2. Salary between $55,000 and $75,000:")
result = df[df['salary'].between(55000, 75000)]
print(f"Found {len(result)} employees:")
print(result[['name', 'salary']].head())

# Example 3: Exclusive boundaries
print("\n3. Age between 28 and 35 (exclusive):")
result = df[df['age'].between(28, 35, inclusive='neither')]
print(f"Found {len(result)} employees (ages 29-34):")
print(result[['name', 'age']])

# Example 4: Left inclusive only
print("\n4. Salary range (left inclusive):")
result = df[df['salary'].between(60000, 70000, inclusive='left')]
print("Includes 60000, excludes 70000:")
print(result[['name', 'salary']])

# Example 5: Date range
print("\n5. Join date between range:")
start_date = pd.Timestamp('2020-01-01')
end_date = pd.Timestamp('2021-01-01')
result = df[df['join_date'].between(start_date, end_date)]
print(f"Joined between {start_date.date()} and {end_date.date()}:")
print(result[['name', 'join_date']])

# Example 6: Performance score range
print("\n6. Performance score 8.0 to 9.0:")
result = df[df['performance_score'].between(8.0, 9.0)]
print(f"Found {len(result)} employees:")
print(result[['name', 'performance_score']].head())

# ============================================================================
# METHOD 6: STRING FILTERING
# ============================================================================
print("\n" + "=" * 80)
print("METHOD 6: STRING FILTERING")
print("=" * 80)

"""
EXPLANATION:
- Special methods for text/string columns
- Access via .str accessor
- Case-sensitive by default
- Many methods available (contains, startswith, endswith, etc.)
"""

print("\n--- String Methods ---")

# Example 1: Contains substring
print("\n1. Names containing 'son':")
result = df[df['name'].str.contains('son')]
print(result[['name']])

# Example 2: Case-insensitive contains
print("\n2. Names containing 'son' (case-insensitive):")
result = df[df['name'].str.contains('son', case=False)]
print(result[['name']])

# Example 3: Starts with
print("\n3. Names starting with 'A':")
result = df[df['name'].str.startswith('A')]
print(result[['name']])

# Example 4: Ends with
print("\n4. Names ending with 'son':")
result = df[df['name'].str.endswith('son')]
print(result[['name']])

# Example 5: Exact length
print("\n5. Cities with exactly 5 characters:")
result = df[df['city'].str.len() == 5]
print(result[['name', 'city']])

# Example 6: Pattern matching (regex)
print("\n6. Names with pattern (starts with vowel):")
result = df[df['name'].str.match('^[AEIOU]', case=False)]
print(result[['name']])

# Example 7: Multiple substrings
print("\n7. Names containing 'a' AND 'n':")
result = df[df['name'].str.contains('a') & df['name'].str.contains('n')]
print(result[['name']].head())

# Example 8: Cities starting with specific letters
print("\n8. Cities starting with S, T, or M:")
result = df[df['city'].str.match('^[STM]')]
print(result[['name', 'city']])

# ============================================================================
# METHOD 7: .where() METHOD
# ============================================================================
print("\n" + "=" * 80)
print("METHOD 7: .where() METHOD")
print("=" * 80)

"""
EXPLANATION:
- Opposite of boolean indexing
- Keeps DataFrame shape (doesn't drop rows)
- Replaces non-matching values with NaN (or other value)
- Useful for conditional replacement
- Syntax: df.where(condition, other_value)
"""

print("\n--- where() Usage ---")

# Example 1: Basic where
print("\n1. Show salary only for IT department (others become NaN):")
result = df[['name', 'department', 'salary']].copy()
result['salary'] = result['salary'].where(result['department'] == 'IT')
print(result.head(10))

# Example 2: where with replacement value
print("\n2. Replace salary with 0 for non-IT employees:")
result = df[['name', 'department', 'salary']].copy()
result['salary'] = result['salary'].where(result['department'] == 'IT', 0)
print(result.head(10))

# Example 3: Multiple conditions
print("\n3. Show performance score only for active high earners:")
result = df[['name', 'salary', 'active', 'performance_score']].copy()
condition = (result['salary'] > 65000) & (result['active'] == True)
result['performance_score'] = result['performance_score'].where(condition)
print(result.head(10))

# Example 4: where vs boolean indexing comparison
print("\n4. Comparison: where vs boolean indexing:")
print("Boolean indexing (drops rows):")
bool_result = df[df['age'] > 35][['name', 'age']]
print(bool_result.head())

print("\nwhere (keeps all rows, NaN for non-matches):")
where_result = df[['name', 'age']].copy()
where_result['age'] = where_result['age'].where(df['age'] > 35)
print(where_result.head(10))

# ============================================================================
# METHOD 8: COMBINING MULTIPLE FILTER METHODS
# ============================================================================
print("\n" + "=" * 80)
print("METHOD 8: COMBINING MULTIPLE FILTER METHODS")
print("=" * 80)

"""
EXPLANATION:
- Can combine different filtering methods
- Chain multiple filters
- Each filter returns a DataFrame
- Apply next filter to the result
"""

print("\n--- Combined Filtering Examples ---")

# Example 1: isin + boolean
print("\n1. Combine isin and boolean conditions:")
result = df[df['department'].isin(['IT', 'Finance']) & (df['salary'] > 60000)]
print(f"IT or Finance with salary > $60,000:")
print(result[['name', 'department', 'salary']].head())

# Example 2: between + string contains
print("\n2. Age range + name pattern:")
result = df[df['age'].between(30, 40) & df['name'].str.contains('a', case=False)]
print("Age 30-40 with 'a' in name:")
print(result[['name', 'age']].head())

# Example 3: Multiple methods chained
print("\n3. Chain multiple filters:")
result = (df[df['department'].isin(['IT', 'Finance'])]
          [lambda x: x['age'].between(25, 35)]
          [lambda x: x['salary'] > 55000])
print("IT/Finance, age 25-35, salary > $55,000:")
print(result[['name', 'department', 'age', 'salary']])

# Example 4: query + isin
print("\n4. Query with isin:")
cities_list = ['London', 'Tokyo', 'Sydney']
result = df.query('department == "IT"')[df['city'].isin(cities_list)]
print(f"IT employees in {cities_list}:")
print(result[['name', 'department', 'city']])

# ============================================================================
# PRACTICAL FILTERING EXAMPLES
# ============================================================================
print("\n" + "=" * 80)
print("PRACTICAL FILTERING EXAMPLES")
print("=" * 80)

print("\n--- Real-World Scenarios ---")

# Example 1: Find top performers
print("\n1. Top Performers (score > 9.0, active, experience > 5):")
top_performers = df[
    (df['performance_score'] > 9.0) &
    (df['active'] == True) &
    (df['experience_years'] > 5)
]
print(top_performers[['name', 'performance_score', 'experience_years']])

# Example 2: Employees due for promotion
print("\n2. Due for Promotion (experience 7-10 years, good performance):")
promotion_candidates = df[
    df['experience_years'].between(7, 10) &
    (df['performance_score'] >= 8.5) &
    (df['active'] == True)
]
print(promotion_candidates[['name', 'experience_years', 'performance_score']])

# Example 3: Salary audit
print("\n3. Salary Audit (below market for experience):")
# Simple formula: should earn at least $45,000 + ($3,000 * years of experience)
expected_salary = 45000 + (df['experience_years'] * 3000)
underpaid = df[df['salary'] < expected_salary]
print(underpaid[['name', 'experience_years', 'salary']].head())

# Example 4: Department analysis
print("\n4. Department Analysis - High earners by department:")
for dept in df['department'].unique():
    dept_high_earners = df[
        (df['department'] == dept) &
        (df['salary'] > df[df['department'] == dept]['salary'].median())
    ]
    print(f"\n{dept}: {len(dept_high_earners)} above median")
    print(dept_high_earners[['name', 'salary']].head(3))

# Example 5: Inactive employees analysis
print("\n5. Inactive Employees - Investigation needed:")
inactive = df[~df['active']]
print(inactive[['name', 'department', 'join_date', 'performance_score']])

# Example 6: Multi-criteria search
print("\n6. Perfect Match Search:")
# Looking for: 30-40 years old, IT or Finance, salary 60-80k, active
perfect_match = df.query(
    '30 <= age <= 40 and '
    'department in ["IT", "Finance"] and '
    '60000 <= salary <= 80000 and '
    'active == True'
)
print(perfect_match[['name', 'age', 'department', 'salary']])



