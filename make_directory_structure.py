from pathlib import Path

import yaml

with open('file_structure.yaml') as fp:
    file_structure = yaml.load(fp, Loader=yaml.Loader)

for key, values in file_structure.items():
    print(f'[{key}]')
    Path(key).mkdir(parents=True, exist_ok=True)
    parent_dir = Path(key)
    for value in values:
        file = Path(value)
        if not file.exists():
            continue
        dest = parent_dir / file
        print(f'  {file!s} -> {dest!s}')
        file.rename(dest)
