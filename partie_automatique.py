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

def lettre_la_plus_frequente(dico):
    maxi=None
    clé=0
    for i in dico:
        if maxi is None:
            maxi=dico[i]
            clé=i
        elif maxi<=dico[i]:
            maxi=dico[i]
            clé=i
    return clé

def fabrique_liste_freq(nom_fichier):
    d1=dict(dico_frequence(nom_fichier))
    l2=[]
    a=len(d1)
    b=0
    while a>=0 :
        b=lettre_la_plus_frequente(d1)
        if b not in l2:
            l2.append(b)
        a+=1
    return l2

        
    


            
