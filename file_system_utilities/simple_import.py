from pathlib import Path

from loguru import logger

from write_image_date_time import get_image_files, label_image_files

def main():

    logger.add('file_{time:YYYY-MM-DD HH.mm.ss}.log')

    source_dir_names = ['20241029', '20241030', '20241031', '20241101', '20241102']
    source_parent = Path('~/temp/camera').expanduser()
    source_dirs = [source_parent / source_dir_name
                   for source_dir_name in source_dir_names]

    dest_parent = Path('~/Repos/timelapse_video').expanduser()
    export_spec = [(source_dir, dest_parent / f'video_{source_dir.name}') 
                   for source_dir in source_dirs]

    for src, dest in export_spec:
        print(f'{src} -> {dest}')
        if not dest.exists():
            dest.mkdir(parents=True, exist_ok=True)

        image_files =  get_image_files(src)
        label_image_files(dest, image_files)

        
if __name__ == '__main__':
    main()