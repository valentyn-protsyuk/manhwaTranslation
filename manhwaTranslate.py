import os
from dotenv import load_dotenv
import time
import tkinter  # user interface
import pyautogui  # screenshot
from googletrans import Translator  # pip install googletrans==4.0.0rc1 regular version was causing issues for some reason
from PIL import Image, ImageTk  # work with screenshot
from pytesseract import pytesseract

translator = Translator()

# window object and settings
window = tkinter.Tk()
window.title('comicTranslate')

# look into this global bs
img = None
cur_cropped_img = None
text = None

# PATH TO YOUR TESSERACT !!! IMPORTANT !!!
pytesseract.tesseract_cmd = os.getenv("TESSERACT_PATH")
pytesseract_config = r'--psm 3 --oem 3'


def image_to_text():
    global cur_cropped_img
    global text
    if cur_cropped_img is not None:
        img_text = pytesseract.image_to_string(cur_cropped_img, config=pytesseract_config, lang='kor')
        img_text = img_text.replace('\n', ' ')     # in comic books they often use line breaks
        img_text = img_text.strip()
        print('img text: ' + img_text)
        translated_text = 'Try again'
        if img_text != '':
            translated_text = translator.translate(text=img_text, dest="en").text
            print('translated: ' + translated_text)
        canvas.delete("all")
        text = 'Insert text'
        canvas.create_text(100, 50, text=translated_text)

def take_screenshot():
    global img
    window.iconify()  # minimize window to take screenshot of the whole screen
    time.sleep(0.2)
    img = pyautogui.screenshot()  # take screenshot
    window.deiconify()  # bring back the window


def crop_screenshot(event=None):
    global cur_cropped_img

    if img is not None:
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
select_area_btn = tkinter.Button(window, text='Translate', command=image_to_text)
select_area_btn.pack()

canvas = tkinter.Canvas(window)
canvas.pack()

window.bind('<Configure>', crop_screenshot)  # creates transparent canvas effect

window.mainloop()

