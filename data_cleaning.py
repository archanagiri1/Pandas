"""
Data Cleaning
================================
cleaning and preparing data
"""

import pandas as pd
import numpy as np
import re

print("=" * 80)
print("DATA CLEANING IN PANDAS")
print("=" * 80)

# ============================================================================
# PART 1: HANDLING DUPLICATES
# ============================================================================
print("\n" + "=" * 80)
print("PART 1: HANDLING DUPLICATES")
print("=" * 80)

# Sample data with duplicates
df_dup = pd.DataFrame({
    'id': [1, 2, 2, 3, 3, 4, 5, 5],
    'name': ['Alice', 'Bob', 'Bob', 'Charlie', 'Charlie', 'David', 'Eve', 'Eve'],
    'age': [25, 30, 30, 35, 35, 28, 32, 32],
    'salary': [50000, 60000, 60000, 75000, 70000, 55000, 65000, 65000]
})

print("\nData with duplicates:")
print(df_dup)

# Check for duplicates
print("\n1. Check for duplicate rows:")
print(df_dup.duplicated())

# Count duplicates
print("\n2. Count duplicate rows:")
print(f"Number of duplicates: {df_dup.duplicated().sum()}")

# Show duplicate rows
print("\n3. Show all duplicate rows (including first occurrence):")
print(df_dup[df_dup.duplicated(keep=False)])

# Drop duplicates (keep first)
print("\n4. Drop duplicates (keep first occurrence):")
print(df_dup.drop_duplicates())

# Drop duplicates (keep last)
print("\n5. Drop duplicates (keep last occurrence):")
print(df_dup.drop_duplicates(keep='last'))

# Drop all duplicates
print("\n6. Drop all duplicate occurrences:")
print(df_dup.drop_duplicates(keep=False))

# Check duplicates on specific columns
print("\n7. Check duplicates based on specific columns:")
print(df_dup.duplicated(subset=['name', 'age']))

# Drop duplicates based on specific columns
print("\n8. Drop duplicates based on 'name' column only:")
print(df_dup.drop_duplicates(subset=['name']))

# Drop duplicates inplace
print("\n9. Drop duplicates inplace:")
df_temp = df_dup.copy()
df_temp.drop_duplicates(inplace=True)
print(df_temp)


# ============================================================================
# PART 2: HANDLING OUTLIERS
# ============================================================================
print("\n" + "=" * 80)
print("PART 2: HANDLING OUTLIERS")
print("=" * 80)

# Data with outliers
df_outliers = pd.DataFrame({
    'value': [10, 12, 11, 13, 12, 100, 11, 14, 13, 200, 12]
})

print("\nData with outliers:")
print(df_outliers)

# Statistical summary
print("\n1. Statistical summary:")
print(df_outliers.describe())

# IQR method
print("\n2. Detect outliers using IQR method:")
Q1 = df_outliers['value'].quantile(0.25)
Q3 = df_outliers['value'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"Lower bound: {lower_bound}")
print(f"Upper bound: {upper_bound}")

outliers = df_outliers[(df_outliers['value'] < lower_bound) | 
                       (df_outliers['value'] > upper_bound)]
print("\nOutliers:")
print(outliers)

# Remove outliers
print("\n3. Remove outliers:")
df_clean = df_outliers[(df_outliers['value'] >= lower_bound) & 
                       (df_outliers['value'] <= upper_bound)]
print(df_clean)

# Z-score method
print("\n4. Detect outliers using Z-score:")
mean = df_outliers['value'].mean()
std = df_outliers['value'].std()
df_outliers['z_score'] = (df_outliers['value'] - mean) / std

outliers_z = df_outliers[abs(df_outliers['z_score']) > 2]
print("\nOutliers (|z-score| > 2):")
print(outliers_z)

# Cap outliers
print("\n5. Cap outliers at bounds:")
df_capped = df_outliers.copy()
df_capped['value'] = df_capped['value'].clip(lower=lower_bound, upper=upper_bound)
print(df_capped)

# Replace outliers with median
print("\n6. Replace outliers with median:")
df_replaced = df_outliers.copy()
median = df_replaced['value'].median()
df_replaced.loc[(df_replaced['value'] < lower_bound) | 
                (df_replaced['value'] > upper_bound), 'value'] = median
print(df_replaced)

# ============================================================================
# PART 3: DATA TYPE CONVERSION
# ============================================================================
print("\n" + "=" * 80)
print("PART 3: DATA TYPE CONVERSION")
print("=" * 80)

# Sample data with wrong types
df_types = pd.DataFrame({
    'id': ['1', '2', '3', '4', '5'],
    'age': ['25', '30', '35', '28', '32'],
    'salary': ['50000', '60000', '75000', '55000', '70000'],
    'date': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01']
})

print("\nOriginal data types:")
print(df_types.dtypes)
print("\nData:")
print(df_types)

# Convert to numeric
print("\n1. Convert to numeric:")
df_types['id'] = pd.to_numeric(df_types['id'])
df_types['age'] = pd.to_numeric(df_types['age'])
df_types['salary'] = pd.to_numeric(df_types['salary'])
print(df_types.dtypes)

# Convert to datetime
print("\n2. Convert to datetime:")
df_types['date'] = pd.to_datetime(df_types['date'])
print(df_types.dtypes)

# Handle conversion errors
df_errors = pd.DataFrame({
    'value': ['1', '2', 'three', '4', 'five']
})

print("\n3. Handle conversion errors (coerce):")
df_errors['value_numeric'] = pd.to_numeric(df_errors['value'], errors='coerce')
print(df_errors)

# Convert to category
df_cat = pd.DataFrame({
    'department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT']
})

print("\n4. Convert to category:")
print(f"Before: {df_cat['department'].dtype}")
df_cat['department'] = df_cat['department'].astype('category')
print(f"After: {df_cat['department'].dtype}")
print(f"Memory saved: {df_cat.memory_usage(deep=True).sum()} bytes")

# ============================================================================
# PART 4: STRING CLEANING
# ============================================================================
print("\n" + "=" * 80)
print("PART 4: STRING CLEANING")
print("=" * 80)

# Data with messy strings
df_str = pd.DataFrame({
    'name': ['  Alice  ', 'BOB', 'charlie  ', '  DAVID', 'eve'],
    'email': ['alice@email.com', 'BOB@EMAIL.COM', 'charlie@email.com', 
              'david@email.com', 'eve@email.com'],
    'phone': ['123-456-7890', '(234) 567-8901', '345.678.9012', 
              '456 567 8901', '5678901234']
})

print("\nMessy string data:")
print(df_str)

# Strip whitespace
print("\n1. Strip whitespace:")
df_str['name'] = df_str['name'].str.strip()
print(df_str['name'])

# Convert case
print("\n2. Convert to lowercase:")
df_str['email'] = df_str['email'].str.lower()
print(df_str['email'])

print("\n3. Convert to title case:")
df_str['name'] = df_str['name'].str.title()
print(df_str['name'])

print("\n4. Convert to uppercase:")
df_str['name_upper'] = df_str['name'].str.upper()
print(df_str['name_upper'])

# Remove special characters
print("\n5. Remove special characters from phone:")
df_str['phone_clean'] = df_str['phone'].str.replace(r'[^0-9]', '', regex=True)
print(df_str[['phone', 'phone_clean']])

# Replace values
print("\n6. Replace substring:")
df_replace = pd.DataFrame({
    'text': ['hello world', 'world hello', 'hello']
})
df_replace['text'] = df_replace['text'].str.replace('hello', 'hi')
print(df_replace)

# Extract patterns
print("\n7. Extract email domain:")
df_str['domain'] = df_str['email'].str.extract(r'@(.+)')
print(df_str[['email', 'domain']])

# Split strings
print("\n8. Split name into first and last:")
df_names = pd.DataFrame({
    'full_name': ['Alice Smith', 'Bob Jones', 'Charlie Brown']
})
df_names[['first_name', 'last_name']] = df_names['full_name'].str.split(' ', expand=True)
print(df_names)

# ============================================================================
# PART 5: HANDLING INCONSISTENT VALUES
# ============================================================================
print("\n" + "=" * 80)
print("PART 5: HANDLING INCONSISTENT VALUES")
print("=" * 80)

# Data with inconsistencies
df_inconsistent = pd.DataFrame({
    'status': ['active', 'Active', 'ACTIVE', 'inactive', 'Inactive', 'INACTIVE'],
    'gender': ['M', 'Male', 'male', 'F', 'Female', 'female'],
    'country': ['USA', 'US', 'United States', 'UK', 'United Kingdom', 'GB']
})

print("\nInconsistent data:")
print(df_inconsistent)

# Standardize values
print("\n1. Standardize status values:")
df_inconsistent['status'] = df_inconsistent['status'].str.lower()
print(df_inconsistent['status'])

# Map to standard values
print("\n2. Map gender to standard values:")
gender_map = {
    'M': 'Male', 'Male': 'Male', 'male': 'Male',
    'F': 'Female', 'Female': 'Female', 'female': 'Female'
}
df_inconsistent['gender'] = df_inconsistent['gender'].map(gender_map)
print(df_inconsistent['gender'])

# Replace multiple values
print("\n3. Standardize country codes:")
country_map = {
    'US': 'USA',
    'United States': 'USA',
    'United Kingdom': 'UK',
    'GB': 'UK'
}
df_inconsistent['country'] = df_inconsistent['country'].replace(country_map)
print(df_inconsistent['country'])

# ============================================================================
# PART 6: REMOVING UNWANTED CHARACTERS
# ============================================================================
print("\n" + "=" * 80)
print("PART 6: REMOVING UNWANTED CHARACTERS")
print("=" * 80)

# Data with unwanted characters
df_unwanted = pd.DataFrame({
    'price': ['$100', '$200', '$300'],
    'percentage': ['50%', '75%', '90%'],
    'code': ['ABC-123', 'DEF-456', 'GHI-789']
})

print("\nData with unwanted characters:")
print(df_unwanted)

# Remove currency symbol
print("\n1. Remove $ symbol:")
df_unwanted['price_clean'] = df_unwanted['price'].str.replace('$', '', regex=False)
print(df_unwanted[['price', 'price_clean']])

# Remove percentage symbol and convert
print("\n2. Remove % and convert to numeric:")
df_unwanted['percentage_clean'] = df_unwanted['percentage'].str.replace('%', '', regex=False).astype(float)
print(df_unwanted[['percentage', 'percentage_clean']])

# Remove hyphens
print("\n3. Remove hyphens:")
df_unwanted['code_clean'] = df_unwanted['code'].str.replace('-', '', regex=False)
print(df_unwanted[['code', 'code_clean']])

# Remove all non-alphanumeric
print("\n4. Remove all non-alphanumeric:")
df_special = pd.DataFrame({
    'text': ['hello@123', 'world#456', 'test!789']
})
df_special['text_clean'] = df_special['text'].str.replace(r'[^a-zA-Z0-9]', '', regex=True)
print(df_special)

# ============================================================================
# PART 7: RENAMING COLUMNS
# ============================================================================
print("\n" + "=" * 80)
print("PART 7: RENAMING COLUMNS")
print("=" * 80)

# Data with messy column names
df_cols = pd.DataFrame({
    'First Name': ['Alice', 'Bob'],
    'Last Name': ['Smith', 'Jones'],
    'Email Address': ['alice@email.com', 'bob@email.com'],
    'Phone Number': ['123-456-7890', '234-567-8901']
})

print("\nOriginal column names:")
print(df_cols.columns.tolist())

# Rename specific columns
print("\n1. Rename specific columns:")
df_cols_renamed = df_cols.rename(columns={
    'First Name': 'first_name',
    'Last Name': 'last_name'
})
print(df_cols_renamed.columns.tolist())

# Rename all columns
print("\n2. Rename all columns:")
df_cols.columns = ['first_name', 'last_name', 'email', 'phone']
print(df_cols.columns.tolist())

# Clean column names (lowercase and replace spaces)
print("\n3. Clean column names (lowercase, replace spaces):")
df_messy_cols = pd.DataFrame({
    'First Name': [1, 2],
    'LAST NAME': [3, 4],
    'Email Address': [5, 6]
})
df_messy_cols.columns = df_messy_cols.columns.str.lower().str.replace(' ', '_')
print(df_messy_cols.columns.tolist())

# Remove special characters from column names
print("\n4. Remove special characters:")
df_special_cols = pd.DataFrame({
    'col@1': [1, 2],
    'col#2': [3, 4],
    'col$3': [5, 6]
})
df_special_cols.columns = df_special_cols.columns.str.replace(r'[^a-zA-Z0-9_]', '', regex=True)
print(df_special_cols.columns.tolist())

# ============================================================================
# PART 8: HANDLING WHITESPACE
# ============================================================================
print("\n" + "=" * 80)
print("PART 8: HANDLING WHITESPACE")
print("=" * 80)

# Data with whitespace issues
df_space = pd.DataFrame({
    'name': ['  Alice  ', 'Bob   ', '   Charlie', 'David'],
    'city': ['New  York', 'Los   Angeles', 'Chicago', 'Boston  ']
})

print("\nData with whitespace:")
print(df_space)
print("\nWith repr to see spaces:")
print(repr(df_space['name'].iloc[0]))

# Strip leading/trailing spaces
print("\n1. Strip leading/trailing spaces:")
df_space['name'] = df_space['name'].str.strip()
print(df_space['name'])

# Remove extra internal spaces
print("\n2. Remove extra internal spaces:")
df_space['city'] = df_space['city'].str.replace(r'\s+', ' ', regex=True)
print(df_space['city'])

# Strip and normalize in one step
print("\n3. Strip and normalize all string columns:")
for col in df_space.select_dtypes(include=['object']).columns:
    df_space[col] = df_space[col].str.strip().str.replace(r'\s+', ' ', regex=True)
print(df_space)

# ============================================================================
# PART 9: STANDARDIZING DATE FORMATS
# ============================================================================
print("\n" + "=" * 80)
print("PART 9: STANDARDIZING DATE FORMATS")
print("=" * 80)

# Data with different date formats
df_dates = pd.DataFrame({
    'date1': ['01/15/2024', '02/20/2024', '03/25/2024'],
    'date2': ['2024-01-15', '2024-02-20', '2024-03-25'],
    'date3': ['15-Jan-2024', '20-Feb-2024', '25-Mar-2024']
})

print("\nDifferent date formats:")
print(df_dates)

# Convert to datetime
print("\n1. Convert all to datetime:")
df_dates['date1'] = pd.to_datetime(df_dates['date1'], format='%m/%d/%Y')
df_dates['date2'] = pd.to_datetime(df_dates['date2'], format='%Y-%m-%d')
df_dates['date3'] = pd.to_datetime(df_dates['date3'], format='%d-%b-%Y')
print(df_dates)
print("\nData types:")
print(df_dates.dtypes)

# Standardize format
print("\n2. Standardize to same format:")
df_dates['date1_str'] = df_dates['date1'].dt.strftime('%Y-%m-%d')
df_dates['date2_str'] = df_dates['date2'].dt.strftime('%Y-%m-%d')
df_dates['date3_str'] = df_dates['date3'].dt.strftime('%Y-%m-%d')
print(df_dates[['date1_str', 'date2_str', 'date3_str']])

# ============================================================================
# PART 10: VALIDATING DATA
# ============================================================================
print("\n" + "=" * 80)
print("PART 10: VALIDATING DATA")
print("=" * 80)

# Sample data for validation
df_validate = pd.DataFrame({
    'email': ['alice@email.com', 'bob@email', 'charlie@email.com', 'invalid'],
    'age': [25, -5, 150, 30],
    'salary': [50000, 60000, -10000, 75000],
    'phone': ['123-456-7890', '123456', '234-567-8901', '345-678-9012']
})

print("\nData to validate:")
print(df_validate)

# Validate email format
print("\n1. Validate email format:")
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
df_validate['valid_email'] = df_validate['email'].str.match(email_pattern)
print(df_validate[['email', 'valid_email']])

# Validate age range
print("\n2. Validate age (must be 0-120):")
df_validate['valid_age'] = df_validate['age'].between(0, 120)
print(df_validate[['age', 'valid_age']])

# Validate salary (positive)
print("\n3. Validate salary (must be positive):")
df_validate['valid_salary'] = df_validate['salary'] > 0
print(df_validate[['salary', 'valid_salary']])

# Validate phone format
print("\n4. Validate phone format (XXX-XXX-XXXX):")
phone_pattern = r'^\d{3}-\d{3}-\d{4}$'
df_validate['valid_phone'] = df_validate['phone'].str.match(phone_pattern)
print(df_validate[['phone', 'valid_phone']])

# Flag invalid rows
print("\n5. Flag rows with any invalid data:")
df_validate['all_valid'] = (df_validate['valid_email'] & 
                            df_validate['valid_age'] & 
                            df_validate['valid_salary'] & 
                            df_validate['valid_phone'])
print(df_validate[['email', 'age', 'salary', 'phone', 'all_valid']])

# ============================================================================
# PART 11: HANDLING SPECIAL VALUES
# ============================================================================
print("\n" + "=" * 80)
print("PART 11: HANDLING SPECIAL VALUES")
print("=" * 80)

# Data with special values
df_special = pd.DataFrame({
    'value': [1, 2, -999, 4, 5, -999, 7, 999, 9],
    'status': ['active', 'N/A', 'inactive', 'n/a', 'active', 'none', 'NA', 'active', 'inactive']
})

print("\nData with special values:")
print(df_special)

# Replace sentinel values with NaN
print("\n1. Replace -999 and 999 with NaN:")
df_special['value'] = df_special['value'].replace([-999, 999], np.nan)
print(df_special['value'])

# Replace various NA indicators
print("\n2. Replace various NA indicators:")
na_values = ['N/A', 'n/a', 'none', 'NA', 'null', 'NULL']
df_special['status'] = df_special['status'].replace(na_values, np.nan)
print(df_special['status'])

# ============================================================================
# PART 12: COMPLETE CLEANING PIPELINE
# ============================================================================
print("\n" + "=" * 80)
print("PART 12: COMPLETE CLEANING PIPELINE")
print("=" * 80)

# Messy dataset
df_messy = pd.DataFrame({
    'Employee ID': ['  001  ', '002', '002', '003', '004'],
    'Full Name': ['  ALICE SMITH  ', 'bob jones', 'bob jones', 'Charlie Brown  ', 'david wilson'],
    'Email Address': ['ALICE@EMAIL.COM', 'bob@email.com', 'bob@email.com', 'charlie@email', 'david@email.com'],
    'Age': ['25', '-5', '30', '35', '150'],
    'Salary': ['$50,000', '$60,000', '$60,000', '$75,000', '$-10,000'],
    'Hire Date': ['01/15/2020', '02/20/2021', '02/20/2021', '03/25/2019', '04/30/2022']
})

print("\nMessy dataset:")
print(df_messy)

print("\nCleaning pipeline:")

# 1. Clean column names
print("\n1. Clean column names:")
df_clean = df_messy.copy()
df_clean.columns = df_clean.columns.str.lower().str.replace(' ', '_')
print(f"Columns: {df_clean.columns.tolist()}")

# 2. Remove duplicates
print("\n2. Remove duplicates:")
print(f"Before: {len(df_clean)} rows")
df_clean = df_clean.drop_duplicates()
print(f"After: {len(df_clean)} rows")

# 3. Clean string columns
print("\n3. Clean string columns:")
df_clean['employee_id'] = df_clean['employee_id'].str.strip()
df_clean['full_name'] = df_clean['full_name'].str.strip().str.title()
df_clean['email_address'] = df_clean['email_address'].str.strip().str.lower()

# 4. Clean salary (remove $ and ,)
print("\n4. Clean salary:")
df_clean['salary'] = df_clean['salary'].str.replace('$', '', regex=False)
df_clean['salary'] = df_clean['salary'].str.replace(',', '', regex=False)
df_clean['salary'] = pd.to_numeric(df_clean['salary'], errors='coerce')

# 5. Convert age to numeric
print("\n5. Convert age to numeric:")
df_clean['age'] = pd.to_numeric(df_clean['age'], errors='coerce')

# 6. Convert hire_date to datetime
print("\n6. Convert hire_date:")
df_clean['hire_date'] = pd.to_datetime(df_clean['hire_date'], format='%m/%d/%Y')

# 7. Validate age range
print("\n7. Validate and clean age:")
df_clean.loc[~df_clean['age'].between(18, 100), 'age'] = np.nan

# 8. Validate salary (must be positive)
print("\n8. Validate and clean salary:")
df_clean.loc[df_clean['salary'] < 0, 'salary'] = np.nan

# 9. Validate email
print("\n9. Validate email:")
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
invalid_emails = ~df_clean['email_address'].str.match(email_pattern)
df_clean.loc[invalid_emails, 'email_address'] = np.nan

# 10. Final result
print("\n10. Final cleaned dataset:")
print(df_clean)
print("\nData types:")
print(df_clean.dtypes)
print("\nMissing values:")
print(df_clean.isnull().sum())

# ============================================================================
# PART 13: DATA QUALITY REPORT
# ============================================================================
print("\n" + "=" * 80)
print("PART 13: DATA QUALITY REPORT")
print("=" * 80)

def data_quality_report(df):
    """Generate comprehensive data quality report"""
    
    report = pd.DataFrame({
        'column': df.columns,
        'dtype': df.dtypes.values,
        'non_null': df.count().values,
        'null_count': df.isnull().sum().values,
        'null_pct': (df.isnull().sum() / len(df) * 100).values,
        'unique': df.nunique().values,
        'duplicates': (df.duplicated().sum() if df.columns.tolist() else 0)
    })
    
    return report

print("\n1. Data quality report before cleaning:")
print(data_quality_report(df_messy))

print("\n2. Data quality report after cleaning:")
print(data_quality_report(df_clean))

print("\n" + "=" * 80)
print(" DATA CLEANING ")
print("=" * 80)