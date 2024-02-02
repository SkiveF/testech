"""
THEY put you in a square shape room, with N meters on each side.
THEY want to know everything about you.
THEY are observing you.
THEY placed some candles in the room.

Every candle makes L "light" in the spot they are, and every spot in square
shape gets one less "light" as the next ones. If a spot is touched by two
candles, it will have the larger "light" it can have. Every spot has the base
light of 0.

You can hide only, if you find a dark spot which has 0 "light".
How many dark spots you have?

You will receive a map of the room, with the empty places (X) and Candles (C)
in N rows, each character separated by a space.

Example for the light spread N = 5, L = 3:
X X X X X
X C X X X
X X X X X
X X X X X
X X X X X

2 2 2 1 0
2 3 2 1 0
2 2 2 1 0
1 1 1 1 0
0 0 0 0 0
"""


class Candle:
    def __init__(self, pos, l):
        self.pos = pos
        self.l = l
    
    def light_room(self, pos, list_lighted_cell, l, n):
        i = pos[0]
        j = pos[1]
        
        # si on est dans les limites de la pièce.
        if 0 <= i < n and 0 <= j < n:
            
            # si la pièce n'est pas eclairée
            if list_lighted_cell[i][j].l == 0:
                list_lighted_cell[i][j].l = l
                list_lighted_cell[i][j].light_by_bouji = self
            
            # si la case est éclairée mais par une aure bougie
            elif list_lighted_cell[i][j].l > 0 and not self.same_bouji(
                    list_lighted_cell[i][j].light_by_bouji):
                list_lighted_cell[i][j].l = self.l
            
            # si la case est eclairee par la même bougie mais avec une
            # intensité plus faible
            elif list_lighted_cell[i][j].l < l and self.same_bouji(
                    list_lighted_cell[i][j].light_by_bouji):
                list_lighted_cell[i][j].l = l
            
            # eclairer une case mais avec une lumière moins
            l = l - 1
            if l > 0:
                for k in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                          (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
                          (i + 1, j + 1)]:
                    list_lighted_cell = self.light_room(k, list_lighted_cell, l,
                                                        n)
        
        return list_lighted_cell
    
    def same_bouji(self, another_bouji):
        if self.pos == another_bouji.pos:
            return True
        else:
            return False


class Cell:
    def __init__(self, pos):
        self.pos = pos
        self.l = 0
        self.light_by_bouji = None


n = int(input())
l = int(input())
list_bouji = list()
list_lighted_cell = list()
nb_dark_spot = 0

# remplissage des listes
for i in range(n):
    line_cell = list()
    line = input().split(" ")
    
    for j in range(n):
        if "C" in line[j]:
            list_bouji.append(Candle((i, j), 1))
        line_cell.append(Cell((i, j)))
    list_lighted_cell.append(line_cell)

# pour chaque bougie dans notre liste de bougies, on éclaire la zone à coté
for candle in list_bouji:
    list_lighted_cell = candle.light_room(candle.pos, list_lighted_cell, l, n)

# cell non eclairées.
for line_cell in list_lighted_cell:
    for cell in line_cell:
        if cell.l == 0:
            nb_dark_spot += 1

print(nb_dark_spot)
