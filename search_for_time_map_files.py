# coding: utf-8
from pathlib import Path
files = [p for p in Path.cwd().iterdir() if p.is_dir() and p.name.startswith('video')]
files.sort()
for p in files:
    time_map_file = p / f'time_map.db'
    if time_map_file.exists():
        print(f'{time_map_file.relative_to(Path.cwd())} exists')
    else:
        print(f'{time_map_file.relative_to(Path.cwd())} does not exist.')
        
