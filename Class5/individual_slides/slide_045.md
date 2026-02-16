## STL Decomposition

STL handles complex seasonality better.

```python
from statsmodels.tsa.seasonal import STL
stl = STL(df['Sales'], period=12)
res = stl.fit()
```