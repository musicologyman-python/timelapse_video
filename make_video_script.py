import datetime as dt
import tkinter as tk

def main():

    root = tk.Tk()

    tk.Label(root, text='Date').pack(side=tk.LEFT)



if __name__ == '__main__':
    main()

'ffmpeg -r 30 -pattern_type glob -i "*.jpeg" -s 1024x768 -pix_fmt yuv420p -vcodec libx264 20241004.mp4'

