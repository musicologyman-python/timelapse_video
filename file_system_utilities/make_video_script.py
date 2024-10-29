from pathlib import Path
import os
import re
import tkinter.filedialog as fd
import subprocess
import sys

FRAME_RATE = 30
STILL_IMAGE_EXT = '.jpeg'
RESOLUTION = '1024x768'
VIDEO_DIR_NAME: re.Pattern = re.compile(
    r'video_(?P<date>20\d{2}(0[1-9]|1[0-2]))')

def main():
    PROMPT: str = 'Select a directory containing the videos to be concatenated'
    if (dir_name:=fd.askdirectory(title=PROMPT, initialdir=Path.cwd())) is None:
        print('No directory selected. Exiting.', file=sys.stderr)
        sys.stderr.flush()
        sys.exit(1)
    
    if (m:=VIDEO_DIR_NAME.search(dir_name)) is None:
        print(f'The name of the directory "{dir_name}" is invalid. Exiting.',
              file=sys.stderr) 
        sys.stderr.flush()
        sys.exit(2)

    video_dir: Path = Path(dir_name)
    video_file_name = f"{m['date']}.mp4"
    cp: subprocess.CompletedProcess \
        = subprocess.run(['ffmpeg', 
                        '-r', str(FRAME_RATE),
                        '-pattern_type', 'glob',
                        '-i',  STILL_IMAGE_EXT,
                        '-s', RESOLUTION,
                        '-pix_fmt', 'yuv420p',
                        '-vcodec', 'libx264',
                        video_file_name],
                        cwd = str(video_dir))
                    

if __name__ == '__main__':
    main()

# 'ffmpeg -r 30 -pattern_type glob -i "*.jpeg" -s 1024x768 -pix_fmt yuv420p -vcodec libx264 20241004.mp4'

