from pathlib import Path
import datetime as dt

def get_jpeg_files(dirpath):
    return [p for p in Path(dirpath).iterdir() 
            if p.is_file() and p.suffix == '.jpeg']

def rename_file(p: Path):
    time_stamp = int(p.stem)
    new_stem = dt.datetime.fromtimestamp(time_stamp).strftime('%Y%m%d%H%M%S')
    p.rename(p.with_stem(new_stem))
    
def rename_files(jpeg_files):
    for p in jpeg_files:
        rename_file(p)

def main():
    dirpaths = [p for p in Path('record_counts.txt').read_text().splitlines()
                if len(p.strip()) > 0]
    for dirpath in dirpaths:
        jpeg_files = get_jpeg_files(dirpath)
        rename_files(jpeg_files)
    

if __name__ == '__main__':
    main()
