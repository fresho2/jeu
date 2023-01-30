from mecanisme import *
import random 
def fabrique_liste_alphabet() :
    """la fonction n'a pas d'argument et renvoie une liste de lettre majuscule dans l'ordre alphabetique"""
    l=[chr(i+65) for i in range(26)] #creation d'une liste de charactere en comprehension
    return l

def fabrique_liste_alea():
    """la fonction n'a pas d'argument et renvoie une liste d'alphabet en majuscule ordonnée de maniere aleatoire"""
    a=list(fabrique_liste_alphabet())
    random.shuffle(a)
    return a

def nb_occurence(mot,lettre):
    """Prend en argument une chaine de caratere et une lettre et un caractere et renvoie le nombre d'occurence de cette lettre dans le mot"""    
    occ=0
    for i in mot:
        if i == lettre:
            occ+=1
    return occ

def dico_frequence(nom_fichier):
    d={}
    occurence=0
    f=open(nom_fichier)
    fichier_txt=f.read()
    for lettre in fabrique_liste_alphabet() :
        occurence=nb_occurence(fichier_txt.upper(),lettre)
        if occurence>=1:
            d[lettre]=occurence
    return d
    f.close()

print(dico_frequence('mots2.txt'))

            
