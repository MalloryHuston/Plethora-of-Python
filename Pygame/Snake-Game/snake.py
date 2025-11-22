"""
Classic Snake game implemented using Python and Pygame
Author: Mallory Huston
"""

import pygame
import random

# Constants
WIDTH = 500
HEIGHT = 500
ROWS = 20
COLS = 25
CELL_SIZE = WIDTH // ROWS

# Initialize Pygame
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


class Cube:
    def __init__(self, pos, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = pos
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        i, j = self.pos
        pygame.draw.rect(
            surface,
            self.color,
            (
                i * CELL_SIZE + 1,
                j * CELL_SIZE + 1,
                CELL_SIZE - 2,
                CELL_SIZE - 2,
            ),
        )
        if eyes:
            centre = CELL_SIZE // 2
            radius = 3
            circleMiddle1 = (
                i * CELL_SIZE + centre - radius,
                j * CELL_SIZE + 8,
            )
            circleMiddle2 = (
                i * CELL_SIZE + CELL_SIZE - radius * 2,
                j * CELL_SIZE + 8,
            )
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle1, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)


class Snake:
    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body = [self.head]
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.dirnx != 1:
            self.dirnx = -1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        elif keys[pygame.K_RIGHT] and self.dirnx != -1:
            self.dirnx = 1
            self.dirny = 0
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        elif keys[pygame.K_UP] and self.dirny != 1:
            self.dirnx = 0
            self.dirny = -1
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
        elif keys[pygame.K_DOWN] and self.dirny != -1:
            self.dirnx = 0
            self.dirny = 1
            self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, cube in enumerate(self.body):
            p = cube.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                cube.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    del self.turns[p]
            else:
                cube.move(cube.dirnx, cube.dirny)

    def reset(self, pos):
        self.head = Cube(pos)
        self.body = [self.head]
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def add_cube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1:
            new_pos = (tail.pos[0] - 1, tail.pos[1])
        elif dx == -1:
            new_pos = (tail.pos[0] + 1, tail.pos[1])
        elif dy == 1:
            new_pos = (tail.pos[0], tail.pos[1] - 1)
        else:
            new_pos = (tail.pos[0], tail.pos[1] + 1)

        new_cube = Cube(new_pos)
        new_cube.dirnx = dx
        new_cube.dirny = dy
        self.body.append(new_cube)

    def draw(self, surface):
        for i, cube in enumerate(self.body):
            cube.draw(surface, eyes=(i == 0))


def draw_grid(surface):
    for i in range(ROWS):
        pygame.draw.line(
            surface,
            (255, 255, 255),
            (0, i * CELL_SIZE),
            (WIDTH, i * CELL_SIZE),
        )
        pygame.draw.line(
            surface,
            (255, 255, 255),
            (i * CELL_SIZE, 0),
            (i * CELL_SIZE, HEIGHT),
        )


def redraw_window(surface, snake, snack):
    surface.fill((0, 0, 0))
    snake.draw(surface)
    snack.draw(surface)
    draw_grid(surface)
    pygame.display.update()


def random_snack(snake):
    positions = [cube.pos for cube in snake.body]
    while True:
        x = random.randrange(ROWS)
        y = random.randrange(ROWS)
        if (x, y) not in positions:
            break
    return Cube((x, y), color=(0, 255, 0))


def main():
    clock = pygame.time.Clock()
    s = Snake((255, 0, 0), (10, 10))
    snack = random_snack(s)
    run = True
    started = False

    while run:
        pygame.time.delay(50)
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                started = True

        if started:
            s.move()
            head_pos = s.head.pos

            # Collision with walls
            if (
                head_pos[0] >= ROWS
                or head_pos[0] < 0
                or head_pos[1] >= ROWS
                or head_pos[1] < 0
            ):
                print("Game Over! Score:", len(s.body))
                s.reset((10, 10))
                snack = random_snack(s)
                started = False

            # Collision with self
            for segment in s.body[1:]:
                if segment.pos == head_pos:
                    print("Game Over! Score:", len(s.body))
                    s.reset((10, 10))
                    snack = random_snack(s)
                    started = False
                    break

            # Eating snack
            if head_pos == snack.pos:
                s.add_cube()
                snack = random_snack(s)

        redraw_window(win, s, snack)


if __name__ == "__main__":
    main()
