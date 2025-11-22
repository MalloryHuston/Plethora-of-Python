import pygame
import time
import os
import random

# Load images (macOS)
IMG_DIR = "/Users/malpal101/Plethora-of-Python/Pygame/Space-Invaders/imgs"

# Load images (Windows)
# IMG_DIR = "C:/Users/User/Plethora-of-Python/Pygame/Space-Invaders/imgs"

RED_SPACE_SHIP = pygame.image.load(os.path.join(IMG_DIR,
                                                "pixel_ship_red_small.png"))
