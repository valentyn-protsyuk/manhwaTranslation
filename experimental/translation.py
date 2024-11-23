from googletrans import Translator  # pip install googletrans==4.0.0rc1 regular version was causing issues for some reason

translator = Translator()

translated_text = translator.translate("hello world", dest="ru")

print(translated_text.text)