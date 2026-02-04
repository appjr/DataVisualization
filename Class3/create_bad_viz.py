"""
Create a deliberately BAD visualization for Exercise 1: Critique This Visualization

This visualization intentionally violates multiple perception and cognitive load principles:
- 3D pie chart (poor encoding)
- Rainbow colors (perceptually non-uniform)
- Too many slices (hard to compare angles)
- Gratuitous gradients
- Poor labeling
- Chart junk
- No clear hierarchy
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
import matplotlib.patches as mpatches

print("Creating intentionally BAD visualization for Exercise 1...")

# Create figure with busy background
fig = plt.figure(figsize=(12, 8), facecolor='#E8F4F8')
ax = fig.add_subplot(111)

# Add decorative background pattern (chart junk)
for i in range(20):
    for j in range(15):
        circle = Circle((i*0.6, j*0.6), 0.1, color='lightblue', alpha=0.1)
        ax.add_patch(circle)

# Bad pie chart data with too many slices
categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E', 
              'Product F', 'Product G', 'Product H', 'Product I', 'Product J']
values = [15, 12, 11, 10, 9, 8, 7, 6, 5, 17]

# Rainbow colors (perceptually non-uniform, creates false boundaries)
colors = ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#0000FF', 
          '#4B0082', '#9400D3', '#FF1493', '#00CED1', '#FFD700']

# Create pie chart with heavy shadow (simulates 3D, distorts perception)
ax1 = plt.subplot(2, 2, 1)
patches, texts, autotexts = ax1.pie(values, labels=categories, colors=colors, 
                                     autopct='%1.1f%%', startangle=45,
                                     shadow=True, explode=[0.1]*10)

# Add gradient effect and heavy borders (more chart junk)
for i, patch in enumerate(patches):
    patch.set_linewidth(3)
    patch.set_edgecolor('black')
    patch.set_alpha(0.7)

# Tiny, unreadable fonts
for text in texts:
    text.set_fontsize(6)
    text.set_rotation(25)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(7)

plt.title('Q4 2025 Sales Performance Dashboard Analytics Report\nMulti-Category Revenue Distribution Analysis', 
          fontsize=16, fontweight='bold', color='darkblue', 
          bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7, linewidth=3))

# Add unnecessary second visualization (dual axis nightmare)
ax2 = plt.subplot(2, 2, 2)

# Truncated y-axis (misleading)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
revenue = [98, 99, 97, 102, 101, 103]  # Small differences
costs = [50, 52, 51, 53, 54, 52]

# Use line width variations (inconsistent)
ax2.plot(months, revenue, color='red', linewidth=5, marker='*', 
         markersize=20, label='Revenue ($K)', linestyle='--')
ax2.set_ylim(95, 105)  # Truncated axis exaggerates differences
ax2.set_ylabel('Revenue ($K)', color='red', fontsize=14, fontweight='bold')
ax2.tick_params(axis='y', labelcolor='red')
ax2.grid(True, linewidth=2, color='purple', linestyle='-.', alpha=0.5)

# Dual axis (misleading comparison)
ax2_twin = ax2.twinx()
ax2_twin.plot(months, costs, color='green', linewidth=2, marker='D', 
              markersize=15, label='Costs ($K)')
ax2_twin.set_ylim(40, 60)  # Different scale!
ax2_twin.set_ylabel('Costs ($K)', color='green', fontsize=14, fontweight='bold')
ax2_twin.tick_params(axis='y', labelcolor='green')

ax2.set_title('Revenue vs Cost Trend Analysis\n***IMPORTANT***', 
              fontsize=12, color='red', fontweight='bold',
              bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))
ax2.set_facecolor('#FFF5E1')

# Add busy legend
legend1 = ax2.legend(loc='upper left', fontsize=8, framealpha=0.9, 
                     facecolor='lightyellow', edgecolor='black')
legend1.get_frame().set_linewidth(2)
legend2 = ax2_twin.legend(loc='upper right', fontsize=8, framealpha=0.9,
                          facecolor='lightgreen', edgecolor='black')
legend2.get_frame().set_linewidth(2)

# Add third chart: bar chart with problems
ax3 = plt.subplot(2, 2, 3)

regions = ['North', 'South', 'East', 'West', 'Central', 'International', 'Online', 'Retail']
sales = [45, 52, 38, 61, 44, 55, 48, 50]

# Use same color for all bars (no differentiation)
# But with heavy 3D effect
bars = ax3.bar(regions, sales, color='steelblue', edgecolor='black', linewidth=2,
               alpha=0.6, width=0.8)

# Add unnecessary 3D effect with shadows
for i, bar in enumerate(bars):
    height = bar.get_height()
    # Add shadow
    shadow = mpatches.Rectangle((bar.get_x()-0.05, 0), bar.get_width(), height,
                                linewidth=0, facecolor='gray', alpha=0.3, zorder=1)
    ax3.add_patch(shadow)

# Rotated x-labels (hard to read)
ax3.set_xticklabels(regions, rotation=45, ha='right', fontsize=8)
ax3.set_ylabel('Sales Performance Metrics (K$)', fontsize=10)
ax3.set_title('Regional Sales Comparison Q4\n(Preliminary Data - Subject to Change)',
              fontsize=10, style='italic')
ax3.set_facecolor('#FFEBCD')
ax3.grid(True, axis='y', linestyle=':', linewidth=3, color='orange', alpha=0.5)

# Add value labels at weird angles
for i, (bar, val) in enumerate(zip(bars, sales)):
    ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
             f'${val}K', ha='center', va='bottom', fontsize=7,
             rotation=30, fontweight='bold', color='darkred')

# Fourth chart: confusing scatter
ax4 = plt.subplot(2, 2, 4)

# Generate random data
np.random.seed(42)
x = np.random.rand(100) * 100
y = np.random.rand(100) * 100
categories_scatter = np.random.choice(['A', 'B', 'C', 'D', 'E'], 100)

# Use many different colors and shapes (no legend)
color_map = {'A': 'red', 'B': 'blue', 'C': 'green', 'D': 'yellow', 'E': 'purple'}
marker_map = {'A': 'o', 'B': 's', 'C': '^', 'D': 'D', 'E': 'v'}

for cat in ['A', 'B', 'C', 'D', 'E']:
    mask = categories_scatter == cat
    ax4.scatter(x[mask], y[mask], c=color_map[cat], marker=marker_map[cat],
               s=np.random.rand(mask.sum())*200, alpha=0.6, edgecolors='black',
               linewidths=2)

ax4.set_xlabel('Metric 1', fontsize=8)
ax4.set_ylabel('Metric 2', fontsize=8)
ax4.set_title('Correlation Analysis\n(Confidential)', fontsize=10, color='red')
ax4.set_facecolor('#F0F8FF')
ax4.grid(True, linewidth=1, color='gray', linestyle='--', alpha=0.7)

# Add text annotations (clutter)
ax4.text(50, 90, 'Peak Region', fontsize=8, color='red', 
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))
ax4.text(10, 10, 'Low Activity', fontsize=8, color='blue',
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

# Overall figure title
fig.suptitle('COMPREHENSIVE QUARTERLY BUSINESS INTELLIGENCE DASHBOARD\n' + 
             'Generated on 2025-12-31 | Version 3.2 | FOR MANAGEMENT REVIEW ONLY',
             fontsize=14, fontweight='bold', color='darkblue',
             bbox=dict(boxstyle='round', facecolor='lightyellow', 
                      alpha=0.8, linewidth=3, edgecolor='darkblue'))

plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig('images/bad_visualization_exercise.png', dpi=150, bbox_inches='tight',
            facecolor='#E8F4F8')
plt.close()

print("\n✅ Created intentionally BAD visualization!")
print("📁 Saved as: images/bad_visualization_exercise.png")
print("\nThis visualization has the following intentional problems:")
print("1. ❌ 3D pie chart with too many slices (poor angle comparison)")
print("2. ❌ Rainbow colors (perceptually non-uniform)")
print("3. ❌ Truncated y-axis (exaggerates differences)")
print("4. ❌ Dual y-axes with different scales (misleading)")
print("5. ❌ Heavy chart junk (backgrounds, borders, shadows)")
print("6. ❌ Too many elements competing for attention")
print("7. ❌ Inconsistent styling and fonts")
print("8. ❌ Poor labeling and tiny text")
print("9. ❌ Confusing scatter plot with no legend")
print("10. ❌ Overall: High cognitive load, low insight")
print("\nStudents should identify these issues in Exercise 1!")
