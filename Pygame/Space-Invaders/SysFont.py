import pygame
pygame.init()

# Get and format font names
fonts = pygame.font.get_fonts()
formatted_fonts = [f.replace('_', ' ').title() for f in fonts]
sorted_fonts = sorted(formatted_fonts)

# Print each font on its own line
for f in sorted_fonts:
    print(f"'{f}'")
