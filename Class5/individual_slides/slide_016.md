**Strategy 3: Remove Missing Periods (for Systematic Gaps)**

```python
# Example: Remove weekends from business data
df_business_days = df[df['Date'].dt.dayofweek < 5]  # Monday=0, Friday=4

fig, axes = plt.subplots(2, 1, figsize=(14, 8))

# With weekends (creates confusing gaps)
axes[0].plot(df['Date'], df['Value'], linewidth=2, 
             color='steelblue', marker='o', markersize=4)
axes[0].set_title('With Weekends (Systematic Gaps)', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Value')
axes[0].grid(True, alpha=0.3)

# Business days only (clean continuity)
axes[1].plot(df_business_days['Date'], df_business_days['Value'].interpolate(), 
             linewidth=2, color='steelblue', marker='o', markersize=4)
axes[1].set_title('Business Days Only (Continuous)', fontsize=12, fontweight='bold')
axes[1].set_ylabel('Value')
axes[1].set_xlabel('Date')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**When to use**: Systematic, expected gaps (weekends, holidays, maintenance windows)