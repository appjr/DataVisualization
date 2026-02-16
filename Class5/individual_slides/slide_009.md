**3. Regular Time Series (Fixed Intervals)**

**Definition**: Measurements at consistent, regular intervals

**Characteristics:**
- Fixed frequency (hourly, daily, monthly)
- Continuous monitoring
- Most common type

**Examples:**
- 📊 Daily stock closing prices
- 🌡️ Hourly temperature readings
- 💰 Monthly sales figures
- 📈 Quarterly GDP
- ⚡ Minute-by-minute power consumption
- 🌐 Weekly website visitors

**Visualization Approaches:**

**Line Chart (Most Common)**:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate sample daily sales data with trend and seasonality
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=365, freq='D')
trend = np.linspace(50000, 65000, 365)
seasonal = 5000 * np.sin(np.arange(365) * 2 * np.pi / 365)
noise = np.random.normal(0, 2000, 365)
sales = trend + seasonal + noise

plt.figure(figsize=(14, 6))
plt.plot(dates, sales, linewidth=1.5, color='steelblue', label='Daily Sales')
plt.xlabel('Date', fontsize=11)
plt.ylabel('Sales ($)', fontsize=11)
plt.title('Daily Sales - 2023 (Regular Time Series)', 
          fontsize=13, fontweight='bold')
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Area Chart (Emphasizes Volume)**:
```python
plt.figure(figsize=(14, 6))
plt.fill_between(dates, sales, alpha=0.3, color='steelblue', label='Daily Sales')
plt.plot(dates, sales, linewidth=1.5, color='steelblue')
plt.xlabel('Date', fontsize=11)
plt.ylabel('Sales ($)', fontsize=11)
plt.title('Daily Sales with Area Fill', fontsize=13, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**When to use**: Continuous monitoring data, business metrics, sensor data