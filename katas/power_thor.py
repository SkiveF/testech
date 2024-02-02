import sys


def power_of_thor(light_x, light_y, initial_tx, initial_ty):
    movements = []
    
    if initial_ty > light_y:
        movements.append("N")
        initial_ty -= 1
    elif initial_ty < light_y:
        movements.append("S")
        initial_ty += 1
    
    if initial_tx > light_x:
        movements.append("W")
        initial_tx -= 1
    elif initial_tx < light_x:
        movements.append("E")
        initial_tx += 1
    
    return "".join(movements)


if __name__ == '__main__':
    # Read initial values
    light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
    
    # Game loop
    while True:
        remaining_turns = int(
            input())  # The remaining amount of turns Thor can move. Do not remove this line.
        
        # Call the power_of_thor function and print the result
        print(power_of_thor(light_x, light_y, initial_tx, initial_ty),
              flush=True)
