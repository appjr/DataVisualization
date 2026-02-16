**2. Time Intervals (Spans/Durations)**

**Definition**: Events with start and end times (duration matters)

**Characteristics:**
- Start time + end time
- Duration is meaningful
- May overlap

**Examples:**
- 🏥 Hospital patient stays (admitted 2024-01-10, discharged 2024-01-15)
- 🏭 Manufacturing batch production (started 08:00, finished 14:30)
- ✈️ Flight durations (departure to arrival)
- 🔧 System maintenance windows
- 📞 Phone call durations
- 🎬 Video viewing sessions

**Visualization Approaches:**

**Gantt Chart**:
```python
import matplotlib.pyplot as plt
import pandas as pd

# Sample data: project tasks
tasks = pd.DataFrame({
    'Task': ['Design', 'Development', 'Testing', 'Deployment'],
    'Start': pd.to_datetime(['2024-01-01', '2024-01-15', '2024-02-15', '2024-03-01']),
    'End': pd.to_datetime(['2024-01-20', '2024-02-20', '2024-03-05', '2024-03-10'])
})

fig, ax = plt.subplots(figsize=(12, 5))

for idx, row in tasks.iterrows():
    ax.barh(idx, (row['End'] - row['Start']).days, 
            left=row['Start'], height=0.5, 
            color='steelblue', alpha=0.8)
    ax.text(row['Start'], idx, f"  {row['Task']}", 
            va='center', fontsize=10, fontweight='bold')

ax.set_yticks(range(len(tasks)))
ax.set_yticklabels([])
ax.set_xlabel('Date', fontsize=11)
ax.set_title('Project Timeline (Gantt Chart)', fontsize=13, fontweight='bold')
ax.grid(True, axis='x', alpha=0.3)
plt.tight_layout()
plt.show()
```

**Timeline with Bars**:
```python
# Hospital bed occupancy
occupancy = pd.DataFrame({
    'Patient': ['A', 'B', 'C', 'D'],
    'Admitted': pd.to_datetime(['2024-01-01', '2024-01-03', '2024-01-05', '2024-01-06']),
    'Discharged': pd.to_datetime(['2024-01-08', '2024-01-12', '2024-01-09', '2024-01-14'])
})

fig, ax = plt.subplots(figsize=(12, 4))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

for idx, row in occupancy.iterrows():
    duration = (row['Discharged'] - row['Admitted']).days
    ax.barh(idx, duration, left=row['Admitted'], 
            height=0.6, color=colors[idx], alpha=0.7,
            label=f"Patient {row['Patient']}")

ax.set_yticks(range(len(occupancy)))
ax.set_yticklabels([f"Patient {p}" for p in occupancy['Patient']])
ax.set_xlabel('Date', fontsize=11)
ax.set_title('Hospital Bed Occupancy', fontsize=13, fontweight='bold')
ax.legend(loc='upper right')
ax.grid(True, axis='x', alpha=0.3)
plt.tight_layout()
plt.show()
```

**When to use**: Project management, resource scheduling, session analysis