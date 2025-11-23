import pygame
import time
import os
import random

# Load images (macOS)
IMG_DIR = "/Users/malpal101/Plethora-of-Python/Pygame/Space-Invaders/assets"

# Load images (Windows)
# IMG_DIR = "C:/Users/User/Plethora-of-Python/Pygame/Space-Invaders/assets"

# Enemy ships
RED_SPACE_SHIP = pygame.image.load(os.path.join(IMG_DIR, "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join(IMG_DIR, "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join(IMG_DIR, "pixel_ship_blue_small.png"))

# Player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join(IMG_DIR, "pixel_ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join(IMG_DIR, "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join(IMG_DIR, "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join(IMG_DIR, "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join(IMG_DIR, "pixel_laser_yellow.png"))

# Background
BG = pygame.image.load(os.path.join(IMG_DIR, "background-black.png"))
