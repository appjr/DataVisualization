# Class 6 – Geographic Data Fundamentals

[Part 1](Class6_Part1.md) | [Part 2](Class6_Part2.md) | [Part 3](Class6_Part3.md) | [Part 4](Class6_Part4.md)

---

# PART 1: GEOGRAPHIC DATA FUNDAMENTALS
# Slides 1-20
# ═══════════════════════════════════════════════════════════════

# Class 6 – Data Visualization
## Geospatial & Geographic Visualization
## Maps, Spatial Patterns, and Location Intelligence

**MIS 6380 - Data Visualization**  
**Spring 2026**

---

## Learning Objectives

**By the end of this class, you will be able to:**

**Foundational Knowledge:**
- ✅ Understand types of geographic data (points, polygons, rasters)
- ✅ Recognize appropriate map types for different data
- ✅ Choose proper coordinate systems and projections

**Technical Skills:**
- ✅ Create choropleth maps with geopandas
- ✅ Build interactive maps with folium and plotly
- ✅ Visualize spatial patterns and clusters
- ✅ Combine geographic and temporal data

**Analytical Abilities:**
- ✅ Identify spatial patterns and correlations
- ✅ Avoid common geographic visualization pitfalls
- ✅ Select appropriate color schemes for maps
- ✅ Communicate location-based insights

**Practical Applications:**
- ✅ Sales territory analysis
- ✅ Demographic visualization
- ✅ Store location planning
- ✅ Geographic dashboards

**Prerequisites**: Classes 3-5 (Visual perception, EDA, Python, Time Series)

---

## Why Geographic Visualization Matters

**Location data is everywhere in business and science:**

**Business Applications:**
- 📍 Sales territory performance
- 🏪 Store location analysis
- 🚚 Supply chain optimization
- 🏘️ Market demographics
- 🌍 Global expansion planning

**Public Health:**
- 🦠 Disease outbreak tracking
- 🏥 Hospital coverage areas
- 💉 Vaccination rate mapping
- 🚑 Emergency response planning

**Real Estate:**
- 🏠 Property value mapping
- 📊 Neighborhood analysis
- 🏗️ Development planning
- 🌳 Amenity proximity

**Transportation:**
- 🚗 Traffic flow visualization
- ✈️ Route optimization
- 🚇 Transit coverage
- 🅿️ Parking utilization

**Environmental:**
- 🌡️ Climate patterns
- 🌊 Flood risk zones
- 🌲 Deforestation tracking
- 🏭 Pollution monitoring

**Key Insight:** 80%+ of business data has a geographic component. Maps make patterns visible that tables cannot show.

---

## Types of Geographic Data

**Understanding your spatial data type guides visualization choice**

**1. Point Data (Discrete Locations)**

**Definition:** Individual locations with lat/lon coordinates

**Examples:**
- Store locations
- Customer addresses
- Disease cases
- Earthquake epicenters
- Cell towers

**Attributes:** Can attach data (sales, demographics, etc.)

**Visualizations:**
- Scatter on map
- Bubble map (size = value)
- Heat map (density)
- Clustering

**2. Line Data (Routes/Boundaries)**

**Definition:** Connected sequences of points

**Examples:**
- Roads and highways
- Rivers and streams
- Flight paths
- Delivery routes
- Transit lines

**Visualizations:**
- Path/route maps
- Flow maps (width = volume)
- Network diagrams

**3. Polygon Data (Areas/Regions)**

**Definition:** Enclosed boundaries defining regions

**Examples:**
- Countries, states, counties
- ZIP codes
- Sales territories
- School districts
- Climate zones

**Visualizations:**
- Choropleth maps (color = value)
- Cartograms (size = value)
- Boundary maps

**4. Raster Data (Grid Surfaces)**

**Definition:** Continuous surfaces on regular grids

**Examples:**
- Satellite imagery
- Elevation (DEMs)
- Temperature surfaces
- Land cover
- Precipitation

**Visualizations:**
- Heat maps
- Contour maps
- 3D surfaces

---

## Map Projections Fundamentals

**All maps distort reality - understanding how matters**

**The Problem:** Earth is 3D (sphere), maps are 2D (flat)

**Tradeoffs:** Cannot preserve all of:
- ❌ Shape
- ❌ Area
- ❌ Distance
- ❌ Direction

**Common Projections:**

| Projection | Preserves | Distorts | Best For |
|------------|-----------|----------|----------|
| **Mercator** | Shape | Area (high lat) | Navigation |
| **Robinson** | Balance | All slightly | World maps |
| **Albers Equal-Area** | Area | Shape | Choropleth |
| **Web Mercator** | Web display | Area | Web maps |

---

## Choropleth Maps

**Choropleth maps use color to show values across regions**

**When to Use:**
- Data aggregated to regions (states, counties)
- Comparing across areas
- Showing spatial patterns

**Example:** Sales by state, unemployment by county

**Best Practices:**
- Use sequential colors for continuous data
- Use diverging colors for +/- data
- Include legend
- Consider population normalization

---

## Basic Map Types: Choropleth Maps

**Choropleth maps are the most common geographic visualization**

**What is a Choropleth Map?**

A **choropleth map** uses color to represent data values across geographic regions (counties, states, countries).

**When to Use:**
- Data aggregated to administrative boundaries
- Comparing rates/ratios across regions
- Showing spatial patterns of continuous variables

**Basic Example:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load US states shapefile (example)
# In practice: geopandas.datasets or download from census.gov
states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
us_states = states[states['continent'] == 'North America'].copy()

# Generate sample data (sales by state)
np.random.seed(42)
us_states['Sales'] = np.random.randint(1000, 10000, len(us_states))

# Create choropleth
fig, ax = plt.subplots(figsize=(15, 10))

us_states.plot(column='Sales',
              cmap='YlOrRd',  # Yellow-Orange-Red color scheme
              legend=True,
              legend_kwds={'label': 'Sales ($)', 'orientation': 'horizontal'},
              edgecolor='black',
              linewidth=0.5,
              ax=ax)

ax.set_title('Sales by Region (Choropleth Map)', fontsize=16, fontweight='bold')
ax.axis('off')  # Hide axes for cleaner look

plt.tight_layout()
plt.show()
```

**Color Scheme Selection:**

- **Sequential** (light to dark): For continuous data (0 to high)
- **Diverging** (red-white-blue): For data with meaningful midpoint (profit/loss)
- **Categorical** (distinct colors): For categories (NOT for choropleth!)

**Common Mistakes:**

❌ Using population totals (shows population, not rate)  
❌ Rainbow colors (hard to interpret)  
❌ Too many color bins (confusing)  
✅ Use rates/percentages when appropriate  
✅ Sequential or diverging color schemes  
✅ 5-7 color bins maximum

---

## Symbol/Bubble Maps

**Symbol maps use size/shape to encode values at point locations**

**What are Symbol Maps?**

**Symbol maps** place markers (circles, squares, icons) at geographic coordinates, with size representing data values.

**When to Use:**
- Point data (specific locations)
- Want to show both location AND magnitude
- Absolute counts (not rates)

**Example:** Store sales, earthquake magnitudes

**Basic Example:**

```python
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate sample store locations
np.random.seed(42)
n_stores = 50

store_data = pd.DataFrame({
    'Store_ID': range(1, n_stores+1),
    'Longitude': np.random.uniform(-120, -70, n_stores),  # US range
    'Latitude': np.random.uniform(25, 50, n_stores),
    'Sales': np.random.randint(100, 5000, n_stores)
})

# Convert to GeoDataFrame
geometry = gpd.points_from_xy(store_data.Longitude, store_data.Latitude)
gdf_stores = gpd.GeoDataFrame(store_data, geometry=geometry)

# Create bubble map
fig, ax = plt.subplots(figsize=(15, 10))

# Load base map (states for context)
states.plot(ax=ax, color='lightgray', edgecolor='white', linewidth=0.5)

# Plot stores as bubbles
gdf_stores.plot(ax=ax,
               markersize=gdf_stores['Sales']/20,  # Scale size
               color='red',
               alpha=0.6,
               edgecolor='darkred',
               linewidth=0.5)

ax.set_title('Store Sales (Bubble Map)', fontsize=16, fontweight='bold')
ax.axis('off')

# Add legend (manually)
legend_sizes = [500, 2000, 4000]
for size in legend_sizes:
    ax.scatter([], [], s=size/20, c='red', alpha=0.6, 
              edgecolor='darkred', label=f'${size}')
ax.legend(title='Sales', loc='lower left', frameon=True, fontsize=10)

plt.tight_layout()
plt.show()
```

**Best Practices:**

✅ **DO:**
- Size proportional to value (NOT area - confusing!)
- Use transparency for overlapping points
- Include size legend
- Limit marker count (< 1000 for clarity)

❌ **DON'T:**
- Use area for scaling (use radius/markersize)
- Overcrowd map with too many points
- Forget basemap for context

---

## Heat Maps (Density Maps)

**Heat maps show concentration and density of point data**

**What are Heat Maps?**

**Heat maps** (or density maps) show where points cluster, using color intensity to represent density.

**When to Use:**
- Many overlapping points
- Want to show "hot spots"
- Interested in density/concentration, not individual points

**Example:** Crime density, customer clusters

**Basic Example:**

```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate clustered point data
np.random.seed(42)

# 3 clusters
cluster1 = np.random.multivariate_normal([40.7, -74.0], [[0.01, 0], [0, 0.01]], 200)  # NYC area
cluster2 = np.random.multivariate_normal([34.0, -118.2], [[0.01, 0], [0, 0.01]], 150)  # LA area
cluster3 = np.random.multivariate_normal([41.8, -87.6], [[0.01, 0], [0, 0.01]], 100)  # Chicago area

points = np.vstack([cluster1, cluster2, cluster3])

# Create hex density plot
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Scatter (shows individual points)
axes[0].scatter(points[:, 1], points[:, 0], alpha=0.3, s=20)
axes[0].set_title('Scatter Plot (Individual Points)', fontsize=13, fontweight='bold')
axes[0].set_xlabel('Longitude')
axes[0].set_ylabel('Latitude')

# Hexbin (shows density)
axes[1].hexbin(points[:, 1], points[:, 0], gridsize=30, cmap='YlOrRd', mincnt=1)
axes[1].set_title('Heat Map (Density)', fontsize=13, fontweight='bold')
axes[1].set_xlabel('Longitude')
axes[1].set_ylabel('Latitude')
plt.colorbar(axes[1].collections[0], ax=axes[1], label='Point Count')

plt.tight_layout()
plt.show()
```

**Types:**

1. **Hexbin** - Hexagonal bins (better than squares)
2. **KDE** - Kernel density estimation (smooth)
3. **Contour** - Density contour lines

**Best Practices:**

✅ Smooth density (KDE) for continuous appearance
✅ Choose bin size carefully (too small = noisy, too large = detail loss)
✅ Use sequential color scale (light to dark)

---

## Point Maps vs Choropleth: When to Use Each

**Choosing between point and area visualization is critical**

**Decision Guide:**

| Data Type | Use | Example |
|-----------|-----|---------|
| **Counts at locations** | Point/bubble map | Number of stores, incidents |
| **Rates aggregated to regions** | Choropleth | Unemployment rate by county |
| **Individual events** | Point map | Earthquake locations |
| **Regional statistics** | Choropleth | Median income by state |
| **High point density** | Heat map | Customer locations |

**Common Mistake:** 

❌ **Don't make choropleth from point data without aggregation!**

**Example - WRONG:**
- You have customer lat/lon points
- You plot on state choropleth using count
- **Problem:** Just shows population! (more people = more customers)

**Example - CORRECT:**
- Calculate customers per capita by state
- Plot RATE on choropleth
- **Result:** Shows where customers are dense relative to population

**Code Example:**

```python
import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simulate customer points
np.random.seed(42)
n_customers = 1000
customer_locs = pd.DataFrame({
    'lat': np.random.uniform(25, 50, n_customers),
    'lon': np.random.uniform(-120, -70, n_customers)
})

# Load states with population
states = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
states = states[states['continent'] == 'North America'].copy()
states['pop_est_millions'] = states['pop_est'] / 1_000_000

# Convert customers to GeoDataFrame
customer_gdf = gpd.GeoDataFrame(
    customer_locs,
    geometry=gpd.points_from_xy(customer_locs.lon, customer_locs.lat),
    crs='EPSG:4326'
)

# Spatial join: count customers per state
joined = gpd.sjoin(customer_gdf, states[['geometry', 'name', 'pop_est_millions']], 
                  how='left', predicate='within')
customer_counts = joined.groupby('name').size().reset_index(name='customer_count')

# Merge back to states
states = states.merge(customer_counts, on='name', how='left')
states['customer_count'] = states['customer_count'].fillna(0)

# Calculate rate
states['customers_per_million'] = states['customer_count'] / states['pop_est_millions']

# Visualize: Raw count vs Rate
fig, axes = plt.subplots(1, 2, figsize=(18, 6))

# WRONG: Raw count (just shows population)
states.plot(column='customer_count', cmap='YlOrRd', legend=True,
           ax=axes[0], edgecolor='black', linewidth=0.3)
axes[0].set_title('❌ Customer Count (Misleading - Shows Population)', 
                 fontsize=13, fontweight='bold', color='red')
axes[0].axis('off')

# CORRECT: Rate (shows true customer density)
states.plot(column='customers_per_million', cmap='YlGnBu', legend=True,
           ax=axes[1], edgecolor='black', linewidth=0.3)
axes[1].set_title('✅ Customers per Million People (Correct)', 
                 fontsize=13, fontweight='bold', color='green')
axes[1].axis('off')

plt.tight_layout()
plt.show()
```

**Key Principle:** Always normalize by population, area, or relevant denominator for choropleth maps!

---

## Coordinate Reference Systems (CRS)

**CRS define how coordinates map to locations on Earth**

**Key Concepts:**
- **Geographic CRS**: Lat/lon in degrees (WGS84, NAD83)
- **Projected CRS**: X/Y in meters (UTM, State Plane)
- **EPSG Codes**: Standard IDs (e.g., EPSG:4326 = WGS84)

**Common CRS:**
- EPSG:4326 - WGS84 (GPS, web standard)
- EPSG:3857 - Web Mercator (web maps)
- EPSG:2163 - US National Atlas (equal area)

**Example:**
```python
import geopandas as gpd

# Check CRS
print(gdf.crs)

# Transform to different CRS
gdf_projected = gdf.to_crs('EPSG:3857')  # Web Mercator

# Ensure matching CRS before operations
if gdf1.crs != gdf2.crs:
    gdf2 = gdf2.to_crs(gdf1.crs)
```

---

## Working with Shapefiles

**Shapefiles are the standard format for vector geographic data**

**Loading:**
```python
import geopandas as gpd

# Read shapefile
gdf = gpd.read_file('path/to/file.shp')

# Explore
print(gdf.head())
print(gdf.columns)
print(gdf.geometry.type.unique())
```

---

## Spatial Joins

**Combine datasets based on location**

**Example:**
```python
# Points in polygons
customers_gdf  # Points
states_gdf     # Polygons

# Join: which state is each customer in?
joined = gpd.sjoin(customers_gdf, states_gdf, how='left', predicate='within')
```

---

## Color Schemes for Maps

**Sequential:** Light to dark (0 to high)
- YlOrRd, Blues, Greens

**Diverging:** Two hues from center
- RdBu, PiYG (for +/-)

**Rule:** Use ColorBrewer schemes!

---

## Classification Methods

**How to bin continuous data for colors**

**Methods:**
- **Quantiles**: Equal number of features per bin
- **Equal Interval**: Equal value ranges
- **Natural Breaks** (Jenks): Minimize within-group variance

**Example:**
```python
gdf.plot(column='value', scheme='quantiles', k=5, cmap='YlOrRd', legend=True)
```

---

## Geocoding & Reverse Geocoding

**Converting between addresses and coordinates**

**Geocoding:** Address → Lat/Lon
**Reverse Geocoding:** Lat/Lon → Address

```python
from geopy.geocoders import Nominatim

geocoder = Nominatim(user_agent="myapp")

# Geocode
location = geocoder.geocode("1600 Pennsylvania Ave, Washington DC")
print(f"Lat: {location.latitude}, Lon: {location.longitude}")

# Reverse geocode
location = geocoder.reverse("38.8977, -77.0365")
print(location.address)
```

---

## Basemaps and Context

**Add geographic context to your maps**

```python
import contextily as ctx

# Add basemap
gdf_web = gdf.to_crs('EPSG:3857')  # Web Mercator for tiles
ax = gdf_web.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
plt.axis('off')
plt.show()
```

---

## Scale and Extent

**Choose map boundaries wisely**

```python
# Set bounds
ax.set_xlim([-130, -60])  # Longitude range
ax.set_ylim([20, 55])     # Latitude range

# Or auto from data
gdf.total_bounds  # Get bounds
```

---

## Part 1 Summary

**You've learned:**
✅ Geographic data types
✅ Map projections
✅ Choropleth, symbol, heat maps
✅ CRS and transformations
✅ Spatial joins
✅ Color and classification
✅ Basemaps and context

**Next:** Part 2 - Mapping Tools & Techniques

---
