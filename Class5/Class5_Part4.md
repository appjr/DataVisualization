# Class 5 – Implementation & Applications

[← Main](Class5.md) | [Part 1](Class5_Part1.md) | [Part 2](Class5_Part2.md) | [Part 3](Class5_Part3.md) | [Part 4](Class5_Part4.md)

---

# PART 4: IMPLEMENTATION & APPLICATIONS
# Slides 61-80
# ═══════════════════════════════════════════════════════════════

## Python Tools for Time Series

**Essential libraries for professional time series work**

**Core Stack:**

1. **pandas** - Data manipulation and time operations
2. **matplotlib** - Customizable plotting
3. **seaborn** - Statistical visualization
4. **statsmodels** - Statistical analysis and forecasting
5. **plotly** - Interactive dashboards
6. **prophet** - Automated forecasting

**Installation:**
```bash
pip install pandas matplotlib seaborn statsmodels plotly prophet
```

**Quick Comparison:**

| Tool | Best For | Learning Curve |
|------|----------|----------------|
| pandas | Data prep | Easy |
| matplotlib | Custom plots | Medium |
| seaborn | Quick stats plots | Easy |
| statsmodels | Statistical models | Hard |
| plotly | Dashboards | Easy |
| prophet | Auto forecasts | Easy |

---

## pandas DateTime Operations

**pandas provides powerful time series manipulation**

**Key Operations:**

**Resampling:**
```python
import pandas as pd
import numpy as np

# Daily to weekly
daily_data.resample('W').mean()

# Hourly to daily
hourly_data.resample('D').sum()

# Custom aggregation
df.resample('M').agg({'Sales': ['sum', 'mean', 'std']})
```

**Shifting & Lagging:**
```python
# Create lagged features
df['Sales_Lag1'] = df['Sales'].shift(1)
df['Sales_Lag7'] = df['Sales'].shift(7)

# Calculate changes
df['Change'] = df['Sales'].diff()
df['Pct_Change'] = df['Sales'].pct_change()
```

**Rolling Windows:**
```python
# Moving statistics
df['MA_7'] = df['Sales'].rolling(window=7).mean()
df['Rolling_Std'] = df['Sales'].rolling(window=30).std()

# Expanding windows
df['Cumulative_Sum'] = df['Sales'].expanding().sum()
```

**Time-based Indexing:**
```python
# Slice by date
df['2024-01':'2024-06']
df.loc['2024-03-15']
df.between_time('09:00', '17:00')  # Business hours
```

---

## Matplotlib Time Series

**matplotlib offers precise control for temporal plots**

**Date Formatting:**
```python
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df.index, df['Sales'])

# Format dates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

**Useful Formatters:**
- `%Y-%m-%d` → 2024-01-15
- `%b %Y` → Jan 2024
- `%d %b` → 15 Jan

**Annotations:**
```python
# Event markers
ax.axvline('2024-06-15', color='red', linestyle='--', label='Launch')
ax.axhline(1000, color='green', linestyle='--', label='Target')

# Text annotations
ax.annotate('Peak', xy=('2024-08-01', 1500),
            xytext=('2024-09-01', 1600),
            arrowprops=dict(arrowstyle='->'))
```

---

## Seaborn for Temporal Data

**seaborn simplifies statistical time series viz**

**Time Series Plots:**
```python
import seaborn as sns

# Line plot with CI
sns.relplot(data=df, x='Date', y='Sales', kind='line', height=6, aspect=2)

# Multiple series by category
sns.relplot(data=df, x='Date', y='Sales', hue='Region', kind='line')

# Small multiples
sns.relplot(data=df, x='Date', y='Sales', col='Product', col_wrap=3, kind='line')
```

**Seasonal Box Plots:**
```python
df['Month'] = df.index.month
sns.boxplot(data=df, x='Month', y='Sales')
plt.title('Sales Distribution by Month')
plt.show()
```

---

## Plotly Interactive Time Series

**plotly creates web-ready interactive visualizations**

**Basic Interactive:**
```python
import plotly.express as px

fig = px.line(df, x='Date', y='Sales', title='Interactive Sales')
fig.show()
```

**Advanced with Range Slider:**
```python
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['Sales'], 
                        mode='lines', name='Sales'))

# Add range slider
fig.update_xaxes(rangeslider_visible=True)
fig.update_layout(hovermode='x unified')

fig.show()
```

**Multiple Series:**
```python
fig = go.Figure()

for col in ['Product_A', 'Product_B', 'Product_C']:
    fig.add_trace(go.Scatter(x=df.index, y=df[col], 
                            mode='lines', name=col))

fig.update_layout(title='Product Comparison',
                 xaxis_title='Date',
                 yaxis_title='Sales')
fig.show()
```

---

## Facebook Prophet

**prophet automates forecasting with seasonality**

**Basic Usage:**
```python
from prophet import Prophet
import pandas as pd

# Prepare data (requires 'ds' and 'y' columns)
df_prophet = pd.DataFrame({
    'ds': df.index,
    'y': df['Sales'].values
})

# Fit model
model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False
)
model.fit(df_prophet)

# Forecast
future = model.make_future_dataframe(periods=90, freq='D')
forecast = model.predict(future)

# Plot
fig1 = model.plot(forecast)
plt.title('Prophet Forecast with Confidence Intervals')
plt.show()

# Component plots
fig2 = model.plot_components(forecast)
plt.show()
```

**Key Features:**
- Automatic seasonality detection
- Built-in uncertainty intervals
- Handles missing data
- Easy to use

---

## statsmodels Decomposition

**statsmodels provides statistical decomposition methods**

**Classical Decomposition:**
```python
from statsmodels.tsa.seasonal import seasonal_decompose

result = seasonal_decompose(df['Sales'], 
                           model='additive',  # or 'multiplicative'
                           period=7)          # Weekly seasonality
result.plot()
plt.show()
```

**STL Decomposition (Robust):**
```python
from statsmodels.tsa.seasonal import STL

stl = STL(df['Sales'], 
          seasonal=13,  # Seasonal smoother length
          robust=True)  # Handle outliers

result = stl.fit()
result.plot()
plt.show()
```

---

## Real-World Case Study 1

**Retail Sales Seasonality Analysis**

**Scenario:** Optimize staffing and inventory for seasonal demand.

**Approach:**
1. Load historical sales data (2+ years)
2. Decompose to identify seasonal patterns
3. Visualize peak months and days of week
4. Forecast next quarter with uncertainty
5. Present findings to management

**Key Visualizations:**
- Year-over-year comparison by month
- Day-of-week box plots
- Decomposition showing seasonal component
- Forecast with confidence bands

---

## Real-World Case Study 2

**Stock Price Volatility Analysis**

**Scenario:** Assess risk and volatility trends.

**Approach:**
1. Load daily stock prices
2. Calculate daily returns (percent change)
3. Compute rolling volatility (30-day std)
4. Identify high/low volatility periods
5. Create Bollinger Bands visualization

**Key Metrics:**
- Daily returns distribution
- Rolling volatility over time
- Maximum drawdown
- Sharpe ratio

---

## Real-World Case Study 3

**Sensor Monitoring & Anomaly Detection**

**Scenario:** Real-time monitoring with alerting.

**Approach:**
1. Stream sensor data (temperature, pressure, etc.)
2. Calculate rolling mean and std
3. Set control limits (±3σ)
4. Flag anomalies automatically
5. Visualize with real-time updates

**Implementation:**
- Rolling statistics for baselines
- Z-score anomaly detection
- Color-coded alerts (red = anomaly)
- Historical comparison overlay

---

## Dashboard Design for Temporal Data

**Best practices for time series dashboards**

**Key Principles:**

1. **Consistent Scales**
   - Same y-axis across comparable panels
   - Aligned time ranges
   - Clear units

2. **Clear Hierarchy**
   - Overview at top
   - Detail views below
   - Most important metrics prominent

3. **Progressive Detail**
   - Start with summary/KPIs
   - Drill down to detail on demand
   - Breadcrumbs for navigation

**Typical Layout:**
```
┌─────────────────────────────────┐
│  KPIs (Current Values)          │
├──────────────┬──────────────────┤
│ Trend        │ Seasonality      │
│ (Long-term)  │ (Patterns)       │
├──────────────┴──────────────────┤
│  Recent Detail (Last 30 days)   │
└─────────────────────────────────┘
```

**Refresh Frequency:**
- Real-time: Every second (sensors)
- Near real-time: Every minute (web traffic)
- Periodic: Hourly, daily (business metrics)

---

## Multi-Scale Dashboards

**Provide overview and detail simultaneously**

**Structure:**

**Top Panel:** Long-term trend (years/months)
- Strategic view
- Overall direction
- Major milestones

**Middle Panels:** Medium-term (weeks/months)
- Tactical view
- Seasonal patterns
- Recent performance

**Bottom Panel:** Recent detail (days/hours)
- Operational view
- Current status
- Immediate issues

**Navigation:**
- Click to drill down
- Synchronized time selection across views
- Zoom maintains context

---

## Best Practices Checklist

**Before finalizing any time series visualization:**

**Data Quality:**
- [ ] Dates parsed correctly
- [ ] Missing data handled transparently
- [ ] Timezone consistent
- [ ] No duplicate timestamps

**Visual Design:**
- [ ] Time on x-axis (horizontal)
- [ ] Appropriate time scale
- [ ] Clear axis labels with units
- [ ] Minimal clutter
- [ ] Professional appearance

**Pattern Communication:**
- [ ] Trend visible (if present)
- [ ] Seasonality annotated
- [ ] Anomalies highlighted
- [ ] Reference lines for context

**Forecasting:**
- [ ] Uncertainty intervals included
- [ ] Forecast clearly distinguished
- [ ] Assumptions documented
- [ ] Validation metrics reported

**Accessibility:**
- [ ] Color-blind friendly palette
- [ ] Adequate contrast
- [ ] Alt text for images
- [ ] Readable font sizes

---

## Assignment & Resources

**Assignment:** Complete time series EDA and forecast report.

**Deliverables:**
1. Jupyter notebook with analysis
2. Executive summary (1 page)
3. Forecast visualization with uncertainty
4. Interactive dashboard (optional)

**Recommended Resources:**

**Books:**
- *Forecasting: Principles and Practice* - Hyndman & Athanasopoulos
- *Time Series Analysis and Its Applications* - Shumway & Stoffer

**Online:**
- statsmodels.org
- plotly.com/python
- facebook.github.io/prophet

**Datasets:**
- FRED (Federal Reserve Economic Data)
- Yahoo Finance
- Kaggle time series competitions
- UCI Machine Learning Repository

**Tools:**
- Jupyter notebooks
- VS Code with Python extension
- Git for version control

---

## Summary & Next Class Preview

**Class 5 Summary:**

**✅ Fundamentals**
- Time series data characteristics
- Line charts and time scales
- Missing data strategies
- Date/time handling

**✅ Patterns & Decomposition**
- Trends (linear, exponential, log)
- Seasonality (additive, multiplicative)
- Decomposition (Classical, STL)
- Smoothing and adjustment

**✅ Advanced Techniques**
- Comparing multiple series
- ACF/PACF analysis
- Forecasting with uncertainty
- Backtesting and validation

**✅ Implementation**
- Python tool ecosystem
- Best practices
- Real-world applications
- Dashboard design

**Key Takeaways:**

1. **Time is special** - Requires specialized visualization approaches
2. **Decompose to understand** - Separate trend, seasonal, noise
3. **Always show uncertainty** - Point forecasts alone are misleading
4. **Choose scale wisely** - Match aggregation to question and audience
5. **Make it interactive** - When possible, enable exploration

**Next Class:** Advanced storytelling and narrative visualization techniques for data-driven communication.

**Keep practicing!** Time series visualization is essential for:
- Financial analysis
- Business forecasting
- Operations monitoring
- Scientific research
- Any data with temporal structure

---

**Thank you for engaging with Class 5!** 🎓

For questions or clarifications:
- Review the Part notebooks (executable code)
- Complete the exercises (hands-on practice)
- Consult the resources listed above

**See you in the next class!**

---

# ═══════════════════════════════════════════════════════════════
