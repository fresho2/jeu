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

print(fabrique_liste_alea())
    
