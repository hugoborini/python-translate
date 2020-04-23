from tkinter import * 
from googletrans import Translator

global sentence
global selected_language
global result_translate


fenetre = Tk()

fenetre.geometry("595x323")

sentence_label = Label(fenetre, text="Enter your sentence : ")


sentence = StringVar() 
sentence.set("your sentence")
entree = Entry(fenetre, textvariable=sentence, width=30)


language_label = Label(fenetre, text="Chose your language : ")


language_liste = Listbox(fenetre)
language_liste.insert(1, "fr")
language_liste.insert(2, "en")
language_liste.insert(3, "ru")
language_liste.insert(4, "ja")

selected_language = StringVar()

def updateLabel():
    line = language_liste.curselection()[0]
    item = language_liste.get(line)
    selected_language.set(item)

translate_bouton=Button(fenetre, text="traduire", command=lambda : translate_func())


quit_button=Button(fenetre, text="quitter", command=fenetre.quit)
result_translate = Label(fenetre, text="your result",bg="yellow")

def translate(sent, country):
    translator = Translator()
    translate_result = translator.translate(sent, dest=country)
    print(translate_result.text)
    result_translate = Label(fenetre, text=translate_result.text, bg="blue")
    fenetre.update
    
    
def createall() : 
    sentence_label.pack()
    entree.pack()
    language_label.pack()
    language_liste.pack()
    translate_bouton.pack()
    quit_button.pack()
    result_translate.pack()



def translate_func() :
    updateLabel()
    translate(sentence.get(), selected_language.get())
   

createall()
fenetre.mainloop()