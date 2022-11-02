from affichage_plateau import affichage_jeu
import random as rd

def lancer_le_jeu () :
    print("\n\nBienvenue dans le jeu du démineur\nCe programme a été implémenté par Valentin Richard\nBon jeu !")
    n = (input("\nDéfinissez la taille de plateau \n(Un entier inférieur ou égal à 21 est demandé)\n"))
    try :
        n = int(n)
    except ValueError:
        print("\nVous n'avez pas rentré un entier\nVeuillez recommencer\n")
        exit()
    if n < 0 or n > 20 :
        print("\nL'entier ne rentre pas dans le domaine demandé\nVeuillez recommencer\n")
        exit()
    

    plateau = []
    for i in range (n) :
        ligne = []
        for j in range (n) :
            ligne.append(["X"])
        plateau.append(ligne)

    #affichage_jeu (plateau)
    mines = creer_liste_mines (plateau)
    #print(mines)
    #print(len(mines))
    return plateau, mines


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