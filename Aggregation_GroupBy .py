"""
Aggregation and GroupBy
==========================================
grouping and aggregating data
"""

import pandas as pd
import numpy as np

print("=" * 80)
print("AGGREGATION AND GROUPBY IN PANDAS")
print("=" * 80)

# Sample DataFrame
df = pd.DataFrame({
    'department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance'],
    'employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry', 'Iris', 'Jack'],
    'salary': [60000, 50000, 65000, 70000, 55000, 68000, 72000, 52000, 63000, 75000],
    'age': [25, 30, 28, 35, 32, 27, 40, 29, 26, 38],
    'experience': [2, 5, 3, 8, 6, 4, 10, 5, 3, 9],
    'performance': [8.5, 7.8, 9.0, 8.2, 8.8, 8.0, 9.2, 7.5, 8.7, 8.4]
})

print("\nSample DataFrame:")
print(df)

# ============================================================================
# PART 1: BASIC AGGREGATION (WITHOUT GROUPBY)
# ============================================================================
print("\n" + "=" * 80)
print("PART 1: BASIC AGGREGATION (WITHOUT GROUPBY)")
print("=" * 80)

# Single aggregation functions
print("\n1. Sum:")
print(df['salary'].sum())

print("\n2. Mean:")
print(df['salary'].mean())

print("\n3. Median:")
print(df['salary'].median())

print("\n4. Min:")
print(df['salary'].min())

print("\n5. Max:")
print(df['salary'].max())

print("\n6. Count:")
print(df['salary'].count())

print("\n7. Standard deviation:")
print(df['salary'].std())

print("\n8. Variance:")
print(df['salary'].var())

# Aggregation on entire DataFrame
print("\n9. Aggregate entire DataFrame (numeric columns only):")
print(df.sum())

print("\n10. Mean of all numeric columns:")
print(df.mean())

# describe() - summary statistics
print("\n11. Summary statistics (describe):")
print(df.describe())

# Multiple aggregations at once
print("\n12. Multiple aggregations using agg():")
print(df['salary'].agg(['sum', 'mean', 'min', 'max', 'std']))

# Custom aggregation function
print("\n13. Custom aggregation function:")
def salary_range(x):
    return x.max() - x.min()

print(df['salary'].agg(salary_range))

# Multiple functions including custom
print("\n14. Mix built-in and custom functions:")
print(df['salary'].agg(['mean', 'median', salary_range]))

# ============================================================================
# PART 2: BASIC GROUPBY
# ============================================================================
print("\n" + "=" * 80)
print("PART 2: BASIC GROUPBY")
print("=" * 80)

# Group by single column
print("\n1. Group by department:")
grouped = df.groupby('department')
print(type(grouped))  # DataFrameGroupBy object

# View groups
print("\n2. View groups:")
for name, group in grouped:
    print(f"\n{name}:")
    print(group)

# Get specific group
print("\n3. Get specific group (IT department):")
print(grouped.get_group('IT'))

# Count of rows per group
print("\n4. Count rows per group:")
print(grouped.size())

# Number of groups
print("\n5. Number of groups:")
print(grouped.ngroups)

# Group names
print("\n6. Group names:")
print(list(grouped.groups.keys()))

# ============================================================================
# PART 3: GROUPBY WITH AGGREGATION
# ============================================================================
print("\n" + "=" * 80)
print("PART 3: GROUPBY WITH AGGREGATION")
print("=" * 80)

# Single aggregation
print("\n1. Mean salary by department:")
print(df.groupby('department')['salary'].mean())

print("\n2. Sum of salaries by department:")
print(df.groupby('department')['salary'].sum())

print("\n3. Count employees by department:")
print(df.groupby('department')['employee'].count())

print("\n4. Max salary by department:")
print(df.groupby('department')['salary'].max())

print("\n5. Min age by department:")
print(df.groupby('department')['age'].min())

# Multiple columns aggregated
print("\n6. Mean of all numeric columns by department:")
print(df.groupby('department').mean())

print("\n7. Sum of all numeric columns by department:")
print(df.groupby('department').sum())

# Specific columns
print("\n8. Mean of salary and age by department:")
print(df.groupby('department')[['salary', 'age']].mean())

# ============================================================================
# PART 4: GROUPBY WITH agg()
# ============================================================================
print("\n" + "=" * 80)
print("PART 4: GROUPBY WITH agg()")
print("=" * 80)

# Single column, multiple aggregations
print("\n1. Multiple aggregations on salary:")
print(df.groupby('department')['salary'].agg(['mean', 'min', 'max', 'count']))

# Multiple columns, same aggregation
print("\n2. Mean of salary and age:")
print(df.groupby('department')[['salary', 'age']].agg('mean'))

# Different aggregations per column (dictionary)
print("\n3. Different aggregations per column:")
print(df.groupby('department').agg({
    'salary': ['mean', 'sum'],
    'age': 'mean',
    'experience': ['min', 'max'],
    'employee': 'count'
}))

# Rename aggregation columns
print("\n4. Rename aggregated columns:")
result = df.groupby('department').agg(
    avg_salary=('salary', 'mean'),
    total_salary=('salary', 'sum'),
    avg_age=('age', 'mean'),
    headcount=('employee', 'count')
)
print(result)

# Custom aggregation function
print("\n5. Custom aggregation function:")
def salary_range(x):
    return x.max() - x.min()

print(df.groupby('department')['salary'].agg(salary_range))

# Mix built-in and custom
print("\n6. Mix built-in and custom functions:")
print(df.groupby('department')['salary'].agg(['mean', 'median', salary_range]))

# Lambda functions
print("\n7. Lambda functions in agg():")
print(df.groupby('department')['salary'].agg([
    ('average', 'mean'),
    ('range', lambda x: x.max() - x.min()),
    ('top_salary', 'max')
]))

# ============================================================================
# PART 5: MULTIPLE GROUPBY COLUMNS
# ============================================================================
print("\n" + "=" * 80)
print("PART 5: MULTIPLE GROUPBY COLUMNS")
print("=" * 80)

# Add more data for better examples
df_multi = pd.DataFrame({
    'department': ['IT', 'IT', 'HR', 'HR', 'IT', 'HR', 'IT', 'HR'],
    'city': ['NY', 'London', 'NY', 'London', 'NY', 'NY', 'London', 'London'],
    'employee': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'salary': [60000, 65000, 50000, 52000, 68000, 55000, 63000, 51000]
})

print("\nDataFrame with multiple group columns:")
print(df_multi)

# Group by multiple columns
print("\n1. Group by department and city:")
print(df_multi.groupby(['department', 'city'])['salary'].mean())

print("\n2. Count by department and city:")
print(df_multi.groupby(['department', 'city']).size())

print("\n3. Multiple aggregations with multiple groups:")
print(df_multi.groupby(['department', 'city']).agg({
    'salary': ['mean', 'count'],
    'employee': 'count'
}))

# Unstack for better readability
print("\n4. Unstack for pivot table format:")
print(df_multi.groupby(['department', 'city'])['salary'].mean().unstack())

# Reset index to flatten
print("\n5. Reset index to regular DataFrame:")
result = df_multi.groupby(['department', 'city'])['salary'].mean().reset_index()
print(result)

# ============================================================================
# PART 6: TRANSFORM
# ============================================================================
print("\n" + "=" * 80)
print("PART 6: TRANSFORM")
print("=" * 80)

# transform keeps same shape as original DataFrame
print("\n1. Add department mean salary to each row:")
df['dept_avg_salary'] = df.groupby('department')['salary'].transform('mean')
print(df[['employee', 'department', 'salary', 'dept_avg_salary']])

print("\n2. Add department max salary:")
df['dept_max_salary'] = df.groupby('department')['salary'].transform('max')
print(df[['employee', 'department', 'salary', 'dept_max_salary']])

print("\n3. Standardize within group (z-score):")
df['salary_zscore'] = df.groupby('department')['salary'].transform(
    lambda x: (x - x.mean()) / x.std()
)
print(df[['employee', 'department', 'salary', 'salary_zscore']])

print("\n4. Difference from group mean:")
df['diff_from_dept_avg'] = df['salary'] - df.groupby('department')['salary'].transform('mean')
print(df[['employee', 'department', 'salary', 'diff_from_dept_avg']])

print("\n5. Ranking within group:")
df['dept_rank'] = df.groupby('department')['salary'].rank(ascending=False)
print(df[['employee', 'department', 'salary', 'dept_rank']])

# ============================================================================
# PART 7: FILTER
# ============================================================================
print("\n" + "=" * 80)
print("PART 7: FILTER")
print("=" * 80)

# Filter groups based on group properties
print("\n1. Departments with average salary > 60000:")
result = df.groupby('department').filter(lambda x: x['salary'].mean() > 60000)
print(result[['employee', 'department', 'salary']])

print("\n2. Departments with more than 2 employees:")
result = df.groupby('department').filter(lambda x: len(x) > 2)
print(result[['employee', 'department', 'salary']])

print("\n3. Departments with max salary > 70000:")
result = df.groupby('department').filter(lambda x: x['salary'].max() > 70000)
print(result[['employee', 'department', 'salary']])

# ============================================================================
# PART 8: APPLY
# ============================================================================
print("\n" + "=" * 80)
print("PART 8: APPLY")
print("=" * 80)

# apply allows custom function on each group
print("\n1. Top 2 salaries per department:")
def top_n(group, n=2):
    return group.nlargest(n, 'salary')

result = df.groupby('department').apply(top_n)
print(result[['employee', 'department', 'salary']])

print("\n2. Custom calculation per group:")
def salary_stats(group):
    return pd.Series({
        'count': len(group),
        'mean': group['salary'].mean(),
        'range': group['salary'].max() - group['salary'].min()
    })

print(df.groupby('department').apply(salary_stats))

print("\n3. Normalize salary within department:")
def normalize(group):
    group = group.copy()
    group['normalized_salary'] = (group['salary'] - group['salary'].min()) / (group['salary'].max() - group['salary'].min())
    return group

result = df.groupby('department').apply(normalize)
print(result[['employee', 'department', 'salary', 'normalized_salary']])

# ============================================================================
# PART 9: AGGREGATION SHORTCUTS
# ============================================================================
print("\n" + "=" * 80)
print("PART 9: AGGREGATION SHORTCUTS")
print("=" * 80)

# first() and last()
print("\n1. First employee per department:")
print(df.groupby('department').first())

print("\n2. Last employee per department:")
print(df.groupby('department').last())

# head() and tail()
print("\n3. First 2 rows per department:")
print(df.groupby('department').head(2)[['employee', 'department', 'salary']])

print("\n4. Last 2 rows per department:")
print(df.groupby('department').tail(2)[['employee', 'department', 'salary']])

# nth() - get nth row
print("\n5. Second employee per department:")
print(df.groupby('department').nth(1)[['employee', 'salary']])

# ============================================================================
# PART 10: PIVOT TABLE
# ============================================================================
print("\n" + "=" * 80)
print("PART 10: PIVOT TABLE")
print("=" * 80)

# pivot_table is similar to groupby with reshaping
print("\n1. Basic pivot table:")
pivot = pd.pivot_table(df, values='salary', index='department', aggfunc='mean')
print(pivot)

print("\n2. Multiple aggregations:")
pivot = pd.pivot_table(df, values='salary', index='department', 
                       aggfunc=['mean', 'min', 'max', 'count'])
print(pivot)

print("\n3. Multiple values:")
pivot = pd.pivot_table(df, values=['salary', 'age'], index='department', aggfunc='mean')
print(pivot)

# With columns parameter
df_pivot = pd.DataFrame({
    'department': ['IT', 'IT', 'HR', 'HR', 'IT', 'HR'],
    'city': ['NY', 'London', 'NY', 'London', 'NY', 'London'],
    'salary': [60000, 65000, 50000, 52000, 68000, 51000]
})

print("\n4. Pivot with columns:")
pivot = pd.pivot_table(df_pivot, values='salary', index='department', columns='city', aggfunc='mean')
print(pivot)

print("\n5. Pivot with margins (totals):")
pivot = pd.pivot_table(df_pivot, values='salary', index='department', columns='city', 
                       aggfunc='mean', margins=True, margins_name='Average')
print(pivot)

print("\n6. Fill missing values in pivot:")
pivot = pd.pivot_table(df_pivot, values='salary', index='department', columns='city', 
                       aggfunc='mean', fill_value=0)
print(pivot)

# ============================================================================
# PART 11: GROUPBY WITH DIFFERENT DATA TYPES
# ============================================================================
print("\n" + "=" * 80)
print("PART 11: GROUPBY WITH DIFFERENT DATA TYPES")
print("=" * 80)

# Grouping with dates
df_dates = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=10, freq='D'),
    'sales': [100, 150, 200, 175, 225, 300, 275, 350, 400, 375],
    'category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']
})

print("\nDataFrame with dates:")
print(df_dates)

print("\n1. Group by date component (month):")
df_dates['month'] = df_dates['date'].dt.month
print(df_dates.groupby('month')['sales'].sum())

print("\n2. Group by day of week:")
df_dates['day_name'] = df_dates['date'].dt.day_name()
print(df_dates.groupby('day_name')['sales'].mean())

# Groupby with categorical data
print("\n3. Group by category:")
print(df_dates.groupby('category')['sales'].agg(['sum', 'mean', 'count']))

# ============================================================================
# PART 12: ADVANCED GROUPBY OPERATIONS
# ============================================================================
print("\n" + "=" * 80)
print("PART 12: ADVANCED GROUPBY OPERATIONS")
print("=" * 80)

# Cumulative operations within groups
print("\n1. Cumulative sum within department:")
df['cumsum_salary'] = df.groupby('department')['salary'].cumsum()
print(df[['employee', 'department', 'salary', 'cumsum_salary']])

print("\n2. Cumulative count within department:")
df['employee_number'] = df.groupby('department').cumcount() + 1
print(df[['employee', 'department', 'employee_number']])

print("\n3. Shift within group:")
df['prev_salary'] = df.groupby('department')['salary'].shift(1)
print(df[['employee', 'department', 'salary', 'prev_salary']])

print("\n4. Percentage change within group:")
df['salary_pct_change'] = df.groupby('department')['salary'].pct_change()
print(df[['employee', 'department', 'salary', 'salary_pct_change']])

# Quantiles
print("\n5. Median (50th percentile) by department:")
print(df.groupby('department')['salary'].quantile(0.5))

print("\n6. Multiple quantiles:")
print(df.groupby('department')['salary'].quantile([0.25, 0.5, 0.75]))

# Unique values
print("\n7. Unique employees per department:")
print(df.groupby('department')['employee'].nunique())

# Value counts within groups
print("\n8. Salary distribution by department:")
for dept, group in df.groupby('department'):
    print(f"\n{dept}:")
    print(group['salary'].value_counts())

# ============================================================================
# PART 13: GROUPBY WITH INDEX
# ============================================================================
print("\n" + "=" * 80)
print("PART 13: GROUPBY WITH INDEX")
print("=" * 80)

# Set department as index
df_indexed = df.set_index('department')

print("\n1. Group by index:")
print(df_indexed.groupby(level=0)['salary'].mean())

# Multi-index groupby
df_multi_index = df.set_index(['department', 'employee'])

print("\n2. Group by first level of multi-index:")
print(df_multi_index.groupby(level=0)['salary'].mean())

print("\n3. Group by second level:")
print(df_multi_index.groupby(level=1)['salary'].sum())

# ============================================================================
# PART 14: COMBINING GROUPBY RESULTS
# ============================================================================
print("\n" + "=" * 80)
print("PART 14: COMBINING GROUPBY RESULTS")
print("=" * 80)

# Calculate and merge back
print("\n1. Add group statistics to original DataFrame:")
dept_stats = df.groupby('department')['salary'].agg(['mean', 'std']).reset_index()
dept_stats.columns = ['department', 'dept_mean', 'dept_std']
result = df.merge(dept_stats, on='department')
print(result[['employee', 'department', 'salary', 'dept_mean', 'dept_std']])

# Multiple groupby results
print("\n2. Combine multiple groupby results:")
salary_stats = df.groupby('department')['salary'].mean().reset_index()
salary_stats.columns = ['department', 'avg_salary']

age_stats = df.groupby('department')['age'].mean().reset_index()
age_stats.columns = ['department', 'avg_age']

result = salary_stats.merge(age_stats, on='department')
print(result)

# ============================================================================
# PART 15: GROUPBY WITH SORTING
# ============================================================================
print("\n" + "=" * 80)
print("PART 15: GROUPBY WITH SORTING")
print("=" * 80)

# Sort groups
print("\n1. Sort department names:")
print(df.groupby('department', sort=True)['salary'].mean())

print("\n2. Disable sorting for performance:")
print(df.groupby('department', sort=False)['salary'].mean())

# Sort aggregation results
print("\n3. Sort by aggregated value:")
result = df.groupby('department')['salary'].mean().sort_values(ascending=False)
print(result)

# Top N groups
print("\n4. Top 2 departments by average salary:")
print(df.groupby('department')['salary'].mean().nlargest(2))

print("\n5. Bottom 2 departments by average salary:")
print(df.groupby('department')['salary'].mean().nsmallest(2))

print("\n" + "=" * 80)
print("END OF AGGREGATION AND GROUPBY TUTORIAL")
print("=" * 80)