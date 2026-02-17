# OpenAI Image Generation Quick Start Guide

## 📖 Overview

This guide shows you how to use OpenAI's DALL-E API to generate images from text descriptions.

---

## 🚀 Quick Setup

### 1. Install Required Packages

```bash
pip install openai pillow requests
```

### 2. Get Your API Key

1. Go to https://platform.openai.com/api-keys
2. Create a new API key
3. Copy it (you won't see it again!)

### 3. Set Your API Key

**Option A: Environment Variable (Recommended)**
```bash
export OPENAI_API_KEY='sk-your-key-here'
```

**Option B: In Code (Not recommended for production)**
```python
api_key = 'sk-your-key-here'
```

---

## 💡 Simple Example

```python
from openai import OpenAI
import os

# Initialize client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Generate image
response = client.images.generate(
    model="dall-e-3",
    prompt="A professional data visualization slide with clean charts",
    size="1024x1024",
    quality="standard",
    n=1
)

# Get the image URL
image_url = response.data[0].url
print(f"Image URL: {image_url}")
```

---

## 📝 Complete Examples

See **`openai_image_generation_guide.py`** for:
- ✅ Basic image generation
- ✅ Save images locally
- ✅ Advanced parameters
- ✅ Batch generation
- ✅ Image variations

---

## 🎨 For Slide Images

Here's a specific example for generating course slide images:

```python
from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO
import os

def generate_slide_image(slide_title, slide_content, output_filename):
    """Generate a professional slide image"""
    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    # Create descriptive prompt
    prompt = f"""
    Create a professional presentation slide with:
    - Title: "{slide_title}"
    - Content: {slide_content}
    - Style: Clean, modern, business professional
    - Colors: Blue and white color scheme
    - Layout: Title at top, content below with bullet points
    - Background: Subtle gradient
    """
    
    # Generate
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1792x1024",  # Wide format for slides
        quality="hd",
        style="natural"
    )
    
    # Download and save
    image_url = response.data[0].url
    img_data = requests.get(image_url).content
    img = Image.open(BytesIO(img_data))
    img.save(output_filename)
    
    print(f"✓ Slide saved: {output_filename}")
    return output_filename

# Example usage
generate_slide_image(
    slide_title="Data Visualization Fundamentals",
    slide_content="Key principles of effective visualizations",
    output_filename="slide_001.png"
)
```

---

## 💰 Pricing (2024)

| Model | Size | Quality | Price per Image |
|-------|------|---------|----------------|
| DALL-E 3 | 1024x1024 | Standard | $0.040 |
| DALL-E 3 | 1024x1024 | HD | $0.080 |
| DALL-E 3 | 1792x1024 | Standard | $0.080 |
| DALL-E 2 | 1024x1024 | - | $0.020 |

**💡 Tip:** Use DALL-E 2 for testing, DALL-E 3 for final images

---

## ⚙️ Available Parameters

### Model Options
- `dall-e-3` - Latest, best quality
- `dall-e-2` - Lower cost, faster

### Size Options
**DALL-E 3:**
- `1024x1024` - Square
- `1792x1024` - Landscape
- `1024x1792` - Portrait

**DALL-E 2:**
- `256x256` - Small
- `512x512` - Medium
- `1024x1024` - Large

### Quality (DALL-E 3 only)
- `standard` - Good quality, lower cost
- `hd` - Higher quality, 2x cost

### Style (DALL-E 3 only)
- `vivid` - More dramatic, artistic
- `natural` - More realistic, less embellished

---

## 📋 Best Practices

### 1. Writing Good Prompts

**❌ Bad Prompt:**
```
"chart"
```

**✅ Good Prompt:**
```
"A professional business chart showing quarterly sales trends with 
clean lines, blue color scheme, minimal design, on white background"
```

### 2. Be Specific

Include:
- **Style**: "minimalist", "professional", "modern"
- **Colors**: "blue and white", "warm tones"
- **Layout**: "centered", "top-aligned"
- **Details**: specific elements you want

### 3. Common Prompt Templates

**For Slides:**
```
"Professional presentation slide titled '[TITLE]' with [CONTENT], 
clean modern design, blue color scheme, white background, 
business professional style"
```

**For Diagrams:**
```
"Clean technical diagram showing [CONCEPT], with arrows indicating 
flow, labeled components, minimalist style, flat design"
```

**For Charts:**
```
"Business chart displaying [DATA TYPE], clean lines, professional 
appearance, [COLOR] color scheme, white background"
```

---

## 🛠️ Troubleshooting

### Issue: "Invalid API Key"
**Solution:** Check that your API key is set correctly
```bash
echo $OPENAI_API_KEY  # Should display your key
```

### Issue: "Rate limit exceeded"
**Solution:** Add delays between requests
```python
import time
time.sleep(1)  # Wait 1 second between requests
```

### Issue: "Content policy violation"
**Solution:** Revise your prompt to be more appropriate

### Issue: "Image URL expired"
**Solution:** Download images immediately (they expire after 1 hour)

---

## 📚 Resources

- **Official Docs:** https://platform.openai.com/docs/guides/images
- **API Reference:** https://platform.openai.com/docs/api-reference/images
- **Pricing:** https://openai.com/pricing
- **Rate Limits:** https://platform.openai.com/docs/guides/rate-limits

---

## 🎯 Next Steps

1. ✅ Set up your API key
2. ✅ Run `openai_image_generation_guide.py` examples
3. ✅ Experiment with different prompts
4. ✅ Generate images for your slides!

---

## 💬 Need Help?

- Check the complete guide: `openai_image_generation_guide.py`
- OpenAI Community: https://community.openai.com/
- Official Documentation: https://platform.openai.com/docs

---

**Created:** February 16, 2026  
**Course:** MIS 6380 - Data Visualization
