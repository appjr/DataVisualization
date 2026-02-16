### Example: Converting Time Zones

```python
# Parse as UTC then convert

df['timestamp'] = pd.to_datetime(df['timestamp'], utc=True)
df['timestamp_local'] = df['timestamp'].dt.tz_convert('America/Chicago')
```

### Handling DST

```python
# Remove ambiguous times

df = df[~df.index.isnull()]
```

**Best Practice:** Always store timestamps in UTC and convert for visualization.