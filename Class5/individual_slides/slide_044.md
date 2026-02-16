## Classical Decomposition Method

```python
from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(df['Sales'], model='additive', period=12)
```