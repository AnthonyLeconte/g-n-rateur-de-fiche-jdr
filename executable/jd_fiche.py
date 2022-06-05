import os
from tkinter import *
from fiche import *



Main = Tk()
Main.title("Bienvenue")



label = Label(Main,text="bienvenue\naventurier",padx=200,pady=100)
label.pack()

menubar=Menu(Main)
Menu_cascade=Menu(menubar, tearoff=0)

Menu_cascade.add_command(label="créer une fiche",command=creation)
Menu_cascade.add_command(label="modifier une fiche",command=edition)
Menu_cascade.add_command(label="afficher une fiche",command=affiche)

menubar.add_cascade(label="fiche",menu=Menu_cascade)



Main.config(menu=menubar)


Main.mainloop()
