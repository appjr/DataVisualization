# Class 6 – Advanced Techniques

[Part 1](Class6_Part1.md) | [Part 2](Class6_Part2.md) | [Part 3](Class6_Part3.md) | [Part 4](Class6_Part4.md)

---

# PART 3: ADVANCED GEOSPATIAL TECHNIQUES
# Slides 41-60
# ═══════════════════════════════════════════════════════════════

## Flow Maps

**Visualize movement between locations**

```python
# Origin-destination with lines
for origin, dest in routes:
    folium.PolyLine([origin, dest], color='blue', weight=2).add_to(m)
```

---

## Animated Maps

**Show change over time**

```python
# Time slider with folium.plugins
from folium.plugins import TimestampedGeoJson

# Animate points over time
```

---

## Spatial Clustering

**Group nearby points**

```python
from sklearn.cluster import DBSCAN

coords = np.array(list(zip(gdf.geometry.x, gdf.geometry.y)))
clusters = DBSCAN(eps=0.5, min_samples=5).fit(coords)
gdf['cluster'] = clusters.labels_
```

---

## Hexbin Aggregation

**Better than square grids**

```python
gdf.plot(kind='hex', x='lon', y='lat', C='value', reduce_C_function=np.sum)
```

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
