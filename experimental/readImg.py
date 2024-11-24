from PIL import Image
from pytesseract import pytesseract

img_kor = 'C:\myProjects\CTvsc\imgs\pietroch1kor.png'
bad_img_eng = 'C:\myProjects\comicTranslation\experimental\imgs\enBadImg.png'
ok_img_eng = 'C:\myProjects\comicTranslation\experimental\imgs\enSomeNoise.png'

my_config = r'--psm 3 --oem 3'

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

korean = pytesseract.image_to_string(Image.open(img_kor), config=my_config, lang='kor')
bad_eng = pytesseract.image_to_string(Image.open(bad_img_eng), config=my_config, lang='eng')
ok_eng = pytesseract.image_to_string(Image.open(ok_img_eng), config=my_config, lang='eng')

print('korean:')
print(korean)

print('Bad English:')
print(bad_eng)

print('Ok English:')
print(ok_eng)