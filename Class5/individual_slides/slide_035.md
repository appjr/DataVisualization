## Annotation Best Practices

Use annotations sparingly to emphasize:
- Key events
- Outliers
- Structural breaks

```python
ax.annotate('Policy Change', xy=(date, value), xytext=(date, value+10),
            arrowprops=dict(arrowstyle='->'))
```