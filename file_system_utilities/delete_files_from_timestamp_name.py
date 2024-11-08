'''
Delete jpeg files named using a timestamp subject to a time constraint
'''

import operator
from pathlib import Path
import tkinter as tk
import tkinter.filedialog as fd

from icecream import ic

class FileDeletionDialog(tk.Tk):

    def __init__(self):
        super().__init__()
        
        WINDOW_BACKGROUND = 'lightgray'
        DEFAULT_RELIEF = tk.SUNKEN
        DEFAULT_BORDER_WIDTH = 1
        
        #self.geometry('300x300+200+200')
        self.configure(background=WINDOW_BACKGROUND)
        self.configure(padx=5, pady=5)

        tk.Label(self, text='Directory:', background=WINDOW_BACKGROUND) \
            .grid(row=0, column=0)
        self.image_directory = tk.StringVar(self)
        self.directory_entry = tk.Entry(self, 
                                        textvariable=self.image_directory,
                                        relief=DEFAULT_RELIEF, 
                                        bd=DEFAULT_BORDER_WIDTH,
                                        state='readonly')
        self.directory_entry.grid(row=0, column=1, pady=2, columnspan=2)
        tk.Label(self, text='First file:', background=WINDOW_BACKGROUND) \
            .grid(row=1, column=0)
        self.first_file = tk.StringVar(self)
        self.first_file_entry =  tk.Entry(self, 
                                          textvariable=self.first_file,
                                          relief=DEFAULT_RELIEF, 
                                          bd=DEFAULT_BORDER_WIDTH,
                                          state='readonly')
        self.first_file_entry.grid(row=1, column=1, pady=2, columnspan=2)

        relief_label_frame = tk.LabelFrame(bg=WINDOW_BACKGROUND, 
                                           bd=1, 
                                           relief=tk.SUNKEN, 
                                           text='Relief')
        relief_label_frame.grid(row=2, column=1, sticky=tk.W)
        
        self.relief_variable = tk.StringVar(relief_label_frame) 
        
        raised_radiobutton = tk.Radiobutton(relief_label_frame,
                                            text='raised', 
                                            value='raised', 
                                            variable=self.relief_variable,
                                            command=self._update_relief,
                                            anchor=tk.W)
        raised_radiobutton.pack(side=tk.TOP, expand=True, fill=tk.X)
                                   
        sunken_radiobutton = tk.Radiobutton(relief_label_frame,
                                            text='sunken', 
                                            value='sunken', 
                                            variable=self.relief_variable,
                                            command=self._update_relief,
                                            anchor=tk.W)
        sunken_radiobutton.pack(side=tk.TOP, expand=True, fill=tk.X)
                                   
        flat_radiobutton = tk.Radiobutton(relief_label_frame,
                                          text='flat', 
                                          value='flat', 
                                          variable=self.relief_variable,
                                          command=self._update_relief,
                                          anchor=tk.W)
        flat_radiobutton.pack(side=tk.TOP, expand=True, fill=tk.X)
                                   
        ridge_radiobutton = tk.Radiobutton(relief_label_frame,
                                           text='ridge', 
                                           value='ridge', 
                                           variable=self.relief_variable,                                        
                                           command=self._update_relief,
                                           anchor=tk.W)
        ridge_radiobutton.pack(side=tk.TOP, expand=True, fill=tk.X)
                                   
        solid_radiobutton = tk.Radiobutton(relief_label_frame,
                                           text='solid', 
                                           value='solid', 
                                           variable=self.relief_variable,                                        
                                           command=self._update_relief,
                                           anchor=tk.W)
        solid_radiobutton.pack(side=tk.TOP, expand=True, fill=tk.X)
                                   
        groove_radiobutton = tk.Radiobutton(relief_label_frame,
                                            text='groove', 
                                            value='groove', 
                                            variable=self.relief_variable,                                        
                                            command=self._update_relief,
                                            anchor=tk.W)
        groove_radiobutton.pack(side=tk.TOP, expand=True, fill=tk.X)

        self.relief_variable.set(DEFAULT_RELIEF)
        
        border_width_frame = tk.Frame()
        border_width_frame.grid(row=2, column=2, padx=5, pady=5, sticky=tk.NW)
        
        tk.Label(border_width_frame, text='Border width:', anchor=tk.W) \
            .pack(fill=tk.X)
        
        self.border_width = tk.StringVar(self)
        self.border_width.set(str(DEFAULT_BORDER_WIDTH))
        self.border_width_spinbox = tk.Spinbox(border_width_frame, 
                                               from_=1, to=5, 
                                               textvariable=self.border_width, 
                                               justify=tk.RIGHT,
                                               command=self._update_border_width)
        self.border_width_spinbox.pack(fill=tk.X, padx=10)
        
    def _update_relief(self):
        ic('_update_relief')
        ic(self.relief_variable.get())
        relief = self.relief_variable.get()
        self.directory_entry.configure(relief=relief)
        self.first_file_entry.configure(relief=relief)
        
    def _update_border_width(self):
        ic('_update_border_width')
        ic(self.border_width.get())
        border_width = self.border_width.get()
        self.directory_entry.configure(bd=int(border_width))
        self.first_file_entry.configure(bd=int(border_width))
                                   
def main():
    FileDeletionDialog().mainloop()

if __name__ == '__main__':
    main()



# files = sorted([p for p in Path.cwd().iterdir() if p.suffix == '.jpeg'], key=operator.attrgetter('stem'))

# for p in files:
#     if int(p.stem) < 20241011000045:
#         p.unlink()
