#!/usr/bin/env python3

# This script contains functions to assist in determining the point in a
# video that correponds to a particular timestamp

from collections.abc import Iterable
from datetime import datetime
from pathlib import Path
from typing import Callable

from toolz.functoolz import pipe

DATESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S'
DEFAULT_FRAME_RATE = 30

type Filter[T] = Callable[[T], bool]

def identity_filter[T](v: T) -> bool:
    return True

def get_simple_suffix_filter(suffix: str):
    def wrapped(p: Path):
        return p.suffix == suffix
    return wrapped

def get_timestamp_named_files(parent: Path=Path.cwd(), 
                              filter: Filter[Path]=identity_filter) \
        -> Iterable[Path]:
    return (p for p in parent.iterdir() 
            if p.is_file() and not p.is_symlink() and filter(p))

def get_posix_timestamp_from_date_string(datestring: str) -> int:
    return pipe(datetime.strptime(datestring, DATESTAMP_FORMAT),
                int)

def find_seq_num_for_timestamp(timestamps: Iterable[int], ts: int) \
        -> int:
    return timestamps.index(ts)

def find_video_time_for_seq_num(seq_num: int, framerate: int=DEFAULT_FRAME_RATE) \
    -> float:
    return seq_num / framerate




