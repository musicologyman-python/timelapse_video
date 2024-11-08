#!/usr/bin/env python3

import argparse
from collections.abc import Iterable
from dataclasses import asdict, dataclass, field
import datetime as dt
from functools import partial
from io import StringIO
from operator import attrgetter
from pathlib import Path
import sqlite3
import sys
import tkinter.filedialog as fd

from icecream import ic
from loguru import logger

TIME_DATABASE_FILENAME = 'time_map.db'
PARSEABLE_TIME_FORMAT = '%Y%m%d%H%M%S'
IMAGE_FILE_SUFFIXES = ['.jpg', '.jpeg', '.png']

@dataclass
class ImageTimeRecord():
    file: Path
    filename: str = field(init=False, repr=False)
    year: int = field(init=False, repr=False)
    month: int = field(init=False, repr=False)
    day: int = field(init=False, repr=False)
    hour: int = field(init=False, repr=False)
    minute: int = field(init=False, repr=False)
    second: int = field(init=False, repr=False)
    posix_timestamp: int = field(init=False, repr=False)
    
    def __post_init__(self):
        self.filename = self.file.name
        image_datetime = \
                dt.datetime.strptime(self.file.stem, PARSEABLE_TIME_FORMAT)
        self.year = image_datetime.year
        self.month = image_datetime.month
        self.day = image_datetime.day
        self.hour = image_datetime.hour
        self.minute = image_datetime.minute
        self.second = image_datetime.second
        self.posix_timestamp = image_datetime.timestamp()

    def __str__(self):
        with StringIO() as sp:
            prints = partial(print, file=sp)
            prints(f'ImageTimeRecord:')
            prints(f'    filename: "{self.filename}"')
            prints(f'    year: {self.year}, month: {self.month}, ', end='')
            prints(f'day: {self.day}')
            prints(f'    hour: {self.hour}, minute: {self.minute}, ', end='')
            prints(f'second: {self.second}')
            prints(f'    posix_timestmap: {self.posix_timestamp}', end='')
            prints()
            return sp.getvalue()


def get_image_files(parent: Path) -> list:
    return sorted((p for p in parent.iterdir()
                   if p.suffix in IMAGE_FILE_SUFFIXES),
                  key=attrgetter('name'))

def make_time_db(db_filename: Path) -> None:
    with sqlite3.connect(db_filename) as cn:
        cn.executescript('''DROP TABLE IF EXISTS timemap;
                            CREATE TABLE timemap (
                                filename TEXT, 
                                year NUMBER,
                                month NUMBER,
                                day NUMBER,
                                hour NUMBER, 
                                minute NUMBER, 
                                second NUMBER,
                                posix_timestamp NUMBER);''')
        cn.executescript('''CREATE VIEW IF NOT EXISTS vw_minutes 
                            AS
                            SELECT DISTINCT day, hour, minute
                            FROM timemap
                            ORDER BY day, hour, minute;''');
        cn.commit()

def populate_db(time_records: Iterable[ImageTimeRecord],
                db_filename: str=TIME_DATABASE_FILENAME) -> None:
    POPULATE_STMT = '''INSERT INTO timemap (
                            filename, year, month, day, hour, minute, second, 
                            posix_timestamp)
                       VALUES (:filename, :year, :month, :day,
                               :hour, :minute, :second, :posix_timestamp)'''
    with sqlite3.connect(db_filename) as cn:
        cur = cn.cursor()
        cur.executemany(POPULATE_STMT, 
                        (asdict(tr) for tr in time_records))
        cn.commit()

# region for standalone operation
        
def prompt_for_image_dir() -> str:
    return fd.askdirectory(initialdir=Path.cwd(), 
                           title='Select the directory containing the images '
                                 'to process')
    
        
def setup_cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('image_dir', type=Path, nargs='*')
    parser.add_argument('--recreate', '-r', type=bool, default=False, 
                        help='if True, drop and recreate the database')
    return parser.parse_args()

@logger.catch
def main():

    logger.add(sys.stdout, level='INFO')
    logger.add(sys.stderr)
    logger.add('make_time_db.log')

    args: argparse.Namespace = setup_cli()

    ic(args.image_dir)
    ic(args.recreate)
    
    image_dir: list[Path] = args.image_dir
    
    if image_dir and len(image_dir) > 0:
        image_dir = image_dir[0]
    elif ((image_dir_name:=prompt_for_image_dir()) is not None):
        image_dir = Path(image_dir_name)
    else:
        print('No image directory selected', file=sys.stdout)
        sys.stdout.flush()
        exit(1)
        
    db_file: Path = image_dir / TIME_DATABASE_FILENAME

    if args.recreate or not db_file.exists():
        make_time_db(db_file)

    image_files = get_image_files(image_dir)
    image_file_records = (
            ImageTimeRecord(image_file) for image_file in image_files)
    populate_db(image_file_records, db_file)

if __name__ == '__main__':
    main()

# endregion