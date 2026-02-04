"""
Create additional diagrams to replace broken external links
- Data to Decision Pipeline
- Visual Processing Pathways
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

os.makedirs('images', exist_ok=True)

# ============================================================================
# 1. DATA TO DECISION PIPELINE
# ============================================================================
print("Creating Data to Decision Pipeline diagram...")
fig, ax = plt.subplots(figsize=(14, 5))
ax.set_xlim(0, 14)
ax.set_ylim(0, 5)
ax.axis('off')
ax.set_title('Data to Decision Pipeline: Visualization as Interface', 
             fontsize=16, fontweight='bold', pad=20)

# Pipeline stages
stages = [
    {'x': 1, 'label': 'Raw\nData', 'color': '#6C8EAD', 'icon': '📊'},
    {'x': 4, 'label': 'AI Model\n(Compute)', 'color': '#457B9D', 'icon': '🤖'},
    {'x': 7.5, 'label': 'Visualization\n(Interface)', 'color': '#E63946', 'icon': '📈'},
    {'x': 11, 'label': 'Human\nDecision', 'color': '#2E86AB', 'icon': '👤'}
]

for stage in stages:
    # Box
    box = FancyBboxPatch((stage['x']-0.8, 1.5), 1.6, 2,
                         boxstyle="round,pad=0.1",
                         linewidth=3, edgecolor=stage['color'],
                         facecolor=stage['color'], alpha=0.2)
    ax.add_patch(box)
    
    # Icon
    ax.text(stage['x'], 3, stage['icon'], fontsize=30, ha='center', va='center')
    
    # Label
    ax.text(stage['x'], 2.2, stage['label'], fontsize=11, fontweight='bold',
           ha='center', va='center', color=stage['color'])

# Arrows
arrow_style = FancyArrowPatch((2.2, 2.5), (3.2, 2.5),
                             arrowstyle='->', lw=3, color='#666666',
                             mutation_scale=30)
ax.add_patch(arrow_style)

arrow_style = FancyArrowPatch((5.6, 2.5), (6.7, 2.5),
                             arrowstyle='->', lw=3, color='#666666',
                             mutation_scale=30)
ax.add_patch(arrow_style)

arrow_style = FancyArrowPatch((9.1, 2.5), (10.2, 2.5),
                             arrowstyle='->', lw=3, color='#666666',
                             mutation_scale=30)
ax.add_patch(arrow_style)

# Key insight box
insight_box = patches.Rectangle((2, 0.2), 10, 0.8,
                               linewidth=2, edgecolor='#E63946',
                               facecolor='#FFE5E5', alpha=0.7)
ax.add_patch(insight_box)
ax.text(7, 0.6, '⚡ If visualization fails, the entire system fails at the decision layer',
       ha='center', fontsize=11, fontweight='bold', color='#E63946')

plt.tight_layout()
plt.savefig('images/data_decision_pipeline.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# 2. VISUAL PROCESSING PATHWAYS (Simplified)
# ============================================================================
print("Creating Visual Processing Pathways diagram...")
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_title('Two Pathways of Visual Processing', 
             fontsize=16, fontweight='bold', pad=20)

# Visual stimulus
stimulus_box = FancyBboxPatch((5, 8), 2, 1,
                             boxstyle="round,pad=0.1",
                             linewidth=3, edgecolor='#666666',
                             facecolor='#CCCCCC', alpha=0.3)
ax.add_patch(stimulus_box)
ax.text(6, 8.5, '👁️ Visual\nStimulus', fontsize=11, fontweight='bold',
       ha='center', va='center')

# Arrow down
ax.arrow(6, 7.8, 0, -0.5, head_width=0.3, head_length=0.2, fc='#666666', ec='#666666', lw=2)

# Split point
ax.plot([6, 6], [7.2, 6.8], 'k-', lw=3)
ax.plot([6, 3], [6.8, 6.3], 'k-', lw=2)
ax.plot([6, 9], [6.8, 6.3], 'k-', lw=2)

# LEFT: Preattentive (Early Vision)
preatt_box = FancyBboxPatch((1, 3.5), 4, 2.5,
                           boxstyle="round,pad=0.15",
                           linewidth=3, edgecolor='#2ECC71',
                           facecolor='#2ECC71', alpha=0.15)
ax.add_patch(preatt_box)

ax.text(3, 5.5, '⚡ PREATTENTIVE', fontsize=13, fontweight='bold',
       ha='center', color='#27AE60')
ax.text(3, 5, 'Early Vision', fontsize=11, ha='center', style='italic')

details = [
    '✓ Parallel processing',
    '✓ Fast (< 200ms)',
    '✓ Automatic',
    '✓ Detects features'
]
for i, detail in enumerate(details):
    ax.text(3, 4.4 - i*0.3, detail, fontsize=9, ha='center')

# Arrow to output
ax.arrow(3, 3.3, 0, -0.5, head_width=0.3, head_length=0.2, fc='#27AE60', ec='#27AE60', lw=2)

# RIGHT: Attentive (Late Vision)
att_box = FancyBboxPatch((7, 3.5), 4, 2.5,
                        boxstyle="round,pad=0.15",
                        linewidth=3, edgecolor='#E74C3C',
                        facecolor='#E74C3C', alpha=0.15)
ax.add_patch(att_box)

ax.text(9, 5.5, '⏱️ ATTENTIVE', fontsize=13, fontweight='bold',
       ha='center', color='#C0392B')
ax.text(9, 5, 'Late Vision', fontsize=11, ha='center', style='italic')

details = [
    '⚠ Serial processing',
    '⚠ Slow (requires focus)',
    '⚠ Conscious effort',
    '⚠ Integrates meaning'
]
for i, detail in enumerate(details):
    ax.text(9, 4.4 - i*0.3, detail, fontsize=9, ha='center')

# Arrow to output
ax.arrow(9, 3.3, 0, -0.5, head_width=0.3, head_length=0.2, fc='#C0392B', ec='#C0392B', lw=2)

# Output/Perception
output_box = FancyBboxPatch((4.5, 1), 3, 1.5,
                           boxstyle="round,pad=0.1",
                           linewidth=3, edgecolor='#9B59B6',
                           facecolor='#9B59B6', alpha=0.2)
ax.add_patch(output_box)
ax.text(6, 1.75, '🧠 Perception &\nUnderstanding', fontsize=12, fontweight='bold',
       ha='center', va='center', color='#8E44AD')

# Design principle box
principle_box = patches.Rectangle((1, 0.1), 10, 0.6,
                                 linewidth=2, edgecolor='#2ECC71',
                                 facecolor='#D5F4E6', alpha=0.8)
ax.add_patch(principle_box)
ax.text(6, 0.4, '💡 Design Principle: Use preattentive features for critical information',
       ha='center', fontsize=11, fontweight='bold', color='#27AE60')

plt.tight_layout()
plt.savefig('images/visual_processing_pathways.png', dpi=150, bbox_inches='tight')
plt.close()

# ============================================================================
# 3. VISUAL ATTENTION LIMITS (for Slide 7)
# ============================================================================
print("Creating Visual Attention diagram...")
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_title('Visual Attention is Limited', fontsize=16, fontweight='bold', pad=20)

# Central spotlight
spotlight = plt.Circle((5, 3), 1.5, color='#FFC107', alpha=0.3, linewidth=3, edgecolor='#FFC107')
ax.add_patch(spotlight)
ax.text(5, 3, '👁️\nFocus', fontsize=14, ha='center', va='center', fontweight='bold')

# Peripheral items (not attended)
peripheral_items = [
    (2, 5, '📊'), (8, 5, '📈'), (1.5, 2, '📉'),
    (8.5, 2, '🎯'), (3, 1, '💡'), (7, 1, '⚙️'),
    (1, 4, '📱'), (9, 4, '💻')
]

for x, y, icon in peripheral_items:
    ax.text(x, y, icon, fontsize=20, alpha=0.3, ha='center', va='center')

# Attention capacity label
capacity_box = patches.Rectangle((2, 0.3), 6, 0.8,
                                linewidth=2, edgecolor='#E74C3C',
                                facecolor='#FFE5E5', alpha=0.8)
ax.add_patch(capacity_box)
ax.text(5, 0.7, '⚠️ Attention Capacity: Only 3-4 objects simultaneously',
       ha='center', fontsize=11, fontweight='bold', color='#E74C3C')

# Key implications
implications = [
    '❌ Cannot attend to everything',
    '❌ Selective and focused',
    '⚡ Priority must be encoded visually'
]

for i, imp in enumerate(implications):
    ax.text(5, 5.2 - i*0.4, imp, fontsize=10, ha='center',
           bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

plt.tight_layout()
plt.savefig('images/attention_limits.png', dpi=150, bbox_inches='tight')
plt.close()

print("\n✅ Created 3 additional images:")
print("1. images/data_decision_pipeline.png - For Slide 2")
print("2. images/visual_processing_pathways.png - For Slide 4")
print("3. images/attention_limits.png - For Slide 7")
