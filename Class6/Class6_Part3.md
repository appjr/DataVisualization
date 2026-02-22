# Class 6 – Advanced Techniques

[Part 1](Class6_Part1.md) | [Part 2](Class6_Part2.md) | [Part 3](Class6_Part3.md) | [Part 4](Class6_Part4.md)

---

# PART 3: ADVANCED GEOSPATIAL TECHNIQUES
# Slides 41-60
# ═══════════════════════════════════════════════════════════════

## Flow Maps

**Visualizing movement and connections between locations**

**What are Flow Maps?**

**Flow maps** show movement between origins and destinations, with lines representing routes and line width/color representing volume or magnitude.

**Use Cases:**
- Migration patterns
- Trade routes
- Commuter flows
- Flight paths
- Supply chain networks
- Customer movement

**Basic Flow Map with folium:**

```python
import folium
import pandas as pd

# Sample route data (flights between cities)
routes = pd.DataFrame({
    'origin_city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'dest_city': ['Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'New York'],
    'origin_lat': [40.7128, 34.0522, 41.8781, 29.7604, 33.4484],
    'origin_lon': [-74.0060, -118.2437, -87.6298, -95.3698, -112.0740],
    'dest_lat': [34.0522, 41.8781, 29.7604, 33.4484, 40.7128],
    'dest_lon': [-118.2437, -87.6298, -95.3698, -112.0740, -74.0060],
    'passengers': [15000, 12000, 8000, 6000, 10000]
})

# Create map
m = folium.Map(location=[37.0902, -95.7129], zoom_start=4, tiles='CartoDB positron')

# Add flow lines
for idx, route in routes.iterrows():
    # Line thickness based on passenger volume
    weight = route['passengers'] / 2000
    
    folium.PolyLine(
        locations=[
            [route['origin_lat'], route['origin_lon']],
            [route['dest_lat'], route['dest_lon']]
        ],
        color='blue',
        weight=weight,
        opacity=0.6,
        popup=f"{route['origin_city']} → {route['dest_city']}<br>Passengers: {route['passengers']:,}"
    ).add_to(m)
    
    # Add origin markers
    folium.CircleMarker(
        [route['origin_lat'], route['origin_lon']],
        radius=5,
        color='red',
        fill=True,
        fillColor='red',
        fillOpacity=0.7,
        popup=route['origin_city']
    ).add_to(m)

m.save('flow_map.html')
```

**Curved Flow Lines (More Aesthetic):**

```python
import folium
from folium.plugins import AntPath
import numpy as np

def create_curved_line(start, end, num_points=100):
    """Create curved line between two points"""
    lat1, lon1 = start
    lat2, lon2 = end
    
    # Create control point for bezier curve (offset to side)
    mid_lat = (lat1 + lat2) / 2
    mid_lon = (lon1 + lon2) / 2
    
    # Offset perpendicular to line
    offset = 5  # degrees
    mid_lat += offset
    
    # Generate curve points
    t = np.linspace(0, 1, num_points)
    lats = (1-t)**2 * lat1 + 2*(1-t)*t * mid_lat + t**2 * lat2
    lons = (1-t)**2 * lon1 + 2*(1-t)*t * mid_lon + t**2 * lon2
    
    return list(zip(lats, lons))

# Create map
m = folium.Map(location=[37, -95], zoom_start=4)

# Add curved flow
origin = [40.7128, -74.0060]  # NYC
destination = [34.0522, -118.2437]  # LA

curved_path = create_curved_line(origin, destination)

# Animated path
AntPath(
    locations=curved_path,
    color='blue',
    weight=3,
    opacity=0.8
).add_to(m)

m.save('curved_flow.html')
```

**Flow Map with Direction Arrows:**

```python
import folium
from folium.plugins import PolyLineTextPath

m = folium.Map(location=[37, -95], zoom_start=4)

# Create directional flow
flow_line = folium.PolyLine(
    locations=[[40.7128, -74.0060], [34.0522, -118.2437]],
    color='blue',
    weight=4,
    opacity=0.7
)

# Add arrows to show direction
PolyLineTextPath(
    flow_line,
    '          ►',
    repeat=True,
    offset=5,
    attributes={'fill': 'blue', 'font-weight': 'bold', 'font-size': '20'}
).add_to(m)

m.save('directional_flow.html')
```

**Best Practices:**

✅ **Line width** = flow magnitude (more = thicker)
✅ **Color** can encode categories or direction
✅ **Curved lines** reduce overlap and improve aesthetics
✅ **Arrows** clearly indicate direction
✅ **Limit flows** shown to avoid clutter (top N routes)

**Common Mistakes:**

❌ Too many lines (cluttered, unreadable)
❌ No directionality indication
❌ Equal width lines (magnitude lost)
❌ Straight lines crossing (hard to trace)

---

## Sankey on Maps

**Combining flow magnitude with geographic routing**

**What is a Sankey Map?**

A **Sankey map** combines traditional Sankey diagrams (flow diagrams with proportional width) with geographic routing.

**Using plotly for Sankey-Style Flows:**

```python
import plotly.graph_objects as go
import pandas as pd

# Migration data example
migration = pd.DataFrame({
    'origin': ['California', 'Texas', 'Florida', 'New York', 'Illinois'],
    'destination': ['Texas', 'California', 'North Carolina', 'Florida', 'Texas'],
    'migrants': [150000, 120000, 95000, 110000, 85000],
    'origin_lat': [36.7783, 31.9686, 27.6648, 43.2994, 40.6331],
    'origin_lon': [-119.4179, -99.9018, -81.5158, -74.2179, -89.3985],
    'dest_lat': [31.9686, 36.7783, 35.7596, 27.6648, 31.9686],
    'dest_lon': [-99.9018, -119.4179, -79.0193, -81.5158, -99.9018]
})

# Create figure
fig = go.Figure()

# Add flows as lines with width based on volume
for idx, row in migration.iterrows():
    fig.add_trace(go.Scattergeo(
        lon=[row['origin_lon'], row['dest_lon']],
        lat=[row['origin_lat'], row['dest_lat']],
        mode='lines',
        line=dict(
            width=row['migrants']/10000,
            color='rgba(100, 100, 200, 0.5)'
        ),
        hoverinfo='text',
        text=f"{row['origin']} → {row['destination']}<br>{row['migrants']:,} migrants"
    ))

# Add origin points
fig.add_trace(go.Scattergeo(
    lon=migration['origin_lon'],
    lat=migration['origin_lat'],
    mode='markers',
    marker=dict(size=10, color='red'),
    text=migration['origin'],
    hoverinfo='text'
))

fig.update_layout(
    title='Interstate Migration Flows',
    geo=dict(
        scope='usa',
        projection_type='albers usa',
        showland=True,
        landcolor='rgb(243, 243, 243)',
        coastlinecolor='rgb(204, 204, 204)',
    ),
    showlegend=False,
    height=600
)

fig.show()
```

**True Sankey Diagram (Non-Geographic):**

```python
import plotly.graph_objects as go

# Sankey for regional trade
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color='black', width=0.5),
        label=['North America', 'Europe', 'Asia', 
               'Manufacturing', 'Services', 'Agriculture',
               'Exports', 'Domestic'],
        color=['blue', 'green', 'red', 'orange', 'purple', 'brown', 'pink', 'gray']
    ),
    link=dict(
        source=[0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
        target=[3, 4, 3, 4, 3, 4, 6, 7, 6, 7, 6, 7],
        value=[100, 80, 90, 70, 150, 60, 200, 180, 120, 90, 40, 30]
    )
)])

fig.update_layout(title='Regional Trade Flows', font_size=12)
fig.show()
```

**When to Use:**

✅ Show proportional flows between regions
✅ Trade, migration, or supply chain analysis
✅ Multiple source/destination combinations
✅ Need to show relative magnitudes clearly

---

## Animated Maps

**Showing temporal change on maps**

**What are Animated Maps?**

**Animated maps** show how geographic data changes over time, using animation to reveal temporal patterns.

**Time Series Animation with plotly:**

```python
import plotly.express as px
import pandas as pd
import numpy as np

# Generate sample data: disease spread over time
dates = pd.date_range('2024-01-01', '2024-12-31', freq='W')
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
lats = [40.7128, 34.0522, 41.8781, 29.7604, 33.4484]
lons = [-74.0060, -118.2437, -87.6298, -95.3698, -112.0740]

data = []
for i, date in enumerate(dates):
    for city, lat, lon in zip(cities, lats, lons):
        cases = int(100 * (1 + i/10) * np.random.rand())
        data.append({
            'date': date,
            'city': city,
            'lat': lat,
            'lon': lon,
            'cases': cases
        })

df = pd.DataFrame(data)

# Create animated scatter plot
fig = px.scatter_geo(
    df,
    lat='lat',
    lon='lon',
    size='cases',
    color='cases',
    hover_name='city',
    animation_frame=df['date'].dt.strftime('%Y-%m-%d'),
    scope='usa',
    color_continuous_scale='Reds',
    size_max=50,
    title='Disease Spread Over Time'
)

fig.update_layout(
    geo=dict(
        projection_type='albers usa',
        showland=True,
        landcolor='rgb(243, 243, 243)'
    )
)

fig.show()
```

**Animated Choropleth:**

```python
import plotly.express as px
import pandas as pd

# Sample data: unemployment by state over years
states_data = []
years = range(2015, 2024)
states = ['California', 'Texas', 'Florida', 'New York', 'Illinois']

for year in years:
    for state in states:
        states_data.append({
            'year': year,
            'state': state,
            'unemployment': np.random.uniform(3, 8)
        })

df_states = pd.DataFrame(states_data)

# Create animated choropleth
fig = px.choropleth(
    df_states,
    locations='state',
    locationmode='USA-states',
    color='unemployment',
    animation_frame='year',
    scope='usa',
    color_continuous_scale='RdYlGn_r',
    range_color=[3, 8],
    title='Unemployment Rate by State (2015-2023)',
    labels={'unemployment': 'Unemployment %'}
)

fig.update_layout(
    geo=dict(
        projection_type='albers usa'
    )
)

fig.show()
```

**Animated Points with folium TimestampedGeoJson:**

```python
import folium
from folium.plugins import TimestampedGeoJson
import pandas as pd
from datetime import datetime, timedelta

# Generate moving point data (e.g., hurricane track)
start_date = datetime(2024, 8, 1)
track_data = []

for i in range(20):
    track_data.append({
        'time': (start_date + timedelta(hours=i*6)).isoformat(),
        'coordinates': [-80 + i*2, 25 + i*0.5],
        'popup': f'Hour {i*6}: Category {min(5, i//4 + 1)}'
    })

# Create GeoJSON features
features = []
for point in track_data:
    features.append({
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': point['coordinates']
        },
        'properties': {
            'time': point['time'],
            'popup': point['popup'],
            'icon': 'circle',
            'iconstyle': {
                'fillColor': 'red',
                'fillOpacity': 0.8,
                'stroke': 'true',
                'radius': 10
            }
        }
    })

# Create map
m = folium.Map(location=[30, -70], zoom_start=4)

# Add animated layer
TimestampedGeoJson({
    'type': 'FeatureCollection',
    'features': features
}, period='PT6H', add_last_point=True, auto_play=False, loop=False).add_to(m)

m.save('hurricane_animation.html')
```

**Best Practices:**

✅ Keep animation speed appropriate (not too fast)
✅ Provide play/pause controls
✅ Show time clearly in title or overlay
✅ Limit frame count (< 50 for smooth experience)
✅ Consider small multiples as alternative

---

## Time Series on Maps

**Visualizing temporal patterns across space**

**What are Time Series Maps?**

**Time series maps** show how values change over time at specific locations, combining temporal and spatial dimensions.

**Small Multiples for Time Comparison:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load states
states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
us_states = states[states['iso_a3'] == 'USA'].copy()

# Generate sample data for multiple years
years = [2018, 2019, 2020, 2021, 2022, 2023]
np.random.seed(42)

fig, axes = plt.subplots(2, 3, figsize=(20, 12))

for ax, year in zip(axes.flat, years):
    # Simulate changing values
    us_states['value'] = np.random.randint(50, 150, len(us_states))
    
    us_states.plot(
        column='value',
        cmap='YlOrRd',
        legend=False,
        edgecolor='black',
        linewidth=0.5,
        ax=ax,
        vmin=50,
        vmax=150
    )
    
    ax.set_title(f'Year {year}', fontsize=14, fontweight='bold')
    ax.axis('off')

# Add shared colorbar
sm = plt.cm.ScalarMappable(cmap='YlOrRd', norm=plt.Normalize(vmin=50, vmax=150))
sm._A = []
cbar = fig.colorbar(sm, ax=axes, orientation='horizontal', 
                   fraction=0.05, pad=0.05, aspect=30)
cbar.set_label('Value', fontsize=12)

plt.suptitle('Regional Values Over Time (Small Multiples)', 
            fontsize=18, fontweight='bold', y=0.98)
plt.tight_layout()
plt.show()
```

**Sparklines on Map:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# Create state centroids
states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
us_states = states[states['iso_a3'] == 'USA'].copy()
us_states['centroid'] = us_states.geometry.centroid

# Generate time series for each state
np.random.seed(42)
time_series_data = {}
for idx, state in us_states.iterrows():
    time_series_data[idx] = np.cumsum(np.random.randn(12))

# Create base map
fig, ax = plt.subplots(figsize=(16, 10))
us_states.plot(ax=ax, color='lightgray', edgecolor='black', linewidth=0.5)

# Add sparklines at centroids
for idx, state in us_states.iterrows():
    centroid = state['centroid']
    values = time_series_data[idx]
    
    # Normalize values for plotting
    values_norm = (values - values.min()) / (values.max() - values.min() + 0.001)
    
    # Create mini time series plot
    x_offset = np.linspace(-2, 2, len(values))
    y_offset = values_norm * 2 - 1
    
    ax.plot(centroid.x + x_offset, centroid.y + y_offset, 
           'b-', linewidth=1, alpha=0.7)

ax.set_title('State-Level Time Series (Sparklines on Map)', 
            fontsize=16, fontweight='bold')
ax.axis('off')
plt.tight_layout()
plt.show()
```

**Heatmap Timeline:**

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Generate data: cities × months
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 
          'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Simulate temperature data
np.random.seed(42)
data = np.random.randint(30, 90, size=(len(cities), len(months)))

df = pd.DataFrame(data, index=cities, columns=months)

# Create heatmap
fig, ax = plt.subplots(figsize=(14, 8))
sns.heatmap(df, annot=True, fmt='d', cmap='RdYlBu_r', 
           cbar_kws={'label': 'Temperature (°F)'}, ax=ax)

ax.set_title('Average Temperature by City and Month', 
            fontsize=16, fontweight='bold')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('City', fontsize=12)

plt.tight_layout()
plt.show()
```

**Best Practices:**

✅ Keep temporal resolution consistent
✅ Use same scale across time periods for comparison
✅ Consider small multiples for discrete time points
✅ Use animation for many time points
✅ Highlight trends with sparklines or line overlays

---

## Spatial Clustering

**Identifying geographic clusters in point data**

**What is Spatial Clustering?**

**Spatial clustering** groups nearby points together to reveal concentrations, hot spots, and spatial patterns.

**DBSCAN Clustering:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN
from shapely.geometry import Point

# Generate clustered point data
np.random.seed(42)

# 3 clusters
cluster1 = np.random.multivariate_normal([40.7, -74.0], [[0.01, 0], [0, 0.01]], 100)
cluster2 = np.random.multivariate_normal([34.0, -118.2], [[0.01, 0], [0, 0.01]], 150)
cluster3 = np.random.multivariate_normal([41.8, -87.6], [[0.01, 0], [0, 0.01]], 80)

points = np.vstack([cluster1, cluster2, cluster3])

# Create GeoDataFrame
geometry = [Point(lon, lat) for lat, lon in points]
gdf = gpd.GeoDataFrame({'geometry': geometry}, crs='EPSG:4326')

# Extract coordinates for clustering
coords = np.array(list(zip(gdf.geometry.x, gdf.geometry.y)))

# Apply DBSCAN
clustering = DBSCAN(eps=0.5, min_samples=5).fit(coords)
gdf['cluster'] = clustering.labels_

# Plot results
fig, axes = plt.subplots(1, 2, figsize=(18, 7))

# Before clustering
gdf.plot(ax=axes[0], color='blue', alpha=0.5, markersize=20)
axes[0].set_title('Original Points', fontsize=14, fontweight='bold')
axes[0].axis('off')

# After clustering
gdf[gdf['cluster'] != -1].plot(
    column='cluster',
    cmap='tab10',
    legend=True,
    ax=axes[1],
    markersize=30,
    alpha=0.7
)
# Plot noise points
gdf[gdf['cluster'] == -1].plot(
    ax=axes[1],
    color='gray',
    markersize=10,
    alpha=0.3,
    label='Noise'
)
axes[1].set_title('DBSCAN Clusters', fontsize=14, fontweight='bold')
axes[1].axis('off')

plt.suptitle('Spatial Clustering with DBSCAN', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

print(f"Found {len(gdf['cluster'].unique()) - 1} clusters")
print(f"Noise points: {(gdf['cluster'] == -1).sum()}")
```

**K-Means Clustering:**

```python
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Apply K-Means
n_clusters = 3
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
gdf['kmeans_cluster'] = kmeans.fit_predict(coords)

# Get cluster centers
centers = kmeans.cluster_centers_

# Plot
fig, ax = plt.subplots(figsize=(12, 10))

gdf.plot(
    column='kmeans_cluster',
    cmap='viridis',
    legend=True,
    ax=ax,
    markersize=30,
    alpha=0.6,
    categorical=True
)

# Plot cluster centers
ax.scatter(centers[:, 0], centers[:, 1], 
          c='red', s=300, alpha=0.8, 
          edgecolors='black', linewidth=2,
          marker='X', label='Cluster Centers')

ax.set_title('K-Means Clustering (k=3)', fontsize=16, fontweight='bold')
ax.legend()
ax.axis('off')

plt.tight_layout()
plt.show()
```

**Cluster Convex Hulls:**

```python
from shapely.ops import unary_union
from shapely.geometry import MultiPoint
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(14, 10))

# Plot points by cluster
gdf.plot(column='cluster', cmap='tab10', ax=ax, markersize=20, alpha=0.6)

# Draw convex hull around each cluster
for cluster_id in gdf[gdf['cluster'] != -1]['cluster'].unique():
    cluster_points = gdf[gdf['cluster'] == cluster_id]
    
    if len(cluster_points) >= 3:
        # Create convex hull
        points = MultiPoint(cluster_points.geometry.tolist())
        hull = points.convex_hull
        
        # Plot hull
        hull_gdf = gpd.GeoDataFrame([1], geometry=[hull], crs='EPSG:4326')
        hull_gdf.boundary.plot(ax=ax, color='red', linewidth=2)

ax.set_title('Clusters with Convex Hulls', fontsize=16, fontweight='bold')
ax.axis('off')
plt.tight_layout()
plt.show()
```

**Hierarchical Clustering Dendrogram:**

```python
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Perform hierarchical clustering
Z = linkage(coords[:50], method='ward')  # Use subset for clarity

# Plot dendrogram
plt.figure(figsize=(14, 7))
dendrogram(Z, truncate_mode='lastp', p=12, leaf_rotation=90, leaf_font_size=12)
plt.title('Hierarchical Clustering Dendrogram', fontsize=16, fontweight='bold')
plt.xlabel('Cluster Index', fontsize=12)
plt.ylabel('Distance', fontsize=12)
plt.tight_layout()
plt.show()
```

**Key Parameters:**

**DBSCAN:**
- `eps`: Maximum distance between points in cluster
- `min_samples`: Minimum points to form cluster
- **Pros**: Finds arbitrary shapes, handles noise
- **Cons**: Sensitive to parameters

**K-Means:**
- `n_clusters`: Number of clusters
- **Pros**: Fast, simple
- **Cons**: Requires k, assumes spherical clusters

**Best Practices:**

✅ Visualize before clustering (understand distribution)
✅ Try multiple algorithms
✅ Validate with domain knowledge
✅ Use convex hulls or buffers to show cluster extent
✅ Consider distance metrics (Euclidean vs Haversine for lat/lon)

---

---

## Spatial Autocorrelation

**Measuring spatial dependence and patterns**

**What is Spatial Autocorrelation?**

**Spatial autocorrelation** measures whether nearby locations have similar values. It answers: "Do neighboring areas tend to be similar?"

**Concepts:**
- **Positive autocorrelation**: Neighbors are similar (clustering)
- **Negative autocorrelation**: Neighbors are different (dispersion)
- **No autocorrelation**: Random spatial pattern

**Moran's I Statistic:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from libpysal.weights import Queen
from esda.moran import Moran

# Load data
states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
us_states = states[states['iso_a3'] == 'USA'].copy()

# Generate sample data with spatial pattern
np.random.seed(42)
us_states['value'] = np.random.randn(len(us_states)) * 10 + 50

# Create spatial weights matrix (defines neighbors)
w = Queen.from_dataframe(us_states)

# Calculate Moran's I
moran = Moran(us_states['value'], w)

print(f"Moran's I: {moran.I:.3f}")
print(f"p-value: {moran.p_sim:.3f}")
print(f"Expected I: {moran.EI:.3f}")

if moran.p_sim < 0.05:
    if moran.I > 0:
        print("Significant positive spatial autocorrelation (clustering)")
    else:
        print("Significant negative spatial autocorrelation (dispersion)")
else:
    print("No significant spatial autocorrelation")

# Visualize
fig, ax = plt.subplots(figsize=(12, 8))
us_states.plot(column='value', cmap='RdYlGn', legend=True, ax=ax,
              edgecolor='black', linewidth=0.5)
ax.set_title(f"Value Distribution (Moran's I = {moran.I:.3f}, p = {moran.p_sim:.3f})",
            fontsize=14, fontweight='bold')
ax.axis('off')
plt.tight_layout()
plt.show()
```

**Moran Scatterplot:**

```python
from splot.esda import plot_moran

fig, ax = plt.subplots(figsize=(10, 8))
plot_moran(moran, zstandard=True, ax=ax)
plt.title("Moran's I Scatterplot", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
```

**Local Indicators of Spatial Association (LISA):**

```python
from esda.moran import Moran_Local
from splot.esda import lisa_cluster

# Local Moran's I
lisa = Moran_Local(us_states['value'], w)

# Add to dataframe
us_states['lisa_cluster'] = lisa.q

# Define cluster labels
lisa_labels = {1: 'HH (High-High)', 2: 'LH (Low-High)', 
               3: 'LL (Low-Low)', 4: 'HL (High-Low)'}

# Plot LISA clusters
fig, ax = plt.subplots(figsize=(14, 10))

# Color by cluster type
colors = {1: 'red', 2: 'pink', 3: 'blue', 4: 'lightblue', 0: 'lightgray'}
us_states['color'] = us_states['lisa_cluster'].map(colors)

us_states.plot(color=us_states['color'], edgecolor='black', 
              linewidth=0.5, ax=ax)

# Create legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='red', label='HH: High value, high neighbors'),
    Patch(facecolor='lightblue', label='HL: High value, low neighbors'),
    Patch(facecolor='blue', label='LL: Low value, low neighbors'),
    Patch(facecolor='pink', label='LH: Low value, high neighbors'),
    Patch(facecolor='lightgray', label='Not significant')
]
ax.legend(handles=legend_elements, loc='lower left', fontsize=10)

ax.set_title('LISA Cluster Map', fontsize=16, fontweight='bold')
ax.axis('off')
plt.tight_layout()
plt.show()
```

**Getis-Ord Gi* (Hot Spot Analysis):**

```python
from esda.getisord import G_Local

# Calculate Getis-Ord Gi*
gi_star = G_Local(us_states['value'], w)

# Add to dataframe
us_states['gi_star'] = gi_star.Zs
us_states['hotspot'] = 'Not Significant'
us_states.loc[(gi_star.Zs > 1.96) & (gi_star.p_sim < 0.05), 'hotspot'] = 'Hot Spot'
us_states.loc[(gi_star.Zs < -1.96) & (gi_star.p_sim < 0.05), 'hotspot'] = 'Cold Spot'

# Plot hot spots
fig, ax = plt.subplots(figsize=(14, 10))

hotspot_colors = {'Hot Spot': 'red', 'Cold Spot': 'blue', 'Not Significant': 'lightgray'}
us_states['hs_color'] = us_states['hotspot'].map(hotspot_colors)

us_states.plot(color=us_states['hs_color'], edgecolor='black', 
              linewidth=0.5, ax=ax)

legend_elements = [
    Patch(facecolor='red', label='Hot Spot (p < 0.05)'),
    Patch(facecolor='blue', label='Cold Spot (p < 0.05)'),
    Patch(facecolor='lightgray', label='Not Significant')
]
ax.legend(handles=legend_elements, loc='lower left', fontsize=11)

ax.set_title('Getis-Ord Gi* Hot Spot Analysis', fontsize=16, fontweight='bold')
ax.axis('off')
plt.tight_layout()
plt.show()
```

**Interpretation:**

**Moran's I:**
- Range: -1 to +1
- **I > 0**: Positive autocorrelation (similar values cluster)
- **I < 0**: Negative autocorrelation (dissimilar values cluster)
- **I ≈ 0**: Random spatial pattern

**Use Cases:**
✅ Identify disease clusters
✅ Find crime hot spots
✅ Detect market concentration
✅ Validate spatial randomness assumptions

---

## Hexbin Aggregation

**Hexagonal binning for point aggregation**

**Why Hexagons?**

**Hexagons** are better than squares for spatial binning because:
- ✅ Equal distance from center to all edges
- ✅ Better sampling efficiency
- ✅ No orientation bias
- ✅ Aesthetically pleasing
- ✅ Tesselate perfectly

**Basic Hexbin with matplotlib:**

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate random point data
np.random.seed(42)
n_points = 5000
x = np.random.randn(n_points) * 2 + 10
y = np.random.randn(n_points) * 2 + 10

# Create hexbin plot
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# Scatter (original points)
axes[0].scatter(x, y, alpha=0.3, s=10)
axes[0].set_title('Original Points', fontsize=14, fontweight='bold')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')

# Hexbin aggregation
hb = axes[1].hexbin(x, y, gridsize=20, cmap='YlOrRd', mincnt=1)
axes[1].set_title('Hexbin Aggregation', fontsize=14, fontweight='bold')
axes[1].set_xlabel('X')
axes[1].set_ylabel('Y')

# Add colorbar
cb = plt.colorbar(hb, ax=axes[1])
cb.set_label('Point Count', fontsize=11)

plt.tight_layout()
plt.show()
```

**Geographic Hexbin:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point

# Generate point data (customer locations)
np.random.seed(42)
n_customers = 2000

# Clustered around major cities
clusters = [
    (40.7, -74.0, 800),   # NYC
    (34.0, -118.2, 600),  # LA
    (41.8, -87.6, 400),   # Chicago
    (29.7, -95.3, 200)    # Houston
]

points = []
for lat, lon, n in clusters:
    cluster_points = np.random.multivariate_normal(
        [lat, lon], [[0.3, 0], [0, 0.3]], n
    )
    points.extend(cluster_points)

points = np.array(points)

# Create figure
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Original points
axes[0].scatter(points[:, 1], points[:, 0], alpha=0.3, s=5, c='blue')
axes[0].set_title('Customer Locations (Points)', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Longitude')
axes[0].set_ylabel('Latitude')
axes[0].set_xlim([-130, -65])
axes[0].set_ylim([25, 50])

# Hexbin density
hb = axes[1].hexbin(points[:, 1], points[:, 0], 
                   gridsize=30, cmap='YlOrRd', mincnt=1)
axes[1].set_title('Customer Density (Hexbin)', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Longitude')
axes[1].set_ylabel('Latitude')
axes[1].set_xlim([-130, -65])
axes[1].set_ylim([25, 50])

cb = plt.colorbar(hb, ax=axes[1])
cb.set_label('Customer Count per Hexagon', fontsize=11)

plt.tight_layout()
plt.show()
```

**Hexbin with Value Aggregation:**

```python
# Generate points with values (e.g., sales)
np.random.seed(42)
n_points = 1000
x = np.random.randn(n_points) * 3 + 10
y = np.random.randn(n_points) * 3 + 10
values = np.random.exponential(100, n_points)  # Sales values

# Create figure
fig, axes = plt.subplots(1, 3, figsize=(20, 6))

# Count
hb1 = axes[0].hexbin(x, y, gridsize=15, cmap='Blues')
axes[0].set_title('Point Count', fontsize=13, fontweight='bold')
plt.colorbar(hb1, ax=axes[0])

# Sum of values
hb2 = axes[1].hexbin(x, y, C=values, gridsize=15, reduce_C_function=np.sum, cmap='Greens')
axes[1].set_title('Total Sales', fontsize=13, fontweight='bold')
plt.colorbar(hb2, ax=axes[1])

# Mean of values
hb3 = axes[2].hexbin(x, y, C=values, gridsize=15, reduce_C_function=np.mean, cmap='Oranges')
axes[2].set_title('Average Sales', fontsize=13, fontweight='bold')
plt.colorbar(hb3, ax=axes[2])

plt.tight_layout()
plt.show()
```

**H3 Hexagonal Hierarchical Geospatial Index:**

```python
# Install: pip install h3
import h3
import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt

# Function to convert H3 hexagon to polygon
def h3_to_polygon(h):
    coords = h3.h3_to_geo_boundary(h, geo_json=True)
    return Polygon(coords)

# Generate hexagons for a region
resolution = 5  # H3 resolution (0-15, higher = smaller hexes)
lat, lon = 40.7, -74.0
hexagons = h3.k_ring(h3.geo_to_h3(lat, lon, resolution), 10)

# Convert to GeoDataFrame
hex_polygons = [h3_to_polygon(h) for h in hexagons]
gdf_hexes = gpd.GeoDataFrame({'h3_id': list(hexagons)}, 
                             geometry=hex_polygons, crs='EPSG:4326')

# Assign random values
gdf_hexes['value'] = np.random.rand(len(gdf_hexes))

# Plot
fig, ax = plt.subplots(figsize=(12, 10))
gdf_hexes.plot(column='value', cmap='viridis', legend=True,
              edgecolor='white', linewidth=0.5, ax=ax)
ax.set_title(f'H3 Hexagons (Resolution {resolution})', 
            fontsize=16, fontweight='bold')
ax.axis('off')
plt.tight_layout()
plt.show()
```

**Best Practices:**

✅ Use hexagons over squares for spatial binning
✅ Adjust `gridsize` to balance detail vs clarity
✅ Choose appropriate aggregation function (count, sum, mean, median)
✅ Consider H3 for multi-scale hierarchical analysis

---

## Voronoi Diagrams

**Dividing space by nearest neighbors**

**What are Voronoi Diagrams?**

**Voronoi diagrams** partition space into regions where each region contains all points closest to a particular seed point.

**Use Cases:**
- Service area delineation
- Nearest facility analysis
- Territory assignment
- Coverage planning

**Basic Voronoi:**

```python
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import numpy as np

# Generate random seed points (e.g., store locations)
np.random.seed(42)
points = np.random.rand(20, 2) * 100

# Create Voronoi diagram
vor = Voronoi(points)

# Plot
fig, ax = plt.subplots(figsize=(12, 10))
voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='blue',
               line_width=2, line_alpha=0.6, point_size=10)

ax.set_title('Voronoi Diagram', fontsize=16, fontweight='bold')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_xlim([0, 100])
ax.set_ylim([0, 100])

plt.tight_layout()
plt.show()
```

**Geographic Voronoi with geopandas:**

```python
import geopandas as gpd
from scipy.spatial import Voronoi
from shapely.geometry import Polygon, Point
import numpy as np
import matplotlib.pyplot as plt

# Create store locations
stores = gpd.GeoDataFrame({
    'name': ['Store A', 'Store B', 'Store C', 'Store D', 'Store E'],
    'geometry': [
        Point(-96.8, 32.8),  # Dallas area
        Point(-96.7, 32.7),
        Point(-96.9, 32.9),
        Point(-96.75, 32.85),
        Point(-96.85, 32.75)
    ]
}, crs='EPSG:4326')

# Extract coordinates
coords = np.array([[p.x, p.y] for p in stores.geometry])

# Create Voronoi
vor = Voronoi(coords)

# Convert Voronoi regions to polygons
polygons = []
for region_index in vor.point_region:
    region = vor.regions[region_index]
    if -1 not in region and len(region) > 0:
        polygon = Polygon([vor.vertices[i] for i in region])
        polygons.append(polygon)
    else:
        polygons.append(None)

# Create GeoDataFrame
voronoi_gdf = gpd.GeoDataFrame({
    'store': stores['name'],
    'geometry': polygons
}, crs='EPSG:4326')

# Plot
fig, ax = plt.subplots(figsize=(12, 10))

# Plot Voronoi regions
voronoi_gdf.plot(ax=ax, alpha=0.3, edgecolor='black', 
                cmap='tab10', linewidth=2)

# Plot stores
stores.plot(ax=ax, color='red', markersize=200, 
           edgecolor='black', linewidth=2, zorder=5)

# Add labels
for idx, row in stores.iterrows():
    ax.annotate(row['name'], xy=(row.geometry.x, row.geometry.y),
               xytext=(5, 5), textcoords='offset points',
               fontsize=11, fontweight='bold')

ax.set_title('Store Service Areas (Voronoi)', fontsize=16, fontweight='bold')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

plt.tight_layout()
plt.show()
```

**Weighted Voronoi (Power Diagram):**

```python
# Assign weights (e.g., store capacity)
stores['capacity'] = [100, 150, 80, 120, 90]

# Note: True weighted Voronoi requires specialized libraries
# Here's a conceptual visualization

fig, ax = plt.subplots(figsize=(12, 10))

# Plot with bubble size = capacity
stores.plot(ax=ax, markersize=stores['capacity']*5, 
           alpha=0.5, color='blue', edgecolor='black', linewidth=2)

# Add labels
for idx, row in stores.iterrows():
    ax.annotate(f"{row['name']}\n({row['capacity']} cap)",
               xy=(row.geometry.x, row.geometry.y),
               ha='center', fontsize=10, fontweight='bold')

ax.set_title('Store Locations with Capacity', fontsize=16, fontweight='bold')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

plt.tight_layout()
plt.show()
```

**Applications:**

✅ **Retail**: Assign customers to nearest store
✅ **Healthcare**: Hospital service areas
✅ **Emergency**: Fire station coverage
✅ **Utilities**: Service territories
✅ **Wildlife**: Animal territory analysis

---

## Contour Maps

**Showing continuous surfaces with isolines**

**What are Contour Maps?**

**Contour maps** use lines (isolines) to connect points of equal value, showing continuous variation across space.

**Types:**
- **Isoline**: Generic equal-value line
- **Contour**: Equal elevation
- **Isotherm**: Equal temperature
- **Isobar**: Equal pressure
- **Isochrone**: Equal travel time

**Basic Contour Plot:**

```python
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata

# Generate sample data (elevation points)
np.random.seed(42)
n_points = 100
x = np.random.rand(n_points) * 100
y = np.random.rand(n_points) * 100
z = np.sin(x/10) * np.cos(y/10) * 50 + 50 + np.random.randn(n_points) * 5

# Create grid
xi = np.linspace(0, 100, 100)
yi = np.linspace(0, 100, 100)
xi, yi = np.meshgrid(xi, yi)

# Interpolate
zi = griddata((x, y), z, (xi, yi), method='cubic')

# Create contour plot
fig, axes = plt.subplots(1, 3, figsize=(20, 6))

# Filled contours
cf = axes[0].contourf(xi, yi, zi, levels=15, cmap='terrain')
axes[0].scatter(x, y, c='red', s=20, alpha=0.5, label='Sample Points')
axes[0].set_title('Filled Contours', fontsize=13, fontweight='bold')
axes[0].legend()
plt.colorbar(cf, ax=axes[0], label='Elevation (m)')

# Line contours
cs = axes[1].contour(xi, yi, zi, levels=15, colors='black', linewidths=1)
axes[1].clabel(cs, inline=True, fontsize=8)
axes[1].set_title('Line Contours with Labels', fontsize=13, fontweight='bold')

# Combined
cf2 = axes[2].contourf(xi, yi, zi, levels=15, cmap='terrain', alpha=0.7)
cs2 = axes[2].contour(xi, yi, zi, levels=15, colors='black', 
                     linewidths=0.5, alpha=0.5)
axes[2].scatter(x, y, c='red', s=20, alpha=0.7)
axes[2].set_title('Combined View', fontsize=13, fontweight='bold')
plt.colorbar(cf2, ax=axes[2], label='Elevation (m)')

plt.tight_layout()
plt.show()
```

**Geographic Contour Map:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata

# Create sample temperature data for US cities
cities = pd.DataFrame({
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
             'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose',
             'Seattle', 'Denver', 'Boston', 'Atlanta', 'Miami'],
    'lat': [40.7, 34.0, 41.9, 29.8, 33.4, 39.9, 29.4, 32.7, 32.8, 37.3,
            47.6, 39.7, 42.4, 33.7, 25.8],
    'lon': [-74.0, -118.2, -87.6, -95.4, -112.1, -75.2, -98.5, -117.2, 
            -96.8, -121.9, -122.3, -105.0, -71.1, -84.4, -80.2],
    'temp': [65, 72, 55, 78, 85, 64, 79, 70, 75, 68, 
             58, 62, 60, 70, 82]
})

# Create interpolation grid
lat_min, lat_max = 25, 50
lon_min, lon_max = -125, -65

grid_lat = np.linspace(lat_min, lat_max, 100)
grid_lon = np.linspace(lon_min, lon_max, 100)
grid_lon, grid_lat = np.meshgrid(grid_lon, grid_lat)

# Interpolate temperature
grid_temp = griddata(
    (cities['lon'], cities['lat']),
    cities['temp'],
    (grid_lon, grid_lat),
    method='cubic'
)

# Plot
fig, ax = plt.subplots(figsize=(16, 10))

# Filled contours
cf = ax.contourf(grid_lon, grid_lat, grid_temp, levels=20, 
                cmap='RdYlBu_r', alpha=0.8)

# Contour lines
cs = ax.contour(grid_lon, grid_lat, grid_temp, levels=10, 
               colors='black', linewidths=0.5, alpha=0.4)
ax.clabel(cs, inline=True, fontsize=9, fmt='%d°F')

# Plot cities
ax.scatter(cities['lon'], cities['lat'], c='black', s=50, 
          edgecolor='white', linewidth=1, zorder=5)

# Add city labels
for idx, row in cities.iterrows():
    ax.annotate(row['city'], xy=(row['lon'], row['lat']),
               xytext=(5, 5), textcoords='offset points',
               fontsize=8)

ax.set_title('Temperature Contour Map (Interpolated)', 
            fontsize=16, fontweight='bold')
ax.set_xlabel('Longitude', fontsize=12)
ax.set_ylabel('Latitude', fontsize=12)
ax.set_xlim([lon_min, lon_max])
ax.set_ylim([lat_min, lat_max])

plt.colorbar(cf, ax=ax, label='Temperature (°F)')
plt.tight_layout()
plt.show()
```

**Isochrone Map (Travel Time Contours):**

```python
# Conceptual example - in practice use routing APIs
import matplotlib.pyplot as plt
import numpy as np

# Store location
store_lat, store_lon = 40.7, -74.0

# Create grid
grid_size = 100
lats = np.linspace(40.5, 40.9, grid_size)
lons = np.linspace(-74.3, -73.7, grid_size)
lon_grid, lat_grid = np.meshgrid(lons, lats)

# Simulate travel time (simplified - actual would use routing)
# Distance-based approximation
travel_time = np.sqrt((lat_grid - store_lat)**2 * 69**2 + 
                     (lon_grid - store_lon)**2 * 54**2) / 30 * 60  # ~30 mph

# Plot isochrones
fig, ax = plt.subplots(figsize=(12, 10))

levels = [5, 10, 15, 20, 30, 45, 60]  # minutes
colors = ['darkgreen', 'green', 'yellow', 'orange', 'red', 'darkred', 'purple']

cf = ax.contourf(lon_grid, lat_grid, travel_time, levels=levels, 
                colors=colors, alpha=0.6)
cs = ax.contour(lon_grid, lat_grid, travel_time, levels=levels,
               colors='black', linewidths=2)
ax.clabel(cs, inline=True, fontsize=10, fmt='%d min')

# Plot store
ax.scatter([store_lon], [store_lat], c='blue', s=300, marker='*',
          edgecolor='white', linewidth=2, zorder=5, label='Store')

ax.set_title('Isochrone Map: Travel Time from Store', 
            fontsize=16, fontweight='bold')
ax.set_xlabel('Longitude', fontsize=12)
ax.set_ylabel('Latitude', fontsize=12)
ax.legend(fontsize=12)

plt.tight_layout()
plt.show()
```

**Best Practices:**

✅ Use appropriate interpolation method
✅ Label contour lines for clarity
✅ Choose color scheme that matches data type
✅ Include sample points when showing interpolated data
✅ Consider smoothing for noisy data

---

## Small Multiples for Maps

**Compare regions or time periods**

```python
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
for i, year in enumerate(years):
    data[data['year']==year].plot(ax=axes.flat[i], column='value')
```

---

## Part 3 Summary

✅ Flow and animation
✅ Clustering techniques
✅ Advanced aggregation
✅ Temporal-spatial combinations

---
