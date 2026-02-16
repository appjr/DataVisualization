"""
Generate slide images for Class 5: Time Series & Temporal Visualization
Creates PNG images for the first 8 slides
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

# Set style
plt.style.use('default')

def create_slide_background(ax, slide_num):
    """Create consistent slide background"""
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7.5)
    ax.axis('off')
    
    # Add slide number
    ax.text(9.5, 0.3, f'Slide {slide_num}', fontsize=10, 
            ha='right', va='bottom', color='#666', style='italic')

def wrap_text(text, width=60):
    """Wrap text to specified width"""
    words = text.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + 1 <= width:
            current_line.append(word)
            current_length += len(word) + 1
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return '\n'.join(lines)

# Slide 1: Title Slide
def create_slide_001():
    fig, ax = plt.subplots(figsize=(12, 9))
    create_slide_background(ax, 1)
    
    # Background gradient
    gradient = ax.imshow([[0, 0], [1, 1]], extent=[0, 10, 0, 7.5], 
                         aspect='auto', cmap='Blues', alpha=0.3)
    
    # Main title
    ax.text(5, 5.5, 'Class 5', fontsize=28, ha='center', 
            fontweight='bold', color='#1f4788')
    ax.text(5, 4.7, 'Data Visualization', fontsize=32, ha='center', 
            fontweight='bold', color='#2E86AB')
    
    # Subtitle
    ax.text(5, 3.8, 'Time Series & Temporal Visualization', 
            fontsize=26, ha='center', color='#333', fontweight='bold')
    ax.text(5, 3.2, 'Patterns, Trends, and Forecasting', 
            fontsize=22, ha='center', color='#555')
    
    # Course info
    ax.text(5, 1.5, 'MIS 6380 - Data Visualization', 
            fontsize=16, ha='center', color='#666')
    ax.text(5, 1.0, 'Spring 2026', 
            fontsize=14, ha='center', color='#666')
    
    plt.tight_layout()
    plt.savefig('slide_images/slide_001.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created slide 001: Title")

# Slide 2: Learning Objectives
def create_slide_002():
    fig, ax = plt.subplots(figsize=(12, 9))
    create_slide_background(ax, 2)
    
    # Title
    ax.text(5, 7, 'Learning Objectives', fontsize=28, ha='center', 
            fontweight='bold', color='#2E86AB')
    
    # Section titles and content
    sections = [
        ("Foundational Knowledge:", 6.2, [
            "• Understand unique characteristics of temporal data",
            "• Recognize different types of time series patterns",
            "• Choose appropriate visualizations for temporal analysis"
        ]),
        ("Technical Skills:", 4.9, [
            "• Create effective time series visualizations in Python",
            "• Perform time series decomposition",
            "• Visualize forecasts with confidence intervals",
            "• Build interactive temporal dashboards"
        ]),
        ("Analytical Abilities:", 3.2, [
            "• Identify trends, seasonality, and cycles",
            "• Detect anomalies and change points",
            "• Compare multiple time series effectively"
        ]),
        ("Practical Applications:", 1.8, [
            "• Apply best practices for temporal dashboards",
            "• Handle missing and irregular temporal data"
        ])
    ]
    
    for title, y_start, items in sections:
        ax.text(0.5, y_start, title, fontsize=14, fontweight='bold', 
                color='#1f4788', va='top')
        for i, item in enumerate(items):
            ax.text(0.7, y_start - 0.35 * (i + 1), item, fontsize=11, 
                    va='top', color='#333')
    
    plt.tight_layout()
    plt.savefig('slide_images/slide_002.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created slide 002: Learning Objectives")

# Slide 3: Why Time Series Visualization Matters
def create_slide_003():
    fig, ax = plt.subplots(figsize=(12, 9))
    create_slide_background(ax, 3)
    
    # Title
    ax.text(5, 7, 'Why Time Series Visualization Matters', fontsize=26, 
            ha='center', fontweight='bold', color='#2E86AB')
    
    # Applications grid
    applications = [
        ("📈 Financial", "Stock prices\nPortfolio tracking\nMarket analysis", 1.5, 5.8),
        ("🛒 Retail", "Sales patterns\nInventory levels\nConversion rates", 4.2, 5.8),
        ("🏭 Manufacturing", "Production output\nQuality control\nDowntime", 6.9, 5.8),
        ("🌐 Digital", "Website traffic\nApp usage\nPerformance", 1.5, 3.8),
        ("🏥 Healthcare", "Patient monitoring\nTreatment effects\nTrials", 4.2, 3.8),
        ("📊 Economics", "GDP indicators\nEmployment\nInflation", 6.9, 3.8),
        ("🌡️ IoT/Sensors", "Temperature\nEnergy use\nTelemetry", 1.5, 1.8),
    ]
    
    for emoji_title, desc, x, y in applications:
        # Box
        box = FancyBboxPatch((x-0.6, y-0.7), 2.2, 1.4, 
                             boxstyle="round,pad=0.1", 
                             edgecolor='#2E86AB', facecolor='#E8F4F8', 
                             linewidth=2)
        ax.add_patch(box)
        ax.text(x+0.5, y+0.4, emoji_title, fontsize=13, fontweight='bold', 
                color='#1f4788')
        ax.text(x+0.5, y-0.3, desc, fontsize=9, color='#333', 
                va='center', ha='center')
    
    # Key insight
    ax.text(5, 0.7, '70-80% of business data has a temporal component', 
            fontsize=13, ha='center', fontweight='bold', color='#d62728',
            bbox=dict(boxstyle='round', facecolor='#fff3cd', edgecolor='#d62728', linewidth=2))
    
    plt.tight_layout()
    plt.savefig('slide_images/slide_003.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created slide 003: Why Time Series Matters")

# Slide 4: What Makes Time Series Data Special
def create_slide_004():
    fig, ax = plt.subplots(figsize=(12, 9))
    create_slide_background(ax, 4)
    
    # Title
    ax.text(5, 7, 'What Makes Time Series Data Special?', fontsize=26, 
            ha='center', fontweight='bold', color='#2E86AB')
    
    # Special properties
    properties = [
        ("1. Temporal Ordering Matters", "Order contains critical information - cannot shuffle!", 6.2),
        ("2. Temporal Dependencies", "Today's value depends on yesterday's values", 5.5),
        ("3. Non-IID", "NOT Independent & Identically Distributed", 4.8),
        ("4. Multiple Time Scales", "Hourly, daily, weekly, monthly, seasonal patterns", 4.1),
        ("5. Non-Stationarity", "Statistical properties change over time", 3.4),
        ("6. Irregular Intervals", "Gaps from weekends, holidays, sensor failures", 2.7),
        ("7. Context-Dependent", "Same value means different things at different times", 2.0),
    ]
    
    for title, desc, y in properties:
        # Number circle
        number = title.split('.')[0]
        circle = plt.Circle((1.2, y), 0.25, color='#2E86AB', ec='#1f4788', linewidth=2)
        ax.add_patch(circle)
        ax.text(1.2, y, number, fontsize=14, ha='center', va='center', 
                color='white', fontweight='bold')
        
        # Text
        ax.text(1.7, y+0.1, title.split('. ')[1], fontsize=13, fontweight='bold', 
                color='#1f4788', va='top')
        ax.text(1.7, y-0.15, desc, fontsize=10, color='#555', va='top')
    
    # Bottom insight
    ax.text(5, 0.8, 'Standard data analysis methods don\'t work for time series!', 
            fontsize=14, ha='center', fontweight='bold', color='#d62728',
            bbox=dict(boxstyle='round', facecolor='#ffe6e6', edgecolor='#d62728', linewidth=2))
    
    plt.tight_layout()
    plt.savefig('slide_images/slide_004.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created slide 004: What Makes Time Series Special")

# Slide 5: Types of Temporal Data
def create_slide_005():
    fig, ax = plt.subplots(figsize=(12, 9))
    create_slide_background(ax, 5)
    
    # Title
    ax.text(5, 7, 'Types of Temporal Data', fontsize=28, ha='center', 
            fontweight='bold', color='#2E86AB')
    
    # Four types in quadrants
    types = [
        ("Time Points", "Discrete Events", "🛒 Purchases\n🌍 Earthquakes\n🐦 Tweets", 
         "Event plot\nTimeline\nScatter", 2, 4.8),
        ("Time Intervals", "Spans/Durations", "🏥 Hospital stays\n🏭 Production\n✈️ Flights", 
         "Gantt chart\nTimeline bars", 7, 4.8),
        ("Regular Time Series", "Fixed Intervals", "📊 Stock prices\n🌡️ Temperature\n💰 Sales", 
         "Line chart\nArea chart", 2, 2.2),
        ("Irregular Time Series", "Variable Intervals", "🏥 Medical checks\n🔧 Maintenance\n📝 Surveys", 
         "Step plot\nMarkers+lines", 7, 2.2),
    ]
    
    for title, subtitle, examples, viz, x, y in types:
        # Box
        box = FancyBboxPatch((x-1.8, y-1.4), 3.5, 2.5, 
                             boxstyle="round,pad=0.15", 
                             edgecolor='#2E86AB', facecolor='#F0F8FF', 
                             linewidth=2.5)
        ax.add_patch(box)
        
        # Content
        ax.text(x, y+0.9, title, fontsize=15, ha='center', fontweight='bold', 
                color='#1f4788')
        ax.text(x, y+0.5, subtitle, fontsize=11, ha='center', color='#555', 
                style='italic')
        ax.text(x, y, examples, fontsize=10, ha='center', color='#333', va='center')
        ax.text(x, y-0.9, viz, fontsize=9, ha='center', color='#2E86AB', 
                va='center', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('slide_images/slide_005.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created slide 005: Types of Temporal Data")

# Slide 6: Basic Time Series Plot - The Line Chart
def create_slide_006():
    fig, ax = plt.subplots(figsize=(12, 9))
    create_slide_background(ax, 6)
    
    # Title
    ax.text(5, 7, 'Basic Time Series Plot: The Line Chart', fontsize=26, 
            ha='center', fontweight='bold', color='#2E86AB')
    
    # Why line charts work
    ax.text(5, 6.3, 'Why Line Charts Work for Time Series', fontsize=16, 
            ha='center', fontweight='bold', color='#1f4788')
    
    reasons = [
        "✓ Shows Continuity - Lines connect data points",
        "✓ Preserves Order - Left-to-right temporal progression",
        "✓ Natural Mental Model - Time flows horizontally",
        "✓ Scales Well - Works from minutes to decades",
        "✓ Easy Comparison - Multiple lines enable series comparison"
    ]
    
    y_pos = 5.7
    for reason in reasons:
        ax.text(1, y_pos, reason, fontsize=12, color='#2c5f2d', va='top')
        y_pos -= 0.4
    
    # Core design principles box
    box = FancyBboxPatch((0.5, 1.2), 9, 3.2, 
                         boxstyle="round,pad=0.15", 
                         edgecolor='#2E86AB', facecolor='#E8F4F8', 
                         linewidth=2)
    ax.add_patch(box)
    
    ax.text(5, 4.1, 'Core Design Principles', fontsize=15, ha='center', 
            fontweight='bold', color='#1f4788')
    
    principles = [
        "1. Time on X-Axis (Horizontal) - Matches reading direction",
        "2. Choose Appropriate Line Style - Solid/dashed/markers",
        "3. Line Width Matters - 1.5-2.5 for standard plots",
        "4. Consistent Time Intervals - Show gaps explicitly",
        "5. Banking to 45° - Choose aspect ratio for clarity"
    ]
    
    y_pos = 3.6
    for principle in principles:
        ax.text(1, y_pos, principle, fontsize=11, color='#333', va='top')
        y_pos -= 0.45
    
    plt.tight_layout()
    plt.savefig('slide_images/slide_006.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created slide 006: Basic Line Chart")

# Slide 7: Choosing Appropriate Time Scales
def create_slide_007():
    fig, ax = plt.subplots(figsize=(12, 9))
    create_slide_background(ax, 7)
    
    # Title
    ax.text(5, 7, 'Choosing Appropriate Time Scales', fontsize=26, 
            ha='center', fontweight='bold', color='#2E86AB')
    
    # The Problem
    ax.text(5, 6.3, 'The Problem: Resolution vs. Noise', fontsize=16, 
            ha='center', fontweight='bold', color='#1f4788')
    
    # Three scenarios
    scenarios = [
        ("TOO GRANULAR", "See noise, miss patterns", "#d62728", 2.5, 5.2),
        ("JUST RIGHT", "Patterns clear, noise manageable", "#2c5f2d", 5, 5.2),
        ("TOO COARSE", "Miss important variations", "#ff7f0e", 7.5, 5.2),
    ]
    
    for title, desc, color, x, y in scenarios:
        box = FancyBboxPatch((x-1.1, y-0.6), 2.2, 1.1, 
                             boxstyle="round,pad=0.1", 
                             edgecolor=color, facecolor='white', 
                             linewidth=3)
        ax.add_patch(box)
        ax.text(x, y+0.2, title, fontsize=12, ha='center', fontweight='bold', 
                color=color)
        ax.text(x, y-0.3, desc, fontsize=10, ha='center', color='#333')
    
    # Decision factors box
    box = FancyBboxPatch((0.5, 0.8), 9, 3.5, 
                         boxstyle="round,pad=0.15", 
                         edgecolor='#2E86AB', facecolor='#F0F8FF', 
                         linewidth=2)
    ax.add_patch(box)
    
    ax.text(5, 4, 'Choosing the Right Scale', fontsize=15, ha='center', 
            fontweight='bold', color='#1f4788')
    
    factors = [
        "1. Match to Business Question - 'Monthly trend?' → Monthly aggregation",
        "2. Match to Data Frequency - High freq → Aggregate; Low freq → Show as-is",
        "3. Consider Pattern Timeframe - Weekly cycles need 4-8 weeks of daily data",
        "4. Audience Considerations - Executives want monthly, analysts want daily",
    ]
    
    y_pos = 3.5
    for factor in factors:
        ax.text(1, y_pos, factor, fontsize=11, color='#333', va='top')
        y_pos -= 0.5
    
    # Best practice
    ax.text(5, 1.3, '💡 Best Practice: Provide multiple views at different scales', 
            fontsize=12, ha='center', fontweight='bold', color='#2c5f2d',
            bbox=dict(boxstyle='round', facecolor='#e8f5e9', edgecolor='#2c5f2d', linewidth=2))
    
    plt.tight_layout()
    plt.savefig('slide_images/slide_007.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created slide 007: Time Scales")

# Slide 8: Handling Missing Temporal Data
def create_slide_008():
    fig, ax = plt.subplots(figsize=(12, 9))
    create_slide_background(ax, 8)
    
    # Title
    ax.text(5, 7, 'Handling Missing Temporal Data', fontsize=26, 
            ha='center', fontweight='bold', color='#2E86AB')
    
    # Why it's different
    ax.text(5, 6.3, 'Why Temporal Missing Data is Different', fontsize=15, 
            ha='center', fontweight='bold', color='#1f4788')
    
    issues = [
        "❌ Gaps break continuity",
        "❌ Missing values have temporal context",
        "❌ Imputation affects subsequent values",
        "❌ Visualization can mislead"
    ]
    
    y_pos = 5.8
    for issue in issues:
        ax.text(2.5, y_pos, issue, fontsize=12, color='#d62728', va='top')
        y_pos -= 0.35
    
    # Visualization strategies
    ax.text(5, 4.5, 'Visualization Strategies', fontsize=15, ha='center', 
            fontweight='bold', color='#1f4788')
    
    strategies = [
        ("1. Show Gaps Explicitly", "Use markers only, no line over gaps", 3.9),
        ("2. Interpolate & Distinguish", "Use dashed/different color for estimates", 3.2),
        ("3. Remove Missing Periods", "Filter out systematic gaps (weekends)", 2.5),
        ("4. Shading + Annotation", "Mark missing regions with vertical lines", 1.8),
    ]
    
    for title, desc, y in strategies:
        ax.text(1, y, title, fontsize=12, fontweight='bold', color='#1f4788', va='top')
        ax.text(1.2, y-0.3, desc, fontsize=10, color='#555', va='top')
    
    # Key principle
    ax.text(5, 0.8, '🔴 NEVER hide missing data without disclosure!', 
            fontsize=13, ha='center', fontweight='bold', color='#d62728',
            bbox=dict(boxstyle='round', facecolor='#ffe6e6', edgecolor='#d62728', linewidth=2))
    
    plt.tight_layout()
    plt.savefig('slide_images/slide_008.png', dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created slide 008: Missing Data")

# Main execution
def main():
    print("Creating Class 5 slide images...")
    print("=" * 50)
    
    create_slide_001()
    create_slide_002()
    create_slide_003()
    create_slide_004()
    create_slide_005()
    create_slide_006()
    create_slide_007()
    create_slide_008()
    
    print("=" * 50)
    print("✅ All 8 slide images created successfully!")
    print(f"📁 Location: Class5/slide_images/")

if __name__ == "__main__":
    main()
