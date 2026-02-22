# Class 6 – Mapping Tools & Techniques

[Part 1](Class6_Part1.md) | [Part 2](Class6_Part2.md) | [Part 3](Class6_Part3.md) | [Part 4](Class6_Part4.md)

---

# PART 2: MAPPING TOOLS & TECHNIQUES
# Slides 21-40
# ═══════════════════════════════════════════════════════════════

## Python Geospatial Stack

**Core libraries:**
- **geopandas**: Spatial data manipulation
- **folium**: Interactive web maps
- **plotly**: Dashboards
- **contextily**: Basemaps

**Install:**
```bash
pip install geopandas folium plotly contextily
```

---

## geopandas Basics

```python
import geopandas as gpd

# Read data
gdf = gpd.read_file('file.shp')

# Basic operations
gdf.plot()
gdf.to_crs('EPSG:4326')
gdf.to_file('output.geojson', driver='GeoJSON')
```

---

## Creating Your First Map

```python
import geopandas as gpd
import matplotlib.pyplot as plt

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world.plot(figsize=(15, 10))
plt.title('World Map')
plt.axis('off')
plt.show()
```

---

## Choropleth with geopandas

```python
# Color by population
world.plot(column='pop_est', cmap='OrRd', legend=True, figsize=(15, 10))
plt.title('World Population')
plt.axis('off')
plt.show()
```

---

## folium Interactive Maps

```python
import folium

# Create base map
m = folium.Map(location=[40.7, -74.0], zoom_start=10)

# Add marker
folium.Marker([40.7, -74.0], popup='NYC').add_to(m)

# Save
m.save('map.html')
```

---

## plotly Maps

```python
import plotly.express as px

fig = px.choropleth(df, locations='state', locationmode='USA-states',
                   color='value', scope='usa')
fig.show()
```

---

## Adding Basemaps

```python
import contextily as ctx

ax = gdf.plot(figsize=(10, 10), alpha=0.5)
ctx.add_basemap(ax, crs=gdf.crs, source=ctx.providers.OpenStreetMap.Mapnik)
plt.show()
```

---

## Combining Layers

```python
fig, ax = plt.subplots(figsize=(15, 10))

# Base layer (states)
states.plot(ax=ax, color='lightgray', edgecolor='black')

# Points layer (cities)
cities.plot(ax=ax, color='red', markersize=50)

plt.title('Multi-Layer Map')
plt.show()
```

---

## Map Export

```python
# Save as image
plt.savefig('map.png', dpi=300, bbox_inches='tight')

# Save interactive as HTML
m.save('interactive_map.html')

# Save data
gdf.to_file('output.geojson', driver='GeoJSON')
```

---

## Part 2 Summary

✅ geopandas for static maps
✅ folium for interactive
✅ plotly for dashboards
✅ Multi-layer visualizations
✅ Export in multiple formats

---
