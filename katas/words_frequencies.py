def words_frenquecies(liste_de_mots):
    compteur = {}
    
    for mot in liste_de_mots:
        if mot in compteur:
            compteur[mot] += 1
        else:
            compteur[mot] = 1
    
    return compteur

if __name__ == '__main__':
    # Exemple d'utilisation
    liste_de_mots = ['le', 'chien', 'le', 'chat', 'le', 'chien', 'le']
    resultat = words_frenquecies(liste_de_mots)
    print(resultat)
