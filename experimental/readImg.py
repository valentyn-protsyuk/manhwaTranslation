from PIL import Image
from pytesseract import pytesseract

img_kor = 'C:\myProjects\CTvsc\imgs\pietroch1kor.png'
bad_img_en = 'C:\myProjects\comicTranslation\experimental\imgs\enBadImg.png'
ok_img_en = 'C:\myProjects\comicTranslation\experimental\imgs\enSomeNoise.png'

myconfig = r'--psm 3 --oem 3'
# r'--psm 3 --oem 3'
# r'-c tessedit_char_whitelist="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.!? " --psm 3'

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

korean = pytesseract.image_to_string(Image.open(img_kor), config=myconfig, lang='kor')
bad_en = pytesseract.image_to_string(Image.open(bad_img_en), config=myconfig, lang='eng')

print('korean:')
print(korean)

print('Bad English:')
print(bad_en)