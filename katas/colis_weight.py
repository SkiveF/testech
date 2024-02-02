from contextlib import redirect_stdout


def solve_colis(weight_0, weight_1, weight_2):
    # Write your code here
    colis = ((weight_0, 0), (weight_1, 1), (weight_2, 2))
    colis_tri = sorted(colis, reverse=True)
    sorted_colis = colis_tri[0][1]
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    return sorted_colis


# Ignore and do not change the code below
def main():
    # pylint: disable = C, W
    
    # game loop
    while True:
        weight_0 = int(input())
        weight_1 = int(input())
        weight_2 = int(input())
        with redirect_stdout(sys.stderr):
            action = solve_colis(weight_0, weight_1, weight_2)
        print(action)


if __name__ == '__main__':
    main()
