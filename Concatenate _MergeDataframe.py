"""
Concatenate and Merge DataFrame (JOINS)
===========================================================
combining DataFrames using concat, merge, and join
"""

import pandas as pd
import numpy as np

print("=" * 80)
print("CONCATENATE AND MERGE DATAFRAME (JOINS)")
print("=" * 80)

# ============================================================================
# PART 1: CONCATENATE - STACKING DATAFRAMES
# ============================================================================
print("\n" + "=" * 80)
print("PART 1: CONCATENATE (pd.concat)")
print("=" * 80)

# Sample DataFrames
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2'],
    'C': ['C0', 'C1', 'C2']
})

df2 = pd.DataFrame({
    'A': ['A3', 'A4', 'A5'],
    'B': ['B3', 'B4', 'B5'],
    'C': ['C3', 'C4', 'C5']
})

print("\nDataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

# Vertical concatenation (stack rows)
print("\n1. Vertical concatenation (axis=0, default):")
result = pd.concat([df1, df2])
print(result)

# Reset index after concatenation
print("\n2. Concatenate and reset index:")
result = pd.concat([df1, df2], ignore_index=True)
print(result)

# Concatenate with keys (multi-index)
print("\n3. Concatenate with keys:")
result = pd.concat([df1, df2], keys=['df1', 'df2'])
print(result)

# Horizontal concatenation (add columns)
df3 = pd.DataFrame({
    'D': ['D0', 'D1', 'D2'],
    'E': ['E0', 'E1', 'E2']
})

print("\n4. Horizontal concatenation (axis=1):")
print("\nDataFrame 3:")
print(df3)
result = pd.concat([df1, df3], axis=1)
print("\nConcatenated:")
print(result)

# Concatenate DataFrames with different columns
df4 = pd.DataFrame({
    'A': ['A0', 'A1'],
    'B': ['B0', 'B1'],
    'D': ['D0', 'D1']  # Different column
})

print("\n5. Concatenate with different columns (outer join, default):")
print("\nDataFrame 4:")
print(df4)
result = pd.concat([df1, df4])
print("\nConcatenated (NaN for missing):")
print(result)

# Inner join - only keep common columns
print("\n6. Concatenate with inner join (only common columns):")
result = pd.concat([df1, df4], join='inner')
print(result)

# Outer join - keep all columns
print("\n7. Concatenate with outer join (all columns):")
result = pd.concat([df1, df4], join='outer')
print(result)

# Concatenate multiple DataFrames
df5 = pd.DataFrame({
    'A': ['A6', 'A7'],
    'B': ['B6', 'B7'],
    'C': ['C6', 'C7']
})

print("\n8. Concatenate multiple DataFrames:")
result = pd.concat([df1, df2, df5], ignore_index=True)
print(result)

# Verify axis
print("\n9. Verify axis parameter:")
result = pd.concat([df1, df3], axis=1, keys=['Left', 'Right'])
print(result)

# ============================================================================
# PART 2: MERGE - DATABASE-STYLE JOINS
# ============================================================================
print("\n" + "=" * 80)
print("PART 2: MERGE (pd.merge)")
print("=" * 80)

# Sample DataFrames for merging
left = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})

right = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K4'],
    'C': ['C0', 'C1', 'C2', 'C4'],
    'D': ['D0', 'D1', 'D2', 'D4']
})

print("\nLeft DataFrame:")
print(left)
print("\nRight DataFrame:")
print(right)

# Inner join (default) - only matching keys
print("\n1. INNER JOIN (default) - only matching keys:")
result = pd.merge(left, right, on='key')
print(result)
print("Note: K3 and K4 are excluded (not in both)")

# Left join - keep all from left
print("\n2. LEFT JOIN - keep all from left:")
result = pd.merge(left, right, on='key', how='left')
print(result)
print("Note: K3 kept with NaN for C and D")

# Right join - keep all from right
print("\n3. RIGHT JOIN - keep all from right:")
result = pd.merge(left, right, on='key', how='right')
print(result)
print("Note: K4 kept with NaN for A and B")

# Outer join - keep all from both
print("\n4. OUTER JOIN - keep all from both:")
result = pd.merge(left, right, on='key', how='outer')
print(result)
print("Note: K3 and K4 both kept with NaN where missing")

# Merge on multiple columns
left_multi = pd.DataFrame({
    'key1': ['K0', 'K0', 'K1', 'K2'],
    'key2': ['K0', 'K1', 'K0', 'K1'],
    'A': ['A0', 'A1', 'A2', 'A3']
})

right_multi = pd.DataFrame({
    'key1': ['K0', 'K1', 'K1', 'K2'],
    'key2': ['K0', 'K0', 'K0', 'K1'],
    'B': ['B0', 'B1', 'B2', 'B3']
})

print("\n5. Merge on multiple columns:")
print("\nLeft:")
print(left_multi)
print("\nRight:")
print(right_multi)
result = pd.merge(left_multi, right_multi, on=['key1', 'key2'])
print("\nMerged:")
print(result)

# Merge with different column names
left_diff = pd.DataFrame({
    'left_key': ['K0', 'K1', 'K2'],
    'A': ['A0', 'A1', 'A2']
})

right_diff = pd.DataFrame({
    'right_key': ['K0', 'K1', 'K2'],
    'B': ['B0', 'B1', 'B2']
})

print("\n6. Merge with different column names:")
print("\nLeft:")
print(left_diff)
print("\nRight:")
print(right_diff)
result = pd.merge(left_diff, right_diff, left_on='left_key', right_on='right_key')
print("\nMerged:")
print(result)

# Suffixes for overlapping columns
left_overlap = pd.DataFrame({
    'key': ['K0', 'K1', 'K2'],
    'value': [1, 2, 3]
})

right_overlap = pd.DataFrame({
    'key': ['K0', 'K1', 'K2'],
    'value': [4, 5, 6]
})

print("\n7. Merge with overlapping column names (suffixes):")
print("\nLeft:")
print(left_overlap)
print("\nRight:")
print(right_overlap)
result = pd.merge(left_overlap, right_overlap, on='key', suffixes=('_left', '_right'))
print("\nMerged:")
print(result)

# Indicator - show source of each row
print("\n8. Merge with indicator:")
result = pd.merge(left, right, on='key', how='outer', indicator=True)
print(result)
print("\n_merge column shows: left_only, right_only, or both")

# Custom indicator name
print("\n9. Merge with custom indicator name:")
result = pd.merge(left, right, on='key', how='outer', indicator='source')
print(result)

# ============================================================================
# PART 3: JOIN - INDEX-BASED MERGE
# ============================================================================
print("\n" + "=" * 80)
print("PART 3: JOIN (Index-based)")
print("=" * 80)

# DataFrames with index
left_idx = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
}, index=['K0', 'K1', 'K2'])

right_idx = pd.DataFrame({
    'C': ['C0', 'C1', 'C2'],
    'D': ['D0', 'D1', 'D2']
}, index=['K0', 'K2', 'K3'])

print("\nLeft DataFrame (with index):")
print(left_idx)
print("\nRight DataFrame (with index):")
print(right_idx)

# Join on index (left join by default)
print("\n1. Join on index (left join, default):")
result = left_idx.join(right_idx)
print(result)

# Inner join
print("\n2. Join with how='inner':")
result = left_idx.join(right_idx, how='inner')
print(result)

# Outer join
print("\n3. Join with how='outer':")
result = left_idx.join(right_idx, how='outer')
print(result)

# Join with suffix
left_idx2 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'value': [1, 2, 3]
}, index=['K0', 'K1', 'K2'])

right_idx2 = pd.DataFrame({
    'B': ['B0', 'B1', 'B2'],
    'value': [4, 5, 6]
}, index=['K0', 'K1', 'K2'])

print("\n4. Join with suffix for overlapping columns:")
print("\nLeft:")
print(left_idx2)
print("\nRight:")
print(right_idx2)
result = left_idx2.join(right_idx2, lsuffix='_left', rsuffix='_right')
print("\nJoined:")
print(result)

# Join column to index
left_col = pd.DataFrame({
    'key': ['K0', 'K1', 'K2'],
    'A': ['A0', 'A1', 'A2']
})

right_idx3 = pd.DataFrame({
    'B': ['B0', 'B1', 'B2']
}, index=['K0', 'K1', 'K2'])

print("\n5. Merge column to index:")
print("\nLeft (key as column):")
print(left_col)
print("\nRight (index):")
print(right_idx3)
result = pd.merge(left_col, right_idx3, left_on='key', right_index=True)
print("\nMerged:")
print(result)

# ============================================================================
# PART 4: COMBINING DIFFERENT SCENARIOS
# ============================================================================
print("\n" + "=" * 80)
print("PART 4: COMMON SCENARIOS")
print("=" * 80)

# One-to-one merge
employees = pd.DataFrame({
    'emp_id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie']
})

salaries = pd.DataFrame({
    'emp_id': [1, 2, 3],
    'salary': [50000, 60000, 70000]
})

print("\n1. One-to-One Merge:")
print("\nEmployees:")
print(employees)
print("\nSalaries:")
print(salaries)
result = pd.merge(employees, salaries, on='emp_id')
print("\nMerged:")
print(result)

# One-to-many merge
departments = pd.DataFrame({
    'dept_id': [1, 2, 3],
    'dept_name': ['HR', 'IT', 'Finance']
})

employees_dept = pd.DataFrame({
    'emp_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'dept_id': [1, 2, 2, 3, 1]
})

print("\n2. One-to-Many Merge:")
print("\nDepartments:")
print(departments)
print("\nEmployees:")
print(employees_dept)
result = pd.merge(employees_dept, departments, on='dept_id')
print("\nMerged:")
print(result)

# Many-to-many merge
students = pd.DataFrame({
    'student_id': [1, 1, 2, 2, 3],
    'course_id': [101, 102, 101, 103, 102]
})

courses = pd.DataFrame({
    'course_id': [101, 102, 103],
    'course_name': ['Math', 'Physics', 'Chemistry']
})

print("\n3. Many-to-Many Merge:")
print("\nStudents:")
print(students)
print("\nCourses:")
print(courses)
result = pd.merge(students, courses, on='course_id')
print("\nMerged:")
print(result)

# Chain multiple merges
employees_chain = pd.DataFrame({
    'emp_id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'dept_id': [1, 2, 1]
})

departments_chain = pd.DataFrame({
    'dept_id': [1, 2],
    'dept_name': ['HR', 'IT'],
    'location_id': [10, 20]
})

locations = pd.DataFrame({
    'location_id': [10, 20],
    'city': ['New York', 'London']
})

print("\n4. Chain Multiple Merges:")
print("\nEmployees:")
print(employees_chain)
print("\nDepartments:")
print(departments_chain)
print("\nLocations:")
print(locations)

result = (employees_chain
          .merge(departments_chain, on='dept_id')
          .merge(locations, on='location_id'))
print("\nMerged:")
print(result)

# ============================================================================
# PART 5: HANDLING DUPLICATES IN MERGE
# ============================================================================
print("\n" + "=" * 80)
print("PART 5: HANDLING DUPLICATES")
print("=" * 80)

# Duplicate keys in left
left_dup = pd.DataFrame({
    'key': ['K0', 'K1', 'K1', 'K2'],
    'A': ['A0', 'A1', 'A2', 'A3']
})

right_dup = pd.DataFrame({
    'key': ['K0', 'K1', 'K2'],
    'B': ['B0', 'B1', 'B2']
})

print("\nLeft (with duplicate K1):")
print(left_dup)
print("\nRight:")
print(right_dup)

print("\n1. Merge with duplicates in left:")
result = pd.merge(left_dup, right_dup, on='key')
print(result)
print("Note: K1 appears twice in result (cartesian product)")

# Duplicate keys in both
left_both = pd.DataFrame({
    'key': ['K0', 'K1', 'K1'],
    'A': ['A0', 'A1', 'A2']
})

right_both = pd.DataFrame({
    'key': ['K0', 'K1', 'K1'],
    'B': ['B0', 'B1', 'B2']
})

print("\n2. Duplicates in both DataFrames:")
print("\nLeft:")
print(left_both)
print("\nRight:")
print(right_both)
result = pd.merge(left_both, right_both, on='key')
print("\nMerged (cartesian product):")
print(result)
print("Note: K1 appears 4 times (2 x 2)")

# Validate merge (detect duplicates)
print("\n3. Validate merge (one_to_one):")
try:
    result = pd.merge(left_dup, right_dup, on='key', validate='one_to_one')
except Exception as e:
    print(f"Error: {e}")

print("\n4. Validate merge (one_to_many):")
result = pd.merge(left_dup, right_dup, on='key', validate='one_to_many')
print("Validation passed")

# ============================================================================
# PART 6: APPEND (DEPRECATED - USE CONCAT)
# ============================================================================
print("\n" + "=" * 80)
print("PART 6: APPEND (Use concat instead)")
print("=" * 80)

df_a = pd.DataFrame({
    'A': ['A0', 'A1'],
    'B': ['B0', 'B1']
})

df_b = pd.DataFrame({
    'A': ['A2', 'A3'],
    'B': ['B2', 'B3']
})

print("\nDataFrame A:")
print(df_a)
print("\nDataFrame B:")
print(df_b)

# Old way (deprecated)
print("\n1. Old append() method (deprecated):")
print("df_a.append(df_b, ignore_index=True)")

# Recommended way
print("\n2. Recommended: Use concat():")
result = pd.concat([df_a, df_b], ignore_index=True)
print(result)


# ============================================================================
# PART 8: EXAMPLES
# ============================================================================
print("\n" + "=" * 80)
print("PART 8:  EXAMPLES")
print("=" * 80)

# Example 1: Combine quarterly sales data
q1 = pd.DataFrame({
    'product': ['A', 'B', 'C'],
    'Q1_sales': [100, 200, 150]
})

q2 = pd.DataFrame({
    'product': ['A', 'B', 'C'],
    'Q2_sales': [120, 180, 160]
})

print("\n1. Combine quarterly data:")
print("\nQ1:")
print(q1)
print("\nQ2:")
print(q2)

# Method 1: Merge
result = pd.merge(q1, q2, on='product')
print("\nUsing merge:")
print(result)

# Method 2: Concat (if same structure)
q1_indexed = q1.set_index('product')
q2_indexed = q2.set_index('product')
result = pd.concat([q1_indexed, q2_indexed], axis=1)
print("\nUsing concat:")
print(result)

# Example 2: Customer and Order data
customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David']
})

orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105],
    'customer_id': [1, 2, 1, 3, 2],
    'amount': [100, 200, 150, 300, 250]
})

print("\n2. Customer-Order relationship:")
print("\nCustomers:")
print(customers)
print("\nOrders:")
print(orders)

result = pd.merge(orders, customers, on='customer_id', how='left')
print("\nMerged (all orders with customer names):")
print(result)

# Example 3: Add metadata to existing data
data = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'value': [10, 20, 30, 40, 50]
})

metadata = pd.DataFrame({
    'id': [1, 3, 5],
    'category': ['A', 'B', 'A']
})

print("\n3. Add metadata (left join to keep all data):")
print("\nData:")
print(data)
print("\nMetadata:")
print(metadata)

result = pd.merge(data, metadata, on='id', how='left')
print("\nMerged:")
print(result)

