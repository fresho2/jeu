#ceci est le fichier principal

from mecanisme import *
from partie_humaine import *
from partie_automatique import *


#choix du mot
l=importer_mots("mots2.txt")
mot=choisir_mot_alea(l)

#voici le menu qui sera afficher 
print("Menu, veuillez choisir:")
print("_______________________")
print("1. Partie humaine (vous essayerez de deviner vous même le mot)")
print("2. Partie automatique (l'ordinateur joue à votre place)")
print("Q. Quitter ")
print("_______________________")
rep=input("")
while rep not in "12Q":
    rep=input("Choix invalide, recommencez :")

while rep != "Q":
    if rep =="1":
        nb_erreur_max=int(input("definissez votre nombre maximum d'erreur: "))
        defaut=input("Voulez vous une partie par défaut? (Oui[O]/Non[N])")
        if defaut.upper() == 'N' or defaut.upper() == 'NON':
            car_subst=input("Entrez un caractere de substitution : ")
            partie_humain(mot,nb_erreur_max,car_subst)
        elif defaut.upper() == 'O' or defaut.upper() == 'OUI':
            partie_humain(mot,nb_erreur_max)
        while defaut.upper() != 'O' or defaut.upper() != 'OUI' or defaut.upper() != 'N' or defaut.upper() != 'NON':
            defaut=input("Choix invalide, recommencez (Oui[O]/Non[N]): ")
    else:
        print("Veuillez choisir une stratégie:")
        print("_______________________")
        print("1. L’ordinateur va les lettres dans l'ordre aphabétique.")
        print("2. L’ordinateur va choisir au hasard une lettre.")
        print("3. L’ordinateur va choisir en fonction de la fréquence des différentes lettres dans le fichier de mots.")
        strategie=input(" ")
        while strategie not in "123":
            strategie=input("Choix invalide, recommencez :")
        if strategie == "1":
            partie_auto(mot,fabrique_liste_alphabet(),affichage=True,pause=False)
        elif strategie == "2":
            partie_auto(mot,fabrique_liste_alea(),affichage=True,pause=False)
        else:
            dico_lettre=dico_frequence("mots2.txt")
            partie_auto(mot,lettre_la_plus_frequente(dico_lettre),affichage=True,pause=False)
    
            
    print("Menu, veuillez choisir:")
    print("_______________________")
    print("1. Partie humaine (vous essayerez de deviner vous même le mot)")
    print("2. Partie automatique (l'ordinateur joue à votre place)")
    print("Q. Quitter ")
    print("_______________________")
    rep=input("")
                
    while rep not in "12":
        rep=input("Choix invalide, recommencez :")
print("Au revoir")









#if __name__=="__main__":
    #programme principal
    #l=importer_mots("mots2.txt")
    #mot=choisir_mot_alea(l)
    #l2=initialiser_mot_part_decouv(mot)
    #l3=fabrique_liste_alphabet()
    #print(partie_auto(mot,l3,affichage=True,pause=True))
     
    #print(l)
    #print(mot)
    #print(l2)
    #print(decouvrir_lettre("O",mot,l2))
    #partie_humain(mot, 5)
    #print(partie_humaine_alea("mots.txt",8))


    #afficher_potence_texte(0,8)
    #afficher_potence_texte(1,8)
    #afficher_potence_texte(2,8)
    #afficher_potence_texte(3,8)
    #afficher_potence_texte(4,8)
    #afficher_potence_texte(5,8)
    #afficher_potence_texte(6,8)
    #afficher_potence_texte(7,8)
    #afficher_potence_texte(8,8)
    #l=["M"]
    #print(demander_proposition(l))
