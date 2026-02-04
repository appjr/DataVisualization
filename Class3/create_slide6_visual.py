"""
Create visual demonstration for Slide 6 - Preattentive vs Attentive Processing
Shows feature search vs conjunction search
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

os.makedirs('images', exist_ok=True)

# ============================================================================
# FEATURE SEARCH (Easy - Preattentive)
# ============================================================================
print("Creating Feature Search example (preattentive)...")
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('FEATURE SEARCH: Find the Red Circle\n(Uses color only - FAST!)', 
             fontsize=14, fontweight='bold', pad=20)

np.random.seed(42)

# Create blue circles
for i in range(50):
    x, y = np.random.uniform(0.5, 9.5), np.random.uniform(0.5, 5.5)
    circle = plt.Circle((x, y), 0.25, color='steelblue', alpha=0.8, linewidth=1, edgecolor='darkblue')
    ax.add_patch(circle)

# ONE red circle (target)
target_circle = plt.Circle((5, 3), 0.25, color='#E63946', alpha=0.9, linewidth=2, edgecolor='darkred')
ax.add_patch(target_circle)

# Add arrow pointing to it
ax.annotate('', xy=(5, 3), xytext=(7, 4.5),
           arrowprops=dict(arrowstyle='->', lw=3, color='#E63946'))
ax.text(7.5, 4.7, 'Found instantly!', fontsize=12, fontweight='bold', color='#E63946')

ax.text(5, 0.2, '< 200ms to find the red circle', 
        ha='center', fontsize=11, style='italic', bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

plt.tight_layout()
plt.savefig('images/feature_search_easy.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# CONJUNCTION SEARCH (Difficult - Requires Attention)
# ============================================================================
print("Creating Conjunction Search example (attentive)...")
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('CONJUNCTION SEARCH: Find the Red Square\n(Requires color AND shape - SLOW!)', 
             fontsize=14, fontweight='bold', pad=20)

np.random.seed(42)

# Create distractors: red circles, blue squares, blue circles
shapes = []
for i in range(15):
    x, y = np.random.uniform(0.5, 9.5), np.random.uniform(0.5, 5.5)
    # Red circles
    circle = plt.Circle((x, y), 0.25, color='#E63946', alpha=0.8, linewidth=1, edgecolor='darkred')
    ax.add_patch(circle)
    shapes.append((x, y, 'red_circle'))

for i in range(15):
    x, y = np.random.uniform(0.5, 9.5), np.random.uniform(0.5, 5.5)
    # Blue squares
    square = patches.Rectangle((x-0.25, y-0.25), 0.5, 0.5, 
                               color='steelblue', alpha=0.8, linewidth=1, edgecolor='darkblue')
    ax.add_patch(square)
    shapes.append((x, y, 'blue_square'))

for i in range(15):
    x, y = np.random.uniform(0.5, 9.5), np.random.uniform(0.5, 5.5)
    # Blue circles
    circle = plt.Circle((x, y), 0.25, color='steelblue', alpha=0.8, linewidth=1, edgecolor='darkblue')
    ax.add_patch(circle)
    shapes.append((x, y, 'blue_circle'))

# ONE red square (target) - place it in a clear spot
target_square = patches.Rectangle((5-0.25, 3-0.25), 0.5, 0.5,
                                 color='#E63946', alpha=0.9, linewidth=3, edgecolor='darkred')
ax.add_patch(target_square)

# Add arrow pointing to it
ax.annotate('', xy=(5, 3), xytext=(7, 4.5),
           arrowprops=dict(arrowstyle='->', lw=3, color='orange'))
ax.text(7.5, 4.7, 'Takes time to find!', fontsize=12, fontweight='bold', color='orange')

ax.text(5, 0.2, 'Much slower - requires checking color AND shape together', 
        ha='center', fontsize=11, style='italic', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

plt.tight_layout()
plt.savefig('images/conjunction_search_difficult.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# SIDE BY SIDE COMPARISON
# ============================================================================
print("Creating side-by-side comparison...")
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# LEFT: Feature search
ax = axes[0]
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('EASY: Feature Search\n(Single feature - color)', 
             fontsize=12, fontweight='bold', color='green')

np.random.seed(42)
for i in range(40):
    x, y = np.random.uniform(0.5, 9.5), np.random.uniform(0.5, 5.5)
    circle = plt.Circle((x, y), 0.2, color='steelblue', alpha=0.7)
    ax.add_patch(circle)
target = plt.Circle((5, 3), 0.2, color='#E63946', alpha=0.9, linewidth=2, edgecolor='darkred')
ax.add_patch(target)
ax.text(5, 0.5, '✓ Preattentive\n< 200ms', ha='center', fontsize=10, 
       fontweight='bold', color='green')

# RIGHT: Conjunction search
ax = axes[1]
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('DIFFICULT: Conjunction Search\n(Multiple features - color AND shape)', 
             fontsize=12, fontweight='bold', color='red')

np.random.seed(42)
# Red circles
for i in range(12):
    x, y = np.random.uniform(0.5, 9.5), np.random.uniform(0.5, 5.5)
    circle = plt.Circle((x, y), 0.2, color='#E63946', alpha=0.7)
    ax.add_patch(circle)
# Blue squares
for i in range(12):
    x, y = np.random.uniform(0.5, 9.5), np.random.uniform(0.5, 5.5)
    square = patches.Rectangle((x-0.2, y-0.2), 0.4, 0.4, color='steelblue', alpha=0.7)
    ax.add_patch(square)
# Blue circles
for i in range(12):
    x, y = np.random.uniform(0.5, 9.5), np.random.uniform(0.5, 5.5)
    circle = plt.Circle((x, y), 0.2, color='steelblue', alpha=0.7)
    ax.add_patch(circle)
# Target: Red square
target_sq = patches.Rectangle((5-0.2, 3-0.2), 0.4, 0.4, 
                              color='#E63946', alpha=0.9, linewidth=2, edgecolor='darkred')
ax.add_patch(target_sq)
ax.text(5, 0.5, '✗ Requires Attention\nMuch slower', ha='center', fontsize=10, 
       fontweight='bold', color='red')

plt.suptitle('Why Preattentive Features Matter in Visualization', 
             fontsize=14, fontweight='bold', y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('images/preattentive_comparison.png', dpi=150, bbox_inches='tight')
plt.close()

print("\n✅ Created 3 images for Slide 6:")
print("1. images/feature_search_easy.png - Demonstrates fast feature search")
print("2. images/conjunction_search_difficult.png - Demonstrates slow conjunction search")
print("3. images/preattentive_comparison.png - Side-by-side comparison")
print("\nRecommendation: Use 'preattentive_comparison.png' for Slide 6")
