from mecanisme import *
from partie_humaine import transforme
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
    """rend en argument un nom de fichier nom_fichier et qui crée
et renvoie un dictionnaire dont les clés sont les lettres majuscules et les valeurs correspondantes sont le
nombre de fois où la clé apparaît dans le fichier.""" 
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
    """ prend en argument un dictionnaire dico dont les clés
sont des lettres majuscules et les valeurs des entiers (comme celui obtenu avec la fonction précédente).
La fonction renvoie la lettre (c’est-à-dire, la clé) qui est associée au plus grand entier dans le diction-
naire (correspond ici à la lettre la plus fréquente). """
    maxi=None
    cle=None
    for lettre in dico:
        if maxi is None:
            maxi=dico[lettre]
            cle=lettre
        elif maxi<=dico[lettre]:
            maxi=dico[lettre]
            cle=lettre
    return cle


def fabrique_liste_freq(nom_fichier):
    """ prend en argument un nom de fichier nom_fichier et qui
renvoie la liste des lettres majuscules, de la plus fréquente à la moins fréquente dans le fichier nom_fichier """
    dico_copie=dict(dico_frequence(nom_fichier))
    liste_freq=[]
    for i in range(len(dico_copie)):
        lettre=lettre_la_plus_frequente(dico_copie)
        liste_freq.append(lettre)
        del(dico_copie[lettre])
    return liste_freq

def partie_auto(mot_myst,liste_lettre,affichage=True,pause=False):
    """prend en argument un mot mystere une liste de lettre et deux option, d affichage et de pause et qui renvoie le nombre d'erreur faite part l ordinateur avant de trouver le resultat"""
    i=0
    erreur=0
    deja_dit=[]
    mot_trouvee=initialiser_mot_part_decouv(mot_myst)
    mot=transforme(mot_trouvee)
    while mot!=mot_myst and i<26:
        deja_dit.append(liste_lettre[i])
        if not decouvrir_lettre(liste_lettre[i],mot_myst,mot_trouvee):
            erreur+=1
        if affichage:
            if pause:
                input("\n Tapez sur entrée pour continuer")
            print("\n le mot à découvrir est: ",mot)
            if i>0:
                print("\n L'ordinateur a deja fait : ",erreur,"erreurs")
            elif i==0:
                print("L'ordinateur n'a pas fait d'erreurs.")
            print("L'ordinateur a déjà proposé :" , deja_dit)
        mot=transforme(mot_trouvee)
        i+=1
    print("le mot mystere était: ",mot_myst)
    return erreur
