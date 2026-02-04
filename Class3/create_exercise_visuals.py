"""
Create visual examples for Exercises 2-5
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import seaborn as sns
import pandas as pd

print("Creating visual examples for Exercises 2-5...")

# =============================================================================
# EXERCISE 2: Redesign Challenge - Before and After Dashboard
# =============================================================================
print("\n1. Creating Exercise 2: Dashboard Redesign Before/After...")

fig = plt.figure(figsize=(14, 10))

# BEFORE: High cognitive load dashboard
ax1 = plt.subplot(2, 1, 1)
ax1.text(0.5, 0.95, 'BEFORE: High Cognitive Load Dashboard', 
         ha='center', va='top', fontsize=16, fontweight='bold',
         transform=ax1.transAxes)

# Simulate a cluttered dashboard
ax1.text(0.5, 0.75, '❌ Everything same size and color', ha='center', fontsize=11,
         transform=ax1.transAxes, color='darkred')
ax1.text(0.5, 0.65, '❌ No visual hierarchy', ha='center', fontsize=11,
         transform=ax1.transAxes, color='darkred')
ax1.text(0.5, 0.55, '❌ Too many metrics competing for attention', ha='center', fontsize=11,
         transform=ax1.transAxes, color='darkred')
ax1.text(0.5, 0.45, '❌ Cluttered legends and labels', ha='center', fontsize=11,
         transform=ax1.transAxes, color='darkred')
ax1.text(0.5, 0.35, '❌ Inconsistent time periods', ha='center', fontsize=11,
         transform=ax1.transAxes, color='darkred')
ax1.text(0.5, 0.2, 'Task: Identify sources of extraneous load', ha='center', fontsize=12,
         transform=ax1.transAxes, style='italic', bbox=dict(boxstyle='round', 
         facecolor='lightyellow', alpha=0.8))
ax1.axis('off')

# AFTER: Low cognitive load dashboard
ax2 = plt.subplot(2, 1, 2)
ax2.text(0.5, 0.95, 'AFTER: Low Cognitive Load Dashboard', 
         ha='center', va='top', fontsize=16, fontweight='bold',
         transform=ax2.transAxes, color='darkgreen')

ax2.text(0.5, 0.75, '✅ Top 3-5 metrics prominently displayed', ha='center', fontsize=11,
         transform=ax2.transAxes, color='darkgreen')
ax2.text(0.5, 0.65, '✅ Clear visual hierarchy', ha='center', fontsize=11,
         transform=ax2.transAxes, color='darkgreen')
ax2.text(0.5, 0.55, '✅ Simple, clean charts', ha='center', fontsize=11,
         transform=ax2.transAxes, color='darkgreen')
ax2.text(0.5, 0.45, '✅ Direct labeling (no legend hunting)', ha='center', fontsize=11,
         transform=ax2.transAxes, color='darkgreen')
ax2.text(0.5, 0.35, '✅ Consistent time periods and scales', ha='center', fontsize=11,
         transform=ax2.transAxes, color='darkgreen')
ax2.text(0.5, 0.2, 'Goal: Apply Gestalt principles and reduce extraneous load', 
         ha='center', fontsize=12, transform=ax2.transAxes, style='italic',
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))
ax2.axis('off')

plt.tight_layout()
plt.savefig('images/exercise2_redesign_challenge.png', dpi=150, bbox_inches='tight')
plt.close()
print("  ✅ Created: exercise2_redesign_challenge.png")

# =============================================================================
# EXERCISE 3: Grammar-Based Plot Example
# =============================================================================
print("\n2. Creating Exercise 3: Grammar of Graphics Example...")

# Create sample data
np.random.seed(42)
data = pd.DataFrame({
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'] * 3,
    'Sales': [45, 52, 48, 55, 50, 58, 53, 62, 48, 55, 51, 60],
    'Product': ['A']*4 + ['B']*4 + ['C']*4,
    'Region': (['North']*2 + ['South']*2) * 3
})

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Exercise 3: Build a Grammar-Based Plot\nDecomposing a Visualization', 
             fontsize=16, fontweight='bold', y=0.98)

# 1. Data
axes[0, 0].text(0.5, 0.9, '1. DATA', ha='center', fontsize=14, fontweight='bold',
                transform=axes[0, 0].transAxes, color='#003366')
axes[0, 0].text(0.1, 0.7, 'Structured Format:', fontsize=11, fontweight='bold',
                transform=axes[0, 0].transAxes)
axes[0, 0].text(0.1, 0.55, '• Quarter (Temporal)', fontsize=10,
                transform=axes[0, 0].transAxes)
axes[0, 0].text(0.1, 0.45, '• Sales (Quantitative)', fontsize=10,
                transform=axes[0, 0].transAxes)
axes[0, 0].text(0.1, 0.35, '• Product (Nominal)', fontsize=10,
                transform=axes[0, 0].transAxes)
axes[0, 0].text(0.1, 0.25, '• Region (Nominal)', fontsize=10,
                transform=axes[0, 0].transAxes)
axes[0, 0].text(0.1, 0.1, 'Each row = observation\nEach column = variable', 
                fontsize=9, style='italic', transform=axes[0, 0].transAxes)
axes[0, 0].axis('off')

# 2. Aesthetic Mappings
axes[0, 1].text(0.5, 0.9, '2. AESTHETICS', ha='center', fontsize=14, fontweight='bold',
                transform=axes[0, 1].transAxes, color='#003366')
axes[0, 1].text(0.1, 0.7, 'Map data to visuals:', fontsize=11, fontweight='bold',
                transform=axes[0, 1].transAxes)
axes[0, 1].text(0.1, 0.55, 'x = Quarter', fontsize=10,
                transform=axes[0, 1].transAxes, family='monospace')
axes[0, 1].text(0.1, 0.45, 'y = Sales', fontsize=10,
                transform=axes[0, 1].transAxes, family='monospace')
axes[0, 1].text(0.1, 0.35, 'color = Product', fontsize=10,
                transform=axes[0, 1].transAxes, family='monospace')
axes[0, 1].text(0.1, 0.25, 'marker = ○ (circle)', fontsize=10,
                transform=axes[0, 1].transAxes, family='monospace')
axes[0, 1].text(0.1, 0.1, 'Task: Show sales trends\nby product over time', 
                fontsize=9, style='italic', transform=axes[0, 1].transAxes)
axes[0, 1].axis('off')

# 3. Geom + Stats
axes[1, 0].text(0.5, 0.9, '3. GEOM + STATS', ha='center', fontsize=14, fontweight='bold',
                transform=axes[1, 0].transAxes, color='#003366')
axes[1, 0].text(0.1, 0.7, 'Visual marks:', fontsize=11, fontweight='bold',
                transform=axes[1, 0].transAxes)
axes[1, 0].text(0.1, 0.55, 'geom = line + point', fontsize=10,
                transform=axes[1, 0].transAxes, family='monospace')
axes[1, 0].text(0.1, 0.45, 'stat = identity', fontsize=10,
                transform=axes[1, 0].transAxes, family='monospace')
axes[1, 0].text(0.1, 0.3, 'Why?', fontsize=10, fontweight='bold',
                transform=axes[1, 0].transAxes)
axes[1, 0].text(0.1, 0.2, '• Lines show trends', fontsize=9,
                transform=axes[1, 0].transAxes)
axes[1, 0].text(0.1, 0.12, '• Points show data values', fontsize=9,
                transform=axes[1, 0].transAxes)
axes[1, 0].axis('off')

# 4. Result visualization
sns.lineplot(data=data, x='Quarter', y='Sales', hue='Product', 
             marker='o', linewidth=2, palette=['#2E86AB', '#A23B72', '#F18F01'],
             ax=axes[1, 1])
axes[1, 1].set_title('4. FINAL RESULT', fontsize=14, fontweight='bold', color='#003366')
axes[1, 1].set_xlabel('Quarter', fontsize=11)
axes[1, 1].set_ylabel('Sales (K$)', fontsize=11)
axes[1, 1].spines['top'].set_visible(False)
axes[1, 1].spines['right'].set_visible(False)
axes[1, 1].legend(title='Product', frameon=False)

plt.tight_layout()
plt.savefig('images/exercise3_grammar_example.png', dpi=150, bbox_inches='tight')
plt.close()
print("  ✅ Created: exercise3_grammar_example.png")

# =============================================================================
# EXERCISE 4: Color Palette Selection for Temperature Data
# =============================================================================
print("\n3. Creating Exercise 4: Color Palette Selection...")

# Create temperature data
np.random.seed(42)
temp_data = np.random.randn(10, 12) * 15 + 15  # Temperature from -10°C to +40°C

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle('Exercise 4: Color Palette Selection for Temperature Data (-10°C to +40°C)',
             fontsize=14, fontweight='bold')

# BAD: Rainbow/Jet
im1 = axes[0].imshow(temp_data, cmap='jet', aspect='auto', vmin=-10, vmax=40)
axes[0].set_title('❌ BAD: Rainbow (Jet)\nNon-perceptual, false boundaries', 
                  fontsize=11, color='darkred')
axes[0].set_xlabel('Month')
axes[0].set_ylabel('Location')
plt.colorbar(im1, ax=axes[0], label='Temperature (°C)')

# BETTER: Viridis (Sequential)
im2 = axes[1].imshow(temp_data, cmap='viridis', aspect='auto', vmin=-10, vmax=40)
axes[1].set_title('⚠️ BETTER: Viridis\nPerceptual but no meaningful zero', 
                  fontsize=11, color='orange')
axes[1].set_xlabel('Month')
axes[1].set_ylabel('Location')
plt.colorbar(im2, ax=axes[1], label='Temperature (°C)')

# BEST: Diverging with zero at center
im3 = axes[2].imshow(temp_data, cmap='RdBu_r', aspect='auto', vmin=-10, vmax=40)
axes[2].set_title('✅ BEST: Diverging (RdBu_r)\nCentered at 0°C', 
                  fontsize=11, color='darkgreen')
axes[2].set_xlabel('Month')
axes[2].set_ylabel('Location')
plt.colorbar(im3, ax=axes[2], label='Temperature (°C)')

plt.tight_layout()
plt.savefig('images/exercise4_color_palette.png', dpi=150, bbox_inches='tight')
plt.close()
print("  ✅ Created: exercise4_color_palette.png")

# =============================================================================
# EXERCISE 5: Preattentive Highlighting for Q4
# =============================================================================
print("\n4. Creating Exercise 5: Preattentive Highlighting...")

# Create quarterly sales data
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
q1 = [45, 52, 38, 48, 42]
q2 = [48, 55, 41, 50, 45]
q3 = [50, 58, 43, 52, 47]
q4 = [62, 68, 55, 65, 60]  # Q4 should pop out

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Exercise 5: Preattentive Highlighting - Make Q4 Pop Out!',
             fontsize=14, fontweight='bold')

# WITHOUT highlighting (hard to see Q4)
x = np.arange(len(products))
width = 0.2
axes[0].bar(x - 1.5*width, q1, width, label='Q1', color='steelblue', alpha=0.7)
axes[0].bar(x - 0.5*width, q2, width, label='Q2', color='steelblue', alpha=0.7)
axes[0].bar(x + 0.5*width, q3, width, label='Q3', color='steelblue', alpha=0.7)
axes[0].bar(x + 1.5*width, q4, width, label='Q4', color='steelblue', alpha=0.7)
axes[0].set_xlabel('Product')
axes[0].set_ylabel('Sales (K$)')
axes[0].set_title('❌ WITHOUT Preattentive Highlighting\n(Q4 blends in)', color='darkred')
axes[0].set_xticks(x)
axes[0].set_xticklabels(products)
axes[0].legend()
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)

# WITH highlighting (Q4 pops out!)
axes[1].bar(x - 1.5*width, q1, width, label='Q1', color='#CCCCCC', alpha=0.6)
axes[1].bar(x - 0.5*width, q2, width, label='Q2', color='#CCCCCC', alpha=0.6)
axes[1].bar(x + 0.5*width, q3, width, label='Q3', color='#CCCCCC', alpha=0.6)
axes[1].bar(x + 1.5*width, q4, width, label='Q4', color='#E63946', alpha=0.9)
axes[1].set_xlabel('Product')
axes[1].set_ylabel('Sales (K$)')
axes[1].set_title('✅ WITH Preattentive Highlighting\n(Q4 immediately visible!)', color='darkgreen')
axes[1].set_xticks(x)
axes[1].set_xticklabels(products)
axes[1].legend()
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)

# Add direct labels on Q4 bars
for i, val in enumerate(q4):
    axes[1].text(x[i] + 1.5*width, val + 1, str(val), ha='center', fontweight='bold',
                color='#E63946', fontsize=9)

plt.tight_layout()
plt.savefig('images/exercise5_preattentive_highlighting.png', dpi=150, bbox_inches='tight')
plt.close()
print("  ✅ Created: exercise5_preattentive_highlighting.png")

print("\n" + "="*60)
print("✅ ALL EXERCISE VISUALS CREATED SUCCESSFULLY!")
print("="*60)
print("\nCreated 4 new visualization files:")
print("  1. exercise2_redesign_challenge.png")
print("  2. exercise3_grammar_example.png")
print("  3. exercise4_color_palette.png")
print("  4. exercise5_preattentive_highlighting.png")
print("\nThese examples will help students understand:")
print("  • Exercise 2: How to reduce cognitive load")
print("  • Exercise 3: How to apply Grammar of Graphics")
print("  • Exercise 4: How to choose appropriate color palettes")
print("  • Exercise 5: How to use preattentive features")
