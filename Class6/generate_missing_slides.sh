#!/bin/bash
# Generate ONLY missing Class 6 slides (smart script - skips existing)

echo "=========================================="
echo "CLASS 6 - SMART SLIDE GENERATOR"
echo "=========================================="
echo "Checking for existing slides..."

# Check for API key
if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ Error: OPENAI_API_KEY not set"
    exit 1
fi

# Count existing slides
existing_count=$(ls Class6/slide_images/*_final.png 2>/dev/null | wc -l)
echo "Found $existing_count existing slides"
echo "Will generate $(( 80 - existing_count )) missing slides"
echo "=========================================="
echo ""

# Confirm
read -p "Continue? (y/n): " confirm
if [ "$confirm" != "y" ]; then
    echo "Cancelled."
    exit 0
fi

echo "Starting generation of missing slides..."
echo "=========================================="

completed=0
skipped=0

# Generate slides 1-80, skip if exists
for i in {1..80}; do
    slide_file="Class6/slide_images/slide_$(printf "%03d" $i)_final.png"
    
    if [ -f "$slide_file" ]; then
        echo "⏭️  Slide $i exists - skipping"
        ((skipped++))
    else
        echo ""
        echo "[$(( completed + skipped + 1 ))/80] Generating slide $i..."
        python Class6/generate_any_slide.py $i
        
        if [ $? -eq 0 ]; then
            ((completed++))
            echo "✅ Slide $i generated ($completed new, $skipped skipped)"
        else
            echo "❌ Failed slide $i"
        fi
        
        # Wait between calls
        sleep 3
    fi
    
    # Commit every 10 slides
    if [ $((i % 10)) -eq 0 ]; then
        echo ""
        echo "📦 Committing progress..."
        git add Class6/slide_images/*.png Class6/slide_*_image_url.txt 2>/dev/null
        git commit -m "Generate slides batch (up to slide $i) - $completed new slides" 2>/dev/null || echo "Nothing to commit"
        echo "✅ Checkpoint at slide $i"
    fi
done

# Final commit
echo ""
echo "📦 Final commit..."
git add Class6/slide_images/*.png Class6/slide_*_image_url.txt
git commit -m "Complete Class 6 slide generation - $completed new slides added"

echo ""
echo "=========================================="
echo "✨ GENERATION COMPLETE!"
echo "=========================================="
echo "New slides generated: $completed"
echo "Existing slides skipped: $skipped"
echo "Total slides: $(( completed + skipped ))/80"
echo "Location: Class6/slide_images/"
echo ""
