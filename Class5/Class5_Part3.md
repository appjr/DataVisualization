# Class 5 – Advanced Techniques

[← Main](Class5.md) | [Part 1](Class5_Part1.md) | [Part 2](Class5_Part2.md) | [Part 3](Class5_Part3.md) | [Part 4](Class5_Part4.md)

---

# PART 3: ADVANCED TIME SERIES TECHNIQUES
# Slides 41-60
# ═══════════════════════════════════════════════════════════════

## Comparing Multiple Time Series

**Comparing multiple time series requires careful attention to scales and alignment**

**The Challenge:**

When visualizing multiple time series together, you face:
- Different absolute levels (one series in thousands, another in millions)
- Different units (dollars vs percentages vs counts)
- Different scales obscure patterns
- Hard to compare trends when baselines differ

**Common Mistakes:**

❌ **Plotting raw values with very different scales**
```python
# BAD: Can't see both series clearly
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(dates, revenue, label='Revenue ($M)')  # Range: 10-50
ax.plot(dates, units, label='Units Sold')      # Range: 1000-5000
# Revenue line is flat because units dominate the y-axis!
```

**Solution Strategies:**

**1. Dual Y-Axes (Use Sparingly)**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate two series with different scales
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=180, freq='D')
revenue = 20 + np.cumsum(np.random.randn(180) * 2)  # $10-30M range
units = 2000 + np.cumsum(np.random.randn(180) * 50)  # 1500-2500 range

# Dual axes
fig, ax1 = plt.subplots(figsize=(14, 6))

# First y-axis (revenue)
ax1.plot(dates, revenue, linewidth=2, color='blue', label='Revenue ($M)')
ax1.set_xlabel('Date', fontsize=12)
ax1.set_ylabel('Revenue ($M)', fontsize=12, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Second y-axis (units)
ax2 = ax1.twinx()
ax2.plot(dates, units, linewidth=2, color='red', label='Units Sold')
ax2.set_ylabel('Units Sold', fontsize=12, color='red')
ax2.tick_params(axis='y', labelcolor='red')

ax1.set_title('Dual Y-Axes: Use Sparingly (Can Be Misleading)', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)

# Add legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()
```

**⚠️ Warning:** Dual y-axes can be misleading. Use only when absolutely necessary.

**2. Small Multiples (Better)**

```python
# BETTER: Separate panels, same x-axis
fig, axes = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

# Revenue
axes[0].plot(dates, revenue, linewidth=2, color='blue')
axes[0].set_ylabel('Revenue ($M)', fontsize=12)
axes[0].set_title('Revenue Trend', fontsize=13, fontweight='bold')
axes[0].grid(True, alpha=0.3)

# Units
axes[1].plot(dates, units, linewidth=2, color='red')
axes[1].set_ylabel('Units Sold', fontsize=12)
axes[1].set_xlabel('Date', fontsize=12)
axes[1].set_title('Units Sold Trend', fontsize=13, fontweight='bold')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**3. Normalization Methods (Best for Pattern Comparison)**

See next slide for index-based comparisons.

**Best Practices:**

✅ **DO:**
- Use consistent time alignment
- Choose appropriate comparison method for your goal
- Label all series clearly
- Use small multiples when scales differ greatly
- Provide context in titles/captions

❌ **DON'T:**
- Force different scales onto same y-axis
- Use dual y-axes without clear justification
- Compare series with different time ranges
- Use more than 5-7 series on one plot

---

## Index-Based Comparisons

**Normalize all series to a common starting point for fair pattern comparison**

**What is Index-Based Comparison?**

**Index normalization** sets all series to the same value (typically 100) at a base time period. This:
- Removes scale differences
- Highlights relative performance
- Shows which series grew faster
- Makes patterns comparable

**When to Use:**

- ✅ Comparing growth rates across different scales
- ✅ Stock price comparisons
- ✅ Economic indicators (GDP, employment, etc.)
- ✅ Sales performance across products/regions
- ✅ When absolute values less important than relative change

**Basic Implementation:**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate 3 series with different starting levels
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=365, freq='D')

# Different baselines but similar growth rates
product_a = 10000 + np.cumsum(np.random.randn(365) * 100)  # ~$10k base
product_b = 50000 + np.cumsum(np.random.randn(365) * 200)  # ~$50k base  
product_c = 100000 + np.cumsum(np.random.randn(365) * 300) # ~$100k base

df = pd.DataFrame({
    'Date': dates,
    'Product_A': product_a,
    'Product_B': product_b,
    'Product_C': product_c
})

# Problem: Hard to compare on raw scale
fig, axes = plt.subplots(2, 1, figsize=(14, 12))

# Raw values (Product C dominates)
axes[0].plot(df['Date'], df['Product_A'], linewidth=2, label='Product A')
axes[0].plot(df['Date'], df['Product_B'], linewidth=2, label='Product B')
axes[0].plot(df['Date'], df['Product_C'], linewidth=2, label='Product C')
axes[0].set_ylabel('Sales ($)', fontsize=11)
axes[0].set_title('❌ Raw Values: Hard to Compare Performance (Different Scales)', 
                   fontsize=13, fontweight='bold', color='red')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Index to base period (Day 1 = 100)
df['Product_A_Index'] = (df['Product_A'] / df['Product_A'].iloc[0]) * 100
df['Product_B_Index'] = (df['Product_B'] / df['Product_B'].iloc[0]) * 100
df['Product_C_Index'] = (df['Product_C'] / df['Product_C'].iloc[0]) * 100

axes[1].plot(df['Date'], df['Product_A_Index'], linewidth=2, label='Product A')
axes[1].plot(df['Date'], df['Product_B_Index'], linewidth=2, label='Product B')
axes[1].plot(df['Date'], df['Product_C_Index'], linewidth=2, label='Product C')
axes[1].axhline(100, color='black', linestyle='--', linewidth=1, alpha=0.5)
axes[1].set_ylabel('Index (Day 1 = 100)', fontsize=11)
axes[1].set_xlabel('Date', fontsize=12)
axes[1].set_title('✅ Indexed Values: Easy to Compare Relative Performance', 
                   fontsize=13, fontweight='bold', color='green')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Report performance
print("Relative Performance (Day 1 to Day 365):")
print(f"  Product A: {df['Product_A_Index'].iloc[-1]:.1f}% ({df['Product_A_Index'].iloc[-1]-100:+.1f}%)")
print(f"  Product B: {df['Product_B_Index'].iloc[-1]:.1f}% ({df['Product_B_Index'].iloc[-1]-100:+.1f}%)")
print(f"  Product C: {df['Product_C_Index'].iloc[-1]:.1f}% ({df['Product_C_Index'].iloc[-1]-100:+.1f}%)")
```

**Choosing Base Period:**

| Base Choice | When to Use | Example |
|-------------|-------------|---------|
| **First period** | Default, shows total change | Jan 1 = 100 |
| **Peak** | Show decline from maximum | Pre-crisis level = 100 |
| **Specific date** | Compare to important event | Pre-policy = 100 |
| **Average** | Remove level, show deviations | Mean = 100 |

**Advanced: Multiple Base Periods**

```python
# Year-over-year index (reset each January)
df['Year'] = df['Date'].dt.year
df['YOY_Index'] = df.groupby('Year')['Product_A'].transform(
    lambda x: (x / x.iloc[0]) * 100
)

fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df['Date'], df['YOY_Index'], linewidth=2)

# Mark January (resets)
for year in df['Year'].unique()[1:]:
    jan_date = df[df['Year'] == year]['Date'].iloc[0]
    ax.axvline(jan_date, color='gray', linestyle='--', alpha=0.5)

ax.axhline(100, color='black', linestyle='-', linewidth=1)
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Year-to-Date Index (Jan 1 = 100)', fontsize=12)
ax.set_title('Year-over-Year Performance Index (Resets Annually)', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Best Practices:**

✅ **DO:**
- Clearly label base period (e.g., "Jan 2020 = 100")
- Use horizontal line at 100 for reference
- Explain index methodology in caption
- Show absolute values in a table if needed

❌ **DON'T:**
- Change base period mid-presentation
- Forget to mention what 100 represents
- Use indexing when absolute values matter
- Index series with different seasonality without adjusting

**Key Insight:** Indexing reveals WHO performed better, not HOW MUCH in absolute terms.

---

## Percent Change Visualization

**Percent change shows growth rates instead of absolute levels**

**Why Use Percent Change?**

**Percent change** (also called returns in finance) shows:
- Rate of growth/decline
- Period-to-period changes
- Volatility and variability
- Comparable metrics across different scales

**Calculation:**

```python
# Simple percent change
pct_change = (Value(t) - Value(t-1)) / Value(t-1) × 100

# In pandas
df['Pct_Change'] = df['Value'].pct_change() * 100
```

**Example:**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate price data
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=252, freq='B')  # Business days
price = 100 * np.exp(np.cumsum(np.random.randn(252) * 0.02))  # Random walk

df = pd.DataFrame({'Date': dates, 'Price': price})

# Calculate percent change
df['Daily_Return'] = df['Price'].pct_change() * 100

# Visualize
fig, axes = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

# Price level
axes[0].plot(df['Date'], df['Price'], linewidth=2, color='blue')
axes[0].set_ylabel('Price ($)', fontsize=11)
axes[0].set_title('Stock Price (Absolute Level)', fontsize=13, fontweight='bold')
axes[0].grid(True, alpha=0.3)

# Percent change
axes[1].plot(df['Date'], df['Daily_Return'], linewidth=1, color='red', alpha=0.7)
axes[1].axhline(0, color='black', linestyle='-', linewidth=1)
axes[1].fill_between(df['Date'], 0, df['Daily_Return'],
                     where=(df['Daily_Return'] > 0), alpha=0.3, color='green', label='Gains')
axes[1].fill_between(df['Date'], 0, df['Daily_Return'],
                     where=(df['Daily_Return'] <= 0), alpha=0.3, color='red', label='Losses')
axes[1].set_xlabel('Date', fontsize=12)
axes[1].set_ylabel('Daily Return (%)', fontsize=11)
axes[1].set_title('Daily Percent Changes (Volatility Visible)', fontsize=13, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Statistics
print(f"Average daily return: {df['Daily_Return'].mean():.3f}%")
print(f"Volatility (std dev): {df['Daily_Return'].std():.3f}%")
print(f"Max gain: {df['Daily_Return'].max():.2f}%")
print(f"Max loss: {df['Daily_Return'].min():.2f}%")
```

**Comparing Multiple Series:**

```python
# Three stocks with different price levels
stock_a = 50 * np.exp(np.cumsum(np.random.randn(252) * 0.015))
stock_b = 150 * np.exp(np.cumsum(np.random.randn(252) * 0.020))
stock_c = 300 * np.exp(np.cumsum(np.random.randn(252) * 0.018))

df_stocks = pd.DataFrame({
    'Date': dates,
    'Stock_A': stock_a,
    'Stock_B': stock_b,
    'Stock_C': stock_c
})

# Calculate returns
df_stocks['Return_A'] = df_stocks['Stock_A'].pct_change() * 100
df_stocks['Return_B'] = df_stocks['Stock_B'].pct_change() * 100
df_stocks['Return_C'] = df_stocks['Stock_C'].pct_change() * 100

# Compare
fig, axes = plt.subplots(2, 1, figsize=(14, 10))

# Prices (hard to compare)
axes[0].plot(df_stocks['Date'], df_stocks['Stock_A'], linewidth=2, label='Stock A (~$50)')
axes[0].plot(df_stocks['Date'], df_stocks['Stock_B'], linewidth=2, label='Stock B (~$150)')
axes[0].plot(df_stocks['Date'], df_stocks['Stock_C'], linewidth=2, label='Stock C (~$300)')
axes[0].set_ylabel('Price ($)', fontsize=11)
axes[0].set_title('Stock Prices: Different Levels Obscure Comparison', fontsize=13, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Returns (easy to compare volatility and performance)
axes[1].plot(df_stocks['Date'], df_stocks['Return_A'], linewidth=1, alpha=0.7, label='Stock A')
axes[1].plot(df_stocks['Date'], df_stocks['Return_B'], linewidth=1, alpha=0.7, label='Stock B')
axes[1].plot(df_stocks['Date'], df_stocks['Return_C'], linewidth=1, alpha=0.7, label='Stock C')
axes[1].axhline(0, color='black', linestyle='-', linewidth=1)
axes[1].set_xlabel('Date', fontsize=12)
axes[1].set_ylabel('Daily Return (%)', fontsize=11)
axes[1].set_title('Daily Returns: Volatility and Performance Comparable', fontsize=13, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**Cumulative Returns:**

```python
# Cumulative percent change from start
df_stocks['Cum_Return_A'] = ((df_stocks['Stock_A'] / df_stocks['Stock_A'].iloc[0]) - 1) * 100
df_stocks['Cum_Return_B'] = ((df_stocks['Stock_B'] / df_stocks['Stock_B'].iloc[0]) - 1) * 100
df_stocks['Cum_Return_C'] = ((df_stocks['Stock_C'] / df_stocks['Stock_C'].iloc[0]) - 1) * 100

fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df_stocks['Date'], df_stocks['Cum_Return_A'], linewidth=2, label='Stock A')
ax.plot(df_stocks['Date'], df_stocks['Cum_Return_B'], linewidth=2, label='Stock B')
ax.plot(df_stocks['Date'], df_stocks['Cum_Return_C'], linewidth=2, label='Stock C')
ax.axhline(0, color='black', linestyle='--', linewidth=1)

ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Cumulative Return (%)', fontsize=12)
ax.set_title('Cumulative Returns from Start', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)

# Annotate final returns
for i, (name, val) in enumerate([('A', df_stocks['Cum_Return_A'].iloc[-1]),
                                  ('B', df_stocks['Cum_Return_B'].iloc[-1]),
                                  ('C', df_stocks['Cum_Return_C'].iloc[-1])]):
    ax.text(df_stocks['Date'].iloc[-1], val, f'  {val:+.1f}%',
            va='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()
```

**Best Practices:**

✅ Use for volatility analysis
✅ Compare growth rates across assets
✅ Analyze risk (variance of returns)
✅ Show 0% reference line

❌ Don't use when absolute values matter
❌ Avoid for cumulative quantities (inventory, population)

---

## Lag Plots

**Lag plots reveal autocorrelation patterns visually**

**What is a Lag Plot?**

A **lag plot** is a scatter plot of:
- X-axis: Values at time t
- Y-axis: Values at time t+k (lagged by k periods)

Shows the relationship between current and past values.

**Why Use Lag Plots?**

- **Detect autocorrelation** - Are values related to past values?
- **Identify patterns** - Random, cyclic, trending behavior
- **Choose models** - Helps select AR, MA parameters
- **Validate assumptions** - Check for independence

**Example:**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate different types of data
np.random.seed(42)
n = 200

# 1. Random (no autocorrelation)
random_data = np.random.randn(n)

# 2. Strong positive autocorrelation
ar_data = np.zeros(n)
ar_data[0] = np.random.randn()
for t in range(1, n):
    ar_data[t] = 0.9 * ar_data[t-1] + np.random.randn() * 0.5

# 3. Seasonal pattern
seasonal_data = np.sin(2 * np.pi * np.arange(n) / 12) + np.random.randn(n) * 0.3

# Create lag plots
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Random data
axes[0].scatter(random_data[:-1], random_data[1:], alpha=0.5, s=30)
axes[0].set_xlabel('Value at time t', fontsize=11)
axes[0].set_ylabel('Value at time t+1', fontsize=11)
axes[0].set_title('Random Data\n(No Pattern = No Autocorrelation)', fontsize=12, fontweight='bold')
axes[0].grid(True, alpha=0.3)
axes[0].axhline(0, color='black', linestyle='-', linewidth=0.8, alpha=0.5)
axes[0].axvline(0, color='black', linestyle='-', linewidth=0.8, alpha=0.5)

# AR data
axes[1].scatter(ar_data[:-1], ar_data[1:], alpha=0.5, s=30, color='red')
axes[1].set_xlabel('Value at time t', fontsize=11)
axes[1].set_ylabel('Value at time t+1', fontsize=11)
axes[1].set_title('AR(1) Data\n(Linear Pattern = Strong Autocorrelation)', fontsize=12, fontweight='bold')
axes[1].grid(True, alpha=0.3)

# Add trend line
z = np.polyfit(ar_data[:-1], ar_data[1:], 1)
p = np.poly1d(z)
axes[1].plot(ar_data[:-1], p(ar_data[:-1]), "r--", linewidth=2, label=f'Slope={z[0]:.2f}')
axes[1].legend()

# Seasonal data
axes[2].scatter(seasonal_data[:-1], seasonal_data[1:], alpha=0.5, s=30, color='green')
axes[2].set_xlabel('Value at time t', fontsize=11)
axes[2].set_ylabel('Value at time t+1', fontsize=11)
axes[2].set_title('Seasonal Data\n(Elliptical Pattern)', fontsize=12, fontweight='bold')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**Using pandas lag_plot:**

```python
from pandas.plotting import lag_plot

fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Different lags
for i, lag in enumerate([1, 5, 10, 20]):
    row, col = i // 2, i % 2
    lag_plot(pd.Series(ar_data), lag=lag, ax=axes[row, col])
    axes[row, col].set_title(f'Lag Plot (lag={lag})', fontsize=13, fontweight='bold')
    axes[row, col].grid(True, alpha=0.3)

plt.suptitle('Lag Plots at Different Lags', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()
```

**Interpretation:**

| Pattern | Meaning | Implication |
|---------|---------|-------------|
| **Random cloud** | No autocorrelation | White noise, unpredictable |
| **Linear (positive slope)** | Positive autocorrelation | AR process, momentum |
| **Linear (negative slope)** | Negative autocorrelation | Mean reversion |
| **Elliptical/Circular** | Cyclic/seasonal | Periodic pattern |

**Best Practices:**

✅ Try multiple lags (1, 7, 30, 365 for daily data)
✅ Use for diagnostic purposes
✅ Compare with ACF plot
✅ Look for unexpected patterns

---

## Autocorrelation Function (ACF)

**The ACF plot shows how a time series correlates with its own past values**

**What is Autocorrelation?**

**Autocorrelation** (also called serial correlation) measures the correlation between a time series and a lagged version of itself.

**ACF** calculates correlation at all possible lags:
- Lag 1: Correlation with previous value
- Lag 2: Correlation with value 2 periods ago
- Lag k: Correlation with value k periods ago

**Why Use ACF?**

- ✅ Detect seasonality (regular spikes at seasonal lags)
- ✅ Identify appropriate lag order for models
- ✅ Check for randomness (white noise)
- ✅ Understand persistence in data

**Python Implementation:**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import acf

# Generate data with different patterns
np.random.seed(42)
n = 200

# 1. White noise (random)
white_noise = np.random.randn(n)

# 2. AR(1) - strong lag-1 correlation
ar1 = np.zeros(n)
ar1[0] = np.random.randn()
for t in range(1, n):
    ar1[t] = 0.7 * ar1[t-1] + np.random.randn() * 0.5

# 3. Seasonal - peaks at lag 12, 24, 36...
seasonal = np.sin(2 * np.pi * np.arange(n) / 12) + np.random.randn(n) * 0.3

# Plot ACF for each
fig, axes = plt.subplots(3, 1, figsize=(14, 12))

# White noise
plot_acf(white_noise, lags=40, ax=axes[0])
axes[0].set_title('ACF: White Noise (No Significant Correlations)', fontsize=13, fontweight='bold')

# AR(1)
plot_acf(ar1, lags=40, ax=axes[1])
axes[1].set_title('ACF: AR(1) Process (Exponential Decay)', fontsize=13, fontweight='bold')

# Seasonal
plot_acf(seasonal, lags=40, ax=axes[2])
axes[2].set_title('ACF: Seasonal Data (Spikes at lag 12, 24, 36...)', fontsize=13, fontweight='bold')

plt.tight_layout()
plt.show()
```

**Reading ACF Plots:**

**Confidence Bands (Blue Shaded Area):**
- Values outside bands are statistically significant
- Typically ±1.96/√n (95% confidence)
- If ACF is within bands → not significantly different from zero

**Patterns to Look For:**

| Pattern | Meaning | Example |
|---------|---------|---------|
| **All within bands** | White noise, random | Stock returns, forecast errors |
| **Slow decay** | Trend present, non-stationary | GDP, population |
| **Exponential decay** | AR process | Temperature, yields |
| **Spikes at specific lags** | Seasonality | Sales (lag 7, 30, 365) |
| **Oscillating** | Cyclical or over-differenced | Some economic data |

**ACF for Seasonality Detection:**

```python
# Daily sales with weekly seasonality
dates = pd.date_range('2024-01-01', periods=365, freq='D')
weekly_pattern = 100 + 20 * np.sin(2 * np.pi * np.arange(365) / 7)
noise = np.random.normal(0, 5, 365)
daily_sales = weekly_pattern + noise

df_sales = pd.DataFrame({'Date': dates, 'Sales': daily_sales})

# Plot ACF
fig, ax = plt.subplots(figsize=(14, 6))
plot_acf(df_sales['Sales'], lags=50, ax=ax)
ax.set_title('ACF: Weekly Seasonality Visible (Spikes at lag 7, 14, 21...)', 
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# Print significant lags
acf_values = acf(df_sales['Sales'], nlags=50)
significant_lags = np.where(np.abs(acf_values) > 1.96/np.sqrt(len(df_sales)))[0]
print(f"Significant lags: {significant_lags[:10]}")  # First 10
```

**ACF vs Time Series Plot:**

```python
fig, axes = plt.subplots(2, 1, figsize=(14, 10))

# Time series
axes[0].plot(df_sales['Date'], df_sales['Sales'], linewidth=1.5)
axes[0].set_ylabel('Sales', fontsize=11)
axes[0].set_title('Daily Sales Time Series', fontsize=13, fontweight='bold')
axes[0].grid(True, alpha=0.3)

# ACF
plot_acf(df_sales['Sales'], lags=50, ax=axes[1])
axes[1].set_title('ACF Reveals Weekly Pattern (lag 7)', fontsize=13, fontweight='bold')

plt.tight_layout()
plt.show()
```

**Best Practices:**

✅ **DO:**
- Plot enough lags to see patterns (at least 1-2 seasonal periods)
- Look for both individual spikes and overall patterns
- Use with PACF for model selection
- Interpret in context of your data frequency

❌ **DON'T:**
- Use too few lags (miss long-term patterns)
- Ignore statistical significance (blue bands)
- Confuse ACF with PACF
- Apply to non-stationary data without differencing

---

## Partial Autocorrelation (PACF)

**PACF shows direct correlation after removing indirect effects**

**What is PACF?**

**Partial autocorrelation** measures the correlation between Y(t) and Y(t-k) **after removing** the effects of all intermediate lags.

**Difference from ACF:**

| Metric | What It Shows | Use |
|--------|---------------|-----|
| **ACF** | Total correlation (direct + indirect) | Detect seasonality, MA order |
| **PACF** | Direct correlation only (controls for intermediate lags) | Identify AR order |

**Why Use PACF?**

- ✅ Identify AR model order (number of lags to include)
- ✅ Distinguish direct vs indirect relationships
- ✅ Avoid including redundant lags in models
- ✅ Understand immediate vs long-term dependencies

**Example:**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Generate AR(2) process
np.random.seed(42)
n = 300
ar2 = np.zeros(n)
ar2[0] = np.random.randn()
ar2[1] = np.random.randn()

for t in range(2, n):
    ar2[t] = 0.5 * ar2[t-1] + 0.3 * ar2[t-2] + np.random.randn() * 0.5

# Plot ACF and PACF side-by-side
fig, axes = plt.subplots(1, 2, figsize=(16, 5))

# ACF
plot_acf(ar2, lags=20, ax=axes[0])
axes[0].set_title('ACF: AR(2) Process\n(Gradual Decay)', fontsize=13, fontweight='bold')

# PACF
plot_pacf(ar2, lags=20, ax=axes[1])
axes[1].set_title('PACF: AR(2) Process\n(Cuts off after lag 2)', fontsize=13, fontweight='bold')

plt.suptitle('ACF vs PACF for AR(2) Process', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()
```

**Pattern Recognition:**

**AR Process:**
- ACF: Exponential decay
- PACF: Cuts off sharply after lag p
- **Conclusion:** Use PACF to identify AR order

**MA Process:**
- ACF: Cuts off sharply after lag q
- PACF: Exponential decay
- **Conclusion:** Use ACF to identify MA order

**ARMA Process:**
- ACF: Gradual decay
- PACF: Gradual decay
- **Conclusion:** Both AR and MA components

**Visualization Examples:**

```python
# Generate different processes
# AR(1)
ar1 = np.zeros(n)
ar1[0] = np.random.randn()
for t in range(1, n):
    ar1[t] = 0.8 * ar1[t-1] + np.random.randn() * 0.5

# MA(1)
ma1 = np.zeros(n)
errors = np.random.randn(n)
for t in range(1, n):
    ma1[t] = errors[t] + 0.6 * errors[t-1]

# Compare
fig, axes = plt.subplots(2, 2, figsize=(16, 10))

# AR(1) - ACF
plot_acf(ar1, lags=20, ax=axes[0,0])
axes[0,0].set_title('AR(1): ACF Decays', fontweight='bold')

# AR(1) - PACF
plot_pacf(ar1, lags=20, ax=axes[0,1])
axes[0,1].set_title('AR(1): PACF Cuts at lag 1', fontweight='bold')

# MA(1) - ACF
plot_acf(ma1, lags=20, ax=axes[1,0])
axes[1,0].set_title('MA(1): ACF Cuts at lag 1', fontweight='bold')

# MA(1) - PACF
plot_pacf(ma1, lags=20, ax=axes[1,1])
axes[1,1].set_title('MA(1): PACF Decays', fontweight='bold')

plt.suptitle('ACF/PACF Patterns for Model Identification', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

**Model Selection Guide:**

| ACF Pattern | PACF Pattern | Suggested Model |
|-------------|--------------|-----------------|
| Decay | Cut-off at lag p | AR(p) |
| Cut-off at lag q | Decay | MA(q) |
| Decay | Decay | ARMA(p,q) |
| Spikes at seasonal lags | Spikes at seasonal lags | Seasonal ARIMA |

**Best Practices:**

✅ Always plot both ACF and PACF together
✅ Use for ARIMA model selection
✅ Look at first 1-2 seasonal periods of lags
✅ Difference data first if non-stationary

---

## Cross-Correlation

**Measure relationship between two time series**

(Will expand...)

---

## Lead-Lag Relationships

**Does one series predict another?**

(Will expand...)

---

## Forecasting Visualization Principles

**Show historical data, forecast horizon, and uncertainty**

(Will expand...)

---

## Point Forecasts vs. Intervals

Always include intervals for uncertainty.

---

## Confidence Intervals

```python
plt.fill_between(dates, lower, upper, alpha=0.2)
```

---

## Fan Charts

Multiple interval bands for forecast risk.

---

## Backtesting Visualizations

Plot predicted vs. actual values.

---

## Forecast Error Analysis

Residual plots to inspect bias.

---

## Calendar Heatmaps

Great for daily/weekly patterns.

---

## Horizon Charts

Compact time series visualization.

---

## Stream Graphs

Use stacked flowing areas for composition.

---

## Cycle Plots

Compare seasons across years.

---

## Interactive Time Series with Plotly

```python
import plotly.express as px
px.line(df, x='Date', y='Sales')
```

---

## Part 3 Summary

✅ Advanced visualization techniques  
✅ Forecast evaluation  
✅ Autocorrelation insights

---

# ═══════════════════════════════════════════════════════════════
# PART 4: IMPLEMENTATION & APPLICATIONS
# Slides 61-80
# ═══════════════════════════════════════════════════════════════

## Python Tools for Time Series

- pandas
