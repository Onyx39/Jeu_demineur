""""
Fichier en charge de l'afficahge du plateau dans la console
"""

def affichage_jeu (plateau) :
    """
    Fonction qui affiche l'état du plateau dans la console

    Entrée :
        plateau (list<list>) : la représentation du plateau

    Aucune sortie
    """

    abscisses = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                 "K" , "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
    compteur = 0
    print("\n")
    print("      ", end="")
    for k in range (len(plateau)) :
        print(abscisses[k], " ", end="")
    print("\n")
    for i in plateau :
        if compteur < 10 :
            print(compteur, "  | ", end="")
        else : print(compteur, " | ", end="")
        compteur += 1
        for j in i :
            print(j[0], " ", end="")
        print("|")
    print("\n")
