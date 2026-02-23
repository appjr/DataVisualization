# Class 6 Slide Generator

## Overview

Generate professional, playful academic cartoon-style slides for Class 6 using the gpt-image-1 model.

## Design Specifications

**Theme:** Playful academic cartoon + clean university style  
**Palette:** Soft blues, oranges, greens on white background  
**Typography:** Bold headers + rounded friendly font  
**Visual Style:** Illustrated icons, simple diagrams, light shadows, subtle texture  
**Model:** gpt-image-1 (latest OpenAI image generation model)  
**Size:** 1536x1024 (16:9 landscape)  
**Quality:** High

## Usage

### Generate Any Slide

```bash
# Set your OpenAI API key
export OPENAI_API_KEY="your-key-here"

# Generate a specific slide
python Class6/generate_any_slide.py <slide_number>
```

### Examples

```bash
# Generate slide 5
python Class6/generate_any_slide.py 5

# Generate slide 10
python Class6/generate_any_slide.py 10

# Generate slide 25
python Class6/generate_any_slide.py 25
```

### Interactive Mode

```bash
# Run without arguments to be prompted
python Class6/generate_any_slide.py
# Then enter the slide number when prompted
```

## Output Files

For each generated slide, you'll get:

1. **Slide image:** `Class6/slide_images/slide_XXX_final.png`
2. **Reference file:** `Class6/slide_XXX_image_url.txt` (contains URL and prompt used)

## How It Works

1. Script extracts slide content from the appropriate markdown file:
   - Slides 1-20: `Class6_Part1.md`
   - Slides 21-40: `Class6_Part2.md`
   - Slides 41-60: `Class6_Part3.md`
   - Slides 61-80: `Class6_Part4.md`

2. Removes emojis from content (sends clean text to API)

3. Generates professional slide image using gpt-image-1 with:
   - Playful academic cartoon illustrations
   - Soft blues, oranges, greens color scheme
   - Bold, friendly typography
   - Clean, organized layout

4. Saves the image to `slide_images/` folder

## Already Generated

✅ Slide 3: "Why Geographic Visualization Matters"
✅ Slide 4: "Types of Geographic Data"

## Generate All Slides (Batch)

To generate multiple slides at once, you can use a loop:

```bash
export OPENAI_API_KEY="your-key-here"

# Generate slides 1-10
for i in {1..10}; do
    python Class6/generate_any_slide.py $i
    echo "Completed slide $i"
    sleep 5  # Wait 5 seconds between calls
done
```

## Notes

- Each API call generates one slide image
- HD quality images (~2-4 MB each)
- Generation takes ~20-30 seconds per slide
- Cost: ~$0.08 per image with gpt-image-1
- Content is extracted automatically from markdown files
- Style remains consistent across all slides

## Troubleshooting

**"Could not extract content":** Check that the markdown files exist and contain the slide content

**"API key not set":** Make sure to export OPENAI_API_KEY before running

**"Model not found":** Verify gpt-image-1 is available in your OpenAI account
