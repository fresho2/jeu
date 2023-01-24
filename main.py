#ceci est le fichier principal

from mecanisme import *





if __name__=="__main__":
    #programme principal
    l=importer_mots("mots2.txt")
    mot=choisir_mot_alea(l)
    l2=initialiser_mot_part_decouv(mot)
    print(l)
    print(mot)
    print(l2)
    print(decouvrir_lettre("O",mot,l2))

    


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
