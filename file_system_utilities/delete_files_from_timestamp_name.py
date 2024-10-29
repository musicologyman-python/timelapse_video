'''
Delete jpeg files named using a timestamp subject to a time constraint
'''

import operator
from pathlib import Path

files = sorted([p for p in Path.cwd().iterdir() if p.suffix == '.jpeg'], 
               key=operator.attrgetter('stem'))

for p in files:
    if int(p.stem) < 20241011000045:
        p.unlink()
