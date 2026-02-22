# Class 6 – Mapping Tools & Techniques

[Part 1](Class6_Part1.md) | [Part 2](Class6_Part2.md) | [Part 3](Class6_Part3.md) | [Part 4](Class6_Part4.md)

---

# PART 2: MAPPING TOOLS & TECHNIQUES
# Slides 21-40
# ═══════════════════════════════════════════════════════════════

## Python Geospatial Stack

**The complete Python ecosystem for geographic visualization**

**Core Libraries:**

**1. geopandas** - Spatial DataFrames
- Extends pandas with geographic operations
- Read/write shapefiles, GeoJSON, etc.
- Spatial joins, buffers, intersections
- Integration with matplotlib

**2. folium** - Interactive Web Maps
- Built on Leaflet.js
- Create slippy maps with Python
- Markers, popups, choropleth
- Export to HTML

**3. plotly** - Interactive Dashboards
- Express API for quick maps
- Graph Objects for advanced control
- Choropleth, scatter_mapbox, density_mapbox
- Integrated with Dash for dashboards

**4. contextily** - Basemap Tiles
- Add context to static maps
- OpenStreetMap, Stamen, CartoDB tiles
- Automatic tile fetching and stitching

**5. Supporting Libraries:**
- **shapely** - Geometric operations (installed with geopandas)
- **pyproj** - Coordinate transformations
- **geopy** - Geocoding services
- **rasterio** - Raster data (if needed)

**Installation:**

```bash
# Core stack
pip install geopandas folium plotly contextily

# Optional but recommended
pip install geopy mapclassify
```

**Import Convention:**

```python
import geopandas as gpd
import folium
import plotly.express as px
import plotly.graph_objects as go
import contextily as ctx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
```

**When to Use Each:**

| Library | Use Case | Output |
|---------|----------|--------|
| **geopandas** | Static maps, analysis | PNG, PDF |
| **folium** | Interactive web maps | HTML |
| **plotly** | Dashboards, presentations | HTML, interactive |
| **contextily** | Add basemaps to static | With geopandas |

---

## geopandas Basics

**geopandas extends pandas with spatial capabilities**

**What is a GeoDataFrame?**

A **GeoDataFrame** is like a pandas DataFrame with a special `geometry` column containing spatial objects (points, lines, polygons).

**Loading Geographic Data:**

```python
import geopandas as gpd

# Read shapefile
states = gpd.read_file('states.shp')

# Read GeoJSON
cities = gpd.read_file('cities.geojson')

# Read from URL
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Read from PostGIS database
gdf = gpd.read_postgis("SELECT * FROM table", connection)
```

**Exploring GeoDataFrame:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt

# Load sample data
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Inspect
print(world.head())
print(world.shape)  # (177, 6) - 177 countries
print(world.columns)
# Index(['pop_est', 'continent', 'name', 'iso_a3', 'gdp_md_est', 'geometry'], dtype='object')

# Check geometry types
print(world.geometry.type.unique())
# ['MultiPolygon' 'Polygon']

# Check CRS (Coordinate Reference System)
print(world.crs)
# EPSG:4326 (WGS84 - lat/lon)

# Get bounds
print(world.total_bounds)
# [minx, miny, maxx, maxy]

# Summary statistics
print(world.describe())
```

**Basic Operations:**

```python
# Filter data
usa = world[world['name'] == 'United States of America']

# Select columns
world_simple = world[['name', 'pop_est', 'geometry']]

# Sort by attribute
world_sorted = world.sort_values('pop_est', ascending=False)

# Calculate area (in CRS units)
world['area_km2'] = world.geometry.area / 1_000_000  # If in meters

# Calculate centroid
world['centroid'] = world.geometry.centroid

# Buffer (expand geometry)
world['buffered'] = world.geometry.buffer(1)  # 1 degree buffer
```

**Coordinate Reference System (CRS) Operations:**

```python
# Check current CRS
print(world.crs)  # EPSG:4326

# Transform to different CRS
world_mercator = world.to_crs('EPSG:3857')  # Web Mercator
world_albers = world.to_crs('EPSG:5070')    # US Albers Equal Area

# Set CRS (if missing)
world = world.set_crs('EPSG:4326')
```

**Writing Data:**

```python
# Save as shapefile
world.to_file('world.shp')

# Save as GeoJSON
world.to_file('world.geojson', driver='GeoJSON')

# Save as GeoPackage (modern alternative to shapefile)
world.to_file('world.gpkg', driver='GPKG')
```

**Key Takeaway:** geopandas combines the power of pandas (data manipulation) with spatial operations, making it the foundation of Python geospatial analysis.

---

## Creating Your First Map

**Simple static maps with geopandas**

**Basic World Map:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt

# Load world data
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Create simple map
fig, ax = plt.subplots(figsize=(15, 10))
world.plot(ax=ax, color='lightblue', edgecolor='black', linewidth=0.5)

ax.set_title('World Map', fontsize=18, fontweight='bold')
ax.set_xlabel('Longitude', fontsize=12)
ax.set_ylabel('Latitude', fontsize=12)

plt.tight_layout()
plt.show()
```

**Filter and Focus on Region:**

```python
# Focus on Europe
europe = world[world['continent'] == 'Europe']

fig, ax = plt.subplots(figsize=(12, 10))
europe.plot(ax=ax, color='lightgreen', edgecolor='darkgreen', linewidth=0.8)

ax.set_title('Europe', fontsize=16, fontweight='bold')
ax.set_xlim([-25, 45])
ax.set_ylim([35, 72])
ax.axis('off')  # Hide axes for cleaner look

plt.tight_layout()
plt.show()
```

**Styling Options:**

```python
# Different styles
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Simple
world.plot(ax=axes[0,0], color='lightblue', edgecolor='black')
axes[0,0].set_title('Simple Style')
axes[0,0].axis('off')

# No borders
world.plot(ax=axes[0,1], color='coral', edgecolor='none')
axes[0,1].set_title('No Borders')
axes[0,1].axis('off')

# Thick borders
world.plot(ax=axes[1,0], color='wheat', edgecolor='brown', linewidth=2)
axes[1,0].set_title('Thick Borders')
axes[1,0].axis('off')

# Transparent fill
world.plot(ax=axes[1,1], facecolor='none', edgecolor='navy', linewidth=0.5)
axes[1,1].set_title('Outline Only')
axes[1,1].axis('off')

plt.tight_layout()
plt.show()
```

**Best Practices:**

✅ Use `figsize` for proper proportions
✅ Use `axis('off')` for cleaner maps
✅ Match colors to purpose (subdued for background)
✅ Set appropriate bounds with `set_xlim()` and `set_ylim()`

---

## Choropleth with geopandas

**Creating data-driven choropleth maps**

**Basic Choropleth:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt

# Load data
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Create choropleth by population
fig, ax = plt.subplots(figsize=(16, 10))

world.plot(column='pop_est',           # Column to visualize
          cmap='YlOrRd',               # Color scheme
          legend=True,                  # Show legend
          legend_kwds={'label': 'Population',
                      'orientation': 'horizontal',
                      'shrink': 0.8},
          edgecolor='black',
          linewidth=0.3,
          ax=ax)

ax.set_title('World Population Choropleth', fontsize=18, fontweight='bold')
ax.axis('off')

plt.tight_layout()
plt.show()
```

**Using Classification Schemes:**

```python
# Install mapclassify for classification schemes
# pip install mapclassify

import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(18, 14))

schemes = ['quantiles', 'equal_interval', 'natural_breaks', 'fisher_jenks']
titles = ['Quantiles (5)', 'Equal Interval (5)', 'Natural Breaks (5)', 'Fisher-Jenks (5)']

for ax, scheme, title in zip(axes.flat, schemes, titles):
    world.plot(column='pop_est',
              scheme=scheme,
              k=5,  # Number of classes
              cmap='YlOrRd',
              legend=True,
              edgecolor='black',
              linewidth=0.3,
              ax=ax)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.axis('off')

plt.suptitle('Classification Schemes Comparison', fontsize=16, fontweight='bold', y=0.98)
plt.tight_layout()
plt.show()
```

**Custom Color Schemes:**

```python
# Using different color maps
fig, axes = plt.subplots(2, 3, figsize=(20, 12))

cmaps = ['YlOrRd', 'Blues', 'Greens', 'viridis', 'plasma', 'RdYlGn']

for ax, cmap in zip(axes.flat, cmaps):
    world.plot(column='gdp_md_est',
              cmap=cmap,
              legend=False,
              edgecolor='black',
              linewidth=0.3,
              ax=ax)
    ax.set_title(f'Colormap: {cmap}', fontsize=12)
    ax.axis('off')

plt.suptitle('GDP by Country - Different Color Schemes', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

**Diverging Choropleth (for +/- data):**

```python
import numpy as np

# Create example data with positive and negative values
world['gdp_growth'] = np.random.randn(len(world)) * 3  # Simulated % growth

# Find center point
vmin, vmax = world['gdp_growth'].min(), world['gdp_growth'].max()

fig, ax = plt.subplots(figsize=(16, 10))

world.plot(column='gdp_growth',
          cmap='RdBu',  # Red-Blue diverging
          legend=True,
          legend_kwds={'label': 'GDP Growth (%)', 'orientation': 'horizontal'},
          edgecolor='black',
          linewidth=0.3,
          vmin=vmin,
          vmax=vmax,
          ax=ax)

ax.set_title('GDP Growth Rate (Simulated)', fontsize=18, fontweight='bold')
ax.axis('off')

plt.tight_layout()
plt.show()
```

**Key Parameters:**

- `column`: Data column to visualize
- `cmap`: Color scheme ('YlOrRd', 'Blues', 'RdBu', etc.)
- `scheme`: Classification method ('quantiles', 'equal_interval', etc.)
- `k`: Number of classes
- `legend`: Show legend (True/False)
- `edgecolor`: Border color
- `linewidth`: Border width

---

## Custom Color Schemes

**Choosing the right colors for your maps**

**ColorBrewer Integration:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Sequential color schemes (light to dark)
sequential = ['YlOrRd', 'YlGnBu', 'PuBuGn', 'BuPu', 'OrRd']

fig, axes = plt.subplots(2, 3, figsize=(18, 12))

for ax, cmap in zip(axes.flat[:5], sequential):
    world.plot(column='pop_est',
              cmap=cmap,
              legend=False,
              edgecolor='gray',
              linewidth=0.2,
              ax=ax)
    ax.set_title(f'{cmap}', fontsize=12, fontweight='bold')
    ax.axis('off')

# Hide last subplot
axes.flat[5].axis('off')

plt.suptitle('Sequential Color Schemes for Choropleth Maps', 
            fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

**Custom Discrete Colors:**

```python
# Create custom discrete color map
from matplotlib.colors import ListedColormap

colors = ['#f7fbff', '#deebf7', '#c6dbef', '#9ecae1', '#6baed6', 
          '#4292c6', '#2171b5', '#08519c', '#08306b']
n_bins = len(colors)

custom_cmap = ListedColormap(colors)

fig, ax = plt.subplots(figsize=(16, 10))

world.plot(column='pop_est',
          cmap=custom_cmap,
          scheme='quantiles',
          k=n_bins,
          legend=True,
          edgecolor='black',
          linewidth=0.3,
          ax=ax)

ax.set_title('Population with Custom Color Palette', fontsize=16, fontweight='bold')
ax.axis('off')
plt.tight_layout()
plt.show()
```

**Perceptually Uniform Colors:**

```python
# Modern perceptually uniform color maps
modern_cmaps = ['viridis', 'plasma', 'inferno', 'cividis']

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

for ax, cmap in zip(axes.flat, modern_cmaps):
    world.plot(column='gdp_md_est',
              cmap=cmap,
              legend=True,
              legend_kwds={'shrink': 0.6},
              edgecolor='white',
              linewidth=0.3,
              ax=ax)
    ax.set_title(f'{cmap.capitalize()}', fontsize=13, fontweight='bold')
    ax.axis('off')

plt.suptitle('Perceptually Uniform Color Schemes', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

**Color-Blind Safe Palettes:**

```python
# Color-blind friendly schemes
cb_safe = ['YlOrBr', 'PuBu', 'BuPu']

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

for ax, cmap in zip(axes.flat, cb_safe):
    world.plot(column='pop_est',
              cmap=cmap,
              legend=False,
              edgecolor='black',
              linewidth=0.3,
              ax=ax)
    ax.set_title(f'{cmap} (Color-blind Safe)', fontsize=12, fontweight='bold')
    ax.axis('off')

plt.tight_layout()
plt.show()
```

**Best Practices:**

✅ **Sequential** for continuous data (0 to high)
✅ **Diverging** for data with meaningful center (profit/loss, anomalies)
✅ **Avoid rainbow** (perceptually non-uniform, not color-blind safe)
✅ **Test color-blindness** using colorbrewer2.org
✅ **Limit classes** to 5-7 for choropleth

---

## Adding Basemaps

**Add geographic context with tile layers**

**Using contextily:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
import numpy as np

# Create sample point data (Texas cities example)
cities = gpd.GeoDataFrame({
    'name': ['Dallas', 'Houston', 'Austin', 'San Antonio', 'Fort Worth'],
    'population': [1343573, 2320268, 978908, 1547253, 909585],
    'geometry': gpd.points_from_xy(
        [-96.7970, -95.3698, -97.7431, -98.4936, -97.3308],  # lon
        [32.7767, 29.7604, 30.2672, 29.4241, 32.7555]        # lat
    )
}, crs='EPSG:4326')

# Transform to Web Mercator (required for contextily)
cities_web = cities.to_crs('EPSG:3857')

# Create map with basemap
fig, ax = plt.subplots(figsize=(12, 10))

# Plot cities
cities_web.plot(ax=ax,
               markersize=cities_web['population']/5000,
               color='red',
               alpha=0.7,
               edgecolor='darkred',
               linewidth=1.5,
               zorder=2)  # Ensure points on top

# Add basemap
ctx.add_basemap(ax, 
               source=ctx.providers.OpenStreetMap.Mapnik,
               zoom=8)

ax.set_title('Texas Cities with OpenStreetMap Basemap', 
            fontsize=16, fontweight='bold')
ax.axis('off')

plt.tight_layout()
plt.show()
```

**Different Basemap Providers:**

```python
# Compare different basemap styles
fig, axes = plt.subplots(2, 2, figsize=(16, 14))

basemaps = [
    (ctx.providers.OpenStreetMap.Mapnik, 'OpenStreetMap'),
    (ctx.providers.CartoDB.Positron, 'CartoDB Positron (Light)'),
    (ctx.providers.CartoDB.DarkMatter, 'CartoDB DarkMatter'),
    (ctx.providers.Stamen.Terrain, 'Stamen Terrain')
]

for ax, (provider, name) in zip(axes.flat, basemaps):
    cities_web.plot(ax=ax,
                   markersize=100,
                   color='red',
                   alpha=0.8,
                   edgecolor='white',
                   linewidth=1,
                   zorder=2)
    
    ctx.add_basemap(ax, source=provider, zoom=7)
    ax.set_title(name, fontsize=13, fontweight='bold')
    ax.axis('off')

plt.suptitle('Basemap Style Comparison', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```

**Basemap with Polygons:**

```python
# Load US states
states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
us_states = states[states['iso_a3'] == 'USA'].copy()
us_states_web = us_states.to_crs('EPSG:3857')

fig, ax = plt.subplots(figsize=(15, 10))

# Plot states with transparency
us_states_web.plot(ax=ax,
                  facecolor='none',
                  edgecolor='red',
                  linewidth=2,
                  alpha=0.8,
                  zorder=2)

# Add basemap
ctx.add_basemap(ax, 
               source=ctx.providers.CartoDB.Positron,
               zoom=4)

ax.set_title('US States Overlay on Basemap', fontsize=16, fontweight='bold')
ax.axis('off')

plt.tight_layout()
plt.show()
```

**Important Notes:**

⚠️ **Must convert to EPSG:3857 (Web Mercator)** before adding basemap
⚠️ Internet connection required (downloads tiles)
✅ Use `zoom` parameter to control tile resolution
✅ Use `zorder` to control layer order (higher = on top)

---

## folium Introduction

**Creating interactive web maps with Python**

**What is folium?**

**folium** builds on Leaflet.js to create interactive maps that can be saved as HTML and viewed in any browser.

**Basic Map:**

```python
import folium

# Create base map centered on New York
m = folium.Map(location=[40.7128, -74.0060], 
              zoom_start=12,
              tiles='OpenStreetMap')

# Save to HTML
m.save('nyc_map.html')

# In Jupyter: display directly
m
```

**Map Tiles (Basemap Styles):**

```python
# Different tile providers
tile_providers = [
    'OpenStreetMap',
    'Stamen Terrain',
    'Stamen Toner',
    'Stamen Watercolor',
    'CartoDB positron',
    'CartoDB dark_matter'
]

# Create map with specific tiles
m = folium.Map(location=[37.7749, -122.4194],  # San Francisco
              zoom_start=12,
              tiles='Stamen Watercolor')

m.save('sf_watercolor.html')
```

**Control Options:**

```python
# Map with custom controls
m = folium.Map(
    location=[34.0522, -118.2437],  # Los Angeles
    zoom_start=10,
    tiles='OpenStreetMap',
    control_scale=True,              # Add scale bar
    zoom_control=True,               # Zoom buttons
    scrollWheelZoom=True,            # Scroll to zoom
    dragging=True,                   # Drag to pan
    max_zoom=18,
    min_zoom=5
)

# Add layer control
folium.TileLayer('CartoDB positron', name='Light Map').add_to(m)
folium.TileLayer('CartoDB dark_matter', name='Dark Map').add_to(m)
folium.LayerControl().add_to(m)

m.save('la_map_controls.html')
```

**Key Features:**

✅ Interactive (pan, zoom, click)
✅ Multiple basemap options
✅ Markers, popups, tooltips
✅ Choropleth layers
✅ Export to HTML (self-contained)

---

## folium Choropleth

**Interactive colored regions**

**Basic Choropleth:**

```python
import folium
import geopandas as gpd
import json

# Load data
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Convert to GeoJSON (folium requirement)
world_json = world.to_json()

# Create base map
m = folium.Map(location=[20, 0], zoom_start=2, tiles='CartoDB positron')

# Add choropleth
folium.Choropleth(
    geo_data=world_json,
    name='Population',
    data=world,
    columns=['name', 'pop_est'],
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Population'
).add_to(m)

folium.LayerControl().add_to(m)

m.save('world_population_choropleth.html')
```

**With Pandas DataFrame:**

```python
import folium
import pandas as pd
import geopandas as gpd

# Load US states
us_states = gpd.read_file('https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/us-states.json')

# Create sample data
state_data = pd.DataFrame({
    'state': ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania'],
    'unemployment': [5.3, 4.8, 4.5, 5.1, 5.6]
})

# Create map
m = folium.Map(location=[37.8, -96], zoom_start=4, tiles='CartoDB positron')

folium.Choropleth(
    geo_data=us_states,
    name='choropleth',
    data=state_data,
    columns=['state', 'unemployment'],
    key_on='feature.properties.name',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name='Unemployment Rate (%)',
    nan_fill_color='lightgray'
).add_to(m)

folium.LayerControl().add_to(m)
m.save('us_unemployment.html')
```

**Interactive with Tooltips:**

```python
import folium
import geopandas as gpd

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

m = folium.Map(location=[20, 0], zoom_start=2)

# Add GeoJson with tooltip
folium.GeoJson(
    world,
    name='countries',
    tooltip=folium.GeoJsonTooltip(
        fields=['name', 'pop_est', 'gdp_md_est'],
        aliases=['Country', 'Population', 'GDP (millions)'],
        localize=True
    ),
    style_function=lambda x: {
        'fillColor': 'lightblue',
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.6
    },
    highlight_function=lambda x: {
        'fillColor': 'darkblue',
        'fillOpacity': 0.8
    }
).add_to(m)

m.save('world_interactive_tooltip.html')
```

---

## folium Markers and Popups

**Adding interactive point features**

**Simple Markers:**

```python
import folium

# Create map
m = folium.Map(location=[40.7128, -74.0060], zoom_start=13)

# Add marker
folium.Marker(
    location=[40.7128, -74.0060],
    popup='New York City',
    tooltip='Click for more info',
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)

m.save('nyc_marker.html')
```

**Multiple Markers:**

```python
import folium
import pandas as pd

# Sample store data
stores = pd.DataFrame({
    'name': ['Store A', 'Store B', 'Store C', 'Store D'],
    'lat': [40.7128, 40.7580, 40.7489, 40.7614],
    'lon': [-74.0060, -73.9855, -73.9680, -73.9776],
    'sales': [125000, 98000, 156000, 87000]
})

# Create map
m = folium.Map(location=[40.7489, -73.9680], zoom_start=13)

# Add markers for each store
for idx, row in stores.iterrows():
    folium.Marker(
        location=[row['lat'], row['lon']],
        popup=f"<b>{row['name']}</b><br>Sales: ${row['sales']:,}",
        tooltip=row['name'],
        icon=folium.Icon(
            color='green' if row['sales'] > 100000 else 'orange',
            icon='shopping-cart',
            prefix='fa'
        )
    ).add_to(m)

m.save('stores_map.html')
```

**Custom Icons:**

```python
import folium

m = folium.Map(location=[34.0522, -118.2437], zoom_start=12)

# Different icon styles
icons = [
    ('red', 'cloud'),
    ('blue', 'star'),
    ('green', 'leaf'),
    ('purple', 'heart'),
    ('orange', 'fire')
]

lats = [34.0522, 34.0622, 34.0422, 34.0522, 34.0722]
lons = [-118.2437, -118.2537, -118.2337, -118.2237, -118.2637]

for (color, icon_name), lat, lon in zip(icons, lats, lons):
    folium.Marker(
        location=[lat, lon],
        popup=f'{color} {icon_name}',
        icon=folium.Icon(color=color, icon=icon_name)
    ).add_to(m)

m.save('custom_icons.html')
```

**Circle Markers (Better for many points):**

```python
import folium
import numpy as np

# Generate random points
np.random.seed(42)
n_points = 50
lats = np.random.uniform(40.70, 40.80, n_points)
lons = np.random.uniform(-74.02, -73.92, n_points)
values = np.random.randint(10, 100, n_points)

m = folium.Map(location=[40.75, -73.97], zoom_start=12)

for lat, lon, val in zip(lats, lons, values):
    folium.CircleMarker(
        location=[lat, lon],
        radius=val/10,  # Size based on value
        popup=f'Value: {val}',
        color='red',
        fill=True,
        fillColor='red',
        fillOpacity=0.6
    ).add_to(m)

m.save('circle_markers.html')
```

---

## Marker Clustering

**Handle thousands of markers efficiently**

**Using MarkerCluster:**

```python
import folium
from folium.plugins import MarkerCluster
import numpy as np

# Generate many random points
np.random.seed(42)
n_points = 1000
lats = np.random.uniform(25, 48, n_points)
lons = np.random.uniform(-125, -65, n_points)

# Create map
m = folium.Map(location=[37, -95], zoom_start=5)

# Create marker cluster
marker_cluster = MarkerCluster().add_to(m)

# Add markers to cluster
for lat, lon in zip(lats, lons):
    folium.Marker(
        location=[lat, lon],
        popup=f'Point at ({lat:.2f}, {lon:.2f})'
    ).add_to(marker_cluster)

m.save('clustered_markers.html')
```

**Custom Cluster Icons:**

```python
from folium.plugins import MarkerCluster
import folium

m = folium.Map(location=[37, -95], zoom_start=5)

# Custom cluster options
marker_cluster = MarkerCluster(
    options={
        'maxClusterRadius': 50,
        'disableClusteringAtZoom': 10,
        'spiderfyOnMaxZoom': True
    }
).add_to(m)

# Add clustered data
for lat, lon in zip(lats[:500], lons[:500]):
    folium.Marker([lat, lon]).add_to(marker_cluster)

m.save('custom_cluster.html')
```

**Key Benefits:**

✅ Performance with 1000s of points
✅ Auto-aggregation at different zoom levels
✅ Click to "spiderfy" overlapping markers
✅ Numbers show cluster size

---

## Part 2 Summary

**You've mastered Python mapping tools:**

**Core Libraries:**
✅ **geopandas** - Spatial data manipulation and static maps
✅ **folium** - Interactive web maps with Leaflet.js
✅ **plotly** - Dashboard-ready interactive visualizations
✅ **contextily** - Basemap integration

**Key Skills:**
✅ Loading and exploring geographic data
✅ Creating choropleth maps with multiple classification schemes
✅ Choosing appropriate color schemes
✅ Adding basemaps for context
✅ Building interactive maps with markers and popups
✅ Clustering markers for performance
✅ Exporting maps in multiple formats

**Best Practices:**
✅ Match CRS before spatial operations
✅ Transform to EPSG:3857 for web tiles
✅ Use sequential colors for continuous data
✅ Limit choropleth classes to 5-7
✅ Add interactivity when sharing with non-technical users
✅ Test maps at different zoom levels

**Next:** Part 3 - Advanced Geospatial Techniques (Flow maps, animations, clustering, and more!)

---
