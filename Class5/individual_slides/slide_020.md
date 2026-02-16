### 1. Parsing Dates with Pandas

```python
import pandas as pd

# From CSV with date column
# df = pd.read_csv('sales.csv')
# df['Date'] = pd.to_datetime(df['Date'])

# Common formats
pd.to_datetime('2025-02-16')        # YYYY-MM-DD
pd.to_datetime('02/16/2025')        # MM/DD/YYYY
pd.to_datetime('16-Feb-2025')       # DD-Mon-YYYY
pd.to_datetime('2025-02-16 14:30')  # With time
```

**Tip:** Always parse date columns immediately after loading data.