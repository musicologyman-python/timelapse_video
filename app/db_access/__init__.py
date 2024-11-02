from dataclasses import dataclass
import datetime as dt
from functools import partial
import io
from pathlib import Path
import sqlite3
import typing

from _protocols import Observable, Observer

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


def time_map_factory(cursor: sqlite3.Cursor, row: typing.Any):
    return TimeMap(*row)

class DbManager(Observable):

    def __init__(self, dbpath: str):
        self.dbpath = dbpath
        self.observers = list()
        self.state: TimeMap = None

    def execute_query(self, command_text: str, 
                      param_dict: dict=dict()) -> TimeMap:
        with sqlite3.connect(self.dbpath) as cn:
            cn.row_factory = time_map_factory
            cur = cn.execute(command_text, param_dict)
            return cur.fetchone()

    def find_record(self, timestamp: int=0) -> TimeMap:
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
        return self.execute_query(COMMAND_TEXT, {'min_time': timestamp})

    def get_last_record(self) -> None:
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
        self.state = self.execute_query(COMMAND_TEXT)
        self.update()

    def get_first_record(self) -> None:
        self.state = self.find_record()
        self.update()

    def advance_one_minute(self) -> None:
        self.state = self.find_record(self.state.posix_timestamp + 60)
        self.update()

    def advance_five_minutes(self) -> None:
        self.state =  self.find_record(self.state.posix_timestamp + 300)
        self.update()

    def advance_one_hour(self) -> None:
        self.state =  self.find_record(self.state.posix_timestamp + 3600)
        self.update()

    def rewind_one_minute(self) -> None:
        self.state =  self.find_record(self.state.posix_timestamp - 60)
        self.update()

    def rewind_five_minutes(self) -> None:
        self.state =  self.find_record(self.state.posix_timestamp - 300)
        self.update()

    def rewind_one_hour(self) -> None:
        self.state =  self.find_record(self.state.posix_timestamp - 3600)
        self.update()

    def advance_one_frame(self) -> None:
        self.state =  self.find_record(self.state.posix_timestamp + 1)
        self.update()

    def rewind_one_frame(self) -> None:
        self.state =  self.find_record(self.state.posix_timestamp - 1)
        self.update()
            
    # region implementation of Observable protocol
    
    def register(self, obs: Observer):
        self.observers.append(obs)
        
    def deregister(self, obs: Observer):
        self.observers.remove(obs)
    
    def update(self):
        obs: Observer
        for obs in self.observers:
            obs.update(self.state)

    # endregion