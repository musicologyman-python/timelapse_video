# This script renames image files with a posix timestamp as the stem to
# year-month-day-hour-minute-second format

import datetime as dt
import operator
from pathlib import Path
import sys
import tkinter.filedialog as fd
import tkinter.messagebox as mb
from typing import Callable

from toolz.functoolz import compose_left, curry, pipe

get_new_file_stem = compose_left(operator.attrgetter('stem'),
                                 int,
                                 dt.datetime.fromtimestamp,
                                 operator.methodcaller('strftime',
                                                       '%Y%m%d%H%M%S'))

def get_path_with_new_name(p: Path):
    new_stem = get_new_file_stem(p)
    return Path(new_stem).with_suffix(p.suffix)

def get_files(parent: Path):
    yield from (p for p in parent.iterdir() 
                if p.suffix in ['.jpeg','.jpg','.png'])

def main():

    if (image_dir:=fd.askdirectory(title='Select an image folder',
                                   initialdir=str(Path.cwd()))) is None:
        message_window = mb.Message(message='No directory selected. Exiting', 
                                    icon=mb.ERROR)
        message_window.show()
        sys.exit(1)

    for p in get_files(Path(image_dir)):
        new_path = get_path_with_new_name(p)
        p.rename(new_path)

if __name__ == '__main__':
    main()
    
