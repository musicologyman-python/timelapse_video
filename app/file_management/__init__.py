from collections.abc import Iterable
from pathlib import Path

def _get_files_from_time_stamped_path(time_stamped_path: Path) -> list[Path]:
    return sorted((p for p in time_stamped_path.parent.cwd().iterdir()
                    if p.is_file()
                    and p.stem.isnumeric()
                    and not p.is_symlink()), 
                    key=lambda p:int(p.stem))

def delete_all_after(time_stamped_path: Path) -> None:
    files: list[Path] = _get_files_from_time_stamped_path(time_stamped_path) 
    first_index_to_delete = files.index(time_stamped_path) + 1
    for file in files[slice(first_index_to_delete, None)]:
        file.unlink()

def delete_all_before(time_stamped_path: Path) -> None:
    files: list[Path] = _get_files_from_time_stamped_path(time_stamped_path) 
    last_index_to_delete = files.index(time_stamped_path) - 1
    for file in files[slice(0, last_index_to_delete)]:
        file.unlink()