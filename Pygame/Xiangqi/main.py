

import pygame
import sys

from classes.Board import Board
from classes.GameUI import GameUI










if __name__ == '__main__':
    gameUI = GameUI()
    WIDTH = gameUI.width
    HEIGHT = gameUI.height
    win = gameUI.win
    board = Board(gameUI)
    mouse_pos = None
    
    while True:
        pygame.time.delay(50) ##stops cpu dying
        WIDTH = gameUI.width
        HEIGHT = WIDTH//9*10
        
        if board.is_inCheck(board.current_turn) and board.isCheckMated():
            print("Check mate!! Red wins" if board.current_turn=='b' else 'Black wins')
            pygame.quit()
            sys.exit()
            
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            """This quits the program if the player closes the window"""
            
            if mouse_pos[0]>WIDTH or mouse_pos[1]>HEIGHT:
                board.picked_up_piece = None
                continue
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                y, x = board.Find_Node(mouse_pos, WIDTH)
                board.handle_mouse_down((x,y))
            elif event.type == pygame.MOUSEBUTTONUP:
                y,  x = board.Find_Node(mouse_pos, WIDTH)
                board.handle_mouse_up((x, y))
            elif event.type == pygame.MOUSEMOTION:
                y, x = board.Find_Node(mouse_pos, WIDTH)
                if (board.picked_up_piece 
                    or (board.on_board((x,y)) and board.config[x][y] and board.config[x][y].team==board.current_turn)):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    
        
        gameState = board.get_game_state()
        gameState.append(mouse_pos)
        gameUI.update_display(gameState, board)        

