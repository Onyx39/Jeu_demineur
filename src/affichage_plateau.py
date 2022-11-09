def affichage_jeu (plateau) :
    n = len(plateau)
    abscisses = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K" , "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
    compteur = 0
    print("\n")
    print("      ", end="")
    for k in range (n) :
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