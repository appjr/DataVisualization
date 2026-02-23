#!/bin/bash
# Generate all remaining Class 6 slides with playful academic cartoon style
# Uses gpt-image-1 model

echo "=========================================="
echo "CLASS 6 - BATCH SLIDE GENERATOR"
echo "=========================================="
echo "This will generate images for all remaining slides"
echo "Total slides to generate: 78 (slides 1-2, 5-80)"
echo "Estimated time: ~40 minutes"
echo "Estimated cost: ~\$6.24 (78 slides × \$0.08)"
echo "=========================================="
echo ""

# Check for API key
if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ Error: OPENAI_API_KEY not set"
    echo "Please run: export OPENAI_API_KEY='your-key-here'"
    exit 1
fi

# Confirm before proceeding
read -p "Continue with batch generation? (y/n): " confirm
if [ "$confirm" != "y" ]; then
    echo "Cancelled."
    exit 0
fi

echo ""
echo "Starting batch generation..."
echo "=========================================="

# Counter for progress
total=78
completed=0

# Generate slides 1-2
for i in 1 2; do
    echo ""
    echo "[$((completed+1))/$total] Generating slide $i..."
    python Class6/generate_any_slide.py $i
    
    if [ $? -eq 0 ]; then
        ((completed++))
        echo "✅ Slide $i complete ($completed/$total)"
    else
        echo "❌ Failed to generate slide $i"
    fi
    
    # Wait between calls to avoid rate limiting
    sleep 3
done

# Generate slides 5-80 (skip 3 and 4 - already done)
for i in {5..80}; do
    echo ""
    echo "[$((completed+1))/$total] Generating slide $i..."
    python Class6/generate_any_slide.py $i
    
    if [ $? -eq 0 ]; then
        ((completed++))
        echo "✅ Slide $i complete ($completed/$total)"
    else
        echo "❌ Failed to generate slide $i"
    fi
    
    # Wait between calls
    sleep 3
    
    # Commit every 10 slides
    if [ $((i % 10)) -eq 0 ]; then
        echo ""
        echo "📦 Committing slides..."
        git add Class6/slide_images/*.png Class6/slide_*_image_url.txt
        git commit -m "Generate slides batch (up to slide $i)"
        echo "✅ Committed"
    fi
done

# Final commit
echo ""
echo "📦 Final commit..."
git add Class6/slide_images/*.png Class6/slide_*_image_url.txt
git commit -m "Complete all Class 6 slide images - playful academic cartoon style"

echo ""
echo "=========================================="
echo "✨ BATCH GENERATION COMPLETE!"
echo "=========================================="
echo "Generated: $completed/$total slides"
echo "Location: Class6/slide_images/"
echo "All changes committed to git"
echo ""
