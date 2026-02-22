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

## 3D Geographic Visualization

**When (and when not) to use 3D maps**

**What is 3D Mapping?**

**3D maps** add a vertical dimension to geographic visualizations, typically representing elevation, building heights, or data values.

**When to Use (Rarely!):**
- ✅ Terrain/elevation visualization
- ✅ Urban planning (building heights)
- ✅ Dramatic presentations
- ✅ Immersive experiences

**When NOT to Use:**
- ❌ Data values (use color instead)
- ❌ Precise comparisons
- ❌ Print media
- ❌ Accessibility concerns

**3D Surface Plot:**

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create elevation data
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create 3D plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='terrain', alpha=0.8,
                      linewidth=0, antialiased=True)

ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_zlabel('Elevation', fontsize=12)
ax.set_title('3D Terrain Surface', fontsize=16, fontweight='bold')

fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

plt.tight_layout()
plt.show()
```

**3D Bar Map with plotly:**

```python
import plotly.graph_objects as go
import numpy as np

# Create sample data (sales by region)
regions = ['North', 'South', 'East', 'West', 'Central']
x_pos = [1, 1, 2, 0, 1]
y_pos = [2, 0, 1, 1, 1]
sales = [100, 80, 120, 90, 110]

fig = go.Figure(data=[go.Mesh3d(
    x=[0, 0, 1, 1, 0, 0, 1, 1],
    y=[0, 1, 1, 0, 0, 1, 1, 0],
    z=[0, 0, 0, 0, 1, 1, 1, 1],
    colorbar_title='z',
    colorscale=[[0, 'gold'],
                [0.5, 'mediumturquoise'],
                [1, 'magenta']],
    intensity=[0, 0.33, 0.66, 1, 0, 0.33, 0.66, 1],
    i=[7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
    j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
    k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
)])

fig.update_layout(
    title='3D Visualization (Use Sparingly!)',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Value'
    ),
    height=600
)

fig.show()
```

**Best Practices:**

⚠️ **Avoid 3D for data values** - Use 2D with color instead
✅ **Use for actual 3D data** (terrain, buildings)
✅ **Provide rotation/interaction** for better understanding
✅ **Include 2D alternative** for comparison
❌ **Never use 3D pie charts** or 3D bar charts for non-spatial data

**Alternative: 2.5D (Extruded Polygons):**

```python
import plotly.express as px

# Better alternative: choropleth with hover
# Shows data clearly without 3D confusion
```

**Key Insight:** "3D is often a solution looking for a problem. Use 2D with effective visual encoding instead."

---

## Cartograms

**Distorting geography to emphasize data**

**What are Cartograms?**

**Cartograms** distort the size/shape of geographic regions to make area proportional to a data variable rather than actual geographic area.

**Types:**
- **Contiguous**: Regions stay connected (topology preserved)
- **Non-contiguous**: Regions can separate
- **Dorling**: Regions become circles

**When to Use:**
- Population-weighted views
- Emphasizing data over geography
- Showing relative importance
- Alternative to choropleth

**Non-Contiguous Cartogram (Simple Scale):**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np

# Load data
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Scale geometries by population
def scale_geometry(geom, scale_factor):
    centroid = geom.centroid
    scaled = geom.scale(xfact=scale_factor, yfact=scale_factor, origin=centroid)
    return scaled

# Normalize population for scaling
world['scale'] = np.sqrt(world['pop_est'] / world['pop_est'].max())

# Create cartogram
world['cartogram_geom'] = world.apply(
    lambda row: scale_geometry(row['geometry'], row['scale']), 
    axis=1
)

# Plot comparison
fig, axes = plt.subplots(1, 2, figsize=(20, 8))

# Original
world.plot(ax=axes[0], color='lightblue', edgecolor='black', linewidth=0.5)
axes[0].set_title('Original Geographic Map', fontsize=14, fontweight='bold')
axes[0].axis('off')

# Cartogram
world.set_geometry('cartogram_geom').plot(
    ax=axes[1], color='lightcoral', edgecolor='black', linewidth=0.5
)
axes[1].set_title('Population Cartogram', fontsize=14, fontweight='bold')
axes[1].axis('off')

plt.suptitle('Geography vs Population-Weighted View', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

**Dorling Cartogram (Circle-based):**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point

# Load US states
states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
us_states = states[states['iso_a3'] == 'USA'].copy()

# Get centroids
us_states['centroid'] = us_states.geometry.centroid

# Create circles proportional to population
us_states['circle_radius'] = np.sqrt(us_states['pop_est'] / np.pi) / 100000

# Create circle geometries
us_states['circles'] = us_states.apply(
    lambda row: row['centroid'].buffer(row['circle_radius']), 
    axis=1
)

# Plot
fig, axes = plt.subplots(1, 2, figsize=(20, 8))

# Original
us_states.plot(column='pop_est', cmap='YlOrRd', legend=True,
              ax=axes[0], edgecolor='black', linewidth=0.5)
axes[0].set_title('Traditional Choropleth', fontsize=14, fontweight='bold')
axes[0].axis('off')

# Dorling Cartogram
us_states.set_geometry('circles').plot(
    column='pop_est', cmap='YlOrRd', legend=True,
    ax=axes[1], edgecolor='black', linewidth=1
)
axes[1].set_title('Dorling Cartogram (Circle Size = Population)', 
                 fontsize=14, fontweight='bold')
axes[1].axis('off')

plt.suptitle('Choropleth vs Dorling Cartogram', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

**Hexagonal Cartogram:**

```python
# Conceptual - create hexagonal grid
import matplotlib.pyplot as plt
import numpy as np

# Simple hex grid representation
fig, ax = plt.subplots(figsize=(12, 10))

# Each state becomes a hexagon
# Position based on actual geography (approximated)
states_hex = {
    'CA': (0, 2), 'OR': (0, 3), 'WA': (0, 4),
    'TX': (3, 1), 'NY': (8, 4), 'FL': (7, 0),
    # ... etc
}

# Draw hexagons
for state, (x, y) in states_hex.items():
    hexagon = plt.Circle((x, y), 0.4, color='lightblue', 
                        edgecolor='black', linewidth=2)
    ax.add_patch(hexagon)
    ax.text(x, y, state, ha='center', va='center', 
           fontweight='bold', fontsize=10)

ax.set_xlim([-1, 10])
ax.set_ylim([-1, 6])
ax.set_aspect('equal')
ax.set_title('Hexagonal Tile Cartogram (Conceptual)', 
            fontsize=16, fontweight='bold')
ax.axis('off')

plt.tight_layout()
plt.show()
```

**Pros and Cons:**

**Pros:**
✅ Equal visual weight per unit of data
✅ Reduces geographic bias
✅ Makes small regions visible

**Cons:**
❌ Unfamiliar to readers
❌ Hard to identify regions
❌ Can be misleading if not explained

**Best Practice:** Always show both traditional map AND cartogram for comparison

---

## Dot Density Maps

**One dot = N units**

**What are Dot Density Maps?**

**Dot density maps** place individual dots to represent quantities, where each dot represents a fixed number of units (e.g., 1 dot = 100 people).

**When to Use:**
- Show distribution within regions
- Reveal patterns invisible in choropleth
- Raw counts (not rates)
- Multiple categories

**Basic Dot Density:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point

# Load states
states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
us_states = states[states['iso_a3'] == 'USA'].copy()

# Generate random points within polygons
def generate_points_in_polygon(polygon, n_points):
    """Generate random points inside polygon"""
    min_x, min_y, max_x, max_y = polygon.bounds
    points = []
    
    while len(points) < n_points:
        random_point = Point(np.random.uniform(min_x, max_x),
                            np.random.uniform(min_y, max_y))
        if polygon.contains(random_point):
            points.append(random_point)
    
    return points

# Create dots (1 dot = 1 million people)
dots_per_million = 1
all_dots = []

for idx, state in us_states.iterrows():
    n_dots = int(state['pop_est'] / 1_000_000)
    if n_dots > 0:
        dots = generate_points_in_polygon(state.geometry, n_dots)
        all_dots.extend(dots)

# Create GeoDataFrame of dots
dots_gdf = gpd.GeoDataFrame({'geometry': all_dots}, crs='EPSG:4326')

# Plot
fig, axes = plt.subplots(1, 2, figsize=(20, 8))

# Choropleth
us_states.plot(column='pop_est', cmap='YlOrRd', legend=True,
              ax=axes[0], edgecolor='black', linewidth=0.5)
axes[0].set_title('Choropleth: Population by State', 
                 fontsize=14, fontweight='bold')
axes[0].axis('off')

# Dot density
us_states.plot(ax=axes[1], color='white', edgecolor='black', linewidth=0.5)
dots_gdf.plot(ax=axes[1], color='red', markersize=5, alpha=0.6)
axes[1].set_title('Dot Density: 1 dot = 1M people', 
                 fontsize=14, fontweight='bold')
axes[1].axis('off')

plt.suptitle('Choropleth vs Dot Density', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

**Multi-Category Dot Density:**

```python
import matplotlib.pyplot as plt
import numpy as np

# Simulate multi-category data (population by ethnicity)
np.random.seed(42)

# Generate dots for different categories
categories = {
    'Category A': {'color': 'red', 'n_dots': 500},
    'Category B': {'color': 'blue', 'n_dots': 300},
    'Category C': {'color': 'green', 'n_dots': 200}
}

fig, ax = plt.subplots(figsize=(12, 10))

for category, props in categories.items():
    # Random points within a region
    x = np.random.rand(props['n_dots']) * 10
    y = np.random.rand(props['n_dots']) * 10
    ax.scatter(x, y, c=props['color'], s=10, alpha=0.6, label=category)

ax.set_title('Multi-Category Dot Density Map', fontsize=16, fontweight='bold')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend(title='Categories', fontsize=11)
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])

plt.tight_layout()
plt.show()
```

**Dasymetric Mapping (Intelligent Dot Placement):**

```python
# Conceptual: Place dots only in habitable areas
# In practice, use land cover data to avoid water, mountains, etc.

# Example: Avoid placing dots in water bodies
# dots_gdf = dots_gdf[~dots_gdf.intersects(water_bodies)]
```

**Best Practices:**

✅ **Specify dot value** clearly (1 dot = X units)
✅ **Use for raw counts**, not rates
✅ **Random placement** within regions
✅ **Semi-transparent dots** for overlap
✅ **Consider dasymetric** for accuracy

**Advantages over Choropleth:**
- Shows distribution within regions
- Doesn't hide variation in large regions
- Visually intuitive (more dots = more units)

---

## Proportional Symbol Maps

**Size encodes magnitude**

**What are Proportional Symbol Maps?**

**Proportional symbol maps** use symbols (usually circles) sized proportionally to represent data values at specific locations.

**When to Use:**
- Point data with associated values
- Absolute quantities (not rates)
- Multiple locations to compare
- Want to show both location AND magnitude

**Basic Proportional Symbols:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

# Sample data: Cities with populations
cities = gpd.GeoDataFrame({
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
             'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'],
    'population': [8336000, 3979000, 2693000, 2320000, 1680000,
                   1584000, 1547000, 1423000, 1343000, 1021000],
    'geometry': gpd.points_from_xy(
        [-74.0, -118.2, -87.6, -95.4, -112.1, -75.2, -98.5, -117.2, -96.8, -121.9],
        [40.7, 34.0, 41.9, 29.8, 33.4, 39.9, 29.4, 32.7, 32.8, 37.3]
    )
}, crs='EPSG:4326')

# Load US states for context
states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
us_states = states[states['iso_a3'] == 'USA']

# Plot
fig, ax = plt.subplots(figsize=(16, 10))

# Base map
us_states.plot(ax=ax, color='lightgray', edgecolor='white', linewidth=0.5)

# Proportional symbols
cities.plot(ax=ax,
           markersize=cities['population']/10000,  # Scale for visibility
           color='red',
           alpha=0.6,
           edgecolor='darkred',
           linewidth=1.5)

# Add city labels
for idx, row in cities.iterrows():
    ax.annotate(row['city'], 
               xy=(row.geometry.x, row.geometry.y),
               xytext=(5, 5),
               textcoords='offset points',
               fontsize=9,
               fontweight='bold')

# Add manual legend
from matplotlib.lines import Line2D
legend_sizes = [1000000, 5000000, 8000000]
legend_elements = [
    Line2D([0], [0], marker='o', color='w', 
          markerfacecolor='red', markersize=np.sqrt(s/10000), 
          alpha=0.6, label=f'{s/1000000:.0f}M')
    for s in legend_sizes
]
ax.legend(handles=legend_elements, title='Population', 
         loc='lower left', fontsize=11, frameon=True)

ax.set_title('US Cities: Proportional Symbol Map', 
            fontsize=16, fontweight='bold')
ax.axis('off')

plt.tight_layout()
plt.show()
```

**Scaled vs Unscaled:**

```python
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Linearly scaled (WRONG - hard to compare)
us_states.plot(ax=axes[0], color='lightgray', edgecolor='white')
cities.plot(ax=axes[0],
           markersize=cities['population']/50000,
           color='blue', alpha=0.6)
axes[0].set_title('❌ Linear Scaling (Misleading)', 
                 fontsize=13, fontweight='bold', color='red')
axes[0].axis('off')

# Square root scaled (CORRECT - area proportional)
us_states.plot(ax=axes[1], color='lightgray', edgecolor='white')
cities.plot(ax=axes[1],
           markersize=np.sqrt(cities['population'])*2,
           color='green', alpha=0.6)
axes[1].set_title('✅ Square Root Scaling (Correct)', 
                 fontsize=13, fontweight='bold', color='green')
axes[1].axis('off')

plt.suptitle('Importance of Proper Scaling', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

**Graduated Symbols (Binned):**

```python
# Bin into size classes
cities['size_class'] = pd.cut(cities['population'], 
                              bins=[0, 2000000, 5000000, 10000000],
                              labels=['Small', 'Medium', 'Large'])

size_map = {'Small': 50, 'Medium': 150, 'Large': 300}
cities['marker_size'] = cities['size_class'].map(size_map)

fig, ax = plt.subplots(figsize=(14, 10))

us_states.plot(ax=ax, color='lightgray', edgecolor='white')

for size_class in ['Small', 'Medium', 'Large']:
    subset = cities[cities['size_class'] == size_class]
    subset.plot(ax=ax,
               markersize=size_map[size_class],
               color='purple',
               alpha=0.6,
               edgecolor='black',
               linewidth=1,
               label=size_class)

ax.legend(title='City Size', fontsize=11)
ax.set_title('Graduated Symbol Map', fontsize=16, fontweight='bold')
ax.axis('off')

plt.tight_layout()
plt.show()
```

**Multivariate Symbols (Size + Color):**

```python
# Add GDP per capita data
cities['gdp_per_capita'] = np.random.uniform(40000, 80000, len(cities))

fig, ax = plt.subplots(figsize=(14, 10))

us_states.plot(ax=ax, color='lightgray', edgecolor='white')

# Size = population, Color = GDP per capita
scatter = ax.scatter(
    cities.geometry.x,
    cities.geometry.y,
    s=cities['population']/10000,
    c=cities['gdp_per_capita'],
    cmap='RdYlGn',
    alpha=0.7,
    edgecolors='black',
    linewidth=1.5
)

# Colorbars
cbar = plt.colorbar(scatter, ax=ax, shrink=0.6)
cbar.set_label('GDP per Capita ($)', fontsize=11)

ax.set_title('Multivariate Map: Size = Population, Color = GDP per Capita',
            fontsize=15, fontweight='bold')
ax.axis('off')

plt.tight_layout()
plt.show()
```

**Best Practices:**

✅ **Scale by radius**, not area (use markersize in matplotlib)
✅ **Limit symbol count** (< 50 for clarity)
✅ **Use transparency** for overlapping symbols
✅ **Include legend** with example sizes
✅ **Consider binning** for many similar values

**Common Mistakes:**

❌ Scaling by diameter or area instead of radius
❌ Too many overlapping symbols
❌ No legend showing scale
❌ Using for rates/ratios (use choropleth instead)

---

## Bivariate Choropleth

**Visualizing two variables simultaneously**

**What are Bivariate Choropleths?**

**Bivariate choropleths** encode TWO variables using a 2D color scheme, allowing comparison of relationships across space.

**When to Use:**
- Explore correlation between two variables
- Show multi-dimensional patterns
- Reveal spatial relationships
- Advanced analysis

**Challenges:**
- Complex legend
- Harder to interpret
- Requires training

**Creating Bivariate Color Scheme:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
import pandas as pd

# Load data
states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
us_states = states[states['iso_a3'] == 'USA'].copy()

# Generate two variables
np.random.seed(42)
us_states['var1'] = np.random.uniform(0, 100, len(us_states))  # e.g., Income
us_states['var2'] = np.random.uniform(0, 100, len(us_states))  # e.g., Education

# Classify into 3x3 bins
us_states['var1_class'] = pd.qcut(us_states['var1'], q=3, labels=[0, 1, 2])
us_states['var2_class'] = pd.qcut(us_states['var2'], q=3, labels=[0, 1, 2])

# Create combined class (0-8)
us_states['bivar_class'] = (us_states['var1_class'].astype(int) * 3 + 
                            us_states['var2_class'].astype(int))

# Define bivariate color scheme
# Rows = var1 (low to high), Columns = var2 (low to high)
bivar_colors = [
    '#e8e8e8', '#b8d6be', '#73ae80',  # Low var1
    '#d3b0c3', '#9972af', '#5a3d99',  # Med var1
    '#c85a5a', '#985356', '#574249'   # High var1
]

# Create colormap
bivar_cmap = ListedColormap(bivar_colors)

# Plot
fig, ax = plt.subplots(figsize=(14, 10))

us_states.plot(column='bivar_class',
              cmap=bivar_cmap,
              edgecolor='black',
              linewidth=0.5,
              ax=ax,
              legend=False)

ax.set_title('Bivariate Choropleth: Income × Education',
            fontsize=16, fontweight='bold')
ax.axis('off')

# Create custom legend (3x3 grid)
from matplotlib.patches import Rectangle

# Add legend box
legend_ax = fig.add_axes([0.15, 0.15, 0.15, 0.15])
legend_ax.set_xlim([0, 3])
legend_ax.set_ylim([0, 3])

# Draw 3x3 grid
for i in range(3):
    for j in range(3):
        color_idx = i * 3 + j
        rect = Rectangle((j, i), 1, 1, 
                        facecolor=bivar_colors[color_idx],
                        edgecolor='black', linewidth=1)
        legend_ax.add_patch(rect)

# Labels
legend_ax.text(1.5, -0.5, 'Education →', ha='center', fontsize=11, fontweight='bold')
legend_ax.text(-0.7, 1.5, 'Income\n↑', ha='center', va='center', 
              fontsize=11, fontweight='bold', rotation=90)

legend_ax.set_xlim([0, 3])
legend_ax.set_ylim([0, 3])
legend_ax.axis('off')

plt.tight_layout()
plt.show()
```

**Diverging Bivariate:**

```python
# For data with meaningful midpoints
# e.g., Change in Variable 1 vs Change in Variable 2

# Diverging bivariate colors (9 classes)
div_bivar_colors = [
    '#3b4994', '#8c62aa', '#e47eb4',  # Decrease in both → Increase in var2
    '#5698b9', '#a5a5a5', '#e88e2e',  # No change var1, varying var2
    '#00796b', '#b8c769', '#f4c72e'   # Increase in both
]

# Same plotting approach as above
```

**Advantages:**

✅ Show relationships between variables
✅ Reveal spatial patterns in correlations
✅ More information in single map

**Disadvantages:**

❌ Complex to interpret
❌ Requires legend explanation
❌ Not colorblind-friendly
❌ Harder for general audiences

**Alternative: Small Multiples**

```python
# Often clearer than bivariate
fig, axes = plt.subplots(1, 2, figsize=(18, 7))

us_states.plot(column='var1', cmap='Blues', legend=True,
              ax=axes[0], edgecolor='black', linewidth=0.5)
axes[0].set_title('Income', fontsize=14, fontweight='bold')
axes[0].axis('off')

us_states.plot(column='var2', cmap='Greens', legend=True,
              ax=axes[1], edgecolor='black', linewidth=0.5)
axes[1].set_title('Education', fontsize=14, fontweight='bold')
axes[1].axis('off')

plt.suptitle('Side-by-Side Comparison (Often Clearer!)',
            fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

**When to Use:**
- Research/analysis contexts
- Sophisticated audiences
- Exploring variable relationships
- When small multiples won't fit

---

## Small Multiples for Maps

**Comparing regions or time periods side-by-side**

**What are Small Multiples?**

**Small multiples** (also called trellis charts or panel charts) show multiple related maps in a grid layout, allowing easy comparison across categories or time periods.

**When to Use:**
- Compare time periods
- Compare regions
- Show multiple related variables
- Alternative to animation

**Time Series Small Multiples:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load states
states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
us_states = states[states['iso_a3'] == 'USA'].copy()

# Generate data for 6 years
years = [2018, 2019, 2020, 2021, 2022, 2023]
np.random.seed(42)

fig, axes = plt.subplots(2, 3, figsize=(20, 12))

for ax, year in zip(axes.flat, years):
    # Simulate different values each year
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

**Comparing Different Variables:**

```python
import matplotlib.pyplot as plt

# Generate multiple variables
variables = ['Population', 'GDP', 'Education', 'Healthcare']
np.random.seed(42)

for var in variables:
    us_states[var] = np.random.uniform(0, 100, len(us_states))

# Plot each variable
fig, axes = plt.subplots(2, 2, figsize=(18, 14))

for ax, var in zip(axes.flat, variables):
    us_states.plot(
        column=var,
        cmap='viridis',
        legend=True,
        edgecolor='black',
        linewidth=0.5,
        ax=ax
    )
    ax.set_title(var, fontsize=14, fontweight='bold')
    ax.axis('off')

plt.suptitle('Comparing Multiple Variables', fontsize=18, fontweight='bold')
plt.tight_layout()
plt.show()
```

**Regional Comparison:**

```python
# Compare different regions
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

fig, axes = plt.subplots(2, 3, figsize=(20, 12))

for ax, continent in zip(axes.flat, continents):
    region = world[world['continent'] == continent]
    
    region.plot(
        column='gdp_md_est',
        cmap='YlGn',
        legend=False,
        edgecolor='black',
        linewidth=0.5,
        ax=ax
    )
    
    ax.set_title(continent, fontsize=14, fontweight='bold')
    ax.axis('off')

plt.suptitle('GDP by Continent', fontsize=18, fontweight='bold')
plt.tight_layout()
plt.show()
```

**Best Practices:**

✅ **Use same color scale** across all panels for comparison
✅ **Keep layouts consistent** (same size, orientation)
✅ **Label clearly** with titles
✅ **Limit panel count** (9-12 maximum)
✅ **Arrange logically** (time: left to right, categories: by importance)

**Advantages over Animation:**
- See all at once (no memory required)
- Easy to compare specific time points
- Works in print
- No technology requirements

---

## Network Maps

**Visualizing routes and connections**

**What are Network Maps?**

**Network maps** show connections between locations, visualizing relationships, routes, or flows in a network structure.

**Use Cases:**
- Transportation networks
- Communication networks
- Social networks (geographic)
- Supply chains
- Trade routes

**Basic Network Map:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create nodes (cities)
cities = gpd.GeoDataFrame({
    'city': ['NYC', 'LA', 'Chicago', 'Houston', 'Phoenix', 'Dallas'],
    'geometry': gpd.points_from_xy(
        [-74.0, -118.2, -87.6, -95.4, -112.1, -96.8],
        [40.7, 34.0, 41.9, 29.8, 33.4, 32.8]
    )
}, crs='EPSG:4326')

# Create edges (connections)
connections = [
    ('NYC', 'LA'), ('NYC', 'Chicago'), ('NYC', 'Dallas'),
    ('LA', 'Phoenix'), ('LA', 'Dallas'),
    ('Chicago', 'Houston'), ('Houston', 'Dallas')
]

# Load US for context
states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
us_states = states[states['iso_a3'] == 'USA']

# Plot
fig, ax = plt.subplots(figsize=(16, 10))

# Base map
us_states.plot(ax=ax, color='lightgray', edgecolor='white', linewidth=0.5)

# Draw connections
for origin_city, dest_city in connections:
    origin = cities[cities['city'] == origin_city].geometry.iloc[0]
    dest = cities[cities['city'] == dest_city].geometry.iloc[0]
    
    ax.plot([origin.x, dest.x], [origin.y, dest.y], 
           'b-', linewidth=2, alpha=0.5)

# Draw nodes
cities.plot(ax=ax, color='red', markersize=200, 
           edgecolor='black', linewidth=2, zorder=5)

# Labels
for idx, row in cities.iterrows():
    ax.annotate(row['city'], 
               xy=(row.geometry.x, row.geometry.y),
               xytext=(5, 5),
               textcoords='offset points',
               fontsize=11,
               fontweight='bold')

ax.set_title('Transportation Network', fontsize=16, fontweight='bold')
ax.axis('off')

plt.tight_layout()
plt.show()
```

**Weighted Network (Edge Thickness = Traffic):**

```python
# Add weights to connections
weighted_connections = pd.DataFrame({
    'origin': ['NYC', 'NYC', 'NYC', 'LA', 'LA', 'Chicago', 'Houston'],
    'dest': ['LA', 'Chicago', 'Dallas', 'Phoenix', 'Dallas', 'Houston', 'Dallas'],
    'traffic': [100, 80, 60, 50, 70, 40, 55]
})

fig, ax = plt.subplots(figsize=(16, 10))

us_states.plot(ax=ax, color='lightgray', edgecolor='white', linewidth=0.5)

# Draw weighted connections
for idx, row in weighted_connections.iterrows():
    origin = cities[cities['city'] == row['origin']].geometry.iloc[0]
    dest = cities[cities['city'] == row['dest']].geometry.iloc[0]
    
    ax.plot([origin.x, dest.x], [origin.y, dest.y], 
           'b-', linewidth=row['traffic']/10, alpha=0.6)

cities.plot(ax=ax, color='red', markersize=200, 
           edgecolor='black', linewidth=2, zorder=5)

ax.set_title('Weighted Network (Line Width = Traffic Volume)', 
            fontsize=16, fontweight='bold')
ax.axis('off')

plt.tight_layout()
plt.show()
```

**Network with folium (Interactive):**

```python
import folium

# Create map
m = folium.Map(location=[37, -95], zoom_start=4, tiles='CartoDB positron')

# Add edges
for idx, row in weighted_connections.iterrows():
    origin = cities[cities['city'] == row['origin']].geometry.iloc[0]
    dest = cities[cities['city'] == row['dest']].geometry.iloc[0]
    
    folium.PolyLine(
        locations=[[origin.y, origin.x], [dest.y, dest.x]],
        color='blue',
        weight=row['traffic']/10,
        opacity=0.7,
        popup=f"{row['origin']} → {row['dest']}: {row['traffic']}"
    ).add_to(m)

# Add nodes
for idx, row in cities.iterrows():
    folium.CircleMarker(
        location=[row.geometry.y, row.geometry.x],
        radius=8,
        popup=row['city'],
        color='red',
        fill=True,
        fillColor='red',
        fillOpacity=0.8
    ).add_to(m)

m.save('network_map.html')
```

**Best Practices:**

✅ Use node size to encode importance
✅ Use edge thickness to encode flow/weight
✅ Limit connections shown (show top N)
✅ Use curved lines to reduce overlap
✅ Add directionality when relevant

---

## Trajectory Maps

**Showing paths over time**

**What are Trajectory Maps?**

**Trajectory maps** show movement paths of objects/people over time, revealing patterns in spatial-temporal behavior.

**Use Cases:**
- Animal migration
- Hurricane tracks
- Vehicle routing
- Person movement
- Ship routes

**Single Trajectory:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate hurricane track
np.random.seed(42)
n_points = 20

lons = np.linspace(-80, -50, n_points) + np.random.randn(n_points) * 2
lats = np.linspace(25, 40, n_points) + np.random.randn(n_points) * 1
times = pd.date_range('2024-08-01', periods=n_points, freq='6H')
categories = np.clip(np.random.randint(1, 5, n_points), 1, 5)

track = pd.DataFrame({
    'lon': lons,
    'lat': lats,
    'time': times,
    'category': categories
})

# Plot
fig, ax = plt.subplots(figsize=(14, 10))

# Plot track
ax.plot(track['lon'], track['lat'], 'b-', linewidth=2, alpha=0.7)

# Plot points with category colors
scatter = ax.scatter(track['lon'], track['lat'], 
                    c=track['category'], 
                    s=100,
                    cmap='YlOrRd',
                    edgecolor='black',
                    linewidth=1,
                    zorder=5)

# Annotate start and end
ax.scatter(track['lon'].iloc[0], track['lat'].iloc[0], 
          s=300, marker='o', color='green', 
          edgecolor='black', linewidth=2, zorder=6, label='Start')
ax.scatter(track['lon'].iloc[-1], track['lat'].iloc[-1], 
          s=300, marker='X', color='red', 
          edgecolor='black', linewidth=2, zorder=6, label='End')

# Colorbar
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Hurricane Category', fontsize=11)

ax.set_title('Hurricane Track (August 2024)', fontsize=16, fontweight='bold')
ax.set_xlabel('Longitude', fontsize=12)
ax.set_ylabel('Latitude', fontsize=12)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**Multiple Trajectories:**

```python
# Generate multiple vehicle tracks
n_vehicles = 5
n_timesteps = 30

fig, ax = plt.subplots(figsize=(12, 10))

colors = plt.cm.tab10(np.linspace(0, 1, n_vehicles))

for i in range(n_vehicles):
    # Random walk
    np.random.seed(i)
    start_lon, start_lat = -95 + np.random.randn() * 5, 30 + np.random.randn() * 5
    
    lons = [start_lon]
    lats = [start_lat]
    
    for t in range(n_timesteps):
        lons.append(lons[-1] + np.random.randn() * 0.3)
        lats.append(lats[-1] + np.random.randn() * 0.3)
    
    ax.plot(lons, lats, color=colors[i], linewidth=2, 
           alpha=0.6, label=f'Vehicle {i+1}')
    ax.scatter(lons[0], lats[0], s=100, color=colors[i], 
              edgecolor='black', linewidth=2, zorder=5)

ax.set_title('Vehicle Trajectories', fontsize=16, fontweight='bold')
ax.set_xlabel('Longitude', fontsize=12)
ax.set_ylabel('Latitude', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

**Trajectory with Time Animation:**

```python
import plotly.graph_objects as go

# Create animated trajectory
fig = go.Figure()

# Add trajectory line
fig.add_trace(go.Scattergeo(
    lon=track['lon'],
    lat=track['lat'],
    mode='lines',
    line=dict(width=2, color='blue'),
    name='Track'
))

# Add animated point
frames = []
for i in range(len(track)):
    frames.append(go.Frame(
        data=[go.Scattergeo(
            lon=track['lon'][:i+1],
            lat=track['lat'][:i+1],
            mode='markers+lines',
            marker=dict(size=10, color='red'),
            line=dict(width=2, color='blue')
        )],
        name=str(i)
    ))

fig.frames = frames

fig.update_layout(
    title='Hurricane Track Animation',
    geo=dict(
        scope='usa',
        projection_type='albers usa',
        showland=True,
        landcolor='lightgray'
    ),
    updatemenus=[{
        'type': 'buttons',
        'showactive': False,
        'buttons': [
            {'label': 'Play', 'method': 'animate', 
             'args': [None, {'frame': {'duration': 500}}]},
            {'label': 'Pause', 'method': 'animate',
             'args': [[None], {'frame': {'duration': 0}, 'mode': 'immediate'}]}
        ]
    }]
)

fig.show()
```

**Best Practices:**

✅ Show direction (arrows or gradient)
✅ Mark start and end points
✅ Use color for attributes (category, speed, etc.)
✅ Consider time stamps on path
✅ Use animation for complex paths

---

## Composite Maps

**Layering multiple data types**

**What are Composite Maps?**

**Composite maps** combine multiple geographic layers (points, lines, polygons, rasters) to show complex spatial relationships.

**When to Use:**
- Show multiple related datasets
- Context + detail
- Multi-dimensional analysis

**Points + Polygons:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load states
states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
us_states = states[states['iso_a3'] == 'USA'].copy()

# Generate state values
np.random.seed(42)
us_states['unemployment'] = np.random.uniform(3, 8, len(us_states))

# Generate city points
cities = gpd.GeoDataFrame({
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'population': [8336000, 3979000, 2693000, 2320000],
    'geometry': gpd.points_from_xy(
        [-74.0, -118.2, -87.6, -95.4],
        [40.7, 34.0, 41.9, 29.8]
    )
}, crs='EPSG:4326')

# Create composite map
fig, ax = plt.subplots(figsize=(16, 10))

# Layer 1: Choropleth (unemployment)
us_states.plot(column='unemployment', cmap='YlOrRd', 
              legend=True, ax=ax, edgecolor='black', 
              linewidth=0.5, alpha=0.7)

# Layer 2: Proportional symbols (population)
cities.plot(ax=ax, markersize=cities['population']/10000,
           color='blue', alpha=0.7, edgecolor='white',
           linewidth=2, zorder=5)

# Layer 3: Labels
for idx, row in cities.iterrows():
    ax.annotate(row['city'], 
               xy=(row.geometry.x, row.geometry.y),
               xytext=(5, 5), textcoords='offset points',
               fontsize=10, fontweight='bold',
               bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

ax.set_title('Composite Map: Unemployment (choropleth) + Population (bubbles)',
            fontsize=16, fontweight='bold')
ax.axis('off')

plt.tight_layout()
plt.show()
```

**Multiple Layers with Different Geometries:**

```python
# Simulate highways (lines)
highway_coords = [
    [(-100, 30), (-95, 32), (-90, 33)],  # I-10
    [(-105, 40), (-100, 40), (-95, 40)],  # I-70
]

from shapely.geometry import LineString

highways = gpd.GeoDataFrame({
    'name': ['I-10', 'I-70'],
    'geometry': [LineString(coords) for coords in highway_coords]
}, crs='EPSG:4326')

# Create comprehensive composite
fig, ax = plt.subplots(figsize=(16, 10))

# Layer 1: States (choropleth)
us_states.plot(column='unemployment', cmap='YlOrRd', 
              legend=False, ax=ax, edgecolor='gray', 
              linewidth=0.5, alpha=0.5)

# Layer 2: Highways (lines)
highways.plot(ax=ax, color='darkred', linewidth=3, 
             linestyle='--', zorder=3, label='Highways')

# Layer 3: Cities (points)
cities.plot(ax=ax, markersize=200, color='navy', 
           edgecolor='white', linewidth=2, zorder=5, label='Cities')

ax.set_title('Multi-Layer Composite Map', fontsize=16, fontweight='bold')
ax.legend(fontsize=12, loc='lower left')
ax.axis('off')

plt.tight_layout()
plt.show()
```

**Interactive Composite with folium:**

```python
import folium
from folium import plugins

# Create base map
m = folium.Map(location=[37, -95], zoom_start=5, tiles='CartoDB positron')

# Layer 1: Choropleth
folium.Choropleth(
    geo_data=us_states,
    data=us_states,
    columns=['name', 'unemployment'],
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    fill_opacity=0.5,
    line_opacity=0.2,
    legend_name='Unemployment Rate (%)',
    name='Unemployment'
).add_to(m)

# Layer 2: City markers
for idx, row in cities.iterrows():
    folium.CircleMarker(
        location=[row.geometry.y, row.geometry.x],
        radius=row['population']/1000000 * 5,
        popup=f"{row['city']}: {row['population']:,}",
        color='blue',
        fill=True,
        fillColor='blue',
        fillOpacity=0.7
    ).add_to(m)

# Layer control
folium.LayerControl().add_to(m)

m.save('composite_interactive.html')
```

**Best Practices:**

✅ Use transparency for overlapping layers
✅ Control z-order (background to foreground)
✅ Limit total layer count (3-5 maximum)
✅ Use layer controls for interactive maps
✅ Ensure color schemes don't conflict

---

## Map Annotations

**Adding context with text, arrows, and highlights**

**Why Annotate Maps?**

**Annotations** add explanatory text, highlight important features, or guide the viewer's attention to specific areas.

**Text Annotations:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt

states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
us_states = states[states['iso_a3'] == 'USA'].copy()

fig, ax = plt.subplots(figsize=(16, 10))

us_states.plot(ax=ax, color='lightgray', edgecolor='black', linewidth=0.5)

# Annotate specific locations
annotations = [
    {'text': 'West Coast\nHigh Tech Hub', 'xy': (-120, 37), 
     'color': 'blue', 'size': 12},
    {'text': 'Midwest\nManufacturing Belt', 'xy': (-90, 42), 
     'color': 'green', 'size': 12},
    {'text': 'Sun Belt\nGrowing Population', 'xy': (-97, 32), 
     'color': 'orange', 'size': 12},
]

for annot in annotations:
    ax.annotate(annot['text'], 
               xy=annot['xy'],
               fontsize=annot['size'],
               fontweight='bold',
               color=annot['color'],
               ha='center',
               bbox=dict(boxstyle='round,pad=0.5', 
                        facecolor='white', 
                        edgecolor=annot['color'], 
                        linewidth=2))

ax.set_title('US Regions with Annotations', fontsize=16, fontweight='bold')
ax.axis('off')

plt.tight_layout()
plt.show()
```

**Arrows and Callouts:**

```python
fig, ax = plt.subplots(figsize=(14, 10))

us_states.plot(ax=ax, color='lightblue', edgecolor='black', linewidth=0.5)

# Arrow annotation pointing to specific area
ax.annotate('Hurricane Impact Zone', 
           xy=(-85, 30),  # Point to
           xytext=(-70, 35),  # Text location
           fontsize=13,
           fontweight='bold',
           color='red',
           arrowprops=dict(
               arrowstyle='->',
               color='red',
               lw=3,
               connectionstyle='arc3,rad=0.3'
           ),
           bbox=dict(boxstyle='round,pad=0.7', 
                    facecolor='yellow',
                    edgecolor='red',
                    linewidth=2))

ax.set_title('Map with Arrow Annotation', fontsize=16, fontweight='bold')
ax.axis('off')

plt.tight_layout()
plt.show()
```

**Highlighting Regions:**

```python
fig, ax = plt.subplots(figsize=(14, 10))

# Plot all states
us_states.plot(ax=ax, color='lightgray', edgecolor='black', linewidth=0.5)

# Highlight specific region
highlight_states = ['California', 'Oregon', 'Washington']  # West Coast
# Note: For naturalearth_lowres, use actual country names
# This is conceptual - adjust based on your data

# Add circle to highlight area
from matplotlib.patches import Circle
highlight = Circle((-120, 40), 5, color='red', fill=False, 
                  linewidth=3, linestyle='--', label='Focus Area')
ax.add_patch(highlight)

# Add text
ax.text(-120, 50, 'FOCUS REGION', fontsize=14, 
       fontweight='bold', color='red', ha='center')

ax.set_title('Highlighting Specific Regions', fontsize=16, fontweight='bold')
ax.legend(fontsize=12)
ax.axis('off')

plt.tight_layout()
plt.show()
```

**Scale Bar and North Arrow:**

```python
from matplotlib.patches import FancyArrowPatch, Rectangle
from matplotlib_scalebar.scalebar import ScaleBar

fig, ax = plt.subplots(figsize=(14, 10))

us_states.plot(ax=ax, color='lightgreen', edgecolor='black', linewidth=0.5)

# Add scale bar
scalebar = ScaleBar(111000, location='lower right')  # 111km per degree
ax.add_artist(scalebar)

# Add north arrow (manual)
arrow = FancyArrowPatch((-70, 45), (-70, 48),
                       arrowstyle='->', mutation_scale=30,
                       linewidth=3, color='black')
ax.add_patch(arrow)
ax.text(-70, 49, 'N', fontsize=16, fontweight='bold', ha='center')

ax.set_title('Map with Scale Bar and North Arrow', fontsize=16, fontweight='bold')
ax.axis('off')

plt.tight_layout()
plt.show()
```

**Best Practices:**

✅ Use annotations sparingly (only key points)
✅ Ensure text is readable (size, contrast)
✅ Use arrows to clearly point to features
✅ Box important text for visibility
✅ Include scale bar for reference maps

---

## Part 3 Summary

**You've mastered advanced geospatial techniques:**

**Movement & Flow:**
✅ Flow maps with proportional lines
✅ Sankey diagrams for geographic flows
✅ Animated maps for temporal patterns
✅ Trajectory visualization

**Analysis Techniques:**
✅ Spatial clustering (DBSCAN, K-means)
✅ Spatial autocorrelation (Moran's I, LISA)
✅ Hot spot analysis (Getis-Ord Gi*)
✅ Hexbin aggregation

**Advanced Visualizations:**
✅ Voronoi diagrams for territories
✅ Contour maps for continuous surfaces
✅ Cartograms for data-weighted geography
✅ Dot density maps

**Specialized Maps:**
✅ Proportional symbol maps
✅ Bivariate choropleths
✅ Small multiples for comparison
✅ Network and composite maps

**Key Takeaways:**

⚠️ **Avoid 3D** for data values (use 2D + color)
✅ **Hexagons > Squares** for spatial binning
✅ **Normalize by population/area** for rates
✅ **Small multiples > Animation** for comparison
✅ **Annotations add clarity** but use sparingly

**When to Use Each:**

| Technique | Best For | Avoid For |
|-----------|----------|-----------|
| Flow maps | Migration, trade routes | Static patterns |
| Animations | Temporal changes | Print, comparison |
| Clustering | Finding patterns | Prescribed regions |
| Hexbin | Point density | Individual points |
| Voronoi | Service areas | Weighted distances |
| Contours | Continuous surfaces | Discrete data |
| Cartograms | Emphasizing data | Geography recognition |
| Dot density | Distribution within regions | Aggregate totals |

**Next:** Part 4 - Real-World Applications & Best Practices

---
