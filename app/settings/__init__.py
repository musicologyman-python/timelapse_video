from pathlib import Path
import typing
import yaml

def read_settings(settings_path: str|Path) -> typing.Optional[dict]:
    match settings_path:
        case str():
            return read_settings(Path(settings_path))
    
    if not settings_path.exists():
        return None
    
    with settings_path.open(encoding='utf-8') as fp:
        return yaml.load(fp, yaml.Loader)
    
def write_settings(settings_path: str|Path, settings_dict:dict) -> None:
    match settings_path:
        case str():
            return write_settings(Path(settings_path))
        
    with settings_path.open(mode='w', encoding='utf-8') as fp:
        yaml.dump(settings_dict, fp)