# Class 5 – Advanced Techniques

[← Main](Class5.md) | [Part 1](Class5_Part1.md) | [Part 2](Class5_Part2.md) | [Part 3](Class5_Part3.md) | [Part 4](Class5_Part4.md)

---

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
