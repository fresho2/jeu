from tkinter import *
from partie_automatique import * 
from partie_humaine import *
from menu import *
def menu_graph():
    window_menu=Tk()
    window_menu.title("Menu/Jeu du pendu") #titre de la fenetre
    window_menu.geometry("1080x720") #intialisation de la taille de la fenetre à la taille HD (1080px * 720px)
    boite_menu=Frame(window_menu)#creation d'une boite
    #texte de bienvenue
    welcome=Label(boite_menu, text="Choisissez le mode de jeu", font=("Neo Fobia",20))#composante -> texte de bienvenue
    welcome.pack()
    #bouton pour mode de jeu 
    auto_bouton= Button(boite_menu, text="Partie automatique")
    auto_bouton.pack()
    humain_bouton= Button(boite_menu, text="Partie humaine")
    humain_bouton.pack()
    #affichage centré
    boite_menu.pack(expand='YES')
    
def interface_graph():
    """ cette foncion met en place l'interface graphique et ne renvoie rien """
    window = Tk() #creer la fenetre de l'interface
    window.title("Jeu du pendu") #titre de la fenetre
    window.geometry("1080x720") #intialisation de la taille de la fenetre à la taille HD (1080px * 720px)
    boite=Frame(window)#creation d'une boite
    #texte de bienvenue
    welcome=Label(boite, text="Bienvenue dans le jeu du pendu", font=("Neo Fobia",20))#composante -> texte de bienvenue
    welcome.pack()
    #bouton pour commencer 
    bg_bouton= Button(boite, text="Commencer une partie", command=menu_graph)
    bg_bouton.pack()
    quitter_bouton= Button(boite, text="Quitter le jeu ", command=quit)
    quitter_bouton.pack()
    #affichage centré
    boite.pack(expand='YES')

