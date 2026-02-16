## Y-Axis Decisions

**Should time series start at zero?**

- **Yes** for absolute magnitude (e.g., revenue)
- **No** when showing percent change or deviation

```python
ax.set_ylim(0, None)   # force zero baseline
```