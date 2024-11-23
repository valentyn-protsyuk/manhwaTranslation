import time
import tkinter  # library for canvas & UI
import pyautogui  # library for screenshots
from PIL import Image, ImageTk   # work with screenshot

# window object and settings
window = tkinter.Tk()
window.title('comicTranslate')

# Function to get position of the window
def window_position(event=None):
    dimensions = window.geometry()  # gets string with format: WxH+X+Y
    wh, x, y = dimensions.split('+')
    w, h = wh.split('x')

    print(dimensions)
    print(w)
    print(h)
    print(x)
    print(y)
    print(int(y))  # + type(int(h)))

    return (x, y, x+w, y+h)

canvas = tkinter.Canvas(window)
canvas.pack()

scr = pyautogui.screenshot()
time.sleep(1)

# Bind the <Configure> event to the window_position function
# window.bind('<Configure>', window_position)
window.after(100, window_position)
tit_y = 30  # title bar offset
bor_x = 5   # border offset
base = 156   # x,y
cropped_img = scr.crop(box=(base+bor_x,base+tit_y,(base+382+bor_x),(base+269+tit_y)))
cropped_img = ImageTk.PhotoImage(cropped_img)

canvas.create_image(0, 0, anchor='nw', image=cropped_img)

window.mainloop()