# Class 4: Exploratory Data Visualization - Exercise Package

## 📚 Overview

This comprehensive exercise package contains 9 progressively challenging exercises designed to teach exploratory data analysis (EDA) and visualization techniques. Students will work with realistic datasets spanning various business scenarios.

## 📁 Package Contents

### Core Files
- **`Class4_Exercises.md`** - All 9 exercises with detailed instructions (3 easy, 3 medium, 3 hard)
- **`Class4_Solutions.md`** - Complete solutions with working code and interpretations
- **`generate_exercise_datasets.py`** - Python script to regenerate datasets
- **`data/`** - Directory containing all 9 CSV datasets

### Datasets (75,730 total data points)

| # | Dataset | Rows | Exercise Level | Topic |
|---|---------|------|----------------|-------|
| 1 | `student_scores.csv` | 200 | Easy | Histogram & Distribution Analysis |
| 2 | `employee_salaries.csv` | 500 | Easy | Box Plot & Outlier Detection |
| 3 | `house_simple.csv` | 300 | Easy | Scatter Plot & Correlation |
| 4 | `customer_transactions.csv` | 10,000 | Medium | Skewness & Data Transformation |
| 5 | `real_estate.csv` | 1,000 | Medium | Correlation Matrix & Feature Selection |
| 6 | `daily_sales.csv` | 730 | Medium | Time Series & Seasonality |
| 7 | `customer_survey.csv` | 5,000 | Hard | Missing Data & Imputation |
| 8 | `ecommerce_full.csv` | 50,000 | Hard | Multi-Dimensional EDA |
| 9 | `credit_risk.csv` | 8,000 | Hard | Complete EDA & Feature Engineering |

## 🎯 Learning Objectives

### Easy Level (Exercises 1-3)
- Load and explore datasets with pandas
- Calculate descriptive statistics
- Create basic visualizations (histograms, box plots, scatter plots)
- Identify distribution shapes and outliers
- Calculate and interpret correlation coefficients

### Medium Level (Exercises 4-6)
- Apply data transformations (log, square root)
- Create correlation heatmaps
- Work with time series data
- Calculate rolling averages
- Detect anomalies statistically
- Make data-driven recommendations

### Hard Level (Exercises 7-9)
- Diagnose missingness types (MCAR, MAR, MNAR)
- Implement multiple imputation methods
- Conduct comprehensive univariate and bivariate analysis
- Engineer features based on EDA insights
- Create multi-dimensional visualizations
- Prepare model-ready datasets

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn
```

### Running Exercises

1. **Navigate to Class4 directory:**
   ```bash
   cd "Class4"
   ```

2. **Verify datasets exist:**
   ```bash
   ls data/
   ```
   You should see all 9 CSV files.

3. **Start with Exercise 1:**
   - Open `Class4_Exercises.md`
   - Read the scenario and tasks
   - Use the starter code as a template
   - Run your analysis

4. **Check solutions:**
   - After completing an exercise, compare with `Class4_Solutions.md`
   - Study alternative approaches
   - Understand the interpretation

### Regenerating Datasets

If you need to regenerate the datasets (e.g., for different random values):

```bash
python generate_exercise_datasets.py
```

This will recreate all 9 CSV files in the `data/` directory with the same structure but potentially different values.

## 📊 Dataset Details

### Easy Level Datasets

#### 1. Student Scores
- **Purpose**: Basic distribution analysis
- **Variables**: student_id, exam_score
- **Characteristics**: Normal distribution, ~200 students
- **Skills**: Histograms, mean/median, distribution shape

#### 2. Employee Salaries
- **Purpose**: Group comparisons and outlier detection
- **Variables**: employee_id, department, salary, years_experience
- **Characteristics**: 4 departments with different salary distributions
- **Skills**: Box plots, IQR method, categorical analysis

#### 3. House Simple
- **Purpose**: Bivariate relationship analysis
- **Variables**: house_id, sqft, price
- **Characteristics**: Strong linear correlation (~0.91)
- **Skills**: Scatter plots, correlation, regression

### Medium Level Datasets

#### 4. Customer Transactions
- **Purpose**: Skewness and transformations
- **Variables**: transaction_id, amount, date, category, customer_type
- **Characteristics**: Right-skewed distribution (skew ~8.35)
- **Skills**: Log transformation, Q-Q plots, outlier analysis

#### 5. Real Estate
- **Purpose**: Feature selection and multicollinearity
- **Variables**: price + 11 features (sqft, bedrooms, age, etc.)
- **Characteristics**: Correlated features, realistic property data
- **Skills**: Correlation heatmap, pair plots, feature selection

#### 6. Daily Sales
- **Purpose**: Time series pattern detection
- **Variables**: date, daily_sales, day_of_week, is_holiday
- **Characteristics**: 2 years of data, seasonal patterns, trend
- **Skills**: Rolling averages, seasonality, anomaly detection

### Hard Level Datasets

#### 7. Customer Survey
- **Purpose**: Missing data strategies
- **Variables**: respondent_id, age, income, education, q1-q20
- **Characteristics**: ~7.9% missing data with MAR patterns
- **Skills**: Missingness diagnosis, KNN/MICE imputation

#### 8. E-commerce Full
- **Purpose**: Multi-dimensional analysis
- **Variables**: transaction_id, customer_segment, product_category, region, order_value, quantity, date, customer_age, is_repeat_customer
- **Characteristics**: 50,000 transactions, business insights focus
- **Skills**: Crosstab, facet grids, multivariate visualization

#### 9. Credit Risk
- **Purpose**: Complete EDA workflow
- **Variables**: 15 features + default target
- **Characteristics**: Class imbalance (~13.9% default), missing values
- **Skills**: Full EDA pipeline, feature engineering, model prep

## 💡 Exercise Tips

### Time Management
- **Easy**: 10-15 minutes per exercise
- **Medium**: 20-25 minutes per exercise  
- **Hard**: 30-45 minutes per exercise
- **Total**: ~4 hours for all 9 exercises

### Approach Strategy
1. **Read carefully**: Understand the business scenario
2. **Explore first**: Use `.head()`, `.info()`, `.describe()`
3. **Visualize early**: See patterns before statistics
4. **Interpret always**: Don't just show numbers, explain meaning
5. **Compare solutions**: Learn from different approaches

### Common Pitfalls to Avoid
- ❌ Not checking for missing values first
- ❌ Using wrong column names (typos!)
- ❌ Forgetting axis labels and titles
- ❌ Not explaining interpretations
- ❌ Skipping data quality checks

## 📈 Skills Progression

```
Easy Level (Foundations)
├── Load & explore data
├── Basic statistics
├── Simple visualizations
└── Distribution interpretation

Medium Level (Techniques)
├── Data transformations
├── Correlation analysis
├── Time series basics
├── Multi-panel plots
└── Pattern detection

Hard Level (Professional)
├── Missing data strategies
├── Feature engineering
├── Multi-dimensional analysis
├── Business insights
└── Model-ready datasets
```

## 🎓 Assessment Criteria

Students should demonstrate:

1. **Technical Competence** (40%)
   - Correct use of pandas, matplotlib, seaborn
   - Proper statistical calculations
   - Appropriate visualization choices

2. **Analytical Thinking** (30%)
   - Identifying patterns and anomalies
   - Making data-driven decisions
   - Choosing appropriate methods

3. **Communication** (20%)
   - Clear interpretations
   - Well-labeled visualizations
   - Actionable recommendations

4. **Code Quality** (10%)
   - Clean, readable code
   - Proper comments
   - Following best practices

## 📚 Additional Resources

### Recommended Reading
- *Practical Statistics for Data Scientists* by Bruce & Bruce
- *Python for Data Analysis* by Wes McKinney
- *Storytelling with Data* by Cole Nussbaumer Knaflic

### Online Resources
- Kaggle EDA Competitions
- Towards Data Science (Medium)
- Seaborn Gallery
- Matplotlib Tutorials

### Practice Datasets
- UCI Machine Learning Repository
- Kaggle Datasets
- Data.gov
- Google Dataset Search

## 🔧 Troubleshooting

### Common Issues

**Issue**: Dataset not found
```python
# Solution: Check your working directory
import os
print(os.getcwd())
# Make sure you're in the Class4 directory
```

**Issue**: Import errors
```python
# Solution: Install required packages
pip install pandas numpy matplotlib seaborn scipy scikit-learn
```

**Issue**: Plots not displaying
```python
# Solution: Add this to show plots
plt.show()
```

**Issue**: Large dataset slow to load
```python
# Solution: Sample for exploration
df_sample = pd.read_csv('data/ecommerce_full.csv', nrows=1000)
```

## 📝 Exercise Completion Checklist

### Easy Level
- [ ] Exercise 1: Student Scores - Histogram Analysis
- [ ] Exercise 2: Employee Salaries - Box Plot Comparison
- [ ] Exercise 3: House Prices - Scatter Plot Relationship

### Medium Level
- [ ] Exercise 4: Transactions - Distribution Transformation
- [ ] Exercise 5: Real Estate - Correlation & Feature Selection
- [ ] Exercise 6: Daily Sales - Time Series Patterns

### Hard Level
- [ ] Exercise 7: Survey - Missing Data Strategy
- [ ] Exercise 8: E-commerce - Multi-Dimensional EDA
- [ ] Exercise 9: Credit Risk - Complete EDA Pipeline

## 🏆 Going Further

After completing all exercises, try:

1. **Apply to Real Data**: Find datasets on Kaggle and apply these techniques
2. **Create Your Own**: Generate custom datasets for specific scenarios
3. **Build a Portfolio**: Document your best EDA projects on GitHub
4. **Teach Others**: Explain your process to solidify understanding
5. **Automate**: Create reusable EDA templates and functions

## 📧 Support

For questions or issues:
- Review the solution file for guidance
- Check the lecture notes in `Class4.md`
- Practice with the provided datasets
- Experiment with variations

---

**Remember**: Great EDA is the foundation of great data science! 📊🔍

**Version**: 1.0  
**Last Updated**: February 2026  
**Author**: MIS 6380 - Data Visualization Course
