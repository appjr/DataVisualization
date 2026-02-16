"""
Create an image for a single slide
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import os

# Create output directory
os.makedirs('slide_images', exist_ok=True)

# Slide 34 content
title = "Y-Axis Decisions"
subtitle = "Should time series start at zero?"

content = [
    ("✓ Yes", "for absolute magnitude (e.g., revenue)", "green"),
    ("✗ No", "when showing percent change or deviation", "red")
]

code_example = "ax.set_ylim(0, None)   # force zero baseline"

# Create figure
fig, ax = plt.subplots(figsize=(12, 8))
ax.axis('off')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Background
rect = FancyBboxPatch((0.2, 0.2), 9.6, 9.6, 
                      boxstyle="round,pad=0.1", 
                      edgecolor='#2c3e50', 
                      facecolor='#ecf0f1',
                      linewidth=3)
ax.add_patch(rect)

# Title
ax.text(5, 8.5, title, 
        ha='center', va='top',
        fontsize=32, fontweight='bold',
        color='#2c3e50')

# Subtitle
ax.text(5, 7.8, subtitle,
        ha='center', va='top',
        fontsize=24, fontweight='bold',
        color='#34495e', style='italic')

# Content items
y_pos = 6.5
for symbol, text, color in content:
    # Symbol with background
    circle_color = '#27ae60' if color == 'green' else '#e74c3c'
    circle = plt.Circle((1.5, y_pos), 0.3, color=circle_color, alpha=0.2)
    ax.add_patch(circle)
    
    # Symbol text
    ax.text(1.5, y_pos, symbol,
            ha='center', va='center',
            fontsize=28, fontweight='bold',
            color=circle_color)
    
    # Main text
    ax.text(2.2, y_pos, text,
            ha='left', va='center',
            fontsize=20,
            color='#2c3e50')
    
    y_pos -= 1.2

# Code example box
code_box = FancyBboxPatch((1, 3.2), 8, 1.2,
                         boxstyle="round,pad=0.05",
                         edgecolor='#95a5a6',
                         facecolor='#34495e',
                         linewidth=2)
ax.add_patch(code_box)

# Code text
ax.text(5, 3.8, 'Python Example:',
        ha='center', va='center',
        fontsize=16, fontweight='bold',
        color='#ecf0f1')

ax.text(5, 3.4, code_example,
        ha='center', va='center',
        fontsize=18,
        color='#3498db',
        family='monospace')

# Footer
ax.text(5, 0.8, 'Class 5 – Time Series & Temporal Visualization',
        ha='center', va='center',
        fontsize=14, color='#7f8c8d')

ax.text(5, 0.4, 'MIS 6380 - Data Visualization',
        ha='center', va='center',
        fontsize=12, color='#95a5a6')

plt.tight_layout()
plt.savefig('slide_images/slide_034.png', dpi=150, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print("✓ Created slide_images/slide_034.png")
plt.close()

print("\n✅ Slide image created successfully!")
