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