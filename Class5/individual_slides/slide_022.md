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