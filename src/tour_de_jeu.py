from creer_plateau import lancer_le_jeu
from affichage_plateau import affichage_jeu

def initialisation() :
    plateau, mines = lancer_le_jeu()
    affichage_jeu(plateau)
    print("Vous avez", len(mines), "mines à trouver\nBonne chance !\n")
    while fin_de_partie(plateau, mines) == False :
        tour_de_jeu(plateau, mines)
    return 0

def tour_de_jeu (plateau, mines) :
    choix = input ("Souhaitez-vous dévoiler une case (0), poser un drapeau (1) ou retirer un drapeau (2) ?")
    if choix == "0" :
        devoiler (plateau, mines)
    elif choix == "1" :
        poser_un_drapeau (plateau, mines)
    elif choix == "2" :
        retirer_un_drapeau (plateau, mines)
    else : 
        print("\nLa valeur que vous avez rentré est incorrecte\n")
        tour_de_jeu(plateau, mines)

def devoiler(plateau, mines) :
    print("devoiler")
    return 0
    
def poser_un_drapeau (plateau, mines) :
    print("poser")
    return 0
    
def retirer_un_drapeau (plateau, mines) :
    print("retirer")
    return 0

def fin_de_partie (plateau, mines) :
    return False