import logging

# Set up the logger
logging.basicConfig(level=logging.INFO)


def compute_dvd_price(num_dvd):
    """calcule prix d'un dvd"""
    dvd_price = 15
    return dvd_price * num_dvd


def compute_other_films_price(number_other_films):
    price_other_film = 20
    return price_other_film * number_other_films


def compute_price_total(basket):
    """cette fonction permet d'appliquer les réductions de 10% et 20% que
    voudrait mettre en place l'équipe de production de Back to the future sur
    la saga uniquement et les autres films qui coutent 20€.
    
    params: list des films
    Returns:
        int: elle retourne le prix des films de la saga Back to the
        futur et les autres achetés s'il y en a
    """
    
    films_back_to_the_future = [film for film in basket if
                                film.startswith("Back to the Future")]
    
    num_dvd = len(films_back_to_the_future)
    number_other_films = len(basket) - num_dvd
    
    total_price = compute_dvd_price(num_dvd)
    
    # Vérification du nombre de dvd achetés afin d'appliquer la réduction de
    # 10% ou de 20% en fonction du nombre.
    if num_dvd == 2:
        total_price *= 0.9
    elif num_dvd == 3:
        total_price *= 0.8
    
    # Ajouter les autres films après applications des réductions
    total_price += compute_other_films_price(number_other_films)
    
    return int(total_price)


if __name__ == '__main__':
    basket = [
        "Back to the Future 1",
        "Back to the Future 2",
        "Back to the Future 3",
        "la chèvre",
    ]
    total_price_films = compute_price_total(basket)
    
    logging.info("Prix total du panier : %d" % total_price_films)
