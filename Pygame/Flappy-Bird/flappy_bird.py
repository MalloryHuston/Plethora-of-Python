"""
The classic game of Flappy Bird. Made with Python
and Pygame. Features pixel perfect collision using masks :O

Date Modified:  November 5, 2025
Author: Mallory Huston
Estimated Work Time: 6.5 hours (2 just for that damn collision)
"""

import pygame
import random
import os

# Initialize pygame and font
pygame.init()
pygame.font.init()

# Global constants
WIN_WIDTH = 600
WIN_HEIGHT = 800
FLOOR = 730
PIPE_VEL = 5
STAT_FONT = pygame.font.SysFont("comicsans", 50)
END_FONT = pygame.font.SysFont("comicsans", 70)

# Set up window
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# macOS – FILE PATH DIRECTORIES #
# "/Users/malpal101/Plethora-of-Python/Pygame/Flappy-Bird/imgs"

# Windows Command Prompt – FILE PATH DIRECTORIES #
# "C:\Users\User\Plethora-of-Python\Pygame\Flappy-Bird\imgs"

# Load images
IMG_DIR = "/Users/malpal101/Plethora-of-Python/Pygame/Flappy-Bird/imgs"

pipe_path = os.path.join(IMG_DIR, "pipe.png")
pipe_img = pygame.transform.scale2x(
    pygame.image.load(pipe_path).convert_alpha()
)

bg_path = os.path.join(IMG_DIR, "bg.png")
bg_raw = pygame.image.load(bg_path).convert_alpha()
bg_img = pygame.transform.scale(bg_raw, (600, 900))

bird_images = []
for x in range(1, 4):
    bird_path = os.path.join(IMG_DIR, f"bird{x}.png")
    bird_img = pygame.image.load(bird_path)
    bird_images.append(pygame.transform.scale2x(bird_img))

base_path = os.path.join(IMG_DIR, "base.png")
base_img = pygame.transform.scale2x(
    pygame.image.load(base_path).convert_alpha()
)


class Bird:
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5
    IMGS = bird_images

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1
        time = self.tick_count
        displacement = self.vel * time + 0.5 * 3 * (time ** 2)

        if displacement >= 16:
            displacement = (displacement / abs(displacement)) * 16

        if displacement < 0:
            displacement -= 2

        self.y += displacement

        if displacement < 0 or self.y < self.height + 50:
            self.tilt = min(self.tilt + self.ROT_VEL, self.MAX_ROTATION)
        else:
            self.tilt = max(self.tilt - self.ROT_VEL, -90)

    def draw(self, win):
        self.img_count += 1

        if self.img_count <= self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count <= self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1]
        elif self.img_count <= self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]
        elif self.img_count <= self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1]
        else:
            self.img = self.IMGS[0]
            self.img_count = 0

        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2

        blit_rotate_center(win, self.img, (self.x, self.y), self.tilt)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


class Pipe:
    GAP = 200
    VEL = PIPE_VEL

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(pipe_img, False, True)
        self.PIPE_BOTTOM = pipe_img
        self.passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        return b_point or t_point


class Base:
    VEL = PIPE_VEL
    WIDTH = base_img.get_width()
    IMG = base_img

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))


def blit_rotate_center(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    orig_rect = image.get_rect(topleft=topleft)
    center_point = orig_rect.center
    new_rect = rotated_image.get_rect(center=center_point)
    surf.blit(rotated_image, new_rect.topleft)


def draw_window(win, bird, pipes, base, score):
    win.blit(bg_img, (0, 0))

    for pipe in pipes:
        pipe.draw(win)

    base.draw(win)
    bird.draw(win)

    score_label = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(score_label, (WIN_WIDTH - score_label.get_width() - 15, 10))

    pygame.display.update()


def end_screen(win):
    run = True
    text_label = END_FONT.render("Press Space to Restart", 1, (255, 255, 255))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                main(win)

        win.blit(text_label, (WIN_WIDTH / 2 - text_label.get_width() / 2, 500))
        pygame.display.update()
    pygame.quit()
    quit()


def main(win):
    bird = Bird(230, 350)
    base = Base(FLOOR)
    pipes = [Pipe(700)]
    score = 0
    clock = pygame.time.Clock()
    run = True
    started = False

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
                    started = True

        if started:
            bird.move()
            base.move()

            add_pipe = False
            rem = []
            for pipe in pipes:
                pipe.move()
                if pipe.collide(bird):
                    end_screen(win)

                if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                    rem.append(pipe)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

            if add_pipe:
                score += 1
                pipes.append(Pipe(WIN_WIDTH))

            for r in rem:
                pipes.remove(r)

            if bird.y + bird.img.get_height() >= FLOOR:
                end_screen(win)

        draw_window(win, bird, pipes, base, score)


if __name__ == "__main__":
    main(WIN)
