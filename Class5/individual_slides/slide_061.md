## Partial Autocorrelation (PACF)

```python
from statsmodels.graphics.tsaplots import plot_pacf
plot_pacf(df['Sales'], lags=30)
```