"""
Split Class5.md into 4 separate files, one for each part
"""

# Read the full file
with open('Class5.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines in Class5.md: {len(lines)}")

# Split points based on grep output (approximate line numbers for parts)
# Part 1: lines 1-1639
# Part 2: lines 1640-3441
# Part 3: lines 3442-end (will need to find)
# Part 4: last section

# Find actual PART markers
part_boundaries = []
for i, line in enumerate(lines, 1):
    if '# PART' in line and '═══' in ''.join(lines[max(0,i-2):min(len(lines),i+2)]):
        part_boundaries.append(i)
        print(f"Found part marker at line {i}: {line.strip()[:50]}")

# Manual split based on structure
toc_end = 109  # Table of contents ends around line 109
part1_start = 110
part2_start = 1640
part3_start = 3442
part4_start = 3600  # Will adjust

# Extract sections
toc = ''.join(lines[:toc_end])
part1 = ''.join(lines[part1_start-1:part2_start-1])
part2 = ''.join(lines[part2_start-1:part3_start-1])
part3 = ''.join(lines[part3_start-1:part4_start-1])
part4 = ''.join(lines[part4_start-1:])

# Create Part files
parts_data = [
    ('Class5_Part1.md', 'Fundamentals', part1),
    ('Class5_Part2.md', 'Temporal Patterns & Decomposition', part2),
    ('Class5_Part3.md', 'Advanced Techniques', part3),
    ('Class5_Part4.md', 'Implementation & Applications', part4),
]

for filename, title, content in parts_data:
    with open(filename, 'w', encoding='utf-8') as f:
        # Add navigation
        f.write(f"# Class 5 – {title}\n\n")
        f.write(f"[← Main](Class5.md) | [Part 1](Class5_Part1.md) | [Part 2](Class5_Part2.md) | [Part 3](Class5_Part3.md) | [Part 4](Class5_Part4.md)\n\n")
        f.write("---\n\n")
        f.write(content)
    
    line_count = content.count('\n')
    print(f"\n✓ Created {filename}")
    print(f"  Title: {title}")
    print(f"  Lines: {line_count}")
    print(f"  Size: {len(content):,} bytes")

print("\n" + "=" * 60)
print("✅ Successfully split Class5.md into 4 parts!")
print("\nOriginal Class5.md remains intact.")
