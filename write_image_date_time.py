#!/usr/bin/env python3

from collections.abc import Iterable
from datetime import datetime
from functools import partial
from operator import attrgetter, methodcaller
from pathlib import Path
from sys import stdout
from typing import Callable

from icecream import ic
from PIL import Image, ImageColor, ImageDraw, ImageFont
from toolz.functoolz import compose_left, pipe

FONT_PATH = 'System/Library/Fonts/Monaco.ttf'
FONT_SIZE = 84
FONT = ImageFont.truetype(font=FONT_PATH, size=FONT_SIZE)
IMAGE_WIDTH = 1024
TEXT_OFFSET_FROM_TOP = 20
TEXT_COLOR = ImageColor.getcolor('white', mode='RGBA')
VIDEO_DIR = Path('video')

get_date_from_file_name: Callable[[Path], datetime] = (
    compose_left(
        attrgetter('stem'),
        int,
        datetime.fromtimestamp))

get_image_date_string_from_file_name: Callable[[Path], str] = (
    compose_left(
        get_date_from_file_name,
        methodcaller('strftime', '%Y-%m-%d %H:%M:%S')))

def get_text_anchor_coordinates(font: ImageFont, text: str)  -> (int, int):
    text_width: int = font.getlength(text)
    left_anchor: int = (IMAGE_WIDTH - text_width) // 2
    return (left_anchor, TEXT_OFFSET_FROM_TOP)

def label_image(p: Path) -> None:
    image_date_string = get_image_date_string_from_file_name(p)
    with Image.open(p) as im:
        draw = ImageDraw.Draw(im)
        xy = get_text_anchor_coordinates(font=FONT, text=image_date_string)
        draw.text(xy=xy, text=image_date_string, font=FONT)
        im.save(VIDEO_DIR / f'{p.stem}.jpeg')
    
def main():
    IMAGE_DIR = Path('20241004')
    image_files: Iterable[Path] = (p for p in IMAGE_DIR.iterdir() 
                                   if p.is_file() 
                                   and not p.is_symlink())
    for i, p in enumerate(image_files, start=1):
        if i % 10 == 0:
            print(f'\rLabeling image {i}', end='')
            stdout.flush()
        label_image(p)

    print('Done')

if __name__ == '__main__':
    main()

    

    

