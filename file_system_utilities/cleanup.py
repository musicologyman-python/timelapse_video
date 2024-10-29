'''
Move log files to a logs folder
'''
from pathlib import Path

DIR_TO_CLEAN = Path.cwd()
LOGS_DIR = Path('logs')

def get_log_files(filter=lambda p:True):
    return (p for p in DIR_TO_CLEAN.iterdir() 
            if p.suffix == '.log' and filter(p))


# get empty log files
empty_log_files = (
    list(get_log_files(filter=lambda p:p.stat().st_size == 0)))

# delete empty log files
for p in empty_log_files:
    p.unlink()
        
# move non-empty logs

LOGS_DIR.mkdir(parents=True, exist_ok=True)

non_empty_log_files = (
    list(get_log_files(filter=lambda p:p.stat().st_size > 0)))

for p in non_empty_log_files:
    p.rename(LOGS_DIR / p.relative_to(DIR_TO_CLEAN))
