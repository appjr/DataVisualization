"""
OpenAI Image Generation API Guide
Using DALL-E for creating images from text prompts

Requirements:
    pip install openai pillow requests
    
Setup:
    1. Get an API key from https://platform.openai.com/api-keys
    2. Set environment variable: export OPENAI_API_KEY='your-key-here'
       Or use in code (not recommended for production)
"""

import os
from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO

# ============================================================================
# METHOD 1: Using OpenAI Python Library (Recommended)
# ============================================================================

def generate_image_basic(prompt, api_key=None):
    """
    Basic image generation with DALL-E 3
    
    Args:
        prompt (str): Description of the image to generate
        api_key (str): Your OpenAI API key (optional if set in environment)
    
    Returns:
        str: URL of the generated image
    """
    # Initialize client
    client = OpenAI(api_key=api_key or os.getenv('OPENAI_API_KEY'))
    
    # Generate image
    response = client.images.generate(
        model="dall-e-3",  # or "dall-e-2" for lower cost
        prompt=prompt,
        size="1024x1024",  # DALL-E 3: "1024x1024", "1792x1024", "1024x1792"
                          # DALL-E 2: "256x256", "512x512", "1024x1024"
        quality="standard",  # "standard" or "hd" (DALL-E 3 only)
        n=1,  # Number of images (1-10 for DALL-E 2, only 1 for DALL-E 3)
    )
    
    image_url = response.data[0].url
    print(f"✓ Image generated: {image_url}")
    return image_url


def generate_and_save_image(prompt, filename, api_key=None):
    """
    Generate image and save it locally
    
    Args:
        prompt (str): Description of the image to generate
        filename (str): Local filename to save (e.g., 'output.png')
        api_key (str): Your OpenAI API key
    """
    # Generate image
    image_url = generate_image_basic(prompt, api_key)
    
    # Download and save
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.save(filename)
    print(f"✓ Image saved to: {filename}")
    return img


# ============================================================================
# METHOD 2: Advanced Usage with Custom Parameters
# ============================================================================

def generate_image_advanced(
    prompt,
    model="dall-e-3",
    size="1024x1024",
    quality="standard",
    style="vivid",
    api_key=None
):
    """
    Advanced image generation with full control
    
    Args:
        prompt (str): Image description
        model (str): "dall-e-3" or "dall-e-2"
        size (str): Image dimensions
        quality (str): "standard" or "hd" (DALL-E 3 only)
        style (str): "vivid" or "natural" (DALL-E 3 only)
        api_key (str): Your OpenAI API key
    
    Returns:
        dict: Full response with URL and revised prompt
    """
    client = OpenAI(api_key=api_key or os.getenv('OPENAI_API_KEY'))
    
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
        quality=quality,
        style=style if model == "dall-e-3" else None,
        n=1
    )
    
    result = {
        'url': response.data[0].url,
        'revised_prompt': response.data[0].revised_prompt  # DALL-E 3 only
    }
    
    print(f"✓ Original prompt: {prompt}")
    print(f"✓ Revised prompt: {result['revised_prompt']}")
    print(f"✓ Image URL: {result['url']}")
    
    return result


# ============================================================================
# METHOD 3: Image Editing (Variations)
# ============================================================================

def create_image_variation(image_path, api_key=None):
    """
    Create variations of an existing image
    
    Args:
        image_path (str): Path to PNG image (must be square, <4MB)
        api_key (str): Your OpenAI API key
    
    Returns:
        str: URL of the variation
    """
    client = OpenAI(api_key=api_key or os.getenv('OPENAI_API_KEY'))
    
    with open(image_path, "rb") as image_file:
        response = client.images.create_variation(
            image=image_file,
            n=1,
            size="1024x1024"
        )
    
    return response.data[0].url


# ============================================================================
# METHOD 4: Batch Image Generation
# ============================================================================

def generate_multiple_images(prompts, output_dir="generated_images", api_key=None):
    """
    Generate multiple images from a list of prompts
    
    Args:
        prompts (list): List of text prompts
        output_dir (str): Directory to save images
        api_key (str): Your OpenAI API key
    """
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    results = []
    for i, prompt in enumerate(prompts, 1):
        print(f"\n[{i}/{len(prompts)}] Generating: {prompt[:50]}...")
        
        try:
            filename = f"{output_dir}/image_{i:03d}.png"
            img = generate_and_save_image(prompt, filename, api_key)
            results.append({
                'prompt': prompt,
                'filename': filename,
                'success': True
            })
        except Exception as e:
            print(f"✗ Error: {e}")
            results.append({
                'prompt': prompt,
                'filename': None,
                'success': False,
                'error': str(e)
            })
    
    # Summary
    successful = sum(1 for r in results if r['success'])
    print(f"\n✓ Generated {successful}/{len(prompts)} images successfully")
    
    return results


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    # Set your API key
    API_KEY = os.getenv('OPENAI_API_KEY') or 'your-api-key-here'
    
    print("=" * 70)
    print("OpenAI Image Generation Examples")
    print("=" * 70)
    
    # Example 1: Basic image generation
    print("\n### Example 1: Basic Image Generation ###")
    prompt1 = "A futuristic data visualization dashboard with holographic charts"
    try:
        url = generate_image_basic(prompt1, API_KEY)
        print(f"View image at: {url}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: Generate and save locally
    print("\n### Example 2: Generate and Save ###")
    prompt2 = "An elegant infographic showing time series data with clean lines"
    try:
        generate_and_save_image(prompt2, "my_visualization.png", API_KEY)
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 3: Advanced with custom parameters
    print("\n### Example 3: Advanced Generation ###")
    prompt3 = "A professional business chart showing sales trends, minimal style"
    try:
        result = generate_image_advanced(
            prompt=prompt3,
            model="dall-e-3",
            size="1792x1024",  # Wide format
            quality="hd",
            style="natural",
            api_key=API_KEY
        )
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 4: Batch generation
    print("\n### Example 4: Batch Generation ###")
    slide_prompts = [
        "Title slide with 'Data Visualization Course' text, modern design",
        "Diagram showing the data analysis workflow with arrows",
        "Chart comparing different visualization types side by side"
    ]
    try:
        results = generate_multiple_images(slide_prompts, "slide_images", API_KEY)
    except Exception as e:
        print(f"Error: {e}")


# ============================================================================
# TIPS & BEST PRACTICES
# ============================================================================

"""
PRICING (as of 2024):
- DALL-E 3:
  - Standard 1024x1024: $0.040 per image
  - HD 1024x1024: $0.080 per image
  - Standard 1792x1024 or 1024x1792: $0.080 per image
  
- DALL-E 2:
  - 1024x1024: $0.020 per image
  - 512x512: $0.018 per image
  - 256x256: $0.016 per image

TIPS FOR BETTER RESULTS:
1. Be specific and descriptive in prompts
2. Include style keywords: "photorealistic", "minimalist", "vintage"
3. Specify colors, mood, and composition
4. Mention art styles: "in the style of infographic design"
5. Use DALL-E 3 for better quality and prompt adherence

LIMITATIONS:
- DALL-E 3: Only 1 image per request
- DALL-E 2: Up to 10 images per request
- Images expire after 1 hour (download immediately)
- Content policy restrictions apply
- Rate limits: 50 requests/min for DALL-E 3

ERROR HANDLING:
- Invalid API key → Check environment variable
- Rate limit → Implement exponential backoff
- Content policy violation → Revise prompt
- Image size error → Use supported dimensions
"""
