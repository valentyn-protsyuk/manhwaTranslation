from PIL import Image
from pytesseract import pytesseract

myconfig = r'--psm 3 --oem 3'
img_kor = 'C:\myProjects\CTvsc\imgs\pietroch1kor.png'
# r'--psm 3 --oem 3'
# r'-c tessedit_char_whitelist="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.!? " --psm 3'

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

korean = pytesseract.image_to_string(Image.open(img_kor), config=myconfig, lang='kor')

print('korean:')
print(korean)