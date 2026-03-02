"""
Trading Slides Generator — Hybrid Approach
  - Category A (~55 slides): Python/matplotlib/mplfinance → authentic financial charts
  - Category B (~25 slides): OpenAI gpt-image-1 → conceptual/educational art
Saves all images to Classx/slide_images/slide_XXX_final.png
"""

import os, sys, re, base64, subprocess
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import warnings
warnings.filterwarnings('ignore')

try:
    import yfinance as yf
    HAS_YF = True
except ImportError:
    HAS_YF = False

from openai import OpenAI

# ── Config ──────────────────────────────────────────────────────
SLIDE_DIR   = 'Classx/slide_images'
PART_FILES  = {
    1: 'Classx/Classx_Part1.md',
    2: 'Classx/Classx_Part2.md',
    3: 'Classx/Classx_Part3.md',
    4: 'Classx/Classx_Part4.md',
}

# Dark theme constants
BG   = '#1e1e1e'
BG2  = '#121212'
BULL = '#26a69a'
BEAR = '#ef5350'
BLUE = '#3498db'
ORANGE = '#f39c12'
RED  = '#e74c3c'
PURPLE = '#9b59b6'
YELLOW = '#f0e68c'
WHITE = '#ffffff'
GRAY  = '#888888'

# Slides that use OpenAI DALL-E (conceptual/intro/summary)
DALLE_SLIDES = {1, 2, 3, 19, 20, 21, 31, 40, 60, 61, 69, 74, 79, 80}

os.makedirs(SLIDE_DIR, exist_ok=True)


# ──────────────────────────────────────────────────────────────
# UTILITY HELPERS
# ──────────────────────────────────────────────────────────────

def dark_fig(w=16, h=9, nrows=1, ncols=1, **kw):
    fig, axes = plt.subplots(nrows, ncols, figsize=(w, h), **kw)
    fig.set_facecolor(BG)
    def _style(ax):
        ax.set_facecolor(BG2)
        ax.tick_params(colors=WHITE, labelsize=9)
        ax.grid(True, alpha=0.12, color='#333')
        for sp in ax.spines.values():
            sp.set_color('#444')
        ax.title.set_color(WHITE)
        ax.xaxis.label.set_color(WHITE)
        ax.yaxis.label.set_color(WHITE)
    if hasattr(axes, '__iter__'):
        try:
            for ax in axes.flat:
                _style(ax)
        except AttributeError:
            for ax in axes:
                _style(ax)
    else:
        _style(axes)
    return fig, axes

def save_fig(fig, slide_num):
    path = f'{SLIDE_DIR}/slide_{slide_num:03d}_final.png'
    fig.savefig(path, dpi=130, bbox_inches='tight', facecolor=BG)
    plt.close(fig)
    print(f'  ✅ Saved {path}')
    return path

def synthetic_ohlcv(n=120, seed=42, trend=0.0003, vol=0.015, start_price=150.0):
    np.random.seed(seed)
    closes = [start_price]
    for _ in range(n - 1):
        r = np.random.normal(trend, vol)
        closes.append(closes[-1] * (1 + r))
    closes = np.array(closes)
    highs  = closes * (1 + np.abs(np.random.normal(0, vol/2, n)))
    lows   = closes * (1 - np.abs(np.random.normal(0, vol/2, n)))
    opens  = np.roll(closes, 1)
    opens[0] = closes[0]
    volumes = np.random.randint(30_000_000, 80_000_000, n).astype(float)
    idx = pd.bdate_range(end=pd.Timestamp('2024-12-31'), periods=n)
    df = pd.DataFrame({'Open':opens,'High':highs,'Low':lows,'Close':closes,'Volume':volumes}, index=idx)
    return df

def get_stock_data(ticker='AAPL', start='2024-01-01', end='2024-12-31', fallback_n=200):
    if HAS_YF:
        try:
            raw = yf.download(ticker, start=start, end=end, auto_adjust=True, progress=False)
            if isinstance(raw.columns, pd.MultiIndex):
                raw.columns = [c[0] for c in raw.columns]
            if len(raw) > 20:
                return raw[['Open','High','Low','Close','Volume']].dropna()
        except Exception:
            pass
    return synthetic_ohlcv(fallback_n)

def calc_rsi(prices, period=14):
    delta = prices.diff()
    gain = delta.clip(lower=0).ewm(com=period-1, min_periods=period).mean()
    loss = (-delta.clip(upper=0)).ewm(com=period-1, min_periods=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def calc_macd(prices, fast=12, slow=26, signal=9):
    ema_f  = prices.ewm(span=fast,   adjust=False).mean()
    ema_s  = prices.ewm(span=slow,   adjust=False).mean()
    macd   = ema_f - ema_s
    sig    = macd.ewm(span=signal, adjust=False).mean()
    hist   = macd - sig
    return macd, sig, hist

def draw_candles(ax, df, width=0.6):
    up = df[df['Close'] >= df['Open']]
    dn = df[df['Close'] <  df['Open']]
    x_up = np.arange(len(df))[df['Close'] >= df['Open']]
    x_dn = np.arange(len(df))[df['Close'] <  df['Open']]
    ax.bar(x_up, up['Close']-up['Open'],  bottom=up['Open'],  color=BULL, width=width, alpha=0.9)
    ax.bar(x_dn, dn['Open'] -dn['Close'], bottom=dn['Close'], color=BEAR, width=width, alpha=0.9)
    ax.vlines(x_up, up['Low'],  up['High'],  color=BULL, linewidth=0.7)
    ax.vlines(x_dn, dn['Low'],  dn['High'],  color=BEAR, linewidth=0.7)
    # x-ticks: show ~6 dates
    step = max(1, len(df)//6)
    ticks = list(range(0, len(df), step))
    ax.set_xticks(ticks)
    ax.set_xticklabels([df.index[i].strftime('%b %Y') for i in ticks],
                       rotation=30, ha='right', color=WHITE, fontsize=8)


# ──────────────────────────────────────────────────────────────
# OPENAI IMAGE GENERATOR
# ──────────────────────────────────────────────────────────────

def extract_slide_content(slide_number):
    part = ((slide_number - 1) // 20) + 1
    offset = (slide_number - 1) % 20
    fpath = PART_FILES.get(part, PART_FILES[1])
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    sections = re.split(r'\n## ', content)
    sections = [s.strip() for s in sections if s.strip()]
    # Filter out navigation/header sections
    body_sections = [s for s in sections if not s.startswith('[') and not s.startswith('#')]
    if offset < len(body_sections):
        return "## " + body_sections[offset]
    return body_sections[0] if body_sections else ""

def generate_dalle_slide(slide_number, api_key):
    client = OpenAI(api_key=api_key)
    content = extract_slide_content(slide_number)
    content_clean = re.sub(r'[^\x00-\x7F]+', '', content).strip()[:800]

    prompt = f"""Create a professional university presentation slide image.

SLIDE CONTENT:
{content_clean}

DESIGN THEME: Playful academic cartoon + clean university style
COLOR PALETTE: Soft blues (primary), oranges (accents), teals (secondary), white background with subtle texture
TYPOGRAPHY: Bold headers in rounded friendly font (Montserrat/Poppins), body in Open Sans, title at top large and centered
VISUAL STYLE: Illustrated cartoon-style icons, simple diagrams, light shadows, subtle paper texture, clean layout with good spacing
LAYOUT: 16:9 landscape (1536x1024), title top center, content well-organized, good white space
REQUIREMENTS: All text readable, professional graduate school quality, engaging and memorable

Style reference: Coursera, Khan Academy, Duolingo — educational, friendly, professional."""

    print(f'  🎨 OpenAI DALL-E for slide {slide_number}...')
    resp = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1536x1024",
        quality="high",
        n=1
    )
    out = f'{SLIDE_DIR}/slide_{slide_number:03d}_final.png'
    item = resp.data[0]
    if hasattr(item, 'b64_json') and item.b64_json:
        with open(out, 'wb') as f:
            f.write(base64.b64decode(item.b64_json))
    elif hasattr(item, 'url') and item.url:
        subprocess.run(['curl', '-s', '-o', out, item.url], check=True)
    else:
        raise ValueError("No image data returned")
    print(f'  ✅ Saved {out}')
    return out


# ──────────────────────────────────────────────────────────────
# PYTHON CHART GENERATORS (one per slide or group)
# ──────────────────────────────────────────────────────────────

def slide_004(n):
    """OHLC: The four dimensions of price data"""
    df = synthetic_ohlcv(5, seed=10)
    fig, axes = dark_fig(16, 8, 1, 2)
    ax1, ax2 = axes
    # Table on left
    ax1.axis('off')
    day = df.iloc[2]
    data = [['OPEN',  f'${day.Open:.2f}',  'First trade of the period'],
            ['HIGH',  f'${day.High:.2f}',  'Highest price reached'],
            ['LOW',   f'${day.Low:.2f}',   'Lowest price reached'],
            ['CLOSE', f'${day.Close:.2f}', 'Last trade of the period'],
            ['VOLUME',f'{int(day.Volume):,}','Shares traded']]
    colors_r = [[BULL]*3,[BEAR]*3,[BEAR]*3,[BULL]*3,['#5dade2']*3]
    t = ax1.table(cellText=data, colLabels=['Dimension','Value','Meaning'],
                  cellColours=colors_r, loc='center', cellLoc='left')
    t.auto_set_font_size(False); t.set_fontsize(12); t.scale(1.2, 2.2)
    ax1.set_title('One Trading Period = 5 Data Points (OHLCV)', color=WHITE, fontsize=13, pad=10)
    # Single candle diagram on right
    ax2.set_xlim(0, 10); ax2.set_ylim(day.Low*0.995, day.High*1.005)
    ax2.set_facecolor(BG2)
    ax2.tick_params(colors=WHITE)
    body_c = BULL if day.Close >= day.Open else BEAR
    ax2.bar([5], [abs(day.Close-day.Open)], bottom=min(day.Open,day.Close),
            color=body_c, width=2, alpha=0.9)
    ax2.vlines([5], day.Low, day.High, color=body_c, linewidth=2)
    for label, price, x_off in [
        ('HIGH',  day.High,  7.5),
        ('CLOSE', day.Close, 7.5),
        ('OPEN',  day.Open,  7.5),
        ('LOW',   day.Low,   7.5),
    ]:
        ax2.axhline(price, color='#555', linewidth=0.6, linestyle='--')
        ax2.text(x_off, price, f'{label}: ${price:.2f}', color=YELLOW, fontsize=11,
                 va='center', fontweight='bold')
    ax2.set_title('Single Candlestick — OHLCV Encoded', color=WHITE, fontsize=13, pad=10)
    fig.suptitle('The Four Dimensions of Price Data (OHLCV)', color=WHITE, fontsize=15, fontweight='bold')
    plt.tight_layout()
    return save_fig(fig, n)

def slide_006_007_008(n):
    """Line vs OHLC vs Candlestick comparison"""
    df = get_stock_data('AAPL','2024-07-01','2024-10-31', fallback_n=65)
    x = np.arange(len(df))
    fig, axes = dark_fig(18, 6, 1, 3)
    titles = ['Line Chart\n(Close only)', 'OHLC Bar Chart\n(All 4 prices)', 'Candlestick Chart\n(Body + Wicks + Color)']
    for ax, title in zip(axes, titles):
        ax.set_title(title, fontsize=11, fontweight='bold')
        ax.tick_params(colors=WHITE, labelsize=8)
    # Line chart
    axes[0].plot(x, df['Close'], color=BLUE, linewidth=2)
    axes[0].fill_between(x, df['Close'], df['Close'].min(), alpha=0.1, color=BLUE)
    # OHLC bar
    for i, (_, row) in enumerate(df.iterrows()):
        col = BULL if row.Close >= row.Open else BEAR
        axes[1].vlines(i, row.Low, row.High, color=col, linewidth=1.2)
        axes[1].hlines(row.Open,  i-0.2, i,   color=col, linewidth=1.2)
        axes[1].hlines(row.Close, i, i+0.2, color=col, linewidth=1.2)
    # Candlestick
    draw_candles(axes[2], df)
    step = max(1,len(df)//5)
    for ax in axes[:2]:
        ticks = list(range(0,len(df),step))
        ax.set_xticks(ticks)
        ax.set_xticklabels([df.index[i].strftime('%b %Y') for i in ticks],
                           rotation=30, ha='right', color=WHITE, fontsize=8)
    fig.suptitle(f'Three Ways to Display Price Data — AAPL', color=WHITE, fontsize=14, fontweight='bold')
    plt.tight_layout()
    return save_fig(fig, n)

def slide_009_010_011(n):
    """Candlestick anatomy + shapes"""
    fig, axes = dark_fig(18, 8, 1, 3)
    shapes = [
        ('DOJI\n(Indecision)', 100.0, 100.1, 97.5, 102.5, WHITE,
         'Equal open & close\nneither side won'),
        ('HAMMER\n(Potential Reversal ↑)', 101.5, 100.0, 95.0, 102.5, BULL,
         'Long lower wick\nbuyerss rejected low'),
        ('SHOOTING STAR\n(Potential Reversal ↓)', 100.5, 101.5, 99.0, 105.0, BEAR,
         'Long upper wick\nsellers rejected high'),
    ]
    for ax, (name, close, open_, low, high, color, note) in zip(axes, shapes):
        body_bot = min(open_, close)
        body_top = max(open_, close)
        ax.set_xlim(0,4); ax.set_ylim(low-1, high+1)
        ax.bar([2], [body_top-body_bot], bottom=body_bot, color=color, width=1.2, alpha=0.9)
        ax.vlines([2], low, high, color=color, linewidth=2)
        ax.set_title(name, color=YELLOW, fontsize=12, fontweight='bold')
        ax.text(2, (high+low)/2, note, color=WHITE, fontsize=9, ha='center',
                bbox=dict(boxstyle='round', fc='#333', alpha=0.7))
        ax.set_xticks([])
        ax.tick_params(colors=WHITE, labelsize=9)
    fig.suptitle('Reading Candlestick Shapes as Visual Signals', color=WHITE, fontsize=14, fontweight='bold')
    plt.tight_layout()
    return save_fig(fig, n)

def slide_012(n):
    """Volume bar"""
    df = get_stock_data('AAPL','2024-01-01','2024-06-30', fallback_n=120)
    fig, (ax1, ax2) = dark_fig(16, 9, 2, 1, gridspec_kw={'height_ratios':[3,1]}, sharex=False)
    x = np.arange(len(df))
    draw_candles(ax1, df)
    ax1.set_title('AAPL — Price + Volume: The Conviction Meter', color=WHITE, fontsize=13)
    vol_colors = [BULL if c>=o else BEAR for c,o in zip(df['Close'],df['Open'])]
    ax2.bar(x, df['Volume'], color=vol_colors, alpha=0.7, width=0.7)
    avg20 = df['Volume'].rolling(20).mean()
    ax2.plot(x, avg20, color=YELLOW, linewidth=1.5, linestyle='--', label='20-day Avg Vol')
    ax2.set_ylabel('Volume', color=WHITE, fontsize=9)
    ax2.legend(facecolor='#2a2a2a', labelcolor=WHITE, fontsize=9)
    step = max(1,len(df)//6)
    ticks = list(range(0,len(df),step))
    ax2.set_xticks(ticks)
    ax2.set_xticklabels([df.index[i].strftime('%b %Y') for i in ticks], rotation=30, ha='right', color=WHITE, fontsize=8)
    plt.tight_layout()
    return save_fig(fig, n)

def slide_013(n):
    """First candlestick chart — code result"""
    df = get_stock_data('AAPL','2024-01-01','2024-12-31', fallback_n=200)
    sma20 = df['Close'].rolling(20).mean()
    x = np.arange(len(df))
    fig, (ax1, ax2) = dark_fig(16,9,2,1, gridspec_kw={'height_ratios':[4,1]}, sharex=False)
    draw_candles(ax1, df)
    ax1.plot(x, sma20, color=YELLOW, linewidth=1.8, label='SMA 20', linestyle='--')
    ax1.set_title('Your First Candlestick Chart in Python — AAPL 2024', color=WHITE, fontsize=13)
    ax1.legend(facecolor='#2a2a2a', labelcolor=WHITE, fontsize=10)
    vol_colors = [BULL if c>=o else BEAR for c,o in zip(df['Close'],df['Open'])]
    ax2.bar(x, df['Volume'], color=vol_colors, alpha=0.7, width=0.7)
    ax2.set_ylabel('Volume', color=WHITE, fontsize=9)
    step = max(1,len(df)//6)
    ticks = list(range(0,len(df),step))
    for ax in [ax2]:
        ax.set_xticks(ticks)
        ax.set_xticklabels([df.index[i].strftime('%b %Y') for i in ticks], rotation=30, ha='right', color=WHITE, fontsize=8)
    plt.tight_layout()
    return save_fig(fig, n)

def slide_014(n):
    """Time scale aggregation — daily/weekly/monthly"""
    df_d = get_stock_data('AAPL','2022-01-01','2024-12-31', fallback_n=600)
    df_w = df_d.resample('W').agg({'Open':'first','High':'max','Low':'min','Close':'last','Volume':'sum'}).dropna()
    df_m = df_d.resample('ME').agg({'Open':'first','High':'max','Low':'min','Close':'last','Volume':'sum'}).dropna()
    fig, axes = dark_fig(18,6,1,3)
    for ax, df, title in [(axes[0],df_d,'Daily (600 bars)'),
                           (axes[1],df_w,'Weekly (130 bars)'),
                           (axes[2],df_m,'Monthly (36 bars)')]:
        x = np.arange(len(df))
        draw_candles(ax, df)
        ax.set_title(title, fontsize=11, fontweight='bold')
    fig.suptitle('Same Data, Different Time Scales — AAPL 3-Year View', color=WHITE, fontsize=14, fontweight='bold')
    plt.tight_layout()
    return save_fig(fig, n)

def slide_015(n):
    """Normalized returns comparison"""
    tickers = ['AAPL','MSFT','NVDA','SPY']
    colors_t = [BULL, BLUE, ORANGE, RED]
    fig, ax = dark_fig(16,8)
    start = '2024-01-01'
    for ticker, color in zip(tickers, colors_t):
        df = get_stock_data(ticker, start, '2024-12-31', fallback_n=250)
        norm = (df['Close'] / df['Close'].iloc[0]) * 100
        x = np.arange(len(norm))
        ax.plot(x, norm.values, color=color, linewidth=2, label=ticker)
    ax.axhline(100, color='#555', linewidth=1, linestyle='--')
    ax.set_title('Multi-Asset Normalized Returns (Base = 100) — 2024', color=WHITE, fontsize=13)
    ax.set_ylabel('Normalized Price (100 = Start)', color=WHITE)
    ax.legend(facecolor='#2a2a2a', labelcolor=WHITE, fontsize=11)
    return save_fig(fig, n)

def slide_016(n):
    """Log vs linear scale"""
    df = get_stock_data('AAPL','2004-01-01','2024-12-31', fallback_n=5000)
    fig, (ax1, ax2) = dark_fig(16,7,1,2)
    x = np.arange(len(df))
    for ax, scale, title in [
        (ax1,'linear','Linear Scale — Recent moves look enormous'),
        (ax2,'log',   'Log Scale — Equal % moves shown equally')]:
        ax.plot(x, df['Close'].values, color=BULL, linewidth=1.2)
        ax.set_yscale(scale)
        ax.set_title(title, fontsize=11, fontweight='bold')
        step = max(1,len(df)//5)
        ticks = list(range(0,len(df),step))
        ax.set_xticks(ticks)
        ax.set_xticklabels([df.index[i].strftime('%Y') for i in ticks], rotation=30, ha='right', color=WHITE, fontsize=8)
    fig.suptitle('Logarithmic vs. Linear Price Scales — AAPL 20-Year View', color=WHITE, fontsize=14, fontweight='bold')
    plt.tight_layout()
    return save_fig(fig, n)

def slide_017(n):
    """Plotly interactive (static screenshot substitute)"""
    df = get_stock_data('AAPL','2024-01-01','2024-12-31', fallback_n=200)
    x = np.arange(len(df))
    fig, ax = dark_fig(16,8)
    draw_candles(ax, df)
    ax.set_title('Interactive Candlestick Chart with Plotly — Hover, Zoom, Range Slider', color=WHITE, fontsize=13)
    # Annotate interactive features
    for label, xi, yi, arrow_d in [
        ('Hover tooltip:\nshows OHLCV', 30, df['High'].iloc[30]*1.02, (0,15)),
        ('Zoom: click-drag\nany region',  100, df['Low'].iloc[100]*0.97, (0,-15)),
        ('Range slider\n(bottom)', len(df)-20, df['Close'].mean(), (0,0)),
    ]:
        ax.annotate(label, xy=(xi, yi), fontsize=9, color=YELLOW,
                    bbox=dict(boxstyle='round', fc='#333', alpha=0.8))
    return save_fig(fig, n)

def slide_018(n):
    """Common charting mistakes"""
    df = get_stock_data('AAPL','2024-01-01','2024-06-30', fallback_n=120)
    x = np.arange(len(df))
    fig, (ax1, ax2) = dark_fig(16,7,1,2)
    # Truncated y-axis (bad)
    close = df['Close'].values
    ax1.plot(x, close, color=BLUE, linewidth=2)
    mn, mx = close.min(), close.max()
    ax1.set_ylim(mn - 0.001*(mx-mn), mx + 0.001*(mx-mn))
    ax1.set_title('❌ Misleading: Truncated Y-axis\n(small move looks like a crash!)', color=BEAR, fontsize=11)
    # Proper scale (good)
    ax2.plot(x, close, color=BULL, linewidth=2)
    ax2.set_ylim(0, mx * 1.05)
    ax2.set_title('✅ Correct: Y-axis includes 0\n(actual scale shown)', color=BULL, fontsize=11)
    fig.suptitle('Common Charting Mistakes — Misleading Axes', color=WHITE, fontsize=14, fontweight='bold')
    for ax in [ax1,ax2]:
        step = max(1,len(df)//5)
        ticks = list(range(0,len(df),step))
        ax.set_xticks(ticks)
        ax.set_xticklabels([df.index[i].strftime('%b') for i in ticks], color=WHITE, fontsize=8)
    plt.tight_layout()
    return save_fig(fig, n)

def slide_022_023(n):
    """SMA visualization"""
    df = get_stock_data('AAPL','2023-01-01','2024-12-31', fallback_n=500)
    df['SMA20']  = df['Close'].rolling(20).mean()
    df['SMA50']  = df['Close'].rolling(50).mean()
    df['SMA200'] = df['Close'].rolling(200).mean()
    x = np.arange(len(df))
    fig, ax = dark_fig(16,8)
    ax.plot(x, df['Close'], color=WHITE, linewidth=0.7, alpha=0.5, label='Close')
    ax.plot(x, df['SMA20'],  color=BLUE,   linewidth=1.5, label='SMA 20')
    ax.plot(x, df['SMA50'],  color=ORANGE, linewidth=1.8, label='SMA 50')
    ax.plot(x, df['SMA200'], color=RED,    linewidth=2.2, label='SMA 200')
    ax.set_title('Simple Moving Averages — 20 / 50 / 200-Day — AAPL 2023–2024', color=WHITE, fontsize=13)
    ax.legend(facecolor='#2a2a2a', labelcolor=WHITE, fontsize=11)
    ax.set_ylabel('Price ($)', color=WHITE)
    step = max(1,len(df)//7)
    ticks = list(range(0,len(df),step))
    ax.set_xticks(ticks)
    ax.set_xticklabels([df.index[i].strftime('%b %Y') for i in ticks], rotation=30, ha='right', color=WHITE, fontsize=8)
    return save_fig(fig, n)

def slide_024_025(n):
    """SMA vs EMA comparison"""
    df = get_stock_data('AAPL','2024-01-01','2024-12-31', fallback_n=200)
    df['SMA20'] = df['Close'].rolling(20).mean()
    df['EMA12'] = df['Close'].ewm(span=12, adjust=False).mean()
    x = np.arange(len(df))
    fig, ax = dark_fig(16,8)
    ax.plot(x, df['Close'], color=WHITE, linewidth=0.7, alpha=0.5, label='Close')
    ax.plot(x, df['SMA20'], color=BLUE,   linewidth=1.8, linestyle='--', label='SMA 20 (equal weight, more lag)')
    ax.plot(x, df['EMA12'], color=ORANGE, linewidth=1.8, label='EMA 12 (recent-biased, more responsive)')
    ax.set_title('SMA vs EMA — Responsiveness Comparison\nEMA hugs price tighter; SMA lags but is calmer', color=WHITE, fontsize=12)
    ax.legend(facecolor='#2a2a2a', labelcolor=WHITE, fontsize=11)
    ax.set_ylabel('Price ($)', color=WHITE)
    step = max(1,len(df)//6)
    ticks = list(range(0,len(df),step))
    ax.set_xticks(ticks)
    ax.set_xticklabels([df.index[i].strftime('%b %Y') for i in ticks], rotation=30, ha='right', color=WHITE, fontsize=8)
    return save_fig(fig, n)

def slide_026(n):
    """Golden Cross / Death Cross"""
    df = get_stock_data('SPY','2018-01-01','2024-12-31', fallback_n=1500)
    df['SMA50']  = df['Close'].rolling(50).mean()
    df['SMA200'] = df['Close'].rolling(200).mean()
    df['above']  = (df['SMA50'] > df['SMA200']).astype(int)
    df['cross']  = df['above'].diff()
    golden = df[df['cross'] ==  1].index[:3]
    death  = df[df['cross'] == -1].index[:3]
    x = np.arange(len(df))
    fig, ax = dark_fig(18,8)
    ax.plot(x, df['Close'], color='#aaa', linewidth=0.8, alpha=0.6, label='SPY Close')
    ax.plot(x, df['SMA50'],  color=BLUE,   linewidth=1.5, label='SMA 50')
    ax.plot(x, df['SMA200'], color=RED,    linewidth=2.0, label='SMA 200')
    for d in golden:
        xi = df.index.get_loc(d)
        ax.axvline(xi, color=BULL, linewidth=2, alpha=0.8)
        ax.text(xi+1, df['Close'].iloc[xi]*0.96, 'Golden\nCross', color=BULL, fontsize=8)
    for d in death:
        xi = df.index.get_loc(d)
        ax.axvline(xi, color=BEAR, linewidth=2, alpha=0.8)
        ax.text(xi+1, df['Close'].iloc[xi]*1.03, 'Death\nCross', color=BEAR, fontsize=8)
    ax.set_title('SPY — Golden Cross & Death Cross Signals (SMA 50 vs SMA 200)', color=WHITE, fontsize=13)
    ax.legend(facecolor='#2a2a2a', labelcolor=WHITE, fontsize=10)
    step = max(1,len(df)//7)
    ticks = list(range(0,len(df),step))
    ax.set_xticks(ticks)
    ax.set_xticklabels([df.index[i].strftime('%Y') for i in ticks], rotation=30, ha='right', color=WHITE, fontsize=8)
    return save_fig(fig, n)

def slide_027(n):
    """WMA + MA ribbon"""
    df = get_stock_data('AAPL','2023-01-01','2024-12-31', fallback_n=500)
    periods = [5,10,20,50,100,200]
    ribbon_colors = ['#ff6b6b','#ffa07a','#ffd700','#98fb98','#87ceeb','#9370db']
    x = np.arange(len(df))
    fig, ax = dark_fig(16,8)
    ax.fill_between(x,
        df['Close'].rolling(5).mean().values,
        df['Close'].rolling(200).mean().values,
        alpha=0.07, color=BULL)
    for p, c in zip(periods, ribbon_colors):
        ma = df['Close'].rolling(p).mean()
        ax.plot(x, ma, color=c, linewidth=1.0, label=f'MA {p}', alpha=0.85)
    ax.plot(x, df['Close'], color=WHITE, linewidth=0.5, alpha=0.4)
    ax.set_title('Moving Average Ribbon — Spread = Trend Strength, Tangle = Consolidation', color=WHITE, fontsize=12)
    ax.legend(facecolor='#2a2a2a', labelcolor=WHITE, ncol=3, fontsize=9)
    step = max(1,len(df)//6)
    ticks = list(range(0,len(df),step))
    ax.set_xticks(ticks)
    ax.set_xticklabels([df.index[i].strftime('%b %Y') for i in ticks], rotation=30, ha='right', color=WHITE, fontsize=8)
    return save_fig(fig, n)

def slide_028(n):
    """VWAP diagram (synthetic intraday)"""
    np.random.seed(7)
    n_pts = 78  # ~6.5hr day, 5-min bars
    trend = np.cumsum(np.random.normal(0.0003, 0.003, n_pts)) * 100 + 175
    vol   = np.random.randint(500000, 3000000, n_pts).astype(float)
    vwap  = np.cumsum(trend * vol) / np.cumsum(vol)
    t = np.arange(n_pts)
    fig, ax = dark_fig(16,8)
    ax.plot(t, trend, color=WHITE, linewidth=1.2, alpha=0.7, label='Price (5-min)')
    ax.plot(t, vwap,  color=YELLOW, linewidth=2.5, label='VWAP')
    ax.fill_between(t, trend, vwap,
        where=(trend >= vwap), alpha=0.15, color=BULL, label='Price > VWAP (bullish)')
    ax.fill_between(t, trend, vwap,
        where=(trend <  vwap), alpha=0.15, color=BEAR, label='Price < VWAP (bearish)')
    ax.set_title('VWAP — Volume Weighted Average Price (Intraday)\nInstitutional benchmark: buy below VWAP, sell above', color=WHITE, fontsize=12)
    ax.set_xlabel('Time (5-min bars, single trading day)', color=WHITE)
    ax.legend(facecolor='#2a2a2a', labelcolor=WHITE, fontsize=10)
    return save_fig(fig, n)

def slide_029(n):
    """MA envelope bands"""
    df = get_stock_data('AAPL','2024-01-01','2024-12-31', fallback_n=200)
    k = 0.025
    df['MA']    = df['Close'].rolling(20).mean()
    df['Upper'] = df['MA'] * (1 + k)
    df['Lower'] = df['MA'] * (1 - k)
    x = np.arange(len(df))
    fig, ax = dark_fig(16,8)
    ax.plot(x, df['Close'], color=WHITE, linewidth=0.8, alpha=0.7)
    ax.plot(x, df['MA'],    color=YELLOW, linewidth=1.5, label='SMA 20')
    ax.plot(x, df['Upper'], color=BULL, linewidth=1.2, linestyle='--', label='Upper Band (+2.5%)')
    ax.plot(x, df['Lower'], color=BEAR, linewidth=1.2, linestyle='--', label='Lower Band (-2.5%)')
    ax.fill_between(x, df['Upper'], df['Lower'], alpha=0.05, color=BLUE)
    ax.set_title('MA Envelope Bands — Dynamic Support & Resistance Channel (SMA 20 ± 2.5%)', color=WHITE, fontsize=12)
    ax.legend(facecolor='#2a2a2a', labelcolor=WHITE, fontsize=10)
    step = max(1,len(df)//6)
    ticks = list(range(0,len(df),step))
    ax.set_xticks(ticks)
    ax.set_xticklabels([df.index[i].strftime('%b %Y') for i in ticks], rotation=30, ha='right', color=WHITE, fontsize=8)
    return save_fig(fig, n)

def slide_032_034(n):
    """Fibonacci retracement levels"""
    df = get_stock_data('AAPL','2024-01-01','2024-12-31', fallback_n=200)
    swing_low  = float(df['Close'].min())
    swing_high = float(df['Close'].max())
    ratios  = [0.0, 0.236, 0.382, 0.5, 0.618, 0.786, 1.0]
    levels  = {r: swing_high - (swing_high - swing_low) * r for r in ratios}
    fib_colors = {0.0:BULL, 0.236:BLUE, 0.382:YELLOW, 0.5:WHITE, 0.618:ORANGE, 0.786:BEAR, 1.0:PURPLE}
    x = np.arange(len(df))
    fig, ax = dark_fig(16,9)
    ax.plot(x, df['Close'], color=WHITE, linewidth=1.0, label='AAPL Close', zorder=5)
    ax.fill_between(x, levels[0.382], levels[0.618], alpha=0.08, color=ORANGE, label='Golden Zone (38.2%–61.8%)')
    for r, lvl in levels.items():
        c = fib_colors[r]
        ax.axhline(lvl, color=c, linewidth=1.5, linestyle='--', alpha=0.9)
        ax.text(len(df)*0.97, lvl, f'  {r:.1%}  ${lvl:.2f}', color=c, fontsize=9, va='center', fontweight='bold')
    ax.set_title('Fibonacci Retracement Levels — AAPL 2024\nHorizontal lines show potential support zones during pullbacks', color=WHITE, fontsize=12)
    ax.legend(facecolor='#2a2a2a', labelcolor=WHITE, fontsize=10)
    ax.set_ylabel('Price ($)', color=WHITE)
    step = max(1,len(df)//6)
    ticks = list(range(0,len(df),step))
    ax.set_xticks(ticks)
    ax.set_xticklabels([df.index[i].strftime('%b %Y') for i in ticks], rotation=30, ha='right', color=WHITE, fontsize=8)
    return save_fig(fig, n)

def slide_033(n):
    """Fibonacci extension"""
    df = get_stock_data('AAPL','2024-01-01','2024-12-31', fallback_n=200)
    swing_low  = float(df['Close'].min())
    swing_high = float(df['Close'].max())
    pullback   = swing_high - (swing_high - swing_low) * 0.382
    move = swing_high - swing_low
    ext = {f'{r*100:.1f}%': pullback + move * r for r in [1.272,1.618,2.0,2.618]}
    x = np.arange(len(df))
    fig, ax = dark_fig(16,9)
    ax.plot(x, df['Close'], color=WHITE, linewidth=1.0)
    ax.axhline(swing_high,  color=BULL,  linewidth=2.0, linestyle='-',  label=f'Swing High ${swing_high:.2f}')
    ax.axhline(swing_low,   color=BEAR,  linewidth=2.0, linestyle='-',  label=f'Swing Low ${swing_low:.2f}')
    ax.axhline(pullback,    color=YELLOW,linewidth=1.5, linestyle='--', label=f'Pullback (38.2%) ${pullback:.2f}')
    ext_colors = [ORANGE, PURPLE, '#00ced1', '#ff69b4']
    for (label, lvl), c in zip(ext.items(), ext_colors):
        ax.axhline(lvl, color=c, linewidth=1.2, linestyle='-.', alpha=0.85)
        ax.text(len(df)*0.97, lvl, f'  EXT {label}  ${lvl:.2f}', color=c, fontsize=9, va='center')
    ax.set_title('Fibonacci Extension Levels — Price Targets Beyond the Swing High', color=WHITE, fontsize=12)
    ax.legend(facecolor='#2a2a2a', labelcolor=WHITE, fontsize=10)
    step = max(1,len(df)//6)
    ticks = list(range(0,len(df),step))
    ax.set_xticks(ticks)
    ax.set_xticklabels([df.index[i].strftime('%b %Y') for i in ticks], rotation=30, ha='right', color=WHITE, fontsize=8)
    return save_fig(fig, n)

def slide_035_036(n, is_fan=True):
    """Fibonacci fan (35) or time zones (36)"""
    df = get_stock_data('AAPL','2024-01-01','2024-12-31', fallback_n=200)
    x = np.arange(len(df))
    fig, ax = dark_fig(16,8)
    ax.plot(x, df['Close'], color=WHITE, linewidth=1.0, alpha=0.8)
    if is_fan:
        anchor_i = df['Close'].idxmin()
        anchor_xi = df.index.get_loc(anchor_i)
        anchor_y  = float(df.loc[anchor_i,'Close'])
        end_y     = float(df['Close'].max())
        for ratio, color in [(0.382,BULL),(0.5,YELLOW),(0.618,ORANGE)]:
            fan_end_y = anchor_y + (end_y - anchor_y) * ratio
            ax.plot([anchor_xi, len(df)-1], [anchor_y, fan_end_y],
                    color=color, linewidth=1.8, label=f'Fan {ratio:.1%}')
        ax.scatter([anchor_xi],[anchor_y], color=BEAR, s=100, zorder=6)
        ax.set_title('Fibonacci Fan Lines — Diagonal Time-Adjusted Support/Resistance', color=WHITE, fontsize=12)
    else:
        fib_nums = [1,2,3,5,8,13,21,34,55]
        anchor_xi = df['Close'].values.argmin()
        for i, fib in enumerate(fib_nums):
            xi = anchor_xi + fib
            if xi < len(df):
                ax.axvline(xi, color=YELLOW, linewidth=1.0, linestyle='--', alpha=0.8-i*0.07)
                ax.text(xi, float(df['Close'].max())*0.98, str(fib),
                        color=YELLOW, fontsize=8, ha='center')
        ax.set_title('Fibonacci Time Zones — Vertical Lines at Fibonacci-Interval Days', color=WHITE, fontsize=12)
    ax.legend(facecolor='#2a2a2a', labelcolor=WHITE, fontsize=10)
    step = max(1,len(df)//6)
    ticks = list(range(0,len(df),step))
    ax.set_xticks(ticks)
    ax.set_xticklabels([df.index[i].strftime('%b %Y') for i in ticks], rotation=30, ha='right', color=WHITE, fontsize=8)
    return save_fig(fig, n)

def slide_037_038(n):
    """MA crossover strategy with buy/sell arrows"""
    df = get_stock_data('AAPL','2022-01-01','2024-12-31', fallback_n=700)
    df['SMA20'] = df['Close'].rolling(20).mean()
    df['SMA50'] = df['Close'].rolling(50).mean()
    df['above'] = (df['SMA20'] > df['SMA50']).astype(int)
    df['cross'] = df['above'].diff()
    buys  = df[df['cross'] ==  1]
    sells = df[df['cross'] == -1]
    x = np.arange(len(df))
    xi_map = {d: i for i, d in enumerate(df.index)}
    fig, ax = dark_fig(18,8)
    ax.plot(x, df['Close'], color=WHITE, linewidth=0.7, alpha=0.5)
    ax.plot(x, df['SMA20'], color=BLUE,   linewidth=1.5, label='SMA 20')
    ax.plot(x, df['SMA50'], color=ORANGE, linewidth=1.8, label='SMA 50')
    for d in buys.index:
        xi = xi_map.get(d, None)
        if xi: ax.scatter([xi],[df.loc[d,'SMA20']*0.96], marker='^', color=BULL, s=120, zorder=5)
    for d in sells.index:
        xi = xi_map.get(d, None)
        if xi: ax.scatter([xi],[df.loc[d,'SMA20']*1.04], marker='v', color=BEAR, s=120, zorder=5)
    ax.scatter([],[], marker='^', color=BULL, s=80, label='BUY Signal (SMA20 cross above SMA50)')
    ax.scatter([],[], marker='v', color=BEAR, s=80, label='SELL Signal (SMA20 cross below SMA50)')
    ax.set_title('SMA 20/50 Crossover Strategy — Entry & Exit Signals Visualized', color=WHITE, fontsize=12)
    ax.legend(facecolor='#2a2a2a', labelcolor=WHITE, fontsize=10)
    step = max(1,len(df)//7)
    ticks = list(range(0,len(df),step))
    ax.set_xticks(ticks)
    ax.set_xticklabels([df.index[i].strftime('%b %Y') for i in ticks], rotation=30, ha='right', color=WHITE, fontsize=8)
    return save_fig(fig, n)

def slide_039(n):
    """Whipsaw in ranging market vs trending"""
    df_trend  = get_stock_data('NVDA','2023-01-01','2023-07-31', fallback_n=150)
    df_range  = synthetic_ohlcv(150, seed=99, trend=0.0, vol=0.01)
    fig, (ax1, ax2) = dark_fig(16,7,1,2)
    for ax, df, title in [
        (ax1, df_trend, 'Trending Market — MA signals work well'),
        (ax2, df_range, 'Ranging Market — MA signals whipsaw (all false)')]:
        x = np.arange(len(df))
        ax.plot(x, df['Close'], color=WHITE, linewidth=0.8, alpha=0.6)
        ax.plot(x, df['Close'].rolling(20).mean(), color=BLUE, linewidth=1.5, label='SMA 20')
        ax.plot(x, df['Close'].rolling(50).mean(), color=ORANGE, linewidth=1.5, label='SMA 50')
        ax.set_title(title, fontsize=11, fontweight='bold')
        ax.legend(facecolor='#2a2a2a', labelcolor=WHITE, fontsize=9)
    fig.suptitle('When Moving Averages Mislead — Ranging vs. Trending Markets', color=WHITE, fontsize=13, fontweight='bold')
    plt.tight_layout()
    return save_fig(fig, n)

def slide_041_058(n):
    """Full 4-panel trading dashboard"""
    df = get_stock_data('AAPL','2024-01-01','2024-12-31', fallback_n=200)
    df['SMA20']   = df['Close'].rolling(20).mean()
    df['BB_mid']  = df['SMA20']
    df['BB_std']  = df['Close'].rolling(20).std()
    df['BB_upper']= df['BB_mid'] + 2*df['BB_std']
    df['BB_lower']= df['BB_mid'] - 2*df['BB_std']
    df['RSI']     = calc_rsi(df['Close'])
    df['MACD'], df['Signal'], df['Hist'] = calc_macd(df['Close'])
    x = np.arange(len(df))
    fig = plt.figure(figsize=(20,14)); fig.set_facecolor(BG)
    gs = gridspec.GridSpec(4,1,height_ratios=[5,1.5,1.5,1.5],hspace=0.04)
    ax_p = fig.add_subplot(gs[0])
    ax_v = fig.add_subplot(gs[1])
    ax_r = fig.add_subplot(gs[2])
    ax_m = fig.add_subplot(gs[3])
    for ax in [ax_p,ax_v,ax_r,ax_m]:
        ax.set_facecolor(BG2)
        ax.tick_params(colors=WHITE, labelsize=8)
        ax.grid(True,alpha=0.12,color='#333')
    # Price
    draw_candles(ax_p, df)
    ax_p.plot(x, df['SMA20'],   color=YELLOW, linewidth=1.2, linestyle='--', label='SMA 20')
    ax_p.plot(x, df['BB_upper'],color=BLUE,   linewidth=0.9, linestyle=':')
    ax_p.plot(x, df['BB_lower'],color=BLUE,   linewidth=0.9, linestyle=':')
    ax_p.fill_between(x, df['BB_upper'],df['BB_lower'],alpha=0.04,color=BLUE)
    ax_p.set_title('AAPL — Complete 4-Panel Trading Dashboard', color=WHITE, fontsize=14, fontweight='bold')
    ax_p.legend(facecolor='#2a2a2a',labelcolor=WHITE,fontsize=9)
    # Volume
    vc = [BULL if c>=o else BEAR for c,o in zip(df['Close'],df['Open'])]
    ax_v.bar(x, df['Volume'], color=vc, alpha=0.7, width=0.7)
    ax_v.set_ylabel('Volume', color=WHITE, fontsize=8)
    # RSI
    ax_r.plot(x, df['RSI'], color=PURPLE, linewidth=1.5)
    ax_r.axhline(70, color=BEAR, linewidth=0.9, linestyle='--')
    ax_r.axhline(30, color=BULL, linewidth=0.9, linestyle='--')
    ax_r.fill_between(x, df['RSI'],70, where=(df['RSI']>=70), alpha=0.2, color=BEAR)
    ax_r.fill_between(x, df['RSI'],30, where=(df['RSI']<=30), alpha=0.2, color=BULL)
    ax_r.set_ylim(0,100); ax_r.set_ylabel('RSI', color=WHITE, fontsize=8)
    # MACD
    hc = [BULL if v>=0 else BEAR for v in df['Hist']]
    ax_m.bar(x, df['Hist'], color=hc, alpha=0.7, width=0.7)
    ax_m.plot(x, df['MACD'],   color=BLUE,   linewidth=1.3)
    ax_m.plot(x, df['Signal'], color=ORANGE, linewidth=1.3)
    ax_m.axhline(0, color=GRAY, linewidth=0.6)
    ax_m.set_ylabel('MACD', color=WHITE, fontsize=8)
    plt.setp(ax_p.get_xticklabels(), visible=False)
    plt.setp(ax_v.get_xticklabels(), visible=False)
    plt.setp(ax_r.get_xticklabels(), visible=False)
    plt.tight_layout()
    return save_fig(fig, n)

def slide_042_044(n):
    """RSI panel"""
    df = get_stock_data('AAPL','2024-01-01','2024-12-31', fallback_n=200)
    df['RSI'] = calc_rsi(df['Close'])
    x = np.arange(len(df))
    fig = plt.figure(figsize=(16,9)); fig.set_facecolor(BG)
    gs = gridspec.GridSpec(2,1,height_ratios=[3,1.5],hspace=0.05)
    ax1 = fig.add_subplot(gs[0]); ax2 = fig.add_subplot(gs[1])
    for ax in [ax1,ax2]:
        ax.set_facecolor(BG2); ax.tick_params(colors=WHITE,labelsize=8); ax.grid(True,alpha=0.12,color='#333')
    ax1.plot(x, df['Close'], color=WHITE, linewidth=1.0)
    ax1.set_title('RSI — Relative Strength Index (14-day) — Momentum Oscillator', color=WHITE, fontsize=13)
    ax2.plot(x, df['RSI'], color=PURPLE, linewidth=1.5, label='RSI 14')
    ax2.axhline(70, color=BEAR, linewidth=1.0, linestyle='--', label='Overbought (70)')
    ax2.axhline(50, color=GRAY, linewidth=0.7, linestyle=':', alpha=0.5)
    ax2.axhline(30, color=BULL, linewidth=1.0, linestyle='--', label='Oversold (30)')
    ax2.fill_between(x, df['RSI'],70, where=(df['RSI']>=70), alpha=0.25, color=BEAR)
    ax2.fill_between(x, df['RSI'],30, where=(df['RSI']<=30), alpha=0.25, color=BULL)
    ax2.set_ylim(0,100)
    ax2.legend(facecolor='#2a2a2a',labelcolor=WHITE,fontsize=9)
    ax2.set_ylabel('RSI', color=WHITE, fontsize=9)
    plt.setp(ax1.get_xticklabels(), visible=False)
    step = max(1,len(df)//6)
    ticks = list(range(0,len(df),step))
    ax2.set_xticks(ticks)
    ax2.set_xticklabels([df.index[i].strftime('%b %Y') for i in ticks], rotation=30, ha='right', color=WHITE, fontsize=8)
    plt.tight_layout()
    return save_fig(fig, n)

def slide_045_047(n):
    """MACD panel"""
    df = get_stock_data('AAPL','2024-01-01','2024-12-31', fallback_n=200)
    df['MACD'], df['Signal'], df['Hist'] = calc_macd(df['Close'])
    x = np.arange(len(df))
    fig = plt.figure(figsize=(16,9)); fig.set_facecolor(BG)
    gs = gridspec.GridSpec(2,1,height_ratios=[3,1.5],hspace=0.05)
    ax1 = fig.add_subplot(gs[0]); ax2 = fig.add_subplot(gs[1])
    for ax in [ax1,ax2]:
        ax.set_facecolor(BG2); ax.tick_params(colors=WHITE,labelsize=8); ax.grid(True,alpha=0.12,color='#333')
    ax1.plot(x, df['Close'], color=WHITE, linewidth=1.0)
    ax1.set_title('MACD — Moving Average Convergence/Divergence (12,26,9)', color=WHITE, fontsize=13)
    hc = [BULL if v>=0 else BEAR for v in df['Hist']]
    ax2.bar(x, df['Hist'], color=hc, alpha=0.75, width=0.7, label='Histogram')
    ax2.plot(x, df['MACD'],   color=BLUE,   linewidth=1.4, label='MACD Line')
    ax2.plot(x, df['Signal'], color=ORANGE, linewidth=1.4, label='Signal Line')
    ax2.axhline(0, color=GRAY, linewidth=0.8, linestyle='-')
    ax2.legend(facecolor='#2a2a2a',labelcolor=WHITE,fontsize=9)
    ax2.set_ylabel('MACD', color=WHITE, fontsize=9)
    plt.setp(ax1.get_xticklabels(), visible=False)
    step = max(1,len(df)//6)
    ticks = list(range(0,len(df),step))
    ax2.set_xticks(ticks)
    ax2.set_xticklabels([df.index[i].strftime('%b %Y') for i in ticks], rotation=30, ha='right', color=WHITE, fontsize=8)
    plt.tight_layout()
    return save_fig(fig, n)

def slide_048_050(n):
    """Bollinger Bands"""
    df = get_stock_data('AAPL','2024-01-01','2024-12-31', fallback_n=200)
    df['BB_mid']  = df['Close'].rolling(20).mean()
    df['BB_std']  = df['Close'].rolling(20).std()
    df['BB_upper']= df['BB_mid'] + 2*df['BB_std']
    df['BB_lower']= df['BB_mid'] - 2*df['BB_std']
    df['BB_width']= (df['BB_upper']-df['BB_lower'])/df['BB_mid']
    x = np.arange(len(df))
    fig = plt.figure(figsize=(16,10)); fig.set_facecolor(BG)
    gs = gridspec.GridSpec(2,1,height_ratios=[4,1],hspace=0.05)
    ax1 = fig.add_subplot(gs[0]); ax2 = fig.add_subplot(gs[1])
    for ax in [ax1,ax2]:
        ax.set_facecolor(BG2); ax.tick_params(colors=WHITE,labelsize=8); ax.grid(True,alpha=0.12,color='#333')
    ax1.plot(x, df['Close'],    color=WHITE, linewidth=0.9, alpha=0.8)
    ax1.plot(x, df['BB_mid'],   color=YELLOW, linewidth=1.5, label='Middle (SMA 20)')
    ax1.plot(x, df['BB_upper'], color=BLUE,   linewidth=1.2, linestyle='-', label='Upper (+2σ)')
    ax1.plot(x, df['BB_lower'], color=BLUE,   linewidth=1.2, linestyle='-', label='Lower (-2σ)')
    ax1.fill_between(x, df['BB_upper'],df['BB_lower'], alpha=0.06, color=BLUE)
    ax1.set_title('Bollinger Bands (20, 2σ) — Dynamic Volatility Channel', color=WHITE, fontsize=13)
    ax1.legend(facecolor='#2a2a2a',labelcolor=WHITE,fontsize=9)
    ax2.plot(x, df['BB_width'], color=PURPLE, linewidth=1.5, label='Band Width')
    ax2.fill_between(x, df['BB_width'], df['BB_width'].min(), alpha=0.2, color=PURPLE)
    ax2.set_ylabel('Width', color=WHITE, fontsize=8)
    ax2.legend(facecolor='#2a2a2a',labelcolor=WHITE,fontsize=9)
    plt.setp(ax1.get_xticklabels(), visible=False)
    step = max(1,len(df)//6)
    ticks = list(range(0,len(df),step))
    ax2.set_xticks(ticks)
    ax2.set_xticklabels([df.index[i].strftime('%b %Y') for i in ticks], rotation=30, ha='right', color=WHITE, fontsize=8)
    plt.tight_layout()
    return save_fig(fig, n)

def slide_051_052(n):
    """Stochastic oscillator"""
    df = get_stock_data('AAPL','2024-01-01','2024-12-31', fallback_n=200)
    lows  = df['Low'].rolling(14).min()
    highs = df['High'].rolling(14).max()
    k_raw = 100*(df['Close']-lows)/(highs-lows)
    df['Stoch_K'] = k_raw.rolling(3).mean()
    df['Stoch_D'] = df['Stoch_K'].rolling(3).mean()
    x = np.arange(len(df))
    fig = plt.figure(figsize=(16,9)); fig.set_facecolor(BG)
    gs = gridspec.GridSpec(2,1,height_ratios=[3,1.5],hspace=0.05)
    ax1=fig.add_subplot(gs[0]); ax2=fig.add_subplot(gs[1])
    for ax in [ax1,ax2]:
        ax.set_facecolor(BG2); ax.tick_params(colors=WHITE,labelsize=8); ax.grid(True,alpha=0.12,color='#333')
    ax1.plot(x, df['Close'], color=WHITE, linewidth=1.0)
    ax1.set_title('Stochastic Oscillator — Where Did Close Sit Within the Range?', color=WHITE, fontsize=12)
    ax2.plot(x, df['Stoch_K'], color=BLUE,   linewidth=1.5, label='%K')
    ax2.plot(x, df['Stoch_D'], color=ORANGE, linewidth=1.5, label='%D (signal)')
    ax2.axhline(80, color=BEAR, linewidth=1.0, linestyle='--', label='Overbought (80)')
    ax2.axhline(20, color=BULL, linewidth=1.0, linestyle='--', label='Oversold (20)')
    ax2.fill_between(x, df['Stoch_K'],80, where=(df['Stoch_K']>=80), alpha=0.2, color=BEAR)
    ax2.fill_between(x, df['Stoch_K'],20, where=(df['Stoch_K']<=20), alpha=0.2, color=BULL)
    ax2.set_ylim(0,100)
    ax2.legend(facecolor='#2a2a2a',labelcolor=WHITE,fontsize=9)
    plt.setp(ax1.get_xticklabels(), visible=False)
    step = max(1,len(df)//6)
    ticks = list(range(0,len(df),step))
    ax2.set_xticks(ticks)
    ax2.set_xticklabels([df.index[i].strftime('%b %Y') for i in ticks], rotation=30, ha='right', color=WHITE, fontsize=8)
    plt.tight_layout()
    return save_fig(fig, n)

def slide_053_054(n):
    """ATR"""
    df = get_stock_data('AAPL','2024-01-01','2024-12-31', fallback_n=200)
    tr1 = df['High']-df['Low']
    tr2 = abs(df['High']-df['Close'].shift(1))
    tr3 = abs(df['Low'] -df['Close'].shift(1))
    df['ATR'] = pd.concat([tr1,tr2,tr3],axis=1).max(axis=1).ewm(com=13,min_periods=14).mean()
    x = np.arange(len(df))
    fig = plt.figure(figsize=(16,9)); fig.set_facecolor(BG)
    gs = gridspec.GridSpec(2,1,height_ratios=[3,1.5],hspace=0.05)
    ax1=fig.add_subplot(gs[0]); ax2=fig.add_subplot(gs[1])
    for ax in [ax1,ax2]:
        ax.set_facecolor(BG2); ax.tick_params(colors=WHITE,labelsize=8); ax.grid(True,alpha=0.12,color='#333')
    ax1.plot(x, df['Close'], color=WHITE, linewidth=1.0)
    ax1.set_title('ATR — Average True Range (14): Volatility Without Direction', color=WHITE, fontsize=12)
    ax2.plot(x, df['ATR'], color=RED, linewidth=1.5, label='ATR 14')
    ax2.fill_between(x, df['ATR'], df['ATR'].min(), alpha=0.2, color=RED)
    ax2.axhline(df['ATR'].mean(), color=YELLOW, linewidth=1.0, linestyle='--',
                label=f"Avg ATR: ${df['ATR'].mean():.2f}")
    ax2.set_ylabel('ATR ($)', color=WHITE, fontsize=8)
    ax2.legend(facecolor='#2a2a2a',labelcolor=WHITE,fontsize=9)
    plt.setp(ax1.get_xticklabels(), visible=False)
    step = max(1,len(df)//6)
    ticks = list(range(0,len(df),step))
    ax2.set_xticks(ticks)
    ax2.set_xticklabels([df.index[i].strftime('%b %Y') for i in ticks], rotation=30, ha='right', color=WHITE, fontsize=8)
    plt.tight_layout()
    return save_fig(fig, n)

def slide_055(n):
    """OBV"""
    df = get_stock_data('AAPL','2024-01-01','2024-12-31', fallback_n=200)
    obv = [0]
    for i in range(1, len(df)):
        if df['Close'].iloc[i] > df['Close'].iloc[i-1]:
            obv.append(obv[-1] + df['Volume'].iloc[i])
        elif df['Close'].iloc[i] < df['Close'].iloc[i-1]:
            obv.append(obv[-1] - df['Volume'].iloc[i])
        else:
            obv.append(obv[-1])
    df['OBV'] = obv
    x = np.arange(len(df))
    fig = plt.figure(figsize=(16,9)); fig.set_facecolor(BG)
    gs = gridspec.GridSpec(2,1,height_ratios=[3,1.5],hspace=0.05)
    ax1=fig.add_subplot(gs[0]); ax2=fig.add_subplot(gs[1])
    for ax in [ax1,ax2]:
        ax.set_facecolor(BG2); ax.tick_params(colors=WHITE,labelsize=8); ax.grid(True,alpha=0.12,color='#333')
    ax1.plot(x, df['Close'], color=WHITE, linewidth=1.0)
    ax1.set_title('On-Balance Volume (OBV) — Cumulative Buy vs. Sell Volume', color=WHITE, fontsize=12)
    ax2.plot(x, df['OBV'], color=ORANGE, linewidth=1.5)
    ax2.fill_between(x, df['OBV'], 0, where=(np.array(df['OBV'])>=0), alpha=0.2, color=BULL)
    ax2.fill_between(x, df['OBV'], 0, where=(np.array(df['OBV'])< 0), alpha=0.2, color=BEAR)
    ax2.axhline(0, color=GRAY, linewidth=0.8, linestyle='--')
    ax2.set_ylabel('OBV', color=WHITE, fontsize=8)
    plt.setp(ax1.get_xticklabels(), visible=False)
    step = max(1,len(df)//6)
    ticks = list(range(0,len(df),step))
    ax2.set_xticks(ticks)
    ax2.set_xticklabels([df.index[i].strftime('%b %Y') for i in ticks], rotation=30, ha='right', color=WHITE, fontsize=8)
    plt.tight_layout()
    return save_fig(fig, n)

def slide_056(n):
    """Volume Profile"""
    df = get_stock_data('AAPL','2024-01-01','2024-12-31', fallback_n=200)
    n_bins = 40
    pmin, pmax = float(df['Low'].min()), float(df['High'].max())
    bins = np.linspace(pmin, pmax, n_bins+1)
    centers = (bins[:-1]+bins[1:])/2
    vp = np.zeros(n_bins)
    for _, row in df.iterrows():
        mask = (centers >= row['Low']) & (centers <= row['High'])
        if mask.sum()>0: vp[mask] += row['Volume']/mask.sum()
    vp_norm = vp/vp.max()
    poc = centers[vp.argmax()]
    x = np.arange(len(df))
    fig, ax = dark_fig(16,9)
    ax.plot(x, df['Close'], color=WHITE, linewidth=1.0, label='Close', zorder=5)
    ax_r = ax.twinx()
    ax_r.barh(centers, vp_norm*0.25, height=(pmax-pmin)/n_bins,
              left=len(df)*0.75, color=BLUE, alpha=0.5)
    ax_r.set_facecolor(BG2)
    ax.axhline(poc, color=YELLOW, linewidth=2, linestyle='-', label=f'POC: ${poc:.2f}', zorder=6)
    ax.set_title('Volume Profile — Where Trading Activity Concentrates\n(Horizontal histogram: most volume by price level)', color=WHITE, fontsize=11)
    ax.legend(facecolor='#2a2a2a',labelcolor=WHITE,fontsize=10)
    ax.set_ylabel('Price ($)', color=WHITE)
    ax_r.set_ylabel('Volume Profile', color=WHITE)
    ax_r.tick_params(colors=WHITE)
    step = max(1,len(df)//6)
    ticks = list(range(0,len(df),step))
    ax.set_xticks(ticks)
    ax.set_xticklabels([df.index[i].strftime('%b %Y') for i in ticks], rotation=30, ha='right', color=WHITE, fontsize=8)
    return save_fig(fig, n)

def slide_057(n):
    """VWAP deviation bands"""
    np.random.seed(5)
    n_pts = 78
    closes = np.cumsum(np.random.normal(0,0.003,n_pts))*100+175
    vols   = np.random.randint(500000,3000000,n_pts).astype(float)
    vwap   = np.cumsum(closes*vols)/np.cumsum(vols)
    dev    = np.array([np.std(closes[:i+1]) if i>0 else 0 for i in range(n_pts)])
    t = np.arange(n_pts)
    fig, ax = dark_fig(16,8)
    ax.plot(t, closes, color=WHITE, linewidth=1.2, alpha=0.8, label='Price (5-min)')
    ax.plot(t, vwap,   color=YELLOW, linewidth=2.5, label='VWAP')
    ax.plot(t, vwap+1*dev, color=BULL, linewidth=1.2, linestyle='--', label='VWAP +1σ')
    ax.plot(t, vwap-1*dev, color=BULL, linewidth=1.2, linestyle='--', label='VWAP -1σ')
    ax.plot(t, vwap+2*dev, color=BEAR, linewidth=1.0, linestyle=':', label='VWAP +2σ')
    ax.plot(t, vwap-2*dev, color=BEAR, linewidth=1.0, linestyle=':', label='VWAP -2σ')
    ax.fill_between(t, vwap+1*dev, vwap-1*dev, alpha=0.07, color=BULL)
    ax.set_title('VWAP Deviation Bands — Intraday Institutional Buy/Sell Zones', color=WHITE, fontsize=12)
    ax.legend(facecolor='#2a2a2a',labelcolor=WHITE,fontsize=9, ncol=3)
    ax.set_xlabel('Time (5-min bars)', color=WHITE)
    return save_fig(fig, n)

def slide_059(n):
    """RSI + MACD combined signals"""
    df = get_stock_data('AAPL','2024-01-01','2024-12-31', fallback_n=200)
    df['RSI']  = calc_rsi(df['Close'])
    df['MACD'], df['Signal'], df['Hist'] = calc_macd(df['Close'])
    x = np.arange(len(df))
    fig = plt.figure(figsize=(16,12)); fig.set_facecolor(BG)
    gs = gridspec.GridSpec(3,1,height_ratios=[4,1.5,1.5],hspace=0.05)
    ax1=fig.add_subplot(gs[0]); ax2=fig.add_subplot(gs[1]); ax3=fig.add_subplot(gs[2])
    for ax in [ax1,ax2,ax3]:
        ax.set_facecolor(BG2); ax.tick_params(colors=WHITE,labelsize=8); ax.grid(True,alpha=0.12,color='#333')
    ax1.plot(x, df['Close'], color=WHITE, linewidth=1.0)
    ax1.set_title('RSI + MACD Confluence — When Two Signals Agree', color=WHITE, fontsize=13)
    ax2.plot(x, df['RSI'], color=PURPLE, linewidth=1.5)
    ax2.axhline(70,color=BEAR,linewidth=0.9,linestyle='--'); ax2.axhline(30,color=BULL,linewidth=0.9,linestyle='--')
    ax2.fill_between(x,df['RSI'],70,where=(df['RSI']>=70),alpha=0.2,color=BEAR)
    ax2.fill_between(x,df['RSI'],30,where=(df['RSI']<=30),alpha=0.2,color=BULL)
    ax2.set_ylim(0,100); ax2.set_ylabel('RSI',color=WHITE,fontsize=8)
    hc=[BULL if v>=0 else BEAR for v in df['Hist']]
    ax3.bar(x,df['Hist'],color=hc,alpha=0.7,width=0.7)
    ax3.plot(x,df['MACD'],color=BLUE,linewidth=1.3)
    ax3.plot(x,df['Signal'],color=ORANGE,linewidth=1.3)
    ax3.axhline(0,color=GRAY,linewidth=0.6); ax3.set_ylabel('MACD',color=WHITE,fontsize=8)
    plt.setp(ax1.get_xticklabels(),visible=False); plt.setp(ax2.get_xticklabels(),visible=False)
    step = max(1,len(df)//6)
    ticks = list(range(0,len(df),step))
    ax3.set_xticks(ticks)
    ax3.set_xticklabels([df.index[i].strftime('%b %Y') for i in ticks], rotation=30, ha='right', color=WHITE, fontsize=8)
    plt.tight_layout()
    return save_fig(fig, n)

def slide_062_070(n):
    """Chart pattern diagram — generic patterns"""
    t = np.linspace(0,12,300)
    fig, ax = dark_fig(14,8)
    # Head and Shoulders by default for 62, can be reused
    hs_y = (80 + 12*np.exp(-((t-2)**2)/0.5) + 18*np.exp(-((t-6)**2)/0.7) + 12*np.exp(-((t-10)**2)/0.5))
    nk   = 88.0
    breakdown = np.where(t>11, nk - (t-11)*8, hs_y)
    price = np.minimum(hs_y, breakdown)
    ax.plot(t, price, color=WHITE, linewidth=2.5)
    ax.axhline(nk, color=YELLOW, linewidth=2, linestyle='--', label=f'Neckline: ${nk:.0f}')
    for label, tx, ty in [('Left\nShoulder',2,103),('Head',6,100),('Right\nShoulder',10,103)]:
        ax.text(tx, ty, label, color=BLUE, ha='center', fontsize=11, fontweight='bold',
                bbox=dict(boxstyle='round', fc='#1e1e1e', ec=BLUE, alpha=0.8))
    ax.annotate('SELL\n(break below neckline)', xy=(11.5, nk-5),
                xytext=(10.5, nk+8), color=BEAR, fontsize=11, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=BEAR, lw=2))
    ax.set_title('Head and Shoulders — Bearish Reversal Pattern', color=WHITE, fontsize=14)
    ax.legend(facecolor='#2a2a2a', labelcolor=WHITE, fontsize=11)
    ax.set_ylabel('Price', color=WHITE)
    ax.set_xlim(0,13)
    return save_fig(fig, n)

def slide_063(n):
    """Inverse H&S"""
    t = np.linspace(0,12,300)
    nk = 112.0
    inv_y = nk - (12*np.exp(-((t-2)**2)/0.5) + 18*np.exp(-((t-6)**2)/0.7) + 12*np.exp(-((t-10)**2)/0.5))
    breakout = np.where(t>11, nk + (t-11)*8, inv_y)
    price = np.maximum(inv_y, breakout)
    fig, ax = dark_fig(14,8)
    ax.plot(t, price, color=WHITE, linewidth=2.5)
    ax.axhline(nk, color=YELLOW, linewidth=2, linestyle='--', label='Neckline')
    for label, tx, ty in [('Left\nShoulder',2,nk-9),('Head\n(lowest)',6,nk-18),('Right\nShoulder',10,nk-9)]:
        ax.text(tx, ty, label, color=BLUE, ha='center', fontsize=11, fontweight='bold',
                bbox=dict(boxstyle='round', fc='#1e1e1e', ec=BLUE, alpha=0.8))
    ax.annotate('BUY!\n(break above neckline)', xy=(11.5, nk+5),
                xytext=(10, nk+12), color=BULL, fontsize=11, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=BULL, lw=2))
    ax.set_title('Inverse Head and Shoulders — Bullish Reversal Pattern', color=WHITE, fontsize=13)
    ax.legend(facecolor='#2a2a2a', labelcolor=WHITE, fontsize=11)
    ax.set_ylabel('Price', color=WHITE)
    return save_fig(fig, n)

def slide_064(n):
    """Cup and Handle"""
    t = np.linspace(0,15,500)
    cup_y = 100 + 20*((t-7)/7)**2 - 20
    cup_y = np.clip(cup_y, 80, 102)
    handle_mask = (t>=11)&(t<=13.5)
    cup_y[handle_mask] -= 5*np.exp(-((t[handle_mask]-12.25)**2)/0.4)
    cup_y[t>=13.5] = 100 + (t[t>=13.5]-13.5)*5
    fig, ax = dark_fig(14,8)
    ax.plot(t, cup_y, color=WHITE, linewidth=2.5, label='Price')
    ax.axhline(100, color=YELLOW, linewidth=2, linestyle='--', label='Rim Level (resistance→support)')
    cup_mask = (t>=2)&(t<=12)
    ax.fill_between(t[cup_mask], cup_y[cup_mask], 100, alpha=0.1, color=BLUE)
    ax.text(7, 83, 'Cup\n(U-shaped)', color=BLUE, ha='center', fontsize=11)
    ax.text(12.25, 91, 'Handle\n(slight pullback)', color=ORANGE, ha='center', fontsize=11)
    ax.text(14, 107, 'Breakout!', color=BULL, ha='center', fontsize=12, fontweight='bold')
    ax.set_title('Cup and Handle — Bullish Continuation Pattern', color=WHITE, fontsize=13)
    ax.legend(facecolor='#2a2a2a', labelcolor=WHITE, fontsize=11)
    ax.set_ylabel('Price', color=WHITE)
    return save_fig(fig, n)

def slide_065(n):
    """Triangles"""
    t = np.linspace(0,10,200)
    fig, axes = dark_fig(18,6,1,3)
    data = [
        ('Symmetrical Triangle\n(Neutral bias)',
         100+t*1.5, 110-t*1.5,
         100+8*np.sin(t*2)*np.exp(-t*0.15)),
        ('Ascending Triangle\n(Bullish bias)',
         np.full_like(t,108), 90+t*1.5,
         100+8*np.sin(t*2)*np.exp(-t*0.1)+t*0.5),
        ('Descending Triangle\n(Bearish bias)',
         110-t*1.5, np.full_like(t,92),
         100+8*np.sin(t*2)*np.exp(-t*0.1)-t*0.3),
    ]
    for ax, (title, upper, lower, price) in zip(axes, data):
        ax.plot(t, price, color=WHITE, linewidth=1.5)
        ax.plot(t, upper, color=BEAR, linewidth=2, linestyle='--', label='Resistance')
        ax.plot(t, lower, color=BULL, linewidth=2, linestyle='--', label='Support')
        ax.set_title(title, fontsize=11, fontweight='bold')
        ax.legend(facecolor='#2a2a2a', labelcolor=WHITE, fontsize=8)
    fig.suptitle('Triangle Patterns — Markets Coiling Before a Breakout', color=WHITE, fontsize=14, fontweight='bold')
    plt.tight_layout()
    return save_fig(fig, n)

def slide_066(n):
    """Flags & Pennants"""
    t = np.linspace(0,12,400)
    pole = np.where(t<3, 90+t*8, None)
    flag_top  = np.where((t>=3)&(t<=7), 114-(t-3)*1.5, None)
    flag_bot  = np.where((t>=3)&(t<=7), 108-(t-3)*1.5, None)
    cont = np.where(t>=7, 108+(t-7)*7, None)
    fig, ax = dark_fig(14,8)
    ax.plot(t[:30], 90+t[:30]*8, color=WHITE, linewidth=2)
    mask = (t>=3)&(t<=7)
    price_mid = np.where(mask, 111-(t-3)*1.5+1.5*np.sin((t-3)*4), np.nan)
    ax.plot(t, price_mid, color=WHITE, linewidth=1.5)
    ax.plot(t[mask], (114-(t-3)*1.5)[mask], color=ORANGE, linewidth=1.5, linestyle='--', label='Flag channel')
    ax.plot(t[mask], (108-(t-3)*1.5)[mask], color=ORANGE, linewidth=1.5, linestyle='--')
    cont_mask = t>=7
    ax.plot(t[cont_mask], (108+(t-7)*7)[cont_mask], color=WHITE, linewidth=2)
    ax.axvline(7, color=BULL, linewidth=2, linestyle='--', label='Breakout')
    ax.text(1.5, 104, 'Pole\n(sharp move)', color=YELLOW, ha='center', fontsize=11)
    ax.text(5, 118, 'Flag\n(consolidation)', color=ORANGE, ha='center', fontsize=11)
    ax.text(10, 130, 'Continuation', color=BULL, ha='center', fontsize=11, fontweight='bold')
    ax.set_title('Bull Flag — Continuation Pattern: Pole + Flag + Breakout', color=WHITE, fontsize=13)
    ax.legend(facecolor='#2a2a2a', labelcolor=WHITE, fontsize=10)
    ax.set_ylabel('Price', color=WHITE)
    return save_fig(fig, n)

def slide_067(n):
    """Double Top / Bottom"""
    t = np.linspace(0,12,300)
    nk = 100.0
    dt = nk + 15*(np.exp(-((t-2)**2)/0.5) + np.exp(-((t-8)**2)/0.5)) - 5*np.exp(-((t-5)**2)/0.5)
    dt = np.where(t>10, nk-(t-10)*5, dt)
    db = nk - 15*(np.exp(-((t-2)**2)/0.5) + np.exp(-((t-8)**2)/0.5)) + 5*np.exp(-((t-5)**2)/0.5)
    db = np.where(t>10, nk+(t-10)*5, db)
    fig, (ax1,ax2) = dark_fig(16,7,1,2)
    for ax, price, c, title, sig, spos in [
        (ax1, dt, BEAR, 'Double Top — Bearish Reversal (M shape)', 'SELL', 1.05),
        (ax2, db, BULL, 'Double Bottom — Bullish Reversal (W shape)', 'BUY',  0.95)]:
        ax.plot(t, price, color=WHITE, linewidth=2.5)
        ax.axhline(nk, color=YELLOW, linewidth=2, linestyle='--', label='Neckline')
        ax.text(10.5, nk*spos, f'{sig}\n(signal)', color=c, fontsize=11, fontweight='bold')
        ax.set_title(title, fontsize=11, fontweight='bold')
        ax.legend(facecolor='#2a2a2a', labelcolor=WHITE, fontsize=9)
    fig.suptitle('Double Top & Double Bottom Reversal Patterns', color=WHITE, fontsize=14, fontweight='bold')
    plt.tight_layout()
    return save_fig(fig, n)

def slide_068(n):
    """Wedges"""
    t = np.linspace(0,10,200)
    fig, (ax1,ax2) = dark_fig(16,7,1,2)
    for ax, upper, lower, title, signal in [
        (ax1, 100+t*3, 100+t*1.5, 'Rising Wedge (BEARISH)\nPrice rising but momentum weakening', 'SELL breakdown'),
        (ax2, 130-t*3, 130-t*1.5, 'Falling Wedge (BULLISH)\nPrice falling but selling exhausting', 'BUY breakout')]:
        ax.plot(t, upper, color=BEAR, linewidth=2, linestyle='--', label='Resistance')
        ax.plot(t, lower, color=BULL, linewidth=2, linestyle='--', label='Support')
        noise = (upper+lower)/2 + (upper-lower)*0.3*np.sin(t*3)
        ax.plot(t, noise, color=WHITE, linewidth=1.5)
        ax.fill_between(t, upper, lower, alpha=0.07, color=ORANGE)
        col = BEAR if 'BEARISH' in title else BULL
        ax.text(9.0, (upper[-1]+lower[-1])/2,
                signal, color=col, fontsize=11, fontweight='bold', ha='center',
                bbox=dict(boxstyle='round', fc='#1e1e1e', ec=col, alpha=0.8))
        ax.set_title(title, fontsize=10, fontweight='bold')
        ax.legend(facecolor='#2a2a2a', labelcolor=WHITE, fontsize=9)
    fig.suptitle('Wedge Patterns — Counterintuitive Signals', color=WHITE, fontsize=14, fontweight='bold')
    plt.tight_layout()
    return save_fig(fig, n)

def slide_070_071(n):
    """Elliott Wave"""
    points = [(0,100),(2,115),(3,107),(6,135),(7,125),(9,142),(10,130),(11,136),(13,118)]
    labels = ['0','1','2','3','4','5','A','B','C']
    xs = [p[0] for p in points]; ys = [p[1] for p in points]
    fig, ax = dark_fig(14,8)
    ax.plot(xs[:6], ys[:6], color=BULL, linewidth=2.5, label='Impulse (1–5)')
    ax.plot(xs[5:], ys[5:], color=BEAR, linewidth=2.5, label='Correction (A–B–C)')
    for label, (x,y) in zip(labels, points):
        off = 4 if label in ['1','3','5','B'] else -6
        c = BULL if label.isdigit() else BEAR
        ax.annotate(label, xy=(x,y), xytext=(x,y+off), color=c,
                    fontsize=14, fontweight='bold', ha='center',
                    bbox=dict(boxstyle='circle,pad=0.3', fc=BG, ec=c, lw=1.5),
                    arrowprops=dict(arrowstyle='-', color=c, lw=1.0))
    ax.set_title('Elliott Wave Theory — 5-Wave Impulse + 3-Wave Correction', color=WHITE, fontsize=13)
    ax.legend(facecolor='#2a2a2a', labelcolor=WHITE, fontsize=11)
    ax.set_ylabel('Price', color=WHITE)
    ax.set_xlim(-0.5,14)
    return save_fig(fig, n)

def slide_072_073(n):
    """Pattern + indicator confirmation / support-resistance"""
    df = get_stock_data('AAPL','2024-01-01','2024-12-31', fallback_n=200)
    df['RSI']  = calc_rsi(df['Close'])
    df['MACD'],df['Signal'],df['Hist'] = calc_macd(df['Close'])
    x = np.arange(len(df))
    fig = plt.figure(figsize=(16,12)); fig.set_facecolor(BG)
    gs = gridspec.GridSpec(3,1,height_ratios=[4,1.5,1.5],hspace=0.05)
    ax1=fig.add_subplot(gs[0]); ax2=fig.add_subplot(gs[1]); ax3=fig.add_subplot(gs[2])
    for ax in [ax1,ax2,ax3]:
        ax.set_facecolor(BG2); ax.tick_params(colors=WHITE,labelsize=8); ax.grid(True,alpha=0.12,color='#333')
    ax1.plot(x, df['Close'], color=WHITE, linewidth=1.0)
    # Support / resistance lines
    q25 = float(df['Close'].quantile(0.25))
    q75 = float(df['Close'].quantile(0.75))
    ax1.axhline(q25, color=BULL, linewidth=2, linestyle='-', alpha=0.7, label=f'Support ${q25:.0f}')
    ax1.axhline(q75, color=BEAR, linewidth=2, linestyle='-', alpha=0.7, label=f'Resistance ${q75:.0f}')
    ax1.set_title('Support & Resistance + Pattern/Indicator Confirmation', color=WHITE, fontsize=12)
    ax1.legend(facecolor='#2a2a2a',labelcolor=WHITE,fontsize=9)
    ax2.plot(x,df['RSI'],color=PURPLE,linewidth=1.5)
    ax2.axhline(70,color=BEAR,linewidth=0.9,linestyle='--'); ax2.axhline(30,color=BULL,linewidth=0.9,linestyle='--')
    ax2.fill_between(x,df['RSI'],70,where=(df['RSI']>=70),alpha=0.2,color=BEAR)
    ax2.fill_between(x,df['RSI'],30,where=(df['RSI']<=30),alpha=0.2,color=BULL)
    ax2.set_ylim(0,100); ax2.set_ylabel('RSI',color=WHITE,fontsize=8)
    hc=[BULL if v>=0 else BEAR for v in df['Hist']]
    ax3.bar(x,df['Hist'],color=hc,alpha=0.7,width=0.7)
    ax3.plot(x,df['MACD'],color=BLUE,linewidth=1.3); ax3.plot(x,df['Signal'],color=ORANGE,linewidth=1.3)
    ax3.axhline(0,color=GRAY,linewidth=0.6); ax3.set_ylabel('MACD',color=WHITE,fontsize=8)
    plt.setp(ax1.get_xticklabels(),visible=False); plt.setp(ax2.get_xticklabels(),visible=False)
    step = max(1,len(df)//6)
    ticks = list(range(0,len(df),step))
    ax3.set_xticks(ticks)
    ax3.set_xticklabels([df.index[i].strftime('%b %Y') for i in ticks], rotation=30, ha='right', color=WHITE, fontsize=8)
    plt.tight_layout()
    return save_fig(fig, n)

def slide_075_077(n):
    """Full dashboard (same as 041 but labelled differently)"""
    return slide_041_058(n)

def slide_078(n):
    """Backtesting visualization: equity curve + drawdown + return dist"""
    df = get_stock_data('AAPL','2020-01-01','2024-12-31', fallback_n=1250)
    df['SMA20'] = df['Close'].rolling(20).mean()
    df['SMA50'] = df['Close'].rolling(50).mean()
    df['pos']   = np.where(df['SMA20'] > df['SMA50'], 1, 0)
    df['pos']   = df['pos'].shift(1).fillna(0)
    df['ret']   = df['Close'].pct_change()
    df['strat'] = df['ret'] * df['pos']
    df['cum_s'] = (1+df['strat']).cumprod()
    df['cum_bh']= (1+df['ret']).cumprod()
    rolling_max = df['cum_s'].cummax()
    df['dd']    = (df['cum_s']-rolling_max)/rolling_max
    x = np.arange(len(df))
    fig, axes = dark_fig(16,14,3,1)
    ax1, ax2, ax3 = axes
    ax1.plot(x, df['cum_s'],  color=BULL, linewidth=2,   label='SMA Crossover Strategy')
    ax1.plot(x, df['cum_bh'], color=BLUE, linewidth=2, linestyle='--', label='Buy & Hold AAPL')
    ax1.axhline(1, color=GRAY, linewidth=0.8, linestyle='--')
    ax1.set_title('Equity Curve: SMA 20/50 Crossover vs. Buy & Hold (2020–2024)', color=WHITE, fontsize=12)
    ax1.set_ylabel('Portfolio Value', color=WHITE)
    ax1.legend(facecolor='#2a2a2a',labelcolor=WHITE,fontsize=10)
    ax2.fill_between(x, df['dd'], 0, color=BEAR, alpha=0.5)
    ax2.plot(x, df['dd'], color=BEAR, linewidth=0.8)
    ax2.set_title('Drawdown Chart — How Far Below Peak', color=WHITE, fontsize=12)
    ax2.set_ylabel('Drawdown (%)', color=WHITE)
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y*100:.0f}%'))
    trade_rets = df[df['strat']!=0]['strat'].dropna()*100
    ax3.hist(trade_rets, bins=40, color=BLUE, edgecolor=BG, alpha=0.8)
    ax3.axvline(0, color=WHITE, linewidth=1.5, linestyle='--')
    ax3.axvline(float(trade_rets.mean()), color=BULL, linewidth=2,
                label=f'Mean: {trade_rets.mean():.3f}%')
    ax3.set_title('Per-Trade Return Distribution', color=WHITE, fontsize=12)
    ax3.set_xlabel('Daily Return (%)', color=WHITE)
    ax3.legend(facecolor='#2a2a2a',labelcolor=WHITE,fontsize=10)
    step = max(1,len(df)//7)
    ticks = list(range(0,len(df),step))
    for ax in [ax1,ax2]:
        ax.set_xticks(ticks)
        ax.set_xticklabels([df.index[i].strftime('%Y') for i in ticks], color=WHITE, fontsize=8)
    plt.tight_layout()
    return save_fig(fig, n)


# ──────────────────────────────────────────────────────────────
# DISPATCH TABLE — maps slide number to generator function
# ──────────────────────────────────────────────────────────────

def get_python_chart(slide_num):
    m = {
        4:  lambda: slide_004(4),
        5:  lambda: slide_004(5),    # reuse OHLCV visual
        6:  lambda: slide_006_007_008(6),
        7:  lambda: slide_006_007_008(7),
        8:  lambda: slide_006_007_008(8),
        9:  lambda: slide_009_010_011(9),
        10: lambda: slide_009_010_011(10),
        11: lambda: slide_009_010_011(11),
        12: lambda: slide_012(12),
        13: lambda: slide_013(13),
        14: lambda: slide_014(14),
        15: lambda: slide_015(15),
        16: lambda: slide_016(16),
        17: lambda: slide_017(17),
        18: lambda: slide_018(18),
        22: lambda: slide_022_023(22),
        23: lambda: slide_022_023(23),
        24: lambda: slide_024_025(24),
        25: lambda: slide_024_025(25),
        26: lambda: slide_026(26),
        27: lambda: slide_027(27),
        28: lambda: slide_028(28),
        29: lambda: slide_029(29),
        30: lambda: slide_029(30),
        32: lambda: slide_032_034(32),
        33: lambda: slide_033(33),
        34: lambda: slide_032_034(34),
        35: lambda: slide_035_036(35, is_fan=True),
        36: lambda: slide_035_036(36, is_fan=False),
        37: lambda: slide_037_038(37),
        38: lambda: slide_037_038(38),
        39: lambda: slide_039(39),
        41: lambda: slide_041_058(41),
        42: lambda: slide_042_044(42),
        43: lambda: slide_042_044(43),
        44: lambda: slide_042_044(44),
        45: lambda: slide_045_047(45),
        46: lambda: slide_045_047(46),
        47: lambda: slide_045_047(47),
        48: lambda: slide_048_050(48),
        49: lambda: slide_048_050(49),
        50: lambda: slide_048_050(50),
        51: lambda: slide_051_052(51),
        52: lambda: slide_051_052(52),
        53: lambda: slide_053_054(53),
        54: lambda: slide_053_054(54),
        55: lambda: slide_055(55),
        56: lambda: slide_056(56),
        57: lambda: slide_057(57),
        58: lambda: slide_041_058(58),
        59: lambda: slide_059(59),
        62: lambda: slide_062_070(62),
        63: lambda: slide_063(63),
        64: lambda: slide_064(64),
        65: lambda: slide_065(65),
        66: lambda: slide_066(66),
        67: lambda: slide_067(67),
        68: lambda: slide_068(68),
        70: lambda: slide_070_071(70),
        71: lambda: slide_070_071(71),
        72: lambda: slide_072_073(72),
        73: lambda: slide_072_073(73),
        75: lambda: slide_075_077(75),
        76: lambda: slide_075_077(76),
        77: lambda: slide_075_077(77),
        78: lambda: slide_078(78),
    }
    return m.get(slide_num, lambda: slide_041_058(slide_num))


# ──────────────────────────────────────────────────────────────
# MAIN ENTRY POINT
# ──────────────────────────────────────────────────────────────

if __name__ == '__main__':
    api_key = os.getenv('OPENAI_API_KEY') or ''

    if len(sys.argv) > 1:
        slides_to_run = [int(a) for a in sys.argv[1:]]
    else:
        slides_to_run = list(range(1, 81))

    print('='*70)
    print('Trading Slides Generator — Hybrid Python + OpenAI Approach')
    print(f'Slides to generate: {slides_to_run}')
    print('='*70)

    for sn in slides_to_run:
        out_path = f'{SLIDE_DIR}/slide_{sn:03d}_final.png'
        if os.path.exists(out_path):
            print(f'  ⏭  Slide {sn:02d} already exists, skipping')
            continue

        print(f'\n▶  Slide {sn:02d}...')
        if sn in DALLE_SLIDES:
            if not api_key:
                print('  ⚠️  OPENAI_API_KEY not set — skipping DALL-E slide')
                continue
            generate_dalle_slide(sn, api_key)
        else:
            fn = get_python_chart(sn)
            fn()

    print('\n' + '='*70)
    print('All done! Images saved to', SLIDE_DIR)
    print('Run: python Classx/create_classx_html.py   to build HTML')
    print('Run: python Classx/create_classx_pptx.py   to build PowerPoint')
