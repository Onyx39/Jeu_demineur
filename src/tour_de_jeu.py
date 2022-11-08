from creer_plateau import lancer_le_jeu
from affichage_plateau import affichage_jeu

def demarrage() :
    plateau, mines = lancer_le_jeu()
    affichage_jeu(plateau)
    print("Vous avez", len(mines), "mines à trouver\nBonne chance !\n")
    tour_de_jeu(plateau, mines)
    return 0

def tour_de_jeu (plateau, mines) :
    choix = input ("Souhaitez-vous dévoiler une case (0), poser un drapeau (1) ou retirer un drapeau (2) ? ")
    if choix == "0" :
        devoiler (plateau, mines)
    elif choix == "1" :
        poser_un_drapeau (plateau, mines)
    elif choix == "2" :
        retirer_un_drapeau (plateau, mines)
    else : 
        print("\nLa valeur que vous avez rentré est incorrecte\n")
        tour_de_jeu(plateau, mines)

def devoiler(plateau, mines, lig = '', col = '') :
    if lig == '' and col == '' :
        entree = input("\nEntrer les coordonnées d'une case (colonne/ligne)\nUne lettre et un nombre sont attendus\n")
        try :
            lig = int(entree[1:])
            col = correspondance(entree[0])
        except ValueError:
            print("\nVous n'avez pas respecté les consignes, recommencez")
            devoiler(plateau, mines)
    if not test_case(lig, col, plateau) :
        print("\nLa case que vous avez rentré est incorrecte\n")
        tour_de_jeu(plateau, mines)
    if plateau[lig][col] == '#' :
        print("\nVous avez placé un drapeau sur cette case, vous ne pouvez pas la dévoiler\n")
        tour_de_jeu(plateau, mines)
    if est_mine (lig, col, mines) :
        print('\nVous avez marché sur une mine, vous avez perdu\n', mines, '\n')
        fin_de_partie()
    else : 
        plateau[lig][col] = calcul_nombre(lig, col, mines)
        """
        if plateau[lig][col] == ' ' :
            devoiler_autour(lig, col, plateau, mines)
        """
        affichage_jeu(plateau)
        if test_fin_de_partie(plateau, mines) :
            print('Vous avez gagné ! Bravo !\n')
            fin_de_partie()
        else : 
            tour_de_jeu(plateau, mines)
    
def poser_un_drapeau (plateau, mines) :
    entree = input("\nEntrer les coordonnées d'une case (colonne/ligne)\nUne lettre et un nombre sont attendus\n")
    try :
        lig = int(entree[1:])
        col = correspondance(entree[0])
    except ValueError:
        print("\nVous n'avez pas respecté les consignes, recommencez")
        devoiler(plateau, mines)
    if not test_case(lig, col, plateau) :
        print("\nLa case que vous avez rentré est incorrecte\n")
        tour_de_jeu(plateau, mines)
    if plateau[lig][col] == ['X'] or plateau[lig][col] == 'X':
        plateau[lig][col] = "#"
        affichage_jeu(plateau)
        tour_de_jeu(plateau, mines)
    elif plateau[lig][col] == '#' or plateau[lig][col] == ['#']: 
        print("Vous avez déjà posé un drapeau ici\n")
        tour_de_jeu(plateau, mines)
    else : 
        print("Vous ne pouvez pas poser de drapeau ici\n")
        tour_de_jeu(plateau, mines)
    
def retirer_un_drapeau (plateau, mines) :
    entree = input("\nEntrer les coordonnées d'une case (colonne/ligne)\nUne lettre et un nombre sont attendus\n")
    try :
        lig = int(entree[1:])
        col = correspondance(entree[0])
    except ValueError:
        print("\nVous n'avez pas respecté les consignes, recommencez")
        devoiler(plateau, mines)
    if not test_case(lig, col, plateau) :
        print("\nLa case que vous avez rentrée est incorrecte\n")
        tour_de_jeu(plateau, mines)
    if plateau[lig][col] == "#" or plateau[lig][col] == ['#'] :
        plateau[lig][col] = "X"
        affichage_jeu(plateau)
        tour_de_jeu(plateau, mines)
    else :
        print("\nVous ne pouvez pas retirer de drapeau ici (car vous êtes médiocre)\n")

def test_fin_de_partie (plateau, mines) :
    for i in range (len(plateau)) :
        for j in range (len(plateau)) :
            if [i, j] not in mines and (plateau[i][j] == 'X' or plateau[i][j] == ['X']) :
                return False
    for i in range (len(plateau)) :
        for j in range (len(plateau)) :
            if [i, j] in mines and (plateau[i][j] == 'X' or plateau[i][j] == ['X']) :
                plateau[i][j] = "#"
    affichage_jeu(plateau)
    return True

def correspondance (str) :
    str = str.upper()
    l = [["A", 0], ["B", 1], ["C", 2], ["D", 3], ["E", 4], ["F", 5], ["G", 6], ["H", 7], ["I", 8], ["J", 9], ["K", 10], ["L", 11], ["M", 12], ["N", 13], ["O", 14], ["P", 15], ["Q", 16], ["R", 17], ["S", 18], ["T", 19]]
    for i in l :
        if i[0] == str :
            return i[1]
    return "Aucune correpondance trouvée"

def test_case (lig, col, plateau) :
    if col >= len(plateau) or lig >= len(plateau) :
        return False
    return True

def calcul_nombre (lig, col, mines) :
    compteur = 0
    for i in range (lig - 1, lig + 2) :
        for j in range (col - 1, col + 2) :
            if [i, j] in mines :
                compteur += 1
    if compteur != 0 :
        return str(compteur)
    else : return ' '

def est_mine (lig, col, mines) :
    if [lig, col] in mines :
        return True
    return False

def fin_de_partie () :
    print("Merci d'avoir joué\nCe jeu vous a été proposé par Valentin Richard\nN'hésitez pas à faire des retours ou à rejouer\n\nA la prochaine fois :)\n")
    exit()


def devoiler_autour (lig, col, plateau, mines) :
    #boucle comme calcul et devoiler toutes les cases.
    #Il faut regler le problème des bords
    for i in range (max(0, (lig - 1)), min(len(plateau) + 1, lig + 2)) :
        for j in range (max(0, col - 1), min(len(plateau), col + 2)) :
            try :
                devoiler(plateau, mines, i, j)
            except ValueError :
                pass
    return 0