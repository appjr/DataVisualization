## Types of Temporal Data

**Understanding your temporal data type guides visualization choice:**

**1. Time Points (Discrete Events)**

**Definition**: Events occurring at specific moments in time

**Characteristics:**
- Precise timestamps
- No duration
- Count-based analysis

**Examples:**
- 🛒 Customer purchases (2024-01-15 14:32:18)
- 🌍 Earthquakes (magnitude 5.2 at 2024-02-10 03:15:42)
- 🐦 Social media posts (tweet at 2024-03-05 09:22:15)
- 📧 Email arrivals
- 🔔 System alerts
- 🏃 Race finish times

**Visualization Approaches:**

**Event Plot (Rug Plot)**:
```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate random event times
np.random.seed(42)
events = pd.to_datetime('2024-01-01') + pd.to_timedelta(
    np.random.exponential(scale=2, size=100), unit='D'
)

fig, ax = plt.subplots(figsize=(12, 2))
ax.eventplot(events, lineoffsets=0.5, linelengths=0.8, color='steelblue')
ax.set_xlabel('Date', fontsize=11)
ax.set_title('Customer Purchase Events', fontsize=13, fontweight='bold')
ax.set_yticks([])
plt.tight_layout()
plt.show()
```

**Timeline (Scatter)**:
```python
# Count events per day
daily_counts = events.value_counts().sort_index()

plt.figure(figsize=(12, 5))
plt.plot(daily_counts.index, daily_counts.values, marker='o', 
         linestyle='-', linewidth=1, markersize=4)
plt.xlabel('Date', fontsize=11)
plt.ylabel('Number of Events', fontsize=11)
plt.title('Daily Event Frequency', fontsize=13, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**When to use**: Transaction data, log files, event streams