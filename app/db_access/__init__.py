from dataclasses import dataclass
import datetime as dt
from functools import partial
import io
import sqlite3
import typing

@dataclass
class TimeMap():
    filename: str
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int
    posix_timestamp: int

    def __str__(self):
        mapped_datetime = dt.datetime.fromtimestamp(self.posix_timestamp)
        with io.StringIO() as sp:
            prints = partial(print, file=sp)
            prints(f'filename: "{self.filename}, ', end='')
            prints(f'time: {mapped_datetime.strftime("%H:%M:%S")}, ', end='')
            prints(f'date: {mapped_datetime.strftime("%Y-%m-%d")}, ', end='')
            prints(f'POSIX timestamp: {self.posix_timestamp}')
            return sp.getvalue()


def time_map_factory(cursor, row):
    return TimeMap(*row)

def execute_query(command_text: str, dbpath: str='timemap.db', 
                  **param_dict: dict) -> TimeMap:
    with sqlite3.connect(dbpath) as cn:
        cn.row_factory = time_map_factory
        cur = cn.execute(command_text, param_dict)
        return cur.fetchone()

def find_record(timestamp: int=0) -> TimeMap:
    COMMAND_TEXT = '''SELECT filename,
                                   year,
                                   month,
                                   day,
                                   hour,
                                   minute,
                                   second,
                                   posix_timestamp
                            FROM timemap 
                            WHERE posix_timestamp >= :min_time
                            ORDER BY posix_timestamp;'''
    return execute_query(COMMAND_TEXT, {'min_time': timestamp})

def get_last_record(timestamp: typing.Any) -> TimeMap:
    COMMAND_TEXT = '''SELECT filename,
                                   year,
                                   month,
                                   day,
                                   hour,
                                   minute,
                                   second,
                                   posix_timestamp
                            FROM timemap 
                            ORDER BY posix_timestamp DESC;'''
    return execute_query(COMMAND_TEXT, {'min_time': timestamp})

def get_first_record() -> TimeMap:
    return find_record()

def advance_one_minute(current_time_map: TimeMap) -> TimeMap:
    return find_record(current_time_map.posix_timestamp + 60)

def advance_five_minutes(current_time_map: TimeMap) -> TimeMap:
    return find_record(current_time_map.posix_timestamp + 300)

def rewind_one_hour(current_time_map: TimeMap) -> TimeMap:
    return find_record(current_time_map.posix_timestamp + 3600)

def rewind_one_minute(current_time_map: TimeMap) -> TimeMap:
    return find_record(current_time_map.posix_timestamp - 60)

def rewind_five_minutes(current_time_map: TimeMap) -> TimeMap:
    return find_record(current_time_map.posix_timestamp - 300)

def rewind_one_hour(current_time_map: TimeMap) -> TimeMap:
    return find_record(current_time_map.posix_timestamp - 3600)

def advance_one_frame(current_time_map: TimeMap) -> TimeMap:
    return find_record(current_time_map.posix_timestamp + 1)

def rewind_one_frame(current_time_map: TimeMap) -> TimeMap:
    return find_record(current_time_map.posix_timestamp - 1)

        
