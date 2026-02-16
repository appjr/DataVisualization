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