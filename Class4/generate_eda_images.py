"""
Generate all conceptual images for Class 4 - Exploratory Data Visualization
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch
import warnings
warnings.filterwarnings('ignore')

print("Generating EDA conceptual images...")
print("="*70)

# Set style
plt.style.use('default')
sns.set_palette("husl")

# Create images directory if it doesn't exist
import os
os.makedirs('images', exist_ok=True)

# =============================================================================
# 1. EDA CYCLE
# =============================================================================
print("\n1. Creating EDA Cycle diagram...")

fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(5, 9.5, 'The EDA Cycle', fontsize=20, fontweight='bold', ha='center')

# Circle positions
centers = [(5, 5)]
radius = 3

# Draw circular flow
angles = [90, 0, -90, -180]  # Top, Right, Bottom, Left
labels = ['Ask\nQuestions', 'Visualize\nData', 'Discover\nPatterns', 'Generate\nHypotheses']
colors = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12']

for i, (angle, label, color) in enumerate(zip(angles, labels, colors)):
    # Calculate position
    rad = np.radians(angle)
    x = 5 + radius * np.cos(rad)
    y = 5 + radius * np.sin(rad)
    
    # Draw circle
    circle = Circle((x, y), 0.8, color=color, alpha=0.3, ec=color, linewidth=3)
    ax.add_patch(circle)
    
    # Add label
    ax.text(x, y, label, fontsize=11, ha='center', va='center', fontweight='bold')
    
    # Draw arrows
    next_angle = angles[(i + 1) % len(angles)]
    next_rad = np.radians(next_angle)
    x2 = 5 + radius * np.cos(next_rad)
    y2 = 5 + radius * np.sin(next_rad)
    
    # Arrow from current to next
    arrow = FancyArrowPatch((x + 0.6*np.cos(rad), y + 0.6*np.sin(rad)),
                           (x2 - 0.6*np.cos(next_rad), y2 - 0.6*np.sin(next_rad)),
                           arrowstyle='->', mutation_scale=30, linewidth=3,
                           color='gray', alpha=0.6)
    ax.add_patch(arrow)

# Center text
ax.text(5, 5, 'Iterative\nProcess', fontsize=13, ha='center', va='center',
        fontweight='bold', style='italic')

plt.tight_layout()
plt.savefig('images/eda_cycle.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: eda_cycle.png")

# =============================================================================
# 2. EDA WORKFLOW
# =============================================================================
print("\n2. Creating EDA Workflow diagram...")

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_xlim(0, 14)
ax.set_ylim(0, 8)
ax.axis('off')

# Title
ax.text(7, 7.5, 'EDA in the Data Science Lifecycle', fontsize=18, fontweight='bold', ha='center')

# Workflow boxes
stages = ['Data\nCollection', 'Data\nCleaning', 'EDA', 'Feature\nEngineering', 
          'Modeling', 'Evaluation', 'Deployment']
x_positions = np.linspace(1, 13, len(stages))
colors_wf = ['lightblue', 'lightgreen', '#FFD700', 'lightcoral', 'plum', 'lightyellow', 'lightgray']

for i, (stage, x, color) in enumerate(zip(stages, x_positions, colors_wf)):
    # Box
    width = 1.5
    height = 1.2
    if stage == 'EDA':
        # Highlight EDA
        rect = FancyBboxPatch((x-width/2, 3-height/2), width, height,
                              boxstyle="round,pad=0.1", 
                              edgecolor='red', facecolor=color, linewidth=3)
    else:
        rect = Rectangle((x-width/2, 3-height/2), width, height,
                        edgecolor='black', facecolor=color, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(x, 3, stage, fontsize=10, ha='center', va='center', fontweight='bold')
    
    # Arrow to next
    if i < len(stages) - 1:
        ax.arrow(x + width/2, 3, x_positions[i+1] - x - width, 0,
                head_width=0.2, head_length=0.1, fc='black', ec='black')

# Feedback loops
ax.annotate('', xy=(3.5, 2.5), xytext=(5.5, 2.5),
            arrowprops=dict(arrowstyle='<->', color='blue', lw=2, linestyle='--'))
ax.text(4.5, 2.2, 'EDA informs\ncleaning', fontsize=8, ha='center', color='blue')

ax.annotate('', xy=(7, 2.5), xytext=(5.5, 2.5),
            arrowprops=dict(arrowstyle='<->', color='green', lw=2, linestyle='--'))
ax.text(6.25, 2.2, 'EDA guides\nfeatures', fontsize=8, ha='center', color='green')

plt.tight_layout()
plt.savefig('images/eda_workflow.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: eda_workflow.png")

# =============================================================================
# 3. TASK-VISUALIZATION MATRIX
# =============================================================================
print("\n3. Creating Task-Visualization Matrix...")

fig, ax = plt.subplots(figsize=(12, 8))

# Data for matrix
tasks = ['Distribution', 'Comparison', 'Relationship', 'Composition',
         'Ranking', 'Deviation', 'Correlation', 'Time']
visualizations = ['Histogram/Box Plot', 'Side-by-side Plots', 'Scatter Plot',
                 'Stacked Bars', 'Horizontal Bars', 'Bar + Reference',
                 'Heatmap', 'Line Chart']
colors_matrix = plt.cm.Set3(np.linspace(0, 1, len(tasks)))

y_pos = np.arange(len(tasks))[::-1]

for i, (task, viz, color) in enumerate(zip(tasks, visualizations, colors_matrix)):
    # Task box
    rect = FancyBboxPatch((0.5, y_pos[i]-0.3), 2, 0.6,
                          boxstyle="round,pad=0.05",
                          edgecolor='black', facecolor=color, linewidth=2)
    ax.add_patch(rect)
    ax.text(1.5, y_pos[i], task, fontsize=11, ha='center', va='center', fontweight='bold')
    
    # Arrow
    ax.arrow(2.6, y_pos[i], 0.6, 0, head_width=0.15, head_length=0.1,
            fc='gray', ec='gray', linewidth=2)
    
    # Visualization box
    rect2 = FancyBboxPatch((3.3, y_pos[i]-0.3), 3, 0.6,
                           boxstyle="round,pad=0.05",
                           edgecolor='darkgreen', facecolor='lightgreen', linewidth=1.5)
    ax.add_patch(rect2)
    ax.text(4.8, y_pos[i], viz, fontsize=10, ha='center', va='center')

ax.set_xlim(0, 7)
ax.set_ylim(-1, len(tasks))
ax.axis('off')
ax.set_title('EDA Task → Visualization Mapping', fontsize=16, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('images/task_viz_matrix.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: task_viz_matrix.png")

# =============================================================================
# 4. DATA QUALITY ISSUES
# =============================================================================
print("\n4. Creating Data Quality Issues diagram...")

fig, ax = plt.subplots(figsize=(12, 10))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(6, 9.5, 'Common Data Quality Issues', fontsize=18, fontweight='bold', ha='center')

issues = [
    ('Missing Values', 'Nulls, NaN, -999', '#e74c3c'),
    ('Duplicates', 'Exact or near-duplicates', '#3498db'),
    ('Inconsistencies', 'Mixed formats, typos', '#9b59b6'),
    ('Outliers', 'Errors vs. extremes', '#f39c12'),
    ('Skewed Distributions', 'Need transformation', '#2ecc71'),
    ('Imbalanced Classes', 'Majority dominance', '#e67e22'),
    ('Data Leakage', 'Future information', '#c0392b'),
    ('Encoding Issues', 'Wrong data types', '#16a085')
]

positions = [(2, 7), (6, 7), (10, 7), (2, 4.5), (6, 4.5), (10, 4.5), (4, 2), (8, 2)]

for (issue, desc, color), (x, y) in zip(issues, positions):
    # Box
    rect = FancyBboxPatch((x-1.3, y-0.6), 2.6, 1.2,
                          boxstyle="round,pad=0.1",
                          edgecolor=color, facecolor=color, alpha=0.3, linewidth=3)
    ax.add_patch(rect)
    ax.text(x, y+0.25, issue, fontsize=11, ha='center', va='center', fontweight='bold')
    ax.text(x, y-0.15, desc, fontsize=9, ha='center', va='center', style='italic')

plt.tight_layout()
plt.savefig('images/data_quality_issues.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: data_quality_issues.png")

# =============================================================================
# 5. DISTRIBUTION SHAPES
# =============================================================================
print("\n5. Creating Distribution Shapes examples...")

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Common Distribution Shapes', fontsize=16, fontweight='bold')

# Normal
x_norm = np.random.normal(0, 1, 1000)
axes[0, 0].hist(x_norm, bins=30, edgecolor='black', alpha=0.7, color='steelblue')
axes[0, 0].set_title('Normal (Gaussian)\nSymmetric, bell-shaped')
axes[0, 0].set_ylabel('Frequency')

# Right-skewed
x_rskew = np.random.exponential(2, 1000)
axes[0, 1].hist(x_rskew, bins=30, edgecolor='black', alpha=0.7, color='coral')
axes[0, 1].set_title('Right-Skewed\nLong tail on right')

# Left-skewed
x_lskew = 10 - np.random.exponential(2, 1000)
axes[0, 2].hist(x_lskew, bins=30, edgecolor='black', alpha=0.7, color='lightgreen')
axes[0, 2].set_title('Left-Skewed\nLong tail on left')

# Bimodal
x_bimodal = np.concatenate([np.random.normal(-2, 0.5, 500), np.random.normal(2, 0.5, 500)])
axes[1, 0].hist(x_bimodal, bins=30, edgecolor='black', alpha=0.7, color='plum')
axes[1, 0].set_title('Bimodal\nTwo peaks')
axes[1, 0].set_xlabel('Value')
axes[1, 0].set_ylabel('Frequency')

# Uniform
x_uniform = np.random.uniform(0, 10, 1000)
axes[1, 1].hist(x_uniform, bins=30, edgecolor='black', alpha=0.7, color='gold')
axes[1, 1].set_title('Uniform\nFlat distribution')
axes[1, 1].set_xlabel('Value')

# Long-tailed
x_longtail = np.random.pareto(1.5, 1000)
axes[1, 2].hist(x_longtail, bins=30, edgecolor='black', alpha=0.7, color='lightcoral')
axes[1, 2].set_title('Long-Tailed\nHeavy tails, outliers')
axes[1, 2].set_xlabel('Value')

plt.tight_layout()
plt.savefig('images/distribution_shapes.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: distribution_shapes.png")

print("\n" + "="*70)
print("✅ PART 1 COMPLETE: Generated 5 core conceptual images")
print("="*70)
print("\nContinuing with remaining images...")

# =============================================================================
# 6. DISTRIBUTION VISUALIZATION COMPARISON
# =============================================================================
print("\n6. Creating Distribution Visualization Comparison...")

np.random.seed(42)
data = np.random.exponential(2, 1000)

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Choosing the Right Distribution Visualization', fontsize=16, fontweight='bold')

# Histogram
axes[0, 0].hist(data, bins=30, edgecolor='black', alpha=0.7, color='steelblue')
axes[0, 0].set_title('Histogram\n✅ Shows shape clearly\n⚠️ Bin width sensitive')
axes[0, 0].set_ylabel('Frequency')

# KDE
from scipy import stats
kde = stats.gaussian_kde(data)
x_range = np.linspace(data.min(), data.max(), 200)
axes[0, 1].plot(x_range, kde(x_range), linewidth=2, color='coral')
axes[0, 1].fill_between(x_range, kde(x_range), alpha=0.3, color='coral')
axes[0, 1].set_title('KDE\n✅ Smooth curve\n⚠️ Can oversmooth')

# Box plot
axes[0, 2].boxplot(data, vert=True)
axes[0, 2].set_title('Box Plot\n✅ Shows quartiles & outliers\n❌ Hides shape')

# Violin plot
parts = axes[1, 0].violinplot([data], positions=[0], showmeans=True, showmedians=True)
axes[1, 0].set_title('Violin Plot\n✅ Combines box + KDE\n✅ Best for groups')
axes[1, 0].set_xticks([])

# ECDF
sorted_data = np.sort(data)
y = np.arange(1, len(sorted_data)+1) / len(sorted_data)
axes[1, 1].plot(sorted_data, y, linewidth=2, color='green')
axes[1, 1].set_title('ECDF\n✅ Shows exact percentiles\n⚠️ Less intuitive')
axes[1, 1].set_ylabel('Cumulative Probability')

# Summary
axes[1, 2].axis('off')
axes[1, 2].text(0.5, 0.7, 'Key Takeaways:', fontsize=12, ha='center', fontweight='bold')
axes[1, 2].text(0.1, 0.5, '• Histogram: Quick overview\n• KDE: Smooth visualization\n• Box: Outlier detection\n• Violin: Group comparison\n• ECDF: Precise percentiles', 
                fontsize=10, va='top')

plt.tight_layout()
plt.savefig('images/distribution_viz_comparison.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: distribution_viz_comparison.png")

# =============================================================================
# 7. UNIVARIATE NUMERIC EXAMPLE
# =============================================================================
print("\n7. Creating Univariate Numeric Example...")

np.random.seed(42)
price = np.random.lognormal(12, 0.5, 1000)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Univariate Analysis: House Prices', fontsize=16, fontweight='bold')

# Histogram with mean and median
axes[0, 0].hist(price, bins=50, edgecolor='black', alpha=0.7, color='steelblue')
axes[0, 0].axvline(price.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: ${price.mean()/1000:.0f}K')
axes[0, 0].axvline(np.median(price), color='green', linestyle='--', linewidth=2, label=f'Median: ${np.median(price)/1000:.0f}K')
axes[0, 0].set_title('Histogram with Central Tendency')
axes[0, 0].set_xlabel('Price ($)')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].legend()

# Box plot
axes[0, 1].boxplot(price, vert=True)
axes[0, 1].set_title(f'Box Plot\nSkewness: {stats.skew(price):.2f}')
axes[0, 1].set_ylabel('Price ($)')

# KDE
axes[1, 0].hist(price, bins=50, density=True, alpha=0.5, color='lightblue', edgecolor='black')
kde = stats.gaussian_kde(price)
x_range = np.linspace(price.min(), price.max(), 200)
axes[1, 0].plot(x_range, kde(x_range), 'r-', linewidth=2, label='KDE')
axes[1, 0].set_title('Histogram + KDE')
axes[1, 0].set_xlabel('Price ($)')
axes[1, 0].set_ylabel('Density')
axes[1, 0].legend()

# Q-Q plot
stats.probplot(price, dist="norm", plot=axes[1, 1])
axes[1, 1].set_title('Q-Q Plot (Normality Check)')
axes[1, 1].get_lines()[0].set_markerfacecolor('steelblue')
axes[1, 1].get_lines()[0].set_markersize(4)

plt.tight_layout()
plt.savefig('images/univariate_numeric.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: univariate_numeric.png")

# =============================================================================
# 8. SKEWNESS TRANSFORMATIONS
# =============================================================================
print("\n8. Creating Skewness Transformations example...")

np.random.seed(42)
data_skewed = np.random.exponential(2, 1000)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Transforming Skewed Data', fontsize=16, fontweight='bold')

# Original
axes[0, 0].hist(data_skewed, bins=30, edgecolor='black', alpha=0.7, color='coral')
axes[0, 0].set_title(f'Original\nSkewness: {stats.skew(data_skewed):.2f}')
axes[0, 0].set_ylabel('Frequency')

# Log transform
data_log = np.log(data_skewed + 1)
axes[0, 1].hist(data_log, bins=30, edgecolor='black', alpha=0.7, color='steelblue')
axes[0, 1].set_title(f'Log Transform\nSkewness: {stats.skew(data_log):.2f}')

# Square root
data_sqrt = np.sqrt(data_skewed)
axes[1, 0].hist(data_sqrt, bins=30, edgecolor='black', alpha=0.7, color='lightgreen')
axes[1, 0].set_title(f'Square Root Transform\nSkewness: {stats.skew(data_sqrt):.2f}')
axes[1, 0].set_xlabel('Transformed Value')
axes[1, 0].set_ylabel('Frequency')

# Box-Cox
data_boxcox, lambda_param = stats.boxcox(data_skewed + 1)
axes[1, 1].hist(data_boxcox, bins=30, edgecolor='black', alpha=0.7, color='plum')
axes[1, 1].set_title(f'Box-Cox Transform\nλ={lambda_param:.2f}, Skew: {stats.skew(data_boxcox):.2f}')
axes[1, 1].set_xlabel('Transformed Value')

plt.tight_layout()
plt.savefig('images/skewness_transformations.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: skewness_transformations.png")

# =============================================================================
# 9. UNIVARIATE CATEGORICAL
# =============================================================================
print("\n9. Creating Univariate Categorical example...")

categories = ['Premium', 'Standard', 'Basic', 'Trial', 'Enterprise']
counts = [250, 450, 300, 150, 100]

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle('Univariate Analysis: Customer Segments', fontsize=16, fontweight='bold')

# Horizontal bar chart
axes[0].barh(categories, counts, color='steelblue', edgecolor='black')
axes[0].set_title('Count Plot')
axes[0].set_xlabel('Count')
for i, v in enumerate(counts):
    axes[0].text(v + 10, i, str(v), va='center')

# Pie chart
axes[1].pie(counts, labels=categories, autopct='%1.1f%%', startangle=90)
axes[1].set_title('Pie Chart (if ≤5 categories)')

# Percentage bars
percentages = np.array(counts) / sum(counts) * 100
axes[2].barh(categories, percentages, color='coral', edgecolor='black')
axes[2].set_title('Percentage Distribution')
axes[2].set_xlabel('Percentage (%)')
for i, v in enumerate(percentages):
    axes[2].text(v + 1, i, f'{v:.1f}%', va='center')

plt.tight_layout()
plt.savefig('images/univariate_categorical.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: univariate_categorical.png")

# =============================================================================
# 10. OUTLIER DETECTION
# =============================================================================
print("\n10. Creating Outlier Detection methods...")

np.random.seed(42)
data_with_outliers = np.concatenate([np.random.normal(50, 10, 950), 
                                     np.random.uniform(100, 150, 50)])

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Outlier Detection Methods', fontsize=16, fontweight='bold')

# Box plot
axes[0, 0].boxplot(data_with_outliers, vert=True)
axes[0, 0].set_title('Box Plot (IQR Method)')
axes[0, 0].set_ylabel('Value')
Q1 = np.percentile(data_with_outliers, 25)
Q3 = np.percentile(data_with_outliers, 75)
IQR = Q3 - Q1
axes[0, 0].text(0.6, Q3 + 1.5*IQR, f'Upper: {Q3 + 1.5*IQR:.0f}', fontsize=8)

# Histogram with bounds
axes[0, 1].hist(data_with_outliers, bins=30, alpha=0.7, edgecolor='black')
axes[0, 1].axvline(Q1 - 1.5*IQR, color='red', linestyle='--', label='Lower bound')
axes[0, 1].axvline(Q3 + 1.5*IQR, color='red', linestyle='--', label='Upper bound')
axes[0, 1].set_title('Histogram with IQR Bounds')
axes[0, 1].legend(fontsize=8)

# Z-score
z_scores = np.abs((data_with_outliers - data_with_outliers.mean()) / data_with_outliers.std())
axes[0, 2].scatter(range(len(z_scores)), z_scores, alpha=0.5, s=10)
axes[0, 2].axhline(3, color='red', linestyle='--', label='|z| = 3')
axes[0, 2].set_title('Z-Score Method')
axes[0, 2].set_ylabel('|Z-score|')
axes[0, 2].legend()

# Percentile
axes[1, 0].hist(data_with_outliers, bins=30, alpha=0.7, edgecolor='black')
p1 = np.percentile(data_with_outliers, 1)
p99 = np.percentile(data_with_outliers, 99)
axes[1, 0].axvline(p1, color='red', linestyle='--', linewidth=2)
axes[1, 0].axvline(p99, color='red', linestyle='--', linewidth=2)
axes[1, 0].set_title('Percentile Method (1%, 99%)')

# Index plot
axes[1, 1].scatter(range(len(data_with_outliers)), data_with_outliers, alpha=0.5, s=10)
axes[1, 1].axhline(Q3 + 1.5*IQR, color='red', linestyle='--')
axes[1, 1].axhline(Q1 - 1.5*IQR, color='red', linestyle='--')
axes[1, 1].set_title('Index Plot')
axes[1, 1].set_xlabel('Index')

# Log scale
axes[1, 2].hist(np.log(data_with_outliers + 1), bins=30, alpha=0.7, edgecolor='black', color='lightgreen')
axes[1, 2].set_title('Log-Transformed View')
axes[1, 2].set_xlabel('Log(Value + 1)')

plt.tight_layout()
plt.savefig('images/outlier_detection.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: outlier_detection.png")

print("\n" + "="*70)
print("✅ PART 2 COMPLETE: Generated 5 more images (10 total)")
print("="*70)

# =============================================================================
# 11-15: BIVARIATE ANALYSIS & CORRELATION
# =============================================================================
print("\nGenerating bivariate analysis images...")

# 11. Bivariate Matrix
print("\n11. Creating Bivariate Analysis Matrix...")
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis('off')

ax.text(6, 7.5, 'Bivariate Analysis: Choosing the Right Visualization', 
        fontsize=16, fontweight='bold', ha='center')

relationships = [
    ('Numeric vs\nNumeric', 'Scatter Plot', '#3498db'),
    ('Numeric vs\nCategorical', 'Box/Violin Plot', '#2ecc71'),
    ('Categorical vs\nCategorical', 'Heatmap/Stacked Bars', '#e74c3c'),
    ('Numeric vs\nTime', 'Line Chart', '#f39c12'),
]

y_positions = [5.5, 4, 2.5, 1]
for (var_type, viz, color), y in zip(relationships, y_positions):
    # Variable type box
    rect1 = FancyBboxPatch((1, y-0.4), 2.5, 0.8, boxstyle="round,pad=0.1",
                           edgecolor=color, facecolor=color, alpha=0.3, linewidth=3)
    ax.add_patch(rect1)
    ax.text(2.25, y, var_type, fontsize=11, ha='center', va='center', fontweight='bold')
    
    # Arrow
    ax.arrow(3.6, y, 1.2, 0, head_width=0.2, head_length=0.15, fc='gray', ec='gray', linewidth=2)
    
    # Visualization box
    rect2 = FancyBboxPatch((5, y-0.4), 3, 0.8, boxstyle="round,pad=0.1",
                           edgecolor='darkgreen', facecolor='lightgreen', linewidth=2)
    ax.add_patch(rect2)
    ax.text(6.5, y, viz, fontsize=10, ha='center', va='center')

plt.tight_layout()
plt.savefig('images/bivariate_matrix.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: bivariate_matrix.png")

# 12. Scatter Plot Variations
print("\n12. Creating Scatter Plot Variations...")
np.random.seed(42)
x = np.random.randn(200) * 2
y = x * 0.8 + np.random.randn(200)
categories = np.random.choice(['A', 'B', 'C'], 200)
sizes = np.random.uniform(10, 100, 200)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Scatter Plot Variations', fontsize=16, fontweight='bold')

# Basic scatter
axes[0, 0].scatter(x, y, alpha=0.6, s=50, color='steelblue')
axes[0, 0].set_title('Basic Scatter Plot')
axes[0, 0].set_xlabel('Variable X')
axes[0, 0].set_ylabel('Variable Y')

# With regression line
axes[0, 1].scatter(x, y, alpha=0.6, s=50, color='steelblue')
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
axes[0, 1].plot(x, p(x), "r--", linewidth=2, label=f'r = {np.corrcoef(x, y)[0,1]:.2f}')
axes[0, 1].set_title('With Regression Line')
axes[0, 1].set_xlabel('Variable X')
axes[0, 1].set_ylabel('Variable Y')
axes[0, 1].legend()

# Color by category
colors_cat = {'A': 'red', 'B': 'green', 'C': 'blue'}
for cat in ['A', 'B', 'C']:
    mask = categories == cat
    axes[1, 0].scatter(x[mask], y[mask], alpha=0.6, s=50, label=f'Group {cat}', color=colors_cat[cat])
axes[1, 0].set_title('Color-Coded by Category')
axes[1, 0].set_xlabel('Variable X')
axes[1, 0].set_ylabel('Variable Y')
axes[1, 0].legend()

# Size encoding
scatter = axes[1, 1].scatter(x, y, alpha=0.6, s=sizes, c=sizes, cmap='viridis')
axes[1, 1].set_title('Size & Color Encoding')
axes[1, 1].set_xlabel('Variable X')
axes[1, 1].set_ylabel('Variable Y')
plt.colorbar(scatter, ax=axes[1, 1], label='Size Variable')

plt.tight_layout()
plt.savefig('images/scatter_variations.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: scatter_variations.png")

# 13. Overplotting Solutions
print("\n13. Creating Overplotting Solutions...")
np.random.seed(42)
n = 10000
x_dense = np.random.randn(n)
y_dense = x_dense * 0.5 + np.random.randn(n)

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Dealing with Overplotting', fontsize=16, fontweight='bold')

# Problem: overplotted
axes[0, 0].scatter(x_dense, y_dense, s=10)
axes[0, 0].set_title('❌ Overplotted\n(Cannot see density)')

# Solution 1: Alpha
axes[0, 1].scatter(x_dense, y_dense, s=10, alpha=0.1)
axes[0, 1].set_title('✅ Alpha Transparency')

# Solution 2: Small points
axes[0, 2].scatter(x_dense, y_dense, s=1, alpha=0.5)
axes[0, 2].set_title('✅ Smaller Points')

# Solution 3: Hexbin
axes[1, 0].hexbin(x_dense, y_dense, gridsize=30, cmap='Blues')
axes[1, 0].set_title('✅ Hexbin')

# Solution 4: 2D KDE
from scipy.stats import gaussian_kde
xy = np.vstack([x_dense, y_dense])
z_kde = gaussian_kde(xy)(xy)
axes[1, 1].scatter(x_dense, y_dense, c=z_kde, s=1, cmap='viridis')
axes[1, 1].set_title('✅ 2D Density Color')

# Solution 5: Sample
sample_idx = np.random.choice(n, 1000, replace=False)
axes[1, 2].scatter(x_dense[sample_idx], y_dense[sample_idx], alpha=0.5, s=20)
axes[1, 2].set_title(f'✅ Random Sample\n({len(sample_idx)} of {n} points)')

plt.tight_layout()
plt.savefig('images/overplotting_solutions.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: overplotting_solutions.png")

# 14. Group Comparison
print("\n14. Creating Group Comparison methods...")
np.random.seed(42)
dept_a = np.random.normal(65, 10, 100)
dept_b = np.random.normal(70, 12, 100)
dept_c = np.random.normal(62, 8, 100)
data_groups = pd.DataFrame({
    'salary': np.concatenate([dept_a, dept_b, dept_c]),
    'department': ['Engineering']*100 + ['Sales']*100 + ['Marketing']*100
})

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Comparing Groups: Numeric vs Categorical', fontsize=16, fontweight='bold')

# Box plots
data_groups.boxplot(column='salary', by='department', ax=axes[0, 0])
axes[0, 0].set_title('Box Plots')
axes[0, 0].set_xlabel('Department')
axes[0, 0].set_ylabel('Salary (K$)')
plt.sca(axes[0, 0])
plt.xticks(rotation=45)

# Violin plots
parts = axes[0, 1].violinplot([dept_a, dept_b, dept_c], positions=[0, 1, 2], 
                               showmeans=True, showmedians=True)
axes[0, 1].set_title('Violin Plots')
axes[0, 1].set_xticks([0, 1, 2])
axes[0, 1].set_xticklabels(['Engineering', 'Sales', 'Marketing'], rotation=45)
axes[0, 1].set_ylabel('Salary (K$)')

# Strip plot
for i, (dept, data) in enumerate([('Engineering', dept_a), ('Sales', dept_b), ('Marketing', dept_c)]):
    axes[0, 2].scatter(np.random.normal(i, 0.04, len(data)), data, alpha=0.3, s=20)
axes[0, 2].set_title('Strip Plot')
axes[0, 2].set_xticks([0, 1, 2])
axes[0, 2].set_xticklabels(['Engineering', 'Sales', 'Marketing'], rotation=45)
axes[0, 2].set_ylabel('Salary (K$)')

# Overlapping histograms
axes[1, 0].hist(dept_a, bins=20, alpha=0.5, label='Engineering', color='blue')
axes[1, 0].hist(dept_b, bins=20, alpha=0.5, label='Sales', color='red')
axes[1, 0].hist(dept_c, bins=20, alpha=0.5, label='Marketing', color='green')
axes[1, 0].set_title('Overlapping Histograms')
axes[1, 0].set_xlabel('Salary (K$)')
axes[1, 0].legend()

# KDE overlay
from scipy.stats import gaussian_kde
x_range = np.linspace(30, 100, 200)
for dept_data, label, color in [(dept_a, 'Engineering', 'blue'), 
                                 (dept_b, 'Sales', 'red'), 
                                 (dept_c, 'Marketing', 'green')]:
    kde = gaussian_kde(dept_data)
    axes[1, 1].plot(x_range, kde(x_range), label=label, linewidth=2, color=color)
    axes[1, 1].fill_between(x_range, kde(x_range), alpha=0.2, color=color)
axes[1, 1].set_title('KDE Overlay')
axes[1, 1].set_xlabel('Salary (K$)')
axes[1, 1].legend()

# Summary statistics
means = [dept_a.mean(), dept_b.mean(), dept_c.mean()]
axes[1, 2].bar(['Engineering', 'Sales', 'Marketing'], means, color=['blue', 'red', 'green'], alpha=0.7)
axes[1, 2].set_title('Mean Comparison')
axes[1, 2].set_ylabel('Mean Salary (K$)')
plt.sca(axes[1, 2])
plt.xticks(rotation=45)
for i, v in enumerate(means):
    axes[1, 2].text(i, v + 1, f'{v:.1f}', ha='center')

plt.tight_layout()
plt.savefig('images/group_comparison.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: group_comparison.png")

# 15. Categorical Relationships
print("\n15. Creating Categorical Relationships...")
np.random.seed(42)
categories_x = np.repeat(['Product A', 'Product B', 'Product C'], 100)
categories_y = np.random.choice(['Premium', 'Standard', 'Basic'], 300, p=[0.3, 0.5, 0.2])
crosstab = pd.crosstab(categories_x, categories_y)

fig, axes = plt.subplots(2, 2, figsize=(14, 12))
fig.suptitle('Categorical vs Categorical Relationships', fontsize=16, fontweight='bold')

# Grouped bars
crosstab.plot(kind='bar', ax=axes[0, 0], color=['#3498db', '#2ecc71', '#e74c3c'])
axes[0, 0].set_title('Grouped Bar Chart')
axes[0, 0].set_xlabel('Product')
axes[0, 0].set_ylabel('Count')
axes[0, 0].legend(title='Segment')
plt.sca(axes[0, 0])
plt.xticks(rotation=45)

# Stacked bars
crosstab.plot(kind='bar', stacked=True, ax=axes[0, 1], color=['#3498db', '#2ecc71', '#e74c3c'])
axes[0, 1].set_title('Stacked Bar Chart')
axes[0, 1].set_xlabel('Product')
axes[0, 1].set_ylabel('Count')
axes[0, 1].legend(title='Segment')
plt.sca(axes[0, 1])
plt.xticks(rotation=45)

# Heatmap
sns.heatmap(crosstab, annot=True, fmt='d', cmap='YlOrRd', ax=axes[1, 0])
axes[1, 0].set_title('Heatmap (Counts)')
axes[1, 0].set_xlabel('Customer Segment')
axes[1, 0].set_ylabel('Product')

# Normalized heatmap
crosstab_norm = crosstab.div(crosstab.sum(axis=1), axis=0)
sns.heatmap(crosstab_norm, annot=True, fmt='.2%', cmap='Blues', ax=axes[1, 1])
axes[1, 1].set_title('Heatmap (Proportions by Row)')
axes[1, 1].set_xlabel('Customer Segment')
axes[1, 1].set_ylabel('Product')

plt.tight_layout()
plt.savefig('images/categorical_relationships.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: categorical_relationships.png")

print("\n" + "="*70)
print("✅ PART 3 COMPLETE: Generated bivariate analysis images (15 total)")
print("="*70)

# =============================================================================
# 16-20: CORRELATION & MULTIVARIATE
# =============================================================================
print("\nGenerating correlation & multivariate images...")

# 16. Correlation Interpretation
print("\n16. Creating Correlation Interpretation guide...")
fig, axes = plt.subplots(3, 3, figsize=(15, 12))
fig.suptitle('Correlation Interpretation Guide', fontsize=16, fontweight='bold')

np.random.seed(42)
x = np.linspace(0, 10, 100)

# Different correlation strengths
correlations = [
    (0.95, 'Strong Positive\nr = 0.95'),
    (0.65, 'Moderate Positive\nr = 0.65'),
    (0.25, 'Weak Positive\nr = 0.25'),
    (0, 'No Correlation\nr = 0.00'),
    (-0.25, 'Weak Negative\nr = -0.25'),
    (-0.65, 'Moderate Negative\nr = -0.65'),
    (-0.95, 'Strong Negative\nr = -0.95'),
]

positions = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0)]

for (r, title), (row, col) in zip(correlations, positions):
    y = x + np.random.randn(100) * (5 * (1 - abs(r)))
    if r < 0:
        y = -y
    axes[row, col].scatter(x, y, alpha=0.6, s=30)
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    axes[row, col].plot(x, p(x), 'r--', linewidth=2)
    axes[row, col].set_title(title, fontweight='bold')
    axes[row, col].set_xticks([])
    axes[row, col].set_yticks([])

# Non-linear (last two plots)
x_nonlin = np.linspace(-3, 3, 100)
y_nonlin = x_nonlin**2 + np.random.randn(100) * 2
axes[2, 1].scatter(x_nonlin, y_nonlin, alpha=0.6, s=30, color='purple')
axes[2, 1].set_title('Non-Linear\n(r ≈ 0, but strong relationship!)', fontweight='bold')
axes[2, 1].set_xticks([])
axes[2, 1].set_yticks([])

# Summary
axes[2, 2].axis('off')
axes[2, 2].text(0.5, 0.8, 'Interpretation Guidelines:', fontsize=12, ha='center', fontweight='bold')
axes[2, 2].text(0.1, 0.6, '|r| > 0.7: Strong\n0.4 < |r| < 0.7: Moderate\n0.2 < |r| < 0.4: Weak\n|r| < 0.2: Very weak', 
                fontsize=10, va='top', family='monospace')
axes[2, 2].text(0.1, 0.2, '⚠️ Correlation ≠ Causation\n⚠️ Only measures LINEAR', 
                fontsize=9, va='top', color='red', fontweight='bold')

plt.tight_layout()
plt.savefig('images/correlation_interpretation.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: correlation_interpretation.png")

# 17. Correlation Heatmap
print("\n17. Creating Correlation Heatmap variations...")
np.random.seed(42)
n = 200
data_corr = pd.DataFrame({
    'price': np.random.randn(n) * 50 + 200,
    'sqft': np.random.randn(n) * 500 + 1500,
    'bedrooms': np.random.randint(1, 5, n),
    'age': np.random.randint(0, 50, n),
    'distance': np.random.randn(n) * 5 + 10
})
# Create correlations
data_corr['price'] = data_corr['sqft'] * 0.15 + data_corr['bedrooms'] * 20 - data_corr['age'] * 0.5 + np.random.randn(n) * 20

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle('Correlation Heatmap Best Practices', fontsize=16, fontweight='bold')

# Basic heatmap
corr = data_corr.corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0, 
            square=True, linewidths=1, ax=axes[0])
axes[0].set_title('Basic Heatmap')

# Lower triangle only
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, mask=mask, annot=True, fmt='.2f', cmap='coolwarm', 
            center=0, square=True, linewidths=1, ax=axes[1])
axes[1].set_title('Lower Triangle\n(Removes redundancy)')

# Strong correlations only
corr_filtered = corr.copy()
corr_filtered[abs(corr) < 0.5] = 0
sns.heatmap(corr_filtered, annot=True, fmt='.2f', cmap='coolwarm', 
            center=0, square=True, linewidths=1, ax=axes[2])
axes[2].set_title('Strong Correlations\n(|r| > 0.5)')

plt.tight_layout()
plt.savefig('images/correlation_heatmap.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: correlation_heatmap.png")

# 18. Anscombe's Quartet
print("\n18. Creating Anscombe's Quartet...")
# Anscombe's quartet data
anscombe_data = {
    'I': {'x': [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
          'y': [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]},
    'II': {'x': [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
           'y': [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]},
    'III': {'x': [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
            'y': [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]},
    'IV': {'x': [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8],
           'y': [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]}
}

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Anscombe's Quartet: Why Visualization Matters!", fontsize=16, fontweight='bold')

for idx, (name, ax) in enumerate(zip(['I', 'II', 'III', 'IV'], axes.flat)):
    x = np.array(anscombe_data[name]['x'])
    y = np.array(anscombe_data[name]['y'])
    
    # Scatter
    ax.scatter(x, y, s=80, alpha=0.7, color='steelblue')
    
    # Regression line
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    ax.plot(x, p(x), 'r--', linewidth=2)
    
    # Statistics
    r = np.corrcoef(x, y)[0, 1]
    ax.set_title(f'Dataset {name}\nr = {r:.3f}, mean(x) = {x.mean():.1f}, mean(y) = {y.mean():.2f}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('images/anscombes_quartet.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: anscombes_quartet.png")

# 19. Pair Plot
print("\n19. Creating Pair Plot example...")
np.random.seed(42)
n = 150
df_pair = pd.DataFrame({
    'Feature_A': np.random.randn(n) * 2 + 5,
    'Feature_B': np.random.randn(n) * 3 + 10,
    'Feature_C': np.random.randn(n) * 1.5 + 3,
    'Target': np.random.randn(n) * 4 + 20
})
# Create some correlations
df_pair['Feature_B'] = df_pair['Feature_A'] * 1.5 + np.random.randn(n) * 2
df_pair['Target'] = df_pair['Feature_A'] * 2 + df_pair['Feature_C'] * 1.5 + np.random.randn(n) * 3

# Create pair plot manually
variables = ['Feature_A', 'Feature_B', 'Feature_C', 'Target']
n_vars = len(variables)

fig, axes = plt.subplots(n_vars, n_vars, figsize=(12, 12))
fig.suptitle('Pair Plot: All Pairwise Relationships', fontsize=16, fontweight='bold')

for i, var1 in enumerate(variables):
    for j, var2 in enumerate(variables):
        ax = axes[i, j]
        
        if i == j:
            # Diagonal: histogram
            ax.hist(df_pair[var1], bins=15, alpha=0.7, color='steelblue', edgecolor='black')
            ax.set_ylabel('')
        else:
            # Off-diagonal: scatter
            ax.scatter(df_pair[var2], df_pair[var1], alpha=0.5, s=20)
            
        # Labels
        if i == n_vars - 1:
            ax.set_xlabel(var2, fontsize=10)
        else:
            ax.set_xlabel('')
            ax.set_xticklabels([])
            
        if j == 0:
            ax.set_ylabel(var1, fontsize=10)
        else:
            ax.set_ylabel('')
            ax.set_yticklabels([])

plt.tight_layout()
plt.savefig('images/pair_plot.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: pair_plot.png")

# 20. Multivariate Encoding
print("\n20. Creating Multivariate Encoding methods...")
np.random.seed(42)
n = 200
df_multi = pd.DataFrame({
    'x': np.random.randn(n) * 2,
    'y': np.random.randn(n) * 2,
    'size_var': np.random.uniform(20, 200, n),
    'color_var': np.random.uniform(0, 100, n),
    'category': np.random.choice(['A', 'B', 'C'], n)
})

fig, axes = plt.subplots(2, 2, figsize=(14, 12))
fig.suptitle('Multivariate Visualization Techniques', fontsize=16, fontweight='bold')

# 1. Color encoding (3 variables: x, y, color)
scatter1 = axes[0, 0].scatter(df_multi['x'], df_multi['y'], 
                              c=df_multi['color_var'], cmap='viridis', 
                              s=50, alpha=0.6)
axes[0, 0].set_title('Color Encoding\n(3 variables: x, y, color)')
axes[0, 0].set_xlabel('Variable X')
axes[0, 0].set_ylabel('Variable Y')
plt.colorbar(scatter1, ax=axes[0, 0], label='Color Variable')

# 2. Size encoding (4 variables: x, y, color, size)
scatter2 = axes[0, 1].scatter(df_multi['x'], df_multi['y'],
                              s=df_multi['size_var'],
                              c=df_multi['color_var'], cmap='plasma',
                              alpha=0.6)
axes[0, 1].set_title('Color + Size Encoding\n(4 variables!)')
axes[0, 1].set_xlabel('Variable X')
axes[0, 1].set_ylabel('Variable Y')
plt.colorbar(scatter2, ax=axes[0, 1], label='Color Var')

# 3. Shape/Category encoding
colors_map = {'A': 'red', 'B': 'green', 'C': 'blue'}
for cat in ['A', 'B', 'C']:
    mask = df_multi['category'] == cat
    axes[1, 0].scatter(df_multi[mask]['x'], df_multi[mask]['y'],
                      label=f'Category {cat}', alpha=0.6, s=50,
                      color=colors_map[cat])
axes[1, 0].set_title('Category Encoding\n(3 variables: x, y, category)')
axes[1, 0].set_xlabel('Variable X')
axes[1, 0].set_ylabel('Variable Y')
axes[1, 0].legend()

# 4. Summary of encoding options
axes[1, 1].axis('off')
axes[1, 1].text(0.5, 0.9, 'Visual Encoding Channels:', fontsize=12, 
                ha='center', fontweight='bold')
encoding_text = '''
Position (x, y):     2 variables
Color (hue):         1 variable (categorical/continuous)
Size:                1 variable (continuous)
Shape:               1 variable (categorical, max 5-6)
Transparency:        1 variable (continuous)
Facets/subplots:     1-2 variables (categorical)

⚠️ Don't overload!
Limit to 3-4 encoding channels max
Too many = cognitive overload
'''
axes[1, 1].text(0.1, 0.7, encoding_text, fontsize=9, va='top', family='monospace')

plt.tight_layout()
plt.savefig('images/multivariate_encoding.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: multivariate_encoding.png")

print("\n" + "="*70)
print("✅ PART 4 COMPLETE: Generated correlation & multivariate images (20 total)")
print("="*70)

# =============================================================================
# 21-24: MISSING DATA
# =============================================================================
print("\nGenerating missing data images...")

# 21. Missing Data Types
print("\n21. Creating Missing Data Types diagram...")
fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(7, 9.5, 'Types of Missingness', fontsize=18, fontweight='bold', ha='center')

types = [
    ('MCAR', 'Missing Completely\nAt Random', 
     'Random sensor failure\nSurvey question skipped randomly',
     'No bias\nSafe to delete or impute', '#2ecc71'),
    ('MAR', 'Missing At Random', 
     'Related to observed data\nOlder patients skip optional Q',
     'Potential bias\nUse sophisticated imputation', '#f39c12'),
    ('MNAR', 'Missing Not At Random',
     'Related to missing value itself\nHigh earners hide income',
     'Serious bias!\nVery difficult to handle', '#e74c3c')
]

y_positions = [7, 4.5, 2]
for (name, full_name, example, impact, color), y in zip(types, y_positions):
    # Main box
    rect = FancyBboxPatch((1, y-0.9), 12, 1.8, boxstyle="round,pad=0.15",
                          edgecolor=color, facecolor=color, alpha=0.2, linewidth=4)
    ax.add_patch(rect)
    
    # Type name
    ax.text(2, y+0.6, name, fontsize=16, fontweight='bold', color=color)
    ax.text(2, y+0.2, full_name, fontsize=11, style='italic')
    
    # Example
    ax.text(6.5, y+0.4, 'Example:', fontsize=10, fontweight='bold')
    ax.text(6.5, y, example, fontsize=9)
    
    # Impact
    ax.text(10.5, y+0.4, 'Impact:', fontsize=10, fontweight='bold')
    ax.text(10.5, y, impact, fontsize=9)

plt.tight_layout()
plt.savefig('images/missing_data_types.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: missing_data_types.png")

# 22. Missing Data Visualization
print("\n22. Creating Missing Data Visualization...")
np.random.seed(42)
n_rows, n_cols = 100, 8
# Create data with different missing patterns
data_missing = np.random.randn(n_rows, n_cols)
# Add missing patterns
data_missing[np.random.choice(n_rows, 15, replace=False), 0] = np.nan  # Random
data_missing[np.random.choice(n_rows, 20, replace=False), 1] = np.nan
data_missing[50:70, 2] = np.nan  # Structured block
data_missing[np.random.choice(n_rows, 25, replace=False), 3] = np.nan
data_missing[::5, 4] = np.nan  # Pattern
data_missing[np.random.choice(n_rows, 30, replace=False), 5] = np.nan
data_missing[np.random.choice(n_rows, 10, replace=False), 6] = np.nan
data_missing[np.random.choice(n_rows, 35, replace=False), 7] = np.nan

df_missing = pd.DataFrame(data_missing, columns=[f'Var_{i+1}' for i in range(n_cols)])

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('Visualizing Missing Data Patterns', fontsize=16, fontweight='bold')

# 1. Missing data heatmap
sns.heatmap(df_missing.isnull(), cbar=False, yticklabels=False,
            cmap=['lightblue', 'darkred'], ax=axes[0, 0])
axes[0, 0].set_title('Missing Data Pattern\n(Red = Missing)')
axes[0, 0].set_xlabel('Variables')

# 2. Missing percentage by column
missing_pct = (df_missing.isnull().sum() / len(df_missing)) * 100
axes[0, 1].barh(df_missing.columns, missing_pct, color='coral', edgecolor='black')
axes[0, 1].set_xlabel('Missing (%)')
axes[0, 1].set_title('Missing Data by Variable')
for i, v in enumerate(missing_pct):
    axes[0, 1].text(v + 1, i, f'{v:.1f}%', va='center')

# 3. Missing data correlation
missing_corr = df_missing.isnull().corr()
sns.heatmap(missing_corr, annot=True, fmt='.2f', cmap='coolwarm', 
            center=0, ax=axes[0, 2])
axes[0, 2].set_title('Missingness Correlation\n(Do variables miss together?)')

# 4. Rows with missing data
rows_missing = df_missing.isnull().sum(axis=1)
axes[1, 0].hist(rows_missing, bins=range(0, 5), edgecolor='black', alpha=0.7, color='steelblue')
axes[1, 0].set_xlabel('Number of Missing Values per Row')
axes[1, 0].set_ylabel('Count of Rows')
axes[1, 0].set_title('Missing Data per Row')

# 5. Missing data matrix
from matplotlib.patches import Rectangle
ax = axes[1, 1]
for i in range(min(30, n_rows)):
    for j in range(n_cols):
        if pd.isna(df_missing.iloc[i, j]):
            rect = Rectangle((j, n_rows-i-1), 1, 1, facecolor='red', edgecolor='white', linewidth=0.5)
        else:
            rect = Rectangle((j, n_rows-i-1), 1, 1, facecolor='lightblue', edgecolor='white', linewidth=0.5)
        ax.add_patch(rect)
ax.set_xlim(0, n_cols)
ax.set_ylim(n_rows-30, n_rows)
ax.set_xlabel('Variables')
ax.set_ylabel('Rows')
ax.set_title('Missing Data Matrix\n(First 30 rows)')
ax.set_xticks(np.arange(n_cols) + 0.5)
ax.set_xticklabels(df_missing.columns, rotation=45)

# 6. Summary table
axes[1, 2].axis('off')
missing_summary = pd.DataFrame({
    'Variable': df_missing.columns,
    'Missing_Count': df_missing.isnull().sum(),
    'Missing_%': missing_pct
})
table_data = missing_summary.values
axes[1, 2].table(cellText=table_data, colLabels=missing_summary.columns,
                cellLoc='center', loc='center', bbox=[0, 0, 1, 1])
axes[1, 2].set_title('Missing Data Summary', pad=20)

plt.tight_layout()
plt.savefig('images/missing_data_visualization.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: missing_data_visualization.png")

# 23. Missing Data Handling
print("\n23. Creating Missing Data Handling strategies...")
fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(7, 9.5, 'Missing Data Handling Strategies', fontsize=18, fontweight='bold', ha='center')

strategies = [
    ('Delete Rows', '< 5% missing\n+ MCAR', 'Quick & simple\nNo bias if MCAR', 'Loss of data\nOnly if truly random', '#3498db'),
    ('Delete Columns', '> 50% missing', 'Removes problematic\nvariables', 'Loss of information', '#2ecc71'),
    ('Mean/Median\nImputation', '5-50% missing\nSymmetric/Skewed', 'Simple\nPreserves sample size', 'Reduces variance\nDistorts relationships', '#f39c12'),
    ('KNN Imputation', 'Similar observations\nexist', 'Uses local patterns\nMore accurate', 'Computationally\nexpensive', '#9b59b6'),
    ('Create Missing\nIndicator', 'Always!', 'Captures missingness\nas feature', 'Adds dimensionality', '#e74c3c'),
]

y_start = 8
for i, (method, when, pros, cons, color) in enumerate(strategies):
    y = y_start - i * 1.7
    
    # Box
    rect = FancyBboxPatch((0.5, y-0.7), 13, 1.4, boxstyle="round,pad=0.1",
                          edgecolor=color, facecolor=color, alpha=0.2, linewidth=3)
    ax.add_patch(rect)
    
    # Method name
    ax.text(1.5, y+0.3, method, fontsize=12, fontweight='bold', color=color)
    
    # When to use
    ax.text(3.5, y+0.4, 'When:', fontsize=10, fontweight='bold')
    ax.text(3.5, y, when, fontsize=9)
    
    # Pros
    ax.text(6.5, y+0.4, '✅ Pros:', fontsize=10, fontweight='bold', color='green')
    ax.text(6.5, y, pros, fontsize=9)
    
    # Cons
    ax.text(10, y+0.4, '❌ Cons:', fontsize=10, fontweight='bold', color='red')
    ax.text(10, y, cons, fontsize=9)

plt.tight_layout()
plt.savefig('images/missing_data_handling.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: missing_data_handling.png")

# 24. Imputation Comparison
print("\n24. Creating Imputation Comparison...")
np.random.seed(42)
# Generate data with missing values
original_data = np.random.normal(50, 15, 300)
data_with_missing = original_data.copy()
missing_idx = np.random.choice(300, 60, replace=False)
data_with_missing[missing_idx] = np.nan

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Comparing Imputation Methods', fontsize=16, fontweight='bold')

# Original (with missing)
axes[0, 0].hist(original_data, bins=30, alpha=0.7, color='steelblue', edgecolor='black')
axes[0, 0].axvline(np.mean(original_data), color='red', linestyle='--', linewidth=2, label='True mean')
axes[0, 0].set_title(f'Original (Complete)\nMean: {np.mean(original_data):.1f}')
axes[0, 0].legend()

# Mean imputation
data_mean = data_with_missing.copy()
data_mean[missing_idx] = np.nanmean(data_mean)
axes[0, 1].hist(data_mean, bins=30, alpha=0.7, color='coral', edgecolor='black')
axes[0, 1].axvline(np.mean(data_mean), color='red', linestyle='--', linewidth=2)
axes[0, 1].set_title(f'Mean Imputation\nMean: {np.mean(data_mean):.1f}\n⚠️ Reduces variance')

# Median imputation
data_median = data_with_missing.copy()
data_median[missing_idx] = np.nanmedian(data_median)
axes[0, 2].hist(data_median, bins=30, alpha=0.7, color='lightgreen', edgecolor='black')
axes[0, 2].axvline(np.mean(data_median), color='red', linestyle='--', linewidth=2)
axes[0, 2].set_title(f'Median Imputation\nMean: {np.mean(data_median):.1f}')

# Random sampling from observed
data_random = data_with_missing.copy()
observed_values = data_random[~np.isnan(data_random)]
data_random[missing_idx] = np.random.choice(observed_values, len(missing_idx))
axes[1, 0].hist(data_random, bins=30, alpha=0.7, color='plum', edgecolor='black')
axes[1, 0].axvline(np.mean(data_random), color='red', linestyle='--', linewidth=2)
axes[1, 0].set_title(f'Random Sampling\nMean: {np.mean(data_random):.1f}\n✅ Preserves distribution')

# KNN-like (using nearby values)
data_knn = data_with_missing.copy()
for idx in missing_idx:
    # Find 5 nearest non-missing neighbors
    distances = np.abs(np.arange(len(data_knn)) - idx)
    valid_idx = ~np.isnan(data_knn)
    valid_distances = distances[valid_idx]
    valid_values = data_knn[valid_idx]
    nearest = np.argsort(valid_distances)[:5]
    data_knn[idx] = np.mean(valid_values[nearest])
axes[1, 1].hist(data_knn, bins=30, alpha=0.7, color='gold', edgecolor='black')
axes[1, 1].axvline(np.mean(data_knn), color='red', linestyle='--', linewidth=2)
axes[1, 1].set_title(f'KNN-like Imputation\nMean: {np.mean(data_knn):.1f}\n✅ Uses local patterns')

# Comparison table
axes[1, 2].axis('off')
comparison_text = f'''
Method Comparison:

Original Mean: {np.mean(original_data):.1f}
Original Std:  {np.std(original_data):.1f}

Mean Imp:      {np.mean(data_mean):.1f} (Std: {np.std(data_mean):.1f})
Median Imp:    {np.mean(data_median):.1f} (Std: {np.std(data_median):.1f})
Random Imp:    {np.mean(data_random):.1f} (Std: {np.std(data_random):.1f})
KNN Imp:       {np.mean(data_knn):.1f} (Std: {np.std(data_knn):.1f})

Best for distribution: Random
Best for relationships: KNN
Fastest: Mean/Median
'''
axes[1, 2].text(0.1, 0.9, comparison_text, fontsize=9, va='top', family='monospace')

plt.tight_layout()
plt.savefig('images/imputation_comparison.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: imputation_comparison.png")

print("\n" + "="*70)
print("✅ PART 5 COMPLETE: Generated missing data images (24 total)")
print("="*70)

print("\n" + "="*70)
print("✅ PART 5 COMPLETE: Generated missing data images (24 total)")
print("="*70)

# =============================================================================
# 25-29: WORKFLOW & BEST PRACTICES (FINAL BATCH!)
# =============================================================================
print("\nGenerating final workflow & best practices images...")

# 25. EDA Workflow Template
print("\n25. Creating EDA Workflow Template diagram...")
fig, ax = plt.subplots(figsize=(12, 14))
ax.set_xlim(0, 12)
ax.set_ylim(0, 14)
ax.axis('off')

ax.text(6, 13.5, 'Complete EDA Workflow Template', fontsize=18, fontweight='bold', ha='center')

steps = [
    ('1. Data Overview', 'Shape, types, memory\nFirst few rows', '#3498db'),
    ('2. Quality Check', 'Missing, duplicates\nInconsistencies', '#2ecc71'),
    ('3. Univariate', 'Distributions, outliers\nSkewness, modality', '#f39c12'),
    ('4. Bivariate', 'Relationships, correlations\nGroup differences', '#e74c3c'),
    ('5. Missing Data', 'Patterns, type (MCAR/MAR/MNAR)\nImputation strategy', '#9b59b6'),
    ('6. Key Findings', 'Patterns discovered\nData quality issues', '#1abc9c'),
    ('7. Recommendations', 'Transformations needed\nFeatures to engineer', '#34495e'),
]

y_start = 12
for i, (step, details, color) in enumerate(steps):
    y = y_start - i * 1.8
    
    # Box
    rect = FancyBboxPatch((1, y-0.7), 10, 1.4, boxstyle="round,pad=0.15",
                          edgecolor=color, facecolor=color, alpha=0.3, linewidth=3)
    ax.add_patch(rect)
    
    # Step name
    ax.text(2, y+0.4, step, fontsize=14, fontweight='bold', color=color)
    
    # Details
    ax.text(2, y-0.2, details, fontsize=10)
    
    # Arrow to next (except last)
    if i < len(steps) - 1:
        ax.arrow(6, y-0.8, 0, -0.3, head_width=0.3, head_length=0.15,
                fc='gray', ec='gray', linewidth=3)

plt.tight_layout()
plt.savefig('images/eda_workflow_template.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: eda_workflow_template.png")

# 26. EDA Best Practices
print("\n26. Creating EDA Best Practices infographic...")
fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(7, 9.5, 'EDA Best Practices', fontsize=18, fontweight='bold', ha='center')

# Do's (left side)
ax.text(3.5, 8.5, '✅ DO:', fontsize=14, fontweight='bold', color='green', ha='center')
dos = [
    'Start simple → Go deeper',
    'Visualize everything',
    'Question assumptions',
    'Document findings',
    'Think about domain',
    'Use multiple views',
    'Iterate and refine'
]
y_dos = 7.8
for do in dos:
    rect = FancyBboxPatch((0.5, y_dos-0.3), 6, 0.6, boxstyle="round,pad=0.05",
                          edgecolor='green', facecolor='lightgreen', alpha=0.3, linewidth=2)
    ax.add_patch(rect)
    ax.text(3.5, y_dos, do, fontsize=11, ha='center', va='center')
    y_dos -= 0.9

# Don'ts (right side)
ax.text(10.5, 8.5, '❌ DON\'T:', fontsize=14, fontweight='bold', color='red', ha='center')
donts = [
    'Skip EDA phase',
    'P-hack for significance',
    'Ignore outliers',
    'Use defaults blindly',
    'Over-automate',
    'Forget to document',
    'Rush to modeling'
]
y_donts = 7.8
for dont in donts:
    rect = FancyBboxPatch((7.5, y_donts-0.3), 6, 0.6, boxstyle="round,pad=0.05",
                          edgecolor='red', facecolor='lightcoral', alpha=0.3, linewidth=2)
    ax.add_patch(rect)
    ax.text(10.5, y_donts, dont, fontsize=11, ha='center', va='center')
    y_donts -= 0.9

plt.tight_layout()
plt.savefig('images/eda_best_practices.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: eda_best_practices.png")

# 27. Common EDA Mistakes
print("\n27. Creating Common EDA Mistakes diagram...")
fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(7, 9.5, 'Common EDA Mistakes to Avoid', fontsize=18, fontweight='bold', ha='center')

mistakes = [
    ('Data Leakage', 'Using future information\nin features', '⚠️ Inflated performance', '#e74c3c'),
    ('Ignoring Cardinality', 'Too many unique categories\nfor one-hot encoding', '⚠️ Curse of dimensionality', '#e67e22'),
    ('Class Imbalance', 'Not checking target\ndistribution', '⚠️ Biased models', '#f39c12'),
    ('Analysis Paralysis', 'Exploring forever\nwithout conclusions', '⚠️ Wasted time', '#9b59b6'),
    ('Confirmation Bias', 'Only looking for\nsupporting patterns', '⚠️ Missed insights', '#3498db'),
    ('Over-interpreting Noise', 'Finding patterns in\nrandom variation', '⚠️ False discoveries', '#2ecc71'),
]

y_start = 8.5
for i, (mistake, description, impact, color) in enumerate(mistakes):
    row = i // 2
    col = i % 2
    x = 3 if col == 0 else 10
    y = y_start - row * 2.2
    
    # Box
    rect = FancyBboxPatch((x-2.3, y-0.8), 4.6, 1.6, boxstyle="round,pad=0.15",
                          edgecolor=color, facecolor=color, alpha=0.2, linewidth=3)
    ax.add_patch(rect)
    
    # Mistake name
    ax.text(x, y+0.5, mistake, fontsize=12, fontweight='bold', ha='center', color=color)
    
    # Description
    ax.text(x, y+0.05, description, fontsize=9, ha='center')
    
    # Impact
    ax.text(x, y-0.5, impact, fontsize=9, ha='center', style='italic')

plt.tight_layout()
plt.savefig('images/common_eda_mistakes.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: common_eda_mistakes.png")

# 28. Data Type Specific EDA
print("\n28. Creating Data Type Specific EDA guide...")
fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(7, 9.5, 'EDA for Different Data Types', fontsize=18, fontweight='bold', ha='center')

data_types = [
    ('Time Series', 'Trend, seasonality, cycles\nRolling statistics\nAutocorrelation', '#3498db'),
    ('Text Data', 'Length distribution\nWord frequency\nN-grams', '#2ecc71'),
    ('Images', 'Dimension distribution\nColor histograms\nSample visualization', '#e74c3c'),
    ('Categorical', 'Frequency tables\nCardinality check\nRare categories', '#f39c12'),
    ('Numeric', 'Distribution shape\nOutliers\nSkewness', '#9b59b6'),
    ('Mixed Types', 'Type consistency\nRelationships\nEncoding strategy', '#1abc9c'),
]

positions = [(3.5, 7), (10.5, 7), (3.5, 4.5), (10.5, 4.5), (3.5, 2), (10.5, 2)]

for (dtype, analysis, color), (x, y) in zip(data_types, positions):
    # Box
    rect = FancyBboxPatch((x-2.8, y-1), 5.6, 2, boxstyle="round,pad=0.15",
                          edgecolor=color, facecolor=color, alpha=0.2, linewidth=3)
    ax.add_patch(rect)
    
    # Data type
    ax.text(x, y+0.6, dtype, fontsize=13, fontweight='bold', ha='center', color=color)
    
    # Analysis approach
    ax.text(x, y-0.1, analysis, fontsize=9, ha='center')

plt.tight_layout()
plt.savefig('images/data_type_eda.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: data_type_eda.png")

# 29. EDA to Features
print("\n29. Creating EDA to Features pipeline...")
fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

ax.text(7, 9.5, 'From EDA Insights to Feature Engineering', fontsize=18, fontweight='bold', ha='center')

mappings = [
    ('Skewness\nDetected', 'Log/Box-Cox\nTransformation', '#3498db'),
    ('Missing\nPatterns', 'Create Missing\nIndicator Features', '#2ecc71'),
    ('Outliers\nFound', 'Capping or\nRobust Scaling', '#e74c3c'),
    ('Temporal\nPatterns', 'Extract Time\nFeatures', '#f39c12'),
    ('High\nCorrelation', 'Create Interaction\nTerms', '#9b59b6'),
    ('Category\nEffects', 'Target/Frequency\nEncoding', '#1abc9c'),
]

y_start = 8.5
for i, (insight, action, color) in enumerate(mappings):
    row = i // 2
    col = i % 2
    x_start = 2.5 if col == 0 else 9
    y = y_start - row * 2.5
    
    # Insight box
    rect1 = FancyBboxPatch((x_start, y-0.5), 2, 1, boxstyle="round,pad=0.1",
                           edgecolor=color, facecolor=color, alpha=0.3, linewidth=2)
    ax.add_patch(rect1)
    ax.text(x_start + 1, y, insight, fontsize=10, ha='center', va='center', fontweight='bold')
    
    # Arrow
    ax.arrow(x_start + 2.1, y, 0.7, 0, head_width=0.2, head_length=0.15,
            fc=color, ec=color, linewidth=2)
    
    # Action box
    rect2 = FancyBboxPatch((x_start + 3, y-0.5), 2, 1, boxstyle="round,pad=0.1",
                           edgecolor='darkgreen', facecolor='lightgreen', alpha=0.4, linewidth=2)
    ax.add_patch(rect2)
    ax.text(x_start + 4, y, action, fontsize=10, ha='center', va='center')

plt.tight_layout()
plt.savefig('images/eda_to_features.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: eda_to_features.png")

print("\n" + "="*70)
print("✅ PART 6 COMPLETE: Generated workflow & best practices images (29 total)")
print("="*70)

print("\n" + "="*70)
print("🎉 ALL 29 CORE IMAGES GENERATED SUCCESSFULLY! 🎉")
print("="*70)
print(f"Total core images created: 29")
print("Images saved in: images/")
print("\nImage categories:")
print("  - Foundation & Overview: 5 images")
print("  - Univariate Analysis: 5 images")
print("  - Bivariate Analysis: 5 images")
print("  - Correlation & Multivariate: 5 images")
print("  - Missing Data: 4 images")
print("  - Workflow & Best Practices: 5 images")
print("="*70)
