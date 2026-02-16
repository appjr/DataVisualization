## Index-Based Comparisons

Normalize all series to 100 at start:

```python
indexed = df / df.iloc[0] * 100
```