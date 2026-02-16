### Example: Faceted Time Series

```python
import seaborn as sns

sns.relplot(
    data=df,
    x='Date', y='Sales',
    col='Region', col_wrap=3,
    kind='line', height=3
)
```