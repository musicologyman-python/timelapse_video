from pathlib import Path

def get_log_files(filter=lambda p:True):
    return (p for p in Path.cwd().iterdir() 
            if p.suffix == '.log' and filter(p))


# cleanup logs
empty_log_files = (
    list(get_log_files(filter=lambda p:p.stat().st_size == 0)))

for p in empty_log_files:
    p.unlink()
        
# move non-empty logs

logs_dir = Path('logs')
logs_dir.mkdir(parents=True, exist_ok=True)

non_empty_log_files = (
    list(get_log_files(filter=lambda p:p.stat().st_size > 0)))

for p in non_empty_log_files:
    p.rename(logs_dir / p.relative_to(Path.cwd()))