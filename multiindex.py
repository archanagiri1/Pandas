"""
 MultiIndex / Hierarchical Indexing
=====================================================
"""

import pandas as pd
import numpy as np

print("=" * 80)
print("MULTIINDEX / HIERARCHICAL INDEXING")
print("=" * 80)

"""
WHAT IS MULTIINDEX?
===================
- Multiple levels of row or column indices
- Like organizing data in nested categories
- Example: Year → Quarter → Month (3 levels)

WHY USE MULTIINDEX?
===================
- Organize complex data hierarchically
- Group related information
- Efficient storage and querying
- Represent multi-dimensional data
"""

# ============================================================================
# PART 1: CREATING MULTIINDEX
# ============================================================================
print("\n" + "=" * 80)
print("PART 1: CREATING MULTIINDEX")
print("=" * 80)

# Method 1: From tuples
print("\n1. Create MultiIndex from tuples:")
index = pd.MultiIndex.from_tuples([
    ('USA', 'NY'),
    ('USA', 'CA'),
    ('UK', 'London'),
    ('UK', 'Manchester')
], names=['Country', 'City'])

df = pd.DataFrame({'Sales': [100, 200, 150, 175]}, index=index)
print(df)

# Method 2: From arrays
print("\n2. Create MultiIndex from arrays:")
countries = ['USA', 'USA', 'UK', 'UK']
cities = ['NY', 'CA', 'London', 'Manchester']
index = pd.MultiIndex.from_arrays([countries, cities], names=['Country', 'City'])
df = pd.DataFrame({'Sales': [100, 200, 150, 175]}, index=index)
print(df)

# Method 3: From product (cartesian product)
print("\n3. Create MultiIndex from product:")
index = pd.MultiIndex.from_product([['2023', '2024'], ['Q1', 'Q2']], 
                                    names=['Year', 'Quarter'])
df = pd.DataFrame({'Revenue': [100, 150, 200, 250]}, index=index)
print(df)

# Method 4: Set existing columns as index
print("\n4. Set columns as MultiIndex:")
df = pd.DataFrame({
    'Country': ['USA', 'USA', 'UK'],
    'City': ['NY', 'CA', 'London'],
    'Sales': [100, 200, 150]
})
df = df.set_index(['Country', 'City'])
print(df)

# ============================================================================
# PART 2: ACCESSING DATA
# ============================================================================
print("\n" + "=" * 80)
print("PART 2: ACCESSING DATA")
print("=" * 80)

# Select outer level
print("\n1. Select by outer level:")
print(df.loc['USA'])

# Select specific combination
print("\n2. Select specific combination:")
print(df.loc[('USA', 'NY')])

# Cross-section (xs)
print("\n3. Cross-section - select by level:")
print(df.xs('NY', level='City'))

# Slice
print("\n4. Slice by level:")
print(df.loc[('USA', 'CA'):('UK', 'London')])

# ============================================================================
# PART 3: MULTIINDEX COLUMNS
# ============================================================================
print("\n" + "=" * 80)
print("PART 3: MULTIINDEX COLUMNS")
print("=" * 80)

# Create MultiIndex for columns
columns = pd.MultiIndex.from_tuples([
    ('Sales', '2023'),
    ('Sales', '2024'),
    ('Profit', '2023'),
    ('Profit', '2024')
])

df_cols = pd.DataFrame(
    [[100, 120, 20, 25],
     [200, 220, 40, 45]],
    index=['Product A', 'Product B'],
    columns=columns
)

print("\nMultiIndex columns:")
print(df_cols)

# Access columns
print("\n1. Access all Sales:")
print(df_cols['Sales'])

print("\n2. Access specific column:")
print(df_cols[('Sales', '2023')])

# ============================================================================
# PART 4: RESHAPING MULTIINDEX
# ============================================================================
print("\n" + "=" * 80)
print("PART 4: RESHAPING MULTIINDEX")
print("=" * 80)

# Stack - columns to rows
print("\n1. Stack (columns → rows):")
stacked = df_cols.stack()
print(stacked)

# Unstack - rows to columns
print("\n2. Unstack (rows → columns):")
unstacked = stacked.unstack()
print(unstacked)

# Reset index
print("\n3. Reset index (flatten):")
df_reset = df.reset_index()
print(df_reset)

# ============================================================================
# PART 5: SORTING MULTIINDEX
# ============================================================================
print("\n" + "=" * 80)
print("PART 5: SORTING MULTIINDEX")
print("=" * 80)

# Sort by index
print("\n1. Sort by index:")
print(df.sort_index())

# Sort by specific level
print("\n2. Sort by level:")
print(df.sort_index(level='City'))

# ============================================================================
# PART 6: AGGREGATING MULTIINDEX
# ============================================================================
print("\n" + "=" * 80)
print("PART 6: AGGREGATING MULTIINDEX")
print("=" * 80)

# Sum by level
print("\n1. Sum by outer level:")
print(df.sum(level='Country'))

# Mean by level
print("\n2. Mean by level:")
print(df.mean(level='Country'))

# ============================================================================
# PART 7: SWAPPING AND REORDERING LEVELS
# ============================================================================
print("\n" + "=" * 80)
print("PART 7: SWAPPING AND REORDERING LEVELS")
print("=" * 80)

# Swap levels
print("\n1. Swap levels:")
swapped = df.swaplevel('Country', 'City')
print(swapped)

# Reorder levels
print("\n2. Reorder levels:")
reordered = df.reorder_levels(['City', 'Country'])
print(reordered)

# ============================================================================
# COMMON OPERATIONS
# ============================================================================
print("\n" + "=" * 80)
print("COMMON OPERATIONS")
print("=" * 80)

print("""
CREATING:
---------
pd.MultiIndex.from_tuples([(a,b), (c,d)])
pd.MultiIndex.from_arrays([[a,c], [b,d]])
pd.MultiIndex.from_product([[a,b], [c,d]])
df.set_index(['col1', 'col2'])

ACCESSING:
----------
df.loc['level1']                  # Outer level
df.loc[('level1', 'level2')]      # Specific combination
df.xs('value', level='name')      # Cross-section

RESHAPING:
----------
df.stack()                        # Columns to rows
df.unstack()                      # Rows to columns
df.reset_index()                  # Flatten

SORTING:
--------
df.sort_index()                   # Sort all levels
df.sort_index(level='name')       # Sort by level

AGGREGATING:
------------
df.sum(level='name')              # Sum by level
df.mean(level=0)                  # Mean by level number

MANIPULATING:
-------------
df.swaplevel()                    # Swap levels
df.reorder_levels([1, 0])         # Reorder levels
df.droplevel('name')              # Drop level
""")

print("\n" + "=" * 80)
print(" MULTIINDEX")
print("=" * 80)