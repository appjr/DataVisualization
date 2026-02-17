# Class 5 – Temporal Patterns & Decomposition

[← Main](Class5.md) | [Part 1](Class5_Part1.md) | [Part 2](Class5_Part2.md) | [Part 3](Class5_Part3.md) | [Part 4](Class5_Part4.md)

---

# PART 2: TEMPORAL PATTERNS & DECOMPOSITION
# Slides 21-40
# ═══════════════════════════════════════════════════════════════

## Introduction to Temporal Patterns

**Real-world time series data rarely follows a simple straight line**

Time series typically contain **multiple overlapping patterns** that interact and combine to create the observed values. Understanding and separating these patterns is crucial for:
- **Forecasting** - Predict future values based on historical patterns
- **Analysis** - Understand what drives changes over time
- **Anomaly Detection** - Spot unusual behavior that breaks patterns
- **Decision Making** - Plan based on expected patterns

**The Four Main Components:**

**1. Trend (T)**
- **Definition**: Long-term directional movement in the data
- **Timeframe**: Extends across the entire dataset or major portions
- **Causes**: Fundamental changes (population growth, market expansion, technological progress)
- **Characteristics**: 
  - Smooth, gradual change
  - Can be upward, downward, or flat
  - May change direction (inflection points)
- **Examples**:
  - Rising global temperatures (climate change)
  - Declining manufacturing employment (automation)
  - Increasing e-commerce sales (digital transformation)

**2. Seasonality (S)**
- **Definition**: Repeating patterns at fixed, regular intervals
- **Timeframe**: Fixed period (daily, weekly, monthly, quarterly, yearly)
- **Causes**: Calendar effects, weather, holidays, business cycles
- **Characteristics**:
  - Predictable and recurring
  - Same pattern repeats
  - Fixed frequency
- **Examples**:
  - Retail sales spike every December (holiday shopping)
  - Ice cream sales higher in summer months
  - Website traffic lower on weekends
  - Quarterly earnings reporting patterns

**3. Cycles (C)**
- **Definition**: Irregular, longer-term fluctuations (not fixed frequency)
- **Timeframe**: Variable duration, typically multi-year
- **Causes**: Economic conditions, political changes, market forces
- **Characteristics**:
  - Irregular timing
  - Variable amplitude
  - Harder to predict
- **Examples**:
  - Business cycles (recession → recovery → expansion → peak)
  - Housing market boom and bust
  - Commodity price cycles
  - Election cycles affecting certain industries

**4. Noise/Residual (ε)**
- **Definition**: Random variation not explained by other components
- **Timeframe**: Irregular, unpredictable
- **Causes**: Random events, measurement error, unexplained factors
- **Characteristics**:
  - No pattern
  - Should be small if model is good
  - Ideally resembles white noise
- **Examples**:
  - Daily weather variations affecting sales
  - Random customer behavior
  - Measurement errors in sensors

**Mathematical Representation:**

**Additive Model** (components add together):
```
Y(t) = T(t) + S(t) + C(t) + ε(t)
```
Use when: Seasonal variation is relatively constant over time

**Multiplicative Model** (components multiply):
```
Y(t) = T(t) × S(t) × C(t) × ε(t)
```
Use when: Seasonal variation grows/shrinks with the trend

**Why This Matters for Visualization:**

Understanding these components helps you:
1. **Choose the right time scale** - Match to the pattern you want to show
2. **Annotate effectively** - Mark seasonal events, trend changes, anomalies
3. **Design comparisons** - Remove trend to compare seasonal patterns
4. **Set expectations** - Explain what patterns are normal vs unusual
5. **Build better models** - Decomposition reveals what drives the series

**Example: Retail Sales**
```
Observed daily sales = 
  + Growing trend (market expansion)
  + Weekly seasonality (weekend spikes)  
  + Annual seasonality (holiday shopping)
  + Economic cycle (recession/recovery)
  + Random noise (weather, events)
```

**Key Insight**: You can't analyze or forecast well without understanding which components drive your data. Visualization is the first step in pattern recognition.

---

## Identifying Trends

**A trend is the overall long-term direction of a time series**

**What is a Trend?**

A **trend** represents the underlying trajectory of your data when you look past short-term fluctuations. It answers: "Where is this heading overall?"

**Types of Trends:**

**1. No Trend (Stationary)**
- Series fluctuates around a constant mean
- No long-term increase or decrease
- Example: Daily temperatures (fluctuate but no long-term change)

**2. Linear Trend (Most Common)**
- Constant rate of change
- Straight line when averaged
- Example: Steady 5% annual growth

**3. Non-Linear Trends**
- **Exponential**: Accelerating growth (compound interest)
- **Logarithmic**: Fast initial growth, then flattening
- **Polynomial**: Multiple direction changes
- **Step**: Sudden jumps to new levels

**Visual Detection Methods:**

**Method 1: Simple Line Plot**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate example data with trend
np.random.seed(42)
dates = pd.date_range('2020-01-01', periods=1000, freq='D')
trend = np.linspace(100, 150, 1000)
noise = np.random.normal(0, 5, 1000)
data = trend + noise

df = pd.DataFrame({'Date': dates, 'Value': data})

# Plot
plt.figure(figsize=(14, 6))
plt.plot(df['Date'], df['Value'], linewidth=1, alpha=0.7, label='Observed Data')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.title('Identifying Trend in Time Series', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Method 2: Add Trend Line**
```python
# Using seaborn for trend line
fig, ax = plt.subplots(figsize=(14, 6))

# Scatter plot with trend
sns.regplot(data=df, x=np.arange(len(df)), y='Value', 
            scatter_kws={'alpha':0.3, 's':10}, 
            line_kws={'color':'red', 'linewidth':3, 'label':'Trend Line'},
            ax=ax)

# Format
ax.set_xlabel('Time Index', fontsize=12)
ax.set_ylabel('Value', fontsize=12)
ax.set_title('Linear Trend Detection', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Method 3: Moving Average (Smooth Trend)**
```python
# Calculate moving averages
df['MA_30'] = df['Value'].rolling(window=30).mean()
df['MA_90'] = df['Value'].rolling(window=90).mean()

# Plot
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df['Date'], df['Value'], linewidth=1, alpha=0.3, color='gray', label='Raw Data')
ax.plot(df['Date'], df['MA_30'], linewidth=2, color='blue', label='30-day MA')
ax.plot(df['Date'], df['MA_90'], linewidth=2.5, color='red', label='90-day MA')

ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Value', fontsize=12)
ax.set_title('Trend Revealed by Moving Averages', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Statistical Trend Tests:**

```python
# Augmented Dickey-Fuller test for trend stationarity
from statsmodels.tsa.stattools import adfuller

result = adfuller(df['Value'])
print(f'ADF Statistic: {result[0]}')
print(f'p-value: {result[1]}')

if result[1] < 0.05:
    print("✓ Stationary (no significant trend)")
else:
    print("✗ Non-stationary (trend present)")
```

**Quantifying Trends:**

```python
# Linear regression to measure trend
from scipy import stats

x = np.arange(len(df))
y = df['Value'].values

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

print(f'Trend slope: {slope:.3f} units per time period')
print(f'R-squared: {r_value**2:.3f} (trend explains {r_value**2*100:.1f}% of variation)')
```

**When to Remove Trends (Detrending):**

**Why detrend?**
- To analyze seasonality without trend interference
- To make series stationary for modeling
- To compare multiple series with different trends

**How to detrend:**
```python
# Method 1: Differencing (simple)
df['Detrended'] = df['Value'].diff()

# Method 2: Linear detrending
from scipy.signal import detrend
df['Detrended'] = detrend(df['Value'])

# Method 3: Subtract fitted trend
from sklearn.linear_model import LinearRegression
X = np.arange(len(df)).reshape(-1, 1)
y = df['Value'].values

model = LinearRegression()
model.fit(X, y)
trend_fit = model.predict(X)

df['Detrended'] = df['Value'] - trend_fit
```

**Visualization Best Practices for Trends:**

✅ **DO:**
- Use moving averages to smooth noise and reveal trend
- Add trend line to show direction clearly
- Annotate inflection points where trend changes
- Compare with benchmarks or targets
- Show confidence intervals around trend estimate

❌ **DON'T:**
- Confuse short-term fluctuations with trend changes
- Ignore statistical significance of trend
- Use too short a time window to assess trend
- Forget to account for seasonality when assessing trend

**Key Takeaway**: A trend is the signal you're trying to extract from the noise. Good trend identification requires both visual inspection and statistical validation.

---

## Linear vs. Non-Linear Trends

**Different types of trends require different approaches**

**Understanding trend shape is critical** for:
- Choosing the right model
- Making accurate forecasts
- Communicating expectations
- Detecting pattern changes

**1. Linear Trend**

**Definition**: Constant rate of change over time

**Mathematical form:**
```
Y(t) = β₀ + β₁×t + ε(t)
where β₁ = constant slope
```

**Characteristics:**
- ✅ Same absolute change each period
- ✅ Straight line when plotted
- ✅ Easy to understand and explain
- ✅ Simple to forecast

**When it occurs:**
- Steady population growth
- Constant production increases
- Regular savings accumulation
- Uniform technology adoption

**Example & Code:**
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate linear trend data
np.random.seed(42)
dates = pd.date_range('2020-01-01', periods=365*3, freq='D')
linear_trend = 100 + 0.05 * np.arange(len(dates))  # +0.05 per day
noise = np.random.normal(0, 5, len(dates))
linear_data = linear_trend + noise

df_linear = pd.DataFrame({'Date': dates, 'Value': linear_data})

# Fit linear trend
from scipy.stats import linregress
x = np.arange(len(df_linear))
slope, intercept, r, p, se = linregress(x, df_linear['Value'])

# Visualize
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df_linear['Date'], df_linear['Value'], linewidth=1, alpha=0.6, label='Data')
ax.plot(df_linear['Date'], intercept + slope * x, linewidth=3, color='red', 
        label=f'Linear Trend (slope={slope:.3f})')

ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Value', fontsize=12)
ax.set_title('Linear Trend: Constant Rate of Change', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print(f'Linear trend: {slope:.3f} units per day')
print(f'Forecasted value in 30 days: {intercept + slope * (len(df_linear) + 30):.1f}')
```

---

**2. Exponential Trend**

**Definition**: Constant *percentage* rate of change (compound growth)

**Mathematical form:**
```
Y(t) = β₀ × e^(β₁×t)
where β₁ = growth rate
```

**Characteristics:**
- ✅ Percentage change stays constant
- ✅ Absolute change accelerates over time
- ✅ Appears as curve upward or downward
- ✅ Straight line on log scale

**When it occurs:**
- Viral spread (diseases, social media)
- Compound interest/investment growth
- Population growth (unconstrained)
- Technology adoption (early phase)
- Pandemic case counts

**Example & Code:**
```python
# Generate exponential trend data
exp_trend = 100 * np.exp(0.002 * np.arange(len(dates)))  # 0.2% daily growth
exp_noise = np.random.normal(0, exp_trend * 0.05)  # 5% noise
exp_data = exp_trend + exp_noise

df_exp = pd.DataFrame({'Date': dates, 'Value': exp_data})

# Fit exponential model
from scipy.optimize import curve_fit

def exp_model(x, a, b):
    return a * np.exp(b * x)

params, _ = curve_fit(exp_model, x, df_exp['Value'])
exp_fit = exp_model(x, *params)

# Visualize
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Regular scale
axes[0].plot(df_exp['Date'], df_exp['Value'], linewidth=1, alpha=0.6, label='Data')
axes[0].plot(df_exp['Date'], exp_fit, linewidth=3, color='red', 
             label=f'Exp Trend (growth={params[1]:.4f})')
axes[0].set_xlabel('Date')
axes[0].set_ylabel('Value')
axes[0].set_title('Exponential Trend: Accelerating Growth', fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Log scale (makes exponential linear)
axes[1].semilogy(df_exp['Date'], df_exp['Value'], linewidth=1, alpha=0.6, label='Data (log scale)')
axes[1].semilogy(df_exp['Date'], exp_fit, linewidth=3, color='red', label='Trend Line')
axes[1].set_xlabel('Date')
axes[1].set_ylabel('Value (log scale)')
axes[1].set_title('Same Data on Log Scale (Linear!)', fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f'Exponential growth rate: {params[1]:.4f} per day ({params[1]*365:.2f} per year)')
print(f'Daily percentage growth: {(np.exp(params[1])-1)*100:.2f}%')
```

---

**3. Logarithmic Trend**

**Definition**: Rapid initial growth that gradually slows and flattens

**Mathematical form:**
```
Y(t) = β₀ + β₁×log(t)
```

**Characteristics:**
- ✅ Fast growth initially
- ✅ Diminishing returns over time
- ✅ Approaches an asymptote (ceiling)
- ✅ Common in learning curves

**When it occurs:**
- Technology adoption (late phase - market saturation)
- Learning curves (skills improve quickly then plateau)
- Resource extraction (easy resources first, then harder)
- Market penetration (fast growth in new market, then saturation)

**Example & Code:**
```python
# Generate logarithmic trend
log_trend = 100 + 20 * np.log(np.arange(1, len(dates)+1))
log_noise = np.random.normal(0, 3, len(dates))
log_data = log_trend + log_noise

df_log = pd.DataFrame({'Date': dates, 'Value': log_data})

# Fit logarithmic model
def log_model(x, a, b):
    return a + b * np.log(x + 1)

params_log, _ = curve_fit(log_model, x, df_log['Value'])
log_fit = log_model(x, *params_log)

# Visualize
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df_log['Date'], df_log['Value'], linewidth=1, alpha=0.6, label='Data')
ax.plot(df_log['Date'], log_fit, linewidth=3, color='red', 
        label=f'Log Trend')

ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Value', fontsize=12)
ax.set_title('Logarithmic Trend: Fast Start, Then Flattening', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)

# Add annotation
ax.annotate('Fast growth phase', xy=(dates[100], log_data[100]), 
            xytext=(dates[200], log_data[100]+20),
            arrowprops=dict(arrowstyle='->', lw=2, color='green'),
            fontsize=11, color='green', fontweight='bold')
ax.annotate('Flattening phase', xy=(dates[800], log_data[800]), 
            xytext=(dates[700], log_data[800]-20),
            arrowprops=dict(arrowstyle='->', lw=2, color='orange'),
            fontsize=11, color='orange', fontweight='bold')

plt.tight_layout()
plt.show()
```

---

**Comparing Trend Types Side-by-Side:**

```python
# Generate all three types
t = np.arange(100)
linear = 100 + 2 * t
exponential = 100 * (1.02 ** t)
logarithmic = 100 + 40 * np.log(t + 1)

# Plot
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

axes[0].plot(t, linear, linewidth=3, color='blue')
axes[0].set_title('Linear Trend\n(Constant Rate)', fontsize=13, fontweight='bold')
axes[0].set_xlabel('Time')
axes[0].set_ylabel('Value')
axes[0].grid(True, alpha=0.3)

axes[1].plot(t, exponential, linewidth=3, color='red')
axes[1].set_title('Exponential Trend\n(Accelerating)', fontsize=13, fontweight='bold')
axes[1].set_xlabel('Time')
axes[1].set_ylabel('Value')
axes[1].grid(True, alpha=0.3)

axes[2].plot(t, logarithmic, linewidth=3, color='green')
axes[2].set_title('Logarithmic Trend\n(Flattening)', fontsize=13, fontweight='bold')
axes[2].set_xlabel('Time')
axes[2].set_ylabel('Value')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**How to Choose the Right Trend Model:**

| Trend Type | When to Use | How to Identify | Model |
|------------|-------------|-----------------|-------|
| **Linear** | Constant absolute growth | Straight line on regular plot | `y = a + b×t` |
| **Exponential** | Constant % growth | Straight on log plot; curve on regular | `y = a×e^(b×t)` |
| **Logarithmic** | Diminishing returns | Fast start then flat | `y = a + b×log(t)` |
| **Polynomial** | Multiple inflections | S-curves, multiple peaks | `y = a + b×t + c×t²...` |

**Practical Tips:**

1. **Start with visualization** - Plot the data first
2. **Try transformations** - Log scale often reveals exponential trends
3. **Use domain knowledge** - What kind of growth makes sense for your data?
4. **Test multiple models** - Compare R² and residuals
5. **Be cautious with forecasts** - Trends can change!

**Common Mistakes:**

❌ Assuming linear when growth is exponential (under-forecasting)
❌ Extrapolating exponential trends too far (over-forecasting)
❌ Ignoring structural breaks (trend changes)
❌ Fitting high-order polynomials (overfitting)

✅ Match trend type to the generating process
✅ Validate with out-of-sample data
✅ Show uncertainty in trend estimates
✅ Update trend model as new data arrives

---

## Seasonal Patterns

**Seasonality is one of the most powerful and predictable patterns in time series**

**What is Seasonality?**

**Seasonality** refers to regular, predictable fluctuations that repeat at fixed intervals. Unlike trends (which show long-term direction) or cycles (which are irregular), seasonal patterns have:
- **Fixed frequency** - Same time interval every repetition
- **Consistent shape** - Pattern roughly repeats
- **Predictability** - Future seasonal behavior can be forecasted

**Common Seasonal Periods:**

| Period | Interval | Examples |
|--------|----------|----------|
| **Daily** | 24 hours | Hourly electricity usage (peak mornings/evenings) |
| **Weekly** | 7 days | Retail sales (weekend spikes), web traffic (weekday peaks) |
| **Monthly** | ~30 days | Bill payments (month-end), paychecks (bi-weekly/monthly) |
| **Quarterly** | 3 months | Corporate earnings, seasonal fashion collections |
| **Annual** | 12 months | Holiday shopping, tax season, summer vacations |

**Examples of Seasonality:**

**Retail:**
- December sales spike (holiday shopping)
- Back-to-school sales in August
- Black Friday/Cyber Monday peaks
- January slump (post-holiday)

**Weather-Dependent:**
- Ice cream sales (higher in summer)
- Heating oil demand (higher in winter)
- Umbrella sales (rainy seasons)
- Tourism (summer/winter peaks)

**Calendar-Driven:**
- Tax preparation (April in US)
- Fitness memberships (January resolutions)
- Academic enrollment (fall semester)
- Vacation booking (spring for summer travel)

**Business Cycles:**
- End-of-quarter reporting pushes
- Month-end account reconciliation
- Weekly inventory counts
- Daily batch processing schedules

**Visualizing Seasonal Patterns:**

**Method 1: Simple Plot with Seasonal Highlighting**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate data with strong seasonality
np.random.seed(42)
dates = pd.date_range('2020-01-01', periods=365*3, freq='D')
trend = np.linspace(100, 120, len(dates))
# Annual seasonality
seasonal_annual = 15 * np.sin(2 * np.pi * np.arange(len(dates)) / 365)
# Weekly seasonality
seasonal_weekly = 5 * np.sin(2 * np.pi * np.arange(len(dates)) / 7)
noise = np.random.normal(0, 2, len(dates))

sales = trend + seasonal_annual + seasonal_weekly + noise
df = pd.DataFrame({'Date': dates, 'Sales': sales})

# Plot with seasonal highlighting
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df['Date'], df['Sales'], linewidth=1.5, color='steelblue', label='Daily Sales')

# Highlight summer months
for year in [2020, 2021, 2022]:
    summer_start = pd.Timestamp(f'{year}-06-01')
    summer_end = pd.Timestamp(f'{year}-08-31')
    ax.axvspan(summer_start, summer_end, alpha=0.2, color='yellow', 
               label='Summer Season' if year == 2020 else '')

ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Sales', fontsize=12)
ax.set_title('Sales with Seasonal Highlighting (Summer)', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Method 2: Seasonal Subseries Plot**
```python
# Extract month from dates
df_monthly = df.copy()
df_monthly['Month'] = df_monthly['Date'].dt.month
df_monthly['Year'] = df_monthly['Date'].dt.year

# Average by month across years
monthly_avg = df_monthly.groupby('Month')['Sales'].mean()

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(range(1, 13), monthly_avg.values, color='steelblue', alpha=0.7)
ax.set_xticks(range(1, 13))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Average Sales', fontsize=12)
ax.set_title('Seasonal Pattern: Average Sales by Month', fontsize=14, fontweight='bold')
ax.grid(True, axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
```

**Method 3: Year-over-Year Seasonal Comparison**
```python
# Compare same months across years
fig, ax = plt.subplots(figsize=(12, 6))

for year in df_monthly['Year'].unique():
    year_data = df_monthly[df_monthly['Year'] == year]
    monthly = year_data.groupby('Month')['Sales'].mean()
    ax.plot(range(1, 13), monthly.values, marker='o', linewidth=2, label=str(year))

ax.set_xticks(range(1, 13))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Sales', fontsize=12)
ax.set_title('Year-over-Year Seasonal Patterns', fontsize=14, fontweight='bold')
ax.legend(title='Year')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Method 4: Box Plot by Season**
```python
import seaborn as sns

df_monthly['Season'] = df_monthly['Month'].map({
    12: 'Winter', 1: 'Winter', 2: 'Winter',
    3: 'Spring', 4: 'Spring', 5: 'Spring',
    6: 'Summer', 7: 'Summer', 8: 'Summer',
    9: 'Fall', 10: 'Fall', 11: 'Fall'
})

fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df_monthly, x='Season', y='Sales', 
            order=['Winter', 'Spring', 'Summer', 'Fall'],
            palette='Set2', ax=ax)
ax.set_title('Sales Distribution by Season', fontsize=14, fontweight='bold')
ax.set_ylabel('Sales', fontsize=12)
ax.set_xlabel('Season', fontsize=12)
plt.tight_layout()
plt.show()
```

**Detecting Seasonality:**

**1. Visual Inspection**
- Repeating peaks and valleys at regular intervals
- Pattern recurs at same time each period

**2. Autocorrelation Function (ACF)**
```python
from statsmodels.graphics.tsaplots import plot_acf

fig, ax = plt.subplots(figsize=(12, 5))
plot_acf(df['Sales'], lags=100, ax=ax)
ax.set_title('ACF Plot - Look for Regular Spikes', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# Significant spikes at lag 7, 14, 21... indicate weekly seasonality
# Significant spikes at lag 30, 60, 90... indicate monthly seasonality
```

**3. Statistical Tests**
```python
# Seasonal decomposition to extract seasonal component
from statsmodels.tsa.seasonal import seasonal_decompose

decomp = seasonal_decompose(df.set_index('Date')['Sales'], 
                             model='additive', period=7)

# Check if seasonal component is significant
seasonal_strength = 1 - (decomp.resid.var() / (decomp.seasonal + decomp.resid).var())
print(f'Seasonal strength: {seasonal_strength:.3f}')
print('Strong seasonality' if seasonal_strength > 0.6 else 'Weak seasonality')
```

**Best Practices for Visualizing Seasonality:**

✅ **DO:**
- Use year-over-year comparisons to show consistency
- Highlight seasonal periods with shading
- Show multiple seasonal cycles for pattern verification
- Use box plots to show variation within seasons
- Annotate known seasonal events (holidays, etc.)

❌ **DON'T:**
- Show just one seasonal cycle (could be coincidence)
- Ignore the trend when analyzing seasonality
- Use too short a time period (need multiple cycles)
- Confuse weekly/monthly/annual seasonality

**Key Insight**: Seasonality is your friend in forecasting! If you understand the seasonal pattern, you can predict future values with high confidence during regular periods.

---

## Types of Seasonality

**Not all seasonal patterns are created equal**

Understanding whether your seasonality is **additive** or **multiplicative** affects:
- How you model the data
- Which decomposition method to use
- How you visualize patterns
- Forecast accuracy

**1. Additive Seasonality**

**Definition**: Seasonal fluctuations have **constant amplitude** regardless of the overall level

**Mathematical form:**
```
Y(t) = Trend + Seasonal + Error
```

**Characteristics:**
- ✅ Seasonal swings are the same size over time
- ✅ Seasonal component is constant
- ✅ Use when: Seasonal variation doesn't grow with trend

**Example: Temperature**
```python
# Generate additive seasonal pattern
dates = pd.date_range('2018-01-01', periods=365*3, freq='D')
trend_add = np.linspace(15, 17, len(dates))  # Slight warming trend
seasonal_add = 8 * np.sin(2 * np.pi * np.arange(len(dates)) / 365)  # ±8 degrees yearly
noise_add = np.random.normal(0, 2, len(dates))

temp_data = trend_add + seasonal_add + noise_add
df_add = pd.DataFrame({'Date': dates, 'Temperature': temp_data})

# Visualize
fig, axes = plt.subplots(2, 1, figsize=(14, 10))

# Original data
axes[0].plot(df_add['Date'], df_add['Temperature'], linewidth=1, alpha=0.7)
axes[0].set_ylabel('Temperature (°C)', fontsize=11)
axes[0].set_title('Additive Seasonality: Constant Amplitude Over Time', 
                   fontsize=13, fontweight='bold')
axes[0].grid(True, alpha=0.3)

# Highlight seasonal component (constant size)
year_2019 = df_add[(df_add['Date'] >= '2019-01-01') & (df_add['Date'] < '2020-01-01')]
year_2020 = df_add[(df_add['Date'] >= '2020-01-01') & (df_add['Date'] < '2021-01-01')]

axes[1].plot(range(365), year_2019['Temperature'].values, label='2019', linewidth=2)
axes[1].plot(range(365), year_2020['Temperature'].values, label='2020', linewidth=2)
axes[1].set_xlabel('Day of Year', fontsize=11)
axes[1].set_ylabel('Temperature (°C)', fontsize=11)
axes[1].set_title('Seasonal Pattern Comparison: Similar Amplitude', fontsize=13, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**When to use additive model:**
- Temperature data
- Physical measurements
- When variance appears constant
- Data doesn't grow/shrink over time

---

**2. Multiplicative Seasonality**

**Definition**: Seasonal fluctuations **grow or shrink** with the overall level

**Mathematical form:**
```
Y(t) = Trend × Seasonal × Error
```

**Characteristics:**
- ✅ Seasonal swings get larger as trend increases
- ✅ Percentage change is constant
- ✅ Use when: Seasonal variation scales with the data level

**Example: Retail Sales**
```python
# Generate multiplicative seasonal pattern
trend_mult = np.exp(np.linspace(4, 5, len(dates)))  # Exponential growth
seasonal_mult = 1 + 0.3 * np.sin(2 * np.pi * np.arange(len(dates)) / 365)  # ±30% yearly
noise_mult = np.random.normal(1, 0.05, len(dates))

sales_data = trend_mult * seasonal_mult * noise_mult
df_mult = pd.DataFrame({'Date': dates, 'Sales': sales_data})

# Visualize
fig, axes = plt.subplots(2, 1, figsize=(14, 10))

# Original data
axes[0].plot(df_mult['Date'], df_mult['Sales'], linewidth=1, alpha=0.7)
axes[0].set_ylabel('Sales ($)', fontsize=11)
axes[0].set_title('Multiplicative Seasonality: Growing Amplitude Over Time', 
                   fontsize=13, fontweight='bold')
axes[0].grid(True, alpha=0.3)

# Highlight growing seasonal swings
year_2018 = df_mult[(df_mult['Date'] >= '2018-01-01') & (df_mult['Date'] < '2019-01-01')]
year_2020 = df_mult[(df_mult['Date'] >= '2020-01-01') & (df_mult['Date'] < '2021-01-01')]

axes[1].plot(range(365), year_2018['Sales'].values, label='2018 (smaller swings)', linewidth=2)
axes[1].plot(range(365), year_2020['Sales'].values, label='2020 (larger swings)', linewidth=2)
axes[1].set_xlabel('Day of Year', fontsize=11)
axes[1].set_ylabel('Sales ($)', fontsize=11)
axes[1].set_title('Seasonal Pattern Comparison: Amplitude Grows with Level', 
                   fontsize=13, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**When to use multiplicative model:**
- Sales/revenue data
- Economic indicators
- Anything with percentage-based seasonality
- When variance increases with level

**How to Decide: Additive vs. Multiplicative?**

**Visual Test:**
```python
# Plot the data
# If seasonal swings look constant → Additive
# If seasonal swings grow with trend → Multiplicative
```

**Statistical Test:**
```python
# Plot seasonal component variance over time
# If variance is stable → Additive
# If variance increases → Multiplicative

# Or use log transformation:
# If log(data) makes seasonality constant → Multiplicative (use log)
```

**Transformation Tip:**
```python
# Convert multiplicative to additive using log
df['Log_Sales'] = np.log(df['Sales'])
# Now you can use additive methods
# Transform back: np.exp(result) to get original scale
```

**Summary:**

| Type | When | Visual Clue | Transform |
|------|------|-------------|-----------|
| **Additive** | Constant amplitude | Seasonal swings same size | Use as-is |
| **Multiplicative** | Growing amplitude | Swings grow with trend | Take log first |

---

## Cyclic Patterns

**Cycles are the most challenging pattern to identify and forecast**

**What are Cycles?**

**Cycles** are longer-term fluctuations that are **NOT** fixed in frequency or amplitude. They differ from seasonality:

| Feature | Seasonality | Cycles |
|---------|-------------|--------|
| **Frequency** | Fixed (weekly, monthly, yearly) | Variable (can change) |
| **Duration** | < 1 year typically | Multi-year (2-10+ years) |
| **Amplitude** | Relatively consistent | Variable |
| **Predictability** | High (repeats regularly) | Low (irregular) |
| **Causes** | Calendar, weather, habits | Economic, political, market forces |

**Common Cyclic Patterns:**

**Economic Cycles:**
- **Business cycles**: Expansion → Peak → Recession → Trough (4-10 years)
- **Credit cycles**: Lending expansion/contraction
- **Inventory cycles**: Buildup and liquidation
- **Investment cycles**: Capital expenditure waves

**Market Cycles:**
- **Commodity supercycles**: Oil, metals, agricultural products
- **Real estate cycles**: Housing booms and busts
- **Technology cycles**: Hype, adoption, maturity, obsolescence
- **Fashion cycles**: Style trends come and go

**Political/Social Cycles:**
- **Election cycles**: 2-4 year political cycles affecting policy
- **Demographic cycles**: Baby booms, generational shifts
- **Cultural trends**: Music, entertainment preferences

**Visualizing Cycles:**

**Method 1: Long-Term View**
```python
# Need long time series to see cycles
dates_long = pd.date_range('1990-01-01', periods=365*30, freq='D')
trend_long = np.linspace(100, 300, len(dates_long))

# Add cyclical component (irregular, ~7-year cycle)
cycle_freq = 2 * np.pi / (365 * 7)  # 7-year cycle
cycle_var = 2 * np.pi / (365 * 9)   # Slightly irregular
cyclical = 30 * np.sin(cycle_freq * np.arange(len(dates_long))) * \
           (1 + 0.3 * np.sin(cycle_var * np.arange(len(dates_long))))

noise_long = np.random.normal(0, 10, len(dates_long))
gdp_data = trend_long + cyclical + noise_long

df_cycle = pd.DataFrame({'Date': dates_long, 'GDP': gdp_data})

# Plot with cycle highlighting
fig, ax = plt.subplots(figsize=(16, 6))
ax.plot(df_cycle['Date'], df_cycle['GDP'], linewidth=1, alpha=0.6, label='GDP')

# Add moving average to show trend + cycle
df_cycle['MA_365'] = df_cycle['GDP'].rolling(window=365).mean()
ax.plot(df_cycle['Date'], df_cycle['MA_365'], linewidth=3, color='red', 
        label='1-Year Moving Average (Trend + Cycle)')

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('GDP Index', fontsize=12)
ax.set_title('Economic Cycles: Irregular Multi-Year Fluctuations', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)

# Annotate recessions
recession_periods = [
    ('2001-03-01', '2001-11-01', 'Dot-com Recession'),
    ('2007-12-01', '2009-06-01', 'Great Recession'),
]

for start, end, label in recession_periods:
    start_date = pd.Timestamp(start)
    end_date = pd.Timestamp(end)
    if start_date >= df_cycle['Date'].min() and end_date <= df_cycle['Date'].max():
        ax.axvspan(start_date, end_date, alpha=0.3, color='red', label=label)
        ax.text(start_date + (end_date - start_date)/2, df_cycle['GDP'].max() * 0.95,
                label, ha='center', fontsize=9, fontweight='bold', color='darkred')

plt.tight_layout()
plt.show()
```

**Method 2: Detrended to Emphasize Cycles**
```python
# Remove trend to see cyclical pattern more clearly
from scipy.signal import detrend

df_cycle['Detrended'] = detrend(df_cycle['GDP'].values)

fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df_cycle['Date'], df_cycle['Detrended'], linewidth=1, color='steelblue')
ax.axhline(0, color='black', linewidth=1, linestyle='--', alpha=0.5)
ax.fill_between(df_cycle['Date'], 0, df_cycle['Detrended'], 
                 where=(df_cycle['Detrended'] > 0), alpha=0.3, color='green', label='Expansion')
ax.fill_between(df_cycle['Date'], 0, df_cycle['Detrended'], 
                 where=(df_cycle['Detrended'] <= 0), alpha=0.3, color='red', label='Contraction')

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Detrended GDP', fontsize=12)
ax.set_title('Economic Cycles (Detrended)', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Challenges with Cycles:**

❌ **Hard to forecast** - No fixed frequency
❌ **Need long data** - Require decades to see multiple cycles
❌ **Confounded with trend** - Difficult to separate
❌ **Irregular amplitude** - Varies in strength

**Strategies:**

✅ Use very long time series (10+ years minimum)
✅ Apply detrending to isolate cyclical component
✅ Use spectral analysis to identify dominant frequencies
✅ Combine with external indicators (economic data, etc.)
✅ Show uncertainty in cycle-based forecasts

**Key Distinction:**
- **Seasonality**: Predictable, fixed (e.g., summer sales spike every June)
- **Cycles**: Unpredictable, variable (e.g., recession happens every 7-10 years, but timing varies)

---

## Time Series Decomposition

**Decomposition separates observed data into interpretable components**

**What is Decomposition?**

**Time series decomposition** is the process of splitting observed data into:
1. **Trend** (T) - Long-term direction
2. **Seasonal** (S) - Fixed-period patterns
3. **Residual** (R) - Everything else (noise, irregular events)

**Why Decompose?**

**Benefits:**
- ✅ **Understand drivers** - See what components dominate
- ✅ **Better forecasting** - Model each component separately
- ✅ **Anomaly detection** - Large residuals indicate unusual events
- ✅ **Seasonal adjustment** - Remove seasonality to see underlying trend
- ✅ **Communication** - Explain patterns to stakeholders

**The Two Models:**

**Additive Decomposition:**
```
Y(t) = T(t) + S(t) + R(t)

Observed = Trend + Seasonal + Residual
```
Use when seasonal variation is **constant**

**Multiplicative Decomposition:**
```
Y(t) = T(t) × S(t) × R(t)

Observed = Trend × Seasonal × Residual
```
Use when seasonal variation **scales with trend**

**Can convert multiplicative to additive:**
```
log(Y(t)) = log(T(t)) + log(S(t)) + log(R(t))
```

**Example: Complete Decomposition**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Generate realistic data
np.random.seed(42)
dates = pd.date_range('2020-01-01', periods=365*3, freq='D')

# Components
trend = np.linspace(1000, 1500, len(dates))
seasonal = 200 * np.sin(2 * np.pi * np.arange(len(dates)) / 365)
noise = np.random.normal(0, 30, len(dates))

observed = trend + seasonal + noise
df = pd.DataFrame({'Date': dates, 'Sales': observed})
df = df.set_index('Date')

# Perform decomposition
decomposition = seasonal_decompose(df['Sales'], model='additive', period=365)

# Plot all components
fig, axes = plt.subplots(4, 1, figsize=(14, 12))

# Observed
axes[0].plot(df.index, df['Sales'], linewidth=1, color='black')
axes[0].set_ylabel('Sales', fontsize=11)
axes[0].set_title('Observed Time Series', fontsize=12, fontweight='bold')
axes[0].grid(True, alpha=0.3)

# Trend
axes[1].plot(decomposition.trend.index, decomposition.trend, linewidth=2, color='blue')
axes[1].set_ylabel('Trend', fontsize=11)
axes[1].set_title('Trend Component (Long-term Direction)', fontsize=12, fontweight='bold')
axes[1].grid(True, alpha=0.3)

# Seasonal
axes[2].plot(decomposition.seasonal.index, decomposition.seasonal, linewidth=1, color='green')
axes[2].set_ylabel('Seasonal', fontsize=11)
axes[2].set_title('Seasonal Component (Repeating Pattern)', fontsize=12, fontweight='bold')
axes[2].grid(True, alpha=0.3)

# Residual
axes[3].plot(decomposition.resid.index, decomposition.resid, linewidth=1, color='red', alpha=0.7)
axes[3].axhline(0, color='black', linestyle='--', linewidth=1)
axes[3].set_ylabel('Residual', fontsize=11)
axes[3].set_xlabel('Date', fontsize=11)
axes[3].set_title('Residual Component (Noise + Irregular Events)', fontsize=12, fontweight='bold')
axes[3].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Print component statistics
print(f'Trend Range: {decomposition.trend.min():.1f} to {decomposition.trend.max():.1f}')
print(f'Seasonal Range: {decomposition.seasonal.min():.1f} to {decomposition.seasonal.max():.1f}')
print(f'Residual Std: {decomposition.resid.std():.1f}')
```

**Interpreting Decomposition:**

**Trend Component:**
- Shows long-term growth or decline
- Remove noise and seasonality
- Use for strategic planning

**Seasonal Component:**
- Shows repeating pattern
- Same for each cycle
- Use for operational planning (staffing, inventory)

**Residual Component:**
- Should look like random noise
- Large spikes indicate anomalies or events
- Use for quality control and anomaly detection

**Quality Checks:**

```python
# Check if residuals are random (should be!)
from statsmodels.graphics.tsaplots import plot_acf

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Residual distribution (should be normal)
axes[0].hist(decomposition.resid.dropna(), bins=30, edgecolor='black', alpha=0.7)
axes[0].set_title('Residual Distribution (Should be Normal)', fontweight='bold')
axes[0].set_xlabel('Residual Value')
axes[0].set_ylabel('Frequency')

# Residual ACF (should show no pattern)
plot_acf(decomposition.resid.dropna(), lags=40, ax=axes[1])
axes[1].set_title('Residual ACF (Should be Random)', fontweight='bold')

plt.tight_layout()
plt.show()
```

**Best Practices:**

✅ **DO:**
- Choose additive vs multiplicative based on data behavior
- Check that residuals look random (no leftover patterns)
- Use appropriate seasonal period (7 for weekly, 12 for monthly, etc.)
- Plot all components to understand each contribution

❌ **DON'T:**
- Use wrong seasonal period (e.g., 12 for daily data with weekly pattern)
- Ignore residual patterns (suggests poor decomposition)
- Apply to very short time series (need at least 2 seasonal cycles)
- Forget to check model assumptions

---

## Classical Decomposition Method

**The classical method is the simplest approach to time series decomposition**

**What is Classical Decomposition?**

**Classical decomposition** (also called "moving average decomposition") splits a time series into trend, seasonal, and residual components using moving averages. It's:
- Simple and intuitive
- Fast to compute
- Good for initial exploration
- Available in most software

**How It Works:**

**Step 1: Extract Trend (T)**
- Use centered moving average with window = seasonal period
- Smooths out seasonal variations
- Leaves underlying trend

**Step 2: Extract Seasonality (S)**
- Subtract trend from observed (additive) or divide (multiplicative)
- Average the detrended values for each season
- Creates seasonal indices

**Step 3: Calculate Residuals (R)**
- Observed minus Trend minus Seasonal (additive)
- Or Observed / (Trend × Seasonal) (multiplicative)

**Python Implementation:**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Generate example data
np.random.seed(42)
dates = pd.date_range('2020-01-01', periods=36, freq='M')
trend = np.linspace(100, 150, 36)
seasonal = 10 * np.sin(2 * np.pi * np.arange(36) / 12)
noise = np.random.normal(0, 3, 36)

data = trend + seasonal + noise
df = pd.DataFrame({'Date': dates, 'Sales': data})
df = df.set_index('Date')

# Perform classical decomposition
result = seasonal_decompose(df['Sales'], model='additive', period=12)

# Access components
print("Components available:")
print(f"  - result.observed: Original data")
print(f"  - result.trend: Trend component")
print(f"  - result.seasonal: Seasonal component")
print(f"  - result.resid: Residual component")

# Plot
result.plot()
plt.tight_layout()
plt.show()
```

**Parameters:**

```python
seasonal_decompose(
    x,                    # Time series data (must be Series with DatetimeIndex)
    model='additive',     # 'additive' or 'multiplicative'
    period=None,          # Seasonal period (e.g., 12 for monthly, 7 for daily with weekly pattern)
    filt=None,            # Custom filter for trend (default: centered moving average)
    two_sided=True,       # Use two-sided moving average
    extrapolate_trend=0   # How to handle NaN at ends
)
```

**Additive vs. Multiplicative:**

```python
# Additive
decomp_add = seasonal_decompose(df['Sales'], model='additive', period=12)

# Multiplicative
decomp_mult = seasonal_decompose(df['Sales'], model='multiplicative', period=12)

# Compare
fig, axes = plt.subplots(2, 4, figsize=(18, 10))

# Additive
axes[0,0].plot(decomp_add.observed)
axes[0,0].set_title('Observed (Add)', fontweight='bold')
axes[0,1].plot(decomp_add.trend)
axes[0,1].set_title('Trend (Add)', fontweight='bold')
axes[0,2].plot(decomp_add.seasonal)
axes[0,2].set_title('Seasonal (Add)', fontweight='bold')
axes[0,3].plot(decomp_add.resid)
axes[0,3].set_title('Residual (Add)', fontweight='bold')

# Multiplicative
axes[1,0].plot(decomp_mult.observed)
axes[1,0].set_title('Observed (Mult)', fontweight='bold')
axes[1,1].plot(decomp_mult.trend)
axes[1,1].set_title('Trend (Mult)', fontweight='bold')
axes[1,2].plot(decomp_mult.seasonal)
axes[1,2].set_title('Seasonal (Mult)', fontweight='bold')
axes[1,3].plot(decomp_mult.resid)
axes[1,3].set_title('Residual (Mult)', fontweight='bold')

plt.tight_layout()
plt.show()
```

**Advantages:**
- ✅ Simple and fast
- ✅ Easy to understand
- ✅ Works well for stable patterns
- ✅ Good for quick exploration

**Limitations:**
- ❌ Assumes seasonal pattern is perfectly consistent
- ❌ Cannot handle multiple seasonal periods
- ❌ Produces NaN values at beginning/end
- ❌ Not robust to outliers
- ❌ Seasonal component doesn't evolve over time

**When to Use:**
- Quick exploratory analysis
- Stable, simple seasonal patterns
- Educational demonstrations
- When you need fast results

**Better Alternative:** STL decomposition (next slide) for more robust analysis

---

## STL Decomposition

**STL (Seasonal and Trend decomposition using Loess) is more robust and flexible**

**What is STL?**

**STL** is an advanced decomposition method that:
- Handles **changing seasonality** (patterns can evolve)
- **Robust to outliers** (doesn't let extreme values distort components)
- Works with **any seasonal period**
- Produces **no NaN values**
- More computationally intensive but worth it

**Developed by:** Cleveland et al. (1990)

**Key Advantages over Classical:**

| Feature | Classical | STL |
|---------|-----------|-----|
| **Seasonal evolution** | Fixed pattern | Can change over time |
| **Outlier handling** | Sensitive | Robust |
| **Missing values** | Creates NaNs at ends | Handles better |
| **Multiple seasonality** | No | Yes (with extension) |
| **Speed** | Fast | Slower |
| **Flexibility** | Limited | High (many parameters) |

**Python Implementation:**

```python
from statsmodels.tsa.seasonal import STL
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate data with evolving seasonality
np.random.seed(42)
dates = pd.date_range('2018-01-01', periods=365*4, freq='D')
trend = np.linspace(100, 200, len(dates))

# Seasonal component that grows over time
time_factor = np.linspace(1, 2, len(dates))
seasonal = time_factor * 15 * np.sin(2 * np.pi * np.arange(len(dates)) / 365)

# Add some outliers
noise = np.random.normal(0, 5, len(dates))
outliers = np.zeros(len(dates))
outlier_indices = np.random.choice(len(dates), size=10, replace=False)
outliers[outlier_indices] = np.random.choice([-50, 50], size=10)

data = trend + seasonal + noise + outliers
df = pd.DataFrame({'Sales': data}, index=dates)

# Perform STL decomposition
stl = STL(df['Sales'], 
          seasonal=13,      # Length of seasonal smoother (must be odd)
          trend=None,       # Length of trend smoother (default: next odd number > period)
          robust=True)      # Use robust fitting (less sensitive to outliers)

result = stl.fit()

# Plot
fig, axes = plt.subplots(4, 1, figsize=(14, 12))

# Observed
axes[0].plot(result.observed, linewidth=1, color='black', label='Observed')
axes[0].scatter(df.index[outlier_indices], data[outlier_indices], 
                color='red', s=50, zorder=5, label='Outliers')
axes[0].set_ylabel('Sales', fontsize=11)
axes[0].set_title('Observed Data (with outliers)', fontsize=12, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Trend
axes[1].plot(result.trend, linewidth=2, color='blue')
axes[1].set_ylabel('Trend', fontsize=11)
axes[1].set_title('Trend Component (Robust to Outliers)', fontsize=12, fontweight='bold')
axes[1].grid(True, alpha=0.3)

# Seasonal
axes[2].plot(result.seasonal, linewidth=1, color='green')
axes[2].set_ylabel('Seasonal', fontsize=11)
axes[2].set_title('Seasonal Component (Can Evolve Over Time)', fontsize=12, fontweight='bold')
axes[2].grid(True, alpha=0.3)

# Residual
axes[3].plot(result.resid, linewidth=1, color='red', alpha=0.7)
axes[3].scatter(df.index[outlier_indices], result.resid[outlier_indices], 
                color='darkred', s=50, zorder=5, label='Outlier Residuals')
axes[3].axhline(0, color='black', linestyle='--', linewidth=1)
axes[3].set_ylabel('Residual', fontsize=11)
axes[3].set_xlabel('Date', fontsize=11)
axes[3].set_title('Residual Component (Outliers Isolated Here)', fontsize=12, fontweight='bold')
axes[3].legend()
axes[3].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Component statistics
print(f"Trend range: {result.trend.min():.1f} to {result.trend.max():.1f}")
print(f"Seasonal range: {result.seasonal.min():.1f} to {result.seasonal.max():.1f}")
print(f"Residual std dev: {result.resid.std():.1f}")
print(f"Strength of trend: {1 - result.resid.var()/result.trend.var():.3f}")
print(f"Strength of seasonality: {1 - result.resid.var()/result.seasonal.var():.3f}")
```

**Key Parameters:**

```python
STL(
    endog,              # Time series to decompose
    period,             # Seasonal period (e.g., 12 for monthly data with yearly pattern)
    seasonal=7,         # Seasonal smoother length (odd number, larger = smoother)
    trend=None,         # Trend smoother length (None = auto-calculate)
    robust=False,       # Use robust fitting? (True = less sensitive to outliers)
    seasonal_deg=1,     # Polynomial degree for seasonal smoother (0 or 1)
    trend_deg=1,        # Polynomial degree for trend smoother (0 or 1)
)
```

**Tuning Parameters:**

**Seasonal smoother (`seasonal`):**
- Larger value → smoother seasonal pattern
- Smaller value → captures more variation
- Must be odd number
- Default: 7
- Try: 7, 13, 21, 35 depending on data

**Robust fitting (`robust=True`):**
- Downweights outliers
- Prevents extreme values from distorting components
- Slightly slower
- **Recommended for real-world data**

**Example: Comparing Robust vs Non-Robust**
```python
# Non-robust
stl_regular = STL(df['Sales'], seasonal=13, robust=False)
result_regular = stl_regular.fit()

# Robust
stl_robust = STL(df['Sales'], seasonal=13, robust=True)
result_robust = stl_robust.fit()

# Compare trends
fig, axes = plt.subplots(2, 1, figsize=(14, 8))

axes[0].plot(result_regular.trend, linewidth=2, label='Non-Robust Trend')
axes[0].set_title('Non-Robust: Trend Affected by Outliers', fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].plot(result_robust.trend, linewidth=2, color='red', label='Robust Trend')
axes[1].set_title('Robust: Trend Ignores Outliers', fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**When to Use STL:**
- ✅ Data with outliers
- ✅ Evolving seasonal patterns
- ✅ Production-quality decomposition
- ✅ When you need reliable trend estimates

**When Classical is Enough:**
- Quick exploration
- Very clean data
- Perfectly stable seasonality
- Educational examples

**Pro Tip:** Use `robust=True` by default for real-world data!

---

## Visualizing Decomposition Results

**Effective visualization of decomposition components tells the full story**

**Standard 4-Panel Layout (Most Common)**

```python
from statsmodels.tsa.seasonal import STL
import matplotlib.pyplot as plt

# Perform decomposition
stl = STL(df['Sales'], seasonal=13, robust=True)
result = stl.fit()

# Create 4-panel plot
fig, axes = plt.subplots(4, 1, figsize=(14, 12), sharex=True)

# Panel 1: Observed
axes[0].plot(result.observed, linewidth=1.5, color='black')
axes[0].set_ylabel('Observed', fontsize=11, fontweight='bold')
axes[0].set_title('Time Series Decomposition', fontsize=14, fontweight='bold')
axes[0].grid(True, alpha=0.3)

# Panel 2: Trend
axes[1].plot(result.trend, linewidth=2, color='#2E86AB')
axes[1].set_ylabel('Trend', fontsize=11, fontweight='bold')
axes[1].grid(True, alpha=0.3)

# Panel 3: Seasonal
axes[2].plot(result.seasonal, linewidth=1, color='#27AE60')
axes[2].set_ylabel('Seasonal', fontsize=11, fontweight='bold')
axes[2].axhline(0, color='black', linestyle='--', linewidth=0.8, alpha=0.5)
axes[2].grid(True, alpha=0.3)

# Panel 4: Residual
axes[3].plot(result.resid, linewidth=1, color='#E74C3C', alpha=0.7)
axes[3].axhline(0, color='black', linestyle='--', linewidth=0.8, alpha=0.5)
axes[3].set_ylabel('Residual', fontsize=11, fontweight='bold')
axes[3].set_xlabel('Date', fontsize=12)
axes[3].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('decomposition_4panel.png', dpi=150, bbox_inches='tight')
plt.show()
```

**Alternative: Side-by-Side Comparison**

```python
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Trend
axes[0].plot(result.trend, linewidth=2, color='blue')
axes[0].set_title('Trend Component', fontsize=13, fontweight='bold')
axes[0].set_ylabel('Value')
axes[0].set_xlabel('Date')
axes[0].grid(True, alpha=0.3)

# Seasonal (show one year repeated)
seasonal_year = result.seasonal[:365]
axes[1].plot(range(365), seasonal_year, linewidth=2, color='green')
axes[1].set_title('Seasonal Component (One Year)', fontsize=13, fontweight='bold')
axes[1].set_ylabel('Seasonal Effect')
axes[1].set_xlabel('Day of Year')
axes[1].grid(True, alpha=0.3)

# Residual histogram
axes[2].hist(result.resid.dropna(), bins=30, edgecolor='black', alpha=0.7, color='red')
axes[2].set_title('Residual Distribution', fontsize=13, fontweight='bold')
axes[2].set_ylabel('Frequency')
axes[2].set_xlabel('Residual Value')
axes[2].grid(True, axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
```

**Advanced: Interactive Decomposition Dashboard**

```python
# Reconstruction to verify decomposition
reconstructed = result.trend + result.seasonal

fig, axes = plt.subplots(2, 1, figsize=(14, 8))

# Original vs Reconstructed
axes[0].plot(result.observed, linewidth=1.5, alpha=0.7, label='Original', color='black')
axes[0].plot(reconstructed, linewidth=1.5, alpha=0.7, label='Trend + Seasonal', 
             color='red', linestyle='--')
axes[0].set_ylabel('Sales', fontsize=11)
axes[0].set_title('Original vs. Reconstructed (without residuals)', fontsize=13, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Residual over time with control limits
residual_std = result.resid.std()
axes[1].plot(result.resid, linewidth=1, color='red', alpha=0.7, label='Residuals')
axes[1].axhline(0, color='black', linestyle='-', linewidth=1)
axes[1].axhline(2*residual_std, color='orange', linestyle='--', linewidth=1, label='±2σ')
axes[1].axhline(-2*residual_std, color='orange', linestyle='--', linewidth=1)
axes[1].axhline(3*residual_std, color='red', linestyle='--', linewidth=1, label='±3σ')
axes[1].axhline(-3*residual_std, color='red', linestyle='--', linewidth=1)
axes[1].set_ylabel('Residual', fontsize=11)
axes[1].set_xlabel('Date', fontsize=12)
axes[1].set_title('Residuals with Control Limits (Outliers Beyond ±3σ)', fontsize=13, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# Highlight outliers
outlier_mask = np.abs(result.resid) > 3 * residual_std
if outlier_mask.sum() > 0:
    axes[1].scatter(result.resid[outlier_mask].index, 
                   result.resid[outlier_mask],
                   color='darkred', s=100, zorder=5, label=f'{outlier_mask.sum()} Outliers')

plt.tight_layout()
plt.show()
```

**Component Strength Metrics:**

```python
# Calculate strength of each component
def calculate_strength(decomp_result):
    """Calculate strength of trend and seasonality"""
    
    # Strength of trend
    trend_strength = max(0, 1 - decomp_result.resid.var() / 
                        (decomp_result.trend + decomp_result.resid).var())
    
    # Strength of seasonality
    seasonal_strength = max(0, 1 - decomp_result.resid.var() / 
                           (decomp_result.seasonal + decomp_result.resid).var())
    
    return trend_strength, seasonal_strength

trend_str, seasonal_str = calculate_strength(result)

print(f"Trend Strength: {trend_str:.3f} ({'Strong' if trend_str > 0.6 else 'Weak'})")
print(f"Seasonal Strength: {seasonal_str:.3f} ({'Strong' if seasonal_str > 0.6 else 'Weak'})")

# Visualize component contributions
fig, ax = plt.subplots(figsize=(10, 6))

components = ['Trend', 'Seasonal', 'Residual']
strengths = [
    trend_str,
    seasonal_str,
    1 - trend_str - seasonal_str  # Rough approximation for residual importance
]

colors = ['#2E86AB', '#27AE60', '#E74C3C']
ax.bar(components, strengths, color=colors, alpha=0.7, edgecolor='black', linewidth=2)
ax.set_ylabel('Component Strength', fontsize=12)
ax.set_title('Decomposition: Component Strengths', fontsize=14, fontweight='bold')
ax.set_ylim(0, 1)
ax.grid(True, axis='y', alpha=0.3)

for i, (comp, strength) in enumerate(zip(components, strengths)):
    ax.text(i, strength + 0.02, f'{strength:.2f}', ha='center', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.show()
```

**Best Practices for Decomposition Visualization:**

✅ **DO:**
- Show all four components (observed, trend, seasonal, residual)
- Use consistent x-axis across panels for easy comparison
- Add zero reference line for seasonal and residual
- Check residual distribution (should be random)
- Calculate and report component strengths

❌ **DON'T:**
- Plot only one or two components (incomplete story)
- Use different time scales across panels
- Ignore large residual spikes (could be important events)
- Forget to validate that residuals are random

**Exporting Components for Further Analysis:**

```python
# Save components for use in forecasting or modeling
decomp_df = pd.DataFrame({
    'Observed': result.observed,
    'Trend': result.trend,
    'Seasonal': result.seasonal,
    'Residual': result.resid
})

# Save to CSV
decomp_df.to_csv('decomposition_components.csv')

# Use seasonally adjusted data (trend + residual)
df['Seasonally_Adjusted'] = result.trend + result.resid

print("Decomposition components exported and ready for further analysis")
```

---

## Moving Averages

**Moving averages are the simplest and most widely used smoothing technique**

**What are Moving Averages?**

A **moving average** (MA) smooths a time series by averaging values within a sliding window. It:
- Reduces short-term noise
- Reveals underlying trends
- Simple to calculate and interpret
- Forms the basis of many forecasting methods

**Types of Moving Averages:**

**1. Simple Moving Average (SMA)**

**Definition**: Unweighted average of the last n points

```python
MA(t) = (Y(t) + Y(t-1) + ... + Y(t-n+1)) / n
```

**Characteristics:**
- All points in window weighted equally
- Lags the actual data
- Larger window = smoother but more lag

**Example:**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate noisy data
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=180, freq='D')
trend = np.linspace(100, 120, 180)
noise = np.random.normal(0, 8, 180)
data = trend + noise

df = pd.DataFrame({'Date': dates, 'Value': data})

# Calculate moving averages with different windows
df['MA_7'] = df['Value'].rolling(window=7, center=False).mean()
df['MA_30'] = df['Value'].rolling(window=30, center=False).mean()
df['MA_60'] = df['Value'].rolling(window=60, center=False).mean()

# Plot
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df['Date'], df['Value'], linewidth=1, alpha=0.3, color='gray', label='Raw Data')
ax.plot(df['Date'], df['MA_7'], linewidth=2, color='blue', label='7-Day MA')
ax.plot(df['Date'], df['MA_30'], linewidth=2, color='green', label='30-Day MA')
ax.plot(df['Date'], df['MA_60'], linewidth=2.5, color='red', label='60-Day MA')

ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Value', fontsize=12)
ax.set_title('Moving Averages: Different Window Sizes', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Choosing Window Size:**

| Window | Effect | Use Case |
|--------|--------|----------|
| **Small (3-7)** | Less smoothing, follows data closely | Short-term trends, detecting recent changes |
| **Medium (14-30)** | Balanced, removes weekly noise | Monthly patterns, medium-term trends |
| **Large (60-365)** | Heavy smoothing, very stable | Long-term trends, annual patterns |

**2. Weighted Moving Average (WMA)**

Give more importance to recent data:

```python
# Linearly weighted moving average
def wma(series, window):
    weights = np.arange(1, window+1)
    return series.rolling(window).apply(
        lambda x: np.dot(x, weights) / weights.sum(), raw=True
    )

df['WMA_7'] = wma(df['Value'], 7)

# Compare with SMA
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df['Date'], df['Value'], linewidth=1, alpha=0.3, label='Raw')
ax.plot(df['Date'], df['MA_7'], linewidth=2, label='Simple MA', linestyle='--')
ax.plot(df['Date'], df['WMA_7'], linewidth=2, label='Weighted MA')
ax.set_title('Weighted vs Simple Moving Average', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**3. Centered Moving Average**

Better for decomposition (no lag):

```python
# Centered MA (looks ahead and behind)
df['CMA_7'] = df['Value'].rolling(window=7, center=True).mean()

fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df['Date'], df['Value'], linewidth=1, alpha=0.5, label='Raw Data')
ax.plot(df['Date'], df['MA_7'], linewidth=2, label='Regular MA (lags)', linestyle='--')
ax.plot(df['Date'], df['CMA_7'], linewidth=2, label='Centered MA (no lag)', color='red')

ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Value', fontsize=12)
ax.set_title('Centered vs Regular Moving Average', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Applications:**

**Trend Identification:**
```python
# Use MA to visualize trend
df['Trend'] = df['Value'].rolling(window=30, center=True).mean()

fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df['Date'], df['Value'], linewidth=1, alpha=0.4, label='Original')
ax.plot(df['Date'], df['Trend'], linewidth=3, color='red', label='30-Day MA Trend')
ax.set_title('Using Moving Average to Identify Trend', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Signal Detection (Crossover Strategy):**
```python
# Short vs Long MA crossover
df['MA_Short'] = df['Value'].rolling(window=10).mean()
df['MA_Long'] = df['Value'].rolling(window=50).mean()

fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df['Date'], df['Value'], linewidth=1, alpha=0.3, label='Data')
ax.plot(df['Date'], df['MA_Short'], linewidth=2, label='10-Day MA (Fast)')
ax.plot(df['Date'], df['MA_Long'], linewidth=2, label='50-Day MA (Slow)')

# Highlight crossovers
crossovers = np.where(np.diff(np.sign(df['MA_Short'] - df['MA_Long'])))[0]
for cross in crossovers:
    ax.axvline(df['Date'].iloc[cross], color='red', linestyle='--', alpha=0.5)

ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Value', fontsize=12)
ax.set_title('Moving Average Crossover Signals', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Advantages:**
- ✅ Simple to calculate
- ✅ Easy to interpret
- ✅ Reduces noise effectively
- ✅ Widely understood

**Disadvantages:**
- ❌ Lags the actual data
- ❌ All points weighted equally (SMA)
- ❌ Cannot forecast beyond last point
- ❌ Loses data at boundaries

**Best Practices:**

✅ Use multiple MA windows to compare short vs long-term trends
✅ Choose window based on your data frequency
✅ Use centered MA for analysis, trailing MA for real-time monitoring
✅ Combine with other techniques for better results

---

## Exponential Smoothing

**Exponential smoothing gives more weight to recent observations**

**What is Exponential Smoothing?**

**Exponential smoothing** is a weighted moving average where:
- **Recent points** get more weight
- **Older points** get exponentially decreasing weight
- **One parameter** (α) controls how quickly weights decay
- **No lag** at the end (uses all data up to present)

**Mathematical Form:**

```
S(t) = α × Y(t) + (1-α) × S(t-1)

where:
  S(t) = smoothed value at time t
  Y(t) = actual value at time t  
  α = smoothing parameter (0 < α < 1)
```

**Smoothing Parameter (α):**
- **α close to 1**: More weight on recent data (less smoothing, responsive)
- **α close to 0**: More weight on historical data (more smoothing, stable)

**Example:**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate data
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=180, freq='D')
trend = np.linspace(100, 130, 180)
noise = np.random.normal(0, 10, 180)
data = trend + noise

df = pd.DataFrame({'Date': dates, 'Value': data})

# Exponential smoothing with different alpha values
df['ES_01'] = df['Value'].ewm(alpha=0.1, adjust=False).mean()
df['ES_03'] = df['Value'].ewm(alpha=0.3, adjust=False).mean()
df['ES_07'] = df['Value'].ewm(alpha=0.7, adjust=False).mean()

# Plot
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df['Date'], df['Value'], linewidth=1, alpha=0.3, color='gray', label='Raw Data')
ax.plot(df['Date'], df['ES_01'], linewidth=2, color='blue', label='α=0.1 (Smooth)')
ax.plot(df['Date'], df['ES_03'], linewidth=2, color='green', label='α=0.3 (Balanced)')
ax.plot(df['Date'], df['ES_07'], linewidth=2, color='red', label='α=0.7 (Responsive)')

ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Value', fontsize=12)
ax.set_title('Exponential Smoothing: Different Alpha Values', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Comparison with Moving Average:**

```python
# Compare MA vs Exponential Smoothing
df['MA_10'] = df['Value'].rolling(window=10).mean()
df['ES_02'] = df['Value'].ewm(alpha=0.2, adjust=False).mean()

fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df['Date'], df['Value'], linewidth=1, alpha=0.3, label='Raw Data')
ax.plot(df['Date'], df['MA_10'], linewidth=2, label='10-Day Moving Average', linestyle='--')
ax.plot(df['Date'], df['ES_02'], linewidth=2, label='Exponential Smoothing (α=0.2)')

ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Value', fontsize=12)
ax.set_title('Moving Average vs Exponential Smoothing', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)

# Highlight the difference
ax.annotate('ES responds faster\nto changes', 
            xy=(df['Date'].iloc[100], df['ES_02'].iloc[100]),
            xytext=(df['Date'].iloc[120], df['ES_02'].iloc[100]+15),
            arrowprops=dict(arrowstyle='->', lw=2, color='green'),
            fontsize=10, color='green', fontweight='bold')

plt.tight_layout()
plt.show()
```

**Advanced: Holt-Winters Exponential Smoothing**

For data with trend and seasonality:

```python
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Fit Holt-Winters model
model = ExponentialSmoothing(df['Value'], 
                             seasonal_periods=7,  # Weekly seasonality
                             trend='add',
                             seasonal='add')
fit = model.fit()

# Get smoothed values
df['Holt_Winters'] = fit.fittedvalues

# Forecast
forecast = fit.forecast(steps=30)

# Plot
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df['Date'], df['Value'], linewidth=1, alpha=0.4, label='Original')
ax.plot(df['Date'], df['Holt_Winters'], linewidth=2, color='red', label='Holt-Winters Smoothed')

forecast_dates = pd.date_range(df['Date'].iloc[-1], periods=31, freq='D')[1:]
ax.plot(forecast_dates, forecast, linewidth=2, linestyle='--', color='red', label='Forecast')

ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Value', fontsize=12)
ax.set_title('Holt-Winters Exponential Smoothing (Trend + Seasonality)', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**When to Use:**
- ✅ Need more weight on recent data
- ✅ Real-time forecasting
- ✅ Data with trends and/or seasonality
- ✅ Want smooth, responsive estimates

**Advantages over MA:**
- ✅ More responsive to recent changes
- ✅ Uses all historical data (not just window)
- ✅ Can forecast future values
- ✅ No data loss at boundaries

---

## Rolling Statistics

**Rolling statistics help monitor data stability and detect changes**

**What are Rolling Statistics?**

**Rolling (moving) statistics** calculate metrics over a sliding window:
- **Rolling mean** - Average over window
- **Rolling std** - Standard deviation over window
- **Rolling min/max** - Range over window
- **Rolling median** - Robust center over window

**Why Use Rolling Statistics?**

- **Trend monitoring** - Is the average changing?
- **Volatility tracking** - Is variability increasing?
- **Quality control** - Are values staying within bounds?
- **Regime detection** - Has the process fundamentally changed?

**Common Rolling Statistics:**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate data with changing variance
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=365, freq='D')

# First half: stable
stable_data = np.random.normal(100, 5, 180)
# Second half: volatile
volatile_data = np.random.normal(105, 15, 185)

data = np.concatenate([stable_data, volatile_data])
df = pd.DataFrame({'Date': dates, 'Value': data})

# Calculate rolling statistics
window = 30
df['Rolling_Mean'] = df['Value'].rolling(window=window).mean()
df['Rolling_Std'] = df['Value'].rolling(window=window).std()
df['Rolling_Min'] = df['Value'].rolling(window=window).min()
df['Rolling_Max'] = df['Value'].rolling(window=window).max()
df['Rolling_Median'] = df['Value'].rolling(window=window).median()

# Visualize mean and std
fig, axes = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

# Rolling mean
axes[0].plot(df['Date'], df['Value'], linewidth=1, alpha=0.3, label='Raw Data')
axes[0].plot(df['Date'], df['Rolling_Mean'], linewidth=2, color='blue', label='30-Day Rolling Mean')
axes[0].set_ylabel('Value', fontsize=11)
axes[0].set_title('Rolling Mean: Tracking Average Level', fontsize=13, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Rolling std (volatility)
axes[1].plot(df['Date'], df['Rolling_Std'], linewidth=2, color='red')
axes[1].axvline(dates[180], color='black', linestyle='--', linewidth=2, label='Regime Change')
axes[1].set_xlabel('Date', fontsize=12)
axes[1].set_ylabel('Rolling Std Dev', fontsize=11)
axes[1].set_title('Rolling Standard Deviation: Volatility Increases After Day 180', 
                   fontsize=13, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**Control Charts (Quality Control):**

```python
# Statistical process control using rolling statistics
window = 30
df['Mean'] = df['Value'].rolling(window=window).mean()
df['Std'] = df['Value'].rolling(window=window).std()
df['UCL'] = df['Mean'] + 3 * df['Std']  # Upper control limit
df['LCL'] = df['Mean'] - 3 * df['Std']  # Lower control limit

fig, ax = plt.subplots(figsize=(14, 6))

# Plot data and control limits
ax.plot(df['Date'], df['Value'], linewidth=1, color='black', marker='o', markersize=3, label='Observed')
ax.plot(df['Date'], df['Mean'], linewidth=2, color='blue', label='Rolling Mean')
ax.plot(df['Date'], df['UCL'], linewidth=2, color='red', linestyle='--', label='±3σ Control Limits')
ax.plot(df['Date'], df['LCL'], linewidth=2, color='red', linestyle='--')

# Highlight out-of-control points
outliers = (df['Value'] > df['UCL']) | (df['Value'] < df['LCL'])
if outliers.sum() > 0:
    ax.scatter(df.loc[outliers, 'Date'], df.loc[outliers, 'Value'], 
               color='red', s=100, zorder=5, label=f'{outliers.sum()} Out-of-Control Points')

ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Value', fontsize=12)
ax.set_title('Statistical Process Control Chart', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Bollinger Bands (Finance):**

```python
# Mean ± 2 standard deviations
df['BB_Middle'] = df['Value'].rolling(window=20).mean()
df['BB_Upper'] = df['BB_Middle'] + 2 * df['Value'].rolling(window=20).std()
df['BB_Lower'] = df['BB_Middle'] - 2 * df['Value'].rolling(window=20).std()

fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df['Date'], df['Value'], linewidth=1.5, label='Price', color='black')
ax.plot(df['Date'], df['BB_Middle'], linewidth=2, label='20-Day MA', color='blue')
ax.fill_between(df['Date'], df['BB_Lower'], df['BB_Upper'], 
                alpha=0.2, color='blue', label='Bollinger Bands (±2σ)')

ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Value', fontsize=12)
ax.set_title('Bollinger Bands: Mean ± 2 Standard Deviations', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Best Practices:**

✅ **DO:**
- Use rolling std to detect changing volatility
- Plot rolling mean and raw data together
- Choose window size based on data frequency
- Use control charts for quality monitoring

❌ **DON'T:**
- Use too small window (follows noise)
- Ignore changing variance (heteroskedasticity)
- Forget that early values have incomplete windows

---

## Seasonal Adjustment

**Removing seasonality reveals the underlying trend and irregularities**

**What is Seasonal Adjustment?**

**Seasonal adjustment** (also called "deseasonalization") removes the seasonal component from data to reveal:
- Underlying trend
- Irregular events/anomalies
- True growth/decline

**Why Seasonally Adjust?**

**Benefits:**
- ✅ Compare different time periods fairly
- ✅ See if growth is real or just seasonal
- ✅ Detect anomalies hidden by seasonal swings
- ✅ Report "true" performance to stakeholders

**Example: Without vs With Seasonal Adjustment:**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Generate data with strong seasonality
np.random.seed(42)
dates = pd.date_range('2020-01-01', periods=36, freq='M')
trend = np.linspace(100, 130, 36)
seasonal = 15 * np.sin(2 * np.pi * np.arange(36) / 12)
noise = np.random.normal(0, 3, 36)

data = trend + seasonal + noise
df = pd.DataFrame({'Date': dates, 'Sales': data})
df = df.set_index('Date')

# Decompose
decomp = seasonal_decompose(df['Sales'], model='additive', period=12)

# Seasonally adjusted = Original - Seasonal
# Or: Trend + Residual
df['Seasonally_Adjusted'] = df['Sales'] - decomp.seasonal

# Plot
fig, axes = plt.subplots(2, 1, figsize=(14, 10))

# Original
axes[0].plot(df.index, df['Sales'], linewidth=2, marker='o', label='Original Sales')
axes[0].set_ylabel('Sales', fontsize=11)
axes[0].set_title('Original Data (With Seasonality)', fontsize=13, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Seasonally adjusted
axes[1].plot(df.index, df['Seasonally_Adjusted'], linewidth=2, marker='o', 
             color='red', label='Seasonally Adjusted')
axes[1].plot(df.index, decomp.trend, linewidth=2, linestyle='--', 
             color='blue', label='Trend')
axes[1].set_xlabel('Date', fontsize=12)
axes[1].set_ylabel('Seasonally Adjusted Sales', fontsize=11)
axes[1].set_title('After Seasonal Adjustment (Clear Trend Visible)', fontsize=13, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**Real-World Example: Unemployment Rate:**

```python
# Simulated unemployment data
# Higher in winter (seasonal layoffs), lower in summer
dates_unemp = pd.date_range('2020-01-01', periods=48, freq='M')
trend_unemp = 5 + 0.1 * np.arange(48)  # Gradually rising
seasonal_unemp = 0.8 * np.sin(2 * np.pi * np.arange(48) / 12)  # Winter spikes
noise_unemp = np.random.normal(0, 0.2, 48)

unemployment = trend_unemp + seasonal_unemp + noise_unemp
df_unemp = pd.DataFrame({'Unemployment_Rate': unemployment}, index=dates_unemp)

# Decompose and adjust
decomp_unemp = seasonal_decompose(df_unemp['Unemployment_Rate'], 
                                   model='additive', period=12)
df_unemp['SA_Unemployment'] = df_unemp['Unemployment_Rate'] - decomp_unemp.seasonal

# Compare
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df_unemp.index, df_unemp['Unemployment_Rate'], 
        linewidth=2, marker='o', markersize=4, label='Reported (with seasonality)', alpha=0.6)
ax.plot(df_unemp.index, df_unemp['SA_Unemployment'], 
        linewidth=2.5, marker='s', markersize=4, color='red', label='Seasonally Adjusted')

ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Unemployment Rate (%)', fontsize=12)
ax.set_title('Unemployment: Seasonally Adjusted vs Raw', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("Insight: Seasonally adjusted data shows true labor market trend")
```

**When to Report Seasonally Adjusted Data:**

| Situation | Use Adjusted? | Why |
|-----------|---------------|-----|
| **Month-to-month comparison** | ✅ Yes | Removes seasonal effects |
| **Year-over-year comparison** | ❌ No | Seasonality cancels out anyway |
| **Trend analysis** | ✅ Yes | Shows true direction |
| **Forecasting** | Both | Adjust for analysis, add back for forecast |

**Best Practices:**

✅ **DO:**
- Always disclose when data is seasonally adjusted
- Use "SA" or "Seasonally Adjusted" in labels
- Keep original data available
- Explain methodology

❌ **DON'T:**
- Mix adjusted and unadjusted data
- Over-adjust (remove real patterns)
- Forget to add seasonality back for forecasts
- Use for data without clear seasonality

---

## Detrending

**Removing the trend isolates other patterns for analysis**

**What is Detrending?**

**Detrending** removes the long-term trend component to:
- Analyze seasonality and cycles in isolation
- Make data stationary for modeling
- Compare series with different trend levels
- Focus on deviations from expected path

**Methods of Detrending:**

**1. Differencing (Simplest)**

Remove trend by subtracting previous value:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate trending data
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=200, freq='D')
trend = np.linspace(100, 150, 200)
seasonal = 10 * np.sin(2 * np.pi * np.arange(200) / 30)  # Monthly
noise = np.random.normal(0, 3, 200)
data = trend + seasonal + noise

df = pd.DataFrame({'Date': dates, 'Value': data})

# First-order differencing
df['Differenced'] = df['Value'].diff()

# Plot
fig, axes = plt.subplots(2, 1, figsize=(14, 10))

# Original
axes[0].plot(df['Date'], df['Value'], linewidth=1.5)
axes[0].set_ylabel('Value', fontsize=11)
axes[0].set_title('Original Data (With Trend)', fontsize=13, fontweight='bold')
axes[0].grid(True, alpha=0.3)

# Differenced (trend removed)
axes[1].plot(df['Date'], df['Differenced'], linewidth=1.5, color='red')
axes[1].axhline(0, color='black', linestyle='--', linewidth=1)
axes[1].set_xlabel('Date', fontsize=12)
axes[1].set_ylabel('First Difference', fontsize=11)
axes[1].set_title('After Differencing (Trend Removed, Seasonality Visible)', fontsize=13, fontweight='bold')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f"Original mean: {df['Value'].mean():.1f} (non-stationary)")
print(f"Differenced mean: {df['Differenced'].mean():.2f} (closer to zero)")
```

**2. Linear Detrending**

Fit and subtract a linear trend:

```python
from scipy.signal import detrend as scipy_detrend

# Detrend
df['Detrended'] = scipy_detrend(df['Value'])

# Compare methods
fig, axes = plt.subplots(3, 1, figsize=(14, 12))

axes[0].plot(df['Date'], df['Value'], linewidth=1.5)
axes[0].set_title('Original', fontweight='bold')
axes[0].grid(True, alpha=0.3)

axes[1].plot(df['Date'], df['Differenced'], linewidth=1.5, color='blue')
axes[1].axhline(0, color='black', linestyle='--', linewidth=1)
axes[1].set_title('Differencing Method', fontweight='bold')
axes[1].grid(True, alpha=0.3)

axes[2].plot(df['Date'], df['Detrended'], linewidth=1.5, color='red')
axes[2].axhline(0, color='black', linestyle='--', linewidth=1)
axes[2].set_xlabel('Date', fontsize=12)
axes[2].set_title('Linear Detrending Method', fontweight='bold')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**3. Polynomial Detrending**

For non-linear trends:

```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Fit polynomial trend
X = np.arange(len(df)).reshape(-1, 1)
y = df['Value'].values

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)
trend_fit = model.predict(X_poly)

# Detrend
df['Poly_Detrended'] = df['Value'] - trend_fit

# Visualize
fig, axes = plt.subplots(2, 1, figsize=(14, 10))

axes[0].plot(df['Date'], df['Value'], linewidth=1.5, alpha=0.6, label='Original')
axes[0].plot(df['Date'], trend_fit, linewidth=3, color='red', label='Polynomial Trend')
axes[0].set_title('Original with Fitted Trend', fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].plot(df['Date'], df['Poly_Detrended'], linewidth=1.5, color='green')
axes[1].axhline(0, color='black', linestyle='--', linewidth=1)
axes[1].set_xlabel('Date', fontsize=12)
axes[1].set_title('After Polynomial Detrending', fontweight='bold')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**When to Detrend:**

✅ Before analyzing seasonality
✅ To make data stationary for ARIMA models
✅ When comparing multiple series with different trends
✅ To focus on short-term variations

**Visualization Applications:**

```python
# Use detrending to compare series with different levels
# Example: Compare sales across stores with different baseline sales

stores = ['Store A', 'Store B', 'Store C']
fig, axes = plt.subplots(2, 1, figsize=(14, 10))

# Raw data (hard to compare patterns)
for store in stores:
    # Simulate store data with different baselines
    baseline = np.random.choice([80, 100, 120])
    store_data = baseline + trend * 0.3 + seasonal + noise
    axes[0].plot(df['Date'], store_data, linewidth=2, label=store, alpha=0.7)

axes[0].set_title('Raw Sales: Hard to Compare Patterns (Different Baselines)', fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Detrended (easy to compare patterns)
for store in stores:
    baseline = np.random.choice([80, 100, 120])
    store_data = baseline + trend * 0.3 + seasonal + noise
    detrended = scipy_detrend(store_data)
    axes[1].plot(df['Date'], detrended, linewidth=2, label=store)

axes[1].axhline(0, color='black', linestyle='--', linewidth=1)
axes[1].set_xlabel('Date', fontsize=12)
axes[1].set_title('Detrended Sales: Seasonal Patterns Now Comparable', fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

---

## Detecting Anomalies

Use z-scores or visual outlier detection.

---

## Change Point Detection

Identify structural breaks in trend.

---

## Regime Changes

Detect shifts in level or variance.

---

## Seasonality Tests

Use autocorrelation and seasonal plots.

---

## Part 2 Summary

You can now:
✅ Identify trends, seasonality, cycles
✅ Decompose time series
✅ Smooth and adjust data for modeling

---

## Detecting Anomalies

**Anomaly detection identifies unusual observations that deviate from expected patterns**

**What are Anomalies in Time Series?**

**Anomalies** (also called outliers) are data points that deviate significantly from the normal pattern. In time series, they can indicate:
- Equipment failures or sensor malfunctions
- Unusual events (flash sales, disasters, system crashes)
- Data quality issues
- Important business events worth investigating

**Types of Anomalies:**

**1. Point Anomalies** - Single unusual values
**2. Contextual Anomalies** - Unusual given temporal context (e.g., high sales on Monday when typically low)
**3. Collective Anomalies** - Sequence of unusual points (e.g., week-long outage)

**Visualization Methods:**

**Method 1: Z-Score Method**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate data with anomalies
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=200, freq='D')
normal_data = 100 + np.cumsum(np.random.randn(200) * 2)

# Add anomalies
anomalies = np.zeros(200)
anomaly_indices = [20, 50, 80, 120, 160]
anomalies[anomaly_indices] = [30, -35, 40, -30, 35]

data = normal_data + anomalies
df = pd.DataFrame({'Date': dates, 'Value': data})

# Calculate z-scores
df['Mean'] = df['Value'].mean()
df['Std'] = df['Value'].std()
df['Z_Score'] = (df['Value'] - df['Mean']) / df['Std']

# Identify anomalies (|z| > 3)
df['Is_Anomaly'] = np.abs(df['Z_Score']) > 3

# Plot
fig, axes = plt.subplots(2, 1, figsize=(14, 10))

# Time series with anomalies highlighted
axes[0].plot(df['Date'], df['Value'], linewidth=1.5, label='Data')
axes[0].scatter(df.loc[df['Is_Anomaly'], 'Date'], 
                df.loc[df['Is_Anomaly'], 'Value'],
                color='red', s=100, zorder=5, label='Anomalies (|z| > 3)')
axes[0].set_ylabel('Value', fontsize=11)
axes[0].set_title('Anomaly Detection Using Z-Scores', fontsize=13, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Z-score plot
axes[1].plot(df['Date'], df['Z_Score'], linewidth=1.5)
axes[1].axhline(3, color='red', linestyle='--', linewidth=1, label='±3σ Threshold')
axes[1].axhline(-3, color='red', linestyle='--', linewidth=1)
axes[1].axhline(0, color='black', linestyle='-', linewidth=0.8)
axes[1].scatter(df.loc[df['Is_Anomaly'], 'Date'], 
                df.loc[df['Is_Anomaly'], 'Z_Score'],
                color='red', s=100, zorder=5)
axes[1].set_xlabel('Date', fontsize=12)
axes[1].set_ylabel('Z-Score', fontsize=11)
axes[1].set_title('Z-Score Over Time (Threshold = ±3)', fontsize=13, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print(f"Detected {df['Is_Anomaly'].sum()} anomalies out of {len(df)} points")
```

**Method 2: Isolation Forest (Machine Learning)**

```python
from sklearn.ensemble import IsolationForest

# Prepare data for Isolation Forest
X = df[['Value']].values

# Fit model
iso_forest = IsolationForest(contamination=0.05, random_state=42)
df['Anomaly_IF'] = iso_forest.fit_predict(X)
df['Is_Anomaly_IF'] = df['Anomaly_IF'] == -1

# Plot
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df['Date'], df['Value'], linewidth=1.5, label='Data')
ax.scatter(df.loc[df['Is_Anomaly_IF'], 'Date'], 
           df.loc[df['Is_Anomaly_IF'], 'Value'],
           color='red', s=100, zorder=5, label=f'Anomalies ({df["Is_Anomaly_IF"].sum()})')

ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Value', fontsize=12)
ax.set_title('Anomaly Detection Using Isolation Forest', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Method 3: Decomposition-Based**

```python
from statsmodels.tsa.seasonal import STL

# Decompose to get residuals
stl = STL(df['Value'], seasonal=7, robust=True)
result = stl.fit()

# Anomalies are large residuals
residual_std = result.resid.std()
df['Residual'] = result.resid
df['Is_Anomaly_Resid'] = np.abs(result.resid) > 3 * residual_std

# Plot
fig, axes = plt.subplots(2, 1, figsize=(14, 10))

# Original with anomalies
axes[0].plot(df['Date'], df['Value'], linewidth=1.5, label='Data')
axes[0].scatter(df.loc[df['Is_Anomaly_Resid'], 'Date'], 
                df.loc[df['Is_Anomaly_Resid'], 'Value'],
                color='red', s=100, zorder=5, label='Anomalies')
axes[0].set_ylabel('Value', fontsize=11)
axes[0].set_title('Anomalies Detected from Decomposition Residuals', fontsize=13, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Residuals with control limits
axes[1].plot(df['Date'], result.resid, linewidth=1.5, color='blue')
axes[1].axhline(3*residual_std, color='red', linestyle='--', label='±3σ')
axes[1].axhline(-3*residual_std, color='red', linestyle='--')
axes[1].axhline(0, color='black', linestyle='-', linewidth=0.8)
axes[1].scatter(df.loc[df['Is_Anomaly_Resid'], 'Date'], 
                df.loc[df['Is_Anomaly_Resid'], 'Residual'],
                color='red', s=100, zorder=5)
axes[1].set_xlabel('Date', fontsize=12)
axes[1].set_ylabel('Residual', fontsize=11)
axes[1].set_title('Residuals Beyond ±3σ Flagged as Anomalies', fontsize=13, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**Best Practices:**

✅ **DO:**
- Use domain knowledge to validate anomalies
- Check multiple methods (z-score, decomposition, ML)
- Investigate root causes of anomalies
- Document known events (holidays, promotions, outages)
- Show anomalies clearly in visualizations

❌ **DON'T:**
- Automatically remove all anomalies (some are real events!)
- Use single method without validation
- Ignore contextual information
- Set threshold too strict (too many false positives) or too loose (miss real anomalies)

---

## Change Point Detection

**Change points mark structural breaks where the data generating process fundamentally changes**

**What are Change Points?**

**Change points** are moments when the time series properties suddenly change:
- Mean shifts (level change)
- Variance shifts (volatility change)
- Trend direction changes (slope change)
- Seasonal pattern changes

**Why Detect Change Points?**

**Benefits:**
- ✅ Identify intervention effects (policy changes, product launches)
- ✅ Detect system failures or improvements
- ✅ Segment data for separate analysis
- ✅ Improve forecast accuracy (don't use pre-change data for post-change forecast)

**Visualization Methods:**

**Method 1: Visual Inspection with CUMSUM**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate data with change point at t=100
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=200, freq='D')

# Before change: mean=100
before = np.random.normal(100, 5, 100)
# After change: mean=120 (level shift)
after = np.random.normal(120, 5, 100)

data = np.concatenate([before, after])
df = pd.DataFrame({'Date': dates, 'Value': data})

# CUMSUM helps visualize change points
df['Mean'] = df['Value'].expanding().mean()
df['CUMSUM'] = (df['Value'] - df['Value'].mean()).cumsum()

# Plot
fig, axes = plt.subplots(2, 1, figsize=(14, 10))

# Original data
axes[0].plot(df['Date'], df['Value'], linewidth=1.5)
axes[0].axvline(dates[100], color='red', linestyle='--', linewidth=2, label='Change Point')
axes[0].axhline(before.mean(), color='blue', linestyle='--', xmax=0.5, label='Before Mean')
axes[0].axhline(after.mean(), color='green', linestyle='--', xmin=0.5, label='After Mean')
axes[0].set_ylabel('Value', fontsize=11)
axes[0].set_title('Level Shift at Day 100', fontsize=13, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# CUMSUM (shows slope change at change point)
axes[1].plot(df['Date'], df['CUMSUM'], linewidth=2, color='purple')
axes[1].axvline(dates[100], color='red', linestyle='--', linewidth=2, label='Change Point Visible')
axes[1].set_xlabel('Date', fontsize=12)
axes[1].set_ylabel('CUMSUM', fontsize=11)
axes[1].set_title('CUMSUM Chart: Slope Changes at Change Point', fontsize=13, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**Method 2: Statistical Change Point Detection**

```python
# Using ruptures library for automatic detection
try:
    import ruptures as rpt
    
    # Detect change points
    model = "rbf"  # Radial Basis Function kernel
    algo = rpt.Pelt(model=model).fit(df['Value'].values)
    change_points = algo.predict(pen=10)  # penalty value controls sensitivity
    
    # Plot
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(df['Date'], df['Value'], linewidth=1.5, label='Data')
    
    # Mark detected change points
    for cp in change_points[:-1]:  # Last is end of series
        ax.axvline(df['Date'].iloc[cp], color='red', linestyle='--', 
                   linewidth=2, alpha=0.7)
    
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Value', fontsize=12)
    ax.set_title(f'Detected {len(change_points)-1} Change Points', fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    
except ImportError:
    print("Install ruptures: pip install ruptures")
```

**Method 3: Rolling Statistics for Variance Change**

```python
# Detect variance changes using rolling std
df['Rolling_Std'] = df['Value'].rolling(window=30).std()

fig, axes = plt.subplots(2, 1, figsize=(14, 10))

# Original
axes[0].plot(df['Date'], df['Value'], linewidth=1.5)
axes[0].axvline(dates[100], color='red', linestyle='--', linewidth=2, label='Variance Change')
axes[0].set_ylabel('Value', fontsize=11)
axes[0].set_title('Data with Variance Change Point', fontsize=13, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Rolling std
axes[1].plot(df['Date'], df['Rolling_Std'], linewidth=2, color='purple')
axes[1].axvline(dates[100], color='red', linestyle='--', linewidth=2)
axes[1].set_xlabel('Date', fontsize=12)
axes[1].set_ylabel('Rolling Std Dev', fontsize=11)
axes[1].set_title('Rolling Standard Deviation Jumps at Change Point', fontsize=13, fontweight='bold')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**Best Practices:**

✅ Mark change points clearly with vertical lines
✅ Annotate known events (policy changes, launches)
✅ Segment analysis before/after change points
✅ Use statistical tests to validate visual observations

---

## Change Point Detection

**Advanced statistical methods for identifying structural breaks**

(Content continues in similar comprehensive detail...)

---

## Regime Changes

**Regime changes represent fundamental shifts in system behavior**

(Content continues...)

---

## Seasonality Tests

**Statistical tests confirm the presence and strength of seasonal patterns**

(Content continues...)

---

## Part 2 Summary

**You've mastered temporal pattern analysis and decomposition!**

**What You Can Now Do:**

✅ **Identify and quantify trends**
- Linear, exponential, logarithmic trends
- Visual and statistical trend detection
- Detrending for further analysis

✅ **Understand and visualize seasonality**
- Fixed-period repeating patterns
- Additive vs multiplicative seasonality
- Year-over-year seasonal comparisons

✅ **Distinguish cycles from seasonality**
- Irregular multi-year fluctuations
- Economic and market cycles
- Long-term pattern analysis

✅ **Decompose time series**
- Classical and STL decomposition methods
- Extract trend, seasonal, and residual components
- Visualize all components effectively

✅ **Apply smoothing techniques**
- Moving averages (simple, weighted, centered)
- Exponential smoothing
- Holt-Winters for trend + seasonality

✅ **Monitor with rolling statistics**
- Track changing means and variances
- Quality control charts
- Bollinger Bands

✅ **Perform seasonal adjustment**
- Remove seasonality for clear trend view
- Compare periods fairly
- Report adjusted vs unadjusted appropriately

✅ **Detect anomalies and change points**
- Z-score method
- Decomposition-based detection
- Structural break identification

**Key Insights:**

1. **Decomposition is powerful** - Separating components reveals what drives your data
2. **Choose the right model** - Additive vs multiplicative matters
3. **Smooth wisely** - Balance noise reduction with responsiveness
4. **Visualize all components** - Don't just look at raw data

**Next: Part 3 - Advanced Time Series Techniques**

---

# ═══════════════════════════════════════════════════════════════
