# Class 5 - Exercises
## Time Series & Temporal Visualization

**MIS 6380 - Data Visualization**  
**Spring 2026**

---

## 📋 Overview

This exercise set provides hands-on practice with time series visualization techniques covered in Class 5. Complete all 5 exercises to master temporal data analysis and visualization.

**Learning Objectives:**
- Apply time series visualization best practices
- Perform decomposition and pattern analysis
- Create forecasts with uncertainty
- Build interactive temporal dashboards
- Communicate temporal insights effectively

**Prerequisites:** Parts 1-3 content, Python (pandas, matplotlib, statsmodels, plotly)

---

## 🎯 Exercise 1: Identify Temporal Patterns

**Objective:** Analyze a time series dataset to identify and visualize its component patterns.

**Dataset:** Daily website traffic data (2 years)

**Tasks:**

1. **Load and visualize the data**
   - Create a line plot of daily visits
   - Add a 30-day moving average to reveal the trend
   - Annotate any obvious anomalies or events

2. **Perform STL decomposition**
   - Use `statsmodels.tsa.seasonal.STL`
   - Extract trend, seasonal, and residual components
   - Create a 4-panel plot showing all components

3. **Analyze each component**
   - Trend: Calculate the overall growth rate
   - Seasonal: Identify the period (weekly, monthly, or both)
   - Residual: Check if residuals are random (use ACF plot)

4. **Calculate component strengths**
   - Trend strength: `1 - var(resid) / var(trend + resid)`
   - Seasonal strength: `1 - var(resid) / var(seasonal + resid)`
   - Report which component dominates

**Deliverables:**
- [ ] Time series plot with trend line
- [ ] 4-panel decomposition visualization
- [ ] Component strength metrics (trend, seasonal)
- [ ] 1-paragraph interpretation

**Sample Data Generation:**
```python
import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=730, freq='D')

# Trend: Growing website traffic
trend = np.linspace(1000, 2000, 730)

# Weekly seasonality: Higher on weekdays
weekly = 200 * np.sin(2 * np.pi * np.arange(730) / 7)

# Annual seasonality: Higher in Q4
annual = 150 * np.sin(2 * np.pi * np.arange(730) / 365 - np.pi/2)

# Noise
noise = np.random.normal(0, 50, 730)

# Combine
visits = trend + weekly + annual + noise

df = pd.DataFrame({'Date': dates, 'Visits': visits})
df.to_csv('website_traffic.csv', index=False)
```

**Grading (25 points):**
- Data visualization (5 pts)
- Decomposition plot (10 pts)
- Component analysis (7 pts)
- Interpretation (3 pts)

---

## 🎯 Exercise 2: Choose the Right Time Scale

**Objective:** Practice selecting appropriate time aggregation for different business questions.

**Dataset:** Hourly sales data for an e-commerce site (3 months)

**Scenario:** Your stakeholders have different questions about sales performance. Create appropriate visualizations for each.

**Questions & Required Visualizations:**

**Question 1:** "How did we perform this month compared to last month?"
- **Suggested scale:** Daily aggregated to weeks or whole month
- **Visualization:** Bar chart or line chart comparing two months
- **Requirement:** Clear comparison, seasonally adjusted if needed

**Question 2:** "Are there patterns in when customers shop during the day?"
- **Suggested scale:** Hourly, averaged across all days
- **Visualization:** Line chart of average hourly traffic
- **Requirement:** Show 24-hour cycle, highlight peak hours

**Question 3:** "What's our growth trend over the quarter?"
- **Suggested scale:** Weekly aggregation
- **Visualization:** Line chart with trend line
- **Requirement:** Smooth enough to see trend, detailed enough to show variation

**Question 4:** "Do we see weekly patterns (weekday vs weekend)?"
- **Suggested scale:** Daily data, grouped by day of week
- **Visualization:** Box plot or bar chart by day of week
- **Requirement:** Show all 7 days, highlight differences

**Tasks:**

1. Generate appropriate time scale for each question
2. Create clear, well-labeled visualization
3. Add appropriate annotations (mean lines, peaks, etc.)
4. Write 1-sentence insight for each

**Deliverables:**
- [ ] 4 visualizations (one per question)
- [ ] Each with appropriate time scale
- [ ] Clear titles and labels
- [ ] Brief insights for each

**Sample Data Generation:**
```python
import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=90*24, freq='H')

# Base level
base = 1000

# Hourly pattern (peaks at lunch and evening)
hour_of_day = dates.hour
hourly_pattern = 200 * np.sin((hour_of_day - 6) * np.pi / 12)

# Day of week pattern (lower on weekends)
day_of_week = dates.dayofweek
weekly_pattern = np.where(day_of_week < 5, 150, -100)

# Growth trend
trend = np.linspace(0, 200, len(dates))

# Noise
noise = np.random.normal(0, 50, len(dates))

# Combine
sales = base + hourly_pattern + weekly_pattern + trend + noise
sales = np.maximum(sales, 0)  # No negative sales

df = pd.DataFrame({'DateTime': dates, 'Sales': sales})
df.to_csv('hourly_sales.csv', index=False)
```

**Grading (25 points):**
- Appropriate scale selection (12 pts - 3 per question)
- Visualization quality (8 pts - 2 per question)
- Insights (5 pts)

---

## 🎯 Exercise 3: Time Series Decomposition

**Objective:** Perform and interpret time series decomposition using both Classical and STL methods.

**Dataset:** Monthly retail sales (5 years, with strong seasonality and trend)

**Tasks:**

**Part A: Classical Decomposition**

1. Load the monthly sales data
2. Apply `seasonal_decompose` with:
   - `model='additive'`
   - `period=12` (monthly data, yearly seasonality)
3. Create the standard 4-panel decomposition plot
4. Identify the seasonal pattern (which months are high/low)

**Part B: STL Decomposition**

1. Apply STL with `robust=True`
2. Compare STL trend to Classical trend
3. Which method handles outliers better?
4. Calculate trend and seasonal strengths

**Part C: Seasonal Adjustment**

1. Create seasonally adjusted series (observed - seasonal)
2. Plot original vs seasonally adjusted
3. Interpret: Is growth real or just seasonal?

**Part D: Residual Analysis**

1. Plot residuals from both methods
2. Check if residuals are random:
   - ACF plot of residuals
   - Histogram of residuals
3. Identify any remaining patterns

**Deliverables:**
- [ ] Classical decomposition plot (4 panels)
- [ ] STL decomposition plot (4 panels)
- [ ] Comparison: Classical vs STL trends
- [ ] Seasonally adjusted series plot
- [ ] Residual diagnostic plots
- [ ] 2-paragraph interpretation

**Sample Data:**
```python
import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range('2020-01-01', periods=60, freq='M')

# Growing trend
trend = np.linspace(10000, 15000, 60)

# Strong seasonality (holiday spike in Dec)
month = (np.arange(60) % 12) + 1
seasonal = 2000 * np.sin(2 * np.pi * month / 12 - np.pi/2)

# Add outliers (simulate promotions)
outliers = np.zeros(60)
outlier_months = [15, 32, 47]  # 3 promotional months
outliers[outlier_months] = 3000

# Noise
noise = np.random.normal(0, 300, 60)

# Combine
sales = trend + seasonal + outliers + noise

df = pd.DataFrame({
    'Month': dates,
    'Sales': sales
})
df.to_csv('monthly_retail_sales.csv', index=False)
```

**Grading (25 points):**
- Decomposition plots (10 pts)
- Seasonal adjustment (5 pts)
- Residual analysis (5 pts)
- Interpretation (5 pts)

---

## 🎯 Exercise 4: Forecasting Visualization

**Objective:** Create professional forecast visualizations with proper uncertainty quantification.

**Dataset:** Daily sales data (1 year historical, forecast next quarter)

**Tasks:**

**Part A: Prepare Data**

1. Load daily sales data
2. Visualize to understand patterns
3. Check for missing values
4. Split into train (first 9 months) and validation (last 3 months)

**Part B: Create Forecast**

1. Choose a forecasting method:
   - Option 1: Holt-Winters Exponential Smoothing
   - Option 2: Facebook Prophet
   - Option 3: SARIMA
2. Fit on training data
3. Generate 90-day forecast

**Part C: Calculate Uncertainty**

1. Compute prediction intervals (80% and 95%)
2. Methods:
   - Use model's built-in intervals, OR
   - Bootstrap residuals, OR
   - Simulate from residual distribution

**Part D: Visualize**

Create a publication-quality forecast plot with:
- Historical data (all)
- Forecast (next 90 days)
- 80% confidence band (darker)
- 95% confidence band (lighter)
- Vertical line marking forecast start
- Clear legend
- Proper axis labels and title

**Part E: Validate**

1. Compare forecast to validation set (last 3 months)
2. Calculate forecast errors:
   - MAE, RMSE, MAPE
3. Plot actual vs predicted
4. Create residual diagnostic plots

**Deliverables:**
- [ ] Forecast visualization with uncertainty bands
- [ ] Validation plot (forecast vs actual)
- [ ] Error metrics table
- [ ] 1-paragraph discussion of forecast quality

**Sample Data:**
```python
import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=365, freq='D')

# Trend
trend = np.linspace(5000, 6500, 365)

# Weekly seasonality (weekend dip)
weekly = 500 * np.sin(2 * np.pi * np.arange(365) / 7)

# Annual seasonality (Q4 spike)
annual = 800 * np.sin(2 * np.pi * np.arange(365) / 365 - np.pi/2)

# Noise
noise = np.random.normal(0, 200, 365)

sales = trend + weekly + annual + noise

df = pd.DataFrame({
    'Date': dates,
    'Sales': sales
})
df.to_csv('daily_sales_forecast.csv', index=False)
```

**Grading (25 points):**
- Forecast visualization (10 pts)
- Uncertainty quantification (5 pts)
- Validation analysis (7 pts)
- Discussion (3 pts)

---

## 🎯 Exercise 5: Interactive Dashboard

**Objective:** Build an interactive time series dashboard using Plotly.

**Dataset:** Multiple time series (sales across 5 products over 2 years)

**Required Features:**

**1. Main Time Series Plot**
- Multiple product lines on one chart
- Range slider for date selection
- Hover tooltips showing exact values
- Toggle visibility (show/hide individual series)

**2. Comparison View**
- Index-based comparison (all start at 100)
- Percent change view
- Selectable base period

**3. Seasonal Analysis**
- Month-over-month comparison
- Box plots by season
- Year-over-year overlay

**4. Summary Statistics Panel**
- Current values for each product
- Growth rates (%, absolute)
- Volatility metrics
- Correlation matrix

**5. Controls**
- Dropdown: Select aggregation (daily, weekly, monthly)
- Radio buttons: Raw vs seasonally adjusted
- Date range picker: Custom time windows
- Export button: Download current view

**Technical Requirements:**

- Use Plotly Dash or Plotly Express
- Responsive design (works on desktop/tablet)
- Professional styling
- Fast updates (< 1 second)
- Export to HTML (standalone)

**Deliverables:**
- [ ] Python script creating the dashboard
- [ ] HTML export of the dashboard
- [ ] Screenshots of key views
- [ ] README with usage instructions

**Sample Data:**
```python
import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range('2022-01-01', periods=730, freq='D')

products = ['Product_A', 'Product_B', 'Product_C', 'Product_D', 'Product_E']
data = {'Date': dates}

for i, product in enumerate(products):
    # Each product has different baseline and growth
    baseline = (i + 1) * 1000
    growth = np.cumsum(np.random.randn(730) * 10)
    seasonal = 200 * np.sin(2 * np.pi * np.arange(730) / 365)
    noise = np.random.normal(0, 50, 730)
    
    data[product] = baseline + growth + seasonal + noise

df = pd.DataFrame(data)
df.to_csv('multi_product_sales.csv', index=False)
```

**Grading (25 points):**
- Interactive plots (10 pts)
- Features/controls (8 pts)
- Design/usability (4 pts)
- Documentation (3 pts)

---

## 📊 Bonus Challenge: Complete Time Series Report

**Objective:** Create a comprehensive time series analysis report combining all techniques.

**Scenario:** 

You are a data analyst for a retail company. Management wants to understand their sales patterns and forecast demand for the next quarter to optimize inventory.

**Dataset:** Daily sales data (3 years) with:
- Strong annual seasonality (holiday shopping)
- Weekly patterns (weekend effects)
- Growing trend
- Several promotional events (anomalies)
- Some missing data (system outages)

**Required Sections:**

**1. Executive Summary** (1 page)
- Key findings
- Forecast summary
- Recommendations

**2. Exploratory Analysis**
- Time series plot with annotations
- Missing data analysis and handling approach
- Trend identification and quantification
- Seasonal pattern visualization

**3. Decomposition Analysis**
- STL decomposition plots
- Component strengths
- Seasonally adjusted series
- Anomaly detection

**4. Forecast**
- 90-day forecast with uncertainty
- Method justification
- Validation on hold-out data
- Error analysis

**5. Interactive Dashboard**
- Multiple views (trend, seasonal, comparison)
- Drill-down capability
- Export functionality

**6. Recommendations**
- Inventory planning based on forecast
- Risk assessment (worst/best case)
- When to revise forecast

**Deliverables:**
- [ ] PDF report (max 10 pages)
- [ ] Jupyter notebook with all code
- [ ] Interactive dashboard (HTML)
- [ ] Presentation slides (5-7 slides)

**Grading (100 points):**
- Executive summary (15 pts)
- Exploratory analysis (20 pts)
- Decomposition (20 pts)
- Forecasting (25 pts)
- Dashboard (15 pts)
- Recommendations (5 pts)

---

## 📝 Submission Guidelines

**Format:**
- Submit via Canvas/LMS
- Include all code (Python scripts or notebooks)
- Visualizations as PNG (300 DPI minimum)
- Write-ups in PDF

**File Naming:**
- `LastName_FirstName_Ex1.pdf`
- `LastName_FirstName_Ex1_code.ipynb`
- Etc.

**Due Dates:**
- Exercises 1-3: Due 1 week after class
- Exercise 4: Due 2 weeks after class
- Exercise 5: Due 3 weeks after class
- Bonus: Optional, due end of semester

**Code Requirements:**
- Well-commented
- Follows PEP 8 style
- Reproducible (include random seeds)
- Clear output/visualizations

---

## 💡 Tips for Success

**1. Start Early**
- Don't wait until the due date
- Time series analysis takes time to do well
- Iterate on visualizations

**2. Use Class Examples**
- All code from Parts 1-3 is available
- Adapt examples to your datasets
- Reference the notebooks

**3. Validate Your Work**
- Check residuals are random
- Verify forecast makes sense
- Test interactive features

**4. Document Assumptions**
- Why did you choose that method?
- What aggregation level and why?
- How did you handle missing data?

**5. Make it Visual**
- Visualization quality matters
- Use color purposefully
- Add annotations and context
- Professional appearance

---

## 📚 Resources

**Documentation:**
- [pandas time series](https://pandas.pydata.org/docs/user_guide/timeseries.html)
- [statsmodels](https://www.statsmodels.org/stable/tsa.html)
- [Plotly time series](https://plotly.com/python/time-series/)
- [Prophet](https://facebook.github.io/prophet/)

**Sample Datasets:**
- Federal Reserve Economic Data (FRED)
- Yahoo Finance (stock data)
- Kaggle time series datasets
- Class-provided CSV files

**Getting Help:**
- Office hours
- Discussion forum
- Study groups
- Class 5 Part notebooks

---

## ✅ Exercise Checklist

Before submitting, ensure:

- [ ] All required visualizations included
- [ ] Code runs without errors
- [ ] Proper time scale selected and justified
- [ ] Missing data handled (if any)
- [ ] Axes labeled with units
- [ ] Titles describe what's shown
- [ ] Uncertainty included in forecasts
- [ ] Interpretation/insights provided
- [ ] Professional appearance
- [ ] Files named correctly

---

**Good luck! These exercises will give you practical experience with time series visualization - a critical skill for data science careers.** 🎓
