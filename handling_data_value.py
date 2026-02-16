"""
Handling Date Values
=======================================
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("=" * 80)
print("HANDLING DATE VALUES IN PANDAS")
print("=" * 80)

# ============================================================================
# PART 1: CREATING DATE/TIME DATA
# ============================================================================
print("\n" + "=" * 80)
print("PART 1: CREATING DATE/TIME DATA")
print("=" * 80)

# Method 1: pd.to_datetime() - String to datetime
print("\n1. Convert string to datetime:")
dates = pd.to_datetime(['2024-01-01', '2024-02-15', '2024-03-30'])
print(dates)

# Method 2: Different date formats
print("\n2. Parse different date formats:")
dates = pd.to_datetime(['01/15/2024', '02/20/2024'], format='%m/%d/%Y')
print(dates)

# Method 3: pd.date_range() - Create date sequence
print("\n3. Create date range:")
date_range = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
print(date_range)

# Method 4: Date range with periods
print("\n4. Date range with number of periods:")
date_range = pd.date_range(start='2024-01-01', periods=10, freq='D')
print(date_range)

# Method 5: Date range with frequency
print("\n5. Date range with different frequencies:")
print("Daily:", pd.date_range('2024-01-01', periods=5, freq='D'))
print("Weekly:", pd.date_range('2024-01-01', periods=5, freq='W'))
print("Monthly:", pd.date_range('2024-01-01', periods=5, freq='M'))
print("Yearly:", pd.date_range('2024-01-01', periods=5, freq='Y'))
print("Hourly:", pd.date_range('2024-01-01', periods=5, freq='H'))

# Method 6: pd.Timestamp() - Single timestamp
print("\n6. Create single timestamp:")
ts = pd.Timestamp('2024-01-15 14:30:00')
print(ts)

# Method 7: Current datetime
print("\n7. Current datetime:")
now = pd.Timestamp.now()
print(now)

# Method 8: From datetime object
print("\n8. From Python datetime:")
dt = datetime(2024, 1, 15, 14, 30, 0)
ts = pd.Timestamp(dt)
print(ts)

# ============================================================================
# PART 2: PARSING DATES IN DATAFRAME
# ============================================================================
print("\n" + "=" * 80)
print("PART 2: PARSING DATES IN DATAFRAME")
print("=" * 80)

# Create sample DataFrame with date strings
df = pd.DataFrame({
    'date_str': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01'],
    'value': [100, 150, 200, 175, 225]
})

print("\nOriginal DataFrame:")
print(df)
print(df.dtypes)

# Method 1: Convert column to datetime
print("\n1. Convert string column to datetime:")
df['date'] = pd.to_datetime(df['date_str'])
print(df)
print(df.dtypes)

# Method 2: Parse during CSV read
print("\n2. Parse dates when reading CSV:")
df.to_csv('/tmp/dates.csv', index=False)
df_read = pd.read_csv('/tmp/dates.csv', parse_dates=['date'])
print(df_read.dtypes)

# Method 3: Parse with specific format
df2 = pd.DataFrame({
    'date_str': ['01/15/2024', '02/20/2024', '03/25/2024'],
    'value': [100, 200, 300]
})

print("\n3. Parse with custom format:")
df2['date'] = pd.to_datetime(df2['date_str'], format='%m/%d/%Y')
print(df2)

# Method 4: Handle errors
df3 = pd.DataFrame({
    'date_str': ['2024-01-01', 'invalid', '2024-03-01'],
    'value': [100, 200, 300]
})

print("\n4. Handle parsing errors (coerce to NaT):")
df3['date'] = pd.to_datetime(df3['date_str'], errors='coerce')
print(df3)

# Method 5: Parse multiple columns
df4 = pd.DataFrame({
    'year': [2024, 2024, 2024],
    'month': [1, 2, 3],
    'day': [15, 20, 25]
})

print("\n5. Parse from multiple columns:")
df4['date'] = pd.to_datetime(df4[['year', 'month', 'day']])
print(df4)

# ============================================================================
# PART 3: EXTRACTING DATE COMPONENTS
# ============================================================================
print("\n" + "=" * 80)
print("PART 3: EXTRACTING DATE COMPONENTS")
print("=" * 80)

# Create DataFrame with dates
df = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=10, freq='D'),
    'value': np.random.randint(100, 500, 10)
})

print("\nDataFrame with dates:")
print(df)

# Extract year
print("\n1. Extract year:")
df['year'] = df['date'].dt.year
print(df[['date', 'year']])

# Extract month
print("\n2. Extract month:")
df['month'] = df['date'].dt.month
print(df[['date', 'month']])

# Extract day
print("\n3. Extract day:")
df['day'] = df['date'].dt.day
print(df[['date', 'day']])

# Extract day of week
print("\n4. Extract day of week (0=Monday):")
df['day_of_week'] = df['date'].dt.dayofweek
print(df[['date', 'day_of_week']])

# Extract day name
print("\n5. Extract day name:")
df['day_name'] = df['date'].dt.day_name()
print(df[['date', 'day_name']])

# Extract month name
print("\n6. Extract month name:")
df['month_name'] = df['date'].dt.month_name()
print(df[['date', 'month_name']])

# Extract quarter
print("\n7. Extract quarter:")
df['quarter'] = df['date'].dt.quarter
print(df[['date', 'quarter']])

# Extract week of year
print("\n8. Extract week of year:")
df['week'] = df['date'].dt.isocalendar().week
print(df[['date', 'week']])

# Extract time components
df_time = pd.DataFrame({
    'datetime': pd.date_range('2024-01-01 10:30:45', periods=5, freq='H')
})

print("\n9. Extract time components:")
df_time['hour'] = df_time['datetime'].dt.hour
df_time['minute'] = df_time['datetime'].dt.minute
df_time['second'] = df_time['datetime'].dt.second
print(df_time)

# Extract date only (no time)
print("\n10. Extract date only:")
df_time['date_only'] = df_time['datetime'].dt.date
print(df_time[['datetime', 'date_only']])

# Extract time only
print("\n11. Extract time only:")
df_time['time_only'] = df_time['datetime'].dt.time
print(df_time[['datetime', 'time_only']])

# ============================================================================
# PART 4: DATE ARITHMETIC
# ============================================================================
print("\n" + "=" * 80)
print("PART 4: DATE ARITHMETIC")
print("=" * 80)

# Create DataFrame
df = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=5, freq='D'),
    'value': [100, 200, 300, 400, 500]
})

print("\nOriginal DataFrame:")
print(df)

# Add days
print("\n1. Add days:")
df['plus_7_days'] = df['date'] + pd.Timedelta(days=7)
print(df[['date', 'plus_7_days']])

# Subtract days
print("\n2. Subtract days:")
df['minus_3_days'] = df['date'] - pd.Timedelta(days=3)
print(df[['date', 'minus_3_days']])

# Add weeks
print("\n3. Add weeks:")
df['plus_2_weeks'] = df['date'] + pd.Timedelta(weeks=2)
print(df[['date', 'plus_2_weeks']])

# Add months (using DateOffset)
print("\n4. Add months:")
df['plus_1_month'] = df['date'] + pd.DateOffset(months=1)
print(df[['date', 'plus_1_month']])

# Add years
print("\n5. Add years:")
df['plus_1_year'] = df['date'] + pd.DateOffset(years=1)
print(df[['date', 'plus_1_year']])

# Add hours
print("\n6. Add hours:")
df['plus_12_hours'] = df['date'] + pd.Timedelta(hours=12)
print(df[['date', 'plus_12_hours']])

# Difference between dates
print("\n7. Calculate date difference:")
df['diff_days'] = (df['plus_7_days'] - df['date']).dt.days
print(df[['date', 'plus_7_days', 'diff_days']])

# Days until/since specific date
print("\n8. Days since start:")
start_date = df['date'].min()
df['days_since_start'] = (df['date'] - start_date).dt.days
print(df[['date', 'days_since_start']])

# Age calculation
df_birth = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'birth_date': pd.to_datetime(['1990-01-15', '1985-06-20', '1995-11-30'])
})

print("\n9. Calculate age:")
today = pd.Timestamp.now()
df_birth['age'] = ((today - df_birth['birth_date']).dt.days / 365.25).astype(int)
print(df_birth)

# ============================================================================
# PART 5: FILTERING BY DATES
# ============================================================================
print("\n" + "=" * 80)
print("PART 5: FILTERING BY DATES")
print("=" * 80)

# Create DataFrame with date range
df = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=30, freq='D'),
    'sales': np.random.randint(100, 500, 30)
})

print("\nDataFrame:")
print(df.head(10))

# Filter by specific date
print("\n1. Filter by specific date:")
result = df[df['date'] == '2024-01-15']
print(result)

# Filter by date range
print("\n2. Filter by date range:")
result = df[(df['date'] >= '2024-01-10') & (df['date'] <= '2024-01-20')]
print(result)

# Filter using between
print("\n3. Filter using between:")
result = df[df['date'].between('2024-01-10', '2024-01-20')]
print(result)

# Filter last N days
print("\n4. Filter last 7 days:")
last_date = df['date'].max()
result = df[df['date'] > last_date - pd.Timedelta(days=7)]
print(result)

# Filter by month
print("\n5. Filter by month:")
result = df[df['date'].dt.month == 1]
print(result.head())

# Filter by year
print("\n6. Filter by year:")
result = df[df['date'].dt.year == 2024]
print(result.head())

# Filter by day of week
print("\n7. Filter weekdays only (Monday=0 to Friday=4):")
result = df[df['date'].dt.dayofweek < 5]
print(result.head())

# Filter weekends
print("\n8. Filter weekends:")
result = df[df['date'].dt.dayofweek >= 5]
print(result.head())

# Filter by quarter
print("\n9. Filter by quarter:")
result = df[df['date'].dt.quarter == 1]
print(result.head())

# ============================================================================
# PART 6: DATE INDEX
# ============================================================================
print("\n" + "=" * 80)
print("PART 6: DATE INDEX")
print("=" * 80)

# Create DataFrame with date index
df = pd.DataFrame({
    'sales': np.random.randint(100, 500, 30)
}, index=pd.date_range('2024-01-01', periods=30, freq='D'))

print("\n1. DataFrame with DatetimeIndex:")
print(df.head(10))

# Select by date string
print("\n2. Select by date string:")
print(df.loc['2024-01-15'])

# Select date range
print("\n3. Select date range:")
print(df.loc['2024-01-10':'2024-01-15'])

# Select by year
print("\n4. Select by year:")
print(df.loc['2024'].head())

# Select by month
print("\n5. Select by year-month:")
print(df.loc['2024-01'].head())

# Partial string indexing
print("\n6. Partial string indexing:")
print(df['2024-01-10':'2024-01-15'])

# ============================================================================
# PART 7: RESAMPLING
# ============================================================================
print("\n" + "=" * 80)
print("PART 7: RESAMPLING")
print("=" * 80)

# Create daily data
df = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=30, freq='D'),
    'sales': np.random.randint(100, 500, 30)
})
df = df.set_index('date')

print("\nDaily data:")
print(df.head(10))

# Resample to weekly (sum)
print("\n1. Resample to weekly (sum):")
weekly = df.resample('W').sum()
print(weekly)

# Resample to weekly (mean)
print("\n2. Resample to weekly (mean):")
weekly_mean = df.resample('W').mean()
print(weekly_mean)

# Resample to monthly
print("\n3. Resample to monthly:")
monthly = df.resample('M').sum()
print(monthly)

# Resample with multiple aggregations
print("\n4. Resample with multiple aggregations:")
monthly_stats = df.resample('M').agg(['sum', 'mean', 'min', 'max'])
print(monthly_stats)

# Upsampling (daily to hourly with forward fill)
df_hourly = pd.DataFrame({
    'value': [100, 200, 300]
}, index=pd.date_range('2024-01-01', periods=3, freq='D'))

print("\n5. Upsample (daily to hourly) - forward fill:")
hourly = df_hourly.resample('H').ffill()
print(hourly.head(10))

# Downsampling with custom function
print("\n6. Resample with custom function:")
weekly_custom = df.resample('W').apply(lambda x: x.max() - x.min())
print(weekly_custom)

# ============================================================================
# PART 8: TIME ZONES
# ============================================================================
print("\n" + "=" * 80)
print("PART 8: TIME ZONES")
print("=" * 80)

# Create timezone-naive datetime
df = pd.DataFrame({
    'datetime': pd.date_range('2024-01-01', periods=5, freq='D')
})

print("\n1. Timezone-naive datetime:")
print(df)

# Localize to timezone
print("\n2. Localize to timezone:")
df['datetime_utc'] = df['datetime'].dt.tz_localize('UTC')
print(df)

# Convert to different timezone
print("\n3. Convert to different timezone:")
df['datetime_ny'] = df['datetime_utc'].dt.tz_convert('America/New_York')
df['datetime_tokyo'] = df['datetime_utc'].dt.tz_convert('Asia/Tokyo')
print(df[['datetime_utc', 'datetime_ny', 'datetime_tokyo']])

# Remove timezone
print("\n4. Remove timezone:")
df['datetime_naive'] = df['datetime_utc'].dt.tz_localize(None)
print(df[['datetime_utc', 'datetime_naive']])

# ============================================================================
# PART 9: PERIOD AND INTERVAL
# ============================================================================
print("\n" + "=" * 80)
print("PART 9: PERIOD AND INTERVAL")
print("=" * 80)

# Create Period
print("\n1. Create Period:")
period = pd.Period('2024-01', freq='M')
print(f"Period: {period}")
print(f"Start: {period.start_time}")
print(f"End: {period.end_time}")

# Period range
print("\n2. Period range:")
periods = pd.period_range('2024-01', periods=6, freq='M')
print(periods)

# Convert to timestamp
print("\n3. Convert Period to Timestamp:")
timestamps = periods.to_timestamp()
print(timestamps)

# DataFrame with Period index
df_period = pd.DataFrame({
    'sales': [100, 150, 200, 175, 225, 250]
}, index=periods)

print("\n4. DataFrame with Period index:")
print(df_period)

# ============================================================================
# PART 10: COMMON DATE OPERATIONS
# ============================================================================
print("\n" + "=" * 80)
print("PART 10: COMMON DATE OPERATIONS")
print("=" * 80)

df = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=100, freq='D'),
    'sales': np.random.randint(100, 500, 100)
})

# Get first day of month
print("\n1. First day of month:")
df['month_start'] = df['date'] - pd.offsets.MonthBegin(1)
print(df[['date', 'month_start']].head(10))

# Get last day of month
print("\n2. Last day of month:")
df['month_end'] = df['date'] + pd.offsets.MonthEnd(0)
print(df[['date', 'month_end']].head(10))

# Check if weekend
print("\n3. Check if weekend:")
df['is_weekend'] = df['date'].dt.dayofweek >= 5
print(df[['date', 'is_weekend']].head(10))

# Check if month end
print("\n4. Check if month end:")
df['is_month_end'] = df['date'].dt.is_month_end
print(df[['date', 'is_month_end']].head(35))

# Check if month start
print("\n5. Check if month start:")
df['is_month_start'] = df['date'].dt.is_month_start
print(df[['date', 'is_month_start']].head(35))

# Check if quarter end
print("\n6. Check if quarter end:")
df['is_quarter_end'] = df['date'].dt.is_quarter_end
print(df[df['is_quarter_end']][['date', 'is_quarter_end']])

# Check if year end
print("\n7. Check if year end:")
df['is_year_end'] = df['date'].dt.is_year_end
print(df[df['is_year_end']][['date', 'is_year_end']])

# Days in month
print("\n8. Days in month:")
df['days_in_month'] = df['date'].dt.days_in_month
print(df[['date', 'days_in_month']].head(35))

# Normalize (set time to midnight)
df_time = pd.DataFrame({
    'datetime': pd.date_range('2024-01-01 14:30:00', periods=5, freq='H')
})

print("\n9. Normalize datetime (set to midnight):")
df_time['normalized'] = df_time['datetime'].dt.normalize()
print(df_time)

# Round datetime
print("\n10. Round datetime:")
df_time['rounded_hour'] = df_time['datetime'].dt.round('H')
df_time['rounded_day'] = df_time['datetime'].dt.round('D')
print(df_time)

# Floor datetime
print("\n11. Floor datetime:")
df_time['floor_hour'] = df_time['datetime'].dt.floor('H')
print(df_time[['datetime', 'floor_hour']])

# Ceil datetime
print("\n12. Ceil datetime:")
df_time['ceil_hour'] = df_time['datetime'].dt.ceil('H')
print(df_time[['datetime', 'ceil_hour']])

print("\n" + "=" * 80)
print("END OF DATE HANDLING TUTORIAL")
print("=" * 80)