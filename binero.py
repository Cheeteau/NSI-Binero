def transpose(g):
    """Fonction qui, à l'aide d'une grille sous forme de liste contenant des listes, retourne une nouvelle grille
    pour laquelle on a inversé les colonnes et les lignes de la grille d'origine.

    Paramètre(s):
        - g list: Grille à transposer sous la forme de liste de liste. La liste parente peut être composé d'un nombre de
            listes indéfinie mais doit être identique au nombre d'éléments des listes enfants. Les éléments de la liste
            enfante peuvent être de tout type et différents les uns des autres.

    Retourne:
        - list: Résultat de la fonction pour lequel on a inversé les colonnes et les lignes du paramètre g.

    Exemples:
        >>> transpose([["1","2","3","4"],["5","6","7","8"],["9","10","11","12"],["13","14","15","16"]])
        [['1', '5', '9', '13'], ['2', '6', '10', '14'], ['3', '7', '11', '15'], ['4', '8', '12', '16']

        >>> transpose([[34, True], [[False, "25"], 0]])
        [[34, [False, '25']], [True, 0]]
    """
    resultat = [[""] * len(i) for i in g]   # Création un tableau vide contenant le même nombre d'éléments que g

    for i in range(len(g)):                 # Parcours des listes parentes de g
        for j in range(len(g)):             # Parcours des éléments de la liste g[i] (rappel: ici, len(g) == len(g[i]))
            resultat[j][i] = g[i][j]        # Remplace les valeurs vides du tableau de resultat en inversant les
                                            # positions afin d'inverser les colonnes et les lignes de la grille

    return resultat


assert transpose([["1", "2", "3", "4"], ["5", "6", "7", "8"], ["9", "10", "11", "12"], ["13", "14", "15", "16"]]) == \
                 [["1", "5", "9", "13"], ["2", "6", "10", "14"], ["3", "7", "11", "15"], ["4", "8", "12", "16"]]
assert transpose([[34, True], [[False, "25"], 0]]) == [[34, [False, '25']], [True, 0]]
