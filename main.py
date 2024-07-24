# main program
import numpy as np

class Game:
    def __init__(self):
        self.num_cols = 7
        self.num_rows = 6
        self.board = np.zeros((self.num_rows, self.num_cols))

        self.turns = 0
        self.player = 1 # player 1 ==1, player 2 == -1

    def move(self, column):
        # place piece in given column
        for i in range(self.num_rows - 1, -1, -1):
            if self.board[i][column] == 0:
                self.board[i][column] = self.player
                self.turns += 1
                return True
        return False

    def update_player(self):
        self.player *= -1

    def check_win(self, lastCol):
        # lastCol is the last move made
        if self.turns < 7:  # need at least 4 pieces for first player
            return False

        # check if four in a row is obtained
        # find row of last move
        row = -10
        for i in range(self.num_rows):
            if self.board[i][lastCol] != 0:
                row = i
                break
        if row < 0: # something went wrong
            return False
        goal = self.board[row][lastCol]
        if row <= 2: # check vertically down
            if self.board[row+1][lastCol] == goal and \
                    self.board[row+2][lastCol] == goal and \
                    self.board[row+3][lastCol] == goal:
                return True

        # check horizontal
        for i in range(lastCol - 3, lastCol + 3):
            if i < 0 or i >= self.num_cols - 3:
                # because algorithm is checking left to right,
                # dont need to check positions 4,5,6 since it would be covered in checks of 0,1,2,3
                continue
            if self.board[row][i] == goal and \
                    self.board[row][i + 1] == goal and \
                    self.board[row][i + 2] == goal and \
                    self.board[row][i + 3] == goal:
                return True

        # check diagonal
        for i in range(3, -4, -1):
            coli = lastCol - i
            rowu = row + i # up diagonal from left to right
            rowd = row - i # down diagonal
            if coli < 0 or coli >= self.num_cols - 3:
                continue
            if rowu > 2 and rowu < self.num_rows: # check at a low enough row for 4 up to be possible
                if self.board[rowu][coli] == goal and \
                        self.board[rowu - 1][coli + 1] == goal and \
                        self.board[rowu - 2][coli + 2] == goal and \
                        self.board[rowu - 3][coli + 3] == goal:
                    return True
            if rowd >= 0 and rowd < self.num_rows - 3:
                if self.board[rowd][coli] == goal and \
                        self.board[rowd + 1][coli + 1] == goal and \
                        self.board[rowd + 2][coli + 2] == goal and \
                        self.board[rowd + 3][coli + 3] == goal:
                    return True

        return False

    # print the current game state in a readable format
    def print_board(self):
        for i in range(self.num_rows):
            print(self.board[i])

def bot_move(board):
    # algorithm to make a move (hopefully a good one)
    pass

def askMove():
    move = input("enter a column:\n")  # meant to check valid, but im going to skip
    return move

def main():
    game = Game()
    game.print_board() # empty board
    while True:
        # ask move for player X
        move = int(askMove())
        if not game.move(move):
            print("try again")
            continue

        game.print_board()  # after move

        if game.check_win(move): # check win given last move
            print("game over player: " + str(game.player) + " wins the game.")
            break
        game.update_player()


main()