from creer_plateau import lancer_le_jeu, fin_de_partie
from affichage_plateau import affichage_jeu

def demarrage() :
    plateau, mines = lancer_le_jeu()
    affichage_jeu(plateau)
    if len(mines) == 1 :
        print("Vous avez 1 mine à trouver\nBonne chance !\n")
    else : print("Vous avez", len(mines), "mines à trouver\nBonne chance !\n")
    tour_de_jeu(plateau, mines)
    return 0

def tour_de_jeu (plateau, mines) :
    choix = input ("Souhaitez-vous dévoiler une case (0), poser un drapeau (1) ou retirer un drapeau (2) ? ")
    test_fin_de_programme(choix)
    if choix == "0" :
        devoiler (plateau, mines)
    elif choix == "1" :
        if test_nombre_mines_restantes(plateau, mines) == 0 :
            print("\nVous avez placé toutes les mines, nous ne pouvez pas en poser plus\n")
            tour_de_jeu(plateau, mines)
        poser_un_drapeau (plateau, mines)
    elif choix == "2" :
        if test_nombre_mines_restantes(plateau, mines) == len(mines) :
            print("\nVous n'avez placé aucun drapeau\n")
            tour_de_jeu(plateau, mines)
        retirer_un_drapeau (plateau, mines)
    else : 
        print("\nLa valeur que vous avez rentré est incorrecte\n")
        tour_de_jeu(plateau, mines)

def devoiler(plateau, mines, lig = '', col = '') :
    if lig == '' and col == '' :
        entree = input("\nEntrer les coordonnées d'une case (colonne/ligne)\nUne lettre et un nombre sont attendus. Entrer 'retour' pour revenir au menu précédent\n")
        test_fin_de_programme(entree)
        test_retour(entree, plateau, mines)
        try :
            lig = int(entree[1:])
            col = correspondance(entree[0])
        except ValueError:
            print("\nVous n'avez pas respecté les consignes, recommencez")
            devoiler(plateau, mines)
    if not test_case(lig, col, plateau) :
        print("\nLa case que vous avez rentré est incorrecte\n")
        devoiler(plateau, mines)
    if plateau[lig][col] == '#' :
        print("\nVous avez placé un drapeau sur cette case, vous ne pouvez pas la dévoiler\n")
        devoiler(plateau, mines)
    if est_mine (lig, col, mines) :
        for i in range (len(plateau)) :
            for j in range (len(plateau)) :
                if [i, j] in mines and (plateau[i][j] == 'x' or plateau[i][j] == ['x']) :
                    plateau[i][j] = "#"
        affichage_jeu(plateau)
        print('\nVous avez marché sur une mine, vous avez perdu\n')
        fin_de_partie()
    else : 
        plateau[lig][col] = calcul_nombre(lig, col, mines)
        if plateau[lig][col] == ' ' :
            devoiler_autour(lig, col, plateau, mines)
        affichage_jeu(plateau)
        if test_fin_de_partie(plateau, mines) :
            print('Vous avez gagné ! Bravo !\n')
            fin_de_partie()
        else : 
            tour_de_jeu(plateau, mines)
    
def poser_un_drapeau (plateau, mines) :
    entree = input("\nEntrer les coordonnées d'une case (colonne/ligne)\nUne lettre et un nombre sont attendus. Entrer 'retour' pour revenir au menu précédent\n")
    test_fin_de_programme(entree)
    test_retour(entree, plateau, mines)
    try :
        lig = int(entree[1:])
        col = correspondance(entree[0])
    except ValueError:
        print("\nVous n'avez pas respecté les consignes, recommencez")
        poser_un_drapeau(plateau, mines)
    if not test_case(lig, col, plateau) :
        print("\nLa case que vous avez rentré est incorrecte\n")
        poser_un_drapeau(plateau, mines)
    if plateau[lig][col] == ['x'] or plateau[lig][col] == 'x':
        plateau[lig][col] = "#"
        affichage_jeu(plateau)
        affichage_nombre_mines_restantes(plateau, mines)
        tour_de_jeu(plateau, mines)
    elif plateau[lig][col] == '#' or plateau[lig][col] == ['#']: 
        print("Vous avez déjà posé un drapeau ici\n")
        tour_de_jeu(plateau, mines)
    else : 
        print("Vous ne pouvez pas poser de drapeau ici\n")
        tour_de_jeu(plateau, mines)
    
def retirer_un_drapeau (plateau, mines) :
    entree = input("\nEntrer les coordonnées d'une case (colonne/ligne)\nUne lettre et un nombre sont attendus. Entrer 'retour' pour revenir au menu précédent\n")
    test_fin_de_programme(entree)
    test_retour(entree, plateau, mines)
    try :
        lig = int(entree[1:])
        col = correspondance(entree[0])
    except ValueError:
        print("\nVous n'avez pas respecté les consignes, recommencez")
        retirer_un_drapeau(plateau, mines)
    if not test_case(lig, col, plateau) :
        print("\nLa case que vous avez rentrée est incorrecte\n")
        retirer_un_drapeau(plateau, mines)
    if plateau[lig][col] == "#" or plateau[lig][col] == ['#'] :
        plateau[lig][col] = "x"
        affichage_jeu(plateau)
        affichage_nombre_mines_restantes(plateau, mines)
        tour_de_jeu(plateau, mines)
    else :
        print("\nVous ne pouvez pas retirer de drapeau ici\n")

def test_fin_de_partie (plateau, mines) :
    for i in range (len(plateau)) :
        for j in range (len(plateau)) :
            if [i, j] not in mines and (plateau[i][j] == 'x' or plateau[i][j] == ['x']) :
                return False
    for i in range (len(plateau)) :
        for j in range (len(plateau)) :
            if [i, j] in mines and (plateau[i][j] == 'x' or plateau[i][j] == ['x']) :
                plateau[i][j] = "#"
    affichage_jeu(plateau)
    return True

def correspondance (str) :
    str = str.upper()
    l = [["A", 0], ["B", 1], ["C", 2], ["D", 3], ["E", 4], ["F", 5], ["G", 6], ["H", 7], ["I", 8], ["J", 9], ["K", 10], ["L", 11], ["M", 12], ["N", 13], ["O", 14], ["P", 15], ["Q", 16], ["R", 17], ["S", 18], ["T", 19]]
    for i in l :
        if i[0] == str :
            return i[1]
    return False

def test_case (lig, col, plateau) :
    if col == 0 and lig < len(plateau) and lig >= 0 :
        return True
    if col >= len(plateau) or lig >= len(plateau) or col == False or col < 0 or lig < 0 :
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


def devoiler_autour (lig, col, plateau, mines) :
    liste_cases_voisines = [[lig - 1, col - 1], [lig - 1, col], [lig - 1, col + 1],
                            [lig, col - 1], [lig, col + 1],
                            [lig + 1, col - 1], [lig + 1, col], [lig + 1, col + 1]]
    liste_attente = []

    for i in liste_cases_voisines:
        if test_case(i[0], i[1], plateau) :
            if plateau[i[0]][i[1]] == ['x'] :
                liste_attente.append(i)
    devoiler_la_liste(plateau, mines, liste_attente)
    return 0

def devoiler_la_liste (plateau, mines, liste) :
    for i in liste :
        plateau[i[0]][i[1]] = calcul_nombre(i[0], i[1], mines)
        if plateau[i[0]][i[1]] == ' ' :
            devoiler_autour(i[0], i[1], plateau, mines)
    return 0

def affichage_nombre_mines_restantes (plateau, mines) :
    compteur = 0
    for i in plateau :
        for j in i :
            if j == '#' :
                compteur += 1
    mines_restantes = int(len(mines) - compteur)
    if mines_restantes < 0 :
        return False
    if mines_restantes == 0 :
        print("\nVous avez placé toutes les mines\n")
    elif mines_restantes == 1 :
        print("Il vous reste 1 mine à trouver\n")
    else : print("Il vous reste", mines_restantes, "mines à trouver\n")
    return True, mines_restantes

def test_nombre_mines_restantes (plateau, mines) :
    compteur = 0
    for i in plateau :
        for j in i :
            if j == '#' :
                compteur += 1
    return int(len(mines) - compteur)
    
def test_fin_de_programme(str) :
    if str == 'exit' :
        fin_de_partie()

def test_retour(str, plateau, mines) :
    if str == 'retour' :
        print('\n')
        tour_de_jeu(plateau, mines)
