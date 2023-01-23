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
    





if __name__=="__main__":
    #programme principal
    l=importer_mots("mots2.txt")
    print(l)
    print(choisir_mot_alea(l))
    
    
