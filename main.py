#ceci est le fichier principal

from mecanisme import *


#deroulement d'une partie joué par l'humain
def transforme(liste):
    """transforme une liste contenant des lettre en un mot """
    mot=""
    for i in liste:
            mot+=i
    return mot 
    
def partie_humain(mot_myst,nb_erreur_max,car_subst="-"):
    """ cette fonction permet au joueur de jouer une partie de pendu.
        Elle renvoie un booleen pour verifier si la partie est gagnée ou pas."""
    nb_erreur=0 #initialise le nombre d'erreur à 0
    mot_part_decouv=initialiser_mot_part_decouv(mot_myst,car_subst) #variable contenant le mot partiellement decouvert
    deja_dit=[] #liste des lettre déjà dite
    gagne=False
    mot=transforme(mot_part_decouv)
    while not gagne and nb_erreur<nb_erreur_max :
        print("le mot mystère est:",mot)
        lettre=input("Votre proposition: ") #demande a l'utilisateur de saisir une lettre
        if not decouvrir_lettre(lettre,mot_myst,mot_part_decouv) and (lettre not in deja_dit):
            nb_erreur+=1
        if (lettre not in deja_dit): #ajoute une lettre a la liste de mot deja dit si celle ci n'a pas encore été dite
            deja_dit.append(lettre)
        if decouvrir_lettre(lettre,mot_myst,mot_part_decouv):#utilise le bouleen retourné et modifie la liste mot_part_decouv
            print("Lettre présente") #affiche lettre presente si la lettre fait partie du mot mystere
        else:
            print("vous avez déjà fait:",nb_erreur,"erreur(s)")
        if (nb_erreur>=1):  #verifie si le nombre d'erreur est superieur ou egale a un et affiche la potence si c'est le cas
            afficher_potence_texte(nb_erreur,nb_erreur_max)
        print("Vous avez déjà proposé: ",deja_dit,"\n")
        mot=transforme(mot_part_decouv)
        if (mot==mot_myst):
            gagne=True
        else:
            gagne=False
        
    if not gagne:
        print("le mot mistère était",mot)
    return gagne





if __name__=="__main__":
    #programme principal
    l=importer_mots("mots2.txt")
    mot=choisir_mot_alea(l)
    l2=initialiser_mot_part_decouv(mot)
    #print(l)
    #print(mot)
    #print(l2)
    #print(decouvrir_lettre("O",mot,l2))
    partie_humain(mot, 5)
    


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
