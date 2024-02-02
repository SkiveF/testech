def is_valid_sudoku(board):
    # Check rows
    for row in board:
        if not is_valid_unit(row):
            return False
    
    # Check columns
    for col in zip(*board):
        if not is_valid_unit(col):
            return False
    
    # Check 3x3 subgrids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [board[x][y] for x in range(i, i + 3) for y in
                       range(j, j + 3)]
            if not is_valid_unit(subgrid):
                return False
    
    return True


def is_valid_unit(unit):
    seen = set()
    for num in unit:
        if num != ".":
            if num in seen:
                return False
            seen.add(num)
    return True


if __name__=='__main__':
    sudoku_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    # Check if the Sudoku board is valid
    result = is_valid_sudoku(sudoku_board)
    print(result)