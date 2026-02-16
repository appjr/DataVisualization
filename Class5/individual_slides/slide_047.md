## Moving Averages

Smooth short-term noise.

```python
df['MA_7'] = df['Sales'].rolling(7).mean()
```