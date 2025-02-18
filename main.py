import pygame
import sys
from menu import display_menu
from uroven1 import start_level1
# Importuj další levely, např.:
# from uroven2 import start_level2

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Robutek")

# Hlavní herní smyčka
def main():
    menu_active = True
    while menu_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Kliknutí levým tlačítkem myši
                    mouse_x, mouse_y = event.pos
                    # Určování, na jaké tlačítko bylo kliknuto a přechod na odpovídající level
                    for i in range(15):
                        if i < 5:
                            row = 1
                            col = i
                        elif i < 10:
                            row = 2
                            col = i - 5
                        else:
                            row = 3
                            col = i - 10

                        button_width, button_height = 60, 60
                        padding = 20
                        x_pos = (250 - (button_width * 2 + padding)) + (col * (button_width + padding))
                        y_pos = (row * (button_height + padding))

                        rect = pygame.Rect(x_pos, y_pos, button_width, button_height)
                        if rect.collidepoint(mouse_x, mouse_y):
                            print(f"Začínám level {i + 1}")
                            menu_active = False
                            if i == 0:  # Level 1
                                start_level1(screen)
                            # přidat další podmínky pro další levely, např.:
                            # elif i == 1:
                            #     start_level2(screen)

        screen.fill((255, 255, 255))
        display_menu(screen)

        pygame.display.update()
        pygame.time.Clock().tick(60)

# Spuštění hlavní smyčky
if __name__ == "__main__":
    main()
