# Class 4 – Exploratory Data Visualization
## Student Exercises

**Instructions**: Complete the following exercises to practice exploratory data analysis and visualization techniques. Exercises are organized by difficulty level.

---

## EASY LEVEL EXERCISES ⭐

---

## Exercise 1: Simple Histogram Analysis

**Difficulty**: ⭐ Easy  
**Time Estimate**: 10 minutes  
**Dataset**: `student_scores.csv`

### Scenario
You are a teaching assistant analyzing exam scores from a statistics course. The professor wants to understand the score distribution to determine if the exam difficulty was appropriate.

### Dataset Description
- **File**: `Class4/data/student_scores.csv`
- **Size**: 200 students
- **Variables**:
  - `student_id`: Unique identifier (1-200)
  - `exam_score`: Final exam score (0-100)

### Learning Objectives
- Load and explore data with pandas
- Calculate basic descriptive statistics
- Create histograms with matplotlib
- Interpret distribution shapes
- Add reference lines to visualizations

### Tasks

**1. Load and Explore the Data**
   - Read the CSV file using pandas
   - Display the first 10 rows
   - Check the shape of the dataset
   - Verify there are no missing values

**2. Calculate Basic Statistics**
   - Calculate mean, median, standard deviation
   - Find the minimum and maximum scores
   - Determine the range (max - min)

**3. Create a Histogram**
   - Plot a histogram with 20 bins
   - Add vertical lines for mean (red, dashed) and median (green, dashed)
   - Label the x-axis as "Exam Score" and y-axis as "Frequency"
   - Add a title: "Distribution of Exam Scores"
   - Include a legend showing mean and median

**4. Interpret the Results**
   - Is the distribution symmetric, left-skewed, or right-skewed?
   - Are mean and median close to each other? What does this tell you?
   - Are most students clustered around a certain score range?
   - Based on the distribution, was the exam difficulty appropriate?

### Data Manipulation Guide
```python
# Loading data
df = pd.read_csv('Class4/data/student_scores.csv')

# Calculating statistics
mean_score = df['exam_score'].mean()
median_score = df['exam_score'].median()
std_score = df['exam_score'].std()

# Creating histogram
plt.hist(df['exam_score'], bins=20, edgecolor='black', alpha=0.7)
plt.axvline(mean_score, color='red', linestyle='--', label='Mean')
plt.axvline(median_score, color='green', linestyle='--', label='Median')
```

### Expected Visualization
A histogram showing the frequency distribution of exam scores with clear reference lines for mean and median.

### Starter Code

```python
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# TODO: Load the data
df = pd.read_csv('Class4/data/student_scores.csv')

# TODO: Display first 10 rows
print(df.head(10))

# TODO: Check shape and missing values
print(f"Dataset shape: {df.shape}")
print(f"Missing values:\n{df.isnull().sum()}")

# TODO: Calculate basic statistics
mean_score = # Calculate mean
median_score = # Calculate median
std_score = # Calculate standard deviation
min_score = # Calculate minimum
max_score = # Calculate maximum

print(f"\n=== EXAM SCORE STATISTICS ===")
print(f"Mean: {mean_score:.2f}")
print(f"Median: {median_score:.2f}")
print(f"Std Dev: {std_score:.2f}")
print(f"Range: {min_score:.2f} - {max_score:.2f}")

# TODO: Create histogram with reference lines
plt.figure(figsize=(10, 6))

# Create histogram


# Add vertical lines for mean and median


# Add labels and title


# Add legend


# Display the plot
plt.show()

# TODO: Answer interpretation questions
print("\n=== INTERPRETATION ===")
print("1. Distribution shape: ")
print("2. Mean vs Median: ")
print("3. Score clustering: ")
print("4. Exam difficulty assessment: ")
```

### Success Criteria
- ✅ Data loaded successfully with 200 rows
- ✅ All statistics calculated correctly
- ✅ Histogram created with 20 bins
- ✅ Mean and median lines visible and labeled
- ✅ Clear interpretation of distribution provided

---

## Exercise 2: Basic Box Plot Comparison

**Difficulty**: ⭐ Easy  
**Time Estimate**: 12 minutes  
**Dataset**: `employee_salaries.csv`

### Scenario
You're a HR analyst examining salary distributions across different departments. Management wants to ensure compensation is fair and identify any unusual salary outliers.

### Dataset Description
- **File**: `Class4/data/employee_salaries.csv`
- **Size**: 500 employees
- **Variables**:
  - `employee_id`: Unique identifier
  - `department`: Department name (Engineering, Sales, Marketing, HR)
  - `salary`: Annual salary in USD
  - `years_experience`: Years of professional experience

### Learning Objectives
- Work with categorical and numeric variables
- Create grouped box plots
- Identify outliers visually
- Compare distributions across categories
- Use seaborn for statistical visualizations

### Tasks

**1. Load and Explore the Data**
   - Read the CSV file
   - Display the first 10 rows
   - Check data types and missing values
   - Count employees per department

**2. Basic Data Quality Checks**
   - Verify no missing values in key columns
   - Check for duplicate employee IDs
   - Display unique departments
   - Show salary range by department

**3. Create Side-by-Side Box Plots**
   - Create box plots comparing salary across departments
   - Use seaborn's boxplot function
   - Rotate x-axis labels if needed for readability
   - Add appropriate title and labels
   - Use a color palette for visual appeal

**4. Identify and Analyze Outliers**
   - Which department has the highest median salary?
   - Which department has the widest salary range?
   - Identify specific outliers (if any) in each department
   - Are outliers above or below the typical range?

**5. Interpretation**
   - Which department pays the most on average?
   - Is there overlap in salary ranges between departments?
   - Should management investigate any outliers?

### Data Manipulation Guide
```python
# Group statistics
department_stats = df.groupby('department')['salary'].describe()

# Create box plots
sns.boxplot(x='department', y='salary', data=df)

# Count per category
department_counts = df['department'].value_counts()

# Identify outliers using IQR method
Q1 = df['salary'].quantile(0.25)
Q3 = df['salary'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['salary'] < Q1 - 1.5*IQR) | (df['salary'] > Q3 + 1.5*IQR)]
```

### Expected Visualization
Side-by-side box plots showing salary distributions for each department, with clear median lines, quartiles, and any outliers marked as points.

### Starter Code

```python
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# TODO: Load the data
df = pd.read_csv('Class4/data/employee_salaries.csv')

# TODO: Explore the data
print("First 10 rows:")
print(df.head(10))

print(f"\nDataset shape: {df.shape}")
print(f"\nData types:\n{df.dtypes}")
print(f"\nMissing values:\n{df.isnull().sum()}")

# TODO: Count employees per department
print("\n=== EMPLOYEES PER DEPARTMENT ===")
# Your code here

# TODO: Check for duplicates
duplicate_count = df.duplicated(subset=['employee_id']).sum()
print(f"\nDuplicate employee IDs: {duplicate_count}")

# TODO: Show unique departments
print(f"\nDepartments: {df['department'].unique()}")

# TODO: Calculate salary statistics by department
print("\n=== SALARY STATISTICS BY DEPARTMENT ===")
# Your code here

# TODO: Create box plots
plt.figure(figsize=(10, 6))

# Create boxplot using seaborn


# Add title and labels


# Rotate x-axis labels if needed


# Display plot
plt.tight_layout()
plt.show()

# TODO: Identify outliers for each department
print("\n=== OUTLIER ANALYSIS ===")
for dept in df['department'].unique():
    dept_data = df[df['department'] == dept]['salary']
    Q1 = dept_data.quantile(0.25)
    Q3 = dept_data.quantile(0.75)
    IQR = Q3 - Q1
    
    # Calculate outlier bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Find outliers
    outliers = dept_data[(dept_data < lower_bound) | (dept_data > upper_bound)]
    
    print(f"\n{dept}:")
    print(f"  Median salary: ${dept_data.median():,.2f}")
    print(f"  IQR: ${IQR:,.2f}")
    print(f"  Number of outliers: {len(outliers)}")
    if len(outliers) > 0:
        print(f"  Outlier values: {outliers.values}")

# TODO: Answer interpretation questions
print("\n=== INTERPRETATION ===")
print("1. Highest median salary department: ")
print("2. Widest salary range department: ")
print("3. Salary overlap between departments: ")
print("4. Recommendation on outliers: ")
```

### Success Criteria
- ✅ Data loaded with all 500 employees
- ✅ Box plots created for all departments
- ✅ Outliers identified and counted
- ✅ Median salary comparison completed
- ✅ Clear recommendations provided

---

## Exercise 3: Simple Scatter Plot Relationship

**Difficulty**: ⭐ Easy  
**Time Estimate**: 15 minutes  
**Dataset**: `house_simple.csv`

### Scenario
You're a real estate analyst helping a client understand home prices. They want to know if there's a clear relationship between house size and price to make informed buying decisions.

### Dataset Description
- **File**: `Class4/data/house_simple.csv`
- **Size**: 300 houses
- **Variables**:
  - `house_id`: Unique identifier
  - `sqft`: Square footage of the house
  - `price`: Selling price in USD

### Learning Objectives
- Create scatter plots for bivariate analysis
- Calculate and interpret correlation coefficients
- Add regression lines to show trends
- Understand linear relationships
- Interpret strength and direction of relationships

### Tasks

**1. Load and Explore the Data**
   - Read the CSV file
   - Display the first 10 rows
   - Check for missing values
   - Display basic statistics for both variables

**2. Calculate Correlation**
   - Calculate Pearson correlation coefficient between sqft and price
   - Interpret the correlation value:
     - |r| > 0.7 = Strong relationship
     - 0.4 < |r| < 0.7 = Moderate relationship
     - |r| < 0.4 = Weak relationship

**3. Create a Scatter Plot**
   - Plot sqft on x-axis, price on y-axis
   - Use appropriate point size and transparency
   - Add a regression line to show the trend
   - Label axes clearly with units
   - Add a title including the correlation coefficient

**4. Analyze the Relationship**
   - Is the relationship positive or negative?
   - Is the relationship linear or non-linear?
   - Are there any obvious outliers?
   - How well does square footage predict price?
   - Based on the plot, approximately how much does price increase per 100 sqft?

### Data Manipulation Guide
```python
# Calculate correlation
correlation = df['sqft'].corr(df['price'])

# Create scatter plot
plt.scatter(df['sqft'], df['price'], alpha=0.5)

# Add regression line using seaborn
sns.regplot(x='sqft', y='price', data=df, scatter_kws={'alpha':0.5})

# Calculate regression coefficients
from scipy import stats
slope, intercept, r_value, p_value, std_err = stats.linregress(df['sqft'], df['price'])
```

### Expected Visualization
A scatter plot showing the relationship between house size and price, with a fitted regression line clearly showing the trend.

### Starter Code

```python
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

# TODO: Load the data
df = pd.read_csv('Class4/data/house_simple.csv')

# TODO: Explore the data
print("First 10 rows:")
print(df.head(10))

print(f"\nDataset shape: {df.shape}")
print(f"\nMissing values:\n{df.isnull().sum()}")

print("\n=== BASIC STATISTICS ===")
print(df[['sqft', 'price']].describe())

# TODO: Calculate correlation coefficient
correlation = # Calculate correlation between sqft and price

print(f"\n=== CORRELATION ANALYSIS ===")
print(f"Correlation coefficient: {correlation:.3f}")

# Interpret correlation strength
if abs(correlation) > 0.7:
    strength = "Strong"
elif abs(correlation) > 0.4:
    strength = "Moderate"
else:
    strength = "Weak"

direction = "positive" if correlation > 0 else "negative"
print(f"Interpretation: {strength} {direction} relationship")

# TODO: Create scatter plot with regression line
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Left plot: Basic scatter plot
axes[0].scatter(df['sqft'], df['price'], alpha=0.5, color='blue')
axes[0].set_xlabel('Square Feet')
axes[0].set_ylabel('Price ($)')
axes[0].set_title('House Size vs Price')
axes[0].grid(True, alpha=0.3)

# Right plot: Scatter plot with regression line
sns.regplot(x='sqft', y='price', data=df, ax=axes[1], 
            scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
axes[1].set_xlabel('Square Feet')
axes[1].set_ylabel('Price ($)')
axes[1].set_title(f'House Size vs Price (r = {correlation:.3f})')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# TODO: Calculate regression equation
slope, intercept, r_value, p_value, std_err = stats.linregress(df['sqft'], df['price'])

print("\n=== REGRESSION ANALYSIS ===")
print(f"Equation: Price = {intercept:,.2f} + {slope:.2f} × Square Feet")
print(f"R-squared: {r_value**2:.3f}")
print(f"For every 100 sqft increase, price increases by: ${slope * 100:,.2f}")

# TODO: Identify potential outliers
# Calculate residuals
predicted_price = intercept + slope * df['sqft']
residuals = df['price'] - predicted_price
std_residual = residuals.std()

# Flag houses with large residuals (> 2 standard deviations)
outliers = df[abs(residuals) > 2 * std_residual]

print(f"\n=== OUTLIER DETECTION ===")
print(f"Number of potential outliers: {len(outliers)}")
if len(outliers) > 0:
    print("\nOutlier details:")
    print(outliers[['house_id', 'sqft', 'price']])

# TODO: Answer interpretation questions
print("\n=== INTERPRETATION ===")
print("1. Relationship direction: ")
print("2. Relationship linearity: ")
print("3. Prediction quality: ")
print("4. Price increase per 100 sqft: ")
print("5. Investment advice: ")
```

### Success Criteria
- ✅ Data loaded with 300 houses
- ✅ Correlation coefficient calculated and interpreted
- ✅ Scatter plot with regression line created
- ✅ Regression equation calculated
- ✅ Clear interpretation of the relationship provided

---

## Tips for Success

**For All Easy Exercises:**
1. **Read Carefully**: Make sure you understand what each task is asking
2. **Test Incrementally**: Run your code frequently to catch errors early
3. **Check Your Work**: Verify your calculations make sense
4. **Visualize Thoughtfully**: Labels, titles, and legends make plots professional
5. **Interpret Honestly**: Say what you see in the data, not what you expect

**Common Mistakes to Avoid:**
- ❌ Forgetting to import required libraries
- ❌ Using wrong column names (check spelling!)
- ❌ Not handling missing values
- ❌ Forgetting axis labels or titles
- ❌ Not explaining your interpretations

**Getting Help:**
- Review the lecture notes on distribution analysis
- Check the starter code for syntax examples
- Use `df.head()` and `df.info()` to understand your data
- Google error messages - they're usually helpful!

---

## What's Next?

Once you complete these easy exercises, you'll be ready for:
- **Medium Level**: Multi-variable analysis, transformations, time series
- **Hard Level**: Missing data strategies, comprehensive EDA workflows, feature engineering

**Remember**: The goal isn't just to create plots - it's to understand your data and extract insights!

---

**Good luck! 🚀**

---

## MEDIUM LEVEL EXERCISES ⭐⭐

---

## Exercise 4: Multi-Variable Distribution Analysis

**Difficulty**: ⭐⭐ Medium  
**Time Estimate**: 20 minutes  
**Dataset**: `customer_transactions.csv`

### Scenario
You're analyzing customer transaction data for an e-commerce company. The data shows a right-skewed distribution with some extreme values. You need to determine if transformations are necessary before modeling and identify any problematic outliers.

### Dataset Description
- **File**: `Class4/data/customer_transactions.csv`
- **Size**: 10,000 transactions
- **Variables**:
  - `transaction_id`: Unique identifier
  - `amount`: Transaction amount in USD
  - `date`: Transaction date
  - `category`: Product category
  - `customer_type`: New, Regular, or Premium

### Learning Objectives
- Detect and quantify skewness in distributions
- Apply data transformations (log, square root, Box-Cox)
- Create multi-panel visualization comparisons
- Use Q-Q plots to assess normality
- Make informed decisions about data preprocessing

### Tasks

**1. Load and Initial Assessment**
   - Load the data and check basic info
   - Calculate skewness of the amount variable
   - Determine if transformation is needed (rule: |skew| > 1)

**2. Create a 2x2 Subplot Comparison**
   - **Top Left**: Histogram of original distribution
   - **Top Right**: Box plot of original distribution
   - **Bottom Left**: Histogram of log-transformed distribution
   - **Bottom Right**: Q-Q plot comparing to normal distribution

**3. Apply and Compare Transformations**
   - Log transformation: `np.log(amount + 1)`
   - Square root transformation: `np.sqrt(amount)`
   - Calculate skewness for each transformation
   - Determine which transformation best normalizes the data

**4. Outlier Detection**
   - Use IQR method on original data
   - Count outliers and calculate percentage
   - Examine outlier characteristics (which categories?)
   - Decide: legitimate extreme values or errors?

**5. Recommendation**
   - Which transformation do you recommend?
   - Should outliers be removed, capped, or kept?
   - What impact might this have on analysis?

### Data Manipulation Guide
```python
# Calculate skewness
skewness = df['amount'].skew()

# Apply log transformation
df['amount_log'] = np.log(df['amount'] + 1)

# Create Q-Q plot
from scipy import stats
stats.probplot(df['amount'], dist="norm", plot=plt)

# Box-Cox transformation (for positive data)
from scipy.stats import boxcox
transformed, lambda_param = boxcox(df['amount'] + 1)
```

### Expected Visualization
A 2x2 grid showing original and transformed distributions from multiple perspectives, clearly demonstrating the effect of transformation.

### Starter Code

```python
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

# TODO: Load the data
df = pd.read_csv('Class4/data/customer_transactions.csv')

# TODO: Initial exploration
print("Dataset shape:", df.shape)
print("\nFirst few rows:")
print(df.head())
print("\nBasic statistics:")
print(df['amount'].describe())

# TODO: Calculate skewness
original_skew = df['amount'].skew()
print(f"\n=== SKEWNESS ANALYSIS ===")
print(f"Original skewness: {original_skew:.3f}")

if abs(original_skew) > 1:
    print("⚠️ Data is heavily skewed - transformation recommended")
else:
    print("✅ Data is fairly symmetric - transformation may not be needed")

# TODO: Apply transformations
df['amount_log'] = np.log(df['amount'] + 1)
df['amount_sqrt'] = np.sqrt(df['amount'])

# Calculate skewness for transformations
log_skew = df['amount_log'].skew()
sqrt_skew = df['amount_sqrt'].skew()

print(f"\nLog transformation skewness: {log_skew:.3f}")
print(f"Square root transformation skewness: {sqrt_skew:.3f}")

# TODO: Create 2x2 visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Top Left: Original histogram
axes[0, 0].hist(df['amount'], bins=50, edgecolor='black', alpha=0.7, color='blue')
axes[0, 0].axvline(df['amount'].mean(), color='red', linestyle='--', label='Mean')
axes[0, 0].axvline(df['amount'].median(), color='green', linestyle='--', label='Median')
axes[0, 0].set_title(f'Original Distribution (Skew: {original_skew:.2f})')
axes[0, 0].set_xlabel('Amount ($)')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].legend()

# Top Right: Original box plot


# Bottom Left: Log-transformed histogram


# Bottom Right: Q-Q plot


plt.tight_layout()
plt.show()

# TODO: Outlier detection using IQR method
Q1 = df['amount'].quantile(0.25)
Q3 = df['amount'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['amount'] < lower_bound) | (df['amount'] > upper_bound)]

print(f"\n=== OUTLIER ANALYSIS ===")
print(f"Number of outliers: {len(outliers)} ({len(outliers)/len(df)*100:.2f}%)")
print(f"Outlier bounds: ${lower_bound:.2f} - ${upper_bound:.2f}")

if len(outliers) > 0:
    print("\nOutlier distribution by category:")
    print(outliers['category'].value_counts())
    print("\nOutlier distribution by customer type:")
    print(outliers['customer_type'].value_counts())

# TODO: Compare transformations side-by-side
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].hist(df['amount'], bins=50, edgecolor='black', alpha=0.7)
axes[0].set_title(f'Original (Skew: {original_skew:.2f})')
axes[0].set_xlabel('Amount')

axes[1].hist(df['amount_log'], bins=50, edgecolor='black', alpha=0.7)
axes[1].set_title(f'Log Transformed (Skew: {log_skew:.2f})')
axes[1].set_xlabel('Log(Amount + 1)')

axes[2].hist(df['amount_sqrt'], bins=50, edgecolor='black', alpha=0.7)
axes[2].set_title(f'Square Root (Skew: {sqrt_skew:.2f})')
axes[2].set_xlabel('√Amount')

plt.tight_layout()
plt.show()

# TODO: Answer questions
print("\n=== RECOMMENDATIONS ===")
print("1. Best transformation: ")
print("2. Outlier handling: ")
print("3. Impact on analysis: ")
```

### Success Criteria
- ✅ Skewness calculated for original and transformed data
- ✅ 2x2 visualization created showing multiple perspectives
- ✅ Outliers identified and analyzed
- ✅ Clear transformation recommendation with justification
- ✅ Outlier handling strategy explained

### Hints
- 💡 Log transformation works well for right-skewed data
- 💡 Q-Q plot points should follow diagonal line for normal data
- 💡 Not all outliers are errors - premium customers may have high transactions
- 💡 The "best" transformation brings skewness closest to 0

---

## Exercise 5: Correlation Heatmap & Feature Selection

**Difficulty**: ⭐⭐ Medium  
**Time Estimate**: 25 minutes  
**Dataset**: `real_estate.csv`

### Scenario
You're building a price prediction model for real estate. Before modeling, you need to understand which features are most predictive of price and identify any multicollinearity issues that could cause problems.

### Dataset Description
- **File**: `Class4/data/real_estate.csv`
- **Size**: 1,000 properties
- **Variables**: 12 numeric features including:
  - `price`: Target variable (selling price)
  - `sqft`: Square footage
  - `bedrooms`: Number of bedrooms
  - `bathrooms`: Number of bathrooms
  - `age`: Property age in years
  - `lot_size`: Lot size in acres
  - `garage_spaces`: Number of garage spaces
  - `distance_to_city`: Miles to city center
  - `crime_rate`: Neighborhood crime rate
  - `school_rating`: Local school rating (1-10)
  - `condition_score`: Property condition (1-10)
  - `renovation_year`: Year of last renovation

### Learning Objectives
- Calculate correlation matrices
- Create and interpret correlation heatmaps
- Identify multicollinearity issues
- Select relevant features for modeling
- Use pair plots for detailed relationship analysis

### Tasks

**1. Load and Prepare Data**
   - Load the dataset
   - Check for missing values
   - Verify all variables are numeric
   - Display correlation with target variable (price)

**2. Create Correlation Matrix Visualizations**
   - Calculate full correlation matrix
   - Create heatmap with annotations
   - Create lower triangle heatmap (no redundancy)
   - Filter to show only strong correlations (|r| > 0.5)

**3. Identify Top Features**
   - Find top 5 features most correlated with price
   - Create a horizontal bar chart of correlations
   - Sort by absolute correlation value

**4. Check for Multicollinearity**
   - Identify pairs with |r| > 0.8 (problematic)
   - List highly correlated feature pairs
   - Recommend which features to keep/drop

**5. Create Pair Plot**
   - Select top 5 features + price
   - Create pair plot to visualize relationships
   - Look for non-linear patterns

**6. Feature Selection Recommendation**
   - Which features should definitely be included?
   - Which features should be dropped due to multicollinearity?
   - Are there any interaction terms to consider?

### Data Manipulation Guide
```python
# Correlation matrix
corr_matrix = df.corr()

# Heatmap with triangle mask
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', cmap='coolwarm')

# Get correlations with target
price_corr = corr_matrix['price'].sort_values(ascending=False)

# Find high correlations
high_corr = []
for i in range(len(corr_matrix.columns)):
    for j in range(i+1, len(corr_matrix.columns)):
        if abs(corr_matrix.iloc[i, j]) > 0.8:
            high_corr.append((corr_matrix.columns[i], 
                            corr_matrix.columns[j], 
                            corr_matrix.iloc[i, j]))
```

### Expected Visualization
Multiple heatmaps showing correlation patterns, a bar chart of top features, and a pair plot for detailed relationship analysis.

### Starter Code

```python
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# TODO: Load the data
df = pd.read_csv('Class4/data/real_estate.csv')

# TODO: Initial exploration
print("Dataset shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())
print("\nData types:")
print(df.dtypes)

# TODO: Calculate correlation matrix
corr_matrix = df.corr()

# TODO: Display correlations with price
print("\n=== CORRELATIONS WITH PRICE ===")
price_corr = corr_matrix['price'].sort_values(ascending=False)
print(price_corr)

# TODO: Create comprehensive heatmap visualization
fig, axes = plt.subplots(1, 3, figsize=(20, 5))

# Full correlation matrix


# Lower triangle only (no redundancy)


# Strong correlations only (|r| > 0.5)


plt.tight_layout()
plt.show()

# TODO: Create bar chart of top correlations with price
top_features = price_corr[1:6]  # Exclude price itself
plt.figure(figsize=(10, 6))
# Your code here


# TODO: Identify multicollinearity issues
print("\n=== MULTICOLLINEARITY ANALYSIS ===")
high_corr_pairs = []
for i in range(len(corr_matrix.columns)):
    for j in range(i+1, len(corr_matrix.columns)):
        if abs(corr_matrix.iloc[i, j]) > 0.8:
            pair = (corr_matrix.columns[i], 
                   corr_matrix.columns[j], 
                   corr_matrix.iloc[i, j])
            high_corr_pairs.append(pair)

if high_corr_pairs:
    print(f"Found {len(high_corr_pairs)} highly correlated pairs (|r| > 0.8):")
    for var1, var2, corr in high_corr_pairs:
        print(f"  {var1} <-> {var2}: r = {corr:.3f}")
else:
    print("No severe multicollinearity detected")

# TODO: Create pair plot for top features
top_5_features = price_corr[1:6].index.tolist()
selected_vars = ['price'] + top_5_features

print(f"\n=== CREATING PAIR PLOT FOR: {selected_vars} ===")
# Your code here


# TODO: Feature selection recommendations
print("\n=== FEATURE SELECTION RECOMMENDATIONS ===")
print("\n1. Highly Predictive Features (|r| > 0.6):")
# Your analysis here

print("\n2. Features to Drop (multicollinearity |r| > 0.8):")
# Your analysis here

print("\n3. Features to Keep:")
# Your analysis here

print("\n4. Potential Interaction Terms:")
# Your suggestions here
```

### Success Criteria
- ✅ Correlation matrix calculated and visualized
- ✅ Top 5 features identified
- ✅ Multicollinearity issues detected
- ✅ Pair plot created for detailed analysis
- ✅ Clear feature selection recommendations provided

### Hints
- 💡 Use `cmap='coolwarm'` for diverging color schemes (red-white-blue)
- 💡 Center the heatmap at 0 for better interpretation
- 💡 If two features are highly correlated, keep the one more correlated with target
- 💡 Look for non-linear patterns in pair plot - may need transformations

---

## Exercise 6: Time Series Pattern Detection

**Difficulty**: ⭐⭐ Medium  
**Time Estimate**: 25 minutes  
**Dataset**: `daily_sales.csv`

### Scenario
You're analyzing 2 years of daily sales data for a retail company. Management wants to understand trends, seasonal patterns, and any unusual spikes or drops that need investigation.

### Dataset Description
- **File**: `Class4/data/daily_sales.csv`
- **Size**: 730 days (2 years)
- **Variables**:
  - `date`: Date (YYYY-MM-DD format)
  - `daily_sales`: Total sales in USD
  - `day_of_week`: Day name (Monday-Sunday)
  - `is_holiday`: Boolean flag for holidays

### Learning Objectives
- Parse and work with datetime data
- Calculate rolling averages for smoothing
- Detect seasonal patterns
- Identify anomalies in time series
- Create multi-panel time series visualizations

### Tasks

**1. Load and Prepare Time Series Data**
   - Load data with proper date parsing
   - Set date as index
   - Sort by date
   - Check for any missing dates or duplicates

**2. Create Initial Time Series Plot**
   - Plot the raw daily sales over time
   - Mark holidays with vertical lines or different colors
   - Identify any obvious trends or patterns

**3. Calculate Rolling Statistics**
   - Calculate 7-day rolling average (weekly smoothing)
   - Calculate 30-day rolling average (monthly smoothing)
   - Plot both on the same chart with the raw data

**4. Analyze Seasonality**
   - Aggregate by day of week - do certain days sell more?
   - Aggregate by month - are there seasonal patterns?
   - Create bar charts showing average sales by day/month

**5. Detect Anomalies**
   - Calculate mean and standard deviation
   - Identify days with sales > 2 std devs from mean
   - Check if anomalies coincide with holidays
   - Investigate the top 10 highest and lowest sales days

**6. Insights and Recommendations**
   - What's the overall trend? (Growing, declining, stable?)
   - What day of week is strongest? Weakest?
   - What seasonal patterns exist?
   - Should any anomalies be investigated further?

### Data Manipulation Guide
```python
# Parse dates
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
df = df.sort_index()

# Rolling averages
df['rolling_7'] = df['daily_sales'].rolling(window=7).mean()
df['rolling_30'] = df['daily_sales'].rolling(window=30).mean()

# Resample for aggregations
monthly_avg = df['daily_sales'].resample('M').mean()
weekly_avg = df['daily_sales'].resample('W').mean()

# Day of week analysis
day_avg = df.groupby('day_of_week')['daily_sales'].mean()
```

### Expected Visualization
A multi-panel visualization showing: (1) raw time series with rolling averages, (2) day-of-week patterns, (3) monthly seasonal patterns, and (4) anomaly detection.

### Starter Code

```python
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# TODO: Load data with date parsing
df = pd.read_csv('Class4/data/daily_sales.csv', parse_dates=['date'])
df = df.set_index('date')
df = df.sort_index()

# TODO: Initial exploration
print("Dataset shape:", df.shape)
print("\nDate range:", df.index.min(), "to", df.index.max())
print("\nFirst few rows:")
print(df.head())
print("\nBasic statistics:")
print(df['daily_sales'].describe())

# TODO: Check for missing dates
date_range = pd.date_range(start=df.index.min(), end=df.index.max(), freq='D')
missing_dates = date_range.difference(df.index)
print(f"\nMissing dates: {len(missing_dates)}")

# TODO: Calculate rolling averages
df['rolling_7'] = df['daily_sales'].rolling(window=7).mean()
df['rolling_30'] = df['daily_sales'].rolling(window=30).mean()

# TODO: Create comprehensive time series visualization
fig, axes = plt.subplots(3, 1, figsize=(15, 12))

# Plot 1: Raw data with rolling averages
axes[0].plot(df.index, df['daily_sales'], alpha=0.3, label='Daily Sales')
axes[0].plot(df.index, df['rolling_7'], linewidth=2, label='7-Day Average')
axes[0].plot(df.index, df['rolling_30'], linewidth=2, label='30-Day Average')

# Mark holidays
holiday_dates = df[df['is_holiday'] == True].index
for hdate in holiday_dates:
    axes[0].axvline(hdate, color='red', alpha=0.2, linewidth=0.5)

axes[0].set_title('Daily Sales with Rolling Averages')
axes[0].set_ylabel('Sales ($)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Plot 2: Day of week analysis


# Plot 3: Monthly aggregation


plt.tight_layout()
plt.show()

# TODO: Anomaly detection
mean_sales = df['daily_sales'].mean()
std_sales = df['daily_sales'].std()

# Define anomaly thresholds (±2 standard deviations)
upper_threshold = mean_sales + 2 * std_sales
lower_threshold = mean_sales - 2 * std_sales

anomalies = df[(df['daily_sales'] > upper_threshold) | 
               (df['daily_sales'] < lower_threshold)]

print(f"\n=== ANOMALY DETECTION ===")
print(f"Mean sales: ${mean_sales:,.2f}")
print(f"Std dev: ${std_sales:,.2f}")
print(f"Upper threshold: ${upper_threshold:,.2f}")
print(f"Lower threshold: ${lower_threshold:,.2f}")
print(f"\nNumber of anomalies: {len(anomalies)} ({len(anomalies)/len(df)*100:.1f}%)")

if len(anomalies) > 0:
    print("\nTop 5 highest sales days:")
    print(df.nlargest(5, 'daily_sales')[['daily_sales', 'day_of_week', 'is_holiday']])
    
    print("\nTop 5 lowest sales days:")
    print(df.nsmallest(5, 'daily_sales')[['daily_sales', 'day_of_week', 'is_holiday']])

# TODO: Seasonality analysis
print("\n=== SEASONALITY ANALYSIS ===")

# Day of week analysis
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_avg = df.groupby('day_of_week')['daily_sales'].mean().reindex(day_order)
print("\nAverage sales by day of week:")
print(day_avg)

# Monthly analysis
df_monthly = df.resample('M')['daily_sales'].mean()
print("\nAverage sales by month:")
print(df_monthly)

# TODO: Answer questions
print("\n=== INSIGHTS & RECOMMENDATIONS ===")
print("1. Overall trend: ")
print("2. Best day of week: ")
print("3. Seasonal patterns: ")
print("4. Anomalies to investigate: ")
```

### Success Criteria
- ✅ Time series properly loaded and indexed by date
- ✅ Rolling averages calculated and visualized
- ✅ Day-of-week and monthly patterns identified
- ✅ Anomalies detected using statistical thresholds
- ✅ Clear insights about trends and patterns provided

### Hints
- 💡 Use `pd.to_datetime()` for date parsing
- 💡 Rolling averages smooth out noise and reveal trends
- 💡 Holidays often cause spikes - mark them on your plot
- 💡 Compare patterns: weekday vs weekend, month-to-month
- 💡 Use `resample()` for aggregating to different time periods

---

## Tips for Medium Exercises

**Key Skills for This Level:**
- ✅ Comparing multiple visualization types
- ✅ Applying data transformations
- ✅ Working with time series data
- ✅ Detecting patterns and anomalies
- ✅ Making data-driven recommendations

**Common Challenges:**
- ⚠️ Choosing the right transformation
- ⚠️ Interpreting correlation vs causation
- ⚠️ Handling datetime data properly
- ⚠️ Deciding which outliers to keep/remove

**Time Management:**
- Spend 5 min understanding the scenario
- Spend 10 min on analysis and visualization
- Spend 5 min on interpretation and recommendations

---

**Ready for the hard exercises? They combine everything you've learned! 💪**

---

## HARD LEVEL EXERCISES ⭐⭐⭐

---

## Exercise 7: Missing Data Investigation & Strategy

**Difficulty**: ⭐⭐⭐ Hard  
**Time Estimate**: 30 minutes  
**Dataset**: `customer_survey.csv`

### Scenario
You're analyzing a customer satisfaction survey with 20 questions. About 15% of responses are missing, but the pattern isn't random. You need to determine the missingness type, test your hypotheses, and choose the best imputation strategy before analysis.

### Dataset Description
- **File**: `Class4/data/customer_survey.csv`
- **Size**: 5,000 respondents
- **Variables**: 20 survey questions + demographics
  - `respondent_id`: Unique identifier
  - `age`: Age in years
  - `income`: Annual income (USD)
  - `education`: Education level (High School, Bachelor, Master, PhD)
  - `q1` - `q20`: Survey responses (1-5 scale or missing)
  - Some questions have structured missingness patterns

### Learning Objectives
- Diagnose missingness types (MCAR, MAR, MNAR)
- Create comprehensive missing data visualizations
- Test hypotheses about missingness mechanisms
- Implement multiple imputation methods
- Compare imputation quality
- Make evidence-based recommendations

### Tasks

**1. Initial Missing Data Assessment**
   - Calculate missing percentages for all variables
   - Create bar chart showing missing data by variable
   - Identify which variables have most missing data
   - Calculate total missing data points

**2. Visualize Missing Patterns**
   - Create missing data heatmap
   - Calculate missingness correlation matrix
   - Check if certain questions tend to be missing together
   - Analyze missing data distribution across rows

**3. Test Missingness Type**
   - **Test for MCAR**: Are missing values random?
   - **Test for MAR**: Does age correlate with income missingness?
   - **Test for MAR**: Does education level correlate with missingness?
   - Create box plots comparing demographics by missingness status

**4. Implement Imputation Methods**
   - **Method 1**: Mean/Mode imputation (simple baseline)
   - **Method 2**: KNN imputation (k=5)
   - **Method 3**: Iterative imputation (MICE algorithm)
   - Keep original data for comparison

**5. Compare Imputation Quality**
   - Compare distributions before/after imputation
   - Calculate how much each method changes the distribution
   - Check if correlations are preserved
   - Create side-by-side visualizations

**6. Recommendation**
   - What is the likely missingness type?
   - Which imputation method is best for this data?
   - What are the risks of each approach?
   - Should any variables be dropped instead?

### Data Manipulation Guide
```python
# Missing data patterns
import missingno as msno  # Optional visualization library
msno.matrix(df)
msno.heatmap(df)

# Test if age differs by income missingness
income_missing = df['income'].isnull()
from scipy.stats import ttest_ind
t_stat, p_value = ttest_ind(df[income_missing]['age'].dropna(), 
                             df[~income_missing]['age'].dropna())

# KNN Imputation
from sklearn.impute import KNNImputer
knn_imputer = KNNImputer(n_neighbors=5)
df_knn = pd.DataFrame(knn_imputer.fit_transform(df_numeric), 
                      columns=df_numeric.columns)

# Iterative Imputation
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
iter_imputer = IterativeImputer(random_state=42, max_iter=10)
df_iter = pd.DataFrame(iter_imputer.fit_transform(df_numeric),
                       columns=df_numeric.columns)
```

### Expected Visualization
A comprehensive 2x3 grid showing missing patterns, imputation comparisons, and distribution preservation checks.

### Starter Code

```python
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# TODO: Load the data
df = pd.read_csv('Class4/data/customer_survey.csv')

print("Dataset shape:", df.shape)
print("\nFirst few rows:")
print(df.head())

# TODO: Calculate missing data statistics
print("\n=== MISSING DATA SUMMARY ===")
missing_counts = df.isnull().sum()
missing_pct = (missing_counts / len(df)) * 100

missing_df = pd.DataFrame({
    'Variable': missing_counts.index,
    'Missing_Count': missing_counts.values,
    'Missing_Pct': missing_pct.values
})
missing_df = missing_df[missing_df['Missing_Count'] > 0].sort_values('Missing_Pct', ascending=False)

print(missing_df)

total_missing = df.isnull().sum().sum()
total_possible = df.shape[0] * df.shape[1]
print(f"\nTotal missing data points: {total_missing} ({total_missing/total_possible*100:.2f}%)")

# TODO: Create missing data visualizations
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# Plot 1: Missing data heatmap (sample of rows)
sample_indices = np.random.choice(df.index, size=min(500, len(df)), replace=False)
sns.heatmap(df.loc[sample_indices].isnull(), cbar=False, yticklabels=False,
            cmap='viridis', ax=axes[0, 0])
axes[0, 0].set_title('Missing Data Pattern\n(Sample of 500 rows)')

# Plot 2: Missing percentages by variable


# Plot 3: Missingness correlation matrix


# Plot 4: Missing data by row


# TODO: Test missingness type - MAR analysis
print("\n=== TESTING FOR MAR: Does Age Correlate with Income Missingness? ===")
df_temp = df.copy()
df_temp['income_missing'] = df['income'].isnull()

# Box plot comparison
plt.figure(figsize=(10, 6))
# Your code here


# Statistical test
# Your code here


# TODO: Prepare data for imputation (numeric columns only)
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
if 'respondent_id' in numeric_cols:
    numeric_cols.remove('respondent_id')

df_numeric = df[numeric_cols].copy()

print(f"\n=== IMPUTATION ANALYSIS ===")
print(f"Numeric columns to impute: {len(numeric_cols)}")

# TODO: Method 1 - Simple mean imputation
simple_imputer = SimpleImputer(strategy='mean')
df_simple = pd.DataFrame(simple_imputer.fit_transform(df_numeric),
                         columns=df_numeric.columns,
                         index=df_numeric.index)

# TODO: Method 2 - KNN imputation


# TODO: Method 3 - Iterative imputation


# TODO: Compare distributions for a key variable (e.g., income)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Original distribution


# Simple imputation


# KNN imputation


# Iterative imputation


plt.tight_layout()
plt.show()

# TODO: Compare correlation preservation
print("\n=== CORRELATION PRESERVATION CHECK ===")
# Original correlations (pairwise complete)
original_corr = df_numeric.corr()

# Imputed correlations
simple_corr = df_simple.corr()
knn_corr = df_knn.corr()
iter_corr = df_iter.corr()

# Calculate difference from original
print("Mean absolute difference from original correlations:")
print(f"Simple Imputation: {np.abs(simple_corr - original_corr).mean().mean():.4f}")
print(f"KNN Imputation: {np.abs(knn_corr - original_corr).mean().mean():.4f}")
print(f"Iterative Imputation: {np.abs(iter_corr - original_corr).mean().mean():.4f}")

# TODO: Statistical comparison of distributions
from scipy.stats import ks_2samp

print("\n=== DISTRIBUTION COMPARISON (Kolmogorov-Smirnov Test) ===")
test_col = 'income'
if test_col in df_numeric.columns:
    original_data = df_numeric[test_col].dropna()
    
    ks_simple = ks_2samp(original_data, df_simple[test_col])
    ks_knn = ks_2samp(original_data, df_knn[test_col])
    ks_iter = ks_2samp(original_data, df_iter[test_col])
    
    print(f"Simple vs Original: KS statistic = {ks_simple.statistic:.4f}, p-value = {ks_simple.pvalue:.4f}")
    print(f"KNN vs Original: KS statistic = {ks_knn.statistic:.4f}, p-value = {ks_knn.pvalue:.4f}")
    print(f"Iterative vs Original: KS statistic = {ks_iter.statistic:.4f}, p-value = {ks_iter.pvalue:.4f}")
    print("\nLower KS statistic = better preservation of original distribution")

# TODO: Final recommendations
print("\n=== RECOMMENDATIONS ===")
print("1. Missingness type diagnosis: ")
print("2. Recommended imputation method: ")
print("3. Justification: ")
print("4. Risks and limitations: ")
print("5. Variables to potentially drop: ")
```

### Success Criteria
- ✅ Missing data patterns thoroughly visualized
- ✅ Missingness type diagnosed with statistical tests
- ✅ Three imputation methods implemented
- ✅ Distribution preservation quantified
- ✅ Clear, evidence-based recommendation provided

### Hints
- 💡 MAR is most common - test if missingness relates to observed variables
- 💡 Simple imputation distorts distributions - use for baseline only
- 💡 KNN preserves local structure better than mean imputation
- 💡 Iterative imputation often best but computationally expensive
- 💡 Create "was_missing" indicator variables for modeling

---

## Exercise 8: Multi-Dimensional EDA with Categorical Analysis

**Difficulty**: ⭐⭐⭐ Hard  
**Time Estimate**: 35 minutes  
**Dataset**: `ecommerce_full.csv`

### Scenario
You're analyzing a large e-commerce dataset to identify which customer segment and product category combinations drive revenue. The CEO wants data-driven insights to guide marketing budget allocation across segments and regions.

### Dataset Description
- **File**: `Class4/data/ecommerce_full.csv`
- **Size**: 50,000 transactions
- **Variables**:
  - `transaction_id`: Unique identifier
  - `customer_segment`: New, Regular, Premium
  - `product_category`: Electronics, Clothing, Home, Books, Sports
  - `region`: North, South, East, West
  - `order_value`: Transaction amount (USD)
  - `quantity`: Items purchased
  - `date`: Transaction date
  - `customer_age`: Customer age
  - `is_repeat_customer`: Boolean flag

### Learning Objectives
- Conduct systematic univariate analysis across variable types
- Perform categorical cross-tabulation analysis
- Create multivariate visualizations with multiple encodings
- Use facet grids for multi-dimensional comparisons
- Identify data quality issues in large datasets
- Translate findings into business recommendations

### Tasks

**1. Univariate Analysis (All Variables)**
   - Numeric variables: distributions, outliers, transformations needed?
   - Categorical variables: frequency, balance, suspicious categories?
   - Create summary report of all variables

**2. Categorical Relationship Analysis**
   - Create crosstab: customer_segment × product_category
   - Calculate proportions and identify patterns
   - Create heatmap showing category combinations
   - Which segment buys which products?

**3. Multivariate Visualization**
   - Create scatter plot with:
     - X-axis: customer_age
     - Y-axis: order_value
     - Color: customer_segment
     - Size: quantity
   - What patterns emerge?

**4. Regional Analysis with Facets**
   - Create facet grid: region × product_category
   - Plot average order value for each combination
   - Identify regional preferences

**5. Data Quality Investigation**
   - Check for duplicates (same customer, same minute)
   - Identify impossible values (negative prices, age > 120)
   - Check for encoding errors (typos in categories)
   - Flag transactions needing review

**6. Business Insights**
   - Which segment + category combination has highest revenue?
   - Which region should get marketing budget for which products?
   - Are Premium customers concentrated in certain categories?
   - Top 3 actionable recommendations for CEO

### Data Manipulation Guide
```python
# Crosstab with proportions
crosstab = pd.crosstab(df['customer_segment'], df['product_category'])
crosstab_pct = pd.crosstab(df['customer_segment'], df['product_category'], 
                            normalize='index') * 100

# Revenue by segment and category
revenue_by_combo = df.groupby(['customer_segment', 'product_category'])['order_value'].agg(['sum', 'mean', 'count'])

# Multivariate scatter
plt.scatter(df['customer_age'], df['order_value'], 
            c=df['customer_segment'].cat.codes, 
            s=df['quantity']*10, alpha=0.5)

# Facet grid
g = sns.FacetGrid(df, col='region', row='product_category', height=3)
g.map(plt.hist, 'order_value', bins=20)
```

### Expected Visualization
A comprehensive dashboard-style layout with multiple coordinated views revealing complex patterns across segments, categories, and regions.

### Starter Code

```python
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# TODO: Load the data
df = pd.read_csv('Class4/data/ecommerce_full.csv', parse_dates=['date'])

print("Dataset shape:", df.shape)
print("\nFirst few rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)

# TODO: PHASE 1 - Univariate Analysis
print("\n" + "="*70)
print("PHASE 1: UNIVARIATE ANALYSIS")
print("="*70)

# Numeric variables
numeric_cols = df.select_dtypes(include=[np.number]).columns
print(f"\nNumeric variables ({len(numeric_cols)}):")
for col in numeric_cols:
    print(f"\n{col}:")
    print(f"  Mean: {df[col].mean():.2f}, Median: {df[col].median():.2f}")
    print(f"  Std: {df[col].std():.2f}, Skew: {df[col].skew():.2f}")
    print(f"  Range: [{df[col].min():.2f}, {df[col].max():.2f}]")
    
    # Flag potential issues
    if df[col].skew() > 2:
        print(f"  ⚠️ Heavily right-skewed - consider transformation")
    if (df[col] < 0).any():
        print(f"  ⚠️ Contains negative values - verify if valid")

# Categorical variables
cat_cols = df.select_dtypes(include=['object', 'category']).columns
print(f"\n\nCategorical variables ({len(cat_cols)}):")
for col in cat_cols:
    if col != 'transaction_id' and col != 'date':
        print(f"\n{col}:")
        print(f"  Unique values: {df[col].nunique()}")
        print(f"  Most common: {df[col].mode()[0]} (n={df[col].value_counts().iloc[0]})")
        print(f"  Distribution:")
        print(df[col].value_counts())

# TODO: PHASE 2 - Categorical Cross-Tabulation
print("\n" + "="*70)
print("PHASE 2: CATEGORICAL RELATIONSHIP ANALYSIS")
print("="*70)

# Crosstab: segment × category


# Revenue analysis by combination


# TODO: Create heatmap visualization
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Heatmap 1: Count of transactions


# Heatmap 2: Average order value


plt.tight_layout()
plt.show()

# TODO: PHASE 3 - Multivariate Visualization
print("\n" + "="*70)
print("PHASE 3: MULTIVARIATE VISUALIZATION")
print("="*70)

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Scatter plot with multiple encodings


# Alternative: Bubble chart by segment


plt.tight_layout()
plt.show()

# TODO: PHASE 4 - Regional Analysis with Facets
print("\n" + "="*70)
print("PHASE 4: REGIONAL ANALYSIS")
print("="*70)

# Calculate average order value by region and category
regional_analysis = df.groupby(['region', 'product_category'])['order_value'].agg(['mean', 'sum', 'count']).reset_index()
print(regional_analysis)

# Create facet grid


# TODO: PHASE 5 - Data Quality Checks
print("\n" + "="*70)
print("PHASE 5: DATA QUALITY INVESTIGATION")
print("="*70)

# Check 1: Duplicates


# Check 2: Impossible values


# Check 3: Encoding errors (typos)


# TODO: PHASE 6 - Business Insights
print("\n" + "="*70)
print("PHASE 6: BUSINESS INSIGHTS & RECOMMENDATIONS")
print("="*70)

# Calculate revenue by segment-category combination


# Find top combinations


print("\n=== ACTIONABLE INSIGHTS ===")
print("1. Highest revenue combination: ")
print("2. Regional marketing strategy: ")
print("3. Premium customer focus: ")
print("\n=== TOP 3 RECOMMENDATIONS FOR CEO ===")
print("1. ")
print("2. ")
print("3. ")
```

### Success Criteria
- ✅ Comprehensive univariate analysis completed
- ✅ Categorical relationships quantified
- ✅ Multivariate visualization with 4+ dimensions
- ✅ Regional patterns identified with facets
- ✅ Data quality issues documented
- ✅ Clear business recommendations provided

### Hints
- 💡 Use `.groupby()` with multiple columns for segment-category analysis
- 💡 Encode categorical variables as numbers for color coding
- 💡 Use `normalize='index'` in crosstab for row percentages
- 💡 FacetGrid is powerful but can be slow - sample large datasets
- 💡 Business insights should be specific and actionable

---

## Exercise 9: Complete EDA with Feature Engineering

**Difficulty**: ⭐⭐⭐ Hard  
**Time Estimate**: 45 minutes  
**Dataset**: `credit_risk.csv`

### Scenario
You're preparing a credit risk dataset for machine learning. You need to conduct a complete EDA following best practices, identify data issues, engineer new features based on your findings, and prepare a model-ready dataset with documentation.

### Dataset Description
- **File**: `Class4/data/credit_risk.csv`
- **Size**: 8,000 loan applications
- **Variables**: 25 features + target
  - **Target**: `default` (1 = defaulted, 0 = paid)
  - **Demographics**: age, income, employment_length, zip_code
  - **Financial**: debt, credit_score, loan_amount, interest_rate
  - **Loan**: term, purpose, grade
  - **History**: delinquencies, inquiries, open_accounts
  - Contains missing values, outliers, and class imbalance

### Learning Objectives
- Execute systematic EDA workflow from start to finish
- Handle class imbalance in classification problems
- Engineer features based on EDA insights
- Create interaction terms and derived features
- Document feature engineering decisions
- Prepare model-ready dataset

### Tasks

**1. Initial Data Profiling**
   - Load data and examine structure
   - Check data types, missing values, duplicates
   - Display target variable distribution (class imbalance?)
   - Create initial data quality report

**2. Univariate Analysis**
   - Analyze all numeric variables (distributions, outliers, skewness)
   - Analyze all categorical variables (frequencies, rare categories)
   - Flag variables needing transformation
   - Identify variables to drop (too many missing, zero variance)

**3. Target-Related Analysis**
   - Calculate correlation of numeric features with target
   - Create box plots: defaulters vs non-defaulters for key variables
   - Identify which features best separate the classes
   - Check for data leakage (features that predict too perfectly)

**4. Bivariate Analysis**
   - Create correlation heatmap
   - Identify multicollinearity issues
   - Look for non-linear relationships
   - Create pair plot for top 5 features

**5. Feature Engineering**
   Based on EDA findings, create these features:
   - **Log transformations** for skewed variables
   - **Debt-to-income ratio**: debt / income
   - **Credit utilization**: (debt / credit_limit) if available
   - **Missing value indicators** for important features
   - **Interaction terms** for correlated features
   - **Binned versions** of continuous variables if needed

**6. Final Dataset Preparation**
   - Handle missing values (imputation strategy)
   - Handle outliers (cap, remove, or keep?)
   - Encode categorical variables
   - Scale numeric features (document method)
   - Create train/test split
   - Save processed dataset

**7. Comprehensive Report**
   - Executive summary (key findings)
   - 5 most important visualizations
   - Feature engineering justification
   - Recommended modeling approach
   - Potential challenges and risks

### Data Manipulation Guide
```python
# Class imbalance check
class_counts = df['default'].value_counts()
imbalance_ratio = class_counts.max() / class_counts.min()

# Feature engineering
df['debt_to_income'] = df['debt'] / df['income']
df['income_log'] = np.log(df['income'] + 1)
df['has_missing_income'] = df['income'].isnull().astype(int)

# Interaction terms
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)

# Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
```

### Expected Visualization
A complete EDA report with multiple coordinated visualizations, clear feature engineering documentation, and model-ready dataset.

### Starter Code

```python
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# TODO: Load the data
df = pd.read_csv('Class4/data/credit_risk.csv')

print("="*70)
print("CREDIT RISK EDA - COMPREHENSIVE ANALYSIS")
print("="*70)

# TODO: PHASE 1 - Initial Data Profiling
print("\n### PHASE 1: INITIAL DATA PROFILING ###\n")
print(f"Dataset shape: {df.shape}")
print(f"\nData types:\n{df.dtypes.value_counts()}")
print(f"\nMemory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

# Missing data
missing_summary = pd.DataFrame({
    'Missing_Count': df.isnull().sum(),
    'Missing_Pct': (df.isnull().sum() / len(df)) * 100
})
missing_summary = missing_summary[missing_summary['Missing_Count'] > 0].sort_values('Missing_Pct', ascending=False)

if len(missing_summary) > 0:
    print(f"\n⚠️ Missing Data Found:")
    print(missing_summary)

# Target variable analysis
print("\n### TARGET VARIABLE ANALYSIS ###")
print(df['default'].value_counts())
print(f"\nClass proportions:")
print(df['default'].value_counts(normalize=True))

# Class imbalance check
class_counts = df['default'].value_counts()
imbalance_ratio = class_counts.max() / class_counts.min()
print(f"\nImbalance ratio: {imbalance_ratio:.2f}:1")
if imbalance_ratio > 3:
    print("⚠️ Severe class imbalance detected - will need to address in modeling")

# TODO: PHASE 2 - Univariate Analysis
print("\n### PHASE 2: UNIVARIATE ANALYSIS ###\n")

# Numeric variables
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
if 'default' in numeric_cols:
    numeric_cols.remove('default')

print(f"Analyzing {len(numeric_cols)} numeric variables...")

# Create comprehensive univariate plots
# Your code here


# TODO: PHASE 3 - Target-Related Analysis
print("\n### PHASE 3: TARGET-RELATED ANALYSIS ###\n")

# Correlation with target


# Box plots: defaulters vs non-defaulters


# TODO: PHASE 4 - Bivariate Analysis
print("\n### PHASE 4: BIVARIATE ANALYSIS ###\n")

# Correlation heatmap


# Multicollinearity check


# TODO: PHASE 5 - Feature Engineering
print("\n### PHASE 5: FEATURE ENGINEERING ###\n")

df_engineered = df.copy()

# Log transformations for skewed variables
skewed_vars = []
for col in numeric_cols:
    if df[col].skew() > 1 and (df[col] > 0).all():
        skewed_vars.append(col)
        df_engineered[f'{col}_log'] = np.log(df[col] + 1)
        print(f"✅ Created: {col}_log (original skew: {df[col].skew():.2f})")

# Ratio features


# Missing indicators


# Interaction terms


print(f"\nOriginal features: {len(df.columns)}")
print(f"Engineered features: {len(df_engineered.columns)}")
print(f"New features created: {len(df_engineered.columns) - len(df.columns)}")

# TODO: PHASE 6 - Final Dataset Preparation
print("\n### PHASE 6: DATASET PREPARATION ###\n")

# Handle missing values


# Handle outliers


# Encode categorical variables


# Scale numeric features


# Train-test split


# TODO: PHASE 7 - Comprehensive Report
print("\n" + "="*70)
print("FINAL REPORT: KEY FINDINGS & RECOMMENDATIONS")
print("="*70)

print("\n### EXECUTIVE SUMMARY ###")
print("1. Data Quality: ")
print("2. Class Imbalance: ")
print("3. Key Predictors: ")
print("4. Feature Engineering: ")

print("\n### TOP 5 VISUALIZATIONS ###")
print("1. Target distribution with class imbalance")
print("2. Correlation heatmap with target")
print("3. Box plots: defaulters vs non-defaulters")
print("4. Distribution transformations comparison")
print("5. Feature importance (correlation-based)")

print("\n### FEATURE ENGINEERING DECISIONS ###")
print("✅ Log transformations: ")
print("✅ Ratio features: ")
print("✅ Missing indicators: ")
print("✅ Interaction terms: ")

print("\n### RECOMMENDED MODELING APPROACH ###")
print("1. Algorithm suggestions: ")
print("2. Handle class imbalance with: ")
print("3. Cross-validation strategy: ")
print("4. Evaluation metrics: ")

print("\n### RISKS & LIMITATIONS ###")
print("1. ")
print("2. ")
print("3. ")
```

### Success Criteria
- ✅ Complete systematic EDA workflow executed
- ✅ Class imbalance identified and documented
- ✅ Minimum 5 engineered features created with justification
- ✅ Model-ready dataset prepared with documentation
- ✅ Comprehensive report with executive summary
- ✅ Clear recommendations for modeling approach

### Hints
- 💡 Start with data quality - don't model garbage data
- 💡 Class imbalance is critical for credit risk - use stratified sampling
- 💡 Feature engineering should be driven by EDA insights, not random
- 💡 Document every decision - future you will thank you
- 💡 Consider business context - false positives vs false negatives
- 💡 Create a "feature dictionary" documenting all engineered features

---

## Congratulations! 🎉

You've completed all 9 exercises across three difficulty levels. You now have practical experience with:

✅ **Basic EDA Skills**: Distributions, comparisons, relationships  
✅ **Advanced Techniques**: Transformations, time series, correlations  
✅ **Professional Workflows**: Missing data, feature engineering, comprehensive reports

### What's Next?

1. **Review Your Solutions**: Compare with provided solutions
2. **Try Real Datasets**: Apply these techniques to your own data
3. **Build Your Portfolio**: Document your best EDA projects
4. **Learn More**: Explore advanced topics like dimensionality reduction, anomaly detection

### Resources for Continued Learning

- **Books**: *Practical Statistics for Data Scientists*, *Python for Data Analysis*
- **Online**: Kaggle EDA competitions, Towards Data Science articles
- **Practice**: UCI ML Repository, Data.gov, Google Dataset Search

---

**Remember**: Great EDA is the foundation of great data science! 📊🔍
