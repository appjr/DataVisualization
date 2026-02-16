### Example

```python
fig, ax = plt.subplots(figsize=(10, 4))  # 2.5:1 ratio
ax.plot(df.index, df['Sales'])
ax.set_title('Balanced aspect ratio')
```

**Rule of thumb:**
- 2:1 or 3:1 width:height for most time series