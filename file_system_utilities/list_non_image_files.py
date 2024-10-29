from pathlib import Path
import re

IMAGE_SUFFIXES = ['.jpg', '.jpeg', '.png', '.ppm', '.bmp']

def is_image_file(p: Path):
    return p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES

cwd = Path.cwd()
non_image_files = (p.relative_to(cwd) 
                  for p in cwd.iterdir() if not is_image_file(p))

for p in non_image_files:
    print(p.name)

