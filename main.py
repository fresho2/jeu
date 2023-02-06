#ceci est le fichier principal

from mecanisme import *
from partie_humaine import *
from partie_automatique import *




if __name__=="__main__":
    #programme principal
    l=importer_mots("mots2.txt")
    mot=choisir_mot_alea(l)
    l2=initialiser_mot_part_decouv(mot)
    l3=fabrique_liste_alphabet()
    print(partie_auto(mot,l3,affichage=True,pause=True))
     
    #print(l)
    #print(mot)
    #print(l2)
    #print(decouvrir_lettre("O",mot,l2))
    #partie_humain(mot, 5)
    #print(partie_humaine_alea("mots.txt",8))


    #afficher_potence_texte(0,8)
    #afficher_potence_texte(1,8)
    #afficher_potence_texte(2,8)
    #afficher_potence_texte(3,8)
    #afficher_potence_texte(4,8)
    #afficher_potence_texte(5,8)
    #afficher_potence_texte(6,8)
    #afficher_potence_texte(7,8)
    #afficher_potence_texte(8,8)
    #l=["M"]
    #print(demander_proposition(l))
