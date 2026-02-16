**4. Irregular Time Series (Variable Intervals)**

**Definition**: Measurements at non-uniform, irregular intervals

**Characteristics:**
- Variable time gaps
- Event-driven sampling
- Requires interpolation decisions

**Examples:**
- 🏥 Medical checkups (as needed, not scheduled)
- 🔧 Equipment maintenance logs (when problems occur)
- 🎯 Survey responses (voluntary participation)
- 📝 Customer feedback (sporadic)
- 🌊 Tide measurements (varies with conditions)
- 💡 System performance snapshots (triggered by thresholds)

**Visualization Approaches:**

**Step Plot (No Interpolation)**:
```python
# Irregular maintenance logs
maintenance = pd.DataFrame({
    'Date': pd.to_datetime(['2024-01-05', '2024-01-12', '2024-01-28', 
                            '2024-02-15', '2024-02-18', '2024-03-10']),
    'Hours': [2.5, 4.0, 1.5, 3.5, 5.0, 2.0]
})

plt.figure(figsize=(12, 5))
plt.step(maintenance['Date'], maintenance['Hours'], 
         where='post', linewidth=2, color='steelblue', label='Maintenance Hours')
plt.scatter(maintenance['Date'], maintenance['Hours'], 
            s=80, color='darkblue', zorder=5)
plt.xlabel('Date', fontsize=11)
plt.ylabel('Maintenance Hours', fontsize=11)
plt.title('Irregular Maintenance Schedule (Step Plot)', 
          fontsize=13, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**Markers with Lines (Show Data Points)**:
```python
plt.figure(figsize=(12, 5))
plt.plot(maintenance['Date'], maintenance['Hours'], 
         marker='o', markersize=8, linestyle='-', linewidth=1.5,
         color='steelblue', markerfacecolor='darkblue')
plt.xlabel('Date', fontsize=11)
plt.ylabel('Maintenance Hours', fontsize=11)
plt.title('Irregular Maintenance Schedule (Interpolated)', 
          fontsize=13, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**When to use**: Medical records, maintenance logs, survey data