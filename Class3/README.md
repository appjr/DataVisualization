# Class 3: Visual Perception, Cognitive Load & Python Visualization

**Course**: MIS 6380 - Data Visualization  
**Week**: 3 (February 4, 2026)  
**Topics**: Visual Perception & Cognitive Load, Data Types & Encodings, Grammar of Graphics, Python Visualization Fundamentals

---

## 📋 Overview

This class introduces the scientific foundations of data visualization, covering human visual perception, cognitive load theory, data types and encodings, the Grammar of Graphics framework, and practical implementation in Python using Matplotlib and Seaborn.

---

## 🎯 Learning Objectives

By the end of this class, students will be able to:

1. **Understand Visual Perception**
   - Explain preattentive processing and its role in visualization
   - Apply Gestalt principles to create effective visual groupings
   - Leverage visual attention mechanisms

2. **Apply Cognitive Load Theory**
   - Distinguish between intrinsic, extraneous, and germane cognitive load
   - Design visualizations that minimize cognitive burden
   - Optimize visualizations for faster decision-making

3. **Master Data Types & Encodings**
   - Identify the four fundamental data types (Nominal, Ordinal, Quantitative, Temporal)
   - Select appropriate visual encodings based on data type and task
   - Apply Cleveland & McGill's encoding effectiveness hierarchy

4. **Implement Grammar of Graphics**
   - Understand the 7 components of the Grammar of Graphics
   - Think compositionally about visualizations
   - Build complex visualizations from simple components

5. **Create Visualizations in Python**
   - Use Matplotlib for custom visualizations
   - Leverage Seaborn for statistical graphics
   - Apply perception principles in code

---

## 📁 Files in This Directory

- **Class3.md** - Complete slide deck with 82 slides covering all topics
- **README.md** - This file, providing overview and guidance
- **Class3_Python_Examples.ipynb** - Jupyter notebook with executable code examples (to be created)

---

## 📚 Main Topics Covered

### Part 1: Visual Perception (Slides 1-15)
- How humans process visual information
- Preattentive features and the 200ms window
- Visual attention limitations
- Change blindness and inattentional blindness
- Gestalt principles (Proximity, Similarity, Enclosure, Connection)
- Dashboard design implications

### Part 2: Cognitive Load Theory (Slides 16-22)
- Introduction to cognitive load
- Three types of load: Intrinsic, Extraneous, Germane
- Managing complexity in visualizations
- Cognitive load balance optimization
- Real-world dashboard examples

### Part 3: Data Types & Encodings (Slides 23-33)
- Four fundamental data types
- Visual variables (Bertin, 1967)
- Cleveland & McGill's graphical perception research
- Encoding effectiveness hierarchy
- Data × Task × Encoding framework
- Common encoding violations

### Part 4: Grammar of Graphics (Slides 34-44)
- From chart types to compositional systems
- The 7 components: Data, Aesthetics, Geoms, Stats, Scales, Coordinates, Facets
- Layered grammar approach
- How grammar reduces cognitive load

### Part 5: Python Implementation (Slides 45-60)
- Python visualization ecosystem overview
- Matplotlib fundamentals and anatomy
- Creating and customizing plots
- Seaborn for statistical visualization
- Color palette selection
- Applying perception principles in code

### Part 6: Practical Applications (Slides 61-70)
- Complete examples integrating all principles
- Before/after comparisons
- Common mistakes to avoid
- Design checklist
- Hands-on exercises
- Connection to data science workflows

### Part 7: Wrap-up & Assignment (Slides 71-82)
- Key takeaways summary
- Resources for further learning
- Assignment details and guidance
- Q&A and next class preview

---

## 🔑 Key Concepts

### Visual Perception
- **Preattentive Processing**: Features detected in < 200ms (color, position, size, shape)
- **Gestalt Principles**: Proximity, Similarity, Enclosure, Connection, Continuity, Closure
- **Visual Attention**: Limited to 3-4 objects simultaneously

### Cognitive Load
- **Intrinsic Load**: Inherent complexity (cannot eliminate, but can manage)
- **Extraneous Load**: Unnecessary complexity from poor design (MINIMIZE)
- **Germane Load**: Productive mental effort toward insight (MAXIMIZE)

### Encoding Effectiveness (Most → Least Effective)
1. Position on common scale ⭐
2. Position on non-aligned scale
3. Length, direction, angle
4. Area
5. Volume, curvature
6. Shading, color saturation

### Grammar of Graphics Components
1. **Data**: The dataset
2. **Aesthetics**: Mappings from data to visual properties
3. **Geoms**: Visual marks (points, lines, bars)
4. **Stats**: Statistical transformations
5. **Scales**: Data-to-visual value mapping
6. **Coordinates**: Plot space
7. **Facets**: Small multiples

---

## 💻 Python Libraries Used

```python
import matplotlib.pyplot as plt  # Core plotting library
import seaborn as sns           # Statistical visualization
import pandas as pd             # Data manipulation
import numpy as np              # Numerical computing
```

---

## 📝 Assignment

**Task**: Find a poor visualization and redesign it using perception principles

**Deliverables**:
1. Original visualization (screenshot + source)
2. Critique (2-3 paragraphs identifying issues)
3. Redesign (Python code + output)
4. Justification (1-2 paragraphs explaining design choices)

**Due**: Next class (Week 4)

**Grading Breakdown**:
- Original visualization: 10%
- Critique: 30%
- Redesign: 40%
- Justification: 20%

---

## 🎓 Tips for Success

1. **Practice the Principles**: Apply perception and cognitive load concepts to every visualization you create
2. **Use the Checklist**: Before finalizing any viz, use the design checklist (Slide 63)
3. **Start Simple**: Begin with clean, simple designs and add complexity only when necessary
4. **Code Examples**: Run all code examples in the slides to understand implementation
5. **Find Bad Examples**: Train your eye by critiquing visualizations you encounter daily

---

## 📖 Recommended Reading

**Essential Books**:
- *The Visual Display of Quantitative Information* by Edward Tufte
- *Visualization Analysis & Design* by Tamara Munzner
- *Storytelling with Data* by Cole Nussbaumer Knaflic

**Research Papers**:
- Cleveland, W. S., & McGill, R. (1984). "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods"
- Heer, J., & Bostock, M. (2010). "Crowdsourcing Graphical Perception"

**Online Resources**:
- Matplotlib Documentation: https://matplotlib.org
- Seaborn Gallery: https://seaborn.pydata.org/examples/
- ColorBrewer (color palettes): https://colorbrewer2.org
- Data Visualization Society: https://datavisualizationsociety.org

---

## 🔗 Connections to Future Topics

- **Week 4 (EDA)**: Apply perception principles to exploratory analysis
- **Week 5 (Time-Series)**: Temporal encodings and dashboard design
- **Week 6 (Geospatial)**: Position encoding on maps
- **Week 10 (Storytelling)**: Direct attention using preattentive features
- **Week 12 (AI/Model Viz)**: Communicate uncertainty and predictions

---

## ❓ Common Questions

**Q: Can I ever use pie charts?**  
A: Yes, but only for 2-3 categories showing parts of a whole. Bar charts are almost always better.

**Q: What about 3D visualizations?**  
A: Avoid unless the data is genuinely 3-dimensional. 3D effects on 2D data distort perception.

**Q: How do I choose between Matplotlib and Seaborn?**  
A: Use Seaborn for statistical plots with DataFrames. Use Matplotlib for custom or low-level control.

**Q: What if stakeholders request rainbow colors?**  
A: Educate them on why perceptually uniform colors lead to better decisions. Show evidence from this class.

---

## 📧 Contact & Support

- **Office Hours**: [Insert times]
- **Course Website**: [Insert URL]
- **Discussion Forum**: [Insert URL]

---

## 📅 Next Class

**Week 4: Exploratory Data Visualization**

**Preparation**:
- Complete this week's assignment
- Review pandas DataFrames
- Install Plotly: `pip install plotly`
- Bring a dataset you want to explore

---

**Last Updated**: February 4, 2026  
**Instructor**: [Your Name]  
**Course**: MIS 6380 - Data Visualization, Spring 2026
