import pyautogui
import tkinter as tk
from tkinter.filedialog import *
import datetime


def screenshot_path() -> str:
    root = tk.Tk()
    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()
    path = []

    def take_screenshot():
        my_screenshot = pyautogui.screenshot()
        fixed_path = "D:\\PythonBasic\\PythonPro\\OCR_text_detection\\image\\"
        t = datetime.datetime.now()
        variable_path = str(t.year)+str(t.month)+str(t.day)+str(t.hour)+str(t.minute)+str(t.microsecond)
        my_screenshot.save(fixed_path+variable_path+"_screenshot.png")
        path.append(fixed_path+variable_path+"_screenshot.png")

    my_button = tk.Button(text="Take Screenshot", command=take_screenshot, font=10)
    canvas.create_window(150, 150, window=my_button)
    print("AFTER UPLOAD THE FILE CLOSE THE TAKE SCREENSHOT WINDOW TO PROCEED FURTHER")
    root.mainloop()
    return path[0]

