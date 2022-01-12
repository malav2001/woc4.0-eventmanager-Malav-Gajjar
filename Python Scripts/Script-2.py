# from googletrans import Translator

# translator = Translator()
# result = translator.translate('Mikä on nimesi', src='fi', dest='fr')

# print(result.src)
# print(result.dest)
# print(result.text)

from googletrans import Translator

with open('spanish_text.txt') as f:
    text_to_translate = f.read()
    translator = Translator()
    # print(translator.detect(text_to_translate))
    result = translator.translate(text_to_translate,dest='en').text
with open('translated_spanish_text_into_english.txt','w') as f:
    f.write(result)