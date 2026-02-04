"""
Create remaining 11 images to replace broken external links
All images designed for educational clarity and professional appearance
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch, Circle
import numpy as np
import os

os.makedirs('images', exist_ok=True)

print("Creating 11 remaining images for Class 3...\n")

# ============================================================================
# 1. SELECTIVE ATTENTION (Slide 7)
# ============================================================================
print("1. Creating Selective Attention diagram...")
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title('Visual Attention is Limited', fontsize=16, fontweight='bold', pad=20)

# Central focus area (spotlight)
spotlight = Circle((5, 5), 2, color='#FFC107', alpha=0.3, linewidth=4, edgecolor='#FFC107')
ax.add_patch(spotlight)
ax.text(5, 5, 'FOCUS\nArea', fontsize=14, ha='center', va='center', fontweight='bold')

# Peripheral items (faded)
items = [
    (2, 8, 'Chart'), (8, 8, 'Graph'), (1.5, 5, 'Data'),
    (8.5, 5, 'Metric'), (2, 2, 'Value'), (8, 2, 'KPI'),
    (1, 7, 'Info'), (9, 7, 'Stats'), (1, 3, 'Fig'), (9, 3, 'Plot')
]

for x, y, label in items:
    ax.text(x, y, label, fontsize=10, alpha=0.3, ha='center', va='center',
           bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.3))

# Capacity note
capacity_box = Rectangle((1, 0.3), 8, 0.9, linewidth=2, edgecolor='#E74C3C',
                         facecolor='#FFE5E5', alpha=0.8)
ax.add_patch(capacity_box)
ax.text(5, 0.75, 'Attention Capacity: Only 3-4 objects simultaneously',
       ha='center', fontsize=11, fontweight='bold', color='#E74C3C')

plt.tight_layout()
plt.savefig('images/selective_attention.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# 2. CHANGE BLINDNESS (Slide 8)
# ============================================================================
print("2. Creating Change Blindness example...")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

for idx, ax in enumerate(axes):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Dashboard elements
    title = 'Dashboard - Before' if idx == 0 else 'Dashboard - After'
    ax.text(5, 7.5, title, fontsize=14, fontweight='bold', ha='center')
    
    # Static elements
    rect1 = Rectangle((1, 5), 3, 1.5, facecolor='steelblue', alpha=0.3)
    ax.add_patch(rect1)
    ax.text(2.5, 5.75, 'Chart 1\n$2.5M', ha='center', va='center', fontsize=10)
    
    rect2 = Rectangle((6, 5), 3, 1.5, facecolor='green', alpha=0.3)
    ax.add_patch(rect2)
    ax.text(7.5, 5.75, 'Chart 2\n$3.1M', ha='center', va='center', fontsize=10)
    
    # Changing element
    if idx == 0:
        rect3 = Rectangle((1, 2.5), 3, 1.5, facecolor='orange', alpha=0.3)
        ax.add_patch(rect3)
        ax.text(2.5, 3.25, 'Chart 3\n$1.8M', ha='center', va='center', fontsize=10)
    else:
        rect3 = Rectangle((1, 2.5), 3, 1.5, facecolor='red', alpha=0.5, linewidth=3, edgecolor='red')
        ax.add_patch(rect3)
        ax.text(2.5, 3.25, 'Chart 3\n$0.9M', ha='center', va='center', fontsize=10, fontweight='bold')
        # Highlight the change
        ax.annotate('CHANGED!', xy=(2.5, 4.2), xytext=(2.5, 5.5),
                   arrowprops=dict(arrowstyle='->', color='red', lw=2),
                   fontsize=11, color='red', fontweight='bold', ha='center')
    
    rect4 = Rectangle((6, 2.5), 3, 1.5, facecolor='purple', alpha=0.3)
    ax.add_patch(rect4)
    ax.text(7.5, 3.25, 'Chart 4\n$2.2M', ha='center', va='center', fontsize=10)

# Note
fig.text(0.5, 0.02, 'Without directed attention, users often miss significant changes',
        ha='center', fontsize=11, style='italic')

plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.savefig('images/change_blindness.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# 3. INVISIBLE GORILLA / INATTENTIONAL BLINDNESS (Slide 9)
# ============================================================================
print("3. Creating Inattentional Blindness illustration...")
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title('Inattentional Blindness', fontsize=16, fontweight='bold', pad=20)

# Task focus (counting passes)
task_box = FancyBboxPatch((1, 6), 3.5, 2.5, boxstyle="round,pad=0.1",
                          linewidth=3, edgecolor='#2E86AB', facecolor='#2E86AB', alpha=0.2)
ax.add_patch(task_box)
ax.text(2.75, 7.8, 'TASK', fontsize=12, fontweight='bold', ha='center', color='#2E86AB')
ax.text(2.75, 7.2, 'Count the\npasses', fontsize=10, ha='center')

# Players passing
for i, pos in enumerate([(1.5, 6.5), (2.5, 6.8), (3.5, 6.5), (4, 7.2)]):
    circle = Circle(pos, 0.15, facecolor='steelblue', alpha=0.7)
    ax.add_patch(circle)

# Unexpected element (gorilla) - large and obvious but missed
gorilla_box = FancyBboxPatch((5.5, 6), 3.5, 2.5, boxstyle="round,pad=0.1",
                            linewidth=3, edgecolor='#E63946', facecolor='#E63946', alpha=0.2)
ax.add_patch(gorilla_box)
ax.text(7.25, 7.8, 'UNEXPECTED', fontsize=12, fontweight='bold', ha='center', color='#E63946')
ax.text(7.25, 7.2, 'Gorilla walks\nthrough scene', fontsize=10, ha='center')
ax.text(7.25, 6.5, '50% MISS THIS!', fontsize=11, ha='center', fontweight='bold', color='#E63946')

# Lesson
lesson_box = Rectangle((1.5, 3.5), 7, 1.5, linewidth=2, edgecolor='#666',
                       facecolor='#F5F5F5', alpha=0.9)
ax.add_patch(lesson_box)
ax.text(5, 4.5, 'Lesson for Visualization:', fontsize=12, fontweight='bold', ha='center')
ax.text(5, 3.9, 'Users focused on one task will miss other information', fontsize=10, ha='center')

# Design principle
principle_box = Rectangle((1.5, 1.5), 7, 1.2, linewidth=2, edgecolor='#2ECC71',
                         facecolor='#D5F4E6', alpha=0.8)
ax.add_patch(principle_box)
ax.text(5, 2.2, 'Make critical information impossible to miss', fontsize=11,
       fontweight='bold', ha='center', color='#27AE60')

plt.tight_layout()
plt.savefig('images/inattentional_blindness.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# 4. GESTALT PRINCIPLES OVERVIEW (Slide 10)
# ============================================================================
print("4. Creating Gestalt Principles Overview...")
fig, axes = plt.subplots(2, 3, figsize=(14, 10))
fig.suptitle('Gestalt Principles of Grouping', fontsize=16, fontweight='bold')

principles = [
    ('Proximity', 'Objects close together\nare grouped'),
    ('Similarity', 'Similar objects\nare grouped'),
    ('Enclosure', 'Enclosed objects\nare grouped'),
    ('Connection', 'Connected objects\nare grouped'),
    ('Continuity', 'Smooth paths\nare grouped'),
    ('Closure', 'We complete\nincomplete shapes')
]

for idx, (ax, (title, desc)) in enumerate(zip(axes.flat, principles)):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title(title, fontsize=12, fontweight='bold', pad=10)
    
    if idx == 0:  # Proximity
        for group in range(3):
            for i in range(3):
                for j in range(3):
                    circle = Circle((1.5 + group*3 + i*0.4, 5 + j*0.4), 0.15, facecolor='#2E86AB')
                    ax.add_patch(circle)
    
    elif idx == 1:  # Similarity
        for i in range(5):
            for j in range(4):
                color = '#2E86AB' if i % 2 == 0 else '#E63946'
                circle = Circle((2 + i*1.5, 4 + j*1.2), 0.2, facecolor=color)
                ax.add_patch(circle)
    
    elif idx == 2:  # Enclosure
        rect1 = Rectangle((1, 4), 3.5, 3, linewidth=2, edgecolor='#2E86AB', facecolor='#2E86AB', alpha=0.1)
        ax.add_patch(rect1)
        for i in range(4):
            circle = Circle((2.5 + (i%2)*1, 5.5 + (i//2)*1), 0.2, facecolor='#2E86AB')
            ax.add_patch(circle)
        
        rect2 = Rectangle((5.5, 4), 3.5, 3, linewidth=2, edgecolor='#E63946', facecolor='#E63946', alpha=0.1)
        ax.add_patch(rect2)
        for i in range(4):
            circle = Circle((7 + (i%2)*1, 5.5 + (i//2)*1), 0.2, facecolor='#E63946')
            ax.add_patch(circle)
    
    elif idx == 3:  # Connection
        points = [(2, 5), (3, 6), (4, 5.5), (5, 6.5)]
        for i in range(len(points)-1):
            ax.plot([points[i][0], points[i+1][0]], [points[i][1], points[i+1][1]],
                   'o-', color='#2E86AB', markersize=10, linewidth=2)
        
        for x in [6.5, 8]:
            circle = Circle((x, 5.5), 0.3, facecolor='#CCCCCC')
            ax.add_patch(circle)
    
    elif idx == 4:  # Continuity
        t = np.linspace(0, 2*np.pi, 100)
        x1 = 3 + 2*np.cos(t)
        y1 = 5 + 2*np.sin(t)
        ax.plot(x1[:50], y1[:50], color='#2E86AB', linewidth=3)
        ax.plot(x1[50:], y1[50:], color='#E63946', linewidth=3)
    
    elif idx == 5:  # Closure
        # Incomplete circle
        t = np.linspace(0, 1.5*np.pi, 50)
        x = 5 + 2*np.cos(t)
        y = 5 + 2*np.sin(t)
        ax.plot(x, y, color='#2E86AB', linewidth=4)
    
    ax.text(5, 2, desc, ha='center', fontsize=9, style='italic')

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig('images/gestalt_overview.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# 5. ORDINAL DATA ENCODING (Slide 25)
# ============================================================================
print("5. Creating Ordinal Data example...")
fig, ax = plt.subplots(figsize=(10, 6))

categories = ['High School', "Bachelor's", "Master's", 'PhD']
values = [25, 35, 28, 12]
colors = ['#E8F4F8', '#A8DADC', '#457B9D', '#1D3557']  # Sequential

bars = ax.barh(categories, values, color=colors, edgecolor='black', linewidth=1.5)

ax.set_xlabel('Percentage of Employees', fontsize=12, fontweight='bold')
ax.set_title('Ordinal Data: Education Level\n(Sequential Color Encoding)', fontsize=14, fontweight='bold', pad=15)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

for i, v in enumerate(values):
    ax.text(v + 1, i, f'{v}%', va='center', fontsize=11, fontweight='bold')

ax.text(5, -0.8, 'Note: Sequential colors match ordinal progression', 
        ha='center', fontsize=10, style='italic', color='#666')

plt.tight_layout()
plt.savefig('images/ordinal_data.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# 6. QUANTITATIVE ENCODINGS (Slide 26)
# ============================================================================
print("6. Creating Quantitative Encodings comparison...")
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Quantitative Data Encodings', fontsize=16, fontweight='bold')

data = [45, 65, 55, 80, 50]
labels = ['A', 'B', 'C', 'D', 'E']

# Position (Best)
axes[0,0].bar(labels, data, color='#2E86AB', alpha=0.7)
axes[0,0].set_title('Position on Common Scale\n(BEST for comparison)', fontsize=11, fontweight='bold', color='green')
axes[0,0].set_ylabel('Value')
axes[0,0].spines['top'].set_visible(False)
axes[0,0].spines['right'].set_visible(False)

# Length
for i, (label, val) in enumerate(zip(labels, data)):
    axes[0,1].barh(i, val, color='#457B9D', alpha=0.7)
axes[0,1].set_yticks(range(len(labels)))
axes[0,1].set_yticklabels(labels)
axes[0,1].set_title('Length\n(Good for comparison)', fontsize=11, fontweight='bold')
axes[0,1].set_xlabel('Value')
axes[0,1].spines['top'].set_visible(False)
axes[0,1].spines['right'].set_visible(False)

# Area (Harder)
for i, (x, val) in enumerate(zip(range(5), data)):
    radius = np.sqrt(val/np.pi) * 0.3
    circle = Circle((x, 0), radius, facecolor='#A8DADC', alpha=0.7, edgecolor='black')
    axes[1,0].add_patch(circle)
    axes[1,0].text(x, -0.8, labels[i], ha='center')
axes[1,0].set_xlim(-1, 5)
axes[1,0].set_ylim(-1, 2)
axes[1,0].set_title('Area\n(Difficult to compare precisely)', fontsize=11, fontweight='bold', color='orange')
axes[1,0].axis('off')

# Color Intensity (Weakest)
colors_intensity = plt.cm.Blues(np.array(data)/100)
axes[1,1].bar(labels, [1]*5, color=colors_intensity, width=0.8)
axes[1,1].set_title('Color Intensity\n(Poor for precise comparison)', fontsize=11, fontweight='bold', color='red')
axes[1,1].set_ylim(0, 1.2)
axes[1,1].set_yticks([])
axes[1,1].spines['top'].set_visible(False)
axes[1,1].spines['right'].set_visible(False)
axes[1,1].spines['left'].set_visible(False)

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig('images/quantitative_encodings.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# 7. TIME SERIES EXAMPLE (Slide 27)
# ============================================================================
print("7. Creating Time Series example...")
fig, ax = plt.subplots(figsize=(12, 6))

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_2024 = [45, 48, 52, 49, 55, 58, 54, 57, 62, 59, 65, 68]
sales_2025 = [47, 51, 56, 54, 60, 65, 62, 66, 72, 69, 75, 80]

ax.plot(months, sales_2024, marker='o', linewidth=2.5, label='2024', color='#6C8EAD', markersize=6)
ax.plot(months, sales_2025, marker='s', linewidth=2.5, label='2025', color='#E63946', markersize=6)

ax.set_xlabel('Month', fontsize=12, fontweight='bold')
ax.set_ylabel('Sales ($K)', fontsize=12, fontweight='bold')
ax.set_title('Temporal Data: Monthly Sales Trends', fontsize=14, fontweight='bold', pad=15)

ax.legend(loc='upper left', frameon=True, fontsize=11)
ax.grid(True, alpha=0.3, linestyle='--')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add trend annotation
ax.annotate('Strong Growth', xy=('Dec', 80), xytext=('Oct', 85),
           arrowprops=dict(arrowstyle='->', color='#E63946', lw=2),
           fontsize=11, color='#E63946', fontweight='bold')

plt.tight_layout()
plt.savefig('images/time_series.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# 8. BERTIN VISUAL VARIABLES (Slide 28)
# ============================================================================
print("8. Creating Bertin Visual Variables diagram...")
fig, ax = plt.subplots(figsize=(12, 10))
ax.set_xlim(0, 12)
ax.set_ylim(0, 14)
ax.axis('off')
ax.set_title("Bertin's Visual Variables (1967)", fontsize=16, fontweight='bold', pad=20)

variables = [
    ('Position', 12, 'x, y coordinates'),
    ('Size', 10.5, 'length, area, volume'),
    ('Value', 9, 'lightness/darkness'),
    ('Texture', 7.5, 'pattern, grain'),
    ('Color', 6, 'hue'),
    ('Orientation', 4.5, 'angle, direction'),
    ('Shape', 3, 'form, symbol')
]

for i, (name, y, desc) in enumerate(variables):
    # Box
    box = FancyBboxPatch((1, y-0.6), 10, 1.2, boxstyle="round,pad=0.1",
                        linewidth=2, edgecolor='#2E86AB', facecolor='#E8F4F8', alpha=0.5)
    ax.add_patch(box)
    
    # Variable name
    ax.text(2, y, f'{i+1}. {name}', fontsize=13, fontweight='bold', va='center')
    
    # Description
    ax.text(9, y, desc, fontsize=10, va='center', style='italic', color='#666')
    
    # Visual example
    if name == 'Position':
        ax.plot([4.5, 5.5, 6.5], [y, y+0.3, y], 'o', color='#2E86AB', markersize=8)
    elif name == 'Size':
        for j, size in enumerate([6, 10, 14]):
            ax.plot(5 + j*0.6, y, 'o', color='#2E86AB', markersize=size)
    elif name == 'Value':
        for j, alpha in enumerate([0.3, 0.6, 0.9]):
            circle = Circle((5 + j*0.6, y), 0.15, facecolor='#2E86AB', alpha=alpha)
            ax.add_patch(circle)
    elif name == 'Texture':
        for j, pattern in enumerate(['/', '\\', '.']):
            rect = Rectangle((4.8 + j*0.6, y-0.15), 0.3, 0.3, facecolor='#2E86AB', hatch=pattern, alpha=0.5)
            ax.add_patch(rect)
    elif name == 'Color':
        for j, color in enumerate(['#E63946', '#F18F01', '#2E86AB']):
            circle = Circle((5 + j*0.6, y), 0.15, facecolor=color)
            ax.add_patch(circle)
    elif name == 'Orientation':
        for j, angle in enumerate([0, 45, 90]):
            rect = Rectangle((4.9 + j*0.6, y-0.1), 0.4, 0.1, facecolor='#2E86AB', 
                           angle=angle, rotation_point='center')
            ax.add_patch(rect)
    elif name == 'Shape':
        shapes = ['o', 's', '^']
        for j, shape in enumerate(shapes):
            ax.plot(5 + j*0.6, y, shape, color='#2E86AB', markersize=12)

# Note at bottom
note_box = Rectangle((1, 0.5), 10, 1, linewidth=2, edgecolor='#666',
                     facecolor='#F5F5F5', alpha=0.9)
ax.add_patch(note_box)
ax.text(6, 1, 'Not all variables are equally effective for all data types',
       ha='center', fontsize=11, style='italic')

plt.tight_layout()
plt.savefig('images/bertin_variables.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# 9. CLEVELAND & McGILL EXPERIMENT (Slide 29)
# ============================================================================
print("9. Creating Cleveland & McGill Experiment illustration...")
fig, axes = plt.subplots(1, 3, figsize=(14, 5))
fig.suptitle("Cleveland & McGill's Graphical Perception Study (1984)", 
            fontsize=14, fontweight='bold')

# Position - Most Accurate
values = [30, 70]
axes[0].bar(['A', 'B'], values, color=['#CCCCCC', '#2E86AB'], width=0.6)
axes[0].set_ylim(0, 100)
axes[0].set_title('Position on Common Scale\n(Most Accurate)', fontsize=11, fontweight='bold', color='green')
axes[0].set_ylabel('Value')
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)

# Angle - Less Accurate
sizes = [30, 70]
colors_pie = ['#CCCCCC', '#2E86AB']
axes[1].pie(sizes, colors=colors_pie, startangle=90, counterclock=False)
axes[1].set_title('Angle (Pie Chart)\n(Less Accurate)', fontsize=11, fontweight='bold', color='orange')

# Area - Least Accurate
areas = [30, 70]
for i, (val, color) in enumerate(zip(areas, ['#CCCCCC', '#2E86AB'])):
    radius = np.sqrt(val/np.pi) * 0.3
    circle = Circle((i*2 + 1, 0), radius, facecolor=color, edgecolor='black', linewidth=2)
    axes[2].add_patch(circle)
axes[2].set_xlim(-0.5, 3.5)
axes[2].set_ylim(-1, 1)
axes[2].set_title('Area (Bubbles)\n(Least Accurate)', fontsize=11, fontweight='bold', color='red')
axes[2].axis('off')

# Question
fig.text(0.5, 0.02, 'Question: "What percentage is the smaller of the larger?"',
        ha='center', fontsize=11, fontweight='bold')

plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.savefig('images/cleveland_mcgill.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# 10. COLOR PERCEPTION ISSUES (Slide 31)
# ============================================================================
print("10. Creating Color Perception Issues diagram...")
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Why Color is Weak for Quantitative Data', fontsize=16, fontweight='bold')

# Non-linear perception
data = np.linspace(0, 1, 100).reshape(10, 10)
axes[0,0].imshow(data, cmap='gray', aspect='auto')
axes[0,0].set_title('Non-Linear Perception\n(Equal steps look unequal)', fontsize=11, fontweight='bold')
axes[0,0].set_xticks([])
axes[0,0].set_yticks([])

# Context dependency
axes[0,1].set_xlim(0, 10)
axes[0,1].set_ylim(0, 10)
axes[0,1].axis('off')
axes[0,1].set_title('Context Dependency\n(Same gray looks different)', fontsize=11, fontweight='bold')
rect1 = Rectangle((1, 3), 3, 4, facecolor='black')
axes[0,1].add_patch(rect1)
rect2 = Rectangle((2, 4), 1, 2, facecolor='gray')
axes[0,1].add_patch(rect2)
rect3 = Rectangle((6, 3), 3, 4, facecolor='white', edgecolor='black')
axes[0,1].add_patch(rect3)
rect4 = Rectangle((7, 4), 1, 2, facecolor='gray')
axes[0,1].add_patch(rect4)

# Color blindness simulation
x = np.arange(5)
colors_normal = ['#E63946', '#F18F01', '#00B894', '#0984E3', '#6C5CE7']
axes[1,0].bar(x, [1]*5, color=colors_normal, width=0.8)
axes[1,0].set_title('Normal Vision\n(5 distinct colors)', fontsize=11, fontweight='bold')
axes[1,0].set_ylim(0, 1.2)
axes[1,0].set_xticks([])
axes[1,0].set_yticks([])

# Deuteranopia simulation (red-green colorblind)
colors_blind = ['#C49B6C', '#C49B6C', '#00B894', '#0984E3', '#6C5CE7']
axes[1,1].bar(x, [1]*5, color=colors_blind, width=0.8)
axes[1,1].set_title('Deuteranopia (8% of males)\n(Red & orange look similar)', 
                   fontsize=11, fontweight='bold', color='#E63946')
axes[1,1].set_ylim(0, 1.2)
axes[1,1].set_xticks([])
axes[1,1].set_yticks([])

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('images/color_perception.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# 11. MATPLOTLIB ANATOMY (Slide 47) - CLEAN VERSION
# ============================================================================
print("11. Creating clean Matplotlib Anatomy diagram...")
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# Title
fig.suptitle('Matplotlib Anatomy', fontsize=16, fontweight='bold')

# Plot some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y, 'b-', linewidth=2, label='Sample Data')

# Labels
ax.set_xlabel('X Axis', fontsize=12, fontweight='bold')
ax.set_ylabel('Y Axis', fontsize=12, fontweight='bold')
ax.set_title('Axes Title', fontsize=13, fontweight='bold', pad=15)
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

# Annotations pointing to components
bbox_props = dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7)

# Figure annotation
ax.annotate('Figure\n(entire canvas)', xy=(1, 0.8), xytext=(1.5, 1.2),
           fontsize=10, fontweight='bold', bbox=bbox_props,
           arrowprops=dict(arrowstyle='->', lw=2, color='red'))

# Axes annotation
ax.annotate('Axes\n(plot area)', xy=(5, 0), xytext=(7, -0.5),
           fontsize=10, fontweight='bold', bbox=bbox_props,
           arrowprops=dict(arrowstyle='->', lw=2, color='red'))

# X-axis annotation
ax.annotate('X-Axis', xy=(5, -1.2), xytext=(2, -1.5),
           fontsize=10, fontweight='bold', bbox=bbox_props,
           arrowprops=dict(arrowstyle='->', lw=2, color='red'))

# Y-axis annotation
ax.annotate('Y-Axis', xy=(-0.3, 0), xytext=(-1, 0.5),
           fontsize=10, fontweight='bold', bbox=bbox_props,
           arrowprops=dict(arrowstyle='->', lw=2, color='red'))

# Line annotation
ax.annotate('Line\n(Artist)', xy=(8, np.sin(8)), xytext=(6, 0.7),
           fontsize=10, fontweight='bold', bbox=bbox_props,
           arrowprops=dict(arrowstyle='->', lw=2, color='red'))

# Title annotation
ax.annotate('Title', xy=(5, 1.2), xytext=(3, 1.4),
           fontsize=10, fontweight='bold', bbox=bbox_props,
           arrowprops=dict(arrowstyle='->', lw=2, color='red'))

# Legend annotation
ax.annotate('Legend', xy=(9, 0.9), xytext=(8.5, 0.5),
           fontsize=10, fontweight='bold', bbox=bbox_props,
           arrowprops=dict(arrowstyle='->', lw=2, color='red'))

plt.tight_layout()
plt.savefig('images/matplotlib_anatomy.png', dpi=150, bbox_inches='tight')
plt.close()

print("\n✅ All 11 images created successfully!")
print("\nGenerated images:")
print("1. selective_attention.png")
print("2. change_blindness.png")
print("3. inattentional_blindness.png")
print("4. gestalt_overview.png")
print("5. ordinal_data.png")
print("6. quantitative_encodings.png")
print("7. time_series.png")
print("8. bertin_variables.png")
print("9. cleveland_mcgill.png")
print("10. color_perception.png")
print("11. matplotlib_anatomy.png")
