#ceci est mon fichier principal
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
    """ cette  foncion renvoie une liste contenant le mot mystere avec les caractères substiués"""
    l=[]
    for indice in range(len(mot_myst)):
        if (indice == 0) or (indice == len(mot_myst)-1):
            l.append(mot_myst[indice])
        else:
            l.append(car_subst)
    return l
    
        





if __name__=="__main__":
    #programme principal
    l=importer_mots("mots2.txt")
    mot=choisir_mot_alea(l)
    print(l)
    print(mot)
    print(initialiser_mot_part_decouv(mot))
    
    
