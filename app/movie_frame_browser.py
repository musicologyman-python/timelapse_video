#!/usr/bin/env python3

from pathlib import Path
import sqlite3
import tkinter as tk
import tkinter.filedialog as fd

from icecream import ic
from PIL import Image, ImageTk, ImageOps

import db_access
import _protocols

PHOTO_SIZE = (768, 1024)
BUTTON_IMAGE_SIZE = (64, 64)

def get_photo_image(image_path: str, parent, image_size=BUTTON_IMAGE_SIZE) \
        -> ImageTk.PhotoImage:
    with Image.open(image_path) as img:
        return ImageTk.PhotoImage(ImageOps.contain(img, image_size), 
                                  master=parent)

class App(tk.Tk, _protocols.Observer):
    
    # region constants

    PLACEHOLDER_IMAGE = 'img/white_rectangle.jpg'
    OPEN_IMAGE_DIR    = 'icons/image_folder.jpg'
    OPEN_DB           = 'icons/db_icon.jpg'
    DELETE_ALL_BEFORE = 'icons/delete_before.jpg'
    DELETE_ALL_AFTER  = 'icons/delete_after.jpg'
    FIRST_FRAME       = 'nav_buttons/0_first_frame.jpg'
    BACK_1_HOUR       = 'nav_buttons/1_back_1_hour.jpg'
    BACK_5_MINUTES    = 'nav_buttons/2_back_5_minutes.jpg'
    BACK_1_MINUTE     = 'nav_buttons/3_back_1_minute.jpg'
    BACK_1_FRAME      = 'nav_buttons/3_back_1_frame.jpg'
    FORWARD_1_FRAME   = 'nav_buttons/4_forward_1_frame.jpg'
    FORWARD_1_MINUTE  = 'nav_buttons/4_forward_1_minute.jpg'
    FORWARD_5_MINUTES = 'nav_buttons/5_forward_5_minutes.jpg'
    FORWARD_1_HOUR    = 'nav_buttons/6_forward_1_hour.jpg'
    LAST_FRAME        = 'nav_buttons/7_last_frame.jpg'
    
    # endregion

    def __init__(self):
        
        super().__init__()
        
        self.title('Movie Frame Browser')
        self.resizable(False, False)
        self._image_database: str = None
        self._image_dir = None
        self._db_manager: db_access.DbManager = None

        content_frame = tk.Frame(self)
        content_frame.pack(fill='both', side='left', expand=True, ipadx=4, 
                         ipady=4)

        # region right top frame setup

        top_frame = tk.Frame(content_frame) 
        top_frame.pack(fill='x', side='top', expand=False)

        toolbar_frame = tk.Frame(top_frame)
        toolbar_frame.pack(fill='x', side='top', expand=True)
        
        self.image_folder_image = get_photo_image(App.OPEN_IMAGE_DIR,
                                                  parent=toolbar_frame)
        self.image_folder_button = tk.Button(toolbar_frame,
                                             image=self.image_folder_image,
                                             command=self._select_image_directory)
        self.image_folder_button.pack(side='left')
        
        self.image_db_image = get_photo_image(App.OPEN_DB,
                                              parent=toolbar_frame)
        self.image_db_button = tk.Button(toolbar_frame,
                                        image=self.image_db_image,
                                        command=self._select_image_database)
        self.image_db_button.pack(side='left')
        
        self.delete_all_before_image = get_photo_image(App.DELETE_ALL_BEFORE,
                                                       parent=toolbar_frame)
        self.delete_all_before_button = \
            tk.Button(toolbar_frame, image=self.delete_all_before_image,
                      command=lambda: ic("delete all before not implemented"))
        self.delete_all_before_button.pack(side='left')

        self.delete_all_after_image = get_photo_image(App.DELETE_ALL_AFTER,
                                                       parent=toolbar_frame)
        self.delete_all_after_button = \
            tk.Button(toolbar_frame, image=self.delete_all_after_image,
                      command=lambda: ic("delete all after not implemented"))
        self.delete_all_after_button.pack(side='left')

        filename_caption_label = tk.Label(top_frame, 
                                          text='current file:', anchor='nw')
        filename_caption_label.pack(side='left')
        
        self.current_file = tk.StringVar(self)
        filename_label = tk.Label(top_frame, 
                                       textvariable=self.current_file,
                                       relief=tk.SUNKEN, anchor=tk.NW, 
                                       bg='#ffffff')
        filename_label.pack(side=tk.LEFT, fill=tk.X, expand=True, 
                                 padx=4, pady=4)

        bottom_frame = tk.Frame(content_frame)
        bottom_frame.pack(fill='both', side='bottom', expand=True, 
                                padx=4, pady=4)

        self.photo = get_photo_image(image_path=App.PLACEHOLDER_IMAGE, 
                                     parent=self, image_size=PHOTO_SIZE)
        self.photo_label = tk.Label(bottom_frame, image=self.photo, 
                               relief=tk.SUNKEN)
        self.photo_label.pack(fill='both', side='top', expand=True)
        
        # endregion

        # region Button setup

        nav_button_frame = tk.Frame(bottom_frame)
        nav_button_frame.pack(ipadx=4, ipady=5, side='bottom')
        
        self.first_frame_image = get_photo_image(App.FIRST_FRAME, 
                                            parent=nav_button_frame)
        self.first_frame_button = tk.Button(nav_button_frame,
                          image=self.first_frame_image,
                          command=self._go_to_first_frame)
        self.first_frame_button.pack(side='left')

        self.back_one_hour_image = get_photo_image(App.BACK_1_HOUR, 
                                              parent=nav_button_frame)
        self.back_one_hour_button = tk.Button(nav_button_frame,
                          image=self.back_one_hour_image,
                          command=self._go_back_one_hour)
        self.back_one_hour_button.pack(side='left')

        self.back_five_minutes_image = get_photo_image(App.BACK_5_MINUTES, 
                                                  parent=nav_button_frame)
        self.back_five_minutes_button = tk.Button(nav_button_frame,
                          image=self.back_five_minutes_image,
                          command=self._go_back_five_minutes)
        self.back_five_minutes_button.pack(side='left')

        self.back_one_minute_image = get_photo_image(App.BACK_1_MINUTE, 
                                                  parent=nav_button_frame)
        self.back_one_minute_button = tk.Button(nav_button_frame,
                          image=self.back_one_minute_image,
                          command=self._go_back_one_minute)
        self.back_one_minute_button.pack(side='left')

        self.back_one_frame_image = get_photo_image(App.BACK_1_FRAME, 
                                               parent=nav_button_frame)
        self.back_one_frame_button = tk.Button(nav_button_frame,
                          image=self.back_one_frame_image,
                          command=self._go_back_one_frame)
        self.back_one_frame_button.pack(side='left')

        self.forward_one_frame_image = get_photo_image(App.FORWARD_1_FRAME, 
                                                  parent=nav_button_frame)
        self.forward_one_frame_button = tk.Button(nav_button_frame,
                          image=self.forward_one_frame_image,
                          command=self._go_forward_one_frame)
        self.forward_one_frame_button.pack(side='left')

        self.forward_one_minute_image = get_photo_image(App.FORWARD_1_MINUTE, 
                                                     parent=nav_button_frame)
        self.forward_one_minute_button = tk.Button(nav_button_frame,
                          image=self.forward_one_minute_image,
                          command=self._go_forward_one_minute)
        self.forward_one_minute_button.pack(side='left')

        self.forward_five_minutes_image = get_photo_image(App.FORWARD_5_MINUTES, 
                                                     parent=nav_button_frame)
        self.forward_five_minutes_button = tk.Button(nav_button_frame,
                          image=self.forward_five_minutes_image,
                          command=self._go_forward_five_minutes)
        self.forward_five_minutes_button.pack(side='left')

        self.forward_one_hour_image = get_photo_image(App.FORWARD_1_HOUR, 
                                                 parent=nav_button_frame)
        self.forward_one_hour_button = tk.Button(nav_button_frame,
                          image=self.forward_one_hour_image,
                          command=self._go_forward_one_hour)
        self.forward_one_hour_button.pack(side='left')

        self.to_last_frame_image = get_photo_image(App.LAST_FRAME, parent=nav_button_frame)
        self.to_last_frame_button = tk.Button(nav_button_frame,
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

        
    # region menu handlers
        
    def _select_image_directory(self):
        if (image_dir := 
                fd.askdirectory(parent=self, title='Select image directory',
                                initialdir=Path.cwd())) is not None:
            self._image_dir = image_dir
            ic(f'The user has selected {self._image_dir}')
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
            
            self._image_database = image_db
            self._image_dir = Path(image_db).parent
            self._db_manager = db_access.DbManager(self._image_database)
            self._db_manager.register(self)

    # endregion 

    # region button event handlers

    def _go_to_first_frame(self):
        ic('_go_to_first_frame')
        self._db_manager.get_first_record()

    def _go_back_one_hour(self):
        ic('_go_back_one_hour')
        self._db_manager.rewind_one_hour()

    def _go_back_five_minutes(self):
        ic("_go_back_five_minutes")
        self._db_manager.rewind_five_minutes()

    def _go_back_one_minute(self):
        ic("_go_back_one_minute")
        self._db_manager.rewind_one_minute()

    def _go_back_one_frame(self):
        ic("_go_back_one_frame")
        self._db_manager.rewind_one_frame()

    def _go_forward_one_frame(self):
        ic("_go_forward_one_frame")
        self._db_manager.advance_one_frame()

    def _go_forward_one_minute(self):
        ic("_go_forward_one_minute")
        self._db_manager.advance_one_minute()

    def _go_forward_five_minutes(self):
        ic("_go_forward_five_minutes")
        self._db_manager.advance_five_minutes()

    def _go_forward_one_hour(self):
        ic("_go_forward_one_hour")
        self._db_manager.advance_one_hour()

    def _go_to_last_frame(self):
        ic("_go_to_last_frame")
        self._db_manager.get_last_record()
        
    # endregion
    
    # region implementation of _protocol.Observer
    def update(self, payload: db_access.TimeMap) -> None:

        image_path = self._image_dir / payload.filename 
        self.current_file.set(str(image_path))
        image = get_photo_image(image_path, parent=self, image_size=PHOTO_SIZE)
        self.photo_label.configure(image=image)
        self.photo_label.image = image

    #end region


def main():
    App().mainloop()

if __name__ == '__main__':
    main()
