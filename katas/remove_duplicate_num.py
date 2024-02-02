def remove_duplicates(input_list):
    # Utilisez un ensemble pour éliminer les doublons
    unique_set = set(input_list)
    
    # Convertissez l'ensemble en liste (si nécessaire)
    unique_list = list(unique_set)
    
    return unique_list


if __name__ == '__main__':
    # Exemple d'utilisation de la fonction
    input_data = [1, 2, 2, 3, 4, 4, 5]
    result = remove_duplicates(input_data)
    print(result)
