# Class 6 – Applications & Best Practices

[Part 1](Class6_Part1.md) | [Part 2](Class6_Part2.md) | [Part 3](Class6_Part3.md) | [Part 4](Class6_Part4.md)

---

# PART 4: APPLICATIONS & BEST PRACTICES
# Slides 61-80
# ═══════════════════════════════════════════════════════════════

## Real-World Case Study 1: Sales Territory Analysis

**Business Problem:**

A retail company wants to:
- Analyze sales performance across territories
- Identify underperforming regions
- Optimize territory assignments
- Plan new store locations

**Data Available:**
- Sales by ZIP code
- Store locations and performance
- Customer demographics
- Competitor locations

**Visualization Approach:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Simulate sales territory data
np.random.seed(42)

# Load US states as territories
states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
us_states = states[states['iso_a3'] == 'USA'].copy()

# Generate sales data
us_states['sales'] = np.random.randint(1000000, 10000000, len(us_states))
us_states['target'] = us_states['sales'] * 1.2
us_states['performance'] = (us_states['sales'] / us_states['target']) * 100

# Generate store locations
stores = gpd.GeoDataFrame({
    'store_id': range(1, 21),
    'sales': np.random.randint(100000, 500000, 20),
    'geometry': gpd.points_from_xy(
        np.random.uniform(-120, -70, 20),
        np.random.uniform(25, 48, 20)
    )
}, crs='EPSG:4326')

# Create comprehensive dashboard
fig = plt.figure(figsize=(20, 12))

# Subplot 1: Territory Performance (Choropleth)
ax1 = plt.subplot(2, 2, 1)
us_states.plot(column='performance', cmap='RdYlGn', 
              legend=True, ax=ax1, edgecolor='black', linewidth=0.5,
              legend_kwds={'label': 'Performance (%)', 'shrink': 0.8})
ax1.set_title('Territory Performance vs Target', fontsize=14, fontweight='bold')
ax1.axis('off')

# Subplot 2: Store Sales (Proportional Symbols)
ax2 = plt.subplot(2, 2, 2)
us_states.plot(ax=ax2, color='lightgray', edgecolor='black', linewidth=0.5)
stores.plot(ax=ax2, markersize=stores['sales']/1000, 
           color='blue', alpha=0.6, edgecolor='darkblue', linewidth=1)
ax2.set_title('Store Sales (Bubble Size = Revenue)', fontsize=14, fontweight='bold')
ax2.axis('off')

# Subplot 3: Top/Bottom Performers
ax3 = plt.subplot(2, 2, 3)
top_bottom = pd.concat([
    us_states.nsmallest(5, 'performance')[['name', 'performance']],
    us_states.nlargest(5, 'performance')[['name', 'performance']]
])
colors = ['red'] * 5 + ['green'] * 5
ax3.barh(range(len(top_bottom)), top_bottom['performance'], color=colors, alpha=0.7)
ax3.set_yticks(range(len(top_bottom)))
ax3.set_yticklabels(top_bottom['name'])
ax3.set_xlabel('Performance (%)', fontsize=11)
ax3.set_title('Top & Bottom Performing Territories', fontsize=14, fontweight='bold')
ax3.axvline(100, color='black', linestyle='--', linewidth=2)

# Subplot 4: Sales Distribution
ax4 = plt.subplot(2, 2, 4)
ax4.hist(us_states['sales']/1000000, bins=10, color='steelblue', 
        edgecolor='black', alpha=0.7)
ax4.axvline(us_states['sales'].mean()/1000000, color='red', 
           linestyle='--', linewidth=2, label='Mean')
ax4.set_xlabel('Sales (Millions $)', fontsize=11)
ax4.set_ylabel('Frequency', fontsize=11)
ax4.set_title('Sales Distribution Across Territories', fontsize=14, fontweight='bold')
ax4.legend()

plt.suptitle('Sales Territory Analysis Dashboard', fontsize=18, fontweight='bold')
plt.tight_layout()
plt.show()
```

**Key Insights:**
✅ Visual comparison of territory performance
✅ Identify geographic patterns in sales
✅ Spot outliers (overperforming/underperforming)
✅ Support data-driven territory adjustments

**Recommendations:**
- Reallocate resources to underperforming territories
- Investigate success factors in top territories
- Consider splitting high-performing territories

---

## Real-World Case Study 2: Demographic Mapping for Marketing

**Business Problem:**

Marketing team needs to:
- Identify target demographics by location
- Plan advertising spend by region
- Understand market penetration
- Find expansion opportunities

**Visualization Strategy:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load geography
states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
us_states = states[states['iso_a3'] == 'USA'].copy()

# Generate demographic data
np.random.seed(42)
us_states['median_income'] = np.random.randint(40000, 80000, len(us_states))
us_states['age_25_34_pct'] = np.random.uniform(10, 20, len(us_states))
us_states['market_penetration'] = np.random.uniform(5, 40, len(us_states))

# Classify states by income and age (bivariate)
us_states['income_class'] = pd.qcut(us_states['median_income'], q=3, labels=[0, 1, 2])
us_states['age_class'] = pd.qcut(us_states['age_25_34_pct'], q=3, labels=[0, 1, 2])
us_states['bivar_class'] = (us_states['income_class'].astype(int) * 3 + 
                            us_states['age_class'].astype(int))

# Bivariate color scheme
from matplotlib.colors import ListedColormap
bivar_colors = [
    '#e8e8e8', '#b8d6be', '#73ae80',  # Low income
    '#d3b0c3', '#9972af', '#5a3d99',  # Med income
    '#c85a5a', '#985356', '#574249'   # High income
]
bivar_cmap = ListedColormap(bivar_colors)

# Create visualization
fig, axes = plt.subplots(1, 2, figsize=(20, 8))

# Bivariate map: Income × Young Adults
us_states.plot(column='bivar_class', cmap=bivar_cmap, 
              ax=axes[0], edgecolor='black', linewidth=0.5, legend=False)
axes[0].set_title('Target Demographics: Income × Young Adults %', 
                 fontsize=14, fontweight='bold')
axes[0].axis('off')

# Add legend
from matplotlib.patches import Rectangle
legend_ax = fig.add_axes([0.12, 0.15, 0.12, 0.12])
for i in range(3):
    for j in range(3):
        rect = Rectangle((j, i), 1, 1, facecolor=bivar_colors[i*3+j],
                        edgecolor='black', linewidth=1)
        legend_ax.add_patch(rect)
legend_ax.text(1.5, -0.4, '% Young Adults →', ha='center', fontsize=10, fontweight='bold')
legend_ax.text(-0.6, 1.5, 'Income\n↑', ha='center', va='center', 
              fontsize=10, fontweight='bold', rotation=90)
legend_ax.set_xlim([0, 3])
legend_ax.set_ylim([0, 3])
legend_ax.axis('off')

# Market penetration
us_states.plot(column='market_penetration', cmap='RdYlGn', 
              legend=True, ax=axes[1], edgecolor='black', linewidth=0.5,
              legend_kwds={'label': 'Penetration (%)', 'shrink': 0.8})
axes[1].set_title('Current Market Penetration', fontsize=14, fontweight='bold')
axes[1].axis('off')

plt.suptitle('Demographic & Market Analysis', fontsize=18, fontweight='bold')
plt.tight_layout()
plt.show()
```

**Strategic Actions:**
1. **High Priority** (High income, Young adults, Low penetration): Growth opportunity
2. **Maintain** (High penetration areas): Customer retention
3. **Evaluate** (Low income, Low penetration): Consider exit strategy

---

## Real-World Case Study 3: Store Location Optimization

**Business Problem:**

Retail chain wants to:
- Open 10 new stores
- Maximize market coverage
- Minimize cannibalization
- Consider competitor locations

**Analysis Approach:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Voronoi
from shapely.geometry import Point, Polygon

# Current store locations
np.random.seed(42)
existing_stores = gpd.GeoDataFrame({
    'store_id': range(1, 16),
    'sales': np.random.randint(1000000, 3000000, 15),
    'geometry': gpd.points_from_xy(
        np.random.uniform(-100, -95, 15),
        np.random.uniform(29, 33, 15)
    )
}, crs='EPSG:4326')

# Potential new locations
candidates = gpd.GeoDataFrame({
    'site_id': range(1, 21),
    'population_nearby': np.random.randint(50000, 200000, 20),
    'competitor_count': np.random.randint(0, 5, 20),
    'geometry': gpd.points_from_xy(
        np.random.uniform(-100, -95, 20),
        np.random.uniform(29, 33, 20)
    )
}, crs='EPSG:4326')

# Calculate score (higher = better)
candidates['score'] = (candidates['population_nearby'] / 
                      (candidates['competitor_count'] + 1))

# Select top candidates
top_candidates = candidates.nlargest(10, 'score')

# Visualize
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Current coverage (Voronoi)
ax1 = axes[0]
ax1.set_xlim([-100.5, -94.5])
ax1.set_ylim([28.5, 33.5])

# Plot existing stores
existing_stores.plot(ax=ax1, color='blue', markersize=100, 
                    edgecolor='black', linewidth=2, zorder=5, label='Existing')

# Simple coverage circles
for idx, store in existing_stores.iterrows():
    circle = store.geometry.buffer(0.5)  # ~50 km radius
    gpd.GeoSeries([circle]).plot(ax=ax1, facecolor='blue', 
                                 alpha=0.1, edgecolor='blue', linewidth=1)

ax1.set_title('Current Store Coverage', fontsize=14, fontweight='bold')
ax1.legend(fontsize=11)
ax1.axis('off')

# Proposed expansion
ax2 = axes[1]
ax2.set_xlim([-100.5, -94.5])
ax2.set_ylim([28.5, 33.5])

# Existing stores
existing_stores.plot(ax=ax2, color='blue', markersize=100, 
                    edgecolor='black', linewidth=2, zorder=5, label='Existing')

# Top candidates
top_candidates.plot(ax=ax2, markersize=top_candidates['score']/500, 
                   color='green', alpha=0.7, edgecolor='darkgreen', 
                   linewidth=2, zorder=5, label='Proposed')

# Coverage for proposed
for idx, store in top_candidates.iterrows():
    circle = store.geometry.buffer(0.5)
    gpd.GeoSeries([circle]).plot(ax=ax2, facecolor='green', 
                                 alpha=0.1, edgecolor='green', linewidth=1)

ax2.set_title('Proposed Expansion Plan', fontsize=14, fontweight='bold')
ax2.legend(fontsize=11)
ax2.axis('off')

plt.suptitle('Store Location Optimization Analysis', fontsize=18, fontweight='bold')
plt.tight_layout()
plt.show()

print(f"Proposed sites: {top_candidates['site_id'].tolist()}")
print(f"Average population coverage: {top_candidates['population_nearby'].mean():,.0f}")
```

**Decision Factors:**
✅ Population density
✅ Competitor proximity
✅ Existing store coverage
✅ Accessibility (roads, parking)
✅ Demographics match

---

## Real-World Case Study 4: Disease Outbreak Tracking

**Public Health Application:**

Track and visualize disease spread to:
- Identify outbreak clusters
- Allocate medical resources
- Implement targeted interventions
- Communicate risk to public

**Visualization:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN
from shapely.geometry import Point

# Generate disease case data
np.random.seed(42)

# Outbreak clusters
outbreak1 = np.random.multivariate_normal([40.7, -74.0], [[0.02, 0], [0, 0.02]], 150)
outbreak2 = np.random.multivariate_normal([34.0, -118.2], [[0.03, 0], [0, 0.03]], 100)
sporadic = np.random.uniform([25, -125], [48, -65], (50, 2))

all_cases = np.vstack([outbreak1, outbreak2, sporadic])

# Create GeoDataFrame
cases = gpd.GeoDataFrame({
    'case_id': range(len(all_cases)),
    'date_reported': pd.date_range('2024-01-01', periods=len(all_cases), freq='D'),
    'geometry': [Point(lon, lat) for lat, lon in all_cases]
}, crs='EPSG:4326')

# Perform clustering
coords = np.array(list(zip(cases.geometry.x, cases.geometry.y)))
clustering = DBSCAN(eps=0.5, min_samples=10).fit(coords)
cases['cluster'] = clustering.labels_

# Load states for context
states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
us_states = states[states['iso_a3'] == 'USA']

# Visualize
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# All cases
ax1 = axes[0]
us_states.plot(ax=ax1, color='lightgray', edgecolor='white', linewidth=0.5)
cases.plot(ax=ax1, color='red', markersize=10, alpha=0.5, edgecolor='darkred')
ax1.set_title('All Reported Cases', fontsize=14, fontweight='bold')
ax1.axis('off')

# Identified clusters
ax2 = axes[1]
us_states.plot(ax=ax2, color='lightgray', edgecolor='white', linewidth=0.5)

# Plot clusters
clusters = cases[cases['cluster'] != -1]
sporadic_cases = cases[cases['cluster'] == -1]

clusters.plot(ax=ax2, column='cluster', cmap='tab10', 
             markersize=30, alpha=0.7, edgecolor='black', 
             linewidth=1, legend=True)
sporadic_cases.plot(ax=ax2, color='gray', markersize=10, 
                   alpha=0.3, label='Sporadic')

# Highlight outbreak areas with circles
for cluster_id in clusters['cluster'].unique():
    cluster_cases = clusters[clusters['cluster'] == cluster_id]
    centroid = cluster_cases.geometry.unary_union.centroid
    buffer = centroid.buffer(1)  # Alert zone
    gpd.GeoSeries([buffer]).boundary.plot(ax=ax2, color='red', 
                                          linewidth=3, linestyle='--')

ax2.set_title('Outbreak Clusters (Hot Spot Analysis)', fontsize=14, fontweight='bold')
ax2.axis('off')

plt.suptitle('Disease Outbreak Tracking & Cluster Detection', 
            fontsize=18, fontweight='bold')
plt.tight_layout()
plt.show()

# Summary statistics
n_clusters = len(clusters['cluster'].unique())
largest_cluster = clusters.groupby('cluster').size().max()

print(f"Clusters identified: {n_clusters}")
print(f"Largest cluster: {largest_cluster} cases")
print(f"Sporadic cases: {len(sporadic_cases)}")
```

**Public Health Actions:**
1. Deploy resources to cluster areas
2. Implement contact tracing in hot spots
3. Issue public health advisories
4. Monitor spread patterns

---

## Dashboard Design for Maps

**Principles for Effective Map Dashboards:**

**1. Layout Hierarchy**

```python
# Example dashboard structure
fig = plt.figure(figsize=(20, 12))

# Main map (largest, most prominent)
ax_main = plt.subplot2grid((3, 3), (0, 0), colspan=2, rowspan=2)

# Supporting charts
ax_bar = plt.subplot2grid((3, 3), (0, 2))
ax_line = plt.subplot2grid((3, 3), (1, 2))
ax_table = plt.subplot2grid((3, 3), (2, 0), colspan=3)

# Main choropleth
# ... map code ...

ax_main.set_title('PRIMARY VIEW: Sales by Region', fontsize=16, fontweight='bold')

# Supporting visualizations
# ... bar chart, line chart, summary table ...
```

**2. Color Consistency**

```python
# Use same color scheme across related elements
primary_cmap = 'YlOrRd'

# Choropleth uses primary colors
states.plot(column='sales', cmap=primary_cmap, ax=ax_main)

# Bar chart uses same colors
colors_for_bars = plt.cm.YlOrRd(np.linspace(0.3, 0.9, len(top_states)))
ax_bar.barh(range(len(top_states)), top_states['sales'], color=colors_for_bars)
```

**3. Interactivity (with plotly)**

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create dashboard with subplots
fig = make_subplots(
    rows=2, cols=2,
    specs=[[{"type": "choropleth", "colspan": 2}, None],
           [{"type": "bar"}, {"type": "scatter"}]],
    subplot_titles=('Regional Sales Map', 'Top Performers', 'Trend')
)

# Add choropleth
fig.add_trace(
    go.Choropleth(
        # ... choropleth config ...
    ),
    row=1, col=1
)

# Add bar chart
fig.add_trace(
    go.Bar(# ... bar config ...),
    row=2, col=1
)

# Add trend line
fig.add_trace(
    go.Scatter(# ... scatter config ...),
    row=2, col=2
)

fig.update_layout(
    title_text="Sales Performance Dashboard",
    showlegend=False,
    height=800
)

fig.show()
```

**Best Practices:**
✅ **F-pattern layout**: Main map top-left, details right/bottom
✅ **Consistent colors**: Same scheme across all components
✅ **Clear labels**: Every element labeled
✅ **White space**: Don't overcrowd
✅ **Responsive design**: Works on different screen sizes

---

## Multi-Map Dashboards

**Overview + Detail Pattern:**

```python
import matplotlib.pyplot as plt
import geopandas as gpd
import numpy as np

# Load data
states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
us_states = states[states['iso_a3'] == 'USA'].copy()
np.random.seed(42)
us_states['value'] = np.random.randint(50, 150, len(us_states))

# Create figure
fig = plt.figure(figsize=(20, 10))

# Overview map (entire country)
ax_overview = plt.subplot(1, 2, 1)
us_states.plot(column='value', cmap='YlOrRd', legend=True,
              ax=ax_overview, edgecolor='black', linewidth=0.5)

# Highlight region of interest
from matplotlib.patches import Rectangle
highlight_box = Rectangle((-100, 28), 6, 5, linewidth=3, 
                         edgecolor='blue', facecolor='none', linestyle='--')
ax_overview.add_patch(highlight_box)

ax_overview.set_title('OVERVIEW: National View', fontsize=14, fontweight='bold')
ax_overview.axis('off')

# Detail map (zoomed region)
ax_detail = plt.subplot(1, 2, 2)
us_states.plot(column='value', cmap='YlOrRd', legend=False,
              ax=ax_detail, edgecolor='black', linewidth=0.5)

# Zoom to region
ax_detail.set_xlim([-100, -94])
ax_detail.set_ylim([28, 33])
ax_detail.set_title('DETAIL: Texas Region', fontsize=14, fontweight='bold')
ax_detail.axis('off')

plt.suptitle('Overview + Detail Dashboard', fontsize=18, fontweight='bold')
plt.tight_layout()
plt.show()
```

**When to Use:**
- Large geographic extent with local details
- National + state level analysis
- Context + specific findings

---

## Mobile-Friendly Maps

**Responsive Design Considerations:**

```python
import folium

# Create mobile-optimized map
m = folium.Map(
    location=[37.0902, -95.7129],
    zoom_start=4,
    tiles='CartoDB positron',
    # Mobile optimizations
    zoom_control=True,
    scrollWheelZoom=False,  # Prevent accidental zooming
    dragging=True,
    max_bounds=True  # Prevent panning too far
)

# Use larger, touch-friendly markers
folium.CircleMarker(
    [40.7, -74.0],
    radius=15,  # Larger for touch
    popup='<b style="font-size:16px">New York</b>',  # Readable text
    color='blue',
    fill=True,
    fillColor='blue'
).add_to(m)

# Save with viewport meta tag
m.save('mobile_map.html')
```

**Mobile Best Practices:**
✅ **Large touch targets** (>44px)
✅ **Readable text** (min 14px)
✅ **Simple interactions** (tap, not hover)
✅ **Fast loading** (< 3 seconds)
✅ **Offline fallback** when possible

---

## Performance Optimization

**Handling Large Datasets:**

**1. Simplify Geometries**

```python
import geopandas as gpd

# Load detailed boundaries
gdf = gpd.read_file('detailed_boundaries.shp')

# Simplify for web display
gdf_simple = gdf.copy()
gdf_simple['geometry'] = gdf_simple.geometry.simplify(
    tolerance=0.01,  # Adjust based on scale
    preserve_topology=True
)

# Reduce file size significantly
print(f"Original: {gdf.memory_usage().sum() / 1024**2:.1f} MB")
print(f"Simplified: {gdf_simple.memory_usage().sum() / 1024**2:.1f} MB")
```

**2. Use Clustering for Many Points**

```python
from folium.plugins import MarkerCluster

m = folium.Map(location=[37, -95], zoom_start=4)

# Instead of 10,000 individual markers, use clustering
marker_cluster = MarkerCluster().add_to(m)

for lat, lon in zip(lats, lons):  # 10,000 points
    folium.Marker([lat, lon]).add_to(marker_cluster)

m.save('clustered_map.html')  # Much faster!
```

**3. Progressive Loading**

```python
# Load data in chunks
chunk_size = 1000

for i in range(0, len(large_dataset), chunk_size):
    chunk = large_dataset[i:i+chunk_size]
    # Process and add to map
    # ... add markers for chunk ...
```

**4. Use Appropriate Data Types**

```python
# Optimize data types
df['category'] = df['category'].astype('category')  # Saves memory
df['value'] = df['value'].astype('float32')  # vs float64
```

**Performance Targets:**
- **< 1 second**: Initial render
- **< 100ms**: Zoom/pan response
- **< 5 MB**: Total page size
- **< 1000**: Visible elements at once

---

## Common Mistakes to Avoid

**Top 10 Geographic Visualization Pitfalls:**

**1. ❌ Using Raw Counts in Choropleth**

```python
# WRONG: Just shows population!
states.plot(column='covid_cases', cmap='Reds')

# CORRECT: Normalize by population
states['cases_per_100k'] = (states['covid_cases'] / states['population']) * 100000
states.plot(column='cases_per_100k', cmap='Reds')
```

**2. ❌ Rainbow Color Schemes**

```python
# WRONG: Perceptually non-uniform, not colorblind safe
states.plot(column='value', cmap='rainbow')

# CORRECT: Use sequential or diverging schemes
states.plot(column='value', cmap='YlOrRd')  # Sequential
# or
states.plot(column='value', cmap='RdBu')  # Diverging
```

**3. ❌ Ignoring Projections**

```python
# WRONG: Comparing areas in Web Mercator (distorted)
gdf_web_mercator = gdf.to_crs('EPSG:3857')
gdf_web_mercator['area'] = gdf_web_mercator.geometry.area  # WRONG!

# CORRECT: Use equal-area projection
gdf_equal_area = gdf.to_crs('EPSG:5070')  # Albers equal area
gdf_equal_area['area_km2'] = gdf_equal_area.geometry.area / 1_000_000
```

**4. ❌ Too Many Data Points**

```python
# WRONG: Plotting 100,000 individual points
for point in all_100k_points:
    folium.Marker(point).add_to(m)  # Slow!

# CORRECT: Use clustering or hexbin
from folium.plugins import MarkerCluster
MarkerCluster(all_100k_points).add_to(m)  # Fast!
```

**5. ❌ No Legend or Scale**

```python
# WRONG
gdf.plot(column='value')
plt.show()

# CORRECT
gdf.plot(column='value', legend=True,
        legend_kwds={'label': 'Sales ($)', 'orientation': 'horizontal'})
plt.title('Sales by Region')
plt.show()
```

**6. ❌ Inconsistent Classification**

```python
# WRONG: Different scales make comparison impossible
for year in years:
    data[year].plot(column='value', cmap='YlOrRd')  # Auto-scales each!

# CORRECT: Use same scale
vmin, vmax = data.stack().min(), data.stack().max()
for year in years:
    data[year].plot(column='value', cmap='YlOrRd', vmin=vmin, vmax=vmax)
```

**7. ❌ Alaska/Hawaii Problem**

```python
# CORRECT: Reposition AK/HI for compact display
# Use specialized tools or manually adjust positions
```

**8. ❌ Missing Attribution**

```python
# WRONG
m = folium.Map()

# CORRECT
m = folium.Map()
folium.TileLayer(
    tiles='OpenStreetMap',
    attr='© OpenStreetMap contributors'
).add_to(m)
```

**9. ❌ Overlapping Labels**

```python
# CORRECT: Use adjustText or limit labels
from adjustText import adjust_text

texts = []
for idx, row in important_only.iterrows():  # Not all points!
    texts.append(ax.text(row.geometry.x, row.geometry.y, row['name']))

adjust_text(texts)  # Automatically prevents overlap
```

**10. ❌ Not Testing on Target Devices**

Always test on:
- Different browsers
- Mobile devices
- Various screen sizes
- Slow connections

---

## Misleading Map Examples

**How Maps Can Deceive (And How to Avoid It)**

**Example 1: Mercator Distortion**

The Mercator projection severely distorts size, making Greenland appear larger than Africa (in reality, Africa is 14x larger!).

**❌ MISLEADING:**
- Using Mercator for area comparisons
- Showing global data without noting distortion

**✅ CORRECT:**
- Use equal-area projections (Albers, Lambert)
- Add disclaimer about projection distortion
- Choose projection appropriate for your data

**Example 2: Manipulated Color Scales**

```python
# ❌ MISLEADING: Truncated scale hides variation
import matplotlib.pyplot as plt
import geopandas as gpd
import numpy as np

states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
us_states = states[states['iso_a3'] == 'USA'].copy()
np.random.seed(42)
us_states['value'] = np.random.uniform(48, 52, len(us_states))

fig, axes = plt.subplots(1, 2, figsize=(18, 7))

# Misleading: Narrow range exaggerates differences
us_states.plot(column='value', cmap='RdYlGn', vmin=48, vmax=52,
              legend=True, ax=axes[0], edgecolor='black', linewidth=0.5)
axes[0].set_title('❌ MISLEADING: Exaggerated Differences', 
                 fontsize=13, fontweight='bold', color='red')
axes[0].axis('off')

# Honest: Full range shows actual variation
us_states.plot(column='value', cmap='RdYlGn', vmin=0, vmax=100,
              legend=True, ax=axes[1], edgecolor='black', linewidth=0.5)
axes[1].set_title('✅ HONEST: True Scale', 
                 fontsize=13, fontweight='bold', color='green')
axes[1].axis('off')

plt.suptitle('Impact of Color Scale Manipulation', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

**Example 3: Cherry-Picked Regions**

Showing only favorable regions while hiding others.

**❌ MISLEADING:**
- Only showing states where product performs well
- Excluding data from analysis without disclosure

**✅ CORRECT:**
- Show all regions
- If filtering, clearly state criteria
- Indicate missing/excluded data

**Red Flags for Misleading Maps:**
🚩 No data source cited
🚩 No legend or unclear units
🚩 Unusual projection choice
🚩 Inconsistent time periods
🚩 Selected regions without explanation
🚩 Truncated or inverted scales

---

## Accessibility in Maps

**Making Maps Usable for Everyone**

**Color-Blind Friendly Palettes:**

```python
import matplotlib.pyplot as plt
import geopandas as gpd
import numpy as np

states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
us_states = states[states['iso_a3'] == 'USA'].copy()
np.random.seed(42)
us_states['value'] = np.random.randint(1, 6, len(us_states))

# Color-blind safe palettes
cb_safe_palettes = {
    'Sequential': 'YlOrBr',  # Yellow-Orange-Brown
    'Diverging': 'PuOr',     # Purple-Orange
    'Qualitative': 'Set2'     # Pastels
}

fig, axes = plt.subplots(1, 3, figsize=(20, 6))

for ax, (name, cmap) in zip(axes, cb_safe_palettes.items()):
    us_states.plot(column='value', cmap=cmap, legend=True,
                  ax=ax, edgecolor='black', linewidth=0.5)
    ax.set_title(f'{name} (Color-Blind Safe)', 
                fontsize=13, fontweight='bold')
    ax.axis('off')

plt.suptitle('Color-Blind Friendly Palettes', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

**Test Your Colors:**
- Use [colorbrewer2.org](http://colorbrewer2.org) "colorblind safe" filter
- Use [Coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/) simulator
- Check contrast ratios (WCAG AA: 4.5:1 minimum)

**Don't Rely on Color Alone:**

```python
# Add patterns/textures in addition to color
import matplotlib.patches as mpatches

fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# Color only
us_states.plot(column='value', cmap='Set1', legend=True,
              ax=axes[0], edgecolor='black', linewidth=0.5)
axes[0].set_title('Color Only (❌ Not Accessible)', 
                 fontsize=13, fontweight='bold')
axes[0].axis('off')

# Color + Borders/Patterns
us_states.plot(column='value', cmap='Set1', legend=False,
              ax=axes[1], edgecolor='black', linewidth=2)  # Thicker borders
axes[1].set_title('Color + Strong Borders (✅ Better)', 
                 fontsize=13, fontweight='bold')
axes[1].axis('off')

plt.tight_layout()
plt.show()
```

**Keyboard Navigation:**
- Interactive maps should be keyboard-accessible
- Tab through features
- Enter to activate popups

**Screen Reader Support:**
- Provide alt text for static maps
- Include data table alongside map
- Describe key patterns in caption

**Accessibility Checklist:**
- [ ] Color-blind safe palette used
- [ ] Contrast ratio meets WCAG AA (4.5:1)
- [ ] Don't rely on color alone (use shapes, patterns, labels)
- [ ] Text readable (min 14px)
- [ ] Alt text provided for images
- [ ] Keyboard navigation works
- [ ] Data table alternative provided
- [ ] Clear, descriptive title and legend

---

## Map Ethics

**Responsible Geographic Visualization**

**1. Respect Privacy**

```python
# ❌ WRONG: Showing exact home locations
customers.plot()  # Individual houses visible!

# ✅ CORRECT: Aggregate to appropriate level
# ZIP code or census tract level
aggregated = customers.groupby('zip_code').size()
```

**2. Avoid Reinforcing Stereotypes**

Be careful when mapping:
- Crime by neighborhood (can reinforce racism)
- Poverty/wealth (stigmatization)
- Health conditions (discrimination)

**Best Practice:** Always provide context, historical factors, and systemic causes.

**3. Consider Impact**

Ask yourself:
- Could this map be used to harm people?
- Does it reveal sensitive information?
- Will it be misinterpreted?
- Have affected communities been consulted?

**4. Cultural Sensitivity**

- Respect disputed borders (show both claims or neutral)
- Use locally-preferred place names
- Acknowledge indigenous territories
- Note historical context

**5. Be Transparent**

Always disclose:
- Data source and collection date
- Sample size and coverage
- Limitations and uncertainties
- Methodology used
- Your affiliations and potential conflicts

**Ethical Framework:**
1. **Do No Harm**: Could this map hurt people?
2. **Informed Consent**: Do people know their data is mapped?
3. **Privacy**: Is location data sufficiently aggregated?
4. **Fairness**: Does this map reinforce inequalities?
5. **Transparency**: Are methods and limitations clear?

---

## Data Privacy on Maps

**Protecting Individual Privacy**

**Problem: Location Data is Extremely Identifying**

```python
# Just 4 spatio-temporal points can uniquely identify 95% of people!
# Example: Home, work, gym, grocery store
```

**Privacy-Preserving Techniques:**

**1. Aggregation**

```python
# Instead of individual points
individual_homes = gpd.GeoDataFrame(...)  # ❌

# Aggregate to census tracts
census_tracts['count'] = individual_homes.groupby('tract_id').size()  # ✅
```

**2. Random Displacement (Jittering)**

```python
import numpy as np

# Add random noise to coordinates
np.random.seed(42)
noise_meters = 500  # 500m displacement

gdf['lon_noisy'] = gdf['lon'] + np.random.uniform(-0.005, 0.005, len(gdf))
gdf['lat_noisy'] = gdf['lat'] + np.random.uniform(-0.005, 0.005, len(gdf))
```

**3. K-Anonymity**

Ensure each location has at least k individuals:

```python
# Remove cells with < 5 people
min_count = 5
aggregated = aggregated[aggregated['count'] >= min_count]
```

**4. Differential Privacy**

Add calibrated noise to protect individual privacy while preserving aggregate patterns.

**5. Heat Maps vs. Points**

```python
# Instead of exact points
folium.Marker([lat, lon]).add_to(m)  # ❌ Reveals exact location

# Use density heat map
from folium.plugins import HeatMap
HeatMap(points).add_to(m)  # ✅ Shows general area only
```

**Privacy Risk Assessment:**

| Risk Level | Mitigation |
|------------|------------|
| **High** (Individual homes) | Aggregate to tract, add noise, or use hexbins |
| **Medium** (Workplace) | Aggregate to block group minimum |
| **Low** (Public venues) | Can show with some jittering |

**Legal Requirements:**
- **GDPR** (Europe): Explicit consent for location data
- **CCPA** (California): Right to know and delete location data
- **HIPAA** (US Healthcare): Strict geographic privacy rules

**Best Practice:** When in doubt, aggregate more!

---

## Best Practices Checklist

**Before Publishing Your Map:**

**Data Quality:**
- [ ] Data source verified and credible
- [ ] Collection date within acceptable range
- [ ] Sample size sufficient for conclusions
- [ ] Missing data handled appropriately
- [ ] Outliers investigated

**Technical Accuracy:**
- [ ] Appropriate map type selected
- [ ] Correct projection for analysis type
- [ ] CRS matches across all layers
- [ ] Data properly normalized (rates, not counts)
- [ ] Classification method appropriate

**Visual Design:**
- [ ] Color scheme appropriate (sequential/diverging/categorical)
- [ ] Colors are colorblind-safe
- [ ] Legend included and clear
- [ ] Title describes what map shows
- [ ] Labels are readable (14px minimum)
- [ ] Scale bar included (if relevant)
- [ ] North arrow (if orientation matters)

**Accessibility:**
- [ ] Meets WCAG AA contrast requirements
- [ ] Doesn't rely solely on color
- [ ] Alt text provided for static maps
- [ ] Keyboard navigation works (interactive)
- [ ] Screen reader compatible

**Ethics & Privacy:**
- [ ] Individual privacy protected
- [ ] Sensitive data aggregated appropriately
- [ ] No harmful stereotypes reinforced
- [ ] Cultural sensitivity considered
- [ ] Informed consent obtained (if needed)

**Documentation:**
- [ ] Data source cited
- [ ] Methodology explained
- [ ] Limitations noted
- [ ] Update date shown
- [ ] Contact information provided
- [ ] License/usage rights clear

**Performance:**
- [ ] Loads in < 3 seconds
- [ ] Interactive response < 100ms
- [ ] Works on mobile devices
- [ ] File size < 5 MB
- [ ] Tested on target browsers

**Communication:**
- [ ] Main insight is obvious
- [ ] Supports intended message
- [ ] Matches audience expertise level
- [ ] Call-to-action clear (if applicable)

---

## Exercise 1: Create Choropleth Map

**Task:** Create a choropleth map showing unemployment rates by state.

**Requirements:**
1. Use sample unemployment data
2. Choose appropriate color scheme
3. Add legend and title
4. Normalize data properly
5. Include data source

**Starter Code:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load state boundaries
states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
us_states = states[states['iso_a3'] == 'USA'].copy()

# Generate sample unemployment data
np.random.seed(42)
us_states['unemployment_rate'] = np.random.uniform(3, 8, len(us_states))

# YOUR CODE HERE: Create choropleth map
# 1. Choose color scheme
# 2. Add legend
# 3. Add title
# 4. Format professionally

plt.show()
```

---

## Exercise 2: Interactive Point Map

**Task:** Create an interactive folium map with store locations and sales data.

**Requirements:**
1. Use marker clustering for performance
2. Add popups with store details
3. Color markers by performance level
4. Include basemap selection

**Starter Code:**

```python
import folium
from folium.plugins import MarkerCluster
import pandas as pd
import numpy as np

# Generate sample store data
np.random.seed(42)
stores = pd.DataFrame({
    'store_id': range(1, 51),
    'name': [f'Store {i}' for i in range(1, 51)],
    'lat': np.random.uniform(25, 48, 50),
    'lon': np.random.uniform(-125, -65, 50),
    'sales': np.random.randint(100000, 1000000, 50)
})

# YOUR CODE HERE: Create interactive map
# 1. Create folium map
# 2. Add markers with clustering
# 3. Add popups showing store details
# 4. Color code by sales performance

# m.save('store_map.html')
```

---

## Exercise 3: Multi-Layer Dashboard

**Task:** Create a dashboard combining choropleth, bubble map, and supporting charts.

**Requirements:**
1. Main map: Choropleth of sales by region
2. Overlay: Bubble map of store locations
3. Bar chart: Top 10 performers
4. Line chart: Sales trend
5. Consistent color scheme throughout

---

## Assignment Overview

**Final Project: Geographic Data Analysis**

**Choose one scenario:**

**Option A: Business Analysis**
- Analyze sales territories
- Identify expansion opportunities
- Create executive dashboard

**Option B: Public Health**
- Track disease outbreak
- Identify hot spots
- Recommend interventions

**Option C: Demographics**
- Map target market segments
- Analyze market penetration
- Plan marketing strategy

**Deliverables:**
1. **Interactive Dashboard** (HTML with folium/plotly)
2. **Static Report** (PDF with matplotlib maps)
3. **Written Analysis** (2-3 pages)
   - Methodology
   - Key findings
   - Recommendations
4. **Code Notebook** (Jupyter with documentation)

**Rubric:**
- Data quality & appropriateness (20%)
- Visualization design & clarity (25%)
- Technical execution (20%)
- Analysis & insights (20%)
- Documentation & presentation (15%)

**Due:** End of week 3

---

## Resources & References

**Data Sources:**

**Geographic Boundaries:**
- **Natural Earth**: [naturalearthdata.com](https://naturalearthdata.com) - Country, state, city boundaries
- **US Census TIGER**: [census.gov/geo/maps-data/data/tiger.html](https://www.census.gov/geo/maps-data/data/tiger.html) - Detailed US boundaries
- **GADM**: [gadm.org](https://gadm.org) - Administrative boundaries worldwide
- **OpenStreetMap**: [openstreetmap.org](https://www.openstreetmap.org) - Crowdsourced geographic data

**Demographic & Economic Data:**
- **US Census Bureau**: [census.gov](https://www.census.gov)
- **World Bank**: [data.worldbank.org](https://data.worldbank.org)
- **OECD**: [stats.oecd.org](https://stats.oecd.org)

**Health Data:**
- **CDC**: [cdc.gov/datastatistics](https://www.cdc.gov/datastatistics/)
- **WHO**: [who.int/data](https://www.who.int/data)

**Basemap Tiles:**
- **OpenStreetMap**: Free, open
- **Stamen**: Artistic tiles
- **CartoDB**: Clean, minimal
- **Mapbox**: Customizable (requires API key)

**Documentation & Tutorials:**

**Libraries:**
- **geopandas**: [geopandas.org](https://geopandas.org)
- **folium**: [python-visualization.github.io/folium](https://python-visualization.github.io/folium/)
- **plotly**: [plotly.com/python/maps](https://plotly.com/python/maps/)
- **contextily**: [contextily.readthedocs.io](https://contextily.readthedocs.io)

**Books:**
- "Python for Geospatial Data Analysis" by Bonny P. McClain
- "Geographic Data Science with Python" by Geographic Data Science Lab
- "Cartography: Thematic Map Design" by Slocum et al.

**Online Courses:**
- Coursera: "Geographic Information Systems (GIS)"
- DataCamp: "Visualizing Geospatial Data in Python"

**Tools:**
- **QGIS**: Free desktop GIS software
- **Kepler.gl**: Web-based geospatial analysis
- **Mapshaper**: Simplify and edit geo files

---

## Summary & Next Class

**Class 6 Summary: Geospatial & Geographic Visualization**

**Key Takeaways:**

**Fundamentals:**
✅ Understand geographic data types (points, lines, polygons, rasters)
✅ Choose appropriate map types (choropleth, symbol, heat maps)
✅ Work with coordinate systems and projections

**Tools Mastered:**
✅ **geopandas** for data manipulation and static maps
✅ **folium** for interactive web maps
✅ **plotly** for dashboards
✅ **contextily** for basemaps

**Advanced Techniques:**
✅ Flow maps and animations
✅ Spatial clustering and autocorrelation
✅ Hexbin aggregation and Voronoi diagrams
✅ Bivariate choropleths and small multiples

**Best Practices:**
✅ Normalize data appropriately
✅ Use color-blind safe palettes
✅ Protect individual privacy
✅ Choose projections wisely
✅ Test on multiple devices

**Common Pitfalls to Avoid:**
❌ Raw counts in choropleth maps
❌ Rainbow color schemes
❌ Ignoring projections
❌ Too many overlapping points
❌ Missing legends or attribution

**Real-World Applications:**
- Sales territory analysis
- Demographic targeting
- Store location optimization
- Public health tracking
- Market expansion planning

**Next Class Options:**

**Option A: Network & Graph Visualization**
- Social networks
- Organizational charts
- Flow diagrams
- Network analysis

**Option B: Advanced Dashboards**
- Interactive dashboards with Dash/Streamlit
- Real-time data visualization
- Multi-page applications
- Deployment strategies

**Option C: Specialized Visualizations**
- Tree maps and sunbursts
- Sankey diagrams
- Parallel coordinates
- Radar charts

**Final Thoughts:**

Geographic visualization is powerful because:
- **Location matters**: 80%+ of data has geographic component
- **Patterns emerge**: Spatial patterns invisible in tables
- **Decisions improve**: Visual insights drive action
- **Stories resonate**: Maps connect emotionally

**"A map is worth a thousand rows of data."**

**Keep practicing, keep mapping, keep discovering insights!**

---

**Class 6 Complete!** 🌍 📊 🗺️



