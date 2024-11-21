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

settings_dict = {'raw_image_source_dir': Path('camera'), 'timestamped_image_dir': None, 'recent_directories': ['video_20241012', 'video_20241014']}
import sys
yaml.dump(settings_dict, sys.stdout)
# OUT: raw_image_source_dir: !!python/object/apply:pathlib.PosixPath
# OUT: - camera
# OUT: recent_directories:
# OUT: - video_20241012
# OUT: - video_20241014
# OUT: timestamped_image_dir: null
settings_dict
# OUT: {'raw_image_source_dir': PosixPath('camera'), 'timestamped_image_dir': None, 'recent_directories': ['video_20241012', 'video_20241014']}
from pprint import pprint
pprint(settings_dict)
# OUT: {'raw_image_source_dir': PosixPath('camera'),
# OUT:  'recent_directories': ['video_20241012', 'video_20241014'],
# OUT:  'timestamped_image_dir': None}
dir(Path)
# OUT: ['__bytes__', '__class__', '__delattr__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__fspath__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rtruediv__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__truediv__', '_drv', '_flavour', '_format_parsed_parts', '_from_parsed_parts', '_hash', '_lines', '_lines_cached', '_load_parts', '_make_child_relpath', '_parse_path', '_parts_normcase', '_parts_normcase_cached', '_raw_paths', '_root', '_scandir', '_str', '_str_normcase', '_str_normcase_cached', '_tail', '_tail_cached', 'absolute', 'anchor', 'as_posix', 'as_uri', 'chmod', 'cwd', 'drive', 'exists', 'expanduser', 'glob', 'group', 'hardlink_to', 'home', 'is_absolute', 'is_block_device', 'is_char_device', 'is_dir', 'is_fifo', 'is_file', 'is_junction', 'is_mount', 'is_relative_to', 'is_reserved', 'is_socket', 'is_symlink', 'iterdir', 'joinpath', 'lchmod', 'lstat', 'match', 'mkdir', 'name', 'open', 'owner', 'parent', 'parents', 'parts', 'read_bytes', 'read_text', 'readlink', 'relative_to', 'rename', 'replace', 'resolve', 'rglob', 'rmdir', 'root', 'samefile', 'stat', 'stem', 'suffix', 'suffixes', 'symlink_to', 'touch', 'unlink', 'walk', 'with_name', 'with_segments', 'with_stem', 'with_suffix', 'write_bytes', 'write_text']
settings_dict['raw_image_source_dir'].resolve()
# OUT: PosixPath('/Users/richard/temp/camera')
settings_dict['raw_image_source_dir'].expanduser()
# OUT: PosixPath('camera')
help(Path.match)
settings_dict['raw_image_source_dir'].parent
# OUT: PosixPath('.')
settings_dict['raw_image_source_dir'].parent.resolve()
# OUT: PosixPath('/Users/richard/Repos/timelapse_video')
str(settings_dict['raw_image_source_dir'])
# OUT: 'camera'
settings_dict['raw_image_source_dir'].as_posix()
# OUT: 'camera'
settings_dict['raw_image_source_dir'].as_uri()
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT:     settings_dict['raw_image_source_dir'].as_uri()
# OUT:   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/pathlib.py", line 467, in as_uri
# OUT:     raise ValueError("relative path can't be expressed as a file URI")
# OUT: ValueError: relative path can't be expressed as a file URI
settings_dict['raw_image_source_dir'].is_absolute()
# OUT: False
settings_dict['raw_image_source_dir'].absolute
# OUT: <bound method Path.absolute of PosixPath('camera')>
settings_dict['raw_image_source_dir'].absolute()
# OUT: PosixPath('/Users/richard/Repos/timelapse_video/camera')
pprint(settings_dict)
# OUT: {'raw_image_source_dir': PosixPath('camera'),
# OUT:  'recent_directories': ['video_20241012', 'video_20241014'],
# OUT:  'timestamped_image_dir': None}
settings_dict['raw_image_source_dir'] = Path('camera').absolute()
del settings_dict['recent_directories']
settings_dict['last_accessed_directory'] = Path('video_20241012').absolute()
settings_dict['timestamped_image_dir'] = Path('video_20241012').absolute()
yaml.dump(settings_dict, stream=sys.sttdout)
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT:     yaml.dump(settings_dict, stream=sys.sttdout)
# OUT:                                      ^^^^^^^^^^^
# OUT: AttributeError: module 'sys' has no attribute 'sttdout'. Did you mean: 'stdout'?
yaml.dump(settings_dict, stream=sys.stdout)
# OUT: last_accessed_directory: !!python/object/apply:pathlib.PosixPath
# OUT: - /
# OUT: - Users
# OUT: - richard
# OUT: - Repos
# OUT: - timelapse_video
# OUT: - video_20241012
# OUT: raw_image_source_dir: !!python/object/apply:pathlib.PosixPath
# OUT: - /
# OUT: - Users
# OUT: - richard
# OUT: - Repos
# OUT: - timelapse_video
# OUT: - camera
# OUT: timestamped_image_dir: !!python/object/apply:pathlib.PosixPath
# OUT: - /
# OUT: - Users
# OUT: - richard
# OUT: - Repos
# OUT: - timelapse_video
# OUT: - video_20241012
import io
with io.StringIO() as sp:
    yaml.dump(settings_dict, stream=sp)
    settings_string = sp.getvalue()
    

print(settings_string)
# OUT: last_accessed_directory: !!python/object/apply:pathlib.PosixPath
# OUT: - /
# OUT: - Users
# OUT: - richard
# OUT: - Repos
# OUT: - timelapse_video
# OUT: - video_20241012
# OUT: raw_image_source_dir: !!python/object/apply:pathlib.PosixPath
# OUT: - /
# OUT: - Users
# OUT: - richard
# OUT: - Repos
# OUT: - timelapse_video
# OUT: - camera
# OUT: timestamped_image_dir: !!python/object/apply:pathlib.PosixPath
# OUT: - /
# OUT: - Users
# OUT: - richard
# OUT: - Repos
# OUT: - timelapse_video
# OUT: - video_20241012
with io.StringIO(settings_string) as sp:
    reconstituted_settings = yaml.load(sp)
    

# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 2, in <module>
# OUT:     reconstituted_settings = yaml.load(sp)
# OUT:                              ^^^^^^^^^^^^^
# OUT: TypeError: load() missing 1 required positional argument: 'Loader'
with io.StringIO(settings_string) as sp:
    reconstituted_settings = yaml.load(sp,yaml.Loader)

pprint(reconstituted_settings)
# OUT: {'last_accessed_directory': PosixPath('/Users/richard/Repos/timelapse_video/video_20241012'),
# OUT:  'raw_image_source_dir': PosixPath('/Users/richard/Repos/timelapse_video/camera'),
# OUT:  'timestamped_image_dir': PosixPath('/Users/richard/Repos/timelapse_video/video_20241012')}
### 