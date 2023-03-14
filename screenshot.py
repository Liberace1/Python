import time
import pyautogui
import tkinter as tk

def screenshot():
    name = int(round(time.time() * 1000))
    name ='C:/Users/Seaka/Downloads/Python/Python/Screenshotsdata/{}.png'.format(name)
    time.sleep(0.5)
    img = pyautogui.screenshot(name)
    img.show ()


root=tk.Tk()
frame = tk.Frame()
frame.pack()


button = tk.Button(frame, text="Screenshot", command=screenshot)
button.pack(side=tk.LEFT)

close = tk.Button(frame, text="Quit", command=quit)
close.pack(side=tk.LEFT)


root.mainloop()