"""
Import & Export CSV Files
============================================
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

print("=" * 80)
print("PANDAS CSV IMPORT & EXPORT - COMPLETE GUIDE")
print("=" * 80)

# ============================================================================
# WHAT IS A CSV FILE?
# ============================================================================
"""
CSV (Comma-Separated Values):
==============================

Definition:
- Plain text file format
- Each line represents a row
- Values separated by commas (or other delimiters)
- First row usually contains column headers

Example CSV structure:
----------------------
name,age,city,salary
Alice,25,New York,50000
Bob,30,London,60000
Charlie,35,Paris,75000

Advantages:
- Universal format (works everywhere)
- Human-readable
- Lightweight
- Easy to create and edit
- Supported by all spreadsheet software

Disadvantages:
- No data type preservation
- No formatting (colors, fonts)
- Cannot store multiple sheets
- Large file size for big datasets
- Special characters need escaping
"""

# ============================================================================
# PART 1: EXPORTING (WRITING) CSV FILES
# ============================================================================
print("\n" + "=" * 80)
print("PART 1: EXPORTING (WRITING) CSV FILES")
print("=" * 80)

# Create sample data for demonstrations
sample_data = pd.DataFrame({
    'employee_id': [101, 102, 103, 104, 105],
    'name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'David Wilson', 'Eve Davis'],
    'age': [25, 30, 35, 28, 32],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'city': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
    'salary': [50000, 60000, 75000, 55000, 70000],
    'join_date': pd.date_range('2020-01-01', periods=5, freq='Y'),
    'performance_score': [8.5, 9.2, 7.8, 9.0, 8.8]
})

print("\nSample data for demonstrations:")
print(sample_data)
print(f"\nShape: {sample_data.shape}")
print(f"Data types:\n{sample_data.dtypes}")

# ============================================================================
# 1. BASIC CSV EXPORT
# ============================================================================
print("\n" + "=" * 80)
print("1. BASIC CSV EXPORT")
print("=" * 80)

print("\n--- Method 1: Basic Export (Default Settings) ---")
"""
EXPLANATION:
- to_csv() is the main method for exporting to CSV
- By default, includes row index as first column
- Uses comma as separator
- Writes column headers
"""

sample_data.to_csv('/tmp/basic_export.csv')
print(" File saved: basic_export.csv")
print("\nFile contents (first 3 lines):")
with open('/tmp/basic_export.csv', 'r') as f:
    for i, line in enumerate(f):
        if i < 3:
            print(f"  {line.strip()}")

print("\n--- Method 2: Export Without Index ---")
"""
EXPLANATION:
- index=False removes the row index column
- Most common way to export CSV
- Cleaner output for most use cases
- Use when row numbers aren't meaningful
"""

sample_data.to_csv('/tmp/no_index.csv', index=False)
print("File saved: no_index.csv (without row index)")
print("\nFile contents (first 3 lines):")
with open('/tmp/no_index.csv', 'r') as f:
    for i, line in enumerate(f):
        if i < 3:
            print(f"  {line.strip()}")

print("\n--- Method 3: Export With Custom Index Name ---")
"""
EXPLANATION:
- You can specify a name for the index column
- Useful when index has meaning
- Makes the CSV more readable
"""

df_with_named_index = sample_data.copy()
df_with_named_index.index.name = 'row_number'
df_with_named_index.to_csv('/tmp/named_index.csv')
print(" File saved: named_index.csv (with named index)")
print("\nFirst line:")
with open('/tmp/named_index.csv', 'r') as f:
    print(f"  {f.readline().strip()}")

# ============================================================================
# 2. CUSTOMIZING CSV OUTPUT
# ============================================================================
print("\n" + "=" * 80)
print("2. CUSTOMIZING CSV OUTPUT")
print("=" * 80)

print("\n--- Custom Separator (Delimiter) ---")
"""
EXPLANATION:
- sep parameter changes the delimiter
- Common alternatives: tab (\t), semicolon (;), pipe (|)
- Use semicolon for European Excel compatibility
- Use tab for TSV (Tab-Separated Values) files
"""

# Semicolon separator
sample_data.to_csv('/tmp/semicolon.csv', index=False, sep=';')
print(" Semicolon-separated file saved")
print("File contents (first line):")
with open('/tmp/semicolon.csv', 'r') as f:
    print(f"  {f.readline().strip()}")

# Tab separator (TSV)
sample_data.to_csv('/tmp/tab_separated.tsv', index=False, sep='\t')
print("\n Tab-separated file saved (.tsv)")
print("File contents (first line):")
with open('/tmp/tab_separated.tsv', 'r') as f:
    print(f"  {f.readline().strip()}")

# Pipe separator
sample_data.to_csv('/tmp/pipe_separated.csv', index=False, sep='|')
print("\n Pipe-separated file saved")
print("File contents (first line):")
with open('/tmp/pipe_separated.csv', 'r') as f:
    print(f"  {f.readline().strip()}")

print("\n--- Custom Header (Column Names) ---")
"""
EXPLANATION:
- header parameter controls column name output
- header=True (default): Include column names
- header=False: Skip column names
- header=[list]: Use custom column names
"""

# No header
sample_data.to_csv('/tmp/no_header.csv', index=False, header=False)
print("\n File saved without column headers")
print("File contents (first 2 lines):")
with open('/tmp/no_header.csv', 'r') as f:
    for i in range(2):
        print(f"  {f.readline().strip()}")

# Custom headers
custom_headers = ['ID', 'Full Name', 'Age', 'Dept', 'City', 'Salary', 'Join Date', 'Score']
sample_data.to_csv('/tmp/custom_headers.csv', index=False, header=custom_headers)
print("\n File saved with custom headers")
print("First line:")
with open('/tmp/custom_headers.csv', 'r') as f:
    print(f"  {f.readline().strip()}")

print("\n--- Custom Line Terminator ---")
"""
EXPLANATION:
- line_terminator controls end-of-line character
- Default: '\n' (Unix/Linux/Mac)
- '\r\n' for Windows compatibility
- Rarely needed to change
"""

sample_data.to_csv('/tmp/windows_line_ending.csv', index=False, line_terminator='\r\n')
print(" File saved with Windows line endings (\\r\\n)")

print("\n--- Custom Quote Character ---")
"""
EXPLANATION:
- quotechar specifies the character for quoting fields
- Default: double quote (")
- Used when field contains separator or special characters
- quoting parameter controls when to quote
"""

# Custom quote character
sample_data.to_csv('/tmp/custom_quote.csv', index=False, quotechar="'")
print(" File saved with single quotes")

# Quote only non-numeric fields
sample_data.to_csv('/tmp/quote_nonnumeric.csv', index=False, quoting=1)  # QUOTE_MINIMAL
print(" File saved with minimal quoting")

# ============================================================================
# 3. SELECTING DATA TO EXPORT
# ============================================================================
print("\n" + "=" * 80)
print("3. SELECTING DATA TO EXPORT")
print("=" * 80)

print("\n--- Export Specific Columns ---")
"""
EXPLANATION:
- Select columns before exporting
- Useful for creating focused datasets
- Reduces file size
- Protects sensitive information
"""

# Method 1: Select columns using list
columns_to_export = ['name', 'age', 'city']
sample_data[columns_to_export].to_csv('/tmp/selected_columns.csv', index=False)
print(f" Exported only: {columns_to_export}")

# Method 2: Using columns parameter
sample_data.to_csv('/tmp/selected_columns2.csv', index=False, columns=['name', 'department', 'salary'])
print(" Exported: name, department, salary")

print("\n--- Export Filtered Rows ---")
"""
EXPLANATION:
- Filter data before exporting
- Apply conditions to select specific rows
- Combine multiple conditions
"""

# Filter by age
sample_data[sample_data['age'] > 28].to_csv('/tmp/filtered_age.csv', index=False)
print("Exported employees older than 28")

# Multiple conditions
high_performers = sample_data[(sample_data['performance_score'] > 8.5) & 
                              (sample_data['salary'] > 55000)]
high_performers.to_csv('/tmp/high_performers.csv', index=False)
print(f" Exported {len(high_performers)} high performers")

# Filter by department
it_employees = sample_data[sample_data['department'] == 'IT']
it_employees.to_csv('/tmp/it_department.csv', index=False)
print(f" Exported {len(it_employees)} IT employees")

print("\n--- Export Top/Bottom N Rows ---")
"""
EXPLANATION:
- head(n): First n rows
- tail(n): Last n rows
- nlargest(n): Top n by value
- nsmallest(n): Bottom n by value
"""

# First 3 rows
sample_data.head(3).to_csv('/tmp/top_3.csv', index=False)
print(" Exported first 3 rows")

# Last 2 rows
sample_data.tail(2).to_csv('/tmp/bottom_2.csv', index=False)
print(" Exported last 2 rows")

# Top 3 by salary
sample_data.nlargest(3, 'salary').to_csv('/tmp/top_3_salary.csv', index=False)
print("Exported top 3 highest salaries")

# ============================================================================
# 4. HANDLING SPECIAL CASES
# ============================================================================
print("\n" + "=" * 80)
print("4. HANDLING SPECIAL CASES")
print("=" * 80)

print("\n--- Handling Missing Values (NaN) ---")
"""
EXPLANATION:
- na_rep parameter controls how NaN values are written
- Default: empty string ""
- Can use any string like "NULL", "NA", "N/A"
"""

# Create data with missing values
df_with_nan = sample_data.copy()
df_with_nan.loc[1, 'age'] = np.nan
df_with_nan.loc[3, 'salary'] = np.nan

# Default (empty string)
df_with_nan.to_csv('/tmp/nan_default.csv', index=False)
print(" NaN values saved as empty strings")

# Custom representation
df_with_nan.to_csv('/tmp/nan_custom.csv', index=False, na_rep='NULL')
print(" NaN values saved as 'NULL'")

print("\n--- Handling Date/Time Columns ---")
"""
EXPLANATION:
- date_format parameter controls date formatting
- Default: ISO format (YYYY-MM-DD)
- Can customize to any format
"""

# Default date format
sample_data.to_csv('/tmp/dates_default.csv', index=False)
print("Dates in ISO format (YYYY-MM-DD)")

# Custom date format
sample_data.to_csv('/tmp/dates_custom.csv', index=False, date_format='%m/%d/%Y')
print(" Dates in US format (MM/DD/YYYY)")

# Another format
sample_data.to_csv('/tmp/dates_readable.csv', index=False, date_format='%B %d, %Y')
print(" Dates in readable format (Month DD, YYYY)")

print("\n--- Handling Decimal Precision ---")
"""
EXPLANATION:
- float_format parameter controls decimal formatting
- Useful for controlling precision
- Can save file space
"""

# 2 decimal places
sample_data.to_csv('/tmp/decimal_2.csv', index=False, float_format='%.2f')
print(" Float values with 2 decimal places")

# No decimal places (integers)
sample_data.to_csv('/tmp/decimal_0.csv', index=False, float_format='%.0f')
print(" Float values rounded to integers")

print("\n--- Handling Large Numbers ---")
"""
EXPLANATION:
- By default, large numbers may use scientific notation
- float_format can prevent this
"""

large_numbers = pd.DataFrame({
    'id': [1, 2, 3],
    'value': [1234567890, 9876543210, 5555555555]
})

large_numbers.to_csv('/tmp/large_numbers.csv', index=False)
print(" Large numbers saved (may use scientific notation)")

large_numbers.to_csv('/tmp/large_numbers_fixed.csv', index=False, float_format='%.0f')
print(" Large numbers saved in fixed notation")

# ============================================================================
# 5. COMPRESSION
# ============================================================================
print("\n" + "=" * 80)
print("5. COMPRESSION")
print("=" * 80)

"""
EXPLANATION:
- Compression reduces file size
- Especially useful for large datasets
- Common formats: gzip, bz2, zip, xz
- Pandas automatically handles decompression on read
"""

print("\n--- Gzip Compression (Most Common) ---")
sample_data.to_csv('/tmp/compressed.csv.gz', index=False, compression='gzip')
print(" Gzip compressed file saved")

print("\n--- Bz2 Compression (Better Compression) ---")
sample_data.to_csv('/tmp/compressed.csv.bz2', index=False, compression='bz2')
print(" Bz2 compressed file saved")

print("\n--- Zip Compression ---")
sample_data.to_csv('/tmp/compressed.csv.zip', index=False, compression='zip')
print(" Zip compressed file saved")

# Compare file sizes
print("\n--- File Size Comparison ---")
uncompressed_size = os.path.getsize('/tmp/no_index.csv')
gzip_size = os.path.getsize('/tmp/compressed.csv.gz')
bz2_size = os.path.getsize('/tmp/compressed.csv.bz2')
zip_size = os.path.getsize('/tmp/compressed.csv.zip')

print(f"Uncompressed: {uncompressed_size:,} bytes")
print(f"Gzip:         {gzip_size:,} bytes ({gzip_size/uncompressed_size*100:.1f}% of original)")
print(f"Bz2:          {bz2_size:,} bytes ({bz2_size/uncompressed_size*100:.1f}% of original)")
print(f"Zip:          {zip_size:,} bytes ({zip_size/uncompressed_size*100:.1f}% of original)")
print(f"\nSpace saved: {uncompressed_size - gzip_size:,} bytes with gzip")

# ============================================================================
# 6. ENCODING
# ============================================================================
print("\n" + "=" * 80)
print("6. ENCODING")
print("=" * 80)

"""
EXPLANATION:
- Encoding defines how characters are stored
- UTF-8: Universal, supports all languages (recommended)
- UTF-8-sig: UTF-8 with BOM (for Excel compatibility)
- Latin1: Western European languages
- CP1252: Windows default
"""

# Create data with special characters
special_chars_data = pd.DataFrame({
    'name': ['José', 'François', '李明', 'Müller', 'Søren'],
    'city': ['São Paulo', 'Paris', '北京', 'München', 'København'],
    'symbol': ['€', '£', '¥', '$', 'kr']
})

print("\nData with special characters:")
print(special_chars_data)

print("\n--- UTF-8 Encoding (Default, Recommended) ---")
special_chars_data.to_csv('/tmp/utf8.csv', index=False, encoding='utf-8')
print(" Saved with UTF-8 encoding")

print("\n--- UTF-8 with BOM (Excel Compatibility) ---")
"""
EXPLANATION:
- BOM (Byte Order Mark) helps Excel recognize UTF-8
- Use when Excel users need to open the file
- Especially important for special characters
"""
special_chars_data.to_csv('/tmp/utf8_bom.csv', index=False, encoding='utf-8-sig')
print(" Saved with UTF-8-sig (Excel will display special characters correctly)")

print("\n--- Latin1 Encoding ---")
try:
    special_chars_data.to_csv('/tmp/latin1.csv', index=False, encoding='latin1')
    print("Saved with Latin1 encoding")
except UnicodeEncodeError:
    print("Some characters cannot be encoded in Latin1")

# ============================================================================
# 7. APPEND MODE
# ============================================================================
print("\n" + "=" * 80)
print("7. APPEND MODE")
print("=" * 80)

"""
EXPLANATION:
- mode='w': Write mode (default) - overwrites existing file
- mode='a': Append mode - adds to existing file
- Use append for incremental data updates
- Remember to set header=False when appending (except first write)
"""

print("\n--- Append to Existing File ---")

# First write (with header)
first_batch = sample_data.head(2)
first_batch.to_csv('/tmp/append_example.csv', index=False, mode='w')
print(" First batch written (2 rows)")

# Append (without header)
second_batch = sample_data.tail(3)
second_batch.to_csv('/tmp/append_example.csv', index=False, mode='a', header=False)
print("Second batch appended (3 rows)")

# Verify
final_df = pd.read_csv('/tmp/append_example.csv')
print(f"\nTotal rows in file: {len(final_df)}")
print(final_df)

# ============================================================================
# 8. ADVANCED TECHNIQUES
# ============================================================================
print("\n" + "=" * 80)
print("8. ADVANCED TECHNIQUES")
print("=" * 80)

print("\n--- Export in Chunks (Large Datasets) ---")
"""
EXPLANATION:
- For very large DataFrames
- Write in batches to avoid memory issues
- Useful when processing data incrementally
"""

# Simulate large dataset
large_df = pd.DataFrame({
    'id': range(1000),
    'value': np.random.rand(1000)
})

chunk_size = 200
num_chunks = len(large_df) // chunk_size + (1 if len(large_df) % chunk_size != 0 else 0)

print(f"Writing {len(large_df)} rows in {num_chunks} chunks...")

# Write first chunk with header
large_df.iloc[:chunk_size].to_csv('/tmp/chunked_output.csv', index=False, mode='w')

# Append remaining chunks
for i in range(1, num_chunks):
    start_idx = i * chunk_size
    end_idx = min((i + 1) * chunk_size, len(large_df))
    large_df.iloc[start_idx:end_idx].to_csv('/tmp/chunked_output.csv', 
                                             index=False, 
                                             mode='a', 
                                             header=False)

print(f" {len(large_df)} rows written in {num_chunks} chunks")

print("\n--- Multiple DataFrames to Separate Files ---")
"""
EXPLANATION:
- Export different subsets to different files
- Useful for splitting data by category
- Good for organizing large datasets
"""

for dept in sample_data['department'].unique():
    dept_data = sample_data[sample_data['department'] == dept]
    filename = f'/tmp/department_{dept.lower()}.csv'
    dept_data.to_csv(filename, index=False)
    print(f" {dept} department: {len(dept_data)} rows → {filename}")

print("\n--- Export with Timestamp in Filename ---")
"""
EXPLANATION:
- Add timestamp to filename for versioning
- Useful for regular exports
- Prevents overwriting previous exports
"""

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
filename_with_timestamp = f'/tmp/export_{timestamp}.csv'
sample_data.to_csv(filename_with_timestamp, index=False)
print(f" File saved: {filename_with_timestamp}")

print("\n--- Export Summary Statistics ---")
"""
EXPLANATION:
- Export aggregated/summary data
- Useful for reports
- Can combine with groupby
"""

# Summary by department
dept_summary = sample_data.groupby('department').agg({
    'age': 'mean',
    'salary': ['mean', 'min', 'max'],
    'performance_score': 'mean'
}).round(2)

dept_summary.to_csv('/tmp/department_summary.csv')
print(" Department summary exported")
print(dept_summary)

# ============================================================================
# PART 2: IMPORTING (READING) CSV FILES
# ============================================================================
print("\n" + "=" * 80)
print("PART 2: IMPORTING (READING) CSV FILES")
print("=" * 80)

# ============================================================================
# 1. BASIC CSV IMPORT
# ============================================================================
print("\n" + "=" * 80)
print("1. BASIC CSV IMPORT")
print("=" * 80)

print("\n--- Method 1: Basic Read ---")
"""
EXPLANATION:
- read_csv() is the main method for importing CSV
- Automatically detects column names from first row
- Infers data types
- Creates numeric index (0, 1, 2...)
"""

df_basic = pd.read_csv('/tmp/no_index.csv')
print(" File read successfully")
print(df_basic.head())
print(f"\nShape: {df_basic.shape}")
print(f"\nData types:\n{df_basic.dtypes}")

print("\n--- Method 2: Read with Custom Delimiter ---")
"""
EXPLANATION:
- sep or delimiter parameter specifies the separator
- Must match the file's actual separator
- Common: comma, semicolon, tab, pipe
"""

df_semicolon = pd.read_csv('/tmp/semicolon.csv', sep=';')
print(" Semicolon-separated file read")

df_tab = pd.read_csv('/tmp/tab_separated.tsv', sep='\t')
print(" Tab-separated file read")

df_pipe = pd.read_csv('/tmp/pipe_separated.csv', sep='|')
print(" Pipe-separated file read")

# ============================================================================
# 2. CONTROLLING WHAT TO READ
# ============================================================================
print("\n" + "=" * 80)
print("2. CONTROLLING WHAT TO READ")
print("=" * 80)

print("\n--- Read Specific Columns ---")
"""
EXPLANATION:
- usecols parameter selects columns to read
- Faster and uses less memory
- Can specify by name or position
"""

# By column names
df_specific_cols = pd.read_csv('/tmp/no_index.csv', usecols=['name', 'age', 'salary'])
print(" Read only name, age, salary columns")
print(df_specific_cols.head())

# By column positions (0-indexed)
df_by_position = pd.read_csv('/tmp/no_index.csv', usecols=[0, 1, 2])
print("\n Read first 3 columns by position")
print(df_by_position.head(3))

print("\n--- Read Limited Number of Rows ---")
"""
EXPLANATION:
- nrows parameter limits number of rows to read
- Useful for testing with large files
- Quick preview of data
"""

df_limited = pd.read_csv('/tmp/no_index.csv', nrows=3)
print(f" Read only first 3 rows")
print(df_limited)

print("\n--- Skip Rows ---")
"""
EXPLANATION:
- skiprows parameter skips specified rows
- Can skip from top of file
- Useful when file has metadata at top
"""

# Skip first 2 rows
df_skip = pd.read_csv('/tmp/no_index.csv', skiprows=2)
print(" Skipped first 2 rows")
print(df_skip.head(3))

# Skip specific row numbers
df_skip_specific = pd.read_csv('/tmp/no_index.csv', skiprows=[1, 3])
print("\n Skipped rows 1 and 3 (0-indexed)")
print(df_skip_specific.head(3))

# Skip rows with a function
df_skip_function = pd.read_csv('/tmp/no_index.csv', 
                               skiprows=lambda x: x > 0 and x % 2 == 0)
print("\n Skipped even-numbered rows")
print(df_skip_function.head())

print("\n--- Read Without Header ---")
"""
EXPLANATION:
- header=None: No header row in file
- Pandas assigns default column names: 0, 1, 2...
- Can specify custom names with names parameter
"""

df_no_header = pd.read_csv('/tmp/no_header.csv', header=None)
print(" Read file without header (default column names)")
print(df_no_header.head())

# With custom column names
custom_names = ['ID', 'Name', 'Age', 'Dept', 'City', 'Salary', 'JoinDate', 'Score']
df_custom_names = pd.read_csv('/tmp/no_header.csv', header=None, names=custom_names)
print("\n Read with custom column names")
print(df_custom_names.head())

# ============================================================================
# 3. DATA TYPE CONTROL
# ============================================================================
print("\n" + "=" * 80)
print("3. DATA TYPE CONTROL")
print("=" * 80)

print("\n--- Specify Data Types ---")
"""
EXPLANATION:
- dtype parameter specifies column data types
- Improves performance (no type inference needed)
- Prevents incorrect type detection
- Saves memory with appropriate types
"""

# Default (automatic type inference)
df_auto_types = pd.read_csv('/tmp/no_index.csv')
print("Automatic type inference:")
print(df_auto_types.dtypes)
print(f"Memory usage: {df_auto_types.memory_usage(deep=True).sum():,} bytes")

# Specify types
df_typed = pd.read_csv('/tmp/no_index.csv', 
                       dtype={'employee_id': 'int32',
                              'name': 'string',
                              'age': 'int16',
                              'department': 'category',
                              'city': 'category',
                              'salary': 'float32',
                              'performance_score': 'float32'})
print("\nWith specified types:")
print(df_typed.dtypes)
print(f"Memory usage: {df_typed.memory_usage(deep=True).sum():,} bytes")
print(f"Memory saved: {df_auto_types.memory_usage(deep=True).sum() - df_typed.memory_usage(deep=True).sum():,} bytes")

print("\n--- Parse Dates ---")
"""
EXPLANATION:
- parse_dates parameter converts columns to datetime
- Can specify single column or list of columns
- Automatic format detection
- Can specify custom date format
"""

# Parse single date column
df_dates = pd.read_csv('/tmp/no_index.csv', parse_dates=['join_date'])
print(" join_date parsed as datetime")
print(f"join_date type: {df_dates['join_date'].dtype}")
print(df_dates[['name', 'join_date']].head())

# Parse with custom format
df_dates_custom = pd.read_csv('/tmp/dates_custom.csv', 
                              parse_dates=['join_date'],
                              date_format='%m/%d/%Y')
print("\n Dates parsed with custom format (MM/DD/YYYY)")

print("\n--- Convert to Category (Save Memory) ---")
"""
EXPLANATION:
- category dtype for columns with repeated values
- Significantly reduces memory usage
- Faster operations on categorical data
"""

df_standard = pd.read_csv('/tmp/no_index.csv')
df_categorical = pd.read_csv('/tmp/no_index.csv', 
                             dtype={'department': 'category', 
                                    'city': 'category'})

print(f"Standard memory: {df_standard.memory_usage(deep=True).sum():,} bytes")
print(f"Categorical memory: {df_categorical.memory_usage(deep=True).sum():,} bytes")
print(f"Savings: {((1 - df_categorical.memory_usage(deep=True).sum() / df_standard.memory_usage(deep=True).sum()) * 100):.1f}%")

# ============================================================================
# 4. HANDLING MISSING VALUES
# ============================================================================
print("\n" + "=" * 80)
print("4. HANDLING MISSING VALUES")
print("=" * 80)

"""
EXPLANATION:
- na_values parameter defines what should be treated as NaN
- Can be string, list, or dictionary
- By default, recognizes: '', 'NA', 'NaN', 'NULL', etc.
"""

print("\n--- Default Missing Value Recognition ---")
df_default_na = pd.read_csv('/tmp/nan_custom.csv')
print(" Default NA values recognized")
print(df_default_na)
print(f"\nMissing values per column:\n{df_default_na.isnull().sum()}")

print("\n--- Custom Missing Value Indicators ---")
"""
EXPLANATION:
- Define custom strings that represent missing data
- Useful when data uses non-standard indicators
"""

# Treat 'NULL', 'N/A', and '-' as missing
df_custom_na = pd.read_csv('/tmp/nan_custom.csv', 
                           na_values=['NULL', 'N/A', '-', '?'])
print(" Custom NA values: 'NULL', 'N/A', '-', '?'")
print(df_custom_na)

print("\n--- Keep Default NA and Add Custom ---")
"""
EXPLANATION:
- keep_default_na=True (default): Keep standard NA values
- keep_default_na=False: Only use your specified values
"""

df_both_na = pd.read_csv('/tmp/nan_custom.csv', 
                         na_values=['MISSING'],
                         keep_default_na=True)
print(" Both default and custom NA values recognized")

print("\n--- Different NA Values per Column ---")
"""
EXPLANATION:
- Use dictionary to specify different NA values per column
- More precise control over missing data detection
"""

df_column_na = pd.read_csv('/tmp/no_index.csv',
                          na_values={'age': [0, -1], 
                                    'salary': [0]})
print(" Column-specific NA values applied")

# ============================================================================
# 5. INDEX COLUMN
# ============================================================================
print("\n" + "=" * 80)
print("5. INDEX COLUMN")
print("=" * 80)

print("\n--- Set Index Column During Read ---")
"""
EXPLANATION:
- index_col parameter sets which column becomes the index
- Can use column name or position
- Useful when row identifier exists in data
"""

# Use first column as index
df_index_0 = pd.read_csv('/tmp/with_index.csv', index_col=0)
print(" First column set as index")
print(df_index_0.head())

# Use named column as index
df_index_name = pd.read_csv('/tmp/no_index.csv', index_col='employee_id')
print("\n 'employee_id' set as index")
print(df_index_name.head())

# Multiple columns as index (MultiIndex)
df_multi_index = pd.read_csv('/tmp/no_index.csv', 
                             index_col=['department', 'city'])
print("\n MultiIndex created from department and city")
print(df_multi_index.head())

# ============================================================================
# 6. READING COMPRESSED FILES
# ============================================================================
print("\n" + "=" * 80)
print("6. READING COMPRESSED FILES")
print("=" * 80)

"""
EXPLANATION:
- Pandas automatically detects compression from file extension
- Can also specify compression explicitly
- Supports: gzip, bz2, zip, xz
"""

print("\n--- Read Gzip Compressed File ---")
df_gzip = pd.read_csv('/tmp/compressed.csv.gz')
print(" Gzip file read (automatic detection)")
print(df_gzip.head(3))

print("\n--- Read Bz2 Compressed File ---")
df_bz2 = pd.read_csv('/tmp/compressed.csv.bz2')
print(" Bz2 file read")

print("\n--- Read Zip Compressed File ---")
df_zip = pd.read_csv('/tmp/compressed.csv.zip')
print("Zip file read")

# Explicit compression specification
df_explicit = pd.read_csv('/tmp/compressed.csv.gz', compression='gzip')
print(" Compression explicitly specified")

# ============================================================================
# 7. ENCODING
# ============================================================================
print("\n" + "=" * 80)
print("7. ENCODING")
print("=" * 80)

"""
EXPLANATION:
- encoding parameter specifies character encoding
- UTF-8 is most common and default
- Use different encoding if file has special characters
- Common: utf-8, latin1, cp1252, iso-8859-1
"""

print("\n--- Read UTF-8 File ---")
df_utf8 = pd.read_csv('/tmp/utf8.csv', encoding='utf-8')
print(" UTF-8 file read")
print(df_utf8)

print("\n--- Read UTF-8 with BOM ---")
df_utf8_bom = pd.read_csv('/tmp/utf8_bom.csv', encoding='utf-8-sig')
print("UTF-8-sig file read (BOM handled)")
print(df_utf8_bom)

print("\n--- Handle Encoding Errors ---")
"""
EXPLANATION:
- If encoding is wrong, you'll get UnicodeDecodeError
- Try different encodings: utf-8, latin1, cp1252
- Use errors parameter to handle issues
"""

# Ignore encoding errors
try:
    df_ignore_errors = pd.read_csv('/tmp/utf8.csv', 
                                   encoding='latin1', 
                                   errors='ignore')
    print("✓ Encoding errors ignored")
except Exception as e:
    print(f"Error: {e}")

# Replace errors
df_replace_errors = pd.read_csv('/tmp/utf8.csv', 
                                encoding='latin1', 
                                errors='replace')
print("Encoding errors replaced with '?'")

# ============================================================================
# 8. READING IN CHUNKS
# ============================================================================
print("\n" + "=" * 80)
print("8. READING IN CHUNKS (LARGE FILES)")
print("=" * 80)

"""
EXPLANATION:
- chunksize parameter reads file in batches
- Essential for files larger than available memory
- Returns iterator, not DataFrame
- Process each chunk separately
"""

print("\n--- Read in Chunks ---")

chunk_size = 2
chunk_iterator = pd.read_csv('/tmp/no_index.csv', chunksize=chunk_size)

print(f"Reading file in chunks of {chunk_size} rows...")
total_salary = 0
total_rows = 0

for i, chunk in enumerate(chunk_iterator):
    print(f"\nChunk {i+1}:")
    print(chunk[['name', 'salary']])
    total_salary += chunk['salary'].sum()
    total_rows += len(chunk)

print(f"\nTotal rows processed: {total_rows}")
print(f" Total salary: ${total_salary:,.2f}")

print("\n--- Process Chunks and Combine ---")
"""
EXPLANATION:
- Read, process, and combine chunks
- Useful for filtering large files
- Apply transformations to each chunk
"""

chunk_iterator = pd.read_csv('/tmp/no_index.csv', chunksize=2)
processed_chunks = []

for chunk in chunk_iterator:
    # Filter and transform each chunk
    filtered = chunk[chunk['age'] > 27]
    if len(filtered) > 0:
        processed_chunks.append(filtered)

# Combine all chunks
if processed_chunks:
    result = pd.concat(processed_chunks, ignore_index=True)
    print(" Chunks processed and combined")
    print(result)

# ============================================================================
# 9. ADVANCED READING OPTIONS
# ============================================================================
print("\n" + "=" * 80)
print("9. ADVANCED READING OPTIONS")
print("=" * 80)

print("\n--- Read with Comment Lines ---")
"""
EXPLANATION:
- comment parameter ignores lines starting with specified character
- Useful when files have metadata or comments
"""

# Create file with comments
with open('/tmp/with_comments.csv', 'w') as f:
    f.write("# This is a comment\n")
    f.write("# Another comment\n")
    f.write("name,age\n")
    f.write("Alice,25\n")
    f.write("# Mid-file comment\n")
    f.write("Bob,30\n")

df_comments = pd.read_csv('/tmp/with_comments.csv', comment='#')
print("Comment lines (starting with #) ignored")
print(df_comments)

print("\n--- Handle Thousands Separator ---")
"""
EXPLANATION:
- thousands parameter handles thousand separators
- Common: comma (1,000) or dot (1.000)
"""

# Create data with thousand separators
with open('/tmp/thousands.csv', 'w') as f:
    f.write("item,price\n")
    f.write("Car,25,000\n")
    f.write("House,250,000\n")

df_thousands = pd.read_csv('/tmp/thousands.csv', thousands=',')
print("✓ Thousand separators handled")
print(df_thousands)
print(f"Price data type: {df_thousands['price'].dtype}")

print("\n--- Handle Decimal Separator ---")
"""
EXPLANATION:
- decimal parameter for non-US decimal separator
- European format uses comma: 1,5 (instead of 1.5)
"""

# Create data with comma decimals
with open('/tmp/decimals.csv', 'w') as f:
    f.write("item;price\n")
    f.write("Item1;10,5\n")
    f.write("Item2;20,75\n")

df_decimals = pd.read_csv('/tmp/decimals.csv', sep=';', decimal=',')
print("Comma as decimal separator handled")
print(df_decimals)

print("\n--- Skip Footer Lines ---")
"""
EXPLANATION:
- skipfooter parameter skips lines from end of file
- Useful when files have summary rows at bottom
"""

# Create file with footer
with open('/tmp/with_footer.csv', 'w') as f:
    f.write("name,value\n")
    f.write("A,100\n")
    f.write("B,200\n")
    f.write("TOTAL,300\n")
    f.write("Generated: 2024-01-01\n")

df_no_footer = pd.read_csv('/tmp/with_footer.csv', 
                           skipfooter=2, 
                           engine='python')
print("Last 2 lines skipped")
print(df_no_footer)

print("\n--- Low Memory Mode ---")
"""
EXPLANATION:
- low_memory=False: Read entire file to determine dtypes
- low_memory=True (default): Read in chunks (faster but less accurate)
- Use low_memory=False for mixed-type columns
"""

df_low_memory = pd.read_csv('/tmp/no_index.csv', low_memory=False)
print("Read with low_memory=False (more accurate type inference)")

print("\n--- Handle Bad Lines ---")
"""
EXPLANATION:
- on_bad_lines parameter controls handling of malformed lines
- Options: 'error' (default), 'warn', 'skip'
"""

# Create file with bad line
with open('/tmp/bad_lines.csv', 'w') as f:
    f.write("name,age\n")
    f.write("Alice,25\n")
    f.write("Bob,30,extra,data\n")  # Bad line (too many fields)
    f.write("Charlie,35\n")

df_skip_bad = pd.read_csv('/tmp/bad_lines.csv', on_bad_lines='skip')
print(" Bad lines skipped")
print(df_skip_bad)

# ============================================================================
# 10. READING FROM DIFFERENT SOURCES
# ============================================================================
print("\n" + "=" * 80)
print("10. READING FROM DIFFERENT SOURCES")
print("=" * 80)

print("\n--- Read from String (StringIO) ---")
"""
EXPLANATION:
- Read CSV data from a string
- Useful for testing or embedded data
"""

from io import StringIO

csv_string = """name,age,city
Alice,25,New York
Bob,30,London
Charlie,35,Paris"""

df_from_string = pd.read_csv(StringIO(csv_string))
print(" Read from string")
print(df_from_string)

print("\n--- Read from URL ---")
"""
EXPLANATION:
- Pandas can read directly from web URLs
- Must be publicly accessible
- Supports HTTP and HTTPS
"""

print("Example (commented out):")
print("# url = 'https://example.com/data.csv'")
print("# df = pd.read_csv(url)")
print(" Can read directly from URLs")

print("\n--- Read from Clipboard ---")
"""
EXPLANATION:
- Read data from clipboard
- Great for copying from Excel or web tables
- Very convenient for quick data imports
"""

print("Example:")
print("# Copy data from Excel or browser")
print("# df = pd.read_clipboard()")
print("Reads data from clipboard")


# List created files
print("\n Files created during this tutorial:")
print("=" * 80)
tmp_files = [f for f in os.listdir('/tmp') if f.endswith(('.csv', '.tsv', '.gz', '.bz2', '.zip'))]
for file in sorted(tmp_files)[:30]:  # Show first 30
    size = os.path.getsize(f'/tmp/{file}')
    print(f"  {file:<40} ({size:>8} bytes)")
if len(tmp_files) > 30:
    print(f"  ... and {len(tmp_files) - 30} more files")
