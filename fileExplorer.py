import tkinter as tk
from tkinter import *
from tkinter import filedialog


def file_path() -> str:
    root = tk.Tk()
    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()
    path = []

    def open_file():
        filepath = filedialog.askopenfilename(initialdir="D:\\PythonBasic\\PythonPro\\OCR_text_detection",
                                              title="Open File", filetypes=[("Image files", ".jpg .jpeg .png")])
        path.append(filepath)

    button = Button(text="Open File Explorer",command=open_file)
    canvas.create_window(150, 150, window=button)
    print("AFTER UPLOAD THE FILE CLOSE THE FILE EXPLORER WINDOW TO PROCEED FURTHER")
    root.mainloop()
    return path[0]

