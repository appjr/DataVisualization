# Class X – Trading Chart Techniques: Lab Exercises

[← Main](Classx.md) | [Part 1](Classx_Part1.md) | [Part 2](Classx_Part2.md) | [Part 3](Classx_Part3.md) | [Part 4](Classx_Part4.md)

---

## Exercise 1: Your First Candlestick Chart (Part 1)

**Objective**: Build a professional dark-theme candlestick chart with volume for a ticker of your choice.

**Requirements:**
1. Download 6 months of OHLCV data for ANY ticker using `yfinance`
2. Create a candlestick chart using `mplfinance` with:
   - Dark background style (`nightclouds`)
   - Green (#26a69a) for bullish candles, Red (#ef5350) for bearish
   - Volume bars color-matched to candle direction
   - A 20-day SMA overlay (yellow dashed line)
   - Proper title with ticker name and date range
3. Save the output as `exercise1_candlestick.png`

**Bonus**: Add a second overlay for the 50-day SMA in a different color.

```python
import mplfinance as mpf
import yfinance as yf
import pandas as pd

# Your code here
ticker = "???"  # Choose any ticker
df = yf.download(ticker, start="????", end="????")

# Define custom style
mc = mpf.make_marketcolors(
    up='#26a69a', down='#ef5350',
    wick={'up': '#26a69a', 'down': '#ef5350'},
    volume={'up': '#26a69a', 'down': '#ef5350'}
)
style = mpf.make_mpf_style(marketcolors=mc, base_mpf_style='nightclouds')

# Add SMA overlay
# ... your code ...
```

---

## Exercise 2: Moving Average Analysis (Part 2)

**Objective**: Visualize and analyze moving average signals for a chosen stock.

**Requirements:**
1. Download 2 years of data for a stock in the S&P 500
2. Plot three SMAs: 20-day (blue), 50-day (orange), 200-day (red)
3. Detect and annotate all Golden Cross and Death Cross events:
   - Mark each Golden Cross with a green vertical line and "GC" label
   - Mark each Death Cross with a red vertical line and "DC" label
4. Add a text box showing the count of each signal type
5. Determine: was each signal profitable? Annotate the chart with the answer.

**Expected Output**: A chart showing price + 3 MAs with clearly labeled crossover signals.

```python
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Your code here
df = yf.download("???", start="2022-01-01", end="2024-12-31")

# Calculate SMAs
df['SMA_20']  = # ...
df['SMA_50']  = # ...
df['SMA_200'] = # ...

# Detect golden/death crosses
# ...

# Plot
# ...
```

---

## Exercise 3: Fibonacci Retracement Tool (Part 2)

**Objective**: Build a reusable function that draws Fibonacci levels on any chart.

**Requirements:**
1. Write a function `draw_fibonacci(ticker, start, end, swing_low_date, swing_high_date)` that:
   - Downloads the price data
   - Calculates all 6 retracement levels (0%, 23.6%, 38.2%, 50%, 61.8%, 100%)
   - Draws horizontal colored lines at each level
   - Shades the "golden zone" (38.2% to 61.8%) in semi-transparent orange
   - Labels each line with its ratio and price level
2. Call the function for a real recent swing in any stock
3. Annotate where price actually bounced (if applicable)

**Expected Output**: A chart with professionally labeled Fibonacci levels.

---

## Exercise 4: RSI + MACD Dashboard (Part 3)

**Objective**: Build a 3-panel chart showing price, RSI, and MACD with all signals annotated.

**Requirements:**
1. Download 1 year of data for any stock
2. Build a 3-panel matplotlib chart (price on top, RSI middle, MACD bottom)
3. On the price panel:
   - Plot close price as a line
   - Mark dates where RSI crossed above 30 with green up-arrows
   - Mark dates where RSI crossed below 70 with red down-arrows
4. On the RSI panel:
   - RSI line with 70/50/30 reference lines
   - Shade overbought (>70) and oversold (<30) zones
5. On the MACD panel:
   - MACD line (blue), Signal line (orange), histogram (green/red)
6. All panels share the x-axis

**Grading Criteria:**
- Clean dark theme throughout
- Correct indicator calculations
- All signal annotations visible and labeled
- Axes labeled, title present, legend present

---

## Exercise 5: Chart Pattern Hunt (Part 4)

**Objective**: Find a real chart pattern in historical price data and annotate it.

**Requirements:**
1. Search through any 3 stocks for ONE of the following patterns (use at least 3 months of daily data):
   - Head and Shoulders (top or bottom)
   - Cup and Handle
   - Ascending or Descending Triangle
   - Double Top or Double Bottom
2. Once you find it, create a chart that:
   - Shows the pattern with candlesticks
   - Draws the key trendlines (neckline, resistance line, etc.) using `ax.plot()` or `ax.axhline()`
   - Labels the pattern components (Left Shoulder, Head, Right Shoulder / Cup, Handle, etc.)
   - Shows whether the breakout/breakdown actually happened
   - Annotates the measured move target price
3. Write 3-4 sentences explaining what you found and what it implied at the time

**Hint**: Look at stocks that had significant price swings in 2022-2024.

---

## Exercise 6: The Complete Trading Dashboard (Part 4 — Capstone)

**Objective**: Build a fully interactive Plotly trading dashboard for any ticker.

**Requirements:**
1. Use `plotly.subplots.make_subplots` to create a 4-panel dashboard:
   - Panel 1: Candlestick chart + SMA 20/50/200 + Bollinger Bands
   - Panel 2: Volume bars (color-matched to candle direction)
   - Panel 3: RSI with 70/30 reference lines and shaded zones
   - Panel 4: MACD line, Signal line, and histogram
2. All panels must share the same x-axis (synchronized scrolling/zoom)
3. Use `plotly_dark` template throughout
4. Add hover tooltips showing OHLCV values on mouse-over
5. Save as an HTML file (`my_dashboard.html`) that works standalone in a browser

**Deliverable**: Submit the `.html` file. Your instructor will open it in a browser.

**Grading:**
- Correct indicator calculations (30%)
- Visual design and readability (25%)
- All 4 panels present and functional (25%)
- Interactive features working (20%)

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import yfinance as yf

# Template
fig = make_subplots(
    rows=4, cols=1,
    shared_xaxes=True,
    # ... your configuration ...
)

# Your complete implementation here
# ...

fig.write_html("my_dashboard.html")
```

---

## Bonus Exercise: Backtesting Visualization

**Objective**: Visualize the performance of the MA crossover strategy.

**Requirements:**
1. Implement the SMA 20/50 crossover strategy on 5 years of AAPL data
2. Create a 3-panel performance visualization:
   - Panel 1: Equity curve (strategy vs. buy-and-hold) with shaded outperformance zone
   - Panel 2: Drawdown chart (red filled area showing % below peak)
   - Panel 3: Histogram of per-trade returns with mean and median lines
3. Print a performance summary:
   ```
   Strategy Results (2020-2024):
   Total Return:     ____%
   Annual Return:    ____%
   Max Drawdown:     ____%
   Win Rate:         ____%
   Number of trades: ____
   Sharpe Ratio:     ____
   ```

---

## Setup Instructions

```bash
# Install all required libraries
pip install mplfinance yfinance plotly pandas numpy matplotlib

# Verify installation
python -c "import mplfinance, yfinance, plotly, pandas, numpy, matplotlib; print('All libraries installed!')"
```

**Data Note**: `yfinance` downloads free real historical data from Yahoo Finance. API limits are generous for class use. If you hit a limit, wait 10 minutes and retry.

**Common Issues:**
- `yfinance` multi-ticker downloads return a multi-level DataFrame — use `df['Close']` to get the close price
- mplfinance requires the index to be a `DatetimeIndex` — use `pd.to_datetime(df.index)`
- Plotly HTML files can be large (5-10 MB) — this is normal

---

*MIS 6380 — Data Visualization | Class X: Trading Chart Techniques | Spring 2026*
