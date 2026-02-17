"""
Create professional high-quality slide for "What Makes Time Series Data Special?"
Using matplotlib for complete control and guaranteed quality
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrow
import os

# Create figure
fig, ax = plt.subplots(figsize=(16, 9))
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')

# Background gradient
from matplotlib.patches import Rectangle
bg = Rectangle((0, 0), 16, 9, facecolor='#F0F8FF', edgecolor='none')
ax.add_patch(bg)

# Title box
title_box = FancyBboxPatch((0.5, 7.5), 15, 1.2,
                           boxstyle="round,pad=0.1",
                           edgecolor='#2E86AB',
                           facecolor='#2E86AB',
                           linewidth=3)
ax.add_patch(title_box)

# Title text
ax.text(8, 8.1, 'What Makes Time Series Data Special?',
        ha='center', va='center',
        fontsize=32, fontweight='bold',
        color='white')

# Subtitle
ax.text(8, 7.2, '7 Unique Properties That Require Specialized Visualization Approaches',
        ha='center', va='top',
        fontsize=16, style='italic',
        color='#34495e')

# Define 7 properties with icons
properties = [
    {
        'num': '1',
        'title': 'Temporal Ordering Matters',
        'desc': 'Order contains critical information\nCannot shuffle time series data',
        'icon': '⏱️',
        'pos': (2, 5.5)
    },
    {
        'num': '2',
        'title': 'Temporal Dependencies',
        'desc': 'Today depends on yesterday\nAutocorrelation and lag effects',
        'icon': '🔗',
        'pos': (8, 5.5)
    },
    {
        'num': '3',
        'title': 'Non-IID',
        'desc': 'Standard assumptions violated\nNeed specialized methods',
        'icon': '⚠️',
        'pos': (14, 5.5)
    },
    {
        'num': '4',
        'title': 'Multiple Time Scales',
        'desc': 'Hourly, daily, weekly, monthly\nAll patterns present simultaneously',
        'icon': '📊',
        'pos': (2, 3)
    },
    {
        'num': '5',
        'title': 'Non-Stationarity',
        'desc': 'Properties change over time\nMean and variance shift',
        'icon': '📈',
        'pos': (8, 3)
    },
    {
        'num': '6',
        'title': 'Irregular Intervals',
        'desc': 'Gaps from weekends, holidays\nMissing values have meaning',
        'icon': '⚡',
        'pos': (14, 3)
    },
    {
        'num': '7',
        'title': 'Context-Dependent',
        'desc': 'Same value, different meanings\nTemporal context matters',
        'icon': '🔍',
        'pos': (8, 0.5)
    }
]

# Draw each property card
for prop in properties:
    x, y = prop['pos']
    
    # Card background
    card = FancyBboxPatch((x-1.8, y-0.9), 3.5, 1.6,
                          boxstyle="round,pad=0.1",
                          edgecolor='#3498db',
                          facecolor='white',
                          linewidth=2)
    ax.add_patch(card)
    
    # Number circle
    circle = Circle((x-1.3, y+0.5), 0.25,
                   facecolor='#e74c3c',
                   edgecolor='#c0392b',
                   linewidth=2)
    ax.add_patch(circle)
    
    # Number
    ax.text(x-1.3, y+0.5, prop['num'],
            ha='center', va='center',
            fontsize=18, fontweight='bold',
            color='white')
    
    # Icon/Emoji (will appear as boxes if font doesn't support)
    ax.text(x+1.2, y+0.5, prop['icon'],
            ha='center', va='center',
            fontsize=32)
    
    # Title
    ax.text(x-0.7, y+0.5, prop['title'],
            ha='left', va='center',
            fontsize=14, fontweight='bold',
            color='#2c3e50')
    
    # Description
    ax.text(x, y-0.2, prop['desc'],
            ha='center', va='top',
            fontsize=10,
            color='#555',
            multialignment='center')

# Bottom banner
banner = Rectangle((0, 0), 16, 0.3, facecolor='#34495e', edgecolor='none')
ax.add_patch(banner)

ax.text(8, 0.15, 'Class 5 – Time Series & Temporal Visualization  |  MIS 6380 Data Visualization',
        ha='center', va='center',
        fontsize=11, color='white')

# Add decorative elements
# Corner accents
for corner_x, corner_y in [(0.3, 8.7), (15.7, 8.7), (0.3, 0.3), (15.7, 0.3)]:
    accent = Rectangle((corner_x, corner_y), 0.15, 0.15,
                      facecolor='#3498db', edgecolor='none')
    ax.add_patch(accent)

plt.tight_layout()

# Save
output_dir = "special_slides"
os.makedirs(output_dir, exist_ok=True)
output_file = f"{output_dir}/what_makes_ts_special_professional.png"

plt.savefig(output_file, dpi=200, bbox_inches='tight',
            facecolor='white', edgecolor='none')

print(f"✓ Professional slide created")
print(f"  File: {output_file}")
print(f"  Size: {os.path.getsize(output_file) / 1024:.0f} KB")
print(f"  Resolution: 200 DPI")
print(f"\n✅ High-quality slide ready!")

plt.close()
