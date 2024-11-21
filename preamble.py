# Utility script to be run at the beginning of a bpython session. Provides
# namespace imports for tkinter and quick access to documentation comments
# through the docit function

import inspect
from pathlib import Path
import tkinter as tk

from toolz.functoolz import compose_left
import yaml

# Create the docit function
docit = compose_left(inspect.getdoc, print)

def write_to_yaml(file:str|Path, data:dict) -> None:
    match file:
        case str():
            write_to_yaml(Path(file))
            
    with file.open(mode='w', encoding='utf-8') as fp:
        yaml.dump(data, fp)

