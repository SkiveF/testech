def prochain_bloc_a_deplacer(width, height, nb_blocs, grid):
    # Votre logique pour déterminer le prochain bloc à déplacer ici
    # ...
    
    # Exemple simple : déplacer les blocs de gauche à droite, de haut en bas
    for ligne in range(height):
        for colonne in range(width):
            if grid[ligne][colonne] == nb_blocs:
                # Bloc actuel trouvé, déplacez-vous vers le suivant
                if colonne < width - 1:
                    return grid[ligne][colonne + 1]
                elif ligne < height - 1:
                    return grid[ligne + 1][0]
    
    # Aucun bloc trouvé (ou bloc situé en bas à droite), retourne le premier
    # bloc
    return grid[0][0]


if __name__ == '__main__':
    largeur = 3
    hauteur = 3
    nombre_blocs = 9
    grille_puzzle = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    prochain = prochain_bloc_a_deplacer(largeur, hauteur, nombre_blocs,
                                        grille_puzzle)
    print(f"Prochain bloc à déplacer : {prochain}")
