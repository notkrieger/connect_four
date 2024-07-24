# main program
import numpy as np
import pygame
import math
from alphaFour import NN
from game import Game

from bot import Bot

def draw_screen(height, width, game, screen):
    white = (255,255,255)
    black = (0,0,0)
    ydif = 0
    xdif = 0
    for i in np.linspace(0, height, game.num_rows + 1):
        if i == 0:
            ydif = np.linspace(0, height, game.num_rows + 1)[1] - \
                   np.linspace(0, height, game.num_rows + 1)[0]
        pygame.draw.line(screen, black, (0, i), (width, i))
    for i in np.linspace(0, width, game.num_cols + 1):
        if i == 0:
            xdif = np.linspace(0, width, game.num_cols + 1)[1] - \
                   np.linspace(0, width, game.num_cols + 1)[0]
        pygame.draw.line(screen, black, (i, 0), (i, height))
    for i in range(game.num_rows):
        for j in range(game.num_cols):
            pygame.draw.circle(screen, white, ((j + 1 / 2) * xdif, (i + 1 / 2) * ydif), 1 / 3 * min(xdif, ydif))
    return xdif, ydif

pygame.init()

def run_game():
    width = 720
    height = 540
    screen = pygame.display.set_mode((width, height))  # open pygame window
    red = (255, 0 ,0)
    blue = (86, 176, 228)
    yellow = (255, 255, 0)

    game = Game() # initialise game

    # draw initial board
    screen.fill(blue)
    xdif, ydif = draw_screen(height, width, game, screen)
    pygame.display.flip()

    bot = Bot(game, -1)

    while True:
        lastMove = -1
        # bot move
        if game.turns % 2 == 1:
            bot_move = bot.make_move()
            if game.move(bot_move):
                game.update_player()
                lastMove = bot_move
                row = -10
                for i in range(game.num_rows):
                    if game.board[i][bot_move] != 0:
                        row = i
                        break
                pygame.draw.circle(screen, yellow, ((bot_move + 1 / 2) * xdif,
                                                (row + 1 / 2) * ydif), 1 / 3 * min(xdif, ydif))
                pygame.display.flip()
        # human move
        else:
            event = pygame.event.poll()
            # ask move for player X
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # check for left click
                x, y = pygame.mouse.get_pos()
                move = math.floor(x / width * game.num_cols)
            elif event.type == pygame.KEYDOWN:
                move = event.key - 48
                if move < 0 or move >= game.num_cols:
                    print("please try again")
                    continue
            else:
                continue
            if game.move(move):
                lastMove = move
                game.update_player()
                row = -10
                for i in range(game.num_rows):
                    if game.board[i][move] != 0:
                        row = i
                        break
                pygame.draw.circle(screen, red, ((move + 1 / 2) * xdif,
                                                (row + 1 / 2) * ydif), 1/3*min(xdif, ydif))
                pygame.display.flip()
            else:
                print("please try again")
        #
        if lastMove != -1:
            pass
        # cehck for win
        if game.check_win(lastMove):  # check win given last move
            winner = ""
            if game.player*-1 == 1:
                winner = "YOU"
            else:
                winner = "the bot"
            print("game over. " + winner + " wins the game.")
            break


def main():
    run_game()

main()