from googletrans import Translator

print('Enter your sentence:')
x = input()

print('Enter the language you want exp (fr,en,ja,etc...)')

y = input ()

def translate(sent, country):
    translator = Translator()
    translate_result = translator.translate(sent, dest=country)
    print(translate_result.text)

translate(x, y)