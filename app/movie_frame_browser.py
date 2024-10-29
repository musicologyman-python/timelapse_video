#!/usr/bin/env python3

from pathlib import Path
import sqlite3
import tkinter as tk
import tkinter.filedialog as fd

from icecream import ic
from PIL import Image, ImageTk, ImageOps

PHOTO_SIZE = (768, 1024)
BUTTON_IMAGE_SIZE = (64, 64)

def get_photo_image(image_path: str, parent, image_size=BUTTON_IMAGE_SIZE) \
        -> ImageTk.PhotoImage:
    with Image.open(image_path) as img:
        return ImageTk.PhotoImage(ImageOps.contain(img, image_size), 
                                  master=parent)

class App(tk.Tk):
    
    # region constants

    PLACEHOLDER_IMAGE = 'img/white_rectangle.jpg'
    FIRST_FRAME       = 'nav_buttons/0_first_frame.jpg'
    BACK_1_HOUR       = 'nav_buttons/1_back_1_hour.jpg'
    BACK_5_MINUTES    = 'nav_buttons/2_back_5_minutes.jpg'
    BACK_1_FRAME      = 'nav_buttons/3_back_1_frame.jpg'
    FORWARD_1_FRAME   = 'nav_buttons/4_forward_1_frame.jpg'
    FORWARD_5_MINUTES = 'nav_buttons/5_forward_5_minutes.jpg'
    FORWARD_1_HOUR    = 'nav_buttons/6_forward_1_hour.jpg'
    LAST_FRAME        = 'nav_buttons/7_last_frame.jpg'
    
    # endregion

    def __init__(self):
        
        super().__init__()
        
        self.title('Movie Frame Browser')
        self.resizable(False, False)

        self.listbox_data = tk.Variable()
        self.time_listbox = tk.Listbox(self, listvariable=self.listbox_data,
                                       relief='sunken', font='Monaco 14')
        self.time_listbox.pack(fill='both', side='left', expand=False, padx=4, 
                               pady=4)

        right_frame = tk.Frame(self)

        right_frame.pack(fill='both', side='left', expand=True, ipadx=4, 
                         ipady=4)

        # region right top frame setup

        right_top_frame = tk.Frame(right_frame) 
        right_top_frame.pack(fill='x', side='top', expand=False)

        filename_caption_label = tk.Label(right_top_frame, 
                                          text='current file:', anchor='nw')
        filename_caption_label.pack(side='left')
        
        self.current_file = tk.StringVar()
        filename_label = tk.Label(right_top_frame, 
                                  textvariable=self.current_file,
                                  relief=tk.SUNKEN, anchor=tk.NW, bg='#ffffff')
        filename_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=4, pady=4)

        right_bottom_frame = tk.Frame(right_frame)
        right_bottom_frame.pack(fill='both', side='bottom', expand=True, 
                                padx=4, pady=4)

        self.photo = get_photo_image(image_path=App.PLACEHOLDER_IMAGE, 
                                     parent=self, image_size=PHOTO_SIZE)
        photo_label = tk.Label(right_bottom_frame, image=self.photo, 
                               relief=tk.SUNKEN)
        photo_label.pack(fill='both', side='top', expand=True)
        
        # endregion

        # region Button setup

        button_frame = tk.Frame(right_bottom_frame)
        button_frame.pack(ipadx=4, ipady=5, side='bottom')
        
        self.first_frame_image = get_photo_image(App.FIRST_FRAME, 
                                            parent=button_frame)
        self.first_frame_button = tk.Button(button_frame,
                          image=self.first_frame_image,
                          command=self._go_to_first_frame)
        self.first_frame_button.pack(side='left')

        self.back_one_hour_image = get_photo_image(App.BACK_1_HOUR, 
                                              parent=button_frame)
        self.back_one_hour_button = tk.Button(button_frame,
                          image=self.back_one_hour_image,
                          command=self._go_back_one_hour)
        self.back_one_hour_button.pack(side='left')

        self.back_five_minutes_image = get_photo_image(App.BACK_5_MINUTES, 
                                                  parent=button_frame)
        self.back_five_minutes_button = tk.Button(button_frame,
                          image=self.back_five_minutes_image,
                          command=self._go_back_five_minutes)
        self.back_five_minutes_button.pack(side='left')

        self.back_one_frame_image = get_photo_image(App.BACK_1_FRAME, 
                                               parent=button_frame)
        self.back_one_frame_button = tk.Button(button_frame,
                          image=self.back_one_frame_image,
                          command=self._go_back_one_frame)
        self.back_one_frame_button.pack(side='left')

        self.forward_one_frame_image = get_photo_image(App.FORWARD_1_FRAME, 
                                                  parent=button_frame)
        self.forward_one_frame_button = tk.Button(button_frame,
                          image=self.forward_one_frame_image,
                          command=self._go_forward_one_frame)
        self.forward_one_frame_button.pack(side='left')

        self.forward_five_minutes_image = get_photo_image(App.FORWARD_5_MINUTES, 
                                                     parent=button_frame)
        self.forward_five_minutes_button = tk.Button(button_frame,
                          image=self.forward_five_minutes_image,
                          command=self._go_forward_five_minutes)
        self.forward_five_minutes_button.pack(side='left')

        self.forward_one_hour_image = get_photo_image(App.FORWARD_1_HOUR, 
                                                 parent=button_frame)
        self.forward_one_hour_button = tk.Button(button_frame,
                          image=self.forward_one_hour_image,
                          command=self._go_forward_one_hour)
        self.forward_one_hour_button.pack(side='left')

        self.to_last_frame_image = get_photo_image(App.LAST_FRAME, parent=button_frame)
        self.to_last_frame_button = tk.Button(button_frame,
                          image=self.to_last_frame_image,
                          command=self._go_to_last_frame)
        self.to_last_frame_button.pack(side='left')
        
        # endregion

        # region Menu setup

        self.menubar = tk.Menu(self)
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label='Select Image Directory ...', 
                              command=self._select_image_directory)
        self.file_menu.add_command(label='Select Image Database ...', 
                              command=self._select_image_database)
        self.menubar.add_cascade(label='File', menu=self.file_menu)

        
        self.config(menu=self.menubar)
        
        # endregion

        self.after(1000, self.time_listbox.focus_force())
        
    def _select_image_directory(self):
        if (image_dir := 
                fd.askdirectory(parent=self, title='Select image directory',
                                initialdir=Path.cwd())) is not None:
            self.image_dir = image_dir
            ic(f'The user has selected {self.image_dir}')
        else:
            ic(f'No directory selected')

    def _select_image_database(self):
        if (image_db :=
                fd.askopenfilename(defaultextension='.db',
                                   filetypes=[('SQLite Databases', '.db'),
                                              ('All files', '.*')],
                                    parent=self, 
                                    title='Select an image database')):
            ic(f'selected {image_db}')
            self.image_database = image_db
            self._populate_time_listbox()

    def _populate_time_listbox(self):
        with sqlite3.connect(self.image_database) as cn:
            cur: sqlite3.Cursor = cn.execute('''SELECT hour, minute
                                                FROM vw_minutes
                                                WHERE mod(minute, 15) = 0
                                                order by day, hour, minute''')
            results = cur.fetchall()
            self.listbox_data.set([f'{row[0]:>2}:{row[1]:02}' for row in results])



    # region button event handlers

    def _go_to_first_frame(self):
        ic('_go_to_first_frame')

    def _go_back_one_hour(self):
        ic('_go_back_one_hour')

    def _go_back_five_minutes(self):
        ic("_go_back_five_minutes")

    def _go_back_one_frame(self):
        ic("_go_back_one_frame")

    def _go_forward_one_frame(self):
        ic("_go_forward_one_frame")

    def _go_forward_five_minutes(self):
        ic("_go_forward_five_minutes")

    def _go_forward_one_hour(self):
        ic("_go_forward_one_hour")

    def _go_to_last_frame(self):
        ic("_go_to_last_frame")
        
    # endregion


def main():
    App().mainloop()

if __name__ == '__main__':
    main()
