"""
 Data Visualization (Plot Methods)
====================================================
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=" * 80)
print("DATA VISUALIZATION ")
print("=" * 80)

"""
WHAT IS DATA VISUALIZATION?
============================
- Converting numbers/data into pictures (charts/graphs)
- Makes patterns easy to see
- Pictures are easier to understand than tables of numbers

WHY VISUALIZE DATA?
===================
- Spot trends quickly (going up? going down?)
- Find patterns (repeated behavior)
- Compare values (which is bigger?)
- Communicate findings (show others your results)
- Make decisions faster (see problems immediately)

PANDAS + MATPLOTLIB:
====================
- Pandas uses matplotlib for plotting
- Just call .plot() on your DataFrame
- No need to write complex code
- Pandas handles most details automatically
"""

# Sample data
df = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'sales': [100, 120, 115, 140, 160, 150],
    'profit': [20, 25, 22, 30, 35, 32],
    'expenses': [80, 95, 93, 110, 125, 118]
})

print("\nSample Data:")
print(df)

# ============================================================================
# PART 1: LINE PLOT
# ============================================================================
print("\n" + "=" * 80)
print("PART 1: LINE PLOT")
print("=" * 80)

"""
WHAT IS A LINE PLOT?
====================
- Connects data points with lines
- Like connecting dots in a drawing
- Shows trend over time

WHEN TO USE:
============
✓ Track changes over time (sales per month, temperature per day)
✓ Show trends (increasing, decreasing, stable)
✓ Compare multiple series (sales vs profit over time)

REAL EXAMPLES:
- Stock prices over months
- Website traffic per day
- Temperature changes throughout the year


SIMPLE EXPLANATION:
If you track your weight every week:
Week 1: 70kg, Week 2: 69kg, Week 3: 68kg
Line plot shows if you're losing/gaining weight
"""

print("\nExample: Sales over months")
df.plot(x='month', y='sales', kind='line', title='Monthly Sales Trend')
plt.ylabel('Sales ($)')
plt.tight_layout()
plt.savefig('/tmp/line_plot.png')
plt.close()
print("✓ Line plot created")
print("  - Shows if sales are increasing or decreasing")
print("  - Easy to spot trends")

# Multiple lines
print("\nExample: Compare sales vs profit")
df.plot(x='month', y=['sales', 'profit'], kind='line', title='Sales vs Profit')
plt.ylabel('Amount ($)')
plt.tight_layout()
plt.savefig('/tmp/multi_line.png')
plt.close()
print("Multiple line plot created")
print("  - Two lines on same chart")
print("  - Easy to compare trends")

# ============================================================================
# PART 2: BAR PLOT
# ============================================================================
print("\n" + "=" * 80)
print("PART 2: BAR PLOT")
print("=" * 80)

"""
WHAT IS A BAR PLOT?
===================
- Vertical or horizontal bars
- Height of bar = value
- Like stacking blocks to show quantity

WHEN TO USE:
============
✓ Compare different categories (cities, products, departments)
✓ Show rankings (top 10 products)
✓ Compare totals (sales by region)

REAL EXAMPLES:
- Sales by product (which product sells most?)
- Population by city (which city is biggest?)
- Scores by student (who scored highest?)

VERTICAL VS HORIZONTAL:
=======================
Vertical (kind='bar'):
- Categories on X-axis (bottom)
- Values on Y-axis (left)
- Good for few categories

Horizontal (kind='barh'):
- Categories on Y-axis (left)
- Values on X-axis (bottom)
- Good for many categories (easier to read names)

SIMPLE EXPLANATION:
Like comparing height of people standing in a line
Taller bar = bigger value
"""

print("\nExample: Sales by month (vertical bars)")
df.plot(x='month', y='sales', kind='bar', title='Sales by Month')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/tmp/bar_plot.png')
plt.close()
print("✓ Bar plot created")
print("  - Easy to compare months")
print("  - Tallest bar = highest sales")

# Horizontal
print("\nExample: Horizontal bar chart")
df.plot(x='month', y='sales', kind='barh', title='Sales by Month')
plt.xlabel('Sales ($)')
plt.tight_layout()
plt.savefig('/tmp/barh_plot.png')
plt.close()
print("✓ Horizontal bar plot created")
print("  - Easier to read month names")
print("  - Good for long category names")

# Stacked bar
print("\nExample: Stacked bar (sales + profit)")
df[['sales', 'profit']].plot(kind='bar', stacked=True, title='Sales Breakdown')
plt.tight_layout()
plt.savefig('/tmp/stacked_bar.png')
plt.close()
print("✓ Stacked bar plot created")
print("  - Shows total and parts")
print("  - Each color is a component")

# ============================================================================
# PART 3: HISTOGRAM
# ============================================================================
print("\n" + "=" * 80)
print("PART 3: HISTOGRAM")
print("=" * 80)

"""
WHAT IS A HISTOGRAM?
====================
- Shows distribution of data
- Groups values into ranges (bins)
- Counts how many fall in each range

WHEN TO USE:
============
✓ Understand data spread (are values clustered or spread out?)
✓ Find patterns (bell curve, skewed)
✓ Spot outliers (unusual values)

REAL EXAMPLES:
- Age distribution in a company (how many people in 20-30, 30-40, etc.)
- Exam scores (how many got 0-10, 10-20, etc.)
- Salary ranges (how many earn 30-40k, 40-50k, etc.)

BINS EXPLAINED:
===============
Bins = ranges that group data
Example: Ages 0-100
- Bin 1: 0-20 years
- Bin 2: 20-40 years
- Bin 3: 40-60 years
- Bin 4: 60-80 years
- Bin 5: 80-100 years

Height of bar = how many people in that range

SIMPLE EXPLANATION:
Imagine sorting marbles by size:
Small (0-2cm), Medium (2-4cm), Large (4-6cm)
Histogram shows how many marbles in each size group
"""

# Generate sample age data
ages = pd.DataFrame({
    'age': [22, 25, 28, 30, 32, 35, 38, 40, 42, 45, 48, 50, 52, 55, 58, 60]
})

print("\nExample: Age distribution")
ages['age'].plot(kind='hist', bins=5, title='Age Distribution', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('/tmp/histogram.png')
plt.close()
print(" Histogram created")
print("  - Shows age ranges")
print("  - Reveals clustering (most people in which age group)")

# ============================================================================
# PART 4: SCATTER PLOT
# ============================================================================
print("\n" + "=" * 80)
print("PART 4: SCATTER PLOT")
print("=" * 80)

"""
WHAT IS A SCATTER PLOT?
=======================
- Shows relationship between two variables
- Each dot represents one data point
- Pattern of dots shows correlation

WHEN TO USE:
============
 Find relationships (does X affect Y?)
 Spot correlations (if X increases, does Y increase?)
Identify clusters (groups of similar data)

REAL EXAMPLES:
- Height vs Weight (are taller people heavier?)
- Study hours vs Exam scores (more study = better score?)
- Age vs Salary (older = higher salary?)

PATTERNS TO LOOK FOR:
=====================
Positive correlation: 
  • Dots go from bottom-left to top-right
  • X increases → Y increases
  
Negative correlation:
  • Dots go from top-left to bottom-right
  • X increases → Y decreases
  
No correlation:
  • Dots scattered randomly
  • X doesn't affect Y

SIMPLE EXPLANATION:
Plot every person's height (X) and weight (Y)
Each person = one dot
Pattern shows if height and weight are related
"""

print("\nExample: Sales vs Profit relationship")
df.plot(x='sales', y='profit', kind='scatter', title='Sales vs Profit')
plt.xlabel('Sales ($)')
plt.ylabel('Profit ($)')
plt.tight_layout()
plt.savefig('/tmp/scatter.png')
plt.close()
print("✓Scatter plot created")
print("  - Each dot = one month")
print("  - Shows if more sales = more profit")

# ============================================================================
# PART 5: PIE CHART
# ============================================================================
print("\n" + "=" * 80)
print("PART 5: PIE CHART")
print("=" * 80)

"""
WHAT IS A PIE CHART?
====================
- Circle divided into slices
- Each slice = proportion of total
- Like cutting a pizza into pieces

WHEN TO USE:
============
 Show parts of a whole (market share, budget breakdown)
 Display percentages (what % is each category)
 Compare proportions (which is the biggest slice?)

WHEN NOT TO USE:
================
 More than 5-6 categories (too many slices = confusing)
 Similar values (hard to distinguish slice sizes)
 Trends over time (use line chart instead)

REAL EXAMPLES:
- Budget allocation (30% rent, 20% food, 15% transport)
- Market share (Company A: 40%, Company B: 35%, Company C: 25%)
- Vote distribution (Candidate A: 45%, Candidate B: 35%, Candidate C: 20%)

SIMPLE EXPLANATION:
You have $100 to spend
- Food: $30 (30% of pie)
- Rent: $50 (50% of pie)
- Entertainment: $20 (20% of pie)
Pie chart shows these proportions visually
"""

# Sample data
expenses = pd.Series({
    'Rent': 1200,
    'Food': 600,
    'Transport': 300,
    'Entertainment': 400,
    'Utilities': 500
})

print("\nExample: Budget breakdown")
expenses.plot(kind='pie', title='Monthly Expenses', autopct='%1.1f%%')
plt.ylabel('')  # Remove y-label
plt.tight_layout()
plt.savefig('/tmp/pie_chart.png')
plt.close()
print("Pie chart created")
print("  - Each slice = expense category")
print("  - Percentages shown automatically")
print("  - Easy to see biggest expense")

# ============================================================================
# PART 6: BOX PLOT
# ============================================================================
print("\n" + "=" * 80)
print("PART 6: BOX PLOT")
print("=" * 80)

"""
WHAT IS A BOX PLOT?
===================
- Shows data distribution using 5 numbers
- Box shows middle 50% of data
- Whiskers show range
- Dots show outliers

WHEN TO USE:
============
 Compare distributions across groups
 Identify outliers (unusual values)
 See data spread (tight or wide?)

THE 5 NUMBERS:
==============
1. Minimum: Smallest value (bottom whisker)
2. Q1 (25%): 25% of data below this (bottom of box)
3. Median (50%): Middle value (line in box)
4. Q3 (75%): 75% of data below this (top of box)
5. Maximum: Largest value (top whisker)

PARTS OF BOX PLOT:
==================
    Maximum (whisker top) ─────┬
                               │
    Q3 (75%) ──────────────────┤
                               │ Box (50% of data)
    Median (50%) ──────────────┤
                               │
    Q1 (25%) ──────────────────┤
                               │
    Minimum (whisker bottom) ──┴
    
    • Outliers shown as dots

SIMPLE EXPLANATION:
Test scores of 100 students:
- Box shows where most students scored
- Line in box = average student score
- Dots outside = unusual scores (very high/low)
"""

# Sample data
scores = pd.DataFrame({
    'Class A': [75, 80, 85, 90, 95, 78, 82, 88],
    'Class B': [60, 65, 70, 72, 75, 68, 71, 74],
    'Class C': [85, 87, 90, 92, 95, 88, 91, 93]
})

print("\nExample: Compare class scores")
scores.plot(kind='box', title='Score Distribution by Class')
plt.ylabel('Score')
plt.tight_layout()
plt.savefig('/tmp/box_plot.png')
plt.close()
print("Box plot created")
print("  - Compare 3 classes at once")
print("  - See which class has higher/lower scores")
print("  - Identify outlier students")

# ============================================================================
# PART 7: AREA PLOT
# ============================================================================
print("\n" + "=" * 80)
print("PART 7: AREA PLOT")
print("=" * 80)

"""
WHAT IS AN AREA PLOT?
=====================
- Like line plot but area under line is filled
- Shows cumulative totals
- Good for showing volume/magnitude

WHEN TO USE:
============
✓ Show cumulative data (total over time)
✓ Compare multiple series (stacked areas)
✓ Emphasize magnitude (how much, not just trend)

STACKED VS UNSTACKED:
=====================
Stacked (stacked=True):
- Areas stack on top of each other
- Shows total and individual contributions
- Like building blocks

Unstacked (stacked=False):
- Areas overlap
- Can see individual values clearly

SIMPLE EXPLANATION:
Filling a bucket with water over time
Area plot shows:
- How full the bucket is (total)
- If you add multiple sources (stack them)
"""

print("\nExample: Stacked area (sales breakdown)")
df[['sales', 'profit', 'expenses']].plot(kind='area', stacked=True, 
                                          title='Sales Breakdown Over Time')
plt.ylabel('Amount ($)')
plt.tight_layout()
plt.savefig('/tmp/area_plot.png')
plt.close()
print("Area plot created")
print("  - Shows total and parts")
print("  - Easy to see contribution of each component")

# ============================================================================
# COMMON PLOT PARAMETERS
# ============================================================================
print("\n" + "=" * 80)
print("COMMON PLOT PARAMETERS ")
print("=" * 80)

"""
BASIC SYNTAX:
=============
df.plot(
    x='column_name',      # What goes on X-axis
    y='column_name',      # What goes on Y-axis
    kind='type',          # Type of plot (line, bar, scatter, etc.)
    title='Title',        # Chart title
    figsize=(10, 6),      # Size (width, height) in inches
    color='red',          # Color
    grid=True,            # Show grid lines
    legend=True           # Show legend
)

COMMON PARAMETERS EXPLAINED:
============================

1. kind: Type of chart
   - 'line': Line plot
   - 'bar': Vertical bar
   - 'barh': Horizontal bar
   - 'hist': Histogram
   - 'scatter': Scatter plot
   - 'pie': Pie chart
   - 'box': Box plot
   - 'area': Area plot

2. figsize: Chart size
   - (10, 6) = 10 inches wide, 6 inches tall
   - Larger = bigger chart
   - Default: (6, 4)

3. color: Chart color
   - 'red', 'blue', 'green'
   - '#FF5733' (hex color)
   - ['red', 'blue'] for multiple series

4. title: Chart title
   - Descriptive name
   - Appears at top

5. grid: Show grid lines
   - True: Show grid (easier to read values)
   - False: No grid (cleaner look)

6. legend: Show legend
   - True: Show labels for each line/bar
   - False: Hide legend

7. xlabel, ylabel: Axis labels
   - plt.xlabel('Month')
   - plt.ylabel('Sales ($)')

SIMPLE EXAMPLE:
===============
"""

print("\nExample: Customized plot")
df.plot(
    x='month',
    y='sales',
    kind='line',
    title='Monthly Sales (Customized)',
    figsize=(8, 5),
    color='green',
    grid=True,
    linewidth=2,
    marker='o'  # Add dots on points
)
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.tight_layout()
plt.savefig('/tmp/customized.png')
plt.close()
print(" Customized plot created")
print("  - Green color")
print("  - Grid lines for easy reading")
print("  - Markers on data points")
print("  - Custom size")



# ============================================================================
# SAVING PLOTS
# ============================================================================
print("\n" + "=" * 80)
print("SAVING PLOTS")
print("=" * 80)

"""
HOW TO SAVE PLOTS:
==================

METHOD 1: Using pandas (simple)
--------------------------------
df.plot(kind='line')
plt.savefig('my_plot.png')  # Save as PNG
plt.close()  # Close to free memory

METHOD 2: With options
-----------------------
plt.savefig('plot.png', 
            dpi=300,              # Quality (higher = better)
            bbox_inches='tight',  # Remove extra white space
            transparent=True)     # Transparent background

FILE FORMATS:
=============
.png  - Best for presentations, web (good quality)
.jpg  - Smaller file size (some quality loss)
.pdf  - Best for printing (vector format)
.svg  - Scalable (vector format)

SIMPLE EXPLANATION:
Save like saving a Word document
Choose format based on where you'll use it
"""

print("\nExample: Save plot in different formats")
df.plot(x='month', y='sales', kind='line')
plt.savefig('/tmp/plot.png', dpi=150, bbox_inches='tight')
plt.savefig('/tmp/plot.pdf', bbox_inches='tight')
plt.close()
print(" Saved as PNG (for screen)")
print(" Saved as PDF (for printing)")

print("\n" + "=" * 80)
print("DATA VISUALIZATION")
print("=" * 80)
print("\nKEY TAKEAWAY:")
print("Choose plot based on what you want to show:")
print("  Trend? → Line")
print("  Compare? → Bar")
print("  Distribution? → Histogram")
print("  Relationship? → Scatter")
print("  Percentage? → Pie")