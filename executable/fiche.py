from tkinter import *


def creation():
    
    global entry_1_1
    
    root_1=Tk()
    root_1.title("creation du personnage")
    root_1.geometry("500x200")
    
    
    text_1_1=Label(root_1,text="saisissez le nom de votre personnage")
    text_1_1.config(font=("courier","15"))
    text_1_1.pack()
    
    entry_1_1=Entry(root_1)
    entry_1_1.config(width=150,font=("courier","20"))
    entry_1_1.pack()
    
    bouton_1_1=Button(root_1,text="valider",command=creation_1)
    bouton_1_1.config(width=10,height=3,font=("courier","20"))
    bouton_1_1.pack()    
    
    root_1.mainloop()

    return



def creation_1():
    
    global box_intelligence,box_perception,box_instinct,box_force,box_charisme,box_mentir,box_sangfroid,box_dexterite,box_endurance,nom
    
    
    
    
    nom=entry_1_1.get()
    
    
    
    root_1_1=Tk()
    root_1_1.title(nom)
    
    frame_savoir=Frame(root_1_1,width=500,height=1500)
    frame_savoir.pack(side="left",padx=10,pady=10)
    
    text_savoir=Label(frame_savoir,text="Savoir",bg="white")
    text_savoir.pack(side="top",padx=10,pady=10)

    frame_intelligence=Frame(frame_savoir)
    frame_intelligence.pack(side="bottom",padx=10,pady=10)
    
    text_intelligence=Label(frame_intelligence,text="Inteligence:",anchor="w")
    text_intelligence.pack(side="left",padx=10,pady=10)
    
    box_intelligence=Spinbox(frame_intelligence,from_="0",to="5")
    box_intelligence.pack(side="right",padx=10,pady=10)

    

    frame_perception=Frame(frame_savoir)
    frame_perception.pack(side="bottom",padx=10,pady=10)
    
    text_perception=Label(frame_perception,text="Perception:",anchor="w")
    text_perception.pack(side="left",padx=10,pady=10)
    
    box_perception=Spinbox(frame_perception,from_="0",to="5")
    box_perception.pack(side="right",padx=10,pady=10)

    

    frame_instinct=Frame(frame_savoir)
    frame_instinct.pack(side="bottom",padx=10,pady=10)
    
    text_instinct=Label(frame_instinct,text="Instinct:",anchor="w")
    text_instinct.pack(side="left",padx=20,pady=10)
    
    box_instinct=Spinbox(frame_instinct,from_="0",to="5")
    box_instinct.pack(side="right",padx=10,pady=10)

    

    frame_social=Frame(root_1_1,width=500,height=1500)
    frame_social.pack(side="left",padx=10,pady=10)
    
    text_social=Label(frame_social,text="Social",bg="white")
    text_social.pack(side="top",padx=10,pady=10)
    ##frame_2_1
    
    frame_charisme=Frame(frame_social)
    frame_charisme.pack(side="bottom",padx=10,pady=10)
    
    text_charisme=Label(frame_charisme,text="Charisme:",anchor="w")
    text_charisme.pack(side="left",padx=10,pady=10)
    
    box_charisme=Spinbox(frame_charisme,from_="0",to="5")
    box_charisme.pack(side="right",padx=15,pady=10)

    

    
    frame_mentir=Frame(frame_social)
    frame_mentir.pack(side="bottom",padx=10,pady=10)
    
    text_mentir=Label(frame_mentir,text="mentir:",anchor="w")
    text_mentir.pack(side="left",padx=20,pady=10)
    
    box_mentir=Spinbox(frame_mentir,from_="0",to="5")
    box_mentir.pack(side="right",padx=10,pady=10)
    


    
    frame_sangfroid=Frame(frame_social)
    frame_sangfroid.pack(side="bottom",padx=10,pady=10)
    
    text_sangfroid=Label(frame_sangfroid,text="Sang-froid:",anchor="w")
    text_sangfroid.pack(side="left",padx=10,pady=10)
    
    box_sangfroid=Spinbox(frame_sangfroid,from_="0",to="5")
    box_sangfroid.pack(side="right",padx=10,pady=10)

    
    frame_pouvoir=Frame(root_1_1,width=500,height=1500)
    frame_pouvoir.pack(side="left",padx=10,pady=10)
    
    text_pouvoir=Label(frame_pouvoir,text="Pouvoir",bg="white")
    text_pouvoir.pack(side="top",padx=10,pady=10)

    
    frame_force=Frame(frame_pouvoir)
    frame_force.pack(side="bottom",padx=10,pady=10)
    
    text_force=Label(frame_force,text="Force:",anchor="w")
    text_force.pack(side="left",padx=22,pady=10)
    
    box_force=Spinbox(frame_force,from_="0",to="5")
    box_force.pack(side="right",padx=10,pady=10)

    
    frame_dexterite=Frame(frame_pouvoir)
    frame_dexterite.pack(side="bottom",padx=10,pady=10)
    
    text_dexterite=Label(frame_dexterite,text="Dextérité:",anchor="w")
    text_dexterite.pack(side="left",padx=14,pady=10)
    
    box_dexterite=Spinbox(frame_dexterite,from_="0",to="5")
    box_dexterite.pack(side="right",padx=10,pady=10)
    

    
    frame_endurance=Frame(frame_pouvoir)
    frame_endurance.pack(side="bottom",padx=10,pady=10)
    
    text_endurance=Label(frame_endurance,text="Endurance:",anchor="w")
    text_endurance.pack(side="left",padx=10,pady=10)
    
    box_endurance=Spinbox(frame_endurance,from_="0",to="5")
    box_endurance.pack(side="right",padx=10,pady=10)


    bouton_1_1_1=Button(root_1_1,text="valider",command=creation_2)
    bouton_1_1_1.config(width=10,height=3,font=("courier","20"))
    bouton_1_1_1.pack()
    
   
    
    root_1_1.mainloop()
    

def creation_2():
    
    charisme=str(box_charisme.get())
    dexterite=str(box_dexterite.get())
    endurance=str(box_endurance.get())
    force=str(box_force.get())
    instinct=str(box_instinct.get())
    intelligence=str(box_intelligence.get())
    mentir=str(box_mentir.get())
    perception=str(box_perception.get())
    sangfroid=str(box_sangfroid.get())
    blessure=str(0)
    
    
    
    fiche=open("../fiche/"+ nom +".txt","w+")
    
    
    fiche.write("savoir\n\nintelligence:\n"+intelligence+"\nperception:\n"+perception+"\ninstinct:\n"+instinct+"\n\nsocial\n\ncharisme:\n"+charisme+"\nmentir:\n"+mentir+"\nsang-froid:\n"+sangfroid+"\n\npouvoir\n\nforces:\n"+force+"\ndexterite:\n"+dexterite+"\nendurance\n"+endurance+"\n\nblessure:\n"+blessure)
    
    
    
    root_1_2=Tk()
    root_1_2.title(nom)

    frame_1=Frame(root_1_2,width=600,height=340,bg="yellow")
    frame_1.pack()

    canvas_savoir=Canvas(frame_1,width=200,height=340,bg="blue")
    
    text_savoir=canvas_savoir.create_text(100,10,text="Savoir")
    text_intelligence=canvas_savoir.create_text(100,95,text="Intelligence:\r\t"+(int(intelligence)*"●")+(int(5-int(intelligence))*"o"))
    text_perception=canvas_savoir.create_text(100,180,text="Perception:\r\t"+(int(perception)*"●")+int(5-int(perception))*"o")
    text_instinct=canvas_savoir.create_text(100,265,text="Instinct:\r\t"+(int(instinct)*"●")+int(5-int(instinct))*"o")


    canvas_savoir.pack(side='left')

    canvas_social=Canvas(frame_1,width=200,height=340,bg="grey")
    
    text_social=canvas_social.create_text(100,10,text="Social")
    text_charisme=canvas_social.create_text(100,95,text="Charisme:\r\t"+(int(charisme)*"●")+int(5-int(charisme))*"o")
    text_mentir=canvas_social.create_text(100,180,text="Mentir:\r\t"+(int(mentir)*"●")+int(5-int(mentir))*"o")
    text_sangfroid=canvas_social.create_text(100,265,text="Sang-froid:\r\t"+(int(sangfroid)*"●")+int(5-int(sangfroid))*"o")
    
    canvas_social.pack(side='left')
    
    canvas_pouvoir=Canvas(frame_1,width=200,height=340,bg="red")
    
    text_pouvoir=canvas_pouvoir.create_text(100,10,text="Pouvoir")
    text_force=canvas_pouvoir.create_text(100,85,text="Forces:\r\t"+(int(force)*"●")+int(5-int(force))*"o")
    text_dexterite=canvas_pouvoir.create_text(100,180,text="Dextérité:\r\t"+(int(dexterite)*"●")+int(5-int(dexterite))*"o")
    text_endurance=canvas_pouvoir.create_text(100,265,text="Endurance:\r\t"+(int(endurance)*"●")+int(5-int(endurance))*"o")

    canvas_pouvoir.pack(side='right')


    frame_2=Frame(root_1_2,width=600,height=340,bg="yellow")
    frame_2.pack()
    
    
    canvas_energie=Canvas(frame_2,width=225,height=340,bg="blue")
    text_energie=canvas_energie.create_text(112,85,text="Energie:\r\t")

    text_res_mag=canvas_energie.create_text(112,211,text="Resistance magique:\r\t")



    canvas_energie.pack(side='left')


    canvas_trophet=Canvas(frame_2,width=150,height=340,bg='black')
    
    
    canvas_trophet.pack(side="left")
    
    canvas_sante=Canvas(frame_2,width=225,height=340,bg="blue")


    text_sante=canvas_sante.create_text(112,85,text="Santé:\r\t"+ str( eval(charisme) + eval(dexterite) + eval(endurance) + eval(force) + eval(instinct) + eval(intelligence) + eval(mentir) + eval(perception) + eval(sangfroid) + 5 - eval(blessure) ))
    

    
    text_res_ph=canvas_sante.create_text(112,211,text="Resistance physique:\r\t")

    canvas_sante.pack(side='left')
    
    
    

    root_1_2.mainloop()


def edition():
    
    root_2=Tk()
    root_2.title("edition du personage")
    
    text_2_1=Label(root_2,text="a venir")
    text_2_1.config(width=15,font=("courier","20"))
    text_2_1.pack()
    
    
    root_2.mainloop()

    return


def affiche():
    global nom_1
    
    root_3=Tk()
    root_3.title("selection du personage")
    
    text_3_1=Label(root_3,text="nom du personnage")
    text_3_1.config(width=30,font=("courier","20"))
    text_3_1.pack()
    
    entry_3_1=Entry(root_3)
    entry_3_1.config(width=30,font=("courier","20"))
    entry_3_1.pack()
    
    bouton_3_1=Button(root_3,text="valider",command=affiche_1)
    bouton_3_1.config(width=15,height=3,font=("courier","20"))
    bouton_3_1.pack()
    

    return


    
def affiche_1():
    
    
    try:
        fiche=open("../system fiche/fiche/"+nom+".txt","r")
    
    except FileNotFoundError:
        erreur_nom()
    
    return

def erreur_nom():
    erreur=Tk()
    erreur.title("erreur")
    
    text=Label(erreur,text="erreur de saisi")
    text.config(width=30,font=("courier","20"))
    text.pack()

    bouton_1_1=Button(erreur,text="quiter",command=erreur.quit)
    bouton_1_1.config(width=15,height=3,font=("courier","20"))
    bouton_1_1.pack()

    erreur.mainloop()


