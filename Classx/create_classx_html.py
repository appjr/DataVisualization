"""
Create Classx_Complete.html from the four markdown Part files.
"""
import re, os

PARTS = [
    'Classx/Classx_Part1.md',
    'Classx/Classx_Part2.md',
    'Classx/Classx_Part3.md',
    'Classx/Classx_Part4.md',
]
OUTPUT = 'Classx/Classx_Complete.html'

def md_to_html(text):
    # Code blocks
    text = re.sub(r'```(\w*)\n(.*?)```', lambda m: f'<pre><code class="language-{m.group(1)}">{m.group(2)}</code></pre>', text, flags=re.DOTALL)
    # Inline code
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # H4
    text = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', text, flags=re.MULTILINE)
    # H3
    text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    # H2
    text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    # H1
    text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    # Tables
    def convert_table(m):
        rows = [r.strip() for r in m.group(0).strip().split('\n') if r.strip() and not re.match(r'^\|[-| ]+\|$', r.strip())]
        html = '<table>\n'
        for i, row in enumerate(rows):
            cells = [c.strip() for c in row.strip('|').split('|')]
            tag = 'th' if i == 0 else 'td'
            html += '<tr>' + ''.join(f'<{tag}>{c}</{tag}>' for c in cells) + '</tr>\n'
        return html + '</table>\n'
    text = re.sub(r'(\|.+\n)+', convert_table, text)
    # Blockquote
    text = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', text, flags=re.MULTILINE)
    # Horizontal rule
    text = re.sub(r'^---+$', '<hr>', text, flags=re.MULTILINE)
    # Unordered lists
    def convert_ul(m):
        items = re.findall(r'^[*\-] (.+)$', m.group(0), re.MULTILINE)
        return '<ul>\n' + ''.join(f'<li>{i}</li>\n' for i in items) + '</ul>\n'
    text = re.sub(r'(^[*\-] .+\n?)+', convert_ul, text, flags=re.MULTILINE)
    # Ordered lists
    def convert_ol(m):
        items = re.findall(r'^\d+\. (.+)$', m.group(0), re.MULTILINE)
        return '<ol>\n' + ''.join(f'<li>{i}</li>\n' for i in items) + '</ol>\n'
    text = re.sub(r'(^\d+\. .+\n?)+', convert_ol, text, flags=re.MULTILINE)
    # Paragraphs
    paras = text.split('\n\n')
    result = []
    for p in paras:
        p = p.strip()
        if not p: continue
        if p.startswith('<'): result.append(p); continue
        result.append(f'<p>{p}</p>')
    return '\n'.join(result)

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Segoe UI', Roboto, Arial, sans-serif; background: #f0f2f5; color: #222; line-height: 1.7; }
.container { max-width: 1200px; margin: 0 auto; padding: 30px 20px; }
.header { background: linear-gradient(135deg, #1e1e1e 0%, #2c3e50 100%); color: white; padding: 50px 40px; border-radius: 12px; margin-bottom: 30px; }
.header h1 { font-size: 2.4em; margin-bottom: 8px; }
.header p  { font-size: 1.1em; opacity: 0.8; }
.slide { background: white; border-radius: 10px; box-shadow: 0 2px 12px rgba(0,0,0,0.08); margin-bottom: 40px; overflow: hidden; }
.slide-header { background: #1e1e1e; color: white; padding: 14px 24px; display: flex; align-items: center; gap: 14px; }
.slide-num { background: #26a69a; color: white; border-radius: 50%; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 0.95em; flex-shrink: 0; }
.slide-title { font-size: 1.05em; font-weight: 600; }
.slide-image { width: 100%; max-height: 520px; object-fit: contain; background: #1e1e1e; display: block; }
.slide-content { padding: 28px 32px; }
h1 { font-size: 1.8em; color: #1e1e1e; border-bottom: 3px solid #26a69a; padding-bottom: 8px; margin: 20px 0 12px; }
h2 { font-size: 1.35em; color: #2c3e50; border-left: 4px solid #26a69a; padding-left: 12px; margin: 18px 0 10px; }
h3 { font-size: 1.1em; color: #34495e; margin: 14px 0 8px; }
h4 { font-size: 1em; color: #555; margin: 10px 0 6px; }
p  { margin: 8px 0; }
ul, ol { margin: 8px 0 8px 24px; }
li { margin: 4px 0; }
pre { background: #1e1e1e; color: #abb2bf; padding: 18px 20px; border-radius: 8px; overflow-x: auto; font-size: 0.85em; margin: 14px 0; line-height: 1.5; }
code { background: #f0f0f0; color: #e83e8c; padding: 2px 5px; border-radius: 4px; font-size: 0.88em; }
pre code { background: none; color: inherit; padding: 0; }
table { border-collapse: collapse; width: 100%; margin: 14px 0; font-size: 0.9em; }
th { background: #2c3e50; color: white; padding: 10px 14px; text-align: left; }
td { border: 1px solid #ddd; padding: 9px 14px; }
tr:nth-child(even) { background: #f8f9fa; }
blockquote { border-left: 4px solid #26a69a; background: #f8fffe; padding: 12px 18px; margin: 14px 0; border-radius: 0 6px 6px 0; font-style: italic; color: #444; }
hr { border: none; border-top: 1px solid #eee; margin: 20px 0; }
strong { color: #1e1e1e; }
.toc { background: white; border-radius: 10px; box-shadow: 0 2px 12px rgba(0,0,0,0.08); padding: 28px 32px; margin-bottom: 30px; }
.toc h2 { margin-bottom: 14px; }
.toc-part { margin: 12px 0 4px; font-weight: bold; color: #26a69a; }
.toc a { color: #2c3e50; text-decoration: none; display: inline-block; padding: 1px 0; }
.toc a:hover { color: #26a69a; }
@media (max-width: 768px) { .container { padding: 12px; } .slide-content { padding: 16px; } }
"""

SLIDE_TITLES = {
    1: "Trading Chart Techniques: Data Visualization in Financial Markets",
    2: "Learning Objectives",
    3: "Why Trading Visualization Matters",
    4: "The Four Dimensions of Price Data (OHLC)",
    5: "From Raw Numbers to Visual Signals",
    6: "Line Charts: The Simplest View",
    7: "OHLC Bar Charts: More Data, Less Beauty",
    8: "Candlestick Charts: The Japanese Art of Price",
    9: "Anatomy of a Single Candlestick",
    10: "Color and Fill Conventions in Candlesticks",
    11: "Reading Candlestick Shapes as Visual Signals",
    12: "The Volume Bar: The Market's Hidden Heartbeat",
    13: "Building Your First Candlestick Chart in Python",
    14: "Time Scales and Aggregation",
    15: "Multi-Asset Comparison: Normalized Returns Charts",
    16: "Logarithmic vs. Linear Price Scales",
    17: "Chart Interactivity with Plotly",
    18: "Common Charting Mistakes",
    19: "Choosing the Right Chart Type",
    20: "Part 1 Summary & Preview of Part 2",
    21: "Introduction: Overlaying Indicators on Price Charts",
    22: "What Is a Moving Average? The Smoothing Intuition",
    23: "Simple Moving Average (SMA): Visualization and Code",
    24: "Exponential Moving Average (EMA): Weighting the Recent Past",
    25: "SMA vs. EMA Side-by-Side: Which to Use?",
    26: "The Golden Cross and Death Cross",
    27: "Weighted Moving Average (WMA): Linear Weighting",
    28: "Volume Weighted Average Price (VWAP)",
    29: "MA Ribbons: Visualizing Multiple MAs Simultaneously",
    30: "MA Envelope Bands: Dynamic Support and Resistance",
    31: "Introduction to Fibonacci: The Golden Ratio in Markets",
    32: "Fibonacci Retracement: Drawing Levels on a Price Chart",
    33: "Fibonacci Extension: Projecting Price Targets",
    34: "Visualizing Fibonacci Levels in Python",
    35: "Fibonacci Fan Lines: Diagonal Trend-Based Levels",
    36: "Fibonacci Time Zones: When Price Might Turn",
    37: "MA Crossover Strategy: Full Visualization with Entry/Exit Signals",
    38: "Combining Fibonacci with Moving Averages: Confluence Zones",
    39: "Critique: When Moving Averages Mislead",
    40: "Part 2 Summary & Preview of Part 3",
    41: "The Multi-Panel Chart Architecture",
    42: "Relative Strength Index (RSI): The Momentum Oscillator",
    43: "RSI Calculation and Visual Interpretation",
    44: "RSI Divergence: The Most Powerful RSI Signal",
    45: "MACD: Moving Average Convergence/Divergence",
    46: "MACD Crossover Signals: Visualizing Buy and Sell Triggers",
    47: "MACD Histogram: Visualizing Momentum Acceleration",
    48: "Bollinger Bands: Visualizing Volatility as a Dynamic Channel",
    49: "Bollinger Band Patterns: The Walk, the Squeeze, and the W-Bottom",
    50: "Building Bollinger Bands in Python",
    51: "Stochastic Oscillator: Visualizing Where Close Sits Within the Range",
    52: "Stochastic Crossovers and Divergence",
    53: "Average True Range (ATR): Measuring Volatility Without Direction",
    54: "ATR-Based Stop Loss Visualization",
    55: "On-Balance Volume (OBV): Cumulative Buy vs. Sell Volume",
    56: "Volume Profile: Visualizing Where Trading Activity Concentrates",
    57: "VWAP Deviation Bands: Combining Volume and Volatility",
    58: "Building a Multi-Panel Indicator Dashboard",
    59: "Indicator Combinations: RSI + MACD Convergence",
    60: "Part 3 Summary & Preview of Part 4",
    61: "Introduction to Chart Pattern Analysis",
    62: "Head and Shoulders: The King of Reversal Patterns",
    63: "Inverse Head and Shoulders: The Bullish Mirror",
    64: "Cup and Handle: The Rounding Bottom",
    65: "Triangle Patterns: Symmetrical, Ascending, Descending",
    66: "Flag and Pennant Patterns: Brief Pauses in Strong Trends",
    67: "Double Top and Double Bottom: Testing Limits Twice",
    68: "Wedge Patterns: Rising and Falling",
    69: "Introduction to Elliott Wave Theory",
    70: "Elliott Wave Rules and Visual Guidelines",
    71: "Annotating Wave Counts in Python",
    72: "Combining Patterns with Indicators: The Confirmation Principle",
    73: "Support and Resistance Visualization",
    74: "Building a Complete Trading Dashboard: Architecture Design",
    75: "Trading Dashboard: Python Implementation Part 1",
    76: "Trading Dashboard: Python Implementation Part 2",
    77: "Interactive Trading Dashboard with Plotly",
    78: "Backtesting Visualizations: Equity Curve, Drawdown, Return Distribution",
    79: "Common Mistakes in Trading Visualization",
    80: "Summary, Resources, and Next Steps",
}

PART_RANGES = {
    "Part 1: Foundations of Financial Chart Visualization": range(1, 21),
    "Part 2: Trend Analysis — Moving Averages & Fibonacci":  range(21, 41),
    "Part 3: Momentum & Volatility Indicators":              range(41, 61),
    "Part 4: Pattern Recognition & Trading Dashboards":      range(61, 81),
}

def build_toc():
    html = '<div class="toc"><h2>Table of Contents</h2>'
    for part, rng in PART_RANGES.items():
        html += f'<div class="toc-part">{part}</div><ul>'
        for i in rng:
            title = SLIDE_TITLES.get(i, f'Slide {i}')
            html += f'<li><a href="#slide-{i:03d}">Slide {i}: {title}</a></li>'
        html += '</ul>'
    html += '</div>'
    return html

def build_slide_html(slide_num, content_md):
    title = SLIDE_TITLES.get(slide_num, f'Slide {slide_num}')
    img_path = f'slide_images/slide_{slide_num:03d}_final.png'
    img_tag = f'<img class="slide-image" src="{img_path}" alt="Slide {slide_num}: {title}">' if os.path.exists(f'Classx/{img_path}') else ''
    content_html = md_to_html(content_md)
    return f'''
<div class="slide" id="slide-{slide_num:03d}">
  <div class="slide-header">
    <div class="slide-num">{slide_num}</div>
    <div class="slide-title">{title}</div>
  </div>
  {img_tag}
  <div class="slide-content">{content_html}</div>
</div>'''

def extract_slides_from_part(filepath):
    with open(filepath, encoding='utf-8') as f:
        text = f.read()
    # Split on ## headers (slide boundaries)
    sections = re.split(r'\n(?=## )', text)
    slides = []
    for s in sections:
        s = s.strip()
        if s.startswith('## ') or (s and not s.startswith('#')):
            slides.append(s)
    return slides

# Build all slides
all_content = []
slide_counter = 1
for part_file in PARTS:
    slides = extract_slides_from_part(part_file)
    for slide_md in slides:
        if slide_counter > 80: break
        all_content.append((slide_counter, slide_md))
        slide_counter += 1

html_slides = '\n'.join(build_slide_html(n, md) for n, md in all_content)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Class X – Trading Chart Techniques: Data Visualization in Financial Markets</title>
<style>{CSS}</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>Class X – Trading Chart Techniques</h1>
    <p>Data Visualization in Financial Markets &nbsp;|&nbsp; MIS 6380 – Data Visualization &nbsp;|&nbsp; Spring 2026</p>
    <p style="margin-top:8px;opacity:0.65">80 Slides across 4 Parts: Foundations · Trend Analysis · Momentum & Volatility · Pattern Recognition</p>
  </div>
  {build_toc()}
  {html_slides}
</div>
</body>
</html>"""

with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'✅ HTML written to {OUTPUT}  ({len(html)//1024} KB)')
