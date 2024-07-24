from game import Game
import numpy as np

class Board:
    def __init__(self, state):
        self.state = state
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class Tree:
    def __init__(self, game, root):
        self.game = game
        self.root = root

    # build the tree to a certain depth
    def build_tree(self, depth):
        pass



class Bot:
    def __init__(self, game, player):
        self.player = player
        self.game = game
        init_board = Board(game.board)
        self.tree = Tree(self.game, init_board)
        # maybe like create some of the tree


    def make_move(self):
        # return the column of bots move
        next_move = -1
        moves = self.game.legal_moves()
        boards = []
        for move in moves:
            board = Board(self.game.peak_board(move))
            self.tree.
            boards.append(board)

        return np.random.randint(0, 6)

    def heuristic(self, player):
        # player is player whos go it is
        # i think will be needed for mini-max to work
        # hopefully look for ways to win
        # check claim even
        pass






