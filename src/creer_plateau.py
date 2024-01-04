import random as rd

def lancer_le_jeu () :
    print("\n\nBienvenue dans le jeu du démineur\nCe programme a été implémenté par Valentin Richard\nEntrer 'exit' à n'importe quel moment pour fermer le programme\nBon jeu !")
    n = (input("\nDéfinissez la taille de plateau \n(Un entier non nul inférieur ou égal à 20 est demandé)\n"))
    if test_entrer_utilisateur(n) == int(n) :
        m = int(n)
        plateau = []
        for i in range (m) :
            ligne = []
            for j in range (m) :
                ligne.append(["x"])
            plateau.append(ligne)

        mines = creer_liste_mines (plateau)
        return plateau, mines

def test_entrer_utilisateur (n) :
    if n == 'exit' :
            fin_de_partie()
    try :
        n = int(n)
    except ValueError:
        print("\nVous n'avez pas entré un entier\nVeuillez recommencer\n")
        print("*"*40)
        lancer_le_jeu()
    print(type(n))
    print(n)
    if n <= 0 or n > 20 :
        print("\nL'entier ne rentre pas dans le domaine demandé\nVeuillez recommencer\n")
        print("*"*40)
        lancer_le_jeu()
    return int(n)


def creer_liste_mines (plateau) :
    n = len(plateau)
    m = round(0.15625*n*n)

    liste_mines = []
    for i in range (m) :
        x = rd.randint(0, n - 1)
        y = rd.randint(0, n - 1)
        if [x, y] not in liste_mines :
            liste_mines.append([x, y])
        elif [y, x] not in liste_mines :
            liste_mines.append([y, x])
        else : 
            x = rd.randint(0, n - 1)
            if [x, y] not in liste_mines :
                liste_mines.append([x, y])
    
    if len(liste_mines) == m :
        return liste_mines
    else : return creer_liste_mines(plateau)

def fin_de_partie () :
    print("\nMerci d'avoir joué\nCe jeu vous a été proposé par Valentin Richard\nN'hésitez pas à faire des retours ou à rejouer\n\nA la prochaine fois :)\n")
    exit()