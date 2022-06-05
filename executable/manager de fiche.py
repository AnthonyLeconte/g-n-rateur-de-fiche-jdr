from tkinter import *


Main = Tk()
Main.title("Bienvenue")



label = Label(Main,text="bienvenue\naventurier",padx=100,pady=100)
label.pack()

menubar=Menu(Main)
menu=Menu(menubar, tearoff=0)

menu.add_command(label="créer une fiche",command=fiche.creation)
menu.add_command(label="modifier une fiche",command=fiche.edition)
menu.add_command(label="afficher une fiche",command=fiche.affiche)

menubar.add_cascade(label="fiche",menu=Menu_fiche)



Main.config(menu=menubar)


Main.mainloop()