import time
import tkinter  # user interface
import pyautogui  # screenshot
from PIL import Image, ImageTk  # work with screenshot

# window object and settings
window = tkinter.Tk()
window.title('comicTranslate')

# look into this global bs
img = None
cur_cropped_img = None
text = None

def take_screenshot():
    global img
    window.iconify()  # minimize window to take screenshot of the whole screen
    time.sleep(0.2)
    img = pyautogui.screenshot()  # take screenshot
    window.deiconify()  # bring back the window


def crop_screenshot(event=None):
    global cur_cropped_img

    dimensions = window.geometry()  # gets string with format: WxH+X+Y
    wh, x, y = dimensions.split('+')
    w, h = wh.split('x')

    cropbox = (int(x),int(y), int(x) + int(w), int(y) + int(h)) 
    cropped_img = img.crop(box=cropbox)
    cur_cropped_img = cropped_img
    cropped_img = ImageTk.PhotoImage(cropped_img)
    canvas.create_image(0, 0, anchor='nw', image=cropped_img)
    canvas.image = cropped_img

select_area_btn = tkinter.Button(window, text='Select Img area', command=take_screenshot)
select_area_btn.pack()

canvas = tkinter.Canvas(window)
canvas.pack()

window.bind('<Configure>', crop_screenshot)  # creates transparent canvas effect

window.mainloop()

