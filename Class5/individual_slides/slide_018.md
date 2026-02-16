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