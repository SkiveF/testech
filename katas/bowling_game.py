class BowlingGame:
    """Bowling game """
    def __init__(self):
        self.rolls = []
    
    def roll(self, pins):
        self.rolls.append(pins)
    
    def score(self):
        score_total = 0
        roll_index = 0
        
        for frame in range(10):
            if self.is_strike(roll_index):
                score_total += 10 + self.strike_bonus(roll_index)
                roll_index += 1
            elif self.is_spare(roll_index):
                score_total += 10 + self.strike_bonus(roll_index)
                roll_index += 2
            else:
                score_total += self.frame_score(roll_index)
                roll_index += 2
        
        return score_total
    
    def is_strike(self, roll_index):
        return self.rolls[roll_index] == 10
    
    def is_spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10
    
    def strike_bonus(self, roll_index):
        return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]
    
    def spare_bonus(self, roll_index):
        return self.rolls[roll_index + 2]
    
    def frame_score(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1]


if __name__ == '__main__':
    game = BowlingGame()
    game.roll(1)
    game.roll(4)
    game.roll(4)
    game.roll(5)
    game.roll(6)
    game.roll(4)
    game.roll(5)
    game.roll(5)
    game.roll(10)  # Strike
    game.roll(0)
    game.roll(1)
    game.roll(7)
    game.roll(3)  # Spare
    game.roll(6)
    game.roll(4)  # Spare
    game.roll(10)  # Strike
    game.roll(2)
    game.roll(8)  # Spare
    game.roll(6)
    print('le score final :', game.score())
