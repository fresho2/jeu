from mecanisme import *

def fabrique_liste_alphabet() :
    """la fonction n'a pas d'argument et renvoie une liste de lettre majuscule dans l'ordre alphabetique"""
    l=[chr(i+65) for i in range(26)] #creation d'une liste de charactere en comprehension
    return l
print(fabrique_liste_alphabet())
