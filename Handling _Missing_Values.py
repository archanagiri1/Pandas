"""
Handling Missing Values
==========================================
detecting, removing, and filling missing values
"""

import pandas as pd
import numpy as np

print("=" * 80)
print("HANDLING MISSING VALUES IN PANDAS")
print("=" * 80)

# Sample DataFrame with missing values
df = pd.DataFrame({
    'name':       ['Alice', 'Bob', np.nan, 'David', 'Eve'],
    'age':        [25, np.nan, 35, np.nan, 32],
    'salary':     [50000, 60000, np.nan, 55000, np.nan],
    'department': ['HR', 'IT', 'Finance', np.nan, 'HR'],
    'score':      [8.5, np.nan, 7.8, 9.0, np.nan]
})

print("\nSample DataFrame:")
print(df)

# ============================================================================
# PART 1: DETECTING MISSING VALUES
# ============================================================================
print("\n" + "=" * 80)
print("PART 1: DETECTING MISSING VALUES")
print("=" * 80)

# isnull() - returns True where value is NaN
print("\n1. isnull() - boolean mask:")
print(df.isnull())

# notnull() - returns True where value is NOT NaN
print("\n2. notnull() - boolean mask:")
print(df.notnull())

# isna() - alias for isnull()
print("\n3. isna() - same as isnull():")
print(df.isna())

# Count missing per column
print("\n4. Count missing values per column:")
print(df.isnull().sum())

# Count missing per row
print("\n5. Count missing values per row:")
print(df.isnull().sum(axis=1))

# Total missing values
print("\n6. Total missing values:")
print(df.isnull().sum().sum())

# Percentage missing per column
print("\n7. Percentage missing per column:")
print((df.isnull().sum() / len(df)) * 100)

# Any missing in column
print("\n8. Any missing in each column:")
print(df.isnull().any())

# Any missing in row
print("\n9. Any missing in each row:")
print(df.isnull().any(axis=1))

# All missing in column
print("\n10. All values missing in each column:")
print(df.isnull().all())

# Show rows with any missing values
print("\n11. Rows that have at least one missing value:")
print(df[df.isnull().any(axis=1)])

# Show rows with no missing values
print("\n12. Rows with no missing values:")
print(df[df.notnull().all(axis=1)])

# ============================================================================
# PART 2: REMOVING MISSING VALUES
# ============================================================================
print("\n" + "=" * 80)
print("PART 2: REMOVING MISSING VALUES")
print("=" * 80)

df_drop = pd.DataFrame({
    'A': [1, np.nan, 3, np.nan, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, 2, 3, 4, 5],
    'D': [np.nan, np.nan, np.nan, np.nan, np.nan]
})

print("\nDataFrame for drop operations:")
print(df_drop)

# dropna() - drop rows with any NaN
print("\n1. Drop rows with ANY missing value:")
print(df_drop.dropna())

# how='all' - drop rows where ALL values are NaN
print("\n2. Drop rows where ALL values are missing:")
print(df_drop.dropna(how='all'))

# Drop columns with any NaN
print("\n3. Drop columns with ANY missing value:")
print(df_drop.dropna(axis=1))

# Drop columns where ALL are NaN
print("\n4. Drop columns where ALL values are missing:")
print(df_drop.dropna(axis=1, how='all'))

# thresh - keep rows with at least N non-NaN values
print("\n5. Keep rows with at least 3 non-NaN values:")
print(df_drop.dropna(thresh=3))

# subset - drop based on specific columns only
print("\n6. Drop rows where column 'A' or 'B' is missing:")
print(df_drop.dropna(subset=['A', 'B']))

# drop based on single column
print("\n7. Drop rows where column 'C' is missing:")
print(df_drop.dropna(subset=['C']))

# inplace
print("\n8. Drop inplace:")
df_copy = df_drop.copy()
df_copy.dropna(inplace=True)
print(df_copy)

# ============================================================================
# PART 3: FILLING MISSING VALUES
# ============================================================================
print("\n" + "=" * 80)
print("PART 3: FILLING MISSING VALUES")
print("=" * 80)

df_fill = pd.DataFrame({
    'A': [1, np.nan, 3, np.nan, 5],
    'B': [np.nan, 2, np.nan, 4, 5],
    'C': [1, 2, 3, 4, 5]
})

print("\nDataFrame for fill operations:")
print(df_fill)

# fillna() with constant
print("\n1. Fill all NaN with 0:")
print(df_fill.fillna(0))

# Fill with string
print("\n2. Fill NaN with string 'Missing':")
print(df.fillna('Missing'))

# Fill specific column
print("\n3. Fill specific column with value:")
df_temp = df_fill.copy()
df_temp['A'] = df_temp['A'].fillna(0)
print(df_temp)

# Fill with dictionary (different value per column)
print("\n4. Fill with different values per column:")
fill_values = {'A': 0, 'B': -1, 'C': 99}
print(df_fill.fillna(fill_values))

# Fill with mean
print("\n5. Fill with column mean:")
print(df_fill.fillna(df_fill.mean()))

# Fill with median
print("\n6. Fill with column median:")
print(df_fill.fillna(df_fill.median()))

# Fill with mode
print("\n7. Fill with column mode:")
df_mode = pd.DataFrame({
    'category': ['A', np.nan, 'B', 'A', np.nan, 'A'],
    'value': [1, 2, np.nan, 4, 5, np.nan]
})
df_mode['category'] = df_mode['category'].fillna(df_mode['category'].mode()[0])
df_mode['value'] = df_mode['value'].fillna(df_mode['value'].mode()[0])
print(df_mode)

# Forward fill (ffill) - fill with previous value
print("\n8. Forward fill (ffill) - use previous value:")
print(df_fill.fillna(method='ffill'))

# Backward fill (bfill) - fill with next value
print("\n9. Backward fill (bfill) - use next value:")
print(df_fill.fillna(method='bfill'))

# Using ffill() method directly
print("\n10. Using ffill() directly:")
print(df_fill.ffill())

# Using bfill() method directly
print("\n11. Using bfill() directly:")
print(df_fill.bfill())

# Limit fills
print("\n12. Forward fill with limit=1 (fill only 1 consecutive NaN):")
df_limit = pd.DataFrame({
    'A': [1, np.nan, np.nan, np.nan, 5]
})
print(df_limit.fillna(method='ffill', limit=1))

# Fill with grouped mean (group-wise imputation)
df_grouped = pd.DataFrame({
    'dept': ['IT', 'IT', 'HR', 'HR', 'IT'],
    'salary': [60000, np.nan, 50000, np.nan, 70000]
})

print("\n13. Fill with group mean (by department):")
df_grouped['salary'] = df_grouped.groupby('dept')['salary'].transform(
    lambda x: x.fillna(x.mean())
)
print(df_grouped)

# ============================================================================
# PART 4: INTERPOLATING MISSING VALUES
# ============================================================================
print("\n" + "=" * 80)
print("PART 4: INTERPOLATING MISSING VALUES")
print("=" * 80)

df_interp = pd.DataFrame({
    'A': [1, np.nan, np.nan, 4, 5],
    'B': [10, np.nan, 30, np.nan, 50]
})

print("\nDataFrame for interpolation:")
print(df_interp)

# Linear interpolation (default)
print("\n1. Linear interpolation:")
print(df_interp.interpolate())

# Forward fill interpolation
print("\n2. Forward fill interpolation (method='pad'):")
print(df_interp.interpolate(method='pad'))

# Backward fill interpolation
print("\n3. Backward fill interpolation (method='backfill'):")
print(df_interp.interpolate(method='backfill'))

# Polynomial interpolation
print("\n4. Polynomial interpolation:")
print(df_interp.interpolate(method='polynomial', order=2))

# Limit interpolation
print("\n5. Limit to filling 1 consecutive NaN:")
print(df_interp.interpolate(limit=1))

# Limit direction
print("\n6. Interpolate from forward direction only:")
print(df_interp.interpolate(limit_direction='forward'))

# Time-based interpolation
df_time = pd.DataFrame({
    'value': [1.0, np.nan, np.nan, 4.0, 5.0]
}, index=pd.date_range('2024-01-01', periods=5, freq='D'))

print("\n7. Time-based interpolation:")
print(df_time.interpolate(method='time'))

# ============================================================================
# PART 5: REPLACING VALUES
# ============================================================================
print("\n" + "=" * 80)
print("PART 5: REPLACING VALUES")
print("=" * 80)

df_replace = pd.DataFrame({
    'A': [1, 0, 3, -999, 5],
    'B': ['yes', 'no', 'n/a', 'yes', 'none'],
    'C': [10, 20, 999, 40, 50]
})

print("\nDataFrame for replace operations:")
print(df_replace)

# Replace single value
print("\n1. Replace single value:")
print(df_replace.replace(-999, np.nan))

# Replace multiple values
print("\n2. Replace multiple values with NaN:")
print(df_replace.replace([-999, 999, 0], np.nan))

# Replace strings
print("\n3. Replace string values:")
print(df_replace.replace({'n/a': np.nan, 'none': np.nan}))

# Replace per column
print("\n4. Replace different values per column:")
print(df_replace.replace({'A': {0: np.nan}, 'C': {999: np.nan}}))

# Replace with regex
print("\n5. Replace with regex:")
print(df_replace.replace(r'^n', np.nan, regex=True))

# Using where() to replace conditionally
print("\n6. Replace values below 0 with NaN using where:")
df_temp = df_replace.copy()
df_temp['A'] = df_temp['A'].where(df_temp['A'] > 0)
print(df_temp)

# Using mask() - opposite of where()
print("\n7. Replace values below 0 with NaN using mask:")
df_temp = df_replace.copy()
df_temp['A'] = df_temp['A'].mask(df_temp['A'] <= 0)
print(df_temp)

# ============================================================================
# PART 6: CHECKING AFTER HANDLING
# ============================================================================
print("\n" + "=" * 80)
print("PART 6: CHECKING AFTER HANDLING")
print("=" * 80)

df_original = pd.DataFrame({
    'A': [1, np.nan, 3, np.nan, 5],
    'B': [np.nan, 2, 3, np.nan, 5]
})

print("\nOriginal:")
print(df_original)
print("Missing:", df_original.isnull().sum().sum())

# After filling
df_filled = df_original.fillna(0)
print("\nAfter fillna(0):")
print(df_filled)
print("Missing:", df_filled.isnull().sum().sum())

# After dropping
df_dropped = df_original.dropna()
print("\nAfter dropna():")
print(df_dropped)
print("Missing:", df_dropped.isnull().sum().sum())

# Verify no missing values remain
print("\nVerify no missing values:")
print(df_filled.isnull().any().any())  # False = no missing

# Info to check dtypes and non-null counts
print("\nDataFrame info after handling:")
df_filled.info()

print("\n" + "=" * 80)
print(" MISSING VALUES")
print("=" * 80)