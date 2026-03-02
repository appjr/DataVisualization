# Class X – Part 3

[← Main](Classx.md) | [Part 1](Classx_Part1.md) | [Part 2](Classx_Part2.md) | [Part 3](Classx_Part3.md) | [Part 4](Classx_Part4.md)

---

# PART 3: MOMENTUM & VOLATILITY INDICATORS
# Slides 41–60
# ═══════════════════════════════════════════════════════════════

---

## The Multi-Panel Chart Architecture

**Professional trading charts are multi-panel structures — each panel answers a different question:**

**Standard Multi-Panel Layout:**
```
┌────────────────────────────────────────────────────────┐
│  PRICE PANEL (60% of height)                           │
│  Candlesticks + MA overlays + Bollinger Bands          │
│  Question: "What direction is price moving?"           │
├────────────────────────────────────────────────────────┤
│  VOLUME PANEL (15% of height)                          │
│  Color-coded histogram                                  │
│  Question: "How much conviction is behind the move?"   │
├────────────────────────────────────────────────────────┤
│  RSI PANEL (12.5% of height)                           │
│  Oscillator 0-100 with overbought/oversold zones       │
│  Question: "Is price stretched too far too fast?"      │
├────────────────────────────────────────────────────────┤
│  MACD PANEL (12.5% of height)                          │
│  MACD line, Signal line, Histogram bars                │
│  Question: "Is momentum accelerating or fading?"       │
└────────────────────────────────────────────────────────┘
```

**Building the Layout with matplotlib GridSpec:**
```python
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
import yfinance as yf

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31")

fig = plt.figure(figsize=(18, 12))
fig.set_facecolor('#1e1e1e')

# GridSpec: 4 rows, height ratios
gs = gridspec.GridSpec(4, 1,
    height_ratios=[5, 1.5, 1.5, 1.5],
    hspace=0.05)

ax_price  = fig.add_subplot(gs[0])
ax_volume = fig.add_subplot(gs[1], sharex=ax_price)
ax_rsi    = fig.add_subplot(gs[2], sharex=ax_price)
ax_macd   = fig.add_subplot(gs[3], sharex=ax_price)

for ax in [ax_price, ax_volume, ax_rsi, ax_macd]:
    ax.set_facecolor('#1e1e1e')
    ax.tick_params(colors='white', labelsize=8)
    ax.grid(True, alpha=0.15, color='gray')
    ax.spines['bottom'].set_color('#333')
    ax.spines['top'].set_color('#333')
    ax.spines['left'].set_color('#333')
    ax.spines['right'].set_color('#333')

# Hide x-tick labels except the bottom panel
plt.setp(ax_price.get_xticklabels(), visible=False)
plt.setp(ax_volume.get_xticklabels(), visible=False)
plt.setp(ax_rsi.get_xticklabels(), visible=False)

print("Multi-panel framework ready — add indicators to each axis")
```

**Key Design Principles:**
- All panels share the same x-axis (`sharex=ax_price`) — zoom applies to all simultaneously
- The price panel is tallest — it's the primary visual focus
- Each sub-panel has its own y-axis scale (RSI is 0-100, MACD is in price units)
- Hide x-tick labels on all but the bottom panel to avoid visual clutter

---

## Relative Strength Index (RSI): The Momentum Oscillator

**RSI is a 0-100 speedometer for price momentum — the single most widely used oscillator in trading:**

**What RSI Measures:**
```
RSI answers: "How fast and how much has price been rising vs. falling?"

RSI = 100                 → Price going UP every single day (theoretical maximum)
RSI = 70                  → Traditional OVERBOUGHT threshold (price rose too fast)
RSI = 50                  → Neutral zone (equal buying and selling pressure)
RSI = 30                  → Traditional OVERSOLD threshold (price fell too fast)
RSI = 0                   → Price going DOWN every single day (theoretical minimum)
```

**Visual Layout of RSI Panel:**
```
100 ─────────────────────────────────────────────────────
 80 ─
 70 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  OVERBOUGHT line
     ████ OVERBOUGHT ZONE (shaded red)
     RSI line oscillates ────/\────/\────
     ████ OVERSOLD ZONE (shaded green)
 30 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  OVERSOLD line
 20 ─
  0 ─────────────────────────────────────────────────────
```

**Python Code:**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def calculate_rsi(prices, period=14):
    delta = prices.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(com=period - 1, min_periods=period).mean()
    avg_loss = loss.ewm(com=period - 1, min_periods=period).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31")
df['RSI'] = calculate_rsi(df['Close'])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 9), sharex=True,
                                gridspec_kw={'height_ratios': [3, 1]})
fig.set_facecolor('#1e1e1e')

# Price panel
ax1.set_facecolor('#1e1e1e')
ax1.plot(df.index, df['Close'], color='white', linewidth=1.0)
ax1.set_title('AAPL – Price + RSI (14)', color='white', fontsize=13, fontweight='bold')
ax1.tick_params(colors='white')
ax1.grid(True, alpha=0.15, color='gray')

# RSI panel
ax2.set_facecolor('#1e1e1e')
ax2.plot(df.index, df['RSI'], color='#9b59b6', linewidth=1.5, label='RSI 14')
ax2.axhline(70, color='#ef5350', linewidth=1.0, linestyle='--', label='Overbought (70)')
ax2.axhline(30, color='#26a69a', linewidth=1.0, linestyle='--', label='Oversold (30)')
ax2.axhline(50, color='gray',    linewidth=0.8, linestyle=':', alpha=0.5)
ax2.fill_between(df.index, df['RSI'], 70, where=(df['RSI'] >= 70), alpha=0.25, color='#ef5350')
ax2.fill_between(df.index, df['RSI'], 30, where=(df['RSI'] <= 30), alpha=0.25, color='#26a69a')
ax2.set_ylim(0, 100)
ax2.tick_params(colors='white')
ax2.legend(facecolor='#2a2a2a', labelcolor='white', fontsize=9)
ax2.grid(True, alpha=0.15, color='gray')

plt.tight_layout()
```

---

## RSI Calculation and Visual Interpretation

**Understanding what the RSI formula produces helps you read the chart intuitively:**

**Step-by-Step Calculation (14-day period):**
```
Day | Close | Change | Gain  | Loss
----|-------|--------|-------|------
  1 | 150.0 |   —    |   —   |   —
  2 | 152.0 |  +2.0  |  2.0  |  0.0
  3 | 148.0 |  -4.0  |  0.0  |  4.0
  4 | 153.0 |  +5.0  |  5.0  |  0.0
  5 | 151.0 |  -2.0  |  0.0  |  2.0
  ...continuing for 14 days...

Average Gain (14 days) = sum(gains) / 14 = e.g. 2.14
Average Loss (14 days) = sum(losses) / 14 = e.g. 0.86

RS = Average Gain / Average Loss = 2.14 / 0.86 = 2.49
RSI = 100 - (100 / (1 + RS)) = 100 - (100 / 3.49) = 100 - 28.65 = 71.35
```

**What RSI Values Mean Visually:**

| RSI Range | Color Zone | Market Condition |
|-----------|------------|-----------------|
| 70 – 100 | Red shading | Overbought — rally may be extended |
| 50 – 70 | Neutral | Bullish momentum, not extreme |
| 50 | Center line | Equal buyers and sellers |
| 30 – 50 | Neutral | Bearish momentum, not extreme |
| 0 – 30 | Green shading | Oversold — decline may be extended |

**The 50 Centerline — Often Overlooked:**
```
RSI staying above 50 throughout a pullback:
→ Bullish — buyers defending the mid-level → strong uptrend intact

RSI staying below 50 during a rally:
→ Bearish — bears defending the mid-level → still in a downtrend
```

**Important Caveat**: In a strong uptrend, RSI can stay in the 60-80 range for months. A reading of 70+ is NOT automatically a sell signal — it just means momentum is elevated. Always combine with price context.

---

## RSI Divergence: The Most Powerful RSI Signal

**Divergence occurs when RSI and price move in opposite directions — an early warning of trend exhaustion:**

**Bearish Divergence:**
```
Price Chart:           RSI Panel:

  B           ← Higher High    RSI(B)  ← Lower High (RSI)
 /                              /
A         Price makes          A  RSI fails to confirm
           higher high          the new price high

Signal: Momentum is WEAKENING even as price rises
        → Possible trend reversal ahead
```

**Bullish Divergence:**
```
Price Chart:           RSI Panel:

A         Price makes    A  RSI stays
 \         lower low     \   higher
  B           ← Lower Low  RSI(B) ← Higher Low (RSI)

Signal: Momentum is STRENGTHENING even as price falls
        → Possible trend reversal ahead (to the upside)
```

**Python Code to Detect and Annotate Divergence:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

def calculate_rsi(prices, period=14):
    delta = prices.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(com=period - 1, min_periods=period).mean()
    avg_loss = loss.ewm(com=period - 1, min_periods=period).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31")
df['RSI'] = calculate_rsi(df['Close'])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 9), sharex=True,
                                gridspec_kw={'height_ratios': [3, 1]})
fig.set_facecolor('#1e1e1e')

for ax in [ax1, ax2]:
    ax.set_facecolor('#1e1e1e')
    ax.tick_params(colors='white')
    ax.grid(True, alpha=0.15, color='gray')

ax1.plot(df.index, df['Close'], color='white', linewidth=1.0)
ax2.plot(df.index, df['RSI'],   color='#9b59b6', linewidth=1.5)
ax2.axhline(70, color='#ef5350', linewidth=1.0, linestyle='--')
ax2.axhline(30, color='#26a69a', linewidth=1.0, linestyle='--')
ax2.set_ylim(0, 100)

# Manually annotate bearish divergence (example)
# Point A: price high with high RSI
# Point B: higher price high but lower RSI → bearish divergence
# Add annotations:
ax1.annotate('', xy=(df.index[200], df['Close'].iloc[200]),
             xytext=(df.index[150], df['Close'].iloc[150]),
             arrowprops=dict(arrowstyle='->', color='#ef5350', lw=1.5))
ax1.text(df.index[180], df['Close'].max() * 0.99,
         'Bearish Divergence\n(price higher, RSI lower)',
         color='#ef5350', fontsize=9)

ax1.set_title('AAPL – RSI Divergence Example', color='white', fontsize=13, fontweight='bold')
plt.tight_layout()
```

---

## MACD: Moving Average Convergence/Divergence

**MACD visualizes the relationship between two moving averages as a momentum oscillator:**

**MACD Components — Three Visual Elements in One Panel:**
```
┌────────────────────────────────────────────────────────┐
│                                                        │
│  MACD Line ───/────╲──/──── (blue line)               │
│  Signal Line ──/────╲─/──── (orange line)             │
│  Histogram  ████░░░░████    (green = above, red below) │
│             ████░░░░████                               │
│  ─ ─ ─ ─ ─ ─ Zero Line ─ ─ ─ ─ ─ ─ ─ ─ ─             │
│             ░░░░████░░░░                               │
└────────────────────────────────────────────────────────┘
```

**The Math Behind MACD:**
```
MACD Line    = EMA(12) - EMA(26)
Signal Line  = EMA(9) of the MACD Line
Histogram    = MACD Line - Signal Line
```

**Python Code:**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def calculate_macd(prices, fast=12, slow=26, signal=9):
    ema_fast   = prices.ewm(span=fast,   adjust=False).mean()
    ema_slow   = prices.ewm(span=slow,   adjust=False).mean()
    macd_line  = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()
    histogram  = macd_line - signal_line
    return macd_line, signal_line, histogram

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31")
macd, signal_line, histogram = calculate_macd(df['Close'])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 9), sharex=True,
                                gridspec_kw={'height_ratios': [3, 1.5]})
fig.set_facecolor('#1e1e1e')

ax1.set_facecolor('#1e1e1e')
ax1.plot(df.index, df['Close'], color='white', linewidth=1.0)
ax1.set_title('AAPL – Price + MACD', color='white', fontsize=13, fontweight='bold')
ax1.tick_params(colors='white')
ax1.grid(True, alpha=0.15, color='gray')

ax2.set_facecolor('#1e1e1e')
# Histogram: green when positive, red when negative
colors_hist = ['#26a69a' if v >= 0 else '#ef5350' for v in histogram]
ax2.bar(df.index, histogram, color=colors_hist, alpha=0.7, width=0.8, label='Histogram')
ax2.plot(df.index, macd,        color='#3498db', linewidth=1.5, label='MACD Line')
ax2.plot(df.index, signal_line, color='#f39c12', linewidth=1.5, label='Signal Line')
ax2.axhline(0, color='gray', linewidth=0.8, linestyle='--')
ax2.tick_params(colors='white')
ax2.legend(facecolor='#2a2a2a', labelcolor='white', fontsize=9)
ax2.grid(True, alpha=0.15, color='gray')

plt.tight_layout()
```

---

## MACD Crossover Signals: Visualizing Buy and Sell Triggers

**MACD crossovers are the most watched momentum signals in all of technical analysis:**

**Bullish MACD Crossover:**
```
MACD Panel:              Price Panel:

Signal ─\─               Price
         ╲               continues
MACD ─────╲/─ ←          to rally
           ↑
   MACD crosses ABOVE Signal Line
   → Bullish crossover signal
   → Green vertical line on chart
   → Green buy arrow on price panel
```

**Bearish MACD Crossover:**
```
MACD Panel:              Price Panel:

MACD ─────╲───           Price
           ╲             begins
Signal ─────╲/─ ←         to decline
             ↑
   MACD crosses BELOW Signal Line
   → Bearish crossover signal
   → Red vertical line on chart
   → Red sell arrow on price panel
```

**Python Code:**
```python
# Detect MACD crossovers and plot with synchronized price panel
df['MACD'], df['Signal'], df['Hist'] = calculate_macd(df['Close'])

df['macd_above'] = (df['MACD'] > df['Signal']).astype(int)
df['macd_cross'] = df['macd_above'].diff()

bullish_cross = df[df['macd_cross'] ==  1]  # MACD crossed above Signal
bearish_cross = df[df['macd_cross'] == -1]  # MACD crossed below Signal

# On the price panel: mark entry/exit points
ax1.scatter(bullish_cross.index, bullish_cross['Close'] * 0.98,
            marker='^', color='#26a69a', s=120, zorder=5, label='MACD Buy')
ax1.scatter(bearish_cross.index, bearish_cross['Close'] * 1.02,
            marker='v', color='#ef5350', s=120, zorder=5, label='MACD Sell')

# On the MACD panel: vertical lines at crossovers
for d in bullish_cross.index:
    ax2.axvline(d, color='#26a69a', linewidth=1.0, alpha=0.6)
for d in bearish_cross.index:
    ax2.axvline(d, color='#ef5350', linewidth=1.0, alpha=0.6)
```

---

## MACD Histogram: Visualizing Momentum Acceleration

**The MACD histogram is the most sensitive component — it shows momentum BEFORE the crossover:**

**Reading Histogram Direction:**
```
Histogram BAR HEIGHT = MACD Line - Signal Line

When bars are GREEN and GROWING:    Momentum accelerating upward
When bars are GREEN and SHRINKING:  Momentum decelerating (crossover coming?)
When bars cross zero to RED:        Bearish crossover just happened
When bars are RED and GROWING:      Momentum accelerating downward
When bars are RED and SHRINKING:    Bearish momentum fading (crossover coming?)
When bars cross zero to GREEN:      Bullish crossover just happened
```

**The Early Warning Signal:**
```
Price is still rising...
MACD line is still above Signal line...
But histogram bars are SHRINKING...

This shrinking histogram is an EARLY WARNING
that momentum is fading BEFORE the crossover.

Advanced traders use this to take partial profits
before the full signal appears.
```

**Python Visualization of Histogram Divergence:**
```python
import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 9), sharex=True,
                                gridspec_kw={'height_ratios': [3, 1.5]})
fig.set_facecolor('#1e1e1e')

# Color gradient: dark green for growing, light for shrinking (positive)
hist_vals = df['Hist'].values
colors = []
for i, v in enumerate(hist_vals):
    if v >= 0:
        # Green: bright when growing, dim when shrinking
        prev = hist_vals[i-1] if i > 0 else 0
        alpha = 1.0 if v >= prev else 0.4
        colors.append(f'#26a69a{int(alpha*255):02x}')
    else:
        prev = hist_vals[i-1] if i > 0 else 0
        alpha = 1.0 if v <= prev else 0.4
        colors.append(f'#ef5350{int(alpha*255):02x}')

ax2.set_facecolor('#1e1e1e')
ax2.bar(df.index, df['Hist'], color='#26a69a', alpha=0.7, width=0.8)
ax2.plot(df.index, df['MACD'],   color='#3498db', linewidth=1.5)
ax2.plot(df.index, df['Signal'], color='#f39c12', linewidth=1.5)
ax2.axhline(0, color='gray', linewidth=0.8)
ax2.tick_params(colors='white')
ax2.grid(True, alpha=0.15, color='gray')
```

---

## Bollinger Bands: Visualizing Volatility as a Dynamic Channel

**Bollinger Bands are drawn ON the price chart — three lines that expand and contract with volatility:**

**Construction:**
```
Middle Band = 20-day SMA
Upper Band  = 20-day SMA + (2 × 20-day Standard Deviation)
Lower Band  = 20-day SMA - (2 × 20-day Standard Deviation)
```

**What the Bands Tell You:**
```
NARROW BANDS (bands close together):
  Standard deviation is LOW → volatility is LOW
  → Market is calm, often consolidating
  → Big move may be coming ("Bollinger Squeeze")

WIDE BANDS (bands far apart):
  Standard deviation is HIGH → volatility is HIGH
  → Market is making big moves
  → Already in a volatile phase

PRICE POSITION:
  Price near upper band → stretched toward the high end
  Price at middle band  → at the average (trend line)
  Price near lower band → stretched toward the low end
```

**Python Code:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31")

# Calculate Bollinger Bands
df['BB_mid']   = df['Close'].rolling(20).mean()
df['BB_std']   = df['Close'].rolling(20).std()
df['BB_upper'] = df['BB_mid'] + 2 * df['BB_std']
df['BB_lower'] = df['BB_mid'] - 2 * df['BB_std']

# Bollinger Band Width (measure of how wide the bands are)
df['BB_width'] = (df['BB_upper'] - df['BB_lower']) / df['BB_mid']

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 10), sharex=True,
                                gridspec_kw={'height_ratios': [4, 1]})
fig.set_facecolor('#1e1e1e')

ax1.set_facecolor('#1e1e1e')
ax1.plot(df.index, df['Close'],    color='white',   linewidth=0.9, label='Close')
ax1.plot(df.index, df['BB_mid'],   color='#f0e68c', linewidth=1.5, label='Middle (SMA 20)')
ax1.plot(df.index, df['BB_upper'], color='#3498db', linewidth=1.2, linestyle='-', label='Upper Band (+2σ)')
ax1.plot(df.index, df['BB_lower'], color='#3498db', linewidth=1.2, linestyle='-', label='Lower Band (-2σ)')
ax1.fill_between(df.index, df['BB_upper'], df['BB_lower'], alpha=0.06, color='#3498db')
ax1.set_title('AAPL – Bollinger Bands (20, 2)', color='white', fontsize=13, fontweight='bold')
ax1.tick_params(colors='white')
ax1.legend(facecolor='#2a2a2a', labelcolor='white', fontsize=9)
ax1.grid(True, alpha=0.15, color='gray')

# BB Width panel (shows volatility compression/expansion)
ax2.set_facecolor('#1e1e1e')
ax2.plot(df.index, df['BB_width'], color='#9b59b6', linewidth=1.5, label='BB Width')
ax2.fill_between(df.index, df['BB_width'], df['BB_width'].min(),
                 alpha=0.2, color='#9b59b6')
ax2.set_ylabel('Band Width', color='white', fontsize=9)
ax2.tick_params(colors='white')
ax2.legend(facecolor='#2a2a2a', labelcolor='white', fontsize=9)
ax2.grid(True, alpha=0.15, color='gray')

plt.tight_layout()
```

---

## Bollinger Band Patterns: The Walk, the Squeeze, and the W-Bottom

**Three key Bollinger Band chart patterns every technical trader knows:**

**Pattern 1: The Bollinger Band Walk**
```
Price "walking" along the upper band:

  Upper Band: ─────/──────── (price hugging this line)
                  ↑price ↑
  Middle Band: ───/─────────
  Lower Band:  ─────────────

Signal: STRONG uptrend in progress
The fact that price can "walk" the upper band = momentum is strong.
This is NOT an automatic sell signal — strong stocks walk the upper band for weeks.
```

**Pattern 2: The Bollinger Squeeze**
```
Before:              After:
  ─────────           ─────────/
  ──────────  ← wide     /
  ─────────────  ← price ─────
  ──────────  ← wide     \
  ─────────           ─────────\

Bands compress to  →  Explosive breakout
their narrowest        in one direction
(squeeze)
```

**Pattern 3: The W-Bottom Reversal**
```
First bottom:   Price touches lower band → slight bounce
Second bottom:  Price touches lower band again but RSI is HIGHER
                (bullish divergence) → real reversal

        /──────
       /
──────/
│    ← First touch (low RSI)
  ──/
 /
│   ← Second touch (higher RSI = divergence)
Lower Band
```

**Python Code to Identify Squeeze:**
```python
# BB Squeeze: when band width drops to 52-week low
df['BB_width_52wk_min'] = df['BB_width'].rolling(252).min()
squeeze_dates = df[df['BB_width'] <= df['BB_width_52wk_min'] * 1.05].index

fig, ax = plt.subplots(figsize=(16, 7))
fig.set_facecolor('#1e1e1e')
ax.set_facecolor('#1e1e1e')
ax.plot(df.index, df['Close'],    color='white',   linewidth=0.8)
ax.plot(df.index, df['BB_upper'], color='#3498db', linewidth=1.0)
ax.plot(df.index, df['BB_lower'], color='#3498db', linewidth=1.0)
ax.fill_between(df.index, df['BB_upper'], df['BB_lower'], alpha=0.05, color='#3498db')

for d in squeeze_dates:
    ax.axvline(d, color='#f0e68c', linewidth=0.5, alpha=0.4)

ax.set_title('AAPL – Bollinger Bands with Squeeze Zones Highlighted',
             color='white', fontsize=13)
ax.tick_params(colors='white')
ax.grid(True, alpha=0.15, color='gray')
plt.tight_layout()
```

---

## Stochastic Oscillator: Visualizing Where Close Sits Within the Range

**The Stochastic Oscillator answers: "Where did price close relative to its recent High-Low range?"**

**Formula:**
```
%K = (Close - Lowest Low(n)) / (Highest High(n) - Lowest Low(n)) × 100
%D = 3-period SMA of %K

Where n = 14 (standard lookback period)

Interpretation:
  %K near 100 → Price closed near the TOP of its n-period range (overbought)
  %K near 0   → Price closed near the BOTTOM of its n-period range (oversold)
  %K = 50     → Price closed in the exact middle of its range
```

**Python Code:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

def stochastic(df, period=14, smooth_k=3, smooth_d=3):
    lowest_low   = df['Low'].rolling(period).min()
    highest_high = df['High'].rolling(period).max()
    pct_k_raw = 100 * (df['Close'] - lowest_low) / (highest_high - lowest_low)
    pct_k = pct_k_raw.rolling(smooth_k).mean()  # Fast %K (smoothed)
    pct_d = pct_k.rolling(smooth_d).mean()       # Slow %D
    return pct_k, pct_d

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31")
df['Stoch_K'], df['Stoch_D'] = stochastic(df)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 9), sharex=True,
                                gridspec_kw={'height_ratios': [3, 1.5]})
fig.set_facecolor('#1e1e1e')

for ax in [ax1, ax2]:
    ax.set_facecolor('#1e1e1e')
    ax.tick_params(colors='white')
    ax.grid(True, alpha=0.15, color='gray')

ax1.plot(df.index, df['Close'], color='white', linewidth=1.0)
ax1.set_title('AAPL – Price + Stochastic Oscillator', color='white', fontsize=13)

ax2.plot(df.index, df['Stoch_K'], color='#3498db', linewidth=1.5, label='%K')
ax2.plot(df.index, df['Stoch_D'], color='#f39c12', linewidth=1.5, label='%D (signal)')
ax2.axhline(80, color='#ef5350', linewidth=1.0, linestyle='--', label='Overbought (80)')
ax2.axhline(20, color='#26a69a', linewidth=1.0, linestyle='--', label='Oversold (20)')
ax2.fill_between(df.index, df['Stoch_K'], 80, where=(df['Stoch_K'] >= 80),
                 alpha=0.2, color='#ef5350')
ax2.fill_between(df.index, df['Stoch_K'], 20, where=(df['Stoch_K'] <= 20),
                 alpha=0.2, color='#26a69a')
ax2.set_ylim(0, 100)
ax2.legend(facecolor='#2a2a2a', labelcolor='white', fontsize=9)

plt.tight_layout()
```

---

## Stochastic Crossovers and Divergence

**Stochastic generates signals through crossovers and divergence — similar to MACD:**

**Stochastic Buy Signal:**
```
Conditions:  1. Both %K and %D are below 20 (oversold zone)
             2. %K crosses ABOVE %D

This signals: Selling exhaustion — price may be ready to bounce

Why the zone requirement matters:
  %K crossing %D at RSI=70 → not meaningful (already overbought)
  %K crossing %D at RSI=15 → high probability bounce signal ✅
```

**Stochastic Divergence:**
```
Bullish Stochastic Divergence:
  Price:     Lower Low (price made new bottom)
  Stoch %K:  Higher Low (oscillator made a shallower bottom)
  → Selling pressure exhausted, buyers quietly accumulating

Bearish Stochastic Divergence:
  Price:     Higher High (price made new top)
  Stoch %K:  Lower High (oscillator failed to confirm)
  → Buying pressure exhausted, distribution phase
```

**Python Code:**
```python
# Detect stochastic buy signals
df['stoch_above'] = (df['Stoch_K'] > df['Stoch_D']).astype(int)
df['stoch_cross'] = df['stoch_above'].diff()

# Buy signals: crossover in oversold zone
buy_signals = df[(df['stoch_cross'] == 1) & (df['Stoch_K'] < 30)]
sell_signals = df[(df['stoch_cross'] == -1) & (df['Stoch_K'] > 70)]

# Plot on price panel
ax1.scatter(buy_signals.index, buy_signals['Close'] * 0.97,
            marker='^', color='#26a69a', s=120, zorder=5, label='Stoch Buy')
ax1.scatter(sell_signals.index, sell_signals['Close'] * 1.03,
            marker='v', color='#ef5350', s=120, zorder=5, label='Stoch Sell')
```

---

## Average True Range (ATR): Measuring Volatility Without Direction

**ATR measures HOW MUCH price moves on average — without regard to direction:**

**What is True Range?**
```
True Range (TR) = maximum of:
  1. High - Low (the day's simple range)
  2. |High - Previous Close| (gap up situations)
  3. |Low  - Previous Close| (gap down situations)

ATR(n) = Exponential Moving Average of TR over n periods

ATR answers: "How many dollars does this stock typically move per day?"
```

**Why "True Range" Instead of Just High-Low?**
```
Day 1:  Close = $100
Day 2:  Gap up open, Low = $105, High = $108

High - Low = $3
|Low - Prev Close| = |$105 - $100| = $5 ← LARGER (the gap is part of the range)

True Range = $5 (includes the overnight gap)
This more accurately represents the full price movement experienced by traders.
```

**Python Code:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

def calculate_atr(df, period=14):
    tr1 = df['High'] - df['Low']
    tr2 = abs(df['High'] - df['Close'].shift(1))
    tr3 = abs(df['Low']  - df['Close'].shift(1))
    true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    atr = true_range.ewm(com=period - 1, min_periods=period).mean()
    return atr

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31")
df['ATR'] = calculate_atr(df)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 9), sharex=True,
                                gridspec_kw={'height_ratios': [3, 1.5]})
fig.set_facecolor('#1e1e1e')

ax1.set_facecolor('#1e1e1e')
ax1.plot(df.index, df['Close'], color='white', linewidth=1.0)
ax1.set_title('AAPL – Price + ATR (14)', color='white', fontsize=13)
ax1.tick_params(colors='white')
ax1.grid(True, alpha=0.15, color='gray')

ax2.set_facecolor('#1e1e1e')
ax2.plot(df.index, df['ATR'], color='#e74c3c', linewidth=1.5, label='ATR 14')
ax2.fill_between(df.index, df['ATR'], df['ATR'].min(), alpha=0.2, color='#e74c3c')
ax2.axhline(df['ATR'].mean(), color='#f0e68c', linewidth=1.0, linestyle='--',
            label=f"Average ATR: ${df['ATR'].mean():.2f}")
ax2.set_ylabel('ATR ($)', color='white', fontsize=9)
ax2.tick_params(colors='white')
ax2.legend(facecolor='#2a2a2a', labelcolor='white', fontsize=9)
ax2.grid(True, alpha=0.15, color='gray')

plt.tight_layout()
```

**ATR Reading**: If AAPL's 14-day ATR = $3.50, it means AAPL typically moves about $3.50 per day. A day where it only moves $0.80 is unusually quiet. A day where it moves $8.00 is unusually volatile.

---

## ATR-Based Stop Loss Visualization

**ATR provides a volatility-adjusted stop loss that adapts to current market conditions:**

**The Problem with Fixed Stop Losses:**
```
Stock A: ATR = $0.50 (very calm)
Stock B: ATR = $5.00 (very volatile)

Fixed stop of $2.00 below entry:
  Stock A: Stop at $2.00 = 4x daily range → way too wide (useless)
  Stock B: Stop at $2.00 = 0.4x daily range → way too tight (whipsawed out)
```

**ATR-Based Stop Loss:**
```
Stop Loss = Entry Price - (ATR Multiplier × ATR)

Common multipliers:
  1.5x ATR → Tight stop (shorter trades, more risk of being stopped out)
  2.0x ATR → Standard stop (balanced)
  3.0x ATR → Wide stop (longer trades, less likely to be stopped out)

Risk-Reward Target = Entry + (2 × Stop Distance) → 1:2 risk/reward
```

**Python Visualization:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

df = yf.download("AAPL", start="2024-06-01", end="2024-12-31")
df['ATR'] = calculate_atr(df)

# Simulate a trade entry
entry_date  = df.index[30]
entry_price = float(df.loc[entry_date, 'Close'])
atr_at_entry = float(df.loc[entry_date, 'ATR'])

stop_loss   = entry_price - 2.0 * atr_at_entry
take_profit = entry_price + 4.0 * atr_at_entry  # 1:2 risk/reward

fig, ax = plt.subplots(figsize=(16, 8))
fig.set_facecolor('#1e1e1e')
ax.set_facecolor('#1e1e1e')
ax.plot(df.index, df['Close'], color='white', linewidth=1.0)

# Entry point
ax.scatter([entry_date], [entry_price], color='#f0e68c', s=200, zorder=6,
           marker='o', label=f'Entry: ${entry_price:.2f}')

# Stop loss line
ax.axhline(stop_loss,   color='#ef5350', linewidth=2, linestyle='--',
           label=f'Stop Loss: ${stop_loss:.2f} (-2x ATR)')

# Take profit line
ax.axhline(take_profit, color='#26a69a', linewidth=2, linestyle='--',
           label=f'Take Profit: ${take_profit:.2f} (+4x ATR)')

# Risk/reward shading
ax.fill_between(df.index, stop_loss, take_profit, alpha=0.05, color='#26a69a')

atr_val = atr_at_entry
ax.set_title(f'ATR-Based Risk Management (ATR = ${atr_val:.2f})\nStop = 2x ATR, Target = 4x ATR (1:2 Risk/Reward)',
             color='white', fontsize=13)
ax.tick_params(colors='white')
ax.legend(facecolor='#2a2a2a', labelcolor='white')
ax.grid(True, alpha=0.15, color='gray')
plt.tight_layout()
```

---

## On-Balance Volume (OBV): Cumulative Buy vs. Sell Volume

**OBV is a cumulative line that adds volume on up days and subtracts volume on down days:**

**OBV Formula:**
```
If Close > Previous Close:   OBV = OBV_prev + Volume   (up day: add volume)
If Close < Previous Close:   OBV = OBV_prev - Volume   (down day: subtract volume)
If Close = Previous Close:   OBV = OBV_prev            (unchanged)

OBV starts at 0 and accumulates
```

**What OBV Reveals — Smart Money vs. Dumb Money:**
```
Scenario A: OBV rising while price is FLAT or falling
  → Money is flowing IN (accumulation) even though price hasn't moved yet
  → "Smart money" is quietly buying
  → Price breakout upward likely coming

Scenario B: OBV falling while price is at NEW HIGHS
  → Volume not confirming the rally
  → "Distribution" — institutional selling into retail buying
  → Potential top formation
```

**Python Code:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31")

# Calculate OBV
obv = [0]
for i in range(1, len(df)):
    if df['Close'].iloc[i] > df['Close'].iloc[i-1]:
        obv.append(obv[-1] + df['Volume'].iloc[i])
    elif df['Close'].iloc[i] < df['Close'].iloc[i-1]:
        obv.append(obv[-1] - df['Volume'].iloc[i])
    else:
        obv.append(obv[-1])
df['OBV'] = obv

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 9), sharex=True,
                                gridspec_kw={'height_ratios': [3, 1.5]})
fig.set_facecolor('#1e1e1e')

ax1.set_facecolor('#1e1e1e')
ax1.plot(df.index, df['Close'], color='white', linewidth=1.0)
ax1.set_title('AAPL – Price + On-Balance Volume (OBV)', color='white', fontsize=13)
ax1.tick_params(colors='white')
ax1.grid(True, alpha=0.15, color='gray')

ax2.set_facecolor('#1e1e1e')
ax2.plot(df.index, df['OBV'], color='#f39c12', linewidth=1.5, label='OBV')
ax2.fill_between(df.index, df['OBV'], 0, where=(df['OBV'] >= 0),
                 alpha=0.2, color='#26a69a')
ax2.fill_between(df.index, df['OBV'], 0, where=(df['OBV'] < 0),
                 alpha=0.2, color='#ef5350')
ax2.axhline(0, color='gray', linewidth=0.8, linestyle='--')
ax2.set_ylabel('OBV', color='white', fontsize=9)
ax2.tick_params(colors='white')
ax2.legend(facecolor='#2a2a2a', labelcolor='white')
ax2.grid(True, alpha=0.15, color='gray')

plt.tight_layout()
```

---

## Volume Profile: Visualizing Where Trading Activity Concentrates

**Volume Profile is a horizontal histogram showing at which PRICE LEVELS the most volume traded:**

**How Volume Profile Differs from Standard Volume:**
```
Standard Volume (time-based, vertical bars):
  Shows HOW MUCH traded at each TIME POINT
  x-axis = time, y-axis = volume

Volume Profile (price-based, horizontal bars):
  Shows HOW MUCH traded at each PRICE LEVEL
  x-axis = volume, y-axis = price
  Rotated 90° and overlaid on the right side of the price chart
```

**Key Terms:**
```
High Volume Node (HVN):  ████████████████ ← lots of volume here
  → Strong support or resistance level
  → Price moves slowly through HVNs (lots of orders)

Low Volume Node (LVN):   ██               ← very little volume
  → "Price vacuum" — price moves quickly through LVNs
  → Few orders = price accelerates past this level

Point of Control (POC):  ████████████████████ ← single most-traded level
  → The single most important price level in the profile
  → Acts as a strong magnet for price
```

**Python Code:**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31")

# Create price bins
n_bins = 50
price_min, price_max = df['Low'].min(), df['High'].max()
bins = np.linspace(price_min, price_max, n_bins + 1)
bin_centers = (bins[:-1] + bins[1:]) / 2

# Calculate volume at each price level
vol_profile = np.zeros(n_bins)
for _, row in df.iterrows():
    in_range = (bin_centers >= row['Low']) & (bin_centers <= row['High'])
    if in_range.sum() > 0:
        vol_profile[in_range] += row['Volume'] / in_range.sum()

# Normalize
vol_profile_norm = vol_profile / vol_profile.max()

fig, ax = plt.subplots(figsize=(16, 10))
fig.set_facecolor('#1e1e1e')
ax.set_facecolor('#1e1e1e')

# Price line
ax.plot(df.index, df['Close'], color='white', linewidth=1.0, zorder=5)

# Volume profile: horizontal bars on the right
ax_right = ax.twinx()
ax_right.barh(bin_centers, vol_profile_norm * 0.3,  # 30% of chart width
              height=(price_max - price_min) / n_bins,
              left=df.index[-1], color='#3498db', alpha=0.5)

# Mark Point of Control
poc_price = bin_centers[vol_profile.argmax()]
ax.axhline(poc_price, color='#f0e68c', linewidth=2, linestyle='-',
           label=f'Point of Control (POC): ${poc_price:.2f}', zorder=6)

ax.set_title('AAPL – Price + Volume Profile', color='white', fontsize=13)
ax.tick_params(colors='white')
ax.legend(facecolor='#2a2a2a', labelcolor='white')
ax.grid(True, alpha=0.15, color='gray')
plt.tight_layout()
```

---

## VWAP Deviation Bands: Combining Volume and Volatility

**VWAP Deviation Bands extend VWAP with standard deviation bands — an intraday institutional map:**

**Construction:**
```
VWAP = Σ(Typical Price × Volume) / Σ(Volume)

Standard Deviation bands:
  VWAP + 1σ  → First upper deviation (mild overbought intraday)
  VWAP + 2σ  → Second upper deviation (extreme overbought intraday)
  VWAP - 1σ  → First lower deviation (mild oversold intraday)
  VWAP - 2σ  → Second lower deviation (extreme oversold intraday)
```

**How Institutional Traders Use VWAP Bands:**
```
Buy Zone:   Price near VWAP - 1σ  → Buying at a discount to average
Sell Zone:  Price near VWAP + 1σ  → Selling at a premium to average
Strong Buy: Price at VWAP - 2σ    → Extreme intraday discount
Strong Sell: Price at VWAP + 2σ   → Extreme intraday premium

Note: VWAP bands reset every day — they are purely intraday tools
```

**Python Code:**
```python
def calculate_vwap_bands(df):
    df = df.copy()
    df['TP'] = (df['High'] + df['Low'] + df['Close']) / 3
    df['TP_Vol'] = df['TP'] * df['Volume']
    df['TP_Sq_Vol'] = (df['TP'] ** 2) * df['Volume']

    # Group by date
    by_date = df.groupby(df.index.date)
    df['cum_tp_vol'] = by_date['TP_Vol'].cumsum()
    df['cum_vol']    = by_date['Volume'].cumsum()
    df['cum_tp2_vol']= by_date['TP_Sq_Vol'].cumsum()

    df['VWAP'] = df['cum_tp_vol'] / df['cum_vol']
    variance   = df['cum_tp2_vol'] / df['cum_vol'] - df['VWAP'] ** 2
    df['VWAP_std'] = np.sqrt(variance.clip(lower=0))

    df['VWAP_upper1'] = df['VWAP'] + 1 * df['VWAP_std']
    df['VWAP_lower1'] = df['VWAP'] - 1 * df['VWAP_std']
    df['VWAP_upper2'] = df['VWAP'] + 2 * df['VWAP_std']
    df['VWAP_lower2'] = df['VWAP'] - 2 * df['VWAP_std']
    return df
```

---

## Building a Multi-Panel Indicator Dashboard

**Assembling all Part 3 indicators into a single professional multi-panel chart:**

```python
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
import yfinance as yf

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31")

# Calculate all indicators
df['SMA_20']  = df['Close'].rolling(20).mean()
df['BB_mid']  = df['Close'].rolling(20).mean()
df['BB_upper']= df['BB_mid'] + 2 * df['Close'].rolling(20).std()
df['BB_lower']= df['BB_mid'] - 2 * df['Close'].rolling(20).std()
df['RSI']     = calculate_rsi(df['Close'])
df['MACD'], df['Signal'], df['Hist'] = calculate_macd(df['Close'])

# Build figure
fig = plt.figure(figsize=(20, 14))
fig.set_facecolor('#1e1e1e')
gs = gridspec.GridSpec(4, 1, height_ratios=[5, 1.5, 1.5, 1.5], hspace=0.05)

ax_p = fig.add_subplot(gs[0])
ax_v = fig.add_subplot(gs[1], sharex=ax_p)
ax_r = fig.add_subplot(gs[2], sharex=ax_p)
ax_m = fig.add_subplot(gs[3], sharex=ax_p)

for ax in [ax_p, ax_v, ax_r, ax_m]:
    ax.set_facecolor('#1e1e1e')
    ax.tick_params(colors='white', labelsize=8)
    ax.grid(True, alpha=0.12, color='gray')

# Price + Bollinger Bands
ax_p.plot(df.index, df['Close'],    color='white',   linewidth=0.8)
ax_p.plot(df.index, df['SMA_20'],   color='#f0e68c', linewidth=1.2, label='SMA 20')
ax_p.plot(df.index, df['BB_upper'], color='#3498db', linewidth=1.0, linestyle='--')
ax_p.plot(df.index, df['BB_lower'], color='#3498db', linewidth=1.0, linestyle='--')
ax_p.fill_between(df.index, df['BB_upper'], df['BB_lower'], alpha=0.05, color='#3498db')
ax_p.set_title('AAPL – Complete 4-Panel Trading Dashboard', color='white', fontsize=14)
ax_p.legend(facecolor='#2a2a2a', labelcolor='white', fontsize=9)

# Volume
colors_v = ['#26a69a' if c >= o else '#ef5350'
            for c, o in zip(df['Close'], df['Open'])]
ax_v.bar(df.index, df['Volume'], color=colors_v, alpha=0.7, width=0.8)
ax_v.set_ylabel('Volume', color='white', fontsize=8)

# RSI
ax_r.plot(df.index, df['RSI'], color='#9b59b6', linewidth=1.3)
ax_r.axhline(70, color='#ef5350', linewidth=0.8, linestyle='--')
ax_r.axhline(30, color='#26a69a', linewidth=0.8, linestyle='--')
ax_r.fill_between(df.index, df['RSI'], 70, where=(df['RSI'] >= 70), alpha=0.2, color='#ef5350')
ax_r.fill_between(df.index, df['RSI'], 30, where=(df['RSI'] <= 30), alpha=0.2, color='#26a69a')
ax_r.set_ylim(0, 100)
ax_r.set_ylabel('RSI', color='white', fontsize=8)

# MACD
hist_colors = ['#26a69a' if v >= 0 else '#ef5350' for v in df['Hist']]
ax_m.bar(df.index, df['Hist'],   color=hist_colors, alpha=0.7, width=0.8)
ax_m.plot(df.index, df['MACD'],  color='#3498db', linewidth=1.3, label='MACD')
ax_m.plot(df.index, df['Signal'],color='#f39c12', linewidth=1.3, label='Signal')
ax_m.axhline(0, color='gray', linewidth=0.6)
ax_m.set_ylabel('MACD', color='white', fontsize=8)
ax_m.legend(facecolor='#2a2a2a', labelcolor='white', fontsize=8)

plt.setp(ax_p.get_xticklabels(), visible=False)
plt.setp(ax_v.get_xticklabels(), visible=False)
plt.setp(ax_r.get_xticklabels(), visible=False)
plt.tight_layout()
plt.savefig('trading_dashboard.png', dpi=150, bbox_inches='tight',
            facecolor='#1e1e1e')
```

---

## Indicator Combinations: RSI + MACD Convergence

**When RSI and MACD both signal at the same time, the combined visual is far more convincing:**

**Confluent Bullish Setup:**
```
Three-Panel View:

Price Panel:    Price forms a bullish candlestick pattern (e.g., Hammer) ✅
RSI Panel:      RSI crossing up through 30 (exiting oversold zone)       ✅
MACD Panel:     MACD line crossing above Signal line (bullish crossover) ✅

Three independent indicators agree → HIGH CONVICTION setup
```

**Conflicting Signals (Trade with Caution):**
```
Price Panel:    Price breaks to new all-time high                         ✅
RSI Panel:      RSI at 78 (overbought, but no divergence)                 ⚠️
MACD Panel:     MACD histogram bars SHRINKING (momentum fading)           ❌

Two out of three agree → MIXED signal → reduce position size, tighten stop
```

**The Signal Scoring Approach:**
```python
# Score each indicator: +1 bullish, -1 bearish, 0 neutral
def score_rsi(rsi_val):
    if rsi_val < 30: return +1   # Oversold → potential buy
    if rsi_val > 70: return -1   # Overbought → potential sell
    return 0

def score_macd(macd_val, signal_val):
    if macd_val > signal_val: return +1   # Bullish alignment
    return -1

def score_price_vs_sma200(price, sma200):
    if price > sma200: return +1   # Above 200-day MA → bull trend
    return -1

# Composite score: -3 to +3
df['Score'] = (
    df['RSI'].apply(score_rsi) +
    df.apply(lambda r: score_macd(r['MACD'], r['Signal']), axis=1) +
    df.apply(lambda r: score_price_vs_sma200(r['Close'], r['SMA_200']), axis=1)
)

# Color the price candles by composite score
high_conviction_buys  = df[df['Score'] == 3]
high_conviction_sells = df[df['Score'] == -3]
```

---

## Part 3 Summary & Preview of Part 4

**Complete Reference: All Part 3 Indicators**

| Indicator | Panel | Scale | Key Levels | Signals |
|-----------|-------|-------|------------|---------|
| RSI | Sub-panel | 0–100 | 70 (OB), 50, 30 (OS) | Crossover of zones, divergence |
| MACD | Sub-panel | Price units | Zero line | Line/signal crossover, histogram shrink |
| Bollinger Bands | Price overlay | Price | Upper/lower bands | Walk, squeeze, W-bottom |
| Stochastic | Sub-panel | 0–100 | 80 (OB), 20 (OS) | %K/%D crossover in zones |
| ATR | Sub-panel | Price units | Rolling average | Stop placement, volatility detection |
| OBV | Sub-panel | Cumulative | Trend direction | Divergence from price |
| Volume Profile | Price side bar | Volume | HVN, LVN, POC | Support/resistance identification |
| VWAP Bands | Intraday overlay | Price | ±1σ, ±2σ | Intraday buy/sell zones |

**Preview of Part 4 — Patterns and Complete Dashboards:**

In Part 4, we go beyond individual indicators to:
- 📐 **Chart Patterns** — geometric shapes: Head & Shoulders, Cup & Handle, Triangles, Flags
- 🌊 **Elliott Wave Theory** — fractal wave structure across all time frames
- 🎯 **Pattern + Indicator Confirmation** — why two signals beat one
- 🖥️ **Full Interactive Dashboard** — building the complete 4-panel Plotly dashboard
- 📈 **Backtesting Visualization** — equity curves, drawdown charts, return distributions

> "No single indicator is a crystal ball. But three indicators all saying the same thing at the same time? That's when experienced traders get serious." — Technical Trading Practicum
