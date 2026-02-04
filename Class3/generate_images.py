"""
Generate all images for Class 3 slides
This script creates visualizations to replace external image links
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

# Create images directory
os.makedirs('images', exist_ok=True)

print("Generating images for Class 3...")

# ============================================================================
# 1. PREATTENTIVE PROCESSING - Visual Pop-Out
# ============================================================================
print("1. Creating preattentive processing example...")
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Preattentive Pop-Out: Find the Red Circle', fontsize=14, fontweight='bold')

# Blue circles
np.random.seed(42)
for _ in range(50):
    x, y = np.random.uniform(0.5, 9.5, 2)
    circle = plt.Circle((x, y), 0.2, color='steelblue', alpha=0.7)
    ax.add_patch(circle)

# One red circle (pop-out)
red_circle = plt.Circle((5, 5), 0.2, color='#E63946', alpha=0.9)
ax.add_patch(red_circle)

plt.tight_layout()
plt.savefig('images/preattentive_popout.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# 2. GESTALT - PROXIMITY
# ============================================================================
print("2. Creating Gestalt proximity example...")
fig, ax = plt.subplots(figsize=(10, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Gestalt Principle: Proximity', fontsize=14, fontweight='bold')

# Three groups of dots with spacing
for group in range(3):
    x_offset = group * 3.5
    for row in range(3):
        for col in range(3):
            circle = plt.Circle((x_offset + col*0.3, row*0.3 + 1), 0.1, 
                              color='#2E86AB', alpha=0.8)
            ax.add_patch(circle)

ax.text(5, 0.2, 'Objects close together are perceived as grouped', 
        ha='center', fontsize=11, style='italic')

plt.tight_layout()
plt.savefig('images/gestalt_proximity.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# 3. GESTALT - SIMILARITY
# ============================================================================
print("3. Creating Gestalt similarity example...")
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Gestalt Principle: Similarity', fontsize=14, fontweight='bold')

# Alternating colors create grouping
for row in range(4):
    for col in range(12):
        if col % 2 == 0:
            color = '#2E86AB'
        else:
            color = '#E63946'
        circle = plt.Circle((col*0.8, row*0.6 + 0.5), 0.2, 
                          color=color, alpha=0.8)
        ax.add_patch(circle)

ax.text(5, 0.1, 'Similar objects are perceived as related', 
        ha='center', fontsize=11, style='italic')

plt.tight_layout()
plt.savefig('images/gestalt_similarity.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# 4. GESTALT - ENCLOSURE
# ============================================================================
print("4. Creating Gestalt enclosure example...")
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Gestalt Principle: Enclosure & Common Region', fontsize=14, fontweight='bold')

# Two boxes with enclosed elements
rect1 = patches.Rectangle((1, 1), 3, 2, linewidth=2, 
                          edgecolor='#2E86AB', facecolor='#2E86AB', alpha=0.1)
ax.add_patch(rect1)
ax.text(2.5, 3.3, 'Group A', fontsize=12, ha='center', fontweight='bold', color='#2E86AB')

rect2 = patches.Rectangle((6, 1), 3, 2, linewidth=2, 
                          edgecolor='#E63946', facecolor='#E63946', alpha=0.1)
ax.add_patch(rect2)
ax.text(7.5, 3.3, 'Group B', fontsize=12, ha='center', fontweight='bold', color='#E63946')

# Dots inside boxes
for i in range(6):
    x, y = np.random.uniform(1.2, 3.8), np.random.uniform(1.2, 2.8)
    circle = plt.Circle((x, y), 0.15, color='#2E86AB', alpha=0.8)
    ax.add_patch(circle)

for i in range(6):
    x, y = np.random.uniform(6.2, 8.8), np.random.uniform(1.2, 2.8)
    circle = plt.Circle((x, y), 0.15, color='#E63946', alpha=0.8)
    ax.add_patch(circle)

ax.text(5, 0.3, 'Enclosure creates strong grouping', 
        ha='center', fontsize=11, style='italic')

plt.tight_layout()
plt.savefig('images/gestalt_enclosure.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# 5. GESTALT - CONNECTION
# ============================================================================
print("5. Creating Gestalt connection example...")
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Gestalt Principle: Connection', fontsize=14, fontweight='bold')

# Connected points
points1 = [(1, 2), (2, 3), (3, 2.5)]
points2 = [(5, 1.5), (6, 2.5), (7, 2)]
points3 = [(8, 3), (9, 2)]

for points in [points1, points2, points3]:
    xs, ys = zip(*points)
    ax.plot(xs, ys, 'o-', markersize=15, linewidth=3, 
           color='#2E86AB', alpha=0.7)

# Unconnected points
for x in [4, 7.5]:
    circle = plt.Circle((x, 1), 0.3, color='#CCCCCC', alpha=0.7)
    ax.add_patch(circle)

ax.text(5, 0.3, 'Connected elements are perceived as groups', 
        ha='center', fontsize=11, style='italic')

plt.tight_layout()
plt.savefig('images/gestalt_connection.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# 6. COGNITIVE LOAD BALANCE
# ============================================================================
print("6. Creating cognitive load balance diagram...")
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title('Cognitive Load Balance', fontsize=16, fontweight='bold', pad=20)

# Total capacity box
total_box = patches.Rectangle((2, 1), 6, 7, linewidth=3, 
                              edgecolor='black', facecolor='white')
ax.add_patch(total_box)
ax.text(5, 8.5, 'Total Cognitive Capacity (Fixed)', 
        ha='center', fontsize=13, fontweight='bold')

# Intrinsic load
intrinsic = patches.Rectangle((2, 6), 6, 2, linewidth=2, 
                              edgecolor='black', facecolor='#A8DADC', alpha=0.7)
ax.add_patch(intrinsic)
ax.text(5, 7, 'Intrinsic Load\n(Necessary)', 
        ha='center', va='center', fontsize=11, fontweight='bold')

# Extraneous load
extraneous = patches.Rectangle((2, 3.5), 6, 2.5, linewidth=2, 
                               edgecolor='black', facecolor='#E63946', alpha=0.7)
ax.add_patch(extraneous)
ax.text(5, 4.75, 'Extraneous Load\n(MINIMIZE!)', 
        ha='center', va='center', fontsize=11, fontweight='bold', color='white')
ax.text(8.5, 4.75, '❌', fontsize=20, va='center')

# Germane load
germane = patches.Rectangle((2, 1), 6, 2.5, linewidth=2, 
                            edgecolor='black', facecolor='#457B9D', alpha=0.7)
ax.add_patch(germane)
ax.text(5, 2.25, 'Germane Load\n(MAXIMIZE!)', 
        ha='center', va='center', fontsize=11, fontweight='bold', color='white')
ax.text(8.5, 2.25, '✅', fontsize=20, va='center')

plt.tight_layout()
plt.savefig('images/cognitive_load_balance.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# 7. ENCODING EFFECTIVENESS RANKING
# ============================================================================
print("7. Creating encoding effectiveness ranking...")
fig, ax = plt.subplots(figsize=(10, 8))

encodings = [
    'Position on common scale',
    'Position on non-aligned scale',
    'Length',
    'Angle / Slope',
    'Area',
    'Volume',
    'Color intensity'
]

accuracy = [95, 85, 75, 65, 50, 35, 30]
colors = ['#1D3557', '#2E5266', '#457B9D', '#6C8EAD', 
          '#A8DADC', '#C8E7ED', '#E8F4F8']

bars = ax.barh(encodings, accuracy, color=colors, edgecolor='black', linewidth=1.5)

ax.set_xlabel('Relative Accuracy', fontsize=12, fontweight='bold')
ax.set_title('Visual Encoding Effectiveness\n(Most → Least Effective)', 
             fontsize=14, fontweight='bold', pad=15)
ax.set_xlim(0, 100)

# Add accuracy labels
for i, (enc, acc) in enumerate(zip(encodings, accuracy)):
    ax.text(acc + 2, i, f'{acc}%', va='center', fontsize=10, fontweight='bold')

# Remove spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# Add star to best encoding
ax.text(-5, 6, '⭐', fontsize=20, va='center')

plt.tight_layout()
plt.savefig('images/encoding_effectiveness.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# 8. DATA TYPES DIAGRAM
# ============================================================================
print("8. Creating data types diagram...")
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title('Four Fundamental Data Types', fontsize=16, fontweight='bold', pad=20)

data_types = [
    {'name': 'Nominal', 'y': 7.5, 'color': '#E63946', 
     'desc': 'Categories\nNo order', 'example': 'Product types'},
    {'name': 'Ordinal', 'y': 5.5, 'color': '#F18F01',
     'desc': 'Ordered categories\nUnequal intervals', 'example': 'Satisfaction: Low → High'},
    {'name': 'Quantitative', 'y': 3.5, 'color': '#2E86AB',
     'desc': 'Numerical\nMagnitude matters', 'example': 'Revenue: $1M, $2M'},
    {'name': 'Temporal', 'y': 1.5, 'color': '#A23B72',
     'desc': 'Time-based\nSequential', 'example': 'Daily sales'}
]

for dt in data_types:
    # Box
    rect = patches.FancyBboxPatch((1, dt['y']-0.6), 8, 1.2, 
                                  boxstyle="round,pad=0.1",
                                  linewidth=3, edgecolor=dt['color'],
                                  facecolor=dt['color'], alpha=0.2)
    ax.add_patch(rect)
    
    # Name
    ax.text(2, dt['y'], dt['name'], fontsize=14, fontweight='bold',
           va='center', color=dt['color'])
    
    # Description
    ax.text(4.5, dt['y'], dt['desc'], fontsize=10, va='center')
    
    # Example
    ax.text(7.5, dt['y'], dt['example'], fontsize=9, va='center',
           style='italic', color='#666666')

plt.tight_layout()
plt.savefig('images/data_types.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# 9. GRAMMAR OF GRAPHICS LAYERS
# ============================================================================
print("9. Creating Grammar of Graphics layers...")
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title('Grammar of Graphics: Layered Structure', 
             fontsize=16, fontweight='bold', pad=20)

layers = [
    {'name': '7. Facets', 'y': 8.5, 'color': '#E63946'},
    {'name': '6. Coordinate System', 'y': 7.5, 'color': '#F18F01'},
    {'name': '5. Scales', 'y': 6.5, 'color': '#FFC857'},
    {'name': '4. Statistical Transform', 'y': 5.5, 'color': '#2E86AB'},
    {'name': '3. Geometric Objects', 'y': 4.5, 'color': '#457B9D'},
    {'name': '2. Aesthetic Mappings', 'y': 3.5, 'color': '#A23B72'},
    {'name': '1. Data', 'y': 2.5, 'color': '#1D3557'}
]

for layer in layers:
    rect = patches.Rectangle((2, layer['y']-0.4), 6, 0.8,
                            linewidth=2, edgecolor='black',
                            facecolor=layer['color'], alpha=0.7)
    ax.add_patch(rect)
    ax.text(5, layer['y'], layer['name'], fontsize=12, fontweight='bold',
           ha='center', va='center', color='white')

# Arrow
ax.annotate('', xy=(1, 2.5), xytext=(1, 8.5),
           arrowprops=dict(arrowstyle='<->', lw=3, color='#666666'))
ax.text(0.5, 5.5, 'Build\nUp', fontsize=11, ha='center', va='center',
       fontweight='bold', rotation=90)

plt.tight_layout()
plt.savefig('images/grammar_layers.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# 10. DATA x TASK x ENCODING FRAMEWORK
# ============================================================================
print("10. Creating Data × Task × Encoding framework...")
fig, ax = plt.subplots(figsize=(12, 5))
ax.set_xlim(0, 12)
ax.set_ylim(0, 4)
ax.axis('off')
ax.set_title('Data × Task × Encoding Framework', 
             fontsize=16, fontweight='bold', pad=20)

# Three boxes
boxes = [
    {'x': 1, 'label': 'Data Type', 'color': '#2E86AB',
     'examples': ['Nominal', 'Ordinal', 'Quantitative', 'Temporal']},
    {'x': 5, 'label': 'User Task', 'color': '#F18F01',
     'examples': ['Compare', 'Find trend', 'Identify outliers']},
    {'x': 9, 'label': 'Visual Encoding', 'color': '#E63946',
     'examples': ['Position', 'Length', 'Color', 'Shape']}
]

for box in boxes:
    rect = patches.FancyBboxPatch((box['x'], 2), 2, 1.5,
                                  boxstyle="round,pad=0.1",
                                  linewidth=3, edgecolor=box['color'],
                                  facecolor=box['color'], alpha=0.2)
    ax.add_patch(rect)
    ax.text(box['x'] + 1, 3.2, box['label'], fontsize=13, fontweight='bold',
           ha='center', va='top', color=box['color'])

# Plus signs
ax.text(3.8, 2.75, '+', fontsize=24, ha='center', va='center', fontweight='bold')
ax.text(7.8, 2.75, '=', fontsize=24, ha='center', va='center', fontweight='bold')

ax.text(6, 0.5, 'Always match all three components for effective visualization',
       ha='center', fontsize=11, style='italic', color='#666666')

plt.tight_layout()
plt.savefig('images/data_task_encoding.png', dpi=150, bbox_inches='tight')
plt.close()

print("\n✅ All images generated successfully in 'images/' directory!")
print("\nGenerated images:")
print("1. preattentive_popout.png")
print("2. gestalt_proximity.png")
print("3. gestalt_similarity.png")
print("4. gestalt_enclosure.png")
print("5. gestalt_connection.png")
print("6. cognitive_load_balance.png")
print("7. encoding_effectiveness.png")
print("8. data_types.png")
print("9. grammar_layers.png")
print("10. data_task_encoding.png")
