from googletrans import Translator

def translate_text(text, dest='en'):
    translator = Translator()
    translated = translator.translate(text, dest=dest)
    return translated.text
