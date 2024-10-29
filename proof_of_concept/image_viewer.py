import tkinter as tk
import tkinter.filedialog as fd

def main():
    root: tk.Tk = tk.Tk()
    # root.geometry('640x480')
    # fr = tk.Frame(root, relief=tk.RAISED, bg='green').pack()
    fr = root
    tk.Label(fr, text='Current image:', font='Verdana 14 bold') \
        .pack(ipadx=4, side='left')
    current_image_label = tk.Label(fr, text='None selected', 
                                   font='Verdana 14', relief='ridge')
    current_image_label.pack(ipadx=4, fill='x', side='left')

    select_image_button = tk.Button(root, text='Select image ...')
    select_image_button.pack()

    # force the window to take system-wide focus after one second
    # by calling focus_force on a control that supports the method
    root.after(1000, lambda: current_image_label.focus_force())
    root.mainloop()


if __name__ == '__main__':
    main()