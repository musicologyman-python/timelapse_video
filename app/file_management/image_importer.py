#!/usr/bin/env python3

from collections.abc import Iterable
from datetime import datetime
from pathlib import Path
import re
from sys import stdout
import tkinter.filedialog as fd

from loguru import logger
from PIL import Image, ImageColor, ImageDraw, ImageFont

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
INTEGER_RE = re.compile(r'^\s*\d+\s*$')
PARSEABLE_DATETIME_FORMAT = '%Y%m%d%H%M%S'
READABLE_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

def is_integer(s: str) -> bool:
    return INTEGER_RE.search(s) is not None 

def get_image_date_string_from_file_name(image_path: Path) -> str:
    MAX_POSIX_TIMESTAMP: int = 253_402_318_800
    stem: str = image_path.stem
    if not is_integer(stem):
        raise ValueError(
            f'The file stem {stem} cannot be converted to an integer')
    stem_int: int = int(stem)
    image_date: datetime
    if stem_int > MAX_POSIX_TIMESTAMP:
        image_date = datetime.strptime(stem, PARSEABLE_DATETIME_FORMAT)
    else:
        image_date = datetime.fromtimestamp(stem_int)
    return image_date.strftime(READABLE_DATETIME_FORMAT)

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

def get_dir(title: str) -> Path:
    return Path(fd.askdirectory(initialdir='.', title=title))

def get_image_src_dir() -> Path:
    IMAGE_DIR_TITLE = 'Choose a folder containing the images to be labeled'
    return get_dir(IMAGE_DIR_TITLE)

def get_video_img_dest_dir_parent() -> Path:
    VIDEO_IMG_DEST_DIR = 'Choose a the parent folder for the video images.'
    return get_dir(VIDEO_IMG_DEST_DIR)

def ensure_video_dest_dir_exists() -> None:
    if not VIDEO_DIR.exists():
        VIDEO_DIR.mkdir(parents=True, exist_ok=True)
        
def create_video_dest_dir(video_dest_parent_dir: Path, src_img_dir: Path) \
        -> Path:
    video_dir_name = f'video_{src_img_dir.name}'
    video_dir = video_dest_parent_dir / video_dir_name
    video_dir.mkdir(parents=True, exist_ok=True)
    return video_dir
        
def get_image_files(image_dir: Path) -> Iterable[Path]:
    return (p for p in image_dir.iterdir() 
            if p.is_file() 
            and not p.is_symlink()
            and p.suffix.lower() in VALID_IMAGE_SUFFIXES)

def count_image_files(image_dir: Path) -> int:
    return sum(1 for _ in get_image_files(image_dir))

def label_image_files(dest_dir: Path, image_files: Iterable[Path]) -> None:
    for i, image_path in enumerate(image_files, start=1):
        if i % 10 == 0:
            print(f'\rLabeling image {i}', end='')
            stdout.flush()
        label_image(dest_dir, image_path)

def main():
    
    logger.add('file_{time:YYYY-MM-DD HH.mm.ss}.log')
    # ensure_video_dest_dir_exists()
    
    image_dir: Path = get_image_src_dir() 
    video_img_dest_dir_parent: Path = get_video_img_dest_dir_parent()
    video_dir: Path = create_video_dest_dir(video_img_dest_dir_parent, 
                                            image_dir)

    image_files: Iterable[Path] = get_image_files(image_dir)
    label_image_files(dest_dir=video_dir, image_files=image_files)

    print()
    print('Done')

if __name__ == '__main__':
    main()
