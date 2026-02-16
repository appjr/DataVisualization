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