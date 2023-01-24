#ceci est mon fichier principal

from mecanisme import * 
if __name__=="__main__":
    #programme principal
    l=importer_mots("mots2.txt")
    mot=choisir_mot_alea(l)
    print(l)
    print(mot)
    print(initialiser_mot_part_decouv(mot))
    afficher_potence_texte(0,8)
    afficher_potence_texte(1,8)
    afficher_potence_texte(2,8)
    afficher_potence_texte(3,8)
    afficher_potence_texte(4,8)
    afficher_potence_texte(5,8)
    afficher_potence_texte(6,8)
    afficher_potence_texte(7,8)
    afficher_potence_texte(8,8)
    
