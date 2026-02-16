import os
import base64
from openai import OpenAI

client = OpenAI()

input_dir = "Class5/locally_created_image"
output_dir = "Class5/local_to_gpt"
os.makedirs(output_dir, exist_ok=True)

print("=== Image-to-Image Transformation (Vintage Cartoon) ===")
print(f"Input directory: {input_dir}")
print(f"Output directory: {output_dir}")

image_files = sorted([f for f in os.listdir(input_dir) if f.endswith('.png')])
print(f"Total images found: {len(image_files)}\n")

# Clear existing output images
removed = 0
for file in os.listdir(output_dir):
    if file.endswith(".png"):
        os.remove(os.path.join(output_dir, file))
        removed += 1
print(f"Cleared {removed} previous images in output folder.\n")

for idx, image_file in enumerate(image_files, 1):
    input_path = os.path.join(input_dir, image_file)
    print(f"[{idx}/{len(image_files)}] Transforming {image_file}...")

    with open(input_path, "rb") as img_file:
        result = client.images.edit(
            model="gpt-image-1",
            image=img_file,
            prompt="Transform this slide into a vintage cartoon style, keeping layout and text legible.",
            size="1024x1536",
            quality="medium",
            n=1
        )

    image_base64 = result.data[0].b64_json
    output_path = os.path.join(output_dir, image_file)
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(image_base64))

    file_size_kb = os.path.getsize(output_path) / 1024
    print(f"    ✓ Saved {output_path} ({file_size_kb:.1f} KB)\n")

print("✅ All images transformed successfully!")
