**Choosing the Right Visualization Based on Data Type:**

| Data Type | Best Visualizations | When to Use |
|-----------|-------------------|-------------|
| **Time Points** | Event plot, scatter, histogram | Transaction logs, events, incidents |
| **Time Intervals** | Gantt chart, timeline bars | Project management, resource allocation |
| **Regular Time Series** | Line chart, area chart | Business metrics, continuous monitoring |
| **Irregular Time Series** | Step plot, markers + lines | Medical data, sporadic measurements |

**Key Decision Factors:**

1. **Frequency of Data**:
   - High frequency (seconds, minutes) → Line chart, aggregation
   - Low frequency (yearly) → Bar chart, markers

2. **Purpose of Analysis**:
   - Trends → Line chart
   - Events → Event plot, timeline
   - Comparisons → Multiple lines, small multiples
   - Composition → Stacked area, stream graph

3. **Audience**:
   - Technical → Can handle complexity, irregular data
   - Executive → Need simple, clean trends

4. **Duration vs. Magnitude**:
   - Duration matters → Gantt, timeline bars
   - Magnitude matters → Line, area charts

**Pro Tip**: When in doubt, start with a simple line chart for regular time series. It's the most versatile and widely understood temporal visualization.