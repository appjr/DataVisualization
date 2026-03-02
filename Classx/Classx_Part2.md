# Class X – Part 2

[← Main](Classx.md) | [Part 1](Classx_Part1.md) | [Part 2](Classx_Part2.md) | [Part 3](Classx_Part3.md) | [Part 4](Classx_Part4.md)

---

# PART 2: TREND ANALYSIS — MOVING AVERAGES & FIBONACCI
# Slides 21–40
# ═══════════════════════════════════════════════════════════════

---

## Introduction: Overlaying Indicators on Price Charts

**Indicators are mathematical transformations of price data drawn on top of (or below) the price chart:**

**What an Indicator Is — and Isn't:**
```
Indicator = f(price history) → a new visual layer on the chart

It does NOT add new information.
It REVEALS structure that is already in the price data.
It makes patterns visible to the human eye.
```

**Three Types of Indicator Placement:**

| Type | Where Drawn | Examples | What They Show |
|------|-------------|----------|----------------|
| **Overlay** | On the price chart | Moving Averages, Bollinger Bands, Fibonacci | Price levels, trend direction |
| **Oscillator** | Sub-panel below price | RSI, MACD, Stochastic | Momentum, overbought/oversold |
| **Volume-based** | Volume panel | OBV, Volume Profile, VWAP | Conviction, flow |

**Why Overlay Indicators on Price?**
```python
import mplfinance as mpf
import yfinance as yf

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31")

# Compute moving averages
sma20  = df['Close'].rolling(20).mean()
sma50  = df['Close'].rolling(50).mean()
sma200 = df['Close'].rolling(200).mean()

# Create overlay plots
overlays = [
    mpf.make_addplot(sma20,  color='#3498db', width=1.5, label='SMA 20'),
    mpf.make_addplot(sma50,  color='#f39c12', width=1.5, label='SMA 50'),
    mpf.make_addplot(sma200, color='#e74c3c', width=2.0, label='SMA 200'),
]

mpf.plot(df, type='candle', volume=True, addplot=overlays,
         style='nightclouds', title='AAPL with MA Overlays', figsize=(16,9))
```

**The Golden Rule of Indicators**: Use the minimum number of indicators needed to answer your specific question. Every additional line adds visual noise. Two indicators that confirm each other are more powerful than five that contradict each other.

---

## What Is a Moving Average? The Smoothing Intuition

**A moving average is a rolling window average that kills short-term noise and reveals long-term direction:**

**The Core Idea — Step by Step:**
```
Raw Close Prices:    [100, 102, 98, 105, 101, 107, 103, 108, 106, 112]

3-day SMA:
  Day 3:  (100 + 102 + 98)  / 3 = 100.0
  Day 4:  (102 + 98  + 105) / 3 = 101.7
  Day 5:  (98  + 105 + 101) / 3 = 101.3
  Day 6:  (105 + 101 + 107) / 3 = 104.3
  Day 7:  (101 + 107 + 103) / 3 = 103.7
  Day 8:  (107 + 103 + 108) / 3 = 106.0
  Day 9:  (103 + 108 + 106) / 3 = 105.7
  Day 10: (108 + 106 + 112) / 3 = 108.7

Raw prices oscillate ↑↓↑↓ (noisy)
SMA smoothly trends ↑    (signal revealed)
```

**Visualization Analogy:**
```
Raw price = driving on a bumpy road (every bump is visible)
SMA       = the road smoothed by GPS averaging (direction without bumps)
```

**The Lag Property — The Tradeoff:**
```
Short SMA (5-day):
  Responds quickly to price changes ← more reactive
  Generates many false signals       ← more noise

Long SMA (200-day):
  Responds slowly to price changes ← major trends only
  Rarely generates false signals    ← very little noise
  But is always late to the party  ← significant lag
```

**Key Insight**: There is no perfect moving average period. The choice always involves the responsiveness vs. noise tradeoff, and the "right" period depends on your trading time horizon.

---

## Simple Moving Average (SMA): Visualization and Code

**The SMA is the most fundamental trend indicator in all of technical analysis:**

**Formula:**
```
SMA(n) = (P₁ + P₂ + P₃ + ... + Pₙ) / n

Where P = closing price and n = number of periods
Each day gets equal weight: 1/n
```

**The Three Key SMAs and What Traders Watch:**

| SMA | Period | What It Shows | Typical Color |
|-----|--------|---------------|---------------|
| Short-term | 20-day | Recent momentum, tactical | Blue |
| Medium-term | 50-day | Intermediate trend | Orange |
| Long-term | 200-day | Major trend direction | Red |

**Complete Python Code:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

df = yf.download("AAPL", start="2023-01-01", end="2024-12-31")

# Calculate all three SMAs
df['SMA_20']  = df['Close'].rolling(window=20).mean()
df['SMA_50']  = df['Close'].rolling(window=50).mean()
df['SMA_200'] = df['Close'].rolling(window=200).mean()

# Plot
fig, ax = plt.subplots(figsize=(16, 7))
fig.set_facecolor('#1e1e1e')
ax.set_facecolor('#1e1e1e')

ax.plot(df.index, df['Close'],   color='white',   linewidth=0.8, label='Close Price', alpha=0.7)
ax.plot(df.index, df['SMA_20'],  color='#3498db', linewidth=1.5, label='SMA 20')
ax.plot(df.index, df['SMA_50'],  color='#f39c12', linewidth=1.5, label='SMA 50')
ax.plot(df.index, df['SMA_200'], color='#e74c3c', linewidth=2.0, label='SMA 200')

ax.set_title('AAPL – Three Moving Averages', color='white', fontsize=14, fontweight='bold')
ax.tick_params(colors='white')
ax.legend(facecolor='#2a2a2a', labelcolor='white', fontsize=11)
ax.grid(True, alpha=0.2, color='gray')
plt.tight_layout()
```

**Reading the Three MAs Together:**
```
Price > SMA20 > SMA50 > SMA200 → Perfect bull trend alignment
Price < SMA20 < SMA50 < SMA200 → Perfect bear trend alignment
MAs tangled/crossing each other → Sideways / no clear trend
```

---

## Exponential Moving Average (EMA): Weighting the Recent Past

**The EMA gives more weight to recent prices, making it more responsive than SMA:**

**How EMA Weighting Works (vs. SMA):**
```
SMA(10): Each of the 10 days gets weight = 10%
         10%, 10%, 10%, 10%, 10%, 10%, 10%, 10%, 10%, 10%

EMA(10): Recent days get more weight:
         Day 1 (today):  ~18.2%
         Day 2:          ~14.9%
         Day 3:          ~12.2%
         ...decreasing exponentially...
         Day 10:          ~3.2%
         (plus infinite tail of older prices)
```

**EMA Formula:**
```
Multiplier k = 2 / (n + 1)
EMA_today = (Close_today × k) + (EMA_yesterday × (1 - k))

For 12-day EMA: k = 2/(12+1) = 0.154
For 26-day EMA: k = 2/(26+1) = 0.074
```

**Python Code:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31")

# pandas ewm: span = period, adjust=False = recursive formula
df['EMA_12'] = df['Close'].ewm(span=12, adjust=False).mean()
df['EMA_26'] = df['Close'].ewm(span=26, adjust=False).mean()
df['SMA_20'] = df['Close'].rolling(20).mean()

fig, ax = plt.subplots(figsize=(16, 7))
fig.set_facecolor('#1e1e1e')
ax.set_facecolor('#1e1e1e')

ax.plot(df.index, df['Close'],  color='white',   linewidth=0.8, alpha=0.6, label='Close')
ax.plot(df.index, df['SMA_20'], color='#3498db', linewidth=1.5, linestyle='--', label='SMA 20 (lagging)')
ax.plot(df.index, df['EMA_12'], color='#f39c12', linewidth=1.8, label='EMA 12 (responsive)')

ax.set_title('EMA 12 vs SMA 20 — Responsiveness Comparison', color='white', fontsize=13)
ax.tick_params(colors='white')
ax.legend(facecolor='#2a2a2a', labelcolor='white')
ax.grid(True, alpha=0.2, color='gray')
plt.tight_layout()
```

**Visual Insight**: After a sharp price reversal, the EMA line turns faster than the SMA. On the chart, you'll see the EMA hugging price more tightly during trend changes, while the SMA lags behind for several days.

---

## SMA vs. EMA Side-by-Side: Which to Use?

**The choice between SMA and EMA is a visualization design decision:**

```
THREE MARKET CONDITIONS:

Condition 1 – STRONG UPTREND:
  SMA 20: ─────────────/
  EMA 12: ──────────────/  ← EMA slightly higher (more responsive)
  Both work well. EMA catches the trend slightly faster.

Condition 2 – CHOPPY / RANGING MARKET:
  Price:  ~~~~~~~~~~~~~~~~~~~~
  SMA 50: ────────── (flat, stays calm)
  EMA 12: ─/\──/\──/\── (whipsaws up and down with each wobble)
  SMA wins here — EMA generates too many false signals

Condition 3 – TREND REVERSAL:
  Price was rising, now drops sharply
  EMA turns down FIRST (more responsive) → earlier warning ✅
  SMA turns down LATER (more lag) → confirmation but late ⚠️
```

**Practical Decision Rule:**
```
Use EMA when:
  ✅ You want early signals
  ✅ Markets are trending (crypto, tech stocks in bull runs)
  ✅ Building MACD (which uses two EMAs)

Use SMA when:
  ✅ You want fewer false signals
  ✅ Markets are choppy or ranging
  ✅ The 200-day MA level (used by Wall Street as a key threshold)
```

**The Industry Standard:**
- 200-day SMA is used by nearly all professional traders as the major bull/bear dividing line
- 12 and 26-day EMAs are the inputs for MACD (the most popular momentum indicator)
- Neither is objectively "better" — context determines the right choice

---

## The Golden Cross and Death Cross

**The two most widely watched moving average signals in global financial markets:**

**Golden Cross:**
```
When the 50-day SMA crosses ABOVE the 200-day SMA:

200-day SMA ──────────────────────────────/─── ← 50-day
              ↑                          ↑
          both declining              50-day
                                      crosses
                                      above 200-day
                                      = GOLDEN CROSS 🌟

Signal: Potential shift from bear to bull market
Action: Long-biased traders pay attention
```

**Death Cross:**
```
When the 50-day SMA crosses BELOW the 200-day SMA:

50-day SMA ──────────────────────────────\─── ← 200-day
                                          ↓
                                      50-day crosses
                                      below 200-day
                                      = DEATH CROSS ☠️

Signal: Potential shift from bull to bear market
Action: Risk managers take defensive positions
```

**Python Code to Detect and Visualize:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

df = yf.download("SPY", start="2018-01-01", end="2024-12-31")
df['SMA_50']  = df['Close'].rolling(50).mean()
df['SMA_200'] = df['Close'].rolling(200).mean()

# Detect crosses
df['above'] = (df['SMA_50'] > df['SMA_200']).astype(int)
df['cross'] = df['above'].diff()

golden = df[df['cross'] ==  1].index  # SMA50 crossed above SMA200
death  = df[df['cross'] == -1].index  # SMA50 crossed below SMA200

fig, ax = plt.subplots(figsize=(18, 8))
fig.set_facecolor('#1e1e1e')
ax.set_facecolor('#1e1e1e')

ax.plot(df.index, df['Close'],   color='#aaa',    linewidth=0.8, alpha=0.7, label='SPY Close')
ax.plot(df.index, df['SMA_50'],  color='#3498db', linewidth=1.5, label='SMA 50')
ax.plot(df.index, df['SMA_200'], color='#e74c3c', linewidth=2.0, label='SMA 200')

# Mark crosses with vertical lines
for d in golden:
    ax.axvline(d, color='#26a69a', linewidth=2, alpha=0.8)
    ax.annotate('Golden\nCross', xy=(d, df.loc[d, 'SMA_200']),
                color='#26a69a', fontsize=8, ha='center')

for d in death:
    ax.axvline(d, color='#ef5350', linewidth=2, alpha=0.8)
    ax.annotate('Death\nCross', xy=(d, df.loc[d, 'SMA_200']),
                color='#ef5350', fontsize=8, ha='center')

ax.set_title('SPY – Golden Cross & Death Cross Signals (2018-2024)',
             color='white', fontsize=14, fontweight='bold')
ax.tick_params(colors='white')
ax.legend(facecolor='#2a2a2a', labelcolor='white')
ax.grid(True, alpha=0.2, color='gray')
```

---

## Weighted Moving Average (WMA): Linear Weighting

**WMA weights prices linearly — most recent period gets the highest weight:**

**How WMA Weighting Works:**
```
WMA(5) weights:
  Day 5 (today):   weight = 5  (highest)
  Day 4:           weight = 4
  Day 3:           weight = 3
  Day 2:           weight = 2
  Day 1 (oldest):  weight = 1  (lowest)
  Total:           15

WMA = (P₅×5 + P₄×4 + P₃×3 + P₂×2 + P₁×1) / 15
```

**Comparing MA Types on the Responsiveness Spectrum:**
```
← Less Responsive                    More Responsive →
SMA ──────────────── WMA ──────────── EMA
(equal weights)   (linear weights)  (exponential weights)
```

**Python Code:**
```python
def weighted_moving_average(series, n):
    weights = np.arange(1, n + 1, dtype=float)
    return series.rolling(n).apply(lambda x: np.dot(x, weights) / weights.sum(), raw=True)

df['WMA_20'] = weighted_moving_average(df['Close'], 20)
df['SMA_20'] = df['Close'].rolling(20).mean()
df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
```

**When to Use WMA**: Less common than SMA or EMA in practice, but useful when you want a middle ground. Some algorithmic trading strategies specifically use WMA to reduce whipsaws while maintaining more responsiveness than SMA.

---

## Volume Weighted Average Price (VWAP)

**VWAP is the most important intraday indicator used by institutional traders:**

**What VWAP Is:**
```
VWAP = Σ(Typical Price × Volume) / Σ(Volume)

Where: Typical Price = (High + Low + Close) / 3

VWAP resets to zero at the start of each trading day.
It represents the average price paid for ALL shares traded so far today,
weighted by how many shares traded at each price level.
```

**How Institutions Use VWAP:**
```
Institutional buyer wants to buy 1,000,000 shares of AAPL:
- They break it into small orders throughout the day
- Goal: Buy at or BELOW VWAP → they paid less than average → good execution
- If final avg cost > VWAP → they paid MORE than average → poor execution
- VWAP is the benchmark used to evaluate trader performance on Wall Street
```

**Python Code (Requires Intraday Data):**
```python
import pandas as pd
import matplotlib.pyplot as plt

def calculate_vwap(df):
    """Calculate VWAP — resets each day"""
    df = df.copy()
    df['Typical_Price'] = (df['High'] + df['Low'] + df['Close']) / 3
    df['TP_Vol'] = df['Typical_Price'] * df['Volume']
    # Group by date for daily reset
    df['Cumulative_TP_Vol'] = df.groupby(df.index.date)['TP_Vol'].cumsum()
    df['Cumulative_Vol']    = df.groupby(df.index.date)['Volume'].cumsum()
    df['VWAP'] = df['Cumulative_TP_Vol'] / df['Cumulative_Vol']
    return df['VWAP']

# Example with 5-minute AAPL data:
# df = yf.download("AAPL", interval="5m", period="5d")
# df['VWAP'] = calculate_vwap(df)
```

**Reading VWAP Visually:**
- Price consistently above VWAP → bullish intraday trend, buyers in control
- Price consistently below VWAP → bearish intraday trend, sellers in control
- Price oscillating around VWAP → balanced, no directional conviction

---

## MA Ribbons: Visualizing Multiple MAs Simultaneously

**An MA ribbon plots 6-12 moving averages on the same chart — the space between them tells the story:**

**How to Read an MA Ribbon:**
```
STRONG UPTREND:           WEAK/TRANSITIONING:        STRONG DOWNTREND:
  MA5    ─────/           MA5  ─\/─/─\/─              MA5   \────────
  MA10   ────/            MA10 ─/─\/─/─               MA10  ─\───────
  MA20  ────/             MA20 ────────  ← tangled     MA20  ──\──────
  MA50 ────/              MA50 ────────    together     MA50  ───\─────
  MA100────/                                            MA100 ────\────
  MA200────/                                            MA200 ─────\───

Ribbon spreading     Ribbon tangling      Ribbon spreading
apart UPWARD =       = consolidation,     apart DOWNWARD =
strong uptrend       uncertainty          strong downtrend
```

**Python Code:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

df = yf.download("AAPL", start="2023-01-01", end="2024-12-31")

periods = [5, 10, 20, 50, 100, 200]
colors  = ['#ff6b6b', '#ffa07a', '#ffd700', '#98fb98', '#87ceeb', '#9370db']

fig, ax = plt.subplots(figsize=(16, 8))
fig.set_facecolor('#1e1e1e')
ax.set_facecolor('#1e1e1e')

ax.fill_between(df.index,
    df['Close'].rolling(5).mean(),
    df['Close'].rolling(200).mean(),
    alpha=0.08, color='#26a69a', label='Ribbon zone')

for period, color in zip(periods, colors):
    ma = df['Close'].rolling(period).mean()
    ax.plot(df.index, ma, color=color, linewidth=1.0, label=f'MA {period}', alpha=0.8)

ax.plot(df.index, df['Close'], color='white', linewidth=0.6, alpha=0.5, label='Close')
ax.set_title('AAPL – Moving Average Ribbon', color='white', fontsize=14, fontweight='bold')
ax.tick_params(colors='white')
ax.legend(facecolor='#2a2a2a', labelcolor='white', ncol=4, fontsize=9)
ax.grid(True, alpha=0.15, color='gray')
plt.tight_layout()
```

---

## MA Envelope Bands: Dynamic Support and Resistance

**MA Envelopes add two percentage-offset bands around a moving average to create a dynamic channel:**

**Construction:**
```
Upper Band = SMA(n) × (1 + k%)
Middle Band = SMA(n)
Lower Band = SMA(n) × (1 - k%)

Common settings:
  SMA(20) ± 2.5%   → Short-term trading signals
  SMA(50) ± 5%     → Intermediate swing trading
  SMA(200) ± 10%   → Long-term trend channel
```

**Python Code:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31")

period = 20
k = 0.025  # 2.5%

df['MA']    = df['Close'].rolling(period).mean()
df['Upper'] = df['MA'] * (1 + k)
df['Lower'] = df['MA'] * (1 - k)

fig, ax = plt.subplots(figsize=(16, 7))
fig.set_facecolor('#1e1e1e')
ax.set_facecolor('#1e1e1e')

ax.plot(df.index, df['Close'], color='white', linewidth=0.8, alpha=0.7)
ax.plot(df.index, df['MA'],    color='#f0e68c', linewidth=1.5, label='SMA 20')
ax.plot(df.index, df['Upper'], color='#26a69a', linewidth=1.2, linestyle='--', label='Upper Band (+2.5%)')
ax.plot(df.index, df['Lower'], color='#ef5350', linewidth=1.2, linestyle='--', label='Lower Band (-2.5%)')
ax.fill_between(df.index, df['Upper'], df['Lower'], alpha=0.05, color='#26a69a')

ax.set_title('AAPL – MA Envelope Bands (SMA 20 ± 2.5%)',
             color='white', fontsize=13, fontweight='bold')
ax.tick_params(colors='white')
ax.legend(facecolor='#2a2a2a', labelcolor='white')
ax.grid(True, alpha=0.2, color='gray')
plt.tight_layout()
```

**Interpretation:**
- Price touching the upper band → potential short-term overbought condition
- Price touching the lower band → potential short-term oversold condition
- Note: MA envelopes differ from Bollinger Bands (which use std deviation instead of fixed %)

---

## Introduction to Fibonacci: The Golden Ratio in Markets

**Why do financial markets respect 23.6%, 38.2%, 50%, 61.8% levels?**

**The Fibonacci Sequence:**
```
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377 ...

Each number = sum of the two preceding numbers
```

**The Ratios That Traders Watch:**
```
Any number ÷ the next number  → converges to 0.618 (Golden Ratio reciprocal)
  89 ÷ 144 = 0.618
Any number ÷ the number 2 ahead → converges to 0.382
  55 ÷ 144 = 0.382
Any number ÷ the number 3 ahead → converges to 0.236
  34 ÷ 144 = 0.236
```

**Key Fibonacci Levels Used in Trading:**
```
23.6%  → Shallow retracement (strong trend)
38.2%  → Moderate retracement (healthy pullback)
50.0%  → Halfway point (not actually Fibonacci, but widely watched)
61.8%  → Deep retracement (weak trend but still intact)
78.6%  → Very deep retracement (trend in question)
100%   → Full retracement (trend reversed)
161.8% → Extension target level
261.8% → Deeper extension target
```

**Why Do Markets Respect These Levels?**
```
The honest answer: Because enough traders believe they will.

Fibonacci levels are a self-fulfilling prophecy:
1. Millions of traders watch the 61.8% retracement level
2. Many place buy orders there (expecting a bounce)
3. When price reaches that level, buy orders activate
4. Price does bounce → traders "confirm" Fibonacci works
5. More traders learn about it → more orders → stronger levels
```

**The Visualization Insight**: Fibonacci levels work as psychological price magnets. The more market participants are aware of them, the stronger the effect.

---

## Fibonacci Retracement: Drawing Levels on a Price Chart

**Fibonacci retracement is drawn between a significant swing HIGH and swing LOW:**

**Construction Rules:**
```
In an UPTREND (measuring a pullback from a high):
  1. Identify the swing LOW (recent bottom)
  2. Identify the swing HIGH (recent top)
  3. Draw horizontal lines at:
     → 23.6% of the distance from Low to High, measured from High
     → 38.2%
     → 50.0%
     → 61.8%
     → 78.6%

Price FALLING from the HIGH toward these levels?
Each Fibonacci level is a potential SUPPORT zone where buying may emerge.
```

**Python Code:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31")

# Define the swing points manually (or detect algorithmically)
swing_low  = df['Close'].min()  # Simplified: use actual low date
swing_high = df['Close'].max()  # Simplified: use actual high date

fib_ratios = [0.0, 0.236, 0.382, 0.5, 0.618, 0.786, 1.0]
fib_levels = {r: swing_high - (swing_high - swing_low) * r for r in fib_ratios}

fib_colors = {
    0.0:   '#26a69a',
    0.236: '#3498db',
    0.382: '#f0e68c',
    0.5:   '#ffffff',
    0.618: '#f39c12',
    0.786: '#e74c3c',
    1.0:   '#9b59b6'
}

fig, ax = plt.subplots(figsize=(16, 8))
fig.set_facecolor('#1e1e1e')
ax.set_facecolor('#1e1e1e')

ax.plot(df.index, df['Close'], color='white', linewidth=1.0, label='AAPL Close')

for ratio, level in fib_levels.items():
    color = fib_colors[ratio]
    ax.axhline(y=level, color=color, linewidth=1.5,
               linestyle='--' if ratio not in [0.0, 1.0] else '-')
    ax.text(df.index[-1], level, f'  {ratio:.1%} — ${level:.2f}',
            color=color, fontsize=9, va='center')

# Shade the 38.2%–61.8% "golden zone"
ax.fill_between(df.index,
    fib_levels[0.382], fib_levels[0.618],
    alpha=0.08, color='#f39c12', label='Golden Zone (38.2% – 61.8%)')

ax.set_title('AAPL – Fibonacci Retracement Levels', color='white',
             fontsize=14, fontweight='bold')
ax.tick_params(colors='white')
ax.legend(facecolor='#2a2a2a', labelcolor='white')
ax.grid(True, alpha=0.2, color='gray')
plt.tight_layout()
```

**The "Golden Zone" (38.2% to 61.8%)**: This range between the two most watched Fibonacci ratios is where the majority of healthy pullbacks end in strong uptrends. Price entering this zone while the overall trend is up is considered a high-probability entry area by many technical analysts.

---

## Fibonacci Extension: Projecting Price Targets

**Fibonacci extensions project ABOVE the swing high (in uptrends) to identify profit targets:**

**Extension Levels:**
```
After price retraces and bounces from a Fibonacci level,
extensions tell you WHERE price might travel next:

  127.2%  → First extension target (conservative)
  161.8%  → Golden ratio extension (most watched)
  200.0%  → Double the original move
  261.8%  → Major extension target

Construction:
  1. Swing Low (A)
  2. Swing High (B) — the measured move
  3. Pullback Low (C) — where price retraced to
  4. Extensions projected UP from A-B-C geometry
```

**Python Code:**
```python
# Extension levels calculated from A, B, C points
swing_low_A  = 150.0   # The starting low
swing_high_B = 200.0   # The peak
pullback_C   = 175.0   # Where price pulled back to

move_AB = swing_high_B - swing_low_A  # = 50.0

extension_levels = {
    '127.2%': pullback_C + move_AB * 1.272,
    '161.8%': pullback_C + move_AB * 1.618,
    '200.0%': pullback_C + move_AB * 2.000,
    '261.8%': pullback_C + move_AB * 2.618
}

print("Fibonacci Extension Targets:")
for label, level in extension_levels.items():
    print(f"  {label}: ${level:.2f}")
```

**Visual Distinction from Retracements:**
- Retracement levels are BETWEEN the swing low and high (pullback zones)
- Extension levels are BEYOND the swing high (profit targets)
- Both are drawn as horizontal lines — color-coded differently to avoid confusion

---

## Visualizing Fibonacci Levels in Python

**Complete, professional Fibonacci chart with retracements and extensions:**

```python
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import yfinance as yf
import numpy as np

def draw_fibonacci_chart(ticker, start, end, swing_low_date, swing_high_date):
    df = yf.download(ticker, start=start, end=end)

    swing_low  = float(df.loc[swing_low_date:swing_low_date, 'Close'].iloc[0])
    swing_high = float(df.loc[swing_high_date:swing_high_date, 'Close'].iloc[0])

    # Retracement levels (between Low and High)
    retrace = {
        '0%':    swing_high,
        '23.6%': swing_high - (swing_high - swing_low) * 0.236,
        '38.2%': swing_high - (swing_high - swing_low) * 0.382,
        '50.0%': swing_high - (swing_high - swing_low) * 0.500,
        '61.8%': swing_high - (swing_high - swing_low) * 0.618,
        '100%':  swing_low
    }

    fig, ax = plt.subplots(figsize=(16, 9))
    fig.set_facecolor('#1e1e1e')
    ax.set_facecolor('#1e1e1e')

    # Price line
    ax.plot(df.index, df['Close'], color='white', linewidth=1.2, zorder=5)

    # Shade zones between Fibonacci levels
    level_list = sorted(retrace.values())
    zone_colors = ['#26a69a20', '#3498db20', '#f0e68c30', '#f39c1225', '#e74c3c20']
    for i in range(len(level_list) - 1):
        ax.fill_between(df.index, level_list[i], level_list[i+1],
                        alpha=0.15, color=zone_colors[i % len(zone_colors)])

    # Draw horizontal lines
    colors = ['#26a69a', '#3498db', '#f0e68c', 'white', '#f39c12', '#9b59b6']
    for (label, level), color in zip(retrace.items(), colors):
        ax.axhline(y=level, color=color, linewidth=1.5, linestyle='--', alpha=0.9)
        ax.text(df.index[5], level + (swing_high - swing_low) * 0.005,
                f'{label}  ${level:.2f}', color=color, fontsize=9, fontweight='bold')

    ax.set_title(f'{ticker} – Fibonacci Retracement Levels\nSwing: ${swing_low:.2f} → ${swing_high:.2f}',
                 color='white', fontsize=13, fontweight='bold')
    ax.tick_params(colors='white')
    ax.grid(True, alpha=0.15, color='gray')
    plt.tight_layout()
    return fig

# Usage:
fig = draw_fibonacci_chart("AAPL", "2024-01-01", "2024-12-31",
                           "2024-01-22", "2024-07-15")
plt.show()
```

---

## Fibonacci Fan Lines: Diagonal Levels

**Fibonacci Fan Lines are diagonal support/resistance lines that incorporate both price AND time:**

**Construction:**
```
1. Draw from a swing LOW (or HIGH) as the anchor point
2. Draw a vertical line at a key future date
3. Divide that vertical line at Fibonacci ratios (38.2%, 50%, 61.8%)
4. Connect each division point back to the anchor point
→ These diagonal lines represent time-adjusted support/resistance
```

**Why Fan Lines Are Different:**
```
Horizontal Fib levels:  ─────────────────  constant price, any time
Fan lines:              /  /  /  diverging at angles from the anchor

Fan lines are dynamic: the same level is at a DIFFERENT price
on Monday vs. Friday, because the line is diagonal.

This makes them time-sensitive: a stock that rallied quickly
has steeper fan lines; a slow rally has shallower fans.
```

**Python Code:**
```python
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
from matplotlib.lines import Line2D

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31")

fig, ax = plt.subplots(figsize=(16, 7))
fig.set_facecolor('#1e1e1e')
ax.set_facecolor('#1e1e1e')

ax.plot(df.index, df['Close'], color='white', linewidth=1.0, alpha=0.8)

# Anchor: the swing low
anchor_idx = df['Close'].idxmin()
anchor_val = df.loc[anchor_idx, 'Close']
anchor_pos = df.index.get_loc(anchor_idx)

# End point (last date), vertical extent to swing high
end_val = df['Close'].max()

fib_fans = [0.382, 0.5, 0.618]
fan_colors = ['#26a69a', '#f0e68c', '#f39c12']

for ratio, color in zip(fib_fans, fan_colors):
    end_y = anchor_val + (end_val - anchor_val) * ratio
    ax.plot([anchor_idx, df.index[-1]], [anchor_val, end_y],
            color=color, linewidth=1.5, linestyle='-',
            label=f'Fan {ratio:.1%}', alpha=0.85)

ax.scatter([anchor_idx], [anchor_val], color='#ef5350', s=100, zorder=6, label='Anchor (swing low)')
ax.set_title('AAPL – Fibonacci Fan Lines', color='white', fontsize=13, fontweight='bold')
ax.tick_params(colors='white')
ax.legend(facecolor='#2a2a2a', labelcolor='white')
ax.grid(True, alpha=0.2, color='gray')
plt.tight_layout()
```

---

## Fibonacci Time Zones: When Price Might Turn

**Fibonacci Time Zones project WHEN future turning points might occur:**

**Construction:**
```
1. Mark a significant swing point (low or high) as Day 0
2. Count forward in Fibonacci intervals: 1, 2, 3, 5, 8, 13, 21, 34, 55...
3. Draw vertical lines at each Fibonacci-numbered day
→ These vertical lines mark potential future turning points
```

**Visual Appearance:**
```
    ↓        ↓      ↓    ↓   ↓  ↓ ↓ ↓
    │        │      │    │   │  │ │ │
    1        2      3    5   8  13 21 34  ← Time zones
    day      days   days days ...
    (sparse early, dense later)
```

**Python Code:**
```python
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31")
df = df.reset_index()

fig, ax = plt.subplots(figsize=(16, 7))
fig.set_facecolor('#1e1e1e')
ax.set_facecolor('#1e1e1e')

ax.plot(df['Date'], df['Close'], color='white', linewidth=1.0, alpha=0.8)

# Start from the first major low
anchor_row = df['Close'].idxmin()
fib_nums = [1, 2, 3, 5, 8, 13, 21, 34, 55]

for i, fib in enumerate(fib_nums):
    zone_idx = anchor_row + fib
    if zone_idx < len(df):
        zone_date = df.loc[zone_idx, 'Date']
        alpha = 0.8 if i < 5 else 0.4
        ax.axvline(zone_date, color='#f0e68c', linewidth=1.0,
                   linestyle='--', alpha=alpha)
        ax.text(zone_date, df['Close'].max() * 0.98,
                str(fib), color='#f0e68c', fontsize=8, ha='center')

ax.set_title('AAPL – Fibonacci Time Zones', color='white', fontsize=13, fontweight='bold')
ax.tick_params(colors='white')
ax.grid(True, alpha=0.2, color='gray')
plt.tight_layout()
```

---

## MA Crossover Strategy: Full Visualization with Entry/Exit Signals

**Turning a visual pattern (MA crossover) into a systematic, visualized trading strategy:**

**Strategy Rules:**
```
BUY  when: SMA_20 crosses ABOVE SMA_50 (and close above SMA_200)
SELL when: SMA_20 crosses BELOW SMA_50

Entry = next open after the crossover candle
Exit  = next open after the death crossover
```

**Complete Python Implementation:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import yfinance as yf
import numpy as np

df = yf.download("AAPL", start="2022-01-01", end="2024-12-31")

df['SMA_20']  = df['Close'].rolling(20).mean()
df['SMA_50']  = df['Close'].rolling(50).mean()
df['SMA_200'] = df['Close'].rolling(200).mean()

# Detect crossovers
df['signal'] = 0
df.loc[df['SMA_20'] > df['SMA_50'], 'signal'] = 1   # Bullish alignment
df['crossover'] = df['signal'].diff()

buys  = df[df['crossover'] ==  1]
sells = df[df['crossover'] == -1]

fig, ax = plt.subplots(figsize=(18, 8))
fig.set_facecolor('#1e1e1e')
ax.set_facecolor('#1e1e1e')

ax.plot(df.index, df['Close'],   color='white',   linewidth=0.8, alpha=0.6)
ax.plot(df.index, df['SMA_20'],  color='#3498db', linewidth=1.5, label='SMA 20')
ax.plot(df.index, df['SMA_50'],  color='#f39c12', linewidth=1.5, label='SMA 50')
ax.plot(df.index, df['SMA_200'], color='#e74c3c', linewidth=2.0, label='SMA 200')

# Buy signals: green up arrows
ax.scatter(buys.index, buys['SMA_20'] * 0.97, marker='^', color='#26a69a',
           s=150, zorder=5, label='BUY Signal')

# Sell signals: red down arrows
ax.scatter(sells.index, sells['SMA_20'] * 1.03, marker='v', color='#ef5350',
           s=150, zorder=5, label='SELL Signal')

ax.set_title('AAPL – MA Crossover Strategy (SMA 20/50 with SMA 200 filter)',
             color='white', fontsize=13, fontweight='bold')
ax.tick_params(colors='white')
ax.legend(facecolor='#2a2a2a', labelcolor='white', fontsize=10)
ax.grid(True, alpha=0.2, color='gray')
plt.tight_layout()
```

---

## Combining Fibonacci with Moving Averages: Confluence Zones

**When a Fibonacci level and a moving average coincide — that is a confluence zone:**

**Why Confluence Matters:**
```
Single Fibonacci level:  Moderate support
  → 1 reason to buy here

Single Moving Average:   Moderate support
  → 1 reason to buy here

Fibonacci + SMA at the same price:  STRONG support
  → 2 independent indicators agree = confluence
  → More traders watching = more orders at that level
  → Higher probability of a price bounce
```

**Visual Representation:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31")

swing_low  = df['Close'].min()
swing_high = df['Close'].max()

fib_618 = swing_high - (swing_high - swing_low) * 0.618
sma_200 = df['Close'].rolling(200).mean().iloc[-1]

# Highlight confluence zone (where Fib and MA are close)
confluence_price = (fib_618 + sma_200) / 2
tolerance = (swing_high - swing_low) * 0.02  # 2% tolerance band

fig, ax = plt.subplots(figsize=(16, 8))
fig.set_facecolor('#1e1e1e')
ax.set_facecolor('#1e1e1e')

ax.plot(df.index, df['Close'], color='white', linewidth=0.8, alpha=0.7)
ax.plot(df.index, df['Close'].rolling(200).mean(),
        color='#e74c3c', linewidth=2.0, label='SMA 200')
ax.axhline(fib_618, color='#f39c12', linewidth=1.5, linestyle='--',
           label=f'Fib 61.8% — ${fib_618:.2f}')

# Mark the confluence band
ax.axhspan(confluence_price - tolerance, confluence_price + tolerance,
           alpha=0.2, color='#f0e68c', label='CONFLUENCE ZONE')

ax.set_title('AAPL – Fibonacci + SMA Confluence Zone', color='white',
             fontsize=13, fontweight='bold')
ax.tick_params(colors='white')
ax.legend(facecolor='#2a2a2a', labelcolor='white')
ax.grid(True, alpha=0.2, color='gray')
plt.tight_layout()
```

---

## Critique: When Moving Averages Mislead

**Moving averages have a serious weakness in ranging (non-trending) markets:**

**The Whipsaw Problem:**
```
TRENDING MARKET (MAs work great):
  Price moves in a clear direction
  MA crossovers align with the actual trend
  Result: Few signals, most profitable

RANGING MARKET (MAs fail):
  Price moves sideways between support and resistance
  Price repeatedly crosses above/below the MA
  Each cross generates a buy or sell signal
  All signals are FALSE (price was never trending)
  Result: Frequent signals, all losing
```

**Visual Diagnosis:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Deliberately choose a sideways-moving period
df_trending = yf.download("NVDA", start="2023-01-01", end="2023-06-30")  # Strong uptrend
df_ranging  = yf.download("NVDA", start="2022-01-01", end="2022-06-30")  # Ranging market

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))
fig.set_facecolor('#1e1e1e')

for ax, df, title in [
    (ax1, df_trending, "Trending Market — MAs Work Well"),
    (ax2, df_ranging,  "Ranging Market — MAs Generate Whipsaws")
]:
    ax.set_facecolor('#1e1e1e')
    sma20 = df['Close'].rolling(20).mean()
    sma50 = df['Close'].rolling(50).mean()
    ax.plot(df.index, df['Close'], color='white', linewidth=0.8, alpha=0.7)
    ax.plot(df.index, sma20, color='#3498db', linewidth=1.5, label='SMA 20')
    ax.plot(df.index, sma50, color='#f39c12', linewidth=1.5, label='SMA 50')
    ax.set_title(title, color='white', fontsize=11, fontweight='bold')
    ax.tick_params(colors='white')
    ax.legend(facecolor='#2a2a2a', labelcolor='white', fontsize=9)
    ax.grid(True, alpha=0.2, color='gray')

plt.suptitle('MA Performance: Trending vs. Ranging Markets', color='white',
             fontsize=14, fontweight='bold')
plt.tight_layout()
```

**The Fix**: Before applying MA signals, visually check if the market is trending (ADX > 25) or ranging. In ranging markets, use oscillators (RSI, Stochastic) instead of trend-following MAs.

---

## Part 2 Summary & Preview of Part 3

**What You Learned in Part 2 — Smoothing and Structure:**

| Concept | Key Visual Takeaway |
|---------|---------------------|
| SMA | Rolling average line, equal weighting, 20/50/200-day are key |
| EMA | More responsive to recent price, hugs price tighter |
| Golden/Death Cross | 50-day vs 200-day MA crossover — market-wide signal |
| WMA | Linear weighting between SMA and EMA responsiveness |
| VWAP | Intraday average weighted by volume — institutional benchmark |
| MA Ribbon | Multiple MAs simultaneously — spread = trend strength |
| Fibonacci Retracement | Horizontal levels where pullbacks tend to find support |
| Fibonacci Extension | Target levels beyond the swing high |
| Fibonacci Fan/Time | Diagonal and vertical temporal Fibonacci tools |
| Confluence Zones | Where multiple indicators agree — highest probability |
| MA Whipsaws | Why MAs fail in ranging markets |

**Preview of Part 3 — Momentum and Volatility:**

In Part 3, we move BELOW the price chart to the indicator sub-panels:

- 📊 **RSI** — The 0-100 momentum speedometer
- 📉 **MACD** — Two moving averages minus each other, made visual
- 🎀 **Bollinger Bands** — Dynamic volatility channel on the price chart
- ⚡ **Stochastic Oscillator** — Where did price close within its recent range?
- 📏 **Average True Range (ATR)** — Measuring volatility without direction
- 📦 **Volume Profile** — The horizontal histogram showing where volume clusters

> "In an uptrend, Fibonacci retracement levels show you where to BUY the dip. The moving average tells you the dip is over. Together, they tell you where AND when." — Technical Analysis Practicum
