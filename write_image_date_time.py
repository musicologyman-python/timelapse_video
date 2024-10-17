#!/usr/bin/env python3

from collections.abc import Iterable
from datetime import datetime
from functools import partial
from operator import attrgetter, methodcaller
from pathlib import Path
from sys import stdout
import tkinter.filedialog as fd
from typing import Callable

from icecream import ic
from loguru import logger
from PIL import Image, ImageColor, ImageDraw, ImageFont
from toolz.functoolz import compose_left, curry

VALID_IMAGE_SUFFIXES = ['.jpg', '.jpeg', '.png']
FONT_PATH = 'System/Library/Fonts/Monaco.ttf'
TIMESTAMP_FONT_SIZE = 84
POSIX_TIMESTAMP_FONT_SIZE = 28
SEQ_NUM_FONT_SIZE = 12
TIMESTAMP_FONT = ImageFont.truetype(font=FONT_PATH, size=TIMESTAMP_FONT_SIZE)
POSIX_TIMESTAMP_FONT = \
    ImageFont.truetype(font=FONT_PATH, size=POSIX_TIMESTAMP_FONT_SIZE)
POSIX_TIMESTAMP_PADDING = POSIX_TIMESTAMP_FONT_SIZE
SEQ_NUM_FONT = ImageFont.truetype(font=FONT_PATH, size=SEQ_NUM_FONT_SIZE)
IMAGE_WIDTH = 1024
TIMESTAMP_OFFSET_FROM_TOP = 20
SEQ_NUM_OFFSET_FROM_BOTTOM = 10
TEXT_COLOR = ImageColor.getcolor('white', mode='RGBA')
VIDEO_DIR: Path = Path('video')

def get_image_date_string_from_file_name(image_path: Path) -> str:
    return (datetime.strptime(image_path.stem, '%Y%m%d%H%M%S')
                    .strftime('%Y-%m-%d %H:%M:%S'))

def get_text_anchor_coordinates(bounding_box: tuple[int, int, int, int]) \
        -> tuple[int, int]:
    left, _, right, _ = bounding_box
    text_width: int= right - left
    left_anchor: int = (IMAGE_WIDTH - text_width) // 2
    return (left_anchor, TIMESTAMP_OFFSET_FROM_TOP)

@logger.catch
def label_image(dest_dir: Path, p: Path) -> None:
    if (dest_file := dest_dir / f'{p.stem}.jpeg').exists():
        return
    image_date_string = get_image_date_string_from_file_name(p)
    with Image.open(p) as im:
        try:
            draw = ImageDraw.Draw(im)
            bounding_box: tuple[int, int, int, int] = \
                TIMESTAMP_FONT.getbbox(text=image_date_string)
            xy = get_text_anchor_coordinates(bounding_box)
            draw.text(xy=xy, text=image_date_string, font=TIMESTAMP_FONT)
            # draw POSIX timestamp
            _, _, _, bottom = bounding_box
            posix_timestamp_left, _ = xy
            draw.text(xy=(posix_timestamp_left, bottom + TIMESTAMP_OFFSET_FROM_TOP), 
                      text=p.stem, font=POSIX_TIMESTAMP_FONT)
            im.save(dest_file)
        except Exception as ex:
            logger.exception(str(ex))
            logger.log('DEBUG', f'Exception writing file {p!s}')

def get_image_src_dir() -> Path:
    IMAGE_DIR_TITLE = 'Choose a folder containing the images to be labeled'
    return Path(fd.askdirectory(initialdir='.', title=IMAGE_DIR_TITLE))

def ensure_video_dest_dir_exists() -> None:
    if not VIDEO_DIR.exists():
        VIDEO_DIR.mkdir(parents=True, exist_ok=True)
        
def create_video_dest_dir(image_dir: Path) -> Path:
    video_dir_name = f'video_{image_dir.name}'
    video_dir = Path(video_dir_name)
    video_dir.mkdir(parents=True, exist_ok=True)
    return video_dir
        
def main():
    logger.add('file_{time:YYYY-MM-DD HH.mm.ss}.log')
    # ensure_video_dest_dir_exists()
    image_dir: Path = get_image_src_dir()
    video_dir: Path = create_video_dest_dir(image_dir)

    image_files: Iterable[Path] = (p for p in image_dir.iterdir() 
                                   if p.is_file() 
                                   and not p.is_symlink()
                                   and p.suffix.lower() in VALID_IMAGE_SUFFIXES)

    for i, p in enumerate(image_files, start=1):
        if i % 10 == 0:
            print(f'\rLabeling image {i}', end='')
            stdout.flush()
        label_image(video_dir, p)

    print()
    print('Done')

if __name__ == '__main__':
    main()
