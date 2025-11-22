import pygame

pygame.init()

# Set up the screen
Black = (0, 0, 0)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255, 255, 255))

# Load The images
imp = pygame.image.load("Cross.png")
imp = pygame.transform.scale(imp, (100, 100))
imp2 = pygame.image.load("Nought.png")
imp2 = pygame.transform.scale(imp2, (100, 100))

# Initialize the font
font = pygame.font.SysFont("Arial", 32)


def RedrawGameWindow():
    screen.fill(255, 255, 255)
    global G00
    global G01
    global G02
    global G10
    global G11
    global G12
    global G20
    global G21
    global G22

    G00 = pygame.draw.rect(screen, Black, (250, 150, 100, 100), 1)

    G01 = pygame.draw.rect(screen, Black, (350, 150, 100, 100), 1)

    G02 = pygame.draw.rect(screen, Black, (450, 150, 100, 100), 1)

    G10 = pygame.draw.rect(screen, Black, (250, 250, 100, 100), 1)

    G11 = pygame.draw.rect(screen, Black, (350, 250, 100, 100), 1)

    G12 = pygame.draw.rect(screen, Black, (450, 250, 100, 100), 1)

    G20 = pygame.draw.rect(screen, Black, (250, 350, 100, 100), 1)

    G21 = pygame.draw.rect(screen, Black, (350, 350, 100, 100), 1)

    G22 = pygame.draw.rect(screen, Black, (450, 350, 100, 100), 1)

    grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    pygame.display.flip()


def displayGrid(grid):
    print(" " + grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2])
    print("-----------")
    print(" " + grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2])
    print("-----------")
    print(" " + grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2])


def checkGridX(grid):
    global RowMsg

    # Checks The Rows
    if grid[0][0] == "X" and grid[0][1] == "X" and grid[0][2] == "X":
        RowMsg = "Three Xs in a row."
        text2 = font.render(RowMsg, True, (0, 0, 0))
        print("Three Xs in a row.")
        screen.blit(text2, text_rect2)
        text3 = font.render(
            "Press R to restart", True, (0, 0, 0)
        )  # Render the text
        text_rect3 = text.get_rect(center=(screen_width / 2, 700))
        screen.blit(text3, text_rect3)

    if grid[1][0] == "X" and grid[1][1] == "X" and grid[1][2] == "X":
        RowMsg = "Three Xs in a row."
        text2 = font.render(RowMsg, True, (0, 0, 0))
        print("Three Xs in a row.")
        screen.blit(text2, text_rect2)
        text3 = font.render(
            "Press R to restart", True, (0, 0, 0)
        )  # Render the text
        text_rect3 = text.get_rect(center=(screen_width / 2, 700))
        screen.blit(text3, text_rect3)

    if grid[2][0] == "X" and grid[2][1] == "X" and grid[2][2] == "X":
        RowMsg = "Three Xs in a row."
        text2 = font.render(RowMsg, True, (0, 0, 0))
        print("Three Xs in a row.")
        screen.blit(text2, text_rect2)
