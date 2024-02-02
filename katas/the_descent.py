def the_descent():
    # game loop
    while True:
        plus_haute_montagne = 0
        hauteur_plus_haute_montagne = -1
        for i in range(8):
            mountain_h = int(input())  # represents the height of one mountain.
            if i == 0 or hauteur_plus_haute_montagne < mountain_h:
                indice_plus_haute_montagne = i
                hauteur_plus_haute_montagne = mountain_h
        
        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)
        
        # The index of the mountain to fire on.
        print(indice_plus_haute_montagne)


if __name__ == '__main__':
    the_descent()
