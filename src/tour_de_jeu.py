"""
Fichier en charge du tour de jeu (gérer les drapeaux, dévoiler des cases)
"""

from creer_plateau import lancer_le_jeu, fin_de_partie
from affichage_plateau import affichage_jeu

def demarrage() :
    """"
    Fonction qui démarre la jeu

    Aucune entrée

    Auncune sortie
    """

    plateau, mines = lancer_le_jeu()
    affichage_jeu(plateau)
    if len(mines) == 1 :
        print("Vous avez 1 mine à trouver\nBonne chance !\n")
    else : print("Vous avez", len(mines), "mines à trouver\nBonne chance !\n")
    tour_de_jeu(plateau, mines)

def tour_de_jeu (plateau, mines) :
    """"
    Fonction qui permet à l'utilisateur de choisir une action

    Entrées :
        plateau (list) : représentation du plateau
        mines (list) : la liste des mines

    Aucune sortie
    """

    choix = input ("Souhaitez-vous dévoiler une case (0)," \
                   + "poser un drapeau (1) ou retirer un drapeau (2) ? ")
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
    """
    Fonction qui permet de dévoiler une case

    Entrées :
        plateau (list) : représentation du plateau
        mines (list) : la liste des mines
        lig (str, defaut ' ') : la ligne à dévoiler
        col (str, defaul ' ') : la colonne à dévoiler

    Aucune sortie
    """

    if lig == '' and col == '' :
        entree = input("\nEntrer les coordonnées d'une case (colonne/ligne)\n" \
                       + "Une lettre et un nombre sont attendus. " \
                       + "Entrer 'retour' pour revenir au menu précédent\n")
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
        for i in enumerate(plateau) :
            for j in enumerate(plateau) :
                if [i[0], j[0]] in mines and (plateau[i[0]][j[0]] == 'x' or
                                              plateau[i[0]][j[0]] == ['x']) :
                    plateau[i[0]][j[0]] = "#"
        affichage_jeu(plateau)
        print('\nVous avez marché sur une mine, vous avez perdu\n')
        fin_de_partie()
    else :
        plateau[lig][col] = calcul_nombre(lig, col, mines)
        if plateau[lig][col] == ' ' :
            devoiler_autour(lig, col, plateau, mines)
        test_devoiler_autour(lig, col, plateau, mines)
        affichage_jeu(plateau)
        if test_fin_de_partie(plateau, mines) :
            print('Vous avez gagné ! Bravo !\n')
            fin_de_partie()
        else :
            tour_de_jeu(plateau, mines)

def poser_un_drapeau (plateau, mines) :
    """
    Fonction qui permet de poser un drapeau

    Entrées :
        plateau (list) : représentation du plateau
        mines (list) : la liste des mines

    Aucune sortie
    """

    entree = input("\nEntrer les coordonnées d'une case (colonne/ligne)\n" \
                       + "Une lettre et un nombre sont attendus. " \
                       + "Entrer 'retour' pour revenir au menu précédent\n")
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
    elif plateau[lig][col] == '#' or plateau[lig][col] == ['#'] :
        print("Vous avez déjà posé un drapeau ici\n")
        tour_de_jeu(plateau, mines)
    else :
        print("Vous ne pouvez pas poser de drapeau ici\n")
        tour_de_jeu(plateau, mines)

def retirer_un_drapeau (plateau, mines) :
    """
    Fonction qui permet de retirer un drapeau

    Entrées :
        plateau (list) : représentation du plateau
        mines (list) : la liste des mines

    Aucune sortie
    """

    entree = input("\nEntrer les coordonnées d'une case (colonne/ligne)\n" \
                       + "Une lettre et un nombre sont attendus. " \
                       + "Entrer 'retour' pour revenir au menu précédent\n")
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
    """
    Fonction qui teste si la partie est terminée

    Entrées :
        plateau (list) : représentation du plateau
        mines (list) : la liste des mines

    Sortie :
        True (bool) si la partie est terminée
    """

    for i in enumerate(plateau) :
        for j in enumerate(plateau) :
            if [i[0], j[0]] not in mines and (plateau[i[0]][j[0]] == 'x' or
                                              plateau[i[0]][j[0]] == ['x']) :
                return False
    for i in enumerate(plateau) :
        for j in enumerate(plateau) :
            if [i[0], j[0]] in mines and (plateau[i[0]][j[0]] == 'x' or
                                          plateau[i[0]][j[0]] == ['x']) :
                plateau[i[0]][j[0]] = "#"
    affichage_jeu(plateau)
    return True

def correspondance (string) :
    """
    Fonction qui fait la correspondance entre une lettre et son chiffre

    Entrée :
        string (str) : la lettre dont on veut la correspondance

    Sortie :
        (int) : le chiffre associé ou False en cas d'erreur
    """

    string = string.upper()
    liste = [["A", 0], ["B", 1], ["C", 2], ["D", 3], ["E", 4],
             ["F", 5], ["G", 6], ["H", 7], ["I", 8], ["J", 9],
             ["K", 10], ["L", 11], ["M", 12], ["N", 13], ["O", 14],
             ["P", 15], ["Q", 16], ["R", 17], ["S", 18], ["T", 19]]
    for i in liste :
        if i[0] == string :
            return i[1]
    return False

def test_case (lig, col, plateau) :
    """"
    Fonction qui teste si la case entrée est valide

    Entrée :
        lig (int) : le numéro de ligne
        col (int) : le numéro de colonne
        plateau (list) : la représentation du plateau

    Sortie :
        True (bool) : si la case est valide, False sinon
    """
    if col == 0 and  0 <= lig < len(plateau) :
        return True
    if col >= len(plateau) or lig >= len(plateau) or not col or col < 0 or lig < 0 :
        return False
    return True

def calcul_nombre (lig, col, mines) :
    """
    Fonction qui calcule le nombre de mines autour d'un case donnée

    Entrée :
        lig (int) : le numéro de ligne
        col (int) : le numéro de colonne
        mines (list) : la liste des mines

    Sortie :
        str(compteur) (str) : le nombre de mines autour de la case
                              string vide si compteur = 0
    """

    compteur = 0
    for i in range (lig - 1, lig + 2) :
        for j in range (col - 1, col + 2) :
            if [i, j] in mines :
                compteur += 1
    if compteur != 0 :
        return str(compteur)

    return ' '

def est_mine (lig, col, mines) :
    """
    Fonction qui détermine si une case est minée

    Entrée :
        lig (int) : le numéro de ligne
        col (int) : le numéro de colonne
        mines (list) : la liste des mines

    Sortie :
        (bool) : True si la case est minée, False sinon
    """
    if [lig, col] in mines :
        return True
    return False

def test_devoiler_autour(lig, col, plateau, mines) :
    """
    Fonction qui créé la liste des cases à dévoiler

    Entrée :
        lig (int) : le uméro de la ligne
        col (int) : le numéro de la colonne
        plateau (list) : la représentation du plateau
        mines (list) : la liste des mines

    Aucune sortie
    """

    nb_mines = plateau[lig][col]
    if nb_mines in ["1", "2", "3", "4", "5", "6", "7", "8"] :
        liste_cases_voisines = [[lig - 1, col - 1], [lig - 1, col], [lig - 1, col + 1],
                                [lig, col - 1], [lig, col + 1],
                                [lig + 1, col - 1], [lig + 1, col], [lig + 1, col + 1]]
        compteur = 0
        for case in liste_cases_voisines :
            if test_case(case[0], case[1], plateau) :
                if plateau[case[0]][case[1]] == '#' :
                    compteur += 1
        if int(nb_mines) == compteur :
            devoiler_autour(lig, col, plateau, mines)



def devoiler_autour (lig, col, plateau, mines) :
    """
    Fonction qui créé la liste des cases à dévoiler

    Entrée :
        lig (int) : le uméro de la ligne
        col (int) : le numéro de la colonne
        plateau (list) : la représentation du plateau
        mines (list) : la liste des mines

    Aucune sortie
    """
    liste_cases_voisines = [[lig - 1, col - 1], [lig - 1, col], [lig - 1, col + 1],
                            [lig, col - 1], [lig, col + 1],
                            [lig + 1, col - 1], [lig + 1, col], [lig + 1, col + 1]]
    liste_attente = []

    for i in liste_cases_voisines:
        if test_case(i[0], i[1], plateau) :
            if plateau[i[0]][i[1]] == ['x'] :
                liste_attente.append(i)
    devoiler_la_liste(plateau, mines, liste_attente)

def devoiler_la_liste (plateau, mines, liste) :
    """
    Fonction qui dévoile toutes les cases d'une liste

    Entrées :
        plateau (list) : la représentation du plateau
        mines (list) : la liste des mines
        liste (list) : la liste des cases à dévoiler

    Aucune sortie
    """

    for i in liste :
        plateau[i[0]][i[1]] = calcul_nombre(i[0], i[1], mines)
        if plateau[i[0]][i[1]] == ' ' :
            devoiler_autour(i[0], i[1], plateau, mines)

def affichage_nombre_mines_restantes (plateau, mines) :
    """
    Fonction qui affiche le nombre de mines restantes à trouver

    Entrées :
        plateau (list) : la représentation du plateau
        mines (list) : la liste des mines

    Sortie :
        mines_restantes (int) : le nombre de mines restantes
    """

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
    return mines_restantes

def test_nombre_mines_restantes (plateau, mines) :
    """
    Fonction qui calcule le nombre de mines restantes à trouver

    Entrées :
        plateau (list) : la représentation du plateau
        mines (list) : la liste des mines

    Sortie :
        (int) : le nombre de mines restantes à trouver
    """

    compteur = 0
    for i in plateau :
        for j in i :
            if j == '#' :
                compteur += 1
    return int(len(mines) - compteur)

def test_fin_de_programme(string) :
    """
    Fonction qui teste si l'utilisateur veut arrêter la partie

    Entrée :
        string (str) : la saisie de l'utilisateur

    Aucune sortie
    """
    if string == 'exit' :
        fin_de_partie()

def test_retour(string, plateau, mines) :
    """"
    Fonction qui teste si l'utilisateur veut revenir au menu précédent

    Entrées :
        string (str) : la saisie de l'utilisateur
        plateau (list) : la représentation du plateau
        mines (list) : la liste des mines

    Aucune sortie
    """

    if string == 'retour' :
        print('\n')
        tour_de_jeu(plateau, mines)
