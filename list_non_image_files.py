from pathlib import Path
import re

cwd = Path.cwd()
files = list(cwd.iterdir())
non_jpeg_files = [p.relative_to(cwd) for p in files if p.is_file() and p.suffix != '.jpeg']
for p in non_jpeg_files:
    print(p.name)

# OUT: timemap.db
# OUT: navigate.py
# OUT: time_map.db
# OUT: make_time_db.py
# OUT: make_time_db.log
Path('../').resolve()
# OUT: PosixPath('/Users/richard/Repos/timelapse_video')
### 