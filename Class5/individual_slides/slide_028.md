### Example: Highlighting a Segment

```python
ax.plot(df.index, df['Sales'], color='gray')
ax.plot(df.index['2025-06':'2025-08'], df['Sales']['2025-06':'2025-08'],
        color='red', linewidth=2, label='Summer spike')
ax.legend()
```