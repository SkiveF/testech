def temperature_plus_proche_de_zero(tableau_temperature):
    if not tableau_temperature:  # Si le tableau est vide
        return None  # Ou une autre valeur par défaut que vous préférez
    
    plus_proche = tableau_temperature[
        0]  # Initialisation avec la première température
    distance_minimale = abs(
        0 - plus_proche)  # Initialisation avec la distance à zéro
    
    for temperature in tableau_temperature:
        if 0 <= temperature <= 10000:
            distance_actuelle = abs(0 - temperature)
            if distance_actuelle < distance_minimale or (
                    distance_actuelle == distance_minimale and temperature > plus_proche):
                plus_proche = temperature
                distance_minimale = distance_actuelle
    
    return plus_proche


if __name__ == '__main__':
    temperatures = [7, -4, 3, -2, 1, -1, -3, 2, -5, 6]
    plus_proche_de_zero = temperature_plus_proche_de_zero(temperatures)
    print("La température la plus proche de zéro est :", plus_proche_de_zero)
