# Class X – Part 4

[← Main](Classx.md) | [Part 1](Classx_Part1.md) | [Part 2](Classx_Part2.md) | [Part 3](Classx_Part3.md) | [Part 4](Classx_Part4.md)

---

# PART 4: PATTERN RECOGNITION & TRADING DASHBOARDS
# Slides 61–80
# ═══════════════════════════════════════════════════════════════

---

## Introduction to Chart Pattern Analysis

**Chart patterns are recurring geometric shapes that markets draw — visual template matching at scale:**

**What is a Chart Pattern?**
```
A chart pattern is a recognizable shape formed by price action over time
that tends to be followed by a predictable directional move.

It is essentially: learned visual template + probabilistic outcome

Examples:
  Head & Shoulders shape → usually precedes a decline
  Cup & Handle shape     → usually precedes a rally
  Triangle shape         → usually precedes a breakout (direction varies)
```

**Why Patterns Work (and Why They're Risky):**
```
WHY THEY WORK:
  1. Mass psychology creates repeatable behavior
  2. Institutional trading algorithms trade the same patterns
  3. Self-fulfilling: enough traders watching = enough orders to make them real
  4. Represent measurable supply/demand imbalances

WHY THEY FAIL:
  1. Never work 100% of the time
  2. Pattern identification is subjective ("in the eye of the beholder")
  3. Market context matters enormously (same pattern in a bull vs. bear market)
  4. The higher the timeframe, the more reliable; noise on 5-min charts
```

**The Two Categories of Chart Patterns:**

| Category | Definition | Examples |
|----------|------------|---------|
| **Reversal Patterns** | Signal end of current trend | Head & Shoulders, Double Top/Bottom |
| **Continuation Patterns** | Signal temporary pause in current trend | Flag, Pennant, Cup & Handle |

**The Visualization Skill**: Pattern recognition is a trained perceptual skill. The more charts you study, the faster your visual system recognizes the shapes. This is why technical traders spend hours reviewing historical charts — they're training their pattern recognition system.

---

## Head and Shoulders: The King of Reversal Patterns

**The Head and Shoulders top is the most recognized and widely respected bearish reversal pattern:**

**Anatomy:**
```
         Head
        /    \
Left   /      \   Right
Shoulder       Shoulder
  /\          /\
 /  \        /  \  ← Approximately same height
/    \──────/    \
      Neckline    ← Support line through the two troughs
              \
               \ ← Breakdown below neckline = SELL SIGNAL
                \
```

**The Five Parts:**
```
1. Left Shoulder:  Price rallies to a high, then pulls back
2. Head:           Price rallies to a HIGHER high (the peak), then pulls back
3. Right Shoulder: Price attempts to rally again, but only reaches APPROX same height as left shoulder
4. Neckline:       Line connecting the two pullback lows (between left shoulder and head, and head and right shoulder)
5. Breakdown:      Price closes below the neckline → bearish signal activated
```

**Python Code:**
```python
import matplotlib.pyplot as plt
import numpy as np

def draw_head_shoulders(ax):
    """Stylized Head and Shoulders pattern"""
    # Left shoulder
    x_ls = np.linspace(0, 3, 50)
    y_ls = -((x_ls - 1.5)**2) * 4 + 100

    # Head
    x_h = np.linspace(3, 7, 80)
    y_h = -((x_h - 5)**2) * 5 + 115

    # Right shoulder
    x_rs = np.linspace(7, 10, 50)
    y_rs = -((x_rs - 8.5)**2) * 4 + 100

    # Neckline (flat between the troughs)
    neckline_y = 88
    x_nk = np.array([1.5, 9.5])
    y_nk = np.array([neckline_y, neckline_y])

    ax.plot(x_ls, y_ls, color='white', linewidth=2)
    ax.plot(x_h,  y_h,  color='white', linewidth=2)
    ax.plot(x_rs, y_rs, color='white', linewidth=2)
    ax.plot(x_nk, y_nk, color='#f0e68c', linewidth=2, linestyle='--', label='Neckline')

    # Breakdown
    x_break = np.linspace(9.5, 12, 30)
    y_break = np.linspace(neckline_y, neckline_y - 20, 30)
    ax.plot(x_break, y_break, color='#ef5350', linewidth=2, label='Breakdown')

    # Labels
    ax.text(1.5, 102, 'Left\nShoulder', color='#3498db', ha='center', fontsize=10)
    ax.text(5,   117, 'Head',           color='#ef5350', ha='center', fontsize=10, fontweight='bold')
    ax.text(8.5, 102, 'Right\nShoulder',color='#3498db', ha='center', fontsize=10)
    ax.annotate('SELL signal:\nBreak below neckline',
                xy=(10.5, neckline_y - 5), xytext=(10, neckline_y + 10),
                color='#ef5350', fontsize=9,
                arrowprops=dict(arrowstyle='->', color='#ef5350'))

fig, ax = plt.subplots(figsize=(14, 7))
fig.set_facecolor('#1e1e1e')
ax.set_facecolor('#1e1e1e')
draw_head_shoulders(ax)
ax.set_title('Head and Shoulders — Bearish Reversal Pattern', color='white', fontsize=14)
ax.tick_params(colors='white')
ax.legend(facecolor='#2a2a2a', labelcolor='white')
ax.set_ylabel('Price', color='white')
plt.tight_layout()
```

**Measured Move Target:**
```
Once price breaks below the neckline, the projected target is:
Target = Neckline Price - (Head Price - Neckline Price)

In other words: the pattern projects a move down equal to the height of the head above the neckline.
```

---

## Inverse Head and Shoulders: The Bullish Mirror

**The Inverse Head and Shoulders is the exact geometric reverse — a bullish reversal from a downtrend:**

**Anatomy:**
```
       Neckline ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  ← Resistance line
      /    \                      /
     /      \    Head            / ← Breakout above neckline = BUY signal
Left         \   /  \          /
Shoulder      \ /    \        /
               V      \──────/  Right Shoulder
              /|\
             / | \
            /  |  \
         (lowest point of Head)
```

**Key Differences From Regular H&S:**
- Forms at the END of a downtrend (not an uptrend)
- Head is the LOWEST point (not the highest)
- Breakout is to the UPSIDE (price closes above the neckline)
- Volume typically increases on the breakout to confirm

**Python Code:**
```python
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(14, 7))
fig.set_facecolor('#1e1e1e')
ax.set_facecolor('#1e1e1e')

# Inverse H&S: mirror of the regular one
t = np.linspace(0, 12, 300)
neckline_y = 112

# Left shoulder (trough)
y_ls = neckline_y - 12 * np.exp(-((t - 1.5)**2) / 0.5)
# Head (deeper trough)
y_head = y_ls - 15 * np.exp(-((t - 5)**2) / 0.8)
# Right shoulder (shallow trough)
y_rs = y_head - 12 * np.exp(-((t - 8.5)**2) / 0.5)
# Combine
price = np.maximum(y_ls, np.maximum(y_head, y_rs))
price = np.clip(price, 85, 130)

ax.plot(t, price, color='white', linewidth=2, label='Price')
ax.axhline(neckline_y, color='#f0e68c', linewidth=2, linestyle='--', label='Neckline')

# Breakout
ax.annotate('', xy=(11, neckline_y + 10), xytext=(10, neckline_y),
            arrowprops=dict(arrowstyle='->', color='#26a69a', lw=2.5))
ax.text(10.5, neckline_y + 12, 'BUY\nBreakout!', color='#26a69a', fontsize=11, fontweight='bold')

# Labels
ax.text(1.5, 95, 'Left\nShoulder', color='#3498db', ha='center', fontsize=10)
ax.text(5,   88, 'Head\n(lowest)',  color='#ef5350', ha='center', fontsize=10, fontweight='bold')
ax.text(8.5, 95, 'Right\nShoulder',color='#3498db', ha='center', fontsize=10)

ax.set_title('Inverse Head and Shoulders — Bullish Reversal Pattern', color='white', fontsize=13)
ax.tick_params(colors='white')
ax.legend(facecolor='#2a2a2a', labelcolor='white')
plt.tight_layout()
```

---

## Cup and Handle: The Rounding Bottom

**The Cup and Handle is one of the most reliably bullish chart patterns — a slow, gradual recovery:**

**Anatomy:**
```
   Left rim            Right rim
   ─────────────────────────────
         \                /────── ← BREAKOUT above rim
          \    Cup       /─────  ← Handle (small pullback)
           \   (U-shape)/
            \          /
             \        /
              ────────
              (The cup bottom)

Formation time: Weeks to MONTHS (longer = more reliable)
Handle depth:   10-15% retracement from the right rim
```

**Why the Shape Matters:**
- The U-shape (not a V-shape) shows a gradual, orderly recovery
- V-shaped recoveries are too sharp — they suggest panic buying, not accumulation
- The handle represents a brief consolidation/shakeout before the final breakout
- Volume should increase on the breakout above the rim — confirms real demand

**Python Code:**
```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 15, 500)

# Create cup: U-shaped curve
cup_depth = 20
cup_center = 7
cup_y = 100 + cup_depth * ((t - cup_center)**2 / (cup_center**2)) - cup_depth
cup_y = np.clip(cup_y, 80, 105)

# Create handle: small pullback from the right rim
handle_mask = (t >= 11) & (t <= 13.5)
handle_y = cup_y.copy()
handle_y[handle_mask] = cup_y[handle_mask] - 5 * np.exp(-((t[handle_mask] - 12.25)**2) / 0.4)

# Breakout
breakout_mask = t >= 13.5
handle_y[breakout_mask] = 100 + (t[breakout_mask] - 13.5) * 4

fig, ax = plt.subplots(figsize=(14, 7))
fig.set_facecolor('#1e1e1e')
ax.set_facecolor('#1e1e1e')

ax.plot(t, handle_y, color='white', linewidth=2)
ax.axhline(100, color='#f0e68c', linewidth=1.5, linestyle='--', label='Rim Level (resistance → support)')

# Shade the cup
cup_x = t[(t >= 2) & (t <= 12)]
cup_vals = handle_y[(t >= 2) & (t <= 12)]
ax.fill_between(cup_x, cup_vals, 100, alpha=0.1, color='#3498db', label='Cup')

# Annotations
ax.text(7, 83, 'Cup Bottom\n(rounded U-shape)', color='#3498db', ha='center', fontsize=10)
ax.text(12.25, 91, 'Handle\n(slight pullback)', color='#f39c12', ha='center', fontsize=10)
ax.text(14, 107, 'Breakout!\n(above rim)', color='#26a69a', ha='center', fontsize=10, fontweight='bold')

ax.set_title('Cup and Handle — Bullish Continuation Pattern', color='white', fontsize=13)
ax.set_ylabel('Price', color='white')
ax.tick_params(colors='white')
ax.legend(facecolor='#2a2a2a', labelcolor='white')
plt.tight_layout()
```

---

## Triangle Patterns: Symmetrical, Ascending, Descending

**Triangles form when price makes progressively narrower swings — the market is "coiling" before a breakout:**

**Three Triangle Variants:**

```
SYMMETRICAL                ASCENDING               DESCENDING
Lower highs + Higher lows  Flat top + Higher lows  Lower highs + Flat bottom

  ╲           ╱             ────────────            ╲
   ╲         ╱              ╱         ╱              ╲────────
    ╲   ╱   ╱              ╱         ╱               ╲
     ╲ ╱   ╱              ╱         ╱                ╲────────
      ╲   ╱              ╱─────────╱                  ╲
       ─────

Breakout: Either direction   Breakout: Usually UP        Breakout: Usually DOWN
Bias: Neutral                Bias: Bullish               Bias: Bearish
(follow the trend)
```

**Python Code:**
```python
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.set_facecolor('#1e1e1e')
titles = ['Symmetrical Triangle', 'Ascending Triangle', 'Descending Triangle']
colors = ['white', 'white', 'white']

for ax, title in zip(axes, titles):
    ax.set_facecolor('#1e1e1e')
    ax.set_title(title, color='white', fontsize=11, fontweight='bold')
    ax.tick_params(colors='white')
    ax.grid(True, alpha=0.1, color='gray')

t = np.linspace(0, 10, 100)

# Symmetrical
upper_s = 110 - t * 1.5
lower_s = 90 + t * 1.5
price_s = 100 + 10 * np.sin(t * 2) * np.exp(-t * 0.15)
axes[0].plot(t, price_s, color='white', linewidth=1.5)
axes[0].plot(t, upper_s, color='#ef5350', linewidth=1.5, linestyle='--', label='Resistance (descending)')
axes[0].plot(t, lower_s, color='#26a69a', linewidth=1.5, linestyle='--', label='Support (ascending)')
axes[0].legend(facecolor='#2a2a2a', labelcolor='white', fontsize=8)

# Ascending
axes[1].plot(t, np.full_like(t, 108), color='#ef5350', linewidth=2, linestyle='--', label='Flat resistance')
lower_a = 90 + t * 1.5
axes[1].plot(t, lower_a, color='#26a69a', linewidth=2, linestyle='--', label='Rising support')
price_a = 100 + 8 * np.sin(t * 2) * np.exp(-t * 0.1) + t * 0.5
axes[1].plot(t, price_a, color='white', linewidth=1.5)
axes[1].legend(facecolor='#2a2a2a', labelcolor='white', fontsize=8)

# Descending
upper_d = 110 - t * 1.5
axes[2].plot(t, upper_d, color='#ef5350', linewidth=2, linestyle='--', label='Falling resistance')
axes[2].plot(t, np.full_like(t, 92), color='#26a69a', linewidth=2, linestyle='--', label='Flat support')
price_d = 100 + 8 * np.sin(t * 2) * np.exp(-t * 0.1) - t * 0.3
axes[2].plot(t, price_d, color='white', linewidth=1.5)
axes[2].legend(facecolor='#2a2a2a', labelcolor='white', fontsize=8)

plt.suptitle('Triangle Patterns: Three Variations', color='white', fontsize=14, fontweight='bold')
plt.tight_layout()
```

---

## Flag and Pennant Patterns: Brief Pauses in Strong Trends

**Flags and pennants are continuation patterns that form after a sharp directional move:**

**Anatomy:**
```
BULL FLAG:                          BEAR FLAG:
     ↑ Flag Pole                              ↓ Flag Pole
    ╱                                          ╲
   ╱                                            ╲
  ╱                                              ╲
 ╱ ────────────────── Flag channel                ╲ ────────  (rises slightly)
   ────────────────── (slight downward drift)           ──────
   ────────────────── (consolidation)            ╲────────────
↓                                                ↓
Breakout UP (continuation of uptrend)            Breakdown DOWN (continuation of downtrend)
```

**Measured Move:**
```
Target = Entry + Flag Pole Height

If flag pole = $20 rise
Entry at breakout = $100
Target = $100 + $20 = $120

This is called the "measured move" — the expected magnitude of the next leg
```

**Python Code:**
```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 12, 400)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
fig.set_facecolor('#1e1e1e')

# Bull Flag
pole_mask = t < 3
flag_mask = (t >= 3) & (t <= 7)
cont_mask = t >= 7

price_bf = np.zeros_like(t)
price_bf[pole_mask] = 90 + t[pole_mask] * 8         # Sharp rise (pole)
price_bf[flag_mask] = price_bf[pole_mask].max() - (t[flag_mask] - 3) * 1.5 + \
                      1.5 * np.sin((t[flag_mask] - 3) * 4)  # Slight drift + noise
price_bf[cont_mask] = price_bf[flag_mask][-1] + (t[cont_mask] - 7) * 7  # Continuation

ax1.set_facecolor('#1e1e1e')
ax1.plot(t, price_bf, color='white', linewidth=2, label='Price')
ax1.axvspan(3, 7, alpha=0.1, color='#3498db', label='Flag (consolidation)')
ax1.axvline(7, color='#26a69a', linewidth=2, linestyle='--', label='Breakout')
ax1.set_title('Bull Flag — Continuation Pattern', color='white', fontsize=12)
ax1.annotate('Pole', xy=(1.5, 104), color='#f39c12', fontsize=11, ha='center')
ax1.annotate('Flag', xy=(5, 122), color='#3498db', fontsize=11, ha='center')
ax1.annotate('Continuation', xy=(10, 135), color='#26a69a', fontsize=10, ha='center')
ax1.tick_params(colors='white')
ax1.legend(facecolor='#2a2a2a', labelcolor='white', fontsize=9)
ax1.grid(True, alpha=0.1, color='gray')

# Pennant (converging trendlines during consolidation)
ax2.set_facecolor('#1e1e1e')
price_p = price_bf.copy()
upper_p = np.where(flag_mask, price_bf[flag_mask][0] - (t - 3) * 0.5, np.nan)
lower_p = np.where(flag_mask, price_bf[flag_mask][0] - (t - 3) * 2.5, np.nan)
ax2.plot(t, price_bf, color='white', linewidth=1.5)
ax2.plot(t, upper_p, color='#f39c12', linewidth=1.5, linestyle='--')
ax2.plot(t, lower_p, color='#f39c12', linewidth=1.5, linestyle='--', label='Pennant trendlines')
ax2.axvline(7, color='#26a69a', linewidth=2, linestyle='--', label='Breakout')
ax2.set_title('Pennant — Similar to Flag, Converging Lines', color='white', fontsize=12)
ax2.tick_params(colors='white')
ax2.legend(facecolor='#2a2a2a', labelcolor='white', fontsize=9)
ax2.grid(True, alpha=0.1, color='gray')

plt.suptitle('Flag and Pennant Continuation Patterns', color='white', fontsize=14, fontweight='bold')
plt.tight_layout()
```

---

## Double Top and Double Bottom: Testing Limits Twice

**Double tops and bottoms test a key level twice — and fail the second time:**

**Double Top (Bearish Reversal) — "M" Shape:**
```
      A           B
     /\          /\     ← Both peaks at approximately the same price
    /  \        /  \
   /    \      /    \
  /      \────/      \
          ↑               \
        Neckline           \─── ← Breakdown below neckline = SELL
  (support at the trough
   between the two peaks)
```

**Double Bottom (Bullish Reversal) — "W" Shape:**
```
  ↑ Breakout above neckline = BUY
Neckline ─────────────────
  \      /    \      /
   \    /      \    /
    \──/        \──/
      A            B
   ← Both troughs at approximately the same price
```

**Python Code:**
```python
import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
fig.set_facecolor('#1e1e1e')

t = np.linspace(0, 12, 300)
neckline = 100

# Double Top (M shape)
dt_price = neckline + 15 * (np.exp(-((t-2)**2)/0.5) + np.exp(-((t-8)**2)/0.5)) - \
           5 * (np.exp(-((t-5)**2)/0.5))
dt_price = np.where(t > 10, neckline - (t - 10) * 5, dt_price)

ax1.set_facecolor('#1e1e1e')
ax1.plot(t, dt_price, color='white', linewidth=2)
ax1.axhline(neckline, color='#f0e68c', linewidth=2, linestyle='--', label=f'Neckline: ${neckline}')
ax1.scatter([2, 8], [neckline + 15, neckline + 15], color='#ef5350', s=200, zorder=6, label='Peaks (A & B)')
ax1.annotate('SELL\n(breakdown)', xy=(10.5, neckline - 5), color='#ef5350', fontsize=11, fontweight='bold')
ax1.set_title('Double Top — Bearish Reversal (M shape)', color='white', fontsize=12)
ax1.legend(facecolor='#2a2a2a', labelcolor='white')
ax1.tick_params(colors='white')
ax1.grid(True, alpha=0.1, color='gray')

# Double Bottom (W shape) — mirror
db_price = neckline - 15 * (np.exp(-((t-2)**2)/0.5) + np.exp(-((t-8)**2)/0.5)) + \
           5 * (np.exp(-((t-5)**2)/0.5))
db_price = np.where(t > 10, neckline + (t - 10) * 5, db_price)

ax2.set_facecolor('#1e1e1e')
ax2.plot(t, db_price, color='white', linewidth=2)
ax2.axhline(neckline, color='#f0e68c', linewidth=2, linestyle='--', label=f'Neckline: ${neckline}')
ax2.scatter([2, 8], [neckline - 15, neckline - 15], color='#26a69a', s=200, zorder=6, label='Troughs (A & B)')
ax2.annotate('BUY\n(breakout)', xy=(10.5, neckline + 5), color='#26a69a', fontsize=11, fontweight='bold')
ax2.set_title('Double Bottom — Bullish Reversal (W shape)', color='white', fontsize=12)
ax2.legend(facecolor='#2a2a2a', labelcolor='white')
ax2.tick_params(colors='white')
ax2.grid(True, alpha=0.1, color='gray')

plt.suptitle('Double Top & Bottom Reversal Patterns', color='white', fontsize=14, fontweight='bold')
plt.tight_layout()
```

---

## Wedge Patterns: Rising and Falling

**Wedges are converging trendlines that slope in the SAME direction — counterintuitively:**

**The Key Insight — Rising Wedge Is BEARISH:**
```
RISING WEDGE (Bearish):           FALLING WEDGE (Bullish):

   ─────────────────╲              ╲────────────────
  ──────────────────╲  ← price      ╲─────────────── ← price
                     ╲               ╲
  Both trendlines      ╲             Both trendlines   ╲
  slope UPWARD,         ╲            slope DOWNWARD,    ╲──
  but converge           ↓           but converge          ↑
  → BREAKDOWN coming     → Bearish   → BREAKOUT coming     → Bullish

REASONING:                          REASONING:
Price making higher highs           Price making lower lows
BUT higher lows are getting         BUT lower highs are getting
increasingly shallow →              less extreme →
buying pressure is WEAKENING        selling pressure is EXHAUSTING
even as price rises                 even as price falls
```

**Python Code:**
```python
import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
fig.set_facecolor('#1e1e1e')
t = np.linspace(0, 10, 200)

# Rising wedge
upper_rw = 100 + t * 3
lower_rw = 100 + t * 1.5

for ax, upper, lower, title, signal_color, signal_text in [
    (ax1, upper_rw, lower_rw, 'Rising Wedge (BEARISH — converging upward)', '#ef5350', 'SELL breakdown'),
    (ax2, 130 - t*3, 130 - t*1.5, 'Falling Wedge (BULLISH — converging downward)', '#26a69a', 'BUY breakout')
]:
    ax.set_facecolor('#1e1e1e')
    ax.plot(t, upper, color='#ef5350' if 'Rising' in title else '#26a69a', linewidth=2, linestyle='--', label='Resistance')
    ax.plot(t, lower, color='#26a69a' if 'Rising' in title else '#ef5350', linewidth=2, linestyle='--', label='Support')
    ax.fill_between(t, upper, lower, alpha=0.07, color='#f39c12')

    # Synthesize price bouncing within the wedge
    price_noise = (upper + lower) / 2 + (upper - lower) * 0.3 * np.sin(t * 3)
    ax.plot(t, price_noise, color='white', linewidth=1.5, label='Price')

    # Breakout arrow
    y_break = lower[-1] - 8 if 'Rising' in title else upper[-1] + 8
    ax.annotate('', xy=(10, y_break), xytext=(9, lower[-1] if 'Rising' in title else upper[-1]),
                arrowprops=dict(arrowstyle='->', color=signal_color, lw=2.5))
    ax.text(9.5, y_break - 2 if 'Rising' in title else y_break + 1,
            signal_text, color=signal_color, fontsize=11, fontweight='bold')

    ax.set_title(title, color='white', fontsize=11, fontweight='bold')
    ax.tick_params(colors='white')
    ax.legend(facecolor='#2a2a2a', labelcolor='white', fontsize=9)
    ax.grid(True, alpha=0.1, color='gray')

plt.suptitle('Wedge Patterns', color='white', fontsize=14, fontweight='bold')
plt.tight_layout()
```

---

## Introduction to Elliott Wave Theory

**Elliott Wave Theory: markets move in predictable 5-wave impulse + 3-wave correction cycles:**

**The Basic Wave Structure:**
```
                        5
                       / \
                  3   /   \     A
                 / \ /     \   / \
                /   4       \ /   B
               /             \   / \
              2                \ /   C ← Correction complete
       /\    /
      /  \  /
     /    \/
    1      (Wave 2 retracement)

IMPULSE WAVE (5 waves):           CORRECTIVE WAVE (3 waves):
Wave 1: First move up              Wave A: First leg down
Wave 2: Pullback (38.2-61.8% Fib)  Wave B: Bounce (partial recovery)
Wave 3: Strongest, longest leg up  Wave C: Final leg down (often = Wave A length)
Wave 4: Pullback (milder than 2)
Wave 5: Final push up
```

**The Three Immutable Rules:**
```
1. Wave 2 can NEVER retrace below the start of Wave 1
2. Wave 3 can NEVER be the shortest impulse wave (1, 3, or 5)
3. Wave 4 can NEVER overlap Wave 1's price territory
```

**Python Code (Stylized Wave Diagram):**
```python
import matplotlib.pyplot as plt
import numpy as np

# Define wave turning points
points = {
    'Start': (0, 100),
    '1': (2, 115),
    '2': (3, 107),  # Fib 50% retracement of Wave 1
    '3': (6, 135),  # Strongest leg
    '4': (7, 125),  # Milder pullback
    '5': (9, 142),  # Final push
    'A': (10, 130), # Correction begins
    'B': (11, 136), # Bounce
    'C': (13, 118)  # Final corrective leg
}

labels = list(points.keys())
coords = list(points.values())

xs = [c[0] for c in coords]
ys = [c[1] for c in coords]

fig, ax = plt.subplots(figsize=(14, 8))
fig.set_facecolor('#1e1e1e')
ax.set_facecolor('#1e1e1e')

# Impulse waves (1-5) in teal
ax.plot(xs[:6], ys[:6], color='#26a69a', linewidth=2.5, label='Impulse (1-5)')
# Corrective waves (A-C) in red/orange
ax.plot(xs[5:], ys[5:], color='#ef5350', linewidth=2.5, label='Correction (A-B-C)')

# Label each wave
for label, (x, y) in points.items():
    offset_y = 3 if label in ['1', '3', '5', 'B'] else -5
    color = '#26a69a' if label.isdigit() else '#ef5350'
    ax.annotate(label, xy=(x, y), xytext=(x, y + offset_y),
                color=color, fontsize=14, fontweight='bold', ha='center',
                bbox=dict(boxstyle='circle,pad=0.3', fc='#1e1e1e', ec=color, lw=1.5))

ax.set_title('Elliott Wave Theory — 5-3 Wave Structure', color='white', fontsize=14, fontweight='bold')
ax.set_ylabel('Price', color='white')
ax.tick_params(colors='white')
ax.legend(facecolor='#2a2a2a', labelcolor='white', fontsize=11)
ax.grid(True, alpha=0.15, color='gray')
plt.tight_layout()
```

---

## Elliott Wave Rules and Visual Guidelines

**Three hard rules and three guidelines that validate or invalidate a wave count:**

**The Three Hard Rules (Cannot Be Violated):**
```
RULE 1: Wave 2 never retraces past Wave 1's origin
  Valid:                  Invalid:
    1                       1
   / \                     / \  2 goes below
  /   2                   /   ← start of 1 ❌
 0

RULE 2: Wave 3 is never the shortest impulse wave
  Valid:                   Invalid:
    3   5                       5
   / \ / \                     / \   3 is shorter
  1   4   \               3   /   \  than 1 or 5 ❌
 / \       \             / \_/     \
0   2                   1
                        2

RULE 3: Wave 4 never enters Wave 1's price territory
  Valid:                   Invalid:
  3  5                    3     5
 / \/                    / \ 4 /
1   4                   1   \/
 \                       \   ↓ Wave 4 drops
  2                       2   below Wave 1 top ❌
```

**Three Fibonacci Guidelines (Common But Not Required):**
```
Wave 2 retracement: Commonly 50% or 61.8% of Wave 1
Wave 3 extension:   Commonly 161.8% of Wave 1
Wave 4 retracement: Commonly 38.2% of Wave 3
```

**Python Validation Code:**
```python
def validate_elliott_waves(turning_points):
    """
    turning_points = {'0': 100, '1': 115, '2': 107, '3': 135, '4': 125, '5': 142}
    Returns: list of rule violations
    """
    violations = []

    # Rule 1: Wave 2 cannot go below Wave 1 start
    if turning_points['2'] <= turning_points['0']:
        violations.append("RULE 1 VIOLATED: Wave 2 retraced below Wave 1 start")

    # Rule 2: Wave 3 cannot be the shortest impulse
    w1_len = turning_points['1'] - turning_points['0']
    w3_len = turning_points['3'] - turning_points['2']
    w5_len = turning_points['5'] - turning_points['4']
    if w3_len == min(w1_len, w3_len, w5_len):
        violations.append("RULE 2 VIOLATED: Wave 3 is the shortest impulse wave")

    # Rule 3: Wave 4 cannot enter Wave 1 territory
    if turning_points['4'] <= turning_points['1']:
        violations.append("RULE 3 VIOLATED: Wave 4 entered Wave 1's price territory")

    return violations if violations else ["✅ All three rules satisfied — valid wave count"]
```

---

## Annotating Wave Counts in Python

**Adding professional Elliott Wave labels to a real historical price chart:**

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import yfinance as yf
import pandas as pd
import numpy as np

df = yf.download("AAPL", start="2023-01-01", end="2024-06-30")

fig, ax = plt.subplots(figsize=(18, 9))
fig.set_facecolor('#1e1e1e')
ax.set_facecolor('#1e1e1e')
ax.plot(df.index, df['Close'], color='white', linewidth=1.2, alpha=0.8)

# Manually identified turning points (dates and prices)
# In practice, you identify these through price structure analysis
wave_points = [
    ('0_Start', '2023-01-03', df.loc['2023-01-03':'2023-01-06', 'Close'].min(), '#aaa'),
    ('1',       '2023-02-02', df.loc['2023-02-01':'2023-02-05', 'Close'].max(), '#26a69a'),
    ('2',       '2023-03-13', df.loc['2023-03-10':'2023-03-15', 'Close'].min(), '#26a69a'),
    ('3',       '2023-07-19', df.loc['2023-07-17':'2023-07-21', 'Close'].max(), '#26a69a'),
    ('4',       '2023-10-26', df.loc['2023-10-24':'2023-10-28', 'Close'].min(), '#26a69a'),
    ('5',       '2023-12-14', df.loc['2023-12-12':'2023-12-16', 'Close'].max(), '#26a69a'),
    ('A',       '2024-01-22', df.loc['2024-01-20':'2024-01-24', 'Close'].min(), '#ef5350'),
    ('B',       '2024-02-01', df.loc['2024-01-30':'2024-02-02', 'Close'].max(), '#ef5350'),
    ('C',       '2024-04-19', df.loc['2024-04-17':'2024-04-22', 'Close'].min(), '#ef5350'),
]

for label, date_str, price, color in wave_points:
    try:
        date = pd.Timestamp(date_str)
        offset = 5 if label in ['1', '3', '5', 'B'] else -8
        ax.annotate(
            label.replace('0_Start', '0'),
            xy=(date, price),
            xytext=(date, price + offset),
            color=color,
            fontsize=13,
            fontweight='bold',
            ha='center',
            arrowprops=dict(arrowstyle='-', color=color, lw=1.0),
            bbox=dict(boxstyle='round,pad=0.2', fc='#1e1e1e', ec=color, lw=1.5)
        )
    except:
        pass

ax.set_title('AAPL – Elliott Wave Count (2023-2024)', color='white', fontsize=14, fontweight='bold')
ax.set_ylabel('Price ($)', color='white')
ax.tick_params(colors='white')
ax.grid(True, alpha=0.15, color='gray')
plt.tight_layout()
```

---

## Combining Patterns with Indicators: The Confirmation Principle

**A chart pattern confirmed by indicators is far more reliable than a pattern alone:**

**Three-Part Confirmation Checklist:**
```
Pattern:    Head & Shoulders forming (bearish)      → +1 bearish signal
RSI:        RSI falling, currently at 55 (neutral)  → +0 neutral signal
MACD:       MACD crosses below Signal line           → +1 bearish signal

Score: 2/3 bearish → moderate confidence, proceed with caution

vs.

Pattern:    Head & Shoulders neckline break           → +1 bearish
RSI:        RSI below 50, bearish divergence          → +1 bearish
MACD:       MACD histogram negative and growing       → +1 bearish
Volume:     Volume surges on the breakdown            → +1 bearish

Score: 4/4 bearish → HIGH CONFIDENCE signal
```

**Python Visualization:**
```python
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import yfinance as yf

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31")
df['RSI']  = calculate_rsi(df['Close'])
df['MACD'], df['Signal'], df['Hist'] = calculate_macd(df['Close'])

fig = plt.figure(figsize=(18, 12))
fig.set_facecolor('#1e1e1e')
gs = gridspec.GridSpec(3, 1, height_ratios=[4, 1.5, 1.5], hspace=0.05)

ax_p = fig.add_subplot(gs[0])
ax_r = fig.add_subplot(gs[1], sharex=ax_p)
ax_m = fig.add_subplot(gs[2], sharex=ax_p)

for ax in [ax_p, ax_r, ax_m]:
    ax.set_facecolor('#1e1e1e')
    ax.tick_params(colors='white', labelsize=9)
    ax.grid(True, alpha=0.12, color='gray')

# Price
ax_p.plot(df.index, df['Close'], color='white', linewidth=1.0)
ax_p.set_title('Pattern + Indicator Confirmation Example', color='white', fontsize=13)

# RSI
ax_r.plot(df.index, df['RSI'], color='#9b59b6', linewidth=1.5)
ax_r.axhline(70, color='#ef5350', linewidth=0.8, linestyle='--')
ax_r.axhline(30, color='#26a69a', linewidth=0.8, linestyle='--')
ax_r.axhline(50, color='gray',    linewidth=0.6, linestyle=':', alpha=0.5)
ax_r.fill_between(df.index, df['RSI'], 70, where=(df['RSI'] >= 70), alpha=0.2, color='#ef5350')
ax_r.fill_between(df.index, df['RSI'], 30, where=(df['RSI'] <= 30), alpha=0.2, color='#26a69a')
ax_r.set_ylim(0, 100)
ax_r.set_ylabel('RSI', color='white', fontsize=9)

# MACD
hist_colors = ['#26a69a' if v >= 0 else '#ef5350' for v in df['Hist']]
ax_m.bar(df.index, df['Hist'], color=hist_colors, alpha=0.7, width=0.8)
ax_m.plot(df.index, df['MACD'],   color='#3498db', linewidth=1.3)
ax_m.plot(df.index, df['Signal'], color='#f39c12', linewidth=1.3)
ax_m.axhline(0, color='gray', linewidth=0.6)
ax_m.set_ylabel('MACD', color='white', fontsize=9)

plt.setp(ax_p.get_xticklabels(), visible=False)
plt.setp(ax_r.get_xticklabels(), visible=False)
plt.tight_layout()
```

---

## Support and Resistance Visualization

**Support and resistance are the foundation of all technical analysis — horizontal price walls:**

**Definitions:**
```
SUPPORT:    A price level where buying interest is strong enough
            to STOP a decline and cause a bounce
            Visual: Price repeatedly "touches" this level and bounces UP

RESISTANCE: A price level where selling interest is strong enough
            to STOP a rally and cause a pullback
            Visual: Price repeatedly "touches" this level and bounces DOWN

ROLE REVERSAL (Critical Concept):
  Old Resistance → becomes new Support (after a breakout above)
  Old Support    → becomes new Resistance (after a breakdown below)
```

**Python Code:**
```python
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31")

fig, ax = plt.subplots(figsize=(16, 8))
fig.set_facecolor('#1e1e1e')
ax.set_facecolor('#1e1e1e')

ax.plot(df.index, df['Close'], color='white', linewidth=1.0, label='AAPL Close', zorder=5)

# Define key levels manually (or use rolling max/min detection)
support_levels    = [165.0, 175.0, 185.0]
resistance_levels = [190.0, 200.0, 210.0]

for level in support_levels:
    if df['Close'].min() <= level <= df['Close'].max():
        ax.axhline(level, color='#26a69a', linewidth=2, linestyle='-', alpha=0.7)
        ax.text(df.index[-1], level, f'  S ${level:.0f}', color='#26a69a', fontsize=10, va='center')

for level in resistance_levels:
    if df['Close'].min() <= level <= df['Close'].max():
        ax.axhline(level, color='#ef5350', linewidth=2, linestyle='-', alpha=0.7)
        ax.text(df.index[-1], level, f'  R ${level:.0f}', color='#ef5350', fontsize=10, va='center')

ax.set_title('AAPL – Support and Resistance Levels', color='white', fontsize=13, fontweight='bold')
ax.tick_params(colors='white')
ax.legend(facecolor='#2a2a2a', labelcolor='white')
ax.grid(True, alpha=0.15, color='gray')
plt.tight_layout()
```

---

## Building a Complete Trading Dashboard: Architecture

**Before writing code, design the layout — architecture first, implementation second:**

**Dashboard Blueprint:**
```
┌─────────────────────────────────────────────────────────────────┐
│  TITLE: "AAPL Trading Dashboard — [Date Range]"                 │
│  Ticker selector / Date range controls (Plotly dropdowns)       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  PANEL 1: PRICE (60% height)                                    │
│  • Candlesticks (green/red)                                      │
│  • SMA 20 (blue dashed), SMA 50 (orange), SMA 200 (red)        │
│  • Bollinger Bands (blue channel, shaded)                        │
│  • Buy/Sell signal arrows (if strategy overlay selected)         │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│  PANEL 2: VOLUME (15% height)                                   │
│  • Color-coded volume bars                                       │
│  • 20-day average volume line (dashed)                          │
├─────────────────────────────────────────────────────────────────┤
│  PANEL 3: RSI (12.5% height)                                    │
│  • RSI line (purple)                                             │
│  • 70 / 50 / 30 reference lines                                 │
│  • Red/green shading in extreme zones                           │
├─────────────────────────────────────────────────────────────────┤
│  PANEL 4: MACD (12.5% height)                                   │
│  • Histogram bars (green/red)                                   │
│  • MACD line (blue) + Signal line (orange)                      │
│  • Zero line                                                    │
└─────────────────────────────────────────────────────────────────┘
                    ↕ All panels share the same x-axis (time)
```

**Key Design Decisions:**
```
1. Height ratios: [5, 1.5, 1.5, 1.5] → price panel dominates
2. sharex=True → zoom in price panel zooms all panels
3. Dark theme → professional trading terminal aesthetic
4. Consistent color coding throughout all panels
5. Y-axes on right side → price scale readable at a glance
6. Grid lines → light gray, not distracting
```

---

## Trading Dashboard: Python Implementation Part 1

**Building the price and volume panels:**

```python
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import pandas as pd
import numpy as np
import yfinance as yf

def build_trading_dashboard(ticker="AAPL", start="2024-01-01", end="2024-12-31"):

    # ── Fetch data ──────────────────────────────────────────────
    df = yf.download(ticker, start=start, end=end, auto_adjust=True)
    df.columns = [c[0] for c in df.columns] if isinstance(df.columns[0], tuple) else df.columns

    # ── Calculate indicators ────────────────────────────────────
    df['SMA_20']  = df['Close'].rolling(20).mean()
    df['SMA_50']  = df['Close'].rolling(50).mean()
    df['SMA_200'] = df['Close'].rolling(200).mean()
    df['BB_mid']  = df['SMA_20']
    df['BB_std']  = df['Close'].rolling(20).std()
    df['BB_upper']= df['BB_mid'] + 2 * df['BB_std']
    df['BB_lower']= df['BB_mid'] - 2 * df['BB_std']

    # ── Build figure ────────────────────────────────────────────
    fig = plt.figure(figsize=(20, 14))
    fig.set_facecolor('#1e1e1e')
    gs = gridspec.GridSpec(4, 1, height_ratios=[5, 1.5, 1.5, 1.5], hspace=0.04)

    ax_p = fig.add_subplot(gs[0])
    ax_v = fig.add_subplot(gs[1], sharex=ax_p)
    ax_r = fig.add_subplot(gs[2], sharex=ax_p)
    ax_m = fig.add_subplot(gs[3], sharex=ax_p)

    for ax in [ax_p, ax_v, ax_r, ax_m]:
        ax.set_facecolor('#121212')
        ax.tick_params(axis='both', colors='#aaa', labelsize=8)
        ax.grid(True, alpha=0.12, color='#333', linestyle='-', linewidth=0.5)
        for spine in ax.spines.values():
            spine.set_color('#333')

    # ── PANEL 1: Price + MAs + Bollinger ────────────────────────
    # Candlestick bars (manual since we're using matplotlib)
    up_mask   = df['Close'] >= df['Open']
    down_mask = ~up_mask

    for mask, color in [(up_mask, '#26a69a'), (down_mask, '#ef5350')]:
        subset = df[mask]
        ax_p.bar(subset.index, subset['Close'] - subset['Open'],
                 bottom=subset['Open'], color=color, width=0.6, alpha=0.9)
        ax_p.vlines(subset.index, subset['Low'], subset['High'],
                    color=color, linewidth=0.7)

    # MA overlays
    ax_p.plot(df.index, df['SMA_20'],  color='#3498db', linewidth=1.2, linestyle='--', label='SMA 20')
    ax_p.plot(df.index, df['SMA_50'],  color='#f39c12', linewidth=1.4, label='SMA 50')
    ax_p.plot(df.index, df['SMA_200'], color='#e74c3c', linewidth=2.0, label='SMA 200')

    # Bollinger Bands
    ax_p.plot(df.index, df['BB_upper'], color='#5dade2', linewidth=0.9, linestyle=':')
    ax_p.plot(df.index, df['BB_lower'], color='#5dade2', linewidth=0.9, linestyle=':')
    ax_p.fill_between(df.index, df['BB_upper'], df['BB_lower'], alpha=0.04, color='#3498db')

    ax_p.set_title(f'{ticker} – Trading Dashboard ({start} to {end})',
                   color='white', fontsize=14, fontweight='bold', pad=12)
    ax_p.set_ylabel('Price (USD)', color='#aaa', fontsize=9)
    ax_p.legend(loc='upper left', facecolor='#1a1a1a', labelcolor='#ccc',
                fontsize=9, framealpha=0.8)

    # ── PANEL 2: Volume ──────────────────────────────────────────
    vol_colors = ['#26a69a' if c >= o else '#ef5350'
                  for c, o in zip(df['Close'], df['Open'])]
    ax_v.bar(df.index, df['Volume'], color=vol_colors, alpha=0.7, width=0.7)
    ax_v.plot(df.index, df['Volume'].rolling(20).mean(),
              color='#f0e68c', linewidth=1.0, linestyle='--', label='Avg Vol (20)')
    ax_v.set_ylabel('Volume', color='#aaa', fontsize=8)
    ax_v.legend(loc='upper right', facecolor='#1a1a1a', labelcolor='#ccc', fontsize=8)

    plt.setp(ax_p.get_xticklabels(), visible=False)
    plt.setp(ax_v.get_xticklabels(), visible=False)

    return fig, ax_p, ax_v, ax_r, ax_m, df

fig, ax_p, ax_v, ax_r, ax_m, df = build_trading_dashboard("AAPL")
print("Price and volume panels complete — adding RSI and MACD next...")
```

---

## Trading Dashboard: Python Implementation Part 2

**Adding RSI and MACD panels to complete the full dashboard:**

```python
# ── PANEL 3: RSI ────────────────────────────────────────────────
def calculate_rsi(prices, period=14):
    delta = prices.diff()
    gain = delta.clip(lower=0).ewm(com=period-1, min_periods=period).mean()
    loss = (-delta.clip(upper=0)).ewm(com=period-1, min_periods=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def calculate_macd(prices, fast=12, slow=26, signal=9):
    ema_f = prices.ewm(span=fast,   adjust=False).mean()
    ema_s = prices.ewm(span=slow,   adjust=False).mean()
    macd  = ema_f - ema_s
    sig   = macd.ewm(span=signal, adjust=False).mean()
    hist  = macd - sig
    return macd, sig, hist

df['RSI'] = calculate_rsi(df['Close'])
df['MACD'], df['Signal_MACD'], df['Hist'] = calculate_macd(df['Close'])

# RSI panel
ax_r.plot(df.index, df['RSI'], color='#9b59b6', linewidth=1.5, label='RSI (14)')
ax_r.axhline(70, color='#ef5350', linewidth=0.9, linestyle='--', alpha=0.8)
ax_r.axhline(50, color='#666',    linewidth=0.6, linestyle=':', alpha=0.6)
ax_r.axhline(30, color='#26a69a', linewidth=0.9, linestyle='--', alpha=0.8)
ax_r.fill_between(df.index, df['RSI'], 70,
    where=(df['RSI'] >= 70), alpha=0.2, color='#ef5350')
ax_r.fill_between(df.index, df['RSI'], 30,
    where=(df['RSI'] <= 30), alpha=0.2, color='#26a69a')
ax_r.set_ylim(0, 100)
ax_r.set_yticks([30, 50, 70])
ax_r.set_ylabel('RSI', color='#aaa', fontsize=8)
ax_r.legend(loc='upper right', facecolor='#1a1a1a', labelcolor='#ccc', fontsize=8)

# MACD panel
hist_colors = ['#26a69a' if v >= 0 else '#ef5350' for v in df['Hist']]
ax_m.bar(df.index, df['Hist'], color=hist_colors, alpha=0.75, width=0.7, label='Histogram')
ax_m.plot(df.index, df['MACD'],        color='#3498db', linewidth=1.4, label='MACD')
ax_m.plot(df.index, df['Signal_MACD'], color='#f39c12', linewidth=1.4, label='Signal')
ax_m.axhline(0, color='#555', linewidth=0.8, linestyle='-')
ax_m.set_ylabel('MACD', color='#aaa', fontsize=8)
ax_m.legend(loc='upper right', facecolor='#1a1a1a', labelcolor='#ccc', fontsize=8)

plt.setp(ax_r.get_xticklabels(), visible=False)

# Format dates on bottom panel
import matplotlib.dates as mdates
ax_m.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax_m.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
plt.setp(ax_m.get_xticklabels(), rotation=30, ha='right', color='#aaa', fontsize=8)

plt.tight_layout()
plt.savefig('aapl_trading_dashboard.png', dpi=150, bbox_inches='tight',
            facecolor='#1e1e1e')
print("Dashboard saved to aapl_trading_dashboard.png")
```

---

## Interactive Trading Dashboard with Plotly

**Upgrade the static matplotlib dashboard to a fully interactive Plotly version:**

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import yfinance as yf

def interactive_trading_dashboard(ticker="AAPL", period="1y"):

    df = yf.download(ticker, period=period, auto_adjust=True)
    df.columns = [c[0] if isinstance(c, tuple) else c for c in df.columns]

    # Calculate indicators
    df['SMA_20']  = df['Close'].rolling(20).mean()
    df['SMA_50']  = df['Close'].rolling(50).mean()
    df['SMA_200'] = df['Close'].rolling(200).mean()
    df['BB_mid']  = df['SMA_20']
    df['BB_upper']= df['BB_mid'] + 2 * df['Close'].rolling(20).std()
    df['BB_lower']= df['BB_mid'] - 2 * df['Close'].rolling(20).std()
    df['RSI']     = calculate_rsi(df['Close'])
    df['MACD_line'], df['Signal_line'], df['Hist'] = calculate_macd(df['Close'])

    # Build subplots
    fig = make_subplots(
        rows=4, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.02,
        row_heights=[0.5, 0.15, 0.17, 0.18],
        subplot_titles=[f'{ticker} Price', 'Volume', 'RSI (14)', 'MACD (12,26,9)']
    )

    # ── Row 1: Candlesticks + MAs + Bollinger ───────────────────
    fig.add_trace(go.Candlestick(
        x=df.index, open=df['Open'], high=df['High'],
        low=df['Low'],  close=df['Close'],
        increasing_line_color='#26a69a', decreasing_line_color='#ef5350',
        name='Price'
    ), row=1, col=1)

    for ma, color, dash, name in [
        ('SMA_20', '#3498db', 'dash', 'SMA 20'),
        ('SMA_50', '#f39c12', 'solid', 'SMA 50'),
        ('SMA_200', '#e74c3c', 'solid', 'SMA 200'),
    ]:
        fig.add_trace(go.Scatter(x=df.index, y=df[ma], line=dict(color=color, width=1.5, dash=dash),
                                 name=name), row=1, col=1)

    fig.add_trace(go.Scatter(x=df.index, y=df['BB_upper'], line=dict(color='#5dade2', width=1, dash='dot'),
                             name='BB Upper', showlegend=False), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['BB_lower'], line=dict(color='#5dade2', width=1, dash='dot'),
                             name='BB Lower', fill='tonexty', fillcolor='rgba(93,173,226,0.05)',
                             showlegend=False), row=1, col=1)

    # ── Row 2: Volume ────────────────────────────────────────────
    vol_colors = ['#26a69a' if c >= o else '#ef5350'
                  for c, o in zip(df['Close'], df['Open'])]
    fig.add_trace(go.Bar(x=df.index, y=df['Volume'], marker_color=vol_colors,
                         name='Volume', opacity=0.7), row=2, col=1)

    # ── Row 3: RSI ───────────────────────────────────────────────
    fig.add_trace(go.Scatter(x=df.index, y=df['RSI'], line=dict(color='#9b59b6', width=1.5),
                             name='RSI'), row=3, col=1)
    for level, color in [(70, 'rgba(239,83,80,0.4)'), (30, 'rgba(38,166,154,0.4)')]:
        fig.add_hline(y=level, line_color=color, line_dash='dash', line_width=1, row=3, col=1)

    # ── Row 4: MACD ──────────────────────────────────────────────
    hist_colors_plotly = ['#26a69a' if v >= 0 else '#ef5350' for v in df['Hist']]
    fig.add_trace(go.Bar(x=df.index, y=df['Hist'], marker_color=hist_colors_plotly,
                         name='MACD Histogram', opacity=0.7), row=4, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['MACD_line'],   line=dict(color='#3498db', width=1.5),
                             name='MACD Line'), row=4, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['Signal_line'], line=dict(color='#f39c12', width=1.5),
                             name='Signal Line'), row=4, col=1)

    # ── Layout ───────────────────────────────────────────────────
    fig.update_layout(
        title=dict(text=f'{ticker} – Interactive Trading Dashboard', font=dict(size=18, color='white')),
        template='plotly_dark',
        height=900,
        showlegend=True,
        xaxis_rangeslider_visible=False,
        legend=dict(bgcolor='rgba(26,26,26,0.8)', font=dict(color='white')),
        paper_bgcolor='#1e1e1e',
        plot_bgcolor='#121212',
    )

    fig.write_html(f'{ticker}_dashboard.html')
    print(f"Interactive dashboard saved to {ticker}_dashboard.html")
    return fig

fig = interactive_trading_dashboard("AAPL", "1y")
fig.show()
```

---

## Backtesting Visualizations: Did the Strategy Work?

**A strategy is not complete until you visualize its performance over historical data:**

**The Three Performance Visualizations:**

```
1. EQUITY CURVE: Portfolio value over time
   y-axis: Portfolio $ value (or cumulative return)
   x-axis: Time
   → Shows if the strategy grew money over time

2. DRAWDOWN CHART: How far from the peak
   y-axis: % below peak (always negative or zero)
   x-axis: Time
   → Shows max loss periods, risk profile

3. TRADE RETURN DISTRIBUTION: Per-trade profitability histogram
   y-axis: Number of trades
   x-axis: % return per trade
   → Shows win/loss ratio and outlier trades
```

**Python Code:**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

df = yf.download("AAPL", start="2020-01-01", end="2024-12-31")
df['SMA_20']  = df['Close'].rolling(20).mean()
df['SMA_50']  = df['Close'].rolling(50).mean()
df['signal']  = np.where(df['SMA_20'] > df['SMA_50'], 1, 0)
df['position']= df['signal'].shift(1)
df['returns'] = df['Close'].pct_change()
df['strategy']= df['returns'] * df['position']

# Cumulative returns
df['cum_return_strat'] = (1 + df['strategy']).cumprod()
df['cum_return_bh']    = (1 + df['returns']).cumprod()

# Drawdown
rolling_max = df['cum_return_strat'].cummax()
df['drawdown'] = (df['cum_return_strat'] - rolling_max) / rolling_max

fig, axes = plt.subplots(3, 1, figsize=(16, 14))
fig.set_facecolor('#1e1e1e')

# Equity curves
axes[0].set_facecolor('#1e1e1e')
axes[0].plot(df.index, df['cum_return_strat'], color='#26a69a', linewidth=2, label='SMA Crossover Strategy')
axes[0].plot(df.index, df['cum_return_bh'],    color='#3498db', linewidth=2, linestyle='--', label='Buy & Hold (AAPL)')
axes[0].set_title('Equity Curve: SMA 20/50 Crossover vs. Buy & Hold (2020-2024)',
                  color='white', fontsize=13, fontweight='bold')
axes[0].axhline(1, color='gray', linewidth=0.8, linestyle='--')
axes[0].set_ylabel('Portfolio Value (Starting = 1.0)', color='white')
axes[0].legend(facecolor='#2a2a2a', labelcolor='white')
axes[0].tick_params(colors='white')
axes[0].grid(True, alpha=0.15, color='gray')

# Drawdown
axes[1].set_facecolor('#1e1e1e')
axes[1].fill_between(df.index, df['drawdown'], 0, color='#ef5350', alpha=0.5, label='Drawdown')
axes[1].plot(df.index, df['drawdown'], color='#ef5350', linewidth=1.0)
axes[1].set_ylabel('Drawdown (%)', color='white')
axes[1].set_title('Drawdown Over Time', color='white', fontsize=12)
axes[1].tick_params(colors='white')
axes[1].grid(True, alpha=0.15, color='gray')
axes[1].yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y*100:.1f}%'))

# Return distribution
axes[2].set_facecolor('#1e1e1e')
trade_returns = df[df['strategy'] != 0]['strategy'].dropna()
axes[2].hist(trade_returns, bins=50, color='#3498db', edgecolor='#1e1e1e', alpha=0.8)
axes[2].axvline(0, color='white', linewidth=1.5, linestyle='--')
axes[2].axvline(trade_returns.mean(), color='#26a69a', linewidth=2, linestyle='-',
                label=f"Mean: {trade_returns.mean()*100:.3f}%")
axes[2].set_xlabel('Daily Return (%)', color='white')
axes[2].set_ylabel('Frequency', color='white')
axes[2].set_title('Per-Trade Return Distribution', color='white', fontsize=12)
axes[2].legend(facecolor='#2a2a2a', labelcolor='white')
axes[2].tick_params(colors='white')
axes[2].grid(True, alpha=0.15, color='gray')

plt.tight_layout()
plt.savefig('backtest_results.png', dpi=150, bbox_inches='tight', facecolor='#1e1e1e')
```

---

## Common Mistakes in Trading Visualization

**Visual pitfalls that lead traders and analysts astray:**

**Mistake 1: Hindsight Bias (Most Common)**
```
❌ WRONG: Drawing Fibonacci levels or patterns on a chart
         and then zooming into only the section where they worked
         → Every pattern "works" if you cherry-pick the examples

✅ RIGHT: Backtesting the pattern over hundreds of occurrences
          and measuring the actual win rate across the full dataset
```

**Mistake 2: Indicator Overload**
```
❌ WRONG: RSI + MACD + Stochastic + CCI + Williams %R + MFI
         All measuring momentum → they all say the same thing
         More indicators ≠ more information

✅ RIGHT: 1 trend indicator (e.g., SMA 200)
         + 1 momentum indicator (e.g., RSI)
         + 1 volatility indicator (e.g., Bollinger Bands)
         = Complete picture without redundancy
```

**Mistake 3: Misleading Y-Axis**
```
❌ WRONG: Y-axis starts at $149 when price ranges from $148 to $155
         → A 0.7% decline looks like a 50% crash
         → Commonly used by financial media to make charts dramatic

✅ RIGHT: Y-axis includes enough range to show context
          Or uses percentage change (honest relative scale)
```

**Mistake 4: Ignoring Time Horizon**
```
❌ WRONG: Using a 5-minute RSI to make a long-term investment decision
         Different time horizons, completely different signals

✅ RIGHT: Match your indicator time frame to your trade time horizon
         Day trader → use intraday indicators (5-min, 1-hour)
         Long-term investor → use weekly/monthly indicators
```

**Mistake 5: Curve Fitting**
```
❌ WRONG: Testing 1,000 different MA combinations on historical data,
         finding the one that worked best → then claiming it's "the strategy"
         This is curve fitting → will fail on future data

✅ RIGHT: Choose indicator parameters based on fundamental reasoning,
         then test on OUT-OF-SAMPLE data (data not used in optimization)
```

---

## Summary, Resources, and Next Steps

**The Complete Journey — What You Learned Across 80 Slides:**

**Part 1 — The Visual Grammar:**
- OHLCV data structure, candlestick anatomy, color conventions
- Line vs. OHLC vs. candlestick chart types
- Volume as the conviction meter
- Python: mplfinance, Plotly, logarithmic scales

**Part 2 — Trend Analysis:**
- SMA, EMA, WMA, VWAP — smoothing and their tradeoffs
- Golden Cross / Death Cross
- Fibonacci retracement, extension, fan lines, time zones
- Confluence zones — where independent indicators agree

**Part 3 — Momentum & Volatility:**
- RSI (0-100 speedometer), RSI divergence
- MACD (three-component oscillator), histogram early signals
- Bollinger Bands (dynamic volatility channel)
- Stochastic Oscillator, ATR, OBV, Volume Profile

**Part 4 — Pattern Recognition & Dashboards:**
- Head & Shoulders, Cup & Handle, triangles, flags, wedges
- Double top/bottom, support/resistance, role reversal
- Elliott Wave Theory and annotation
- Multi-panel dashboards: matplotlib static + Plotly interactive
- Backtesting visualization: equity curve, drawdown, return distribution

**Recommended Resources:**

| Resource | Type | Focus |
|----------|------|-------|
| *Technical Analysis of Financial Markets* — John Murphy | Book | Comprehensive reference |
| TradingView.com | Platform | Real-time charting (free tier available) |
| `mplfinance` docs | Library | Python candlestick charts |
| `yfinance` docs | Library | Free stock data |
| `plotly` Finance docs | Library | Interactive dashboards |
| Investopedia Technical Analysis | Website | Pattern definitions |
| `backtrader` library | Library | Full backtesting framework |

**Libraries to Install:**
```bash
pip install mplfinance yfinance plotly pandas numpy matplotlib
pip install python-pptx  # For PowerPoint export
```

**Next Steps:**
- 🔧 Build your own automated screening script to scan 500 stocks for patterns
- 📊 Create a live dashboard that pulls real-time data every minute
- 🤖 Code a full systematic strategy with entry, exit, and position sizing rules
- 📈 Connect your strategy to a paper trading account (Alpaca, Interactive Brokers)
- 🧪 Learn proper backtesting methodology with walk-forward analysis

> "The goal of technical analysis is not to predict the future — it is to objectively identify what the market is doing right now and react accordingly. The chart is the map. You still have to drive." — Final Principle of Technical Analysis
