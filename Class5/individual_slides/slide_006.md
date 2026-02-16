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