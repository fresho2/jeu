#ce fichier contient le déroulement de la partie humaine

def demander_proposition(deja_dit):
    """ renvoie une lettre saisie par l'utilisateur """
    mot=input("Saisissez une lettre:")
    while (mot.upper()<"A" or mot.upper()>"Z") or len(mot)!=1 or (mot.upper() in deja_dit):
        mot=input("Saisissez une lettre:")
    return mot.upper()
