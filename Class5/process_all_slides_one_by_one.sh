#!/bin/bash
# Process all slides one at a time to avoid batch processing issues

echo "Processing 94 slides one at a time..."
echo "Started: $(date)"
echo "=" | sed 's/./ /g' | tr ' ' '='

for i in {001..094}; do
    input_file="slide_images/slide_${i}.png"
    if [ -f "$input_file" ]; then
        echo "[$(date +%H:%M:%S)] Processing slide ${i}..."
        /opt/anaconda3/bin/python generateSlidesFromImages.py "$input_file" --master master.png --outdir slide_images_ai
        if [ $? -eq 0 ]; then
            echo "✓ Completed slide ${i}"
        else
            echo "✗ Failed slide ${i}"
        fi
    fi
done

echo "=" | sed 's/./ /g' | tr ' ' '='
echo "Finished: $(date)"
echo "Total AI slides created: $(ls slide_images_ai/*.png 2>/dev/null | wc -l)"
