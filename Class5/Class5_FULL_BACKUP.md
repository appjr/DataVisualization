# Class 5 – Data Visualization
## Time Series & Temporal Visualization
## Patterns, Trends, and Forecasting

---

# 📚 Table of Contents

## Quick Navigation
- [Part 1: Fundamentals of Time Series Visualization](#part-1-fundamentals-of-time-series-visualization)
- [Part 2: Temporal Patterns & Decomposition](#part-2-temporal-patterns--decomposition)
- [Part 3: Advanced Time Series Techniques](#part-3-advanced-time-series-techniques)
- [Part 4: Implementation & Applications](#part-4-implementation--applications)

---

## Detailed Index

### Part 1: Fundamentals (Slides 1-20)
- [Title Slide](#class-5--data-visualization)
- [Learning Objectives](#learning-objectives)
- [Why Time Series Visualization Matters](#why-time-series-visualization-matters)
- [What Makes Time Series Data Special](#what-makes-time-series-data-special)
- [Types of Temporal Data](#types-of-temporal-data)
- [Basic Time Series Plot: The Line Chart](#basic-time-series-plot-the-line-chart)
- [Choosing Appropriate Time Scales](#choosing-appropriate-time-scales)
- [Handling Missing Temporal Data](#handling-missing-temporal-data)
- [Date/Time Formatting in Python](#datetime-formatting-in-python)
- [Time Zones and DST Issues](#time-zones-and-dst-issues)
- [Aspect Ratio and Chart Proportions](#aspect-ratio-and-chart-proportions)
- [Color in Time Series](#color-in-time-series)
- [Multiple Time Series on One Plot](#multiple-time-series-on-one-plot)
- [Small Multiples for Time Series](#small-multiples-for-time-series)
- [Common Temporal Visualization Mistakes](#common-temporal-visualization-mistakes)
- [Y-Axis Decisions](#y-axis-decisions)
- [Annotation Best Practices](#annotation-best-practices)
- [Reference Lines and Benchmarks](#reference-lines-and-benchmarks)
- [Interactive vs. Static Time Series](#interactive-vs-static-time-series)
- Part 1 Summary

### Part 2: Temporal Patterns & Decomposition (Slides 21-40)
- [Introduction to Temporal Patterns](#introduction-to-temporal-patterns)
- [Identifying Trends](#identifying-trends)
- [Linear vs. Non-Linear Trends](#linear-vs-non-linear-trends)
- [Seasonal Patterns](#seasonal-patterns)
- [Types of Seasonality](#types-of-seasonality)
- [Cyclic Patterns](#cyclic-patterns)
- [Time Series Decomposition](#time-series-decomposition)
- [Classical Decomposition Method](#classical-decomposition-method)
- [STL Decomposition](#stl-decomposition)
- [Visualizing Decomposition Results](#visualizing-decomposition-results)
- [Moving Averages](#moving-averages)
- [Exponential Smoothing](#exponential-smoothing)
- [Rolling Statistics](#rolling-statistics)
- [Seasonal Adjustment](#seasonal-adjustment)
- [Detrending](#detrending)
- [Detecting Anomalies](#detecting-anomalies)
- [Change Point Detection](#change-point-detection)
- [Regime Changes](#regime-changes)
- [Seasonality Tests](#seasonality-tests)
- [Part 2 Summary](#part-2-summary)

### Part 3: Advanced Techniques (Slides 41-60)
- [Comparing Multiple Time Series](#comparing-multiple-time-series)
- [Index-Based Comparisons](#index-based-comparisons)
- [Percent Change Visualization](#percent-change-visualization)
- [Lag Plots](#lag-plots)
- [Autocorrelation Function (ACF)](#autocorrelation-function-acf)
- [Partial Autocorrelation (PACF)](#partial-autocorrelation-pacf)
- [Cross-Correlation](#cross-correlation)
- [Lead-Lag Relationships](#lead-lag-relationships)
- [Forecasting Visualization Principles](#forecasting-visualization-principles)
- [Point Forecasts vs. Intervals](#point-forecasts-vs-intervals)
- [Confidence Intervals](#confidence-intervals)
- [Fan Charts](#fan-charts)
- [Backtesting Visualizations](#backtesting-visualizations)
- [Forecast Error Analysis](#forecast-error-analysis)
- [Calendar Heatmaps](#calendar-heatmaps)
- [Horizon Charts](#horizon-charts)
- [Stream Graphs](#stream-graphs)
- [Cycle Plots](#cycle-plots)
- [Interactive Time Series with Plotly](#interactive-time-series-with-plotly)
- [Part 3 Summary](#part-3-summary)

### Part 4: Implementation & Applications (Slides 61-80)
- [Python Tools for Time Series](#python-tools-for-time-series)
- [pandas DateTime Operations](#pandas-datetime-operations)
- [Matplotlib Time Series](#matplotlib-time-series)
- [Seaborn for Temporal Data](#seaborn-for-temporal-data)
- [Plotly Interactive Time Series](#plotly-interactive-time-series)
- [Facebook Prophet](#facebook-prophet)
- [statsmodels Decomposition](#statsmodels-decomposition)
- [Real-World Case Study 1](#real-world-case-study-1)
- [Real-World Case Study 2](#real-world-case-study-2)
- [Real-World Case Study 3](#real-world-case-study-3)
- [Dashboard Design for Temporal Data](#dashboard-design-for-temporal-data)
- [Multi-Scale Dashboards](#multi-scale-dashboards)
- [Best Practices Checklist](#best-practices-checklist)
- [Exercise 1: Identify Temporal Patterns](#exercise-1-identify-temporal-patterns)
- [Exercise 2: Choose the Right Time Scale](#exercise-2-choose-the-right-time-scale)
- [Exercise 3: Time Series Decomposition](#exercise-3-time-series-decomposition)
- [Exercise 4: Forecasting Visualization](#exercise-4-forecasting-visualization)
- [Exercise 5: Interactive Dashboard](#exercise-5-interactive-dashboard)
- [Assignment & Resources](#assignment--resources)
- [Summary & Next Class Preview](#summary--next-class-preview)

---

# ═══════════════════════════════════════════════════════════════
# PART 1: FUNDAMENTALS OF TIME SERIES VISUALIZATION
# Slides 1-20
# ═══════════════════════════════════════════════════════════════

# Class 5 – Data Visualization
## Time Series & Temporal Visualization
## Patterns, Trends, and Forecasting

**MIS 6380 - Data Visualization**  
**Spring 2026**

---

## Learning Objectives

**By the end of this class, you will be able to:**

**Foundational Knowledge:**
- ✅ Understand unique characteristics of temporal data
- ✅ Recognize different types of time series patterns
- ✅ Choose appropriate visualizations for temporal analysis

**Technical Skills:**
- ✅ Create effective time series visualizations in Python
- ✅ Perform time series decomposition
- ✅ Visualize forecasts with confidence intervals
- ✅ Build interactive temporal dashboards

**Analytical Abilities:**
- ✅ Identify trends, seasonality, and cycles
- ✅ Detect anomalies and change points
- ✅ Compare multiple time series effectively
- ✅ Communicate temporal insights clearly

**Practical Applications:**
- ✅ Apply best practices for temporal dashboards
- ✅ Handle missing and irregular temporal data
- ✅ Visualize uncertainty in predictions
- ✅ Make data-driven temporal decisions

**Prerequisites**: Classes 3-4 (Visual perception, EDA, Python visualization basics)

---

## Why Time Series Visualization Matters

**Time is everywhere in business analytics:**

**Financial Services:**
- 📈 Stock prices and trading volumes
- 💰 Portfolio performance tracking
- 📊 Market volatility analysis
- 💵 Revenue and profit trends
- 🏦 Transaction patterns

**Retail & E-commerce:**
- 🛒 Daily/hourly sales patterns
- 📦 Inventory levels over time
- 👥 Customer traffic patterns
- 🎯 Conversion rate trends
- 🎁 Seasonal demand forecasting

**Manufacturing & Operations:**
- 🏭 Production output trends
- ⚙️ Equipment performance metrics
- 📉 Quality control over time
- 🔧 Maintenance schedules
- ⏱️ Downtime analysis

**Digital & Technology:**
- 🌐 Website traffic patterns
- 📱 App usage metrics
- 🔍 Search trends over time
- ⚡ System performance monitoring
- 🚨 Incident detection

**Healthcare & Science:**
- 🏥 Patient vital signs monitoring
- 💊 Treatment effectiveness over time
- 🦠 Disease spread patterns
- 🧪 Experimental measurements
- 📋 Clinical trial results

**Economics & Government:**
- 📊 GDP and economic indicators
- 👔 Employment statistics
- 💰 Inflation rates
- 🏘️ Housing market trends
- 📈 Policy impact analysis

**IoT & Sensors:**
- 🌡️ Temperature and climate data
- 📡 Network traffic patterns
- ⚡ Energy consumption
- 🚗 Vehicle telemetry
- 🏢 Building automation

**Why temporal visualization is critical:**

1. **Pattern Discovery** - Trends and cycles invisible in static data become obvious over time
2. **Forecasting** - Historical patterns enable prediction of future values
3. **Anomaly Detection** - Unusual events stand out in temporal context
4. **Causality** - Temporal relationships suggest cause-and-effect
5. **Decision Making** - Timing of actions depends on temporal insights

**Key Insight**: 70-80% of business data has a temporal component. Mastering temporal visualization is essential for data-driven decision making.

> "Time series analysis is not just about predicting the future—it's about understanding how we got here and what patterns govern change." — Rob Hyndman

---

## What Makes Time Series Data Special?

**Time series data has unique properties that standard data analysis doesn't handle:**

**1. Temporal Ordering Matters**
```
Standard data:     [A, B, C, D, E] can be shuffled
Time series data:  [t₁, t₂, t₃, t₄, t₅] CANNOT be shuffled
```
- Order contains critical information
- Shuffling destroys temporal dependencies
- Chronological sequence must be preserved

**2. Temporal Dependencies**
```
Today's value depends on yesterday's value
Y(t) = f(Y(t-1), Y(t-2), ..., Y(t-n))
```
- **Autocorrelation** - correlation with past values
- **Lag effects** - impacts from previous time periods
- **Momentum** - trends tend to continue
- **Mean reversion** - tendency to return to average

**3. Non-IID (Not Independent and Identically Distributed)**

Standard statistical assumptions **VIOLATED:**
- ❌ Observations are NOT independent
- ❌ Distributions may NOT be identical across time
- ❌ Standard hypothesis tests may be invalid
- ❌ Regression assumptions may fail

**Implications:**
- ✅ Must use time-specific analysis methods
- ✅ Cannot treat as cross-sectional data
- ✅ Need specialized visualization techniques

**4. Multiple Time Scales Simultaneously**

Time series often contain patterns at different scales:
```
Hourly patterns:  Peak usage during work hours
Daily patterns:   Weekday vs weekend differences  
Weekly patterns:  Consistent 7-day cycles
Monthly patterns: End-of-month effects
Seasonal patterns: Summer vs winter variations
Annual patterns:  Year-over-year growth
```

**5. Non-Stationarity**

**Stationary process**: Statistical properties (mean, variance) constant over time  
**Non-stationary process**: Properties change over time

Most real-world time series are **non-stationary:**
- Trends (mean changes)
- Seasonality (variance changes)
- Structural breaks (sudden shifts)
- Regime changes (different behaviors in different periods)

**6. Irregular Intervals & Missing Data**

Unlike designed experiments:
- ❌ May have gaps (weekends, holidays, sensor failures)
- ❌ Irregular sampling intervals
- ❌ Missing values have temporal meaning
- ✅ Must handle carefully in visualization

**7. Context-Dependent Interpretation**

Same value means different things at different times:
- $100 daily revenue in January vs December (holiday effects)
- 75°F in March vs September (seasonal context)
- 1000 website visitors on Monday vs Sunday (day-of-week effects)

**Why this matters for visualization:**

**Standard Approach:**
```python
# WRONG for time series!
plt.scatter(x, y)  # Ignores temporal order
plt.bar(categories, values)  # Loses time information
```

**Time Series Approach:**
```python
# CORRECT for time series!
plt.plot(dates, values)  # Preserves temporal order
plt.plot(dates, values, marker='o')  # Shows continuity + points
```

**Key Principles:**
1. **Always show time explicitly** (usually on x-axis)
2. **Preserve chronological order** (never shuffle)
3. **Show continuity** (use lines, not just points)
4. **Provide temporal context** (reference periods, benchmarks)
5. **Handle multiple scales** (zoom, aggregation, decomposition)
6. **Visualize uncertainty** (especially in forecasts)

**Bottom line**: Time series require specialized visualization approaches because temporal structure contains critical information that standard methods destroy.

---

## Types of Temporal Data

**Understanding your temporal data type guides visualization choice:**

**1. Time Points (Discrete Events)**

**Definition**: Events occurring at specific moments in time

**Characteristics:**
- Precise timestamps
- No duration
- Count-based analysis

**Examples:**
- 🛒 Customer purchases (2024-01-15 14:32:18)
- 🌍 Earthquakes (magnitude 5.2 at 2024-02-10 03:15:42)
- 🐦 Social media posts (tweet at 2024-03-05 09:22:15)
- 📧 Email arrivals
- 🔔 System alerts
- 🏃 Race finish times

**Visualization Approaches:**

**Event Plot (Rug Plot)**:
```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate random event times
np.random.seed(42)
events = pd.to_datetime('2024-01-01') + pd.to_timedelta(
    np.random.exponential(scale=2, size=100), unit='D'
)

fig, ax = plt.subplots(figsize=(12, 2))
ax.eventplot(events, lineoffsets=0.5, linelengths=0.8, color='steelblue')
ax.set_xlabel('Date', fontsize=11)
ax.set_title('Customer Purchase Events', fontsize=13, fontweight='bold')
ax.set_yticks([])
plt.tight_layout()
plt.show()
```

**Timeline (Scatter)**:
```python
# Count events per day
daily_counts = events.value_counts().sort_index()

plt.figure(figsize=(12, 5))
plt.plot(daily_counts.index, daily_counts.values, marker='o', 
         linestyle='-', linewidth=1, markersize=4)
plt.xlabel('Date', fontsize=11)
plt.ylabel('Number of Events', fontsize=11)
plt.title('Daily Event Frequency', fontsize=13, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**When to use**: Transaction data, log files, event streams

---

**2. Time Intervals (Spans/Durations)**

**Definition**: Events with start and end times (duration matters)

**Characteristics:**
- Start time + end time
- Duration is meaningful
- May overlap

**Examples:**
- 🏥 Hospital patient stays (admitted 2024-01-10, discharged 2024-01-15)
- 🏭 Manufacturing batch production (started 08:00, finished 14:30)
- ✈️ Flight durations (departure to arrival)
- 🔧 System maintenance windows
- 📞 Phone call durations
- 🎬 Video viewing sessions

**Visualization Approaches:**

**Gantt Chart**:
```python
import matplotlib.pyplot as plt
import pandas as pd

# Sample data: project tasks
tasks = pd.DataFrame({
    'Task': ['Design', 'Development', 'Testing', 'Deployment'],
    'Start': pd.to_datetime(['2024-01-01', '2024-01-15', '2024-02-15', '2024-03-01']),
    'End': pd.to_datetime(['2024-01-20', '2024-02-20', '2024-03-05', '2024-03-10'])
})

fig, ax = plt.subplots(figsize=(12, 5))

for idx, row in tasks.iterrows():
    ax.barh(idx, (row['End'] - row['Start']).days, 
            left=row['Start'], height=0.5, 
            color='steelblue', alpha=0.8)
    ax.text(row['Start'], idx, f"  {row['Task']}", 
            va='center', fontsize=10, fontweight='bold')

ax.set_yticks(range(len(tasks)))
ax.set_yticklabels([])
ax.set_xlabel('Date', fontsize=11)
ax.set_title('Project Timeline (Gantt Chart)', fontsize=13, fontweight='bold')
ax.grid(True, axis='x', alpha=0.3)
plt.tight_layout()
plt.show()
```

**Timeline with Bars**:
```python
# Hospital bed occupancy
occupancy = pd.DataFrame({
    'Patient': ['A', 'B', 'C', 'D'],
    'Admitted': pd.to_datetime(['2024-01-01', '2024-01-03', '2024-01-05', '2024-01-06']),
    'Discharged': pd.to_datetime(['2024-01-08', '2024-01-12', '2024-01-09', '2024-01-14'])
})

fig, ax = plt.subplots(figsize=(12, 4))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

for idx, row in occupancy.iterrows():
    duration = (row['Discharged'] - row['Admitted']).days
    ax.barh(idx, duration, left=row['Admitted'], 
            height=0.6, color=colors[idx], alpha=0.7,
            label=f"Patient {row['Patient']}")

ax.set_yticks(range(len(occupancy)))
ax.set_yticklabels([f"Patient {p}" for p in occupancy['Patient']])
ax.set_xlabel('Date', fontsize=11)
ax.set_title('Hospital Bed Occupancy', fontsize=13, fontweight='bold')
ax.legend(loc='upper right')
ax.grid(True, axis='x', alpha=0.3)
plt.tight_layout()
plt.show()
```

**When to use**: Project management, resource scheduling, session analysis

---

**3. Regular Time Series (Fixed Intervals)**

**Definition**: Measurements at consistent, regular intervals

**Characteristics:**
- Fixed frequency (hourly, daily, monthly)
- Continuous monitoring
- Most common type

**Examples:**
- 📊 Daily stock closing prices
- 🌡️ Hourly temperature readings
- 💰 Monthly sales figures
- 📈 Quarterly GDP
- ⚡ Minute-by-minute power consumption
- 🌐 Weekly website visitors

**Visualization Approaches:**

**Line Chart (Most Common)**:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate sample daily sales data with trend and seasonality
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=365, freq='D')
trend = np.linspace(50000, 65000, 365)
seasonal = 5000 * np.sin(np.arange(365) * 2 * np.pi / 365)
noise = np.random.normal(0, 2000, 365)
sales = trend + seasonal + noise

plt.figure(figsize=(14, 6))
plt.plot(dates, sales, linewidth=1.5, color='steelblue', label='Daily Sales')
plt.xlabel('Date', fontsize=11)
plt.ylabel('Sales ($)', fontsize=11)
plt.title('Daily Sales - 2023 (Regular Time Series)', 
          fontsize=13, fontweight='bold')
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Area Chart (Emphasizes Volume)**:
```python
plt.figure(figsize=(14, 6))
plt.fill_between(dates, sales, alpha=0.3, color='steelblue', label='Daily Sales')
plt.plot(dates, sales, linewidth=1.5, color='steelblue')
plt.xlabel('Date', fontsize=11)
plt.ylabel('Sales ($)', fontsize=11)
plt.title('Daily Sales with Area Fill', fontsize=13, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**When to use**: Continuous monitoring data, business metrics, sensor data

---

**4. Irregular Time Series (Variable Intervals)**

**Definition**: Measurements at non-uniform, irregular intervals

**Characteristics:**
- Variable time gaps
- Event-driven sampling
- Requires interpolation decisions

**Examples:**
- 🏥 Medical checkups (as needed, not scheduled)
- 🔧 Equipment maintenance logs (when problems occur)
- 🎯 Survey responses (voluntary participation)
- 📝 Customer feedback (sporadic)
- 🌊 Tide measurements (varies with conditions)
- 💡 System performance snapshots (triggered by thresholds)

**Visualization Approaches:**

**Step Plot (No Interpolation)**:
```python
# Irregular maintenance logs
maintenance = pd.DataFrame({
    'Date': pd.to_datetime(['2024-01-05', '2024-01-12', '2024-01-28', 
                            '2024-02-15', '2024-02-18', '2024-03-10']),
    'Hours': [2.5, 4.0, 1.5, 3.5, 5.0, 2.0]
})

plt.figure(figsize=(12, 5))
plt.step(maintenance['Date'], maintenance['Hours'], 
         where='post', linewidth=2, color='steelblue', label='Maintenance Hours')
plt.scatter(maintenance['Date'], maintenance['Hours'], 
            s=80, color='darkblue', zorder=5)
plt.xlabel('Date', fontsize=11)
plt.ylabel('Maintenance Hours', fontsize=11)
plt.title('Irregular Maintenance Schedule (Step Plot)', 
          fontsize=13, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Markers with Lines (Show Data Points)**:
```python
plt.figure(figsize=(12, 5))
plt.plot(maintenance['Date'], maintenance['Hours'], 
         marker='o', markersize=8, linestyle='-', linewidth=1.5,
         color='steelblue', markerfacecolor='darkblue')
plt.xlabel('Date', fontsize=11)
plt.ylabel('Maintenance Hours', fontsize=11)
plt.title('Irregular Maintenance Schedule (Interpolated)', 
          fontsize=13, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**When to use**: Medical records, maintenance logs, survey data

---

**Choosing the Right Visualization Based on Data Type:**

| Data Type | Best Visualizations | When to Use |
|-----------|-------------------|-------------|
| **Time Points** | Event plot, scatter, histogram | Transaction logs, events, incidents |
| **Time Intervals** | Gantt chart, timeline bars | Project management, resource allocation |
| **Regular Time Series** | Line chart, area chart | Business metrics, continuous monitoring |
| **Irregular Time Series** | Step plot, markers + lines | Medical data, sporadic measurements |

**Key Decision Factors:**

1. **Frequency of Data**:
   - High frequency (seconds, minutes) → Line chart, aggregation
   - Low frequency (yearly) → Bar chart, markers

2. **Purpose of Analysis**:
   - Trends → Line chart
   - Events → Event plot, timeline
   - Comparisons → Multiple lines, small multiples
   - Composition → Stacked area, stream graph

3. **Audience**:
   - Technical → Can handle complexity, irregular data
   - Executive → Need simple, clean trends

4. **Duration vs. Magnitude**:
   - Duration matters → Gantt, timeline bars
   - Magnitude matters → Line, area charts

**Pro Tip**: When in doubt, start with a simple line chart for regular time series. It's the most versatile and widely understood temporal visualization.

---

## Basic Time Series Plot: The Line Chart

**The line chart is the foundation of temporal visualization**

**Why line charts work for time series:**

1. **Shows Continuity** - Lines connect data points, showing flow over time
2. **Preserves Order** - Left-to-right reading matches temporal progression
3. **Natural Mental Model** - We intuitively understand time flowing horizontally
4. **Scales Well** - Works from minutes to decades
5. **Easy Comparison** - Multiple lines enable series comparison

**Core Design Principles:**

**1. Time on X-Axis (Horizontal)**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=180, freq='D')
revenue = 100000 + np.cumsum(np.random.randn(180) * 5000)

# Correct orientation
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(dates, revenue, linewidth=2, color='steelblue')
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Revenue ($)', fontsize=12)
ax.set_title('Daily Revenue - First Half 2024', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Why horizontal?**
- ✅ Matches reading direction (left to right in most cultures)
- ✅ More screen/page width available than height
- ✅ Multiple series stack vertically for comparison
- ❌ Vertical time axis is confusing and non-standard

**2. Choose Appropriate Line Style**

```python
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Solid line (most common)
axes[0,0].plot(dates, revenue, linewidth=2, color='steelblue')
axes[0,0].set_title('Solid Line - Standard Choice', fontweight='bold')
axes[0,0].grid(True, alpha=0.3)

# Line with markers (when you want to emphasize data points)
axes[0,1].plot(dates[::7], revenue[::7], marker='o', markersize=5, 
               linewidth=2, color='steelblue')
axes[0,1].set_title('Line + Markers - Weekly Data', fontweight='bold')
axes[0,1].grid(True, alpha=0.3)

# Dashed line (for forecasts or secondary data)
axes[1,0].plot(dates, revenue, linewidth=2, color='steelblue', label='Actual')
forecast_dates = pd.date_range('2024-06-29', periods=30, freq='D')
forecast_values = revenue.iloc[-1] + np.cumsum(np.random.randn(30) * 5000)
axes[1,0].plot(forecast_dates, forecast_values, linewidth=2, 
               linestyle='--', color='coral', label='Forecast')
axes[1,0].set_title('Dashed Line - Forecast', fontweight='bold')
axes[1,0].legend()
axes[1,0].grid(True, alpha=0.3)

# Multiple series
product_a = revenue
product_b = revenue * 0.8 + np.random.randn(180) * 3000
axes[1,1].plot(dates, product_a, linewidth=2, color='steelblue', label='Product A')
axes[1,1].plot(dates, product_b, linewidth=2, color='coral', label='Product B')
axes[1,1].set_title('Multiple Series Comparison', fontweight='bold')
axes[1,1].legend()
axes[1,1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**Line Style Guidelines:**

| Style | Use Case | When to Use |
|-------|----------|-------------|
| **Solid** | Actual data | Default choice, historical data |
| **Dashed** | Projected/forecast | Future predictions, estimates |
| **Dotted** | Reference/benchmark | Targets, averages, goals |
| **Markers only** | Sparse data | Quarterly, annual data |
| **Line + markers** | Emphasis on points | Weekly, monthly with data points |

**3. Line Width Matters**

```python
fig, ax = plt.subplots(figsize=(12, 5))

# Too thin (hard to see)
ax.plot(dates, revenue * 0.7, linewidth=0.5, color='gray', 
        alpha=0.5, label='Too thin (0.5)')

# Good (clear and visible)
ax.plot(dates, revenue, linewidth=2, color='steelblue', label='Good (2.0)')

# Too thick (cluttered)
ax.plot(dates, revenue * 1.3, linewidth=6, color='coral', 
        alpha=0.7, label='Too thick (6.0)')

ax.set_xlabel('Date', fontsize=11)
ax.set_ylabel('Revenue ($)', fontsize=11)
ax.set_title('Line Width Comparison', fontsize=13, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Recommended line widths:**
- **1.5-2.5**: Standard for most plots
- **1.0-1.5**: Multiple series (4+) to reduce clutter
- **3.0+**: Emphasis on single important series
- **0.5-1.0**: Background/reference lines

**4. Consistent Time Intervals**

```python
# WRONG: Gaps create misleading visual
dates_with_gaps = dates[::5]  # Every 5th day
values_with_gaps = revenue[::5]

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Misleading (line interpolates over gaps)
axes[0].plot(dates_with_gaps, values_with_gaps, linewidth=2, 
             color='coral', marker='o', markersize=4)
axes[0].set_title('❌ WRONG: Gaps Not Shown', fontweight='bold', color='red')
axes[0].set_xlabel('Date')
axes[0].set_ylabel('Revenue ($)')
axes[0].grid(True, alpha=0.3)

# Correct (fill gaps or use markers)
axes[1].plot(dates_with_gaps, values_with_gaps, linewidth=0, 
             marker='o', markersize=6, color='steelblue')
axes[1].set_title('✅ CORRECT: Gaps Visible', fontweight='bold', color='green')
axes[1].set_xlabel('Date')
axes[1].set_ylabel('Revenue ($)')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**Rule**: If data has irregular intervals, either:
- Use markers only (no line)
- Use step plot
- Explicitly fill gaps and mark interpolated regions

**5. Aspect Ratio: "Banking to 45 Degrees"**

**Cleveland's Banking Principle**: Choose aspect ratio so average line slope is ~45°

**Why?** Human perception best detects changes at 45° angles.

```python
# Same data, different aspect ratios
fig, axes = plt.subplots(1, 3, figsize=(16, 4))

# Too wide (slopes look flat)
axes[0].plot(dates, revenue, linewidth=2, color='steelblue')
axes[0].set_title('Too Wide - Slopes Look Flat', fontweight='bold')
axes[0].set_xlabel('Date')
axes[0].set_ylabel('Revenue ($)')

# Good (45° banking)
axes[1].plot(dates, revenue, linewidth=2, color='steelblue')
axes[1].set_title('✅ Good Aspect Ratio', fontweight='bold', color='green')
axes[1].set_xlabel('Date')
axes[1].set_ylabel('Revenue ($)')
axes[1].set_aspect('auto')

# Too tall (slopes look steep)
axes[2].plot(dates, revenue, linewidth=2, color='steelblue')
axes[2].set_title('Too Tall - Slopes Look Steep', fontweight='bold')
axes[2].set_xlabel('Date')
axes[2].set_ylabel('Revenue ($)')

# Adjust individual subplot sizes
axes[0].set_box_aspect(0.2)
axes[1].set_box_aspect(0.5)
axes[2].set_box_aspect(1.2)

plt.tight_layout()
plt.show()
```

**General guidelines:**
- **Width:Height ratio** of 2:1 to 3:1 works for most time series
- Adjust based on data range and trend magnitude
- More data points → wider chart
- Steeper trends → taller chart

**Summary: Line Chart Best Practices**

✅ **DO:**
- Put time on x-axis (horizontal)
- Use appropriate line width (1.5-2.5)
- Choose aspect ratio to show patterns clearly
- Use consistent time intervals
- Add grid for easier reading
- Label axes clearly with units

❌ **DON'T:**
- Put time on y-axis (vertical)
- Use 3D effects
- Connect non-adjacent time points over gaps
- Use rainbow colors for single series
- Clutter with too many decorations
- Forget to show time units

---

## Choosing Appropriate Time Scales

**Time granularity dramatically affects what patterns you see**

**The Problem: Resolution vs. Noise**

```
Too granular    → See noise, miss patterns
Too coarse      → Miss important variations
Just right      → Patterns clear, noise manageable
```

**Example: Daily Sales Data**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate 2 years of daily sales with weekly and seasonal patterns
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=730, freq='D')
trend = np.linspace(50000, 70000, 730)
weekly = 3000 * np.sin(np.arange(730) * 2 * np.pi / 7)  # Weekly pattern
seasonal = 8000 * np.sin(np.arange(730) * 2 * np.pi / 365)  # Yearly pattern
noise = np.random.normal(0, 2000, 730)
daily_sales = trend + weekly + seasonal + noise

df = pd.DataFrame({'Date': dates, 'Sales': daily_sales})

# Create different aggregations
weekly_sales = df.set_index('Date').resample('W').sum()
monthly_sales = df.set_index('Date').resample('M').sum()
quarterly_sales = df.set_index('Date').resample('Q').sum()

# Visualize at different scales
fig, axes = plt.subplots(4, 1, figsize=(14, 12))

# Daily (too granular - noisy)
axes[0].plot(df['Date'], df['Sales'], linewidth=1, color='steelblue', alpha=0.6)
axes[0].set_title('Daily Sales - TOO GRANULAR (Noisy)', 
                  fontsize=12, fontweight='bold', color='coral')
axes[0].set_ylabel('Sales ($)')
axes[0].grid(True, alpha=0.3)

# Weekly (good for short-term patterns)
axes[1].plot(weekly_sales.index, weekly_sales['Sales'], 
             linewidth=2, color='steelblue', marker='o', markersize=3)
axes[1].set_title('Weekly Sales - GOOD for Short-Term Trends', 
                  fontsize=12, fontweight='bold', color='green')
axes[1].set_ylabel('Sales ($)')
axes[1].grid(True, alpha=0.3)

# Monthly (good for seasonal patterns)
axes[2].plot(monthly_sales.index, monthly_sales['Sales'], 
             linewidth=2, color='steelblue', marker='o', markersize=5)
axes[2].set_title('Monthly Sales - GOOD for Seasonal Patterns', 
                  fontsize=12, fontweight='bold', color='green')
axes[2].set_ylabel('Sales ($)')
axes[2].grid(True, alpha=0.3)

# Quarterly (too coarse - misses monthly variations)
axes[3].plot(quarterly_sales.index, quarterly_sales['Sales'], 
             linewidth=2, color='steelblue', marker='o', markersize=7)
axes[3].set_title('Quarterly Sales - TOO COARSE (Misses Detail)', 
                  fontsize=12, fontweight='bold', color='coral')
axes[3].set_ylabel('Sales ($)')
axes[3].set_xlabel('Date')
axes[3].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**Choosing the Right Time Scale:**

**1. Match to Business Question**

| Question | Appropriate Scale |
|----------|------------------|
| "What's our monthly revenue trend?" | Monthly aggregation |
| "Are there weekly patterns in traffic?" | Daily data, weekly comparison |
| "How did we perform this quarter?" | Quarterly or monthly |
| "When did the server crash?" | Minute or second-level data |
| "What's our annual growth rate?" | Yearly data |

**2. Match to Data Frequency**

```python
# Rule of thumb: Show enough points to see pattern, not so many that it's cluttered

# High-frequency data (seconds, minutes)
# → Aggregate to hours or days for visualization

# Medium-frequency (daily)
# → Show as-is, or aggregate to weekly/monthly

# Low-frequency (monthly, quarterly)
# → Show as-is, use markers to emphasize points
```

**3. Consider the Pattern Timeframe**

```
Pattern Type          | Minimum Data Needed | Recommended Scale
---------------------|---------------------|-------------------
Daily patterns       | 1-2 weeks           | Hourly or daily
Weekly cycles        | 4-8 weeks           | Daily
Monthly seasonality  | 12-24 months        | Daily or weekly  
Quarterly patterns   | 2-4 years           | Monthly
Annual trends        | 3-10 years          | Monthly or quarterly
```

**4. Audience Considerations**

**Executive dashboards:**
- Prefer monthly/quarterly views
- Want clear trends, not daily noise
- Need simple, clean visualizations

**Analyst dashboards:**
- Want daily/weekly granularity
- Need to drill down to details
- Can handle more complex visuals

**Operational dashboards:**
- Need hourly/daily real-time data
- Focus on recent periods
- Require quick anomaly detection

**Multi-Scale Approach: The Solution**

**Best practice**: Provide multiple views at different scales

```python
fig = plt.figure(figsize=(14, 10))
gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

# Overview: Full 2 years (monthly)
ax1 = fig.add_subplot(gs[0, :])
ax1.plot(monthly_sales.index, monthly_sales['Sales'], 
         linewidth=2.5, color='steelblue', marker='o', markersize=5)
ax1.set_title('Overview: 2-Year Monthly Sales Trend', 
              fontsize=13, fontweight='bold')
ax1.set_ylabel('Monthly Sales ($)', fontsize=11)
ax1.grid(True, alpha=0.3)

# Zoom 1: Last 6 months (weekly)
recent_weeks = weekly_sales.loc['2024-07-01':]
ax2 = fig.add_subplot(gs[1, 0])
ax2.plot(recent_weeks.index, recent_weeks['Sales'], 
         linewidth=2, color='coral', marker='o', markersize=4)
ax2.set_title('Last 6 Months: Weekly Detail', fontsize=12, fontweight='bold')
ax2.set_ylabel('Weekly Sales ($)', fontsize=10)
ax2.grid(True, alpha=0.3)

# Zoom 2: Last month (daily)
recent_days = df[df['Date'] >= '2024-12-01']
ax3 = fig.add_subplot(gs[1, 1])
ax3.plot(recent_days['Date'], recent_days['Sales'], 
         linewidth=1.5, color='green', marker='o', markersize=3)
ax3.set_title('Last Month: Daily Detail', fontsize=12, fontweight='bold')
ax3.set_ylabel('Daily Sales ($)', fontsize=10)
ax3.grid(True, alpha=0.3)

# Comparison: Year-over-year (monthly)
monthly_2023 = monthly_sales.loc['2023']
monthly_2024 = monthly_sales.loc['2024']
ax4 = fig.add_subplot(gs[2, :])
ax4.plot(range(1, 13), monthly_2023['Sales'].values, 
         linewidth=2, color='steelblue', marker='o', label='2023')
ax4.plot(range(1, 13), monthly_2024['Sales'].values, 
         linewidth=2, color='coral', marker='o', label='2024')
ax4.set_xticks(range(1, 13))
ax4.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                     'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax4.set_title('Year-over-Year Comparison', fontsize=13, fontweight='bold')
ax4.set_ylabel('Monthly Sales ($)', fontsize=11)
ax4.set_xlabel('Month', fontsize=11)
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.show()
```

**Interactive Solution: Zoom + Filter**

For interactive dashboards, provide:
- **Range slider** - Select time window
- **Aggregation selector** - Switch between daily/weekly/monthly
- **Zoom controls** - Focus on specific periods
- **Drill-down** - Click to see finer granularity

**Pro Tips:**

1. **Start broad, drill down**
   - Show yearly/quarterly overview first
   - Provide ability to zoom into months/weeks/days

2. **Use rolling averages** to smooth noise
   ```python
   df['Sales_7d_avg'] = df['Sales'].rolling(window=7).mean()
   ```

3. **Show both raw and aggregated** side-by-side
   ```python
   ax.plot(dates, daily_values, alpha=0.3, label='Daily')
   ax.plot(dates, weekly_avg, linewidth=2, label='7-day average')
   ```

4. **Annotate what scale is shown**
   ```python
   ax.set_title('Weekly Average Sales (7-day rolling mean)', fontsize=13)
   ```

**Common Mistakes:**

❌ Showing 5 years of daily data (too cluttered)  
❌ Showing 1 month of annual data (not enough context)  
❌ Mixing scales without labels (confusing)  
❌ Using same scale for all audiences (one-size-fits-all doesn't work)

✅ Match scale to question and audience  
✅ Provide multiple scales when possible  
✅ Use aggregation to reduce noise  
✅ Label time units clearly

---

## Handling Missing Temporal Data

**Missing data in time series requires special attention**

**Why temporal missing data is different:**

In regular data:
- Missing values are independent
- Can use simple imputation
- Order doesn't matter

In time series:
- ❌ Gaps break continuity
- ❌ Missing values have temporal context
- ❌ Imputation affects subsequent values
- ❌ Visualization can mislead

**Types of Missing Temporal Data:**

**1. Random Gaps (Sensor Failures)**
```
Jan 1  ✓
Jan 2  ✓
Jan 3  ✗ (sensor failed)
Jan 4  ✓
Jan 5  ✓
```

**2. Systematic Gaps (Weekends, Holidays)**
```
Mon    ✓
Tue    ✓
Wed    ✓
Thu    ✓
Fri    ✓
Sat    ✗ (business closed)
Sun    ✗ (business closed)
```

**3. Extended Outages**
```
Jan 1-10   ✓✓✓✓✓✓✓✓✓✓
Jan 11-20  ✗✗✗✗✗✗✗✗✗✗ (system down)
Jan 21-30  ✓✓✓✓✓✓✓✓✓✓
```

**Visualization Strategies:**

**Strategy 1: Show Gaps Explicitly**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create time series with gaps
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=60, freq='D')
values = 100 + np.cumsum(np.random.randn(60) * 5)

# Create DataFrame
df = pd.DataFrame({'Date': dates, 'Value': values})

# Introduce random gaps
missing_indices = np.random.choice(df.index, size=10, replace=False)
df.loc[missing_indices, 'Value'] = np.nan

# Visualize
fig, axes = plt.subplots(2, 1, figsize=(14, 8))

# WRONG: Line connects over gaps (misleading)
axes[0].plot(df['Date'], df['Value'], linewidth=2, color='steelblue', marker='o')
axes[0].set_title('❌ WRONG: Line Connects Over Missing Data (Misleading)', 
                  fontsize=12, fontweight='bold', color='red')
axes[0].set_ylabel('Value')
axes[0].grid(True, alpha=0.3)

# CORRECT: Gaps shown explicitly
axes[1].plot(df['Date'], df['Value'], linewidth=0, 
             marker='o', markersize=6, color='steelblue', label='Actual Data')
# Mark missing data regions
for idx in missing_indices:
    if idx < len(df) - 1:
        axes[1].axvspan(df.loc[idx, 'Date'], df.loc[idx+1, 'Date'], 
                        alpha=0.2, color='red', label='Missing' if idx == missing_indices[0] else '')
axes[1].set_title('✅ CORRECT: Gaps Visible (Markers Only)', 
                  fontsize=12, fontweight='bold', color='green')
axes[1].set_ylabel('Value')
axes[1].set_xlabel('Date')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**When to use**: Small number of missing values, need to preserve data integrity

---

**Strategy 2: Interpolate and Distinguish**

```python
# Interpolate missing values
df['Value_interpolated'] = df['Value'].interpolate(method='linear')

# Identify interpolated regions
df['is_interpolated'] = df['Value'].isna()

fig, ax = plt.subplots(figsize=(14, 6))

# Plot actual data (solid)
actual_data = df[~df['is_interpolated']]
ax.plot(actual_data['Date'], actual_data['Value'], 
        linewidth=2.5, color='steelblue', marker='o', 
        markersize=5, label='Actual Data', zorder=3)

# Plot interpolated data (dashed, different color)
interpolated_segments = df[df['is_interpolated']]
for idx in interpolated_segments.index:
    # Find segment start and end
    start_idx = idx - 1 if idx > 0 else idx
    end_idx = idx + 1 if idx < len(df) - 1 else idx
    
    if start_idx >= 0 and end_idx < len(df):
        segment_dates = [df.loc[start_idx, 'Date'], df.loc[idx, 'Date'], df.loc[end_idx, 'Date']]
        segment_values = [df.loc[start_idx, 'Value_interpolated'], 
                         df.loc[idx, 'Value_interpolated'], 
                         df.loc[end_idx, 'Value_interpolated']]
        ax.plot(segment_dates, segment_values, 
                linewidth=2, linestyle='--', color='coral', alpha=0.7, zorder=2)

# Add legend
from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], color='steelblue', linewidth=2.5, 
                          marker='o', label='Actual Data'),
                   Line2D([0], [0], color='coral', linewidth=2, 
                          linestyle='--', label='Interpolated')]
ax.legend(handles=legend_elements, loc='upper left', fontsize=11)

ax.set_title('Interpolated Values Shown Differently', 
             fontsize=13, fontweight='bold')
ax.set_ylabel('Value', fontsize=11)
ax.set_xlabel('Date', fontsize=11)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**When to use**: Need continuous line, but must show where data is estimated

---

**Strategy 3: Remove Missing Periods (for Systematic Gaps)**

```python
# Example: Remove weekends from business data
df_business_days = df[df['Date'].dt.dayofweek < 5]  # Monday=0, Friday=4

fig, axes = plt.subplots(2, 1, figsize=(14, 8))

# With weekends (creates confusing gaps)
axes[0].plot(df['Date'], df['Value'], linewidth=2, 
             color='steelblue', marker='o', markersize=4)
axes[0].set_title('With Weekends (Systematic Gaps)', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Value')
axes[0].grid(True, alpha=0.3)

# Business days only (clean continuity)
axes[1].plot(df_business_days['Date'], df_business_days['Value'].interpolate(), 
             linewidth=2, color='steelblue', marker='o', markersize=4)
axes[1].set_title('Business Days Only (Continuous)', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Value')
axes[1].set_xlabel('Date')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**When to use**: Systematic, expected gaps (weekends, holidays, maintenance windows)

---

**Strategy 4: Shading + Annotation**

```python
fig, ax = plt.subplots(figsize=(14, 6))

# Plot data
ax.plot(df['Date'], df['Value_interpolated'], 
        linewidth=2, color='steelblue', label='Values (interpolated where missing)')

# Shade missing data regions
for idx in missing_indices:
    ax.axvline(df.loc[idx, 'Date'], color='red', 
               linestyle='--', alpha=0.3, linewidth=1)
    
# Add annotation for first missing point
first_missing = missing_indices[0]
ax.annotate('Missing Data Points', 
            xy=(df.loc[first_missing, 'Date'], df.loc[first_missing, 'Value_interpolated']),
            xytext=(df.loc[first_missing, 'Date'], df['Value_interpolated'].max()),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=10, color='red', fontweight='bold')

ax.set_title('Missing Data Indicated with Vertical Lines', 
             fontsize=13, fontweight='bold')
ax.set_ylabel('Value', fontsize=11)
ax.set_xlabel('Date', fontsize=11)
ax.legend(loc='upper left')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**When to use**: Few missing points, need to call attention to gaps

---

**Best Practices for Missing Temporal Data:**

**1. Always disclose missing data**
- ✅ Show gaps explicitly in visualization
- ✅ Add note in caption or legend
- ✅ Use different styling for interpolated values
- ❌ Never hide missing data without disclosure

**2. Choose interpolation method carefully**

```python
# Linear interpolation (simple, assumes linear change)
df['linear'] = df['Value'].interpolate(method='linear')

# Time-weighted (accounts for uneven intervals)
df['time'] = df['Value'].interpolate(method='time')

# Polynomial (smooth curve)
df['poly'] = df['Value'].interpolate(method='polynomial', order=2)

# Forward fill (use last known value)
df['ffill'] = df['Value'].fillna(method='ffill')

# Mean of surrounding values
df['mean'] = df['Value'].fillna(df['Value'].rolling(window=3, center=True).mean())
```

**3. Consider the context**

| Situation | Recommended Approach |
|-----------|---------------------|
| Financial data | Show gaps (never interpolate stock prices!) |
| Temperature | Interpolate (continuous physical process) |
| Sales transactions | Show gaps or use zero (no sale = zero) |
| Sensor readings | Interpolate, mark as estimated |
| Survey responses | Cannot interpolate (discrete events) |

**4. Report missing data statistics**

```python
# Add text box with missing data info
missing_count = df['Value'].isna().sum()
total_count = len(df)
missing_pct = (missing_count / total_count) * 100

textstr = f'Missing: {missing_count}/{total_count} ({missing_pct:.1f}%)'
ax.text(0.02, 0.98, textstr, transform=ax.transAxes, 
        fontsize=10, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
```

**Summary:**

✅ **DO:**
- Show gaps explicitly when possible
- Use different styling for interpolated vs. actual data
- Document missing data in captions
- Choose interpolation method based on data type
- Consider removing systematic gaps (weekends, etc.)

❌ **DON'T:**
- Connect lines over large gaps without notation
- Interpolate financial or discrete event data
- Hide missing data from viewers
- Use complex interpolation without justification
- Ignore the temporal context of missing values

**Remember**: In time series, how you handle missing data affects interpretation. Transparency is critical!

---


## Date/Time Formatting in Python

**Working with dates is essential for time series visualization**

**Why it matters:**
- Date formats drive axis labels and tick density
- Parsing correctly avoids missing/incorrect points
- Formatting improves readability and interpretation

---

### 1. Parsing Dates with Pandas

```python
import pandas as pd

# From CSV with date column
# df = pd.read_csv('sales.csv')
# df['Date'] = pd.to_datetime(df['Date'])

# Common formats
pd.to_datetime('2025-02-16')        # YYYY-MM-DD
pd.to_datetime('02/16/2025')        # MM/DD/YYYY
pd.to_datetime('16-Feb-2025')       # DD-Mon-YYYY
pd.to_datetime('2025-02-16 14:30')  # With time
```

**Tip:** Always parse date columns immediately after loading data.

---

### 2. Setting Date as Index

```python
# Set date as index for time series operations

df = df.sort_values('Date')
df = df.set_index('Date')
```

This enables:
- Resampling (`.resample()`)
- Rolling windows (`.rolling()`)
- Time slicing (`df['2025-01':'2025-06']`)

---

### 3. Date Formatting for Plots

```python
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(df.index, df['Sales'])

# Format x-axis
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

**Readable formats:**
- `%b %Y` → “Feb 2025”
- `%d-%b` → “16-Feb”
- `%Y-%m-%d` → “2025-02-16”

---

## Time Zones and DST Issues

**Time zones can quietly break your analysis**

### Common Problems:
- Data recorded in UTC but plotted in local time
- Daylight Savings Time (DST) creates duplicate or missing hours
- Mixed time zones in a dataset

---

### Example: Converting Time Zones

```python
# Parse as UTC then convert

df['timestamp'] = pd.to_datetime(df['timestamp'], utc=True)
df['timestamp_local'] = df['timestamp'].dt.tz_convert('America/Chicago')
```

### Handling DST

```python
# Remove ambiguous times

df = df[~df.index.isnull()]
```

**Best Practice:** Always store timestamps in UTC and convert for visualization.

---

## Aspect Ratio and Chart Proportions

**Aspect ratio changes how trends are perceived**

### Problem:
- Too wide → trends look flat
- Too tall → trends look extreme

### Guideline:
**Use "banking to 45°"** (Cleveland, 1984)
- Average slopes should be near 45° for best perception

---

### Example

```python
fig, ax = plt.subplots(figsize=(10, 4))  # 2.5:1 ratio
ax.plot(df.index, df['Sales'])
ax.set_title('Balanced aspect ratio')
```

**Rule of thumb:**
- 2:1 or 3:1 width:height for most time series

---

## Color in Time Series

**Color can encode additional dimensions, but use carefully**

### Best Practices:
✅ Use distinct colors for multiple series  
✅ Use muted colors for reference lines  
✅ Highlight key events with a single accent color  
❌ Avoid rainbow scales for time series lines  

---

### Example: Highlighting a Segment

```python
ax.plot(df.index, df['Sales'], color='gray')
ax.plot(df.index['2025-06':'2025-08'], df['Sales']['2025-06':'2025-08'],
        color='red', linewidth=2, label='Summer spike')
ax.legend()
```

---

## Multiple Time Series on One Plot

**Good for comparison, but can quickly become cluttered**

### Guidelines:
- Limit to 3–5 series per chart
- Use consistent scales
- Label lines directly if possible

---

### Example: Multiple Products

```python
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(df.index, df['ProductA'], label='Product A')
ax.plot(df.index, df['ProductB'], label='Product B')
ax.plot(df.index, df['ProductC'], label='Product C')
ax.legend()
ax.set_title('Sales by Product')
```

**Alternative:** Use small multiples if too many series.

---

## Small Multiples for Time Series

**Small multiples reduce clutter and improve comparison**

Instead of stacking many lines on one plot, separate into panels:

✅ Easier to compare patterns  
✅ Same scale = fair comparison  
✅ Reduces visual overload  

---

### Example: Faceted Time Series

```python
import seaborn as sns

sns.relplot(
    data=df,
    x='Date', y='Sales',
    col='Region', col_wrap=3,
    kind='line', height=3
)
```

---

## Common Temporal Visualization Mistakes

**Avoid these frequent errors:**

❌ Misaligned time scales across charts  
❌ Truncated axes that exaggerate trends  
❌ Too many series on one plot  
❌ Irregular gaps hidden by lines  
❌ Over-annotating every data point  

---

## Y-Axis Decisions

**Should time series start at zero?**

- **Yes** for absolute magnitude (e.g., revenue)
- **No** when showing percent change or deviation

```python
ax.set_ylim(0, None)   # force zero baseline
```

---

## Annotation Best Practices

Use annotations sparingly to emphasize:
- Key events
- Outliers
- Structural breaks

```python
ax.annotate('Policy Change', xy=(date, value), xytext=(date, value+10),
            arrowprops=dict(arrowstyle='->'))
```

---

## Reference Lines and Benchmarks

Add context with:
- Average line
- Target threshold
- Historical benchmark

```python
ax.axhline(df['Sales'].mean(), color='red', linestyle='--', label='Average')
```

---

## Interactive vs. Static Time Series

**Static plots** are good for reports.  
**Interactive plots** are better for exploration.

Interactive features:
- Zoom/pan
- Hover tooltips
- Range sliders

---

# ═══════════════════════════════════════════════════════════════
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

Smooth short-term noise.

```python
df['MA_7'] = df['Sales'].rolling(7).mean()
```

---

## Exponential Smoothing

Recent data weighted more heavily.

---

## Rolling Statistics

Track rolling mean, std for stability checks.

---

## Seasonal Adjustment

Remove seasonal component to reveal trend.

---

## Detrending

Subtract trend to analyze cyclical/seasonal behavior.

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

# ═══════════════════════════════════════════════════════════════
# PART 3: ADVANCED TIME SERIES TECHNIQUES
# Slides 41-60
# ═══════════════════════════════════════════════════════════════

## Comparing Multiple Time Series

Compare series with consistent scales and aligned timelines.

---

## Index-Based Comparisons

Normalize all series to 100 at start:

```python
indexed = df / df.iloc[0] * 100
```

---

## Percent Change Visualization

```python
df.pct_change().plot()
```

---

## Lag Plots

Visualize autocorrelation:

```python
pd.plotting.lag_plot(df['Sales'], lag=1)
```

---

## Autocorrelation Function (ACF)

```python
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(df['Sales'], lags=30)
```

---

## Partial Autocorrelation (PACF)

```python
from statsmodels.graphics.tsaplots import plot_pacf
plot_pacf(df['Sales'], lags=30)
```

---

## Cross-Correlation

Measure relationship between two time series.

---

## Lead-Lag Relationships

Does one series predict another?

---

## Forecasting Visualization Principles

Show:
- Historical data
- Forecast horizon
- Uncertainty band

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
- statsmodels
- prophet
- plotly

---

## pandas DateTime Operations

Resampling, shifting, rolling windows.

---

## Matplotlib Time Series

Date locators and formatters.

---

## Seaborn for Temporal Data

Relational plots and facets.

---

## Plotly Interactive Time Series

Range sliders and hover tooltips.

---

## Facebook Prophet

Automated forecasting with uncertainty.

---

## statsmodels Decomposition

STL and seasonal_decompose.

---

## Real-World Case Study 1

Retail sales seasonality analysis.

---

## Real-World Case Study 2

Stock price volatility visualization.

---

## Real-World Case Study 3

Sensor monitoring and anomaly alerts.

---

## Dashboard Design for Temporal Data

- Consistent scales
- Clear hierarchy
- Progressive detail

---

## Multi-Scale Dashboards

Overview + drill-down views.

---

## Best Practices Checklist

✅ Clear time axis  
✅ Minimal clutter  
✅ Annotate key events

---

## Exercise 1: Identify Temporal Patterns

Given a time series, identify trend, seasonality, and noise.

---

## Exercise 2: Choose the Right Time Scale

Match granularity to a given business question.

---

## Exercise 3: Time Series Decomposition

Use STL decomposition in Python.

---

## Exercise 4: Forecasting Visualization

Create forecasts with confidence bands.

---

## Exercise 5: Interactive Dashboard

Build an interactive plotly dashboard.

---

## Assignment & Resources

Build a full EDA + forecast report.

---

## Summary & Next Class Preview

Next: Advanced storytelling with time series.

---
