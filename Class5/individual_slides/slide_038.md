## Identifying Trends

A **trend** is the overall direction of change.

```python
# Simple linear trend
sns.lineplot(data=df, x='Date', y='Sales')
```

Add trend line:

```python
sns.regplot(x=np.arange(len(df)), y=df['Sales'], scatter=False)
```