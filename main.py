# main program

class Game:
    def __init__(self):
        self.num_cols = 7
        self.num_rows = 6
        self.board = [] # array 7x6 or something

        self.turns = 0 # counts num of turns, if % 2 ==0 -> player 1, else player 2

    def move(self, column):
        # place piece in given column

        # check col not full
        # change next turn is valid move
        pass

    def check_win(self):
        # check if four in a row is obtained
        pass


def main():
    game = Game()
    while True:
        # ask move for player X
        move = input("enter a column")
        game.move(move)
        game.check_win()

main()