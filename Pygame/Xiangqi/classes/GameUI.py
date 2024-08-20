# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 21:57:44 2023

@author: dell
"""


import pygame
from pygame import mixer
import sys
import ctypes
from classes.Board import Board


WIDTH = 900
GAP = WIDTH // 9
HEIGHT = GAP * 10


ctypes.windll.user32.SetProcessDPIAware()

WHITE = (255, 255, 255)
GREY = (128, 128, 128)
RED = (250, 0, 0, 128)
BLACK = (0, 0, 0)
ORANGE = (210, 100, 40)
PURPLE = (35, 5, 170)
YELLOW = (255, 165, 0)
GREEN = (0, 80, 10, 128)
BLUE = (10, 30, 210, 128)
SHADOW = (53, 75, 94) # '#354B5E'
river_words = ['楚河', '漢界']


class GameUI:
    def __init__(self):
        pygame.init()
        WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Xiangqi")
        self.win = WIN
        self.width = WIDTH
        self.height = HEIGHT

        mixer.init()
        self.sounds = {'move':mixer.Sound('Audios/move-self.mp3'),
                       'capture': mixer.Sound('Audios/capture.mp3'),
                       'check':  mixer.Sound('Audios/move-check.mp3'),
                       'notify':  mixer.Sound('Audios/notify.mp3')}
        self.sounds['notify'].play()
        

    def update_display(self, gameState: list, board):
        self.width = min(pygame.display.get_surface().get_width(),
                         pygame.display.get_surface().get_height()*9//10)
        gap = self.width//9
        PIECE_SIZE = gap * 0.8
        #gap = WIDTH//9
        current_turn = board.current_turn
        possible_moves, fromPos, lastPos, picked_up_piece, mouse_pos = gameState
        line_width = gap//20
        self.win.fill((153, 204, 255))
        pygame.draw.rect(self.win, SHADOW, (0.1*gap, 0.1*gap, 9.1*gap, 10.1*gap), border_radius=10)
        pygame.draw.rect(self.win, ORANGE, (0, 0, 9*gap, 10*gap))
        pygame.draw.rect(self.win, YELLOW, (0.5*gap, 0.5*gap, 8*gap, 9*gap))
        
        """
        The squares are all white so this we need to draw the grey lines that separate all the chess tiles
        from each other and that is what this function does"""
        for i in range(10):
            pygame.draw.line(self.win, BLACK, (0.5 * gap, (i+0.5) * gap),
                             (8.5 * gap, (i+0.5) * gap), width=line_width)
        for j in range(9):
            pygame.draw.line(self.win, BLACK, ((j+0.5) * gap, 0.5 * gap),
                             ((j+0.5) * gap, 4.5 * gap), width=line_width)
            pygame.draw.line(self.win, BLACK, ((j+0.5) * gap, 5.5 * gap),
                             ((j+0.5) * gap, 9.5 * gap), width=line_width)
        pygame.draw.line(self.win, BLACK, (3.5 * gap, 0.5 * gap),
                         (5.5 * gap, 2.5 * gap), width=line_width)
        pygame.draw.line(self.win, BLACK, (5.5 * gap, 0.5 * gap),
                         (3.5 * gap, 2.5 * gap), width=line_width)
        pygame.draw.line(self.win, BLACK, (3.5 * gap, 9.5 * gap),
                         (5.5 * gap, 7.5 * gap), width=line_width)
        pygame.draw.line(self.win, BLACK, (5.5 * gap, 9.5 * gap),
                         (3.5 * gap, 7.5 * gap), width=line_width)

        # dislay chess pieces
        for i in range(10):
            for j in range(9):
                if board.config[i][j] and board.config[i][j] != picked_up_piece:
                    piece_gap = (gap - PIECE_SIZE) // 2
                    # creates the shadow of a piece
                    center = ((j+0.5)*gap, (i+0.56)*gap)
                    pygame.draw.circle(self.win, SHADOW, center, PIECE_SIZE//2)
                    image = pygame.transform.scale(
                        board.config[i][j].image, (PIECE_SIZE, PIECE_SIZE))
                    self.win.blit(
                        image, (piece_gap + j*gap, piece_gap + i*gap))
        if picked_up_piece:
            image = pygame.transform.scale(
                picked_up_piece.image, (PIECE_SIZE, PIECE_SIZE))
            self.win.blit(
                image, (mouse_pos[0] - PIECE_SIZE//2, mouse_pos[1] - PIECE_SIZE//2))

        # show possible moves
        for i in range(10):
            for j in range(9):
                if (i, j) in possible_moves:
                    center = ((j+0.5)*gap, (i+0.5)*gap)
                    radius = gap*0.2
                    target_rect = pygame.Rect(center, (0, 0)).inflate(
                        (radius * 2, radius * 2))
                    shape_surf = pygame.Surface(
                        target_rect.size, pygame.SRCALPHA)
                    pygame.draw.circle(shape_surf, GREEN,
                                       (radius, radius), radius)
                    self.win.blit(shape_surf, target_rect)
        if fromPos:
            center = ((fromPos[1]+0.5)*gap, (fromPos[0]+0.5)*gap)
            pygame.draw.circle(self.win, PURPLE, center,
                               PIECE_SIZE*0.4, line_width)

        if lastPos:
            center = ((lastPos[1]+0.5)*gap, (lastPos[0]+0.5)*gap)
            radius = gap*0.3
            target_rect = pygame.Rect(center, (0, 0)).inflate(
                (radius * 2, radius * 2))
            shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
            pygame.draw.circle(shape_surf, BLUE, (radius, radius), radius)
            self.win.blit(shape_surf, target_rect)

        # notify that current player is in check
        if board.is_inCheck(current_turn):
            i, j = board.find_King(current_turn)
            center = ((j+0.5)*gap, (i+0.5)*gap)
            radius = gap*0.5
            target_rect = pygame.Rect(center, (0, 0)).inflate(
                (radius * 2, radius * 2))
            shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
            pygame.draw.circle(shape_surf, RED, (radius, radius), radius)
            self.win.blit(shape_surf, target_rect)

        pygame.display.update()
    
    def play_sound(self, action:str):
        self.sounds[action].play()
