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