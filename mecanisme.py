#ceci est le fichier contenant le mecanisme du jeu 
import copy
import random




def importer_mots(nom_fichier):
    """cette fonction prend en argument un nom de fichier
        et renvoie une liste de mots contenus dans le fichier tout
        en se limitant à trois (03) lettres minimum"""
    fichier=open(nom_fichier)
    liste=[]
    for ligne in fichier:
        l=ligne.strip()#supprime les caractère comme les retours à la ligne, les espaces et divers
        if len(l)>=3:
            liste.append(l.upper())#ajoute le mot en majuscule à la liste
    return liste
    fichier.close()

def choisir_mot_alea(liste_de_mot):
    """la fonction choisir_mot_alea() choisi aleatoirement un mot dans une liste passée en argument
        grace à la fonction randint de random"""
    index=random.randint(0,len(liste_de_mot)-1)
    return liste_de_mot[index]


def initialiser_mot_part_decouv(mot_myst,car_subst="-"):
    """ cette  foncion renvoie une liste contenant le mot mystere (passeé en argument) avec les caractères substiués"""
    l=[]
    for indice in range(len(mot_myst)):
        if (indice == 0) or (indice == len(mot_myst)-1):
            l.append(mot_myst[indice])
        else:
            l.append(car_subst)
    return l


def afficher_potence_texte(nb_erreur,nb_erreur_max):
    """ la fonction afficher_potence_texte affiche la chaine de caractères carractérisant le nombre d'erreur restant """
    l_erreur=["-" for i in range(nb_erreur_max)]
    l_erreur.append("!")
    perdu="PERDU"
    potence=""
    # Ma conditon if remplace au fur et à mesure les "-"par les caractères adaptés
    # ici j'utilise [nb_erreur-1] car si le nombre d'erreur est 1 par exemple
    #il faudrait placé le "P" d'indice 0 dans "PERDU"
    for i in range(nb_erreur+1): 
        if (0<i<=5) and (perdu[i-1] not in l_erreur):
            l_erreur[i-1]=perdu[i-1] 
        elif i<=nb_erreur_max: #remplace le "-" par "!" si PERDU est totalement ecrit et que le nombre maximal d'erreur n'est pas depassé
            l_erreur[i-1]="!"
    for i in l_erreur: #créer une chaine de caractère à partir de la liste créer au dessus
        potence+=i    
    print(potence)  



    
