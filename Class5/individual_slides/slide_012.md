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