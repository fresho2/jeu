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
            liste.append(l.upper())#ajoute le mot en majuscule
    return liste
    fichier.close()






if __name__=="__main__":
    #programme principal
    print(importer_mots("mots2.txt"))
    
