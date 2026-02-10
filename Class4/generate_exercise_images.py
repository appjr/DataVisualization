"""
Generate placeholder images for the 5 exercises
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.patches import FancyBboxPatch
import os

print("Generating exercise example images...")
print("="*70)

os.makedirs('images', exist_ok=True)

# Exercise 1: Distribution Diagnosis
print("\n1. Creating Exercise 1: Distribution Diagnosis example...")
np.random.seed(42)
transaction_amounts = np.random.lognormal(mean=3, sigma=1, size=10000)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Exercise 1: Distribution Diagnosis - Example Solution', 
             fontsize=16, fontweight='bold')

# Histogram
axes[0, 0].hist(transaction_amounts, bins=50, edgecolor='black', alpha=0.7, color='steelblue')
axes[0, 0].axvline(transaction_amounts.mean(), color='red', linestyle='--', linewidth=2, label='Mean')
axes[0, 0].axvline(np.median(transaction_amounts), color='green', linestyle='--', linewidth=2, label='Median')
axes[0, 0].set_title('Original Distribution')
axes[0, 0].set_xlabel('Transaction Amount ($)')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].legend()

# Box plot
axes[0, 1].boxplot(transaction_amounts, vert=True)
axes[0, 1].set_title('Box Plot\n(Shows outliers)')
axes[0, 1].set_ylabel('Transaction Amount ($)')

# Q-Q plot
from scipy import stats
stats.probplot(transaction_amounts, dist="norm", plot=axes[1, 0])
axes[1, 0].set_title('Q-Q Plot\n(Not normal)')
axes[1, 0].get_lines()[0].set_markerfacecolor('steelblue')

# Log transformation
log_amounts = np.log(transaction_amounts)
axes[1, 1].hist(log_amounts, bins=50, edgecolor='black', alpha=0.7, color='coral')
axes[1, 1].set_title(f'Log Transformed\nSkew: {stats.skew(log_amounts):.2f}')
axes[1, 1].set_xlabel('Log(Amount)')
axes[1, 1].set_ylabel('Frequency')

plt.tight_layout()
plt.savefig('images/exercise1_distribution.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: exercise1_distribution.png")

# Exercise 2: Outlier Investigation
print("\n2. Creating Exercise 2: Outlier Investigation example...")
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=365, freq='D')
base_revenue = np.random.normal(50000, 5000, 365)
# Add spikes for holidays
base_revenue[0] = 120000  # New Year
base_revenue[60] = 90000  # Valentine's
base_revenue[180] = 110000  # Summer sale
base_revenue[334] = 150000  # Black Friday
base_revenue[359] = 130000  # Christmas

df_rev = pd.DataFrame({'date': dates, 'revenue': base_revenue})

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Exercise 2: Outlier Investigation - Example Solution', 
             fontsize=16, fontweight='bold')

# Time series with outliers marked
Q1 = df_rev['revenue'].quantile(0.25)
Q3 = df_rev['revenue'].quantile(0.75)
IQR = Q3 - Q1
outlier_mask = (df_rev['revenue'] < Q1 - 1.5*IQR) | (df_rev['revenue'] > Q3 + 1.5*IQR)

axes[0, 0].plot(df_rev['date'], df_rev['revenue'], alpha=0.6, linewidth=1)
axes[0, 0].scatter(df_rev[outlier_mask]['date'], df_rev[outlier_mask]['revenue'], 
                   color='red', s=100, zorder=5, label='Outliers')
axes[0, 0].set_title('Revenue Over Time (Outliers Marked)')
axes[0, 0].set_xlabel('Date')
axes[0, 0].set_ylabel('Revenue ($)')
axes[0, 0].legend()
axes[0, 0].tick_params(axis='x', rotation=45)

# Box plot
axes[0, 1].boxplot(df_rev['revenue'])
axes[0, 1].set_title('Box Plot')
axes[0, 1].set_ylabel('Revenue ($)')

# Outlier dates table
outlier_dates = df_rev[outlier_mask].sort_values('revenue', ascending=False)
axes[1, 0].axis('off')
axes[1, 0].text(0.5, 0.9, 'Outlier Dates:', fontsize=12, ha='center', fontweight='bold')
table_text = f"""
Date          Revenue      Reason
────────────────────────────────
{outlier_dates.iloc[0]['date'].strftime('%Y-%m-%d')}  ${outlier_dates.iloc[0]['revenue']:,.0f}  Black Friday
{outlier_dates.iloc[1]['date'].strftime('%Y-%m-%d')}  ${outlier_dates.iloc[1]['revenue']:,.0f}  Christmas
{outlier_dates.iloc[2]['date'].strftime('%Y-%m-%d')}  ${outlier_dates.iloc[2]['revenue']:,.0f}  New Year
{outlier_dates.iloc[3]['date'].strftime('%Y-%m-%d')}  ${outlier_dates.iloc[3]['revenue']:,.0f}  Summer Sale

Decision: KEEP - Legitimate spikes
"""
axes[1, 0].text(0.1, 0.7, table_text, fontsize=9, va='top', family='monospace')

# Recommendation
axes[1, 1].axis('off')
axes[1, 1].text(0.5, 0.8, 'Recommendation:', fontsize=14, ha='center', fontweight='bold')
rec_text = """
✅ Keep outliers in dataset

Reasons:
• Outliers coincide with major holidays
• Values are legitimate sales spikes
• Removing would lose business insights
• Important for forecasting seasonal peaks

Action:
• Create 'is_holiday' feature
• Use robust models (e.g., tree-based)
• Track separately for reporting
"""
axes[1, 1].text(0.1, 0.65, rec_text, fontsize=10, va='top')

plt.tight_layout()
plt.savefig('images/exercise2_outliers.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: exercise2_outliers.png")

# Exercise 3: Relationship Mapping
print("\n3. Creating Exercise 3: Relationship Mapping example...")
np.random.seed(42)
n = 500
df_house = pd.DataFrame({
    'price': np.random.normal(300000, 100000, n),
    'sqft': np.random.normal(2000, 500, n),
    'bedrooms': np.random.randint(1, 6, n),
    'age': np.random.randint(0, 50, n),
    'distance_to_city': np.random.uniform(0, 30, n)
})
# Create correlations
df_house['price'] = (df_house['sqft'] * 150 + 
                      df_house['bedrooms'] * 20000 - 
                      df_house['age'] * 1000 - 
                      df_house['distance_to_city'] * 3000 + 
                      np.random.normal(0, 30000, n))

fig, axes = plt.subplots(2, 2, figsize=(14, 12))
fig.suptitle('Exercise 3: Relationship Mapping - Example Solution', 
             fontsize=16, fontweight='bold')

# Correlation heatmap
corr = df_house.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, mask=mask, annot=True, fmt='.2f', cmap='coolwarm', 
            center=0, square=True, linewidths=1, ax=axes[0, 0])
axes[0, 0].set_title('Correlation Heatmap')

# Top correlations scatter
axes[0, 1].scatter(df_house['sqft'], df_house['price'], alpha=0.5, s=20)
z = np.polyfit(df_house['sqft'], df_house['price'], 1)
p = np.poly1d(z)
axes[0, 1].plot(df_house['sqft'], p(df_house['sqft']), "r--", linewidth=2)
r = df_house['sqft'].corr(df_house['price'])
axes[0, 1].set_title(f'Price vs. Sqft (r = {r:.3f})')
axes[0, 1].set_xlabel('Square Feet')
axes[0, 1].set_ylabel('Price ($)')

# Second strongest correlation
axes[1, 0].scatter(df_house['distance_to_city'], df_house['price'], alpha=0.5, s=20, color='coral')
z2 = np.polyfit(df_house['distance_to_city'], df_house['price'], 1)
p2 = np.poly1d(z2)
axes[1, 0].plot(df_house['distance_to_city'], p2(df_house['distance_to_city']), "r--", linewidth=2)
r2 = df_house['distance_to_city'].corr(df_house['price'])
axes[1, 0].set_title(f'Price vs. Distance (r = {r2:.3f})')
axes[1, 0].set_xlabel('Distance to City (miles)')
axes[1, 0].set_ylabel('Price ($)')

# Summary table
axes[1, 1].axis('off')
axes[1, 1].text(0.5, 0.9, 'Key Findings:', fontsize=12, ha='center', fontweight='bold')
findings_text = f"""
Top Correlations with Price:
1. Sqft:       r = {df_house['sqft'].corr(df_house['price']):.3f} (Strong +)
2. Distance:   r = {df_house['distance_to_city'].corr(df_house['price']):.3f} (Strong -)
3. Bedrooms:   r = {df_house['bedrooms'].corr(df_house['price']):.3f} (Moderate +)
4. Age:        r = {df_house['age'].corr(df_house['price']):.3f} (Weak -)

Recommendations:
• Sqft is strongest predictor
• Location matters (distance effect)
• Consider sqft × location interaction
• Age effect is minimal
• All relationships are linear
"""
axes[1, 1].text(0.1, 0.75, findings_text, fontsize=9, va='top', family='monospace')

plt.tight_layout()
plt.savefig('images/exercise3_relationships.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: exercise3_relationships.png")

# Exercise 4: Missing Data Detective
print("\n4. Creating Exercise 4: Missing Data Detective example...")
np.random.seed(42)
n_rows, n_cols = 500, 6
df_survey = pd.DataFrame(
    np.random.randn(n_rows, n_cols),
    columns=['Q1', 'Q2_optional', 'Q3', 'Q4_income', 'Q5', 'age']
)
# Add structured missingness
df_survey.loc[df_survey['age'] < -0.5, 'Q4_income'] = np.nan  # MAR: younger less likely to report income
df_survey.loc[np.random.choice(n_rows, 100, replace=False), 'Q2_optional'] = np.nan  # MCAR
df_survey.loc[np.random.choice(n_rows, 50, replace=False), 'Q5'] = np.nan

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('Exercise 4: Missing Data Detective - Example Solution', 
             fontsize=16, fontweight='bold')

# Missing heatmap
sns.heatmap(df_survey.isnull(), cbar=False, yticklabels=False,
            cmap=['lightblue', 'darkred'], ax=axes[0, 0])
axes[0, 0].set_title('Missing Data Pattern\n(Red = Missing)')
axes[0, 0].set_xlabel('Questions')

# Missing percentage
missing_pct = (df_survey.isnull().sum() / len(df_survey)) * 100
axes[0, 1].barh(df_survey.columns, missing_pct, color='coral', edgecolor='black')
axes[0, 1].set_xlabel('Missing (%)')
axes[0, 1].set_title('Missing Data by Question')
for i, v in enumerate(missing_pct):
    axes[0, 1].text(v + 1, i, f'{v:.1f}%', va='center')

# Check MAR: income missing related to age?
df_temp = df_survey.copy()
df_temp['income_missing'] = df_survey['Q4_income'].isnull()
age_with_income = df_temp[~df_temp['income_missing']]['age']
age_without_income = df_temp[df_temp['income_missing']]['age']

axes[0, 2].hist([age_with_income, age_without_income], bins=20, 
                label=['Reported Income', 'Missing Income'], alpha=0.7)
axes[0, 2].set_title('Age Distribution\nby Income Reporting')
axes[0, 2].set_xlabel('Age (normalized)')
axes[0, 2].legend()

# Imputation comparison: Mean vs KNN
from sklearn.impute import SimpleImputer, KNNImputer

# Mean imputation
mean_imp = SimpleImputer(strategy='mean')
df_mean = pd.DataFrame(mean_imp.fit_transform(df_survey), columns=df_survey.columns)

# KNN imputation
knn_imp = KNNImputer(n_neighbors=5)
df_knn = pd.DataFrame(knn_imp.fit_transform(df_survey), columns=df_survey.columns)

# Compare distributions for one column
col = 'Q4_income'
axes[1, 0].hist([df_survey[col].dropna(), df_mean[col], df_knn[col]], 
                bins=20, alpha=0.6, label=['Original', 'Mean Imp', 'KNN Imp'])
axes[1, 0].set_title(f'{col}: Imputation Comparison')
axes[1, 0].legend()

# Summary table
axes[1, 1].axis('off')
axes[1, 1].text(0.5, 0.9, 'Diagnosis:', fontsize=12, ha='center', fontweight='bold')
diagnosis_text = f"""
Missingness Analysis:

Q2_optional:  20% missing (MCAR)
  • Random pattern
  • Safe to delete or impute

Q4_income:    ~15% missing (MAR)
  • Related to age
  • Younger respondents skip
  • Use KNN imputation

Q5:           10% missing (MCAR)
  • Random pattern
  • Mean imputation OK
"""
axes[1, 1].text(0.1, 0.75, diagnosis_text, fontsize=9, va='top', family='monospace')

# Recommendation
axes[1, 2].axis('off')
axes[1, 2].text(0.5, 0.9, 'Recommendation:', fontsize=12, ha='center', fontweight='bold')
rec_text = """
Strategy:

1. Q2_optional (20% MCAR)
   → Drop column if not critical
   → OR mean imputation

2. Q4_income (15% MAR)
   → KNN imputation (k=5)
   → Create missing indicator
   → Preserves relationships

3. Q5 (10% MCAR)
   → Mean imputation
   → Low impact on analysis

Result: KNN preserves
distributions best!
"""
axes[1, 2].text(0.05, 0.75, rec_text, fontsize=9, va='top')

plt.tight_layout()
plt.savefig('images/exercise4_missing_data.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: exercise4_missing_data.png")

# Exercise 5: Mini EDA Report
print("\n5. Creating Exercise 5: Mini EDA Report example...")

fig = plt.figure(figsize=(14, 10))
gs = fig.add_gridspec(3, 3, hspace=0.4, wspace=0.3)
fig.suptitle('Exercise 5: Mini EDA Report - Example Structure', 
             fontsize=16, fontweight='bold')

# Title section
ax_title = fig.add_subplot(gs[0, :])
ax_title.axis('off')
ax_title.text(0.5, 0.7, 'Employee Attrition Analysis', fontsize=18, ha='center', fontweight='bold')
ax_title.text(0.5, 0.4, 'A Comprehensive EDA Report', fontsize=12, ha='center', style='italic')

# Section 1: Data Overview
ax1 = fig.add_subplot(gs[1, 0])
ax1.axis('off')
ax1.text(0.5, 0.9, '1. DATA OVERVIEW', fontsize=11, ha='center', fontweight='bold', 
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
overview_text = """
• Rows: 1,470
• Features: 35
• Target: Attrition (16%)
• Missing: None
• Duplicates: None
• Data Types:
  - Numeric: 26
  - Categorical: 9
"""
ax1.text(0.1, 0.7, overview_text, fontsize=8, va='top', family='monospace')

# Section 2: Data Quality
ax2 = fig.add_subplot(gs[1, 1])
ax2.axis('off')
ax2.text(0.5, 0.9, '2. DATA QUALITY', fontsize=11, ha='center', fontweight='bold',
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))
quality_text = """
✅ No missing values
✅ No duplicates
✅ Consistent formats
✅ Logical value ranges

⚠️ Issues found:
• Salary highly skewed
• Employee count = 1
  (constant, drop)
• Over18 = 'Y' always
  (constant, drop)
"""
ax2.text(0.1, 0.7, quality_text, fontsize=8, va='top')

# Section 3: Key Findings
ax3 = fig.add_subplot(gs[1, 2])
ax3.axis('off')
ax3.text(0.5, 0.9, '3. KEY FINDINGS', fontsize=11, ha='center', fontweight='bold',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))
findings_text = """
1. Attrition Rate: 16%
   (237 of 1,470 left)

2. Top Predictors:
   • Overtime (54% leave)
   • Low job satisfaction
   • Distance from home
   • Years at company

3. Patterns:
   • Young employees leave
   • Sales has highest rate
   • Recent hires risky
"""
ax3.text(0.1, 0.7, findings_text, fontsize=8, va='top')

# Visualization 1: Target distribution
ax4 = fig.add_subplot(gs[2, 0])
categories = ['Stayed', 'Left']
values = [1233, 237]
colors_viz = ['lightgreen', 'coral']
ax4.bar(categories, values, color=colors_viz, edgecolor='black')
ax4.set_title('Attrition Distribution', fontsize=10, fontweight='bold')
ax4.set_ylabel('Count')
for i, v in enumerate(values):
    ax4.text(i, v + 30, f'{v}\n({v/sum(values)*100:.1f}%)', ha='center')

# Visualization 2: Top correlations
ax5 = fig.add_subplot(gs[2, 1])
features = ['Overtime', 'JobSat', 'Distance', 'Years', 'Age']
correlations_viz = [0.45, -0.38, 0.28, -0.25, -0.22]
colors_corr = ['red' if c > 0 else 'green' for c in correlations_viz]
ax5.barh(features, correlations_viz, color=colors_corr, edgecolor='black')
ax5.set_xlabel('Correlation with Attrition')
ax5.set_title('Top Predictors', fontsize=10, fontweight='bold')
ax5.axvline(0, color='black', linewidth=0.5)

# Recommendations
ax6 = fig.add_subplot(gs[2, 2])
ax6.axis('off')
ax6.text(0.5, 0.9, '4. RECOMMENDATIONS', fontsize=11, ha='center', fontweight='bold',
         bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.5))
rec_eda_text = """
Data Preparation:
• Drop constant columns
• Log-transform salary
• Create age groups
• Encode categoricals

Features to Engineer:
• Overtime flag
• Satisfaction score
• Tenure buckets
• Distance categories

Next Steps:
• Build predictive model
• Focus on high-risk groups
• Test interventions
"""
ax6.text(0.05, 0.7, rec_eda_text, fontsize=8, va='top')

plt.savefig('images/exercise5_eda_report.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("  ✅ Created: exercise5_eda_report.png")

print("\n" + "="*70)
print("🎉 ALL 5 EXERCISE IMAGES GENERATED SUCCESSFULLY!")
print("="*70)
print("Total exercise images created: 5")
print("Images saved in: images/")
print("="*70)
