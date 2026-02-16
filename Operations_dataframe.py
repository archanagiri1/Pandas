"""
DataFrame Operations: Add, Update, Delete, Sort
==================================================================
"""

import pandas as pd
import numpy as np

print("=" * 80)
print("DATAFRAME OPERATIONS - ADD, UPDATE, DELETE, SORT")
print("=" * 80)

# Sample data
df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 28, 32],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'salary': [50000, 60000, 75000, 55000, 70000]
})

print("\nOriginal DataFrame:")
print(df)

# ============================================================================
# PART 1: ADD OPERATIONS
# ============================================================================
print("\n" + "=" * 80)
print("PART 1: ADD OPERATIONS")
print("=" * 80)

# ----------------------------------------------------------------------------
# ADD COLUMNS
# ----------------------------------------------------------------------------
print("\n--- ADD COLUMNS ---")

# Method 1: Direct assignment
print("\n1. Add column with single value:")
df['country'] = 'USA'
print(df)

# Method 2: Add column with list
print("\n2. Add column with list of values:")
df['city'] = ['New York', 'London', 'Paris', 'Tokyo', 'Sydney']
print(df)

# Method 3: Add calculated column
print("\n3. Add calculated column:")
df['annual_salary'] = df['salary'] * 12
print(df)

# Method 4: Add column based on condition
print("\n4. Add column based on condition:")
df['senior'] = df['age'] > 30
print(df)

# Method 5: Using assign() method
print("\n5. Add column using assign():")
df = df.assign(bonus=df['salary'] * 0.1)
print(df)

# Method 6: Add multiple columns at once
print("\n6. Add multiple columns at once:")
df['tax'] = df['salary'] * 0.2
df['net_salary'] = df['salary'] - df['tax']
print(df)

# Method 7: Insert column at specific position
print("\n7. Insert column at specific position:")
df.insert(2, 'gender', ['F', 'M', 'M', 'M', 'F'])
print(df)

# ----------------------------------------------------------------------------
# ADD ROWS
# ----------------------------------------------------------------------------
print("\n--- ADD ROWS ---")

# Reset df for clarity
df = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
})

# Method 1: Using loc[] with new index
print("\n1. Add row using loc[]:")
df.loc[3] = [4, 'David', 28]
print(df)

# Method 2: Using concat() - Recommended
print("\n2. Add row using concat():")
new_row = pd.DataFrame({'id': [5], 'name': ['Eve'], 'age': [32]})
df = pd.concat([df, new_row], ignore_index=True)
print(df)

# Method 3: Add multiple rows
print("\n3. Add multiple rows:")
new_rows = pd.DataFrame({
    'id': [6, 7],
    'name': ['Frank', 'Grace'],
    'age': [45, 29]
})
df = pd.concat([df, new_rows], ignore_index=True)
print(df)

# Method 4: Append dictionary as row
print("\n4. Append dictionary as row:")
new_data = pd.DataFrame([{'id': 8, 'name': 'Henry', 'age': 38}])
df = pd.concat([df, new_data], ignore_index=True)
print(df)

# ============================================================================
# PART 2: UPDATE OPERATIONS
# ============================================================================
print("\n" + "=" * 80)
print("PART 2: UPDATE OPERATIONS")
print("=" * 80)

# Reset df
df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 28, 32],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'salary': [50000, 60000, 75000, 55000, 70000]
})

# ----------------------------------------------------------------------------
# UPDATE SINGLE VALUE
# ----------------------------------------------------------------------------
print("\n--- UPDATE SINGLE VALUE ---")

# Method 1: Using loc[]
print("\n1. Update single value using loc[]:")
df.loc[0, 'age'] = 26
print(df)

# Method 2: Using at[] (faster for single value)
print("\n2. Update single value using at[]:")
df.at[0, 'salary'] = 52000
print(df)

# Method 3: Using iloc[] (position-based)
print("\n3. Update using iloc[]:")
df.iloc[0, 2] = 27
print(df)

# Method 4: Using iat[] (fastest for single value)
print("\n4. Update using iat[]:")
df.iat[0, 4] = 53000
print(df)

# ----------------------------------------------------------------------------
# UPDATE ENTIRE COLUMN
# ----------------------------------------------------------------------------
print("\n--- UPDATE ENTIRE COLUMN ---")

# Method 1: Replace all values
print("\n5. Update entire column:")
df['department'] = 'Engineering'
print(df)

# Method 2: Update with calculation
print("\n6. Update column with calculation:")
df['salary'] = df['salary'] * 1.1  # 10% raise
print(df)

# Method 3: Update with list
print("\n7. Update column with list:")
df['department'] = ['HR', 'IT', 'Finance', 'IT', 'HR']
print(df)

# ----------------------------------------------------------------------------
# UPDATE MULTIPLE VALUES
# ----------------------------------------------------------------------------
print("\n--- UPDATE MULTIPLE VALUES ---")

# Method 1: Update row
print("\n8. Update entire row:")
df.loc[0] = [1, 'Alice Smith', 28, 'HR', 60000]
print(df)

# Method 2: Update multiple columns for a row
print("\n9. Update multiple columns:")
df.loc[1, ['age', 'salary']] = [31, 65000]
print(df)

# Method 3: Update subset of rows
print("\n10. Update subset of rows:")
df.loc[0:2, 'department'] = 'Sales'
print(df)

# ----------------------------------------------------------------------------
# CONDITIONAL UPDATE
# ----------------------------------------------------------------------------
print("\n--- CONDITIONAL UPDATE ---")

# Reset df
df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 28, 32],
    'salary': [50000, 60000, 75000, 55000, 70000]
})

# Method 1: Update based on condition
print("\n11. Update where age > 30:")
df.loc[df['age'] > 30, 'salary'] = df.loc[df['age'] > 30, 'salary'] * 1.2
print(df)

# Method 2: Update multiple columns conditionally
print("\n12. Update multiple columns based on condition:")
df.loc[df['age'] < 30, ['salary', 'age']] = [45000, 25]
print(df)

# Method 3: Replace specific values
print("\n13. Replace specific values:")
df['name'] = df['name'].replace('Alice', 'Alice Johnson')
print(df)

# Method 4: Replace multiple values
print("\n14. Replace multiple values:")
df['age'] = df['age'].replace({25: 26, 30: 31})
print(df)

# Method 5: Update using apply
print("\n15. Update using apply:")
df['salary'] = df['salary'].apply(lambda x: x * 1.05)
print(df)

# Method 6: Update using np.where
print("\n16. Update using np.where:")
df['category'] = np.where(df['age'] > 30, 'Senior', 'Junior')
print(df)

# ============================================================================
# PART 3: DELETE OPERATIONS
# ============================================================================
print("\n" + "=" * 80)
print("PART 3: DELETE OPERATIONS")
print("=" * 80)

# Reset df
df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 28, 32],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'salary': [50000, 60000, 75000, 55000, 70000],
    'bonus': [5000, 6000, 7500, 5500, 7000]
})

# ----------------------------------------------------------------------------
# DELETE COLUMNS
# ----------------------------------------------------------------------------
print("\n--- DELETE COLUMNS ---")

# Method 1: Using drop() - returns new DataFrame
print("\n1. Delete column using drop():")
df_new = df.drop('bonus', axis=1)
print(df_new)
print("\nOriginal df unchanged:")
print(df)

# Method 2: Using drop() with inplace
print("\n2. Delete column inplace:")
df.drop('bonus', axis=1, inplace=True)
print(df)

# Method 3: Delete multiple columns
df['bonus'] = [5000, 6000, 7500, 5500, 7000]
df['commission'] = [1000, 2000, 1500, 1200, 1800]
print("\n3. Delete multiple columns:")
df = df.drop(['bonus', 'commission'], axis=1)
print(df)

# Method 4: Using del keyword
df['temp'] = 'temporary'
print("\n4. Delete using del:")
del df['temp']
print(df)

# Method 5: Using pop() - returns the deleted column
df['extra'] = 100
print("\n5. Delete using pop():")
removed_col = df.pop('extra')
print("Removed column:", removed_col.head())
print("DataFrame after pop:")
print(df)

# ----------------------------------------------------------------------------
# DELETE ROWS
# ----------------------------------------------------------------------------
print("\n--- DELETE ROWS ---")

# Method 1: Drop by index
print("\n6. Delete row by index:")
df_new = df.drop(0)
print(df_new)

# Method 2: Drop multiple rows
print("\n7. Delete multiple rows:")
df_new = df.drop([0, 2, 4])
print(df_new)

# Method 3: Drop by condition
print("\n8. Delete rows by condition:")
df_new = df[df['age'] <= 30]  # Keep only age <= 30
print(df_new)

# Method 4: Drop using index range
print("\n9. Delete using index range:")
df_new = df.drop(df.index[0:2])
print(df_new)

# Method 5: Delete based on condition using drop
print("\n10. Delete high salary employees:")
df_new = df.drop(df[df['salary'] > 60000].index)
print(df_new)

# ----------------------------------------------------------------------------
# DELETE DUPLICATES
# ----------------------------------------------------------------------------
print("\n--- DELETE DUPLICATES ---")

# Create df with duplicates
df_dup = pd.DataFrame({
    'id': [1, 2, 2, 3, 3, 4],
    'name': ['Alice', 'Bob', 'Bob', 'Charlie', 'Charlie', 'David'],
    'value': [100, 200, 200, 300, 350, 400]
})

print("\n11. DataFrame with duplicates:")
print(df_dup)

# Method 1: Drop all duplicates
print("\n12. Drop duplicate rows:")
df_clean = df_dup.drop_duplicates()
print(df_clean)

# Method 2: Drop duplicates based on specific columns
print("\n13. Drop duplicates based on column:")
df_clean = df_dup.drop_duplicates(subset=['name'])
print(df_clean)

# Method 3: Keep last occurrence
print("\n14. Keep last occurrence of duplicates:")
df_clean = df_dup.drop_duplicates(subset=['name'], keep='last')
print(df_clean)

# Method 4: Keep first occurrence (default)
print("\n15. Keep first occurrence:")
df_clean = df_dup.drop_duplicates(subset=['name'], keep='first')
print(df_clean)

# Method 5: Remove all duplicates
print("\n16. Remove all duplicate occurrences:")
df_clean = df_dup.drop_duplicates(subset=['name'], keep=False)
print(df_clean)

# ----------------------------------------------------------------------------
# DELETE MISSING VALUES
# ----------------------------------------------------------------------------
print("\n--- DELETE MISSING VALUES ---")

# Create df with NaN
df_nan = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, 2, 3, 4, 5]
})

print("\n17. DataFrame with NaN:")
print(df_nan)

# Method 1: Drop rows with any NaN
print("\n18. Drop rows with any NaN:")
df_clean = df_nan.dropna()
print(df_clean)

# Method 2: Drop rows where all values are NaN
print("\n19. Drop rows where all are NaN:")
df_clean = df_nan.dropna(how='all')
print(df_clean)

# Method 3: Drop columns with any NaN
print("\n20. Drop columns with any NaN:")
df_clean = df_nan.dropna(axis=1)
print(df_clean)

# Method 4: Drop based on threshold
print("\n21. Drop rows with less than 2 non-NaN values:")
df_clean = df_nan.dropna(thresh=2)
print(df_clean)

# Method 5: Drop based on specific columns
print("\n22. Drop rows where column A is NaN:")
df_clean = df_nan.dropna(subset=['A'])
print(df_clean)

# ============================================================================
# PART 4: SORT OPERATIONS
# ============================================================================
print("\n" + "=" * 80)
print("PART 4: SORT OPERATIONS")
print("=" * 80)

# Reset df
df = pd.DataFrame({
    'id': [5, 2, 8, 1, 9],
    'name': ['Eve', 'Bob', 'Henry', 'Alice', 'Iris'],
    'age': [32, 30, 38, 25, 27],
    'department': ['HR', 'IT', 'Finance', 'HR', 'IT'],
    'salary': [70000, 60000, 78000, 50000, 79000]
})

print("\nUnsorted DataFrame:")
print(df)

# ----------------------------------------------------------------------------
# SORT BY VALUES
# ----------------------------------------------------------------------------
print("\n--- SORT BY VALUES ---")

# Method 1: Sort by single column (ascending)
print("\n1. Sort by age (ascending):")
df_sorted = df.sort_values('age')
print(df_sorted)

# Method 2: Sort by single column (descending)
print("\n2. Sort by salary (descending):")
df_sorted = df.sort_values('salary', ascending=False)
print(df_sorted)

# Method 3: Sort by multiple columns
print("\n3. Sort by department, then salary:")
df_sorted = df.sort_values(['department', 'salary'])
print(df_sorted)

# Method 4: Sort by multiple columns with different order
print("\n4. Sort by department (asc), salary (desc):")
df_sorted = df.sort_values(['department', 'salary'], ascending=[True, False])
print(df_sorted)

# Method 5: Sort inplace
print("\n5. Sort inplace:")
df.sort_values('age', inplace=True)
print(df)

# Method 6: Sort with NaN handling
df_with_nan = df.copy()
df_with_nan.loc[2, 'age'] = np.nan
print("\n6. Sort with NaN (NaN at end):")
df_sorted = df_with_nan.sort_values('age', na_position='last')
print(df_sorted)

print("\n7. Sort with NaN (NaN at start):")
df_sorted = df_with_nan.sort_values('age', na_position='first')
print(df_sorted)

# Method 7: Sort by custom key function
print("\n8. Sort by name length:")
df_sorted = df.sort_values('name', key=lambda x: x.str.len())
print(df_sorted)

# ----------------------------------------------------------------------------
# SORT BY INDEX
# ----------------------------------------------------------------------------
print("\n--- SORT BY INDEX ---")

# Shuffle for demonstration
df_shuffled = df.sample(frac=1)
print("\n9. Shuffled DataFrame:")
print(df_shuffled)

# Method 1: Sort by index (ascending)
print("\n10. Sort by index (ascending):")
df_sorted = df_shuffled.sort_index()
print(df_sorted)

# Method 2: Sort by index (descending)
print("\n11. Sort by index (descending):")
df_sorted = df_shuffled.sort_index(ascending=False)
print(df_sorted)

# Method 3: Sort by column names (axis=1)
df_cols = df.copy()
df_cols = df_cols[['salary', 'name', 'age', 'id', 'department']]
print("\n12. Before sorting columns:")
print(df_cols.head())

print("\n13. Sort by column names:")
df_sorted = df_cols.sort_index(axis=1)
print(df_sorted.head())

# ----------------------------------------------------------------------------
# ADVANCED SORTING
# ----------------------------------------------------------------------------
print("\n--- ADVANCED SORTING ---")

# Method 1: Get top N values
print("\n14. Top 3 by salary:")
top_3 = df.nlargest(3, 'salary')
print(top_3)

# Method 2: Get bottom N values
print("\n15. Bottom 2 by age:")
bottom_2 = df.nsmallest(2, 'age')
print(bottom_2)

# Method 3: Sort and reset index
print("\n16. Sort and reset index:")
df_sorted = df.sort_values('salary', ascending=False).reset_index(drop=True)
print(df_sorted)

# Method 4: Sort by multiple columns with nlargest
print("\n17. Top 3 by department and salary:")
# Group by department and get top salaries
for dept in df['department'].unique():
    dept_top = df[df['department'] == dept].nlargest(2, 'salary')
    print(f"\n{dept} department top salaries:")
    print(dept_top[['name', 'department', 'salary']])

# Method 5: Stable sort (maintains order for equal values)
df_stable = pd.DataFrame({
    'category': ['A', 'B', 'A', 'B', 'A'],
    'value': [1, 1, 2, 1, 1],
    'id': [1, 2, 3, 4, 5]
})

print("\n18. Stable sort (preserves original order for ties):")
print("Original:")
print(df_stable)
print("\nSorted (stable):")
df_sorted = df_stable.sort_values(['category', 'value'], kind='stable')
print(df_sorted)

# ============================================================================
# COMBINING OPERATIONS
# ============================================================================
print("\n" + "=" * 80)
print("COMBINING OPERATIONS")
print("=" * 80)

# Reset df
df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 28, 32],
    'salary': [50000, 60000, 75000, 55000, 70000]
})

print("\n1. Add column, update values, delete rows, and sort:")

# Add bonus column
df['bonus'] = df['salary'] * 0.1

# Update salary for age > 30
df.loc[df['age'] > 30, 'salary'] = df.loc[df['age'] > 30, 'salary'] * 1.15

# Delete bonus column
df = df.drop('bonus', axis=1)

# Sort by salary descending
df = df.sort_values('salary', ascending=False)

print(df)

print("\n2. Add, filter, update, and sort in chain:")
df_result = (df.copy()
             .assign(category=lambda x: np.where(x['age'] > 30, 'Senior', 'Junior'))
             .query('salary > 55000')
             .sort_values('age', ascending=False)
             .reset_index(drop=True))

print(df_result)

print("\n" + "=" * 80)
print("END OF DATAFRAME OPERATIONS TUTORIAL")
print("=" * 80)