import pygame
import sys

# Funkce pro zobrazení levelu
def start_level1(screen):
    # Nastavení počátečních pozic a proměnných
    x, y = 250, 250  # Počáteční pozice větší krychle
    width, height = 40, 40  # Rozměry větší krychle
    velocity = 5  # Rychlost pohybu
    font = pygame.font.Font(None, 36)
    text_input = ""  # Text, který bude uživatel zadávat
    clock = pygame.time.Clock()

    # Menší krychle (snížena, pokud na ni větší krychle najede)
    small_x, small_y = 500, 250
    small_width, small_height = 30, 30

    # Menší krychle (snížena, pokud na ni větší krychle najede)
    small_x2, small_y2 = 400, 120
    small_width2, small_height2 = 30, 30

    running = True
    while running:
        # Čistíme obrazovku
        screen.fill((0,0,0))  # barva pozadí

        # Zpracování událostí (klávesy, zavření okna)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Pokud uživatel stiskne ESC, zavře úroveň
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]  # Odstranit poslední znak
                else:
                    text_input += event.unicode  # Přidat znak do textového pole

        # Pohyb větší krychle pomocí kláves
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= velocity
        if keys[pygame.K_RIGHT]:
            x += velocity
        if keys[pygame.K_UP]:
            y -= velocity
        if keys[pygame.K_DOWN]:
            y += velocity

        # Kolize mezi větší a menší krychlí (když se krychle střetnou)
        if pygame.Rect(x, y, width, height).colliderect(pygame.Rect(small_x, small_y, small_width, small_height)):
            small_x, small_y = -100, -100  # "Snížení" menší krychle (posune ji mimo obrazovku)
            # Kolize mezi větší a menší krychlí (když se krychle střetnou)
        if pygame.Rect(x, y, width, height).colliderect(pygame.Rect(small_x2, small_y2, small_width2, small_height2)):
            small_x2, small_y2 = -100, -100

        # Zobrazení větší krychle (ovládané hráčem)
        pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))

        # Zobrazení menší krychle (statická)
        pygame.draw.rect(screen, (0, 255, 255), (small_x, small_y, small_width, small_height))
        
        # Zobrazení menší krychle (statická)
        pygame.draw.rect(screen, (0, 255, 255), (small_x2, small_y2, small_width2, small_height2))

        # Zobrazení textového pole
        input_box = pygame.Rect(150, 500, 500, 40)  # Textové pole
        pygame.draw.rect(screen, (255, 255, 255), input_box, 2)  # Rámeček
        text_surface = font.render(text_input, True, (255, 255, 255))  # Text v textovém poli
        screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))  # Zobrazení textu

        # Aktualizace displeje
        pygame.display.update()
        clock.tick(60)  # FPS

# Spuštění pygame a hlavní smyčky
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Robutek - Level 1")
    start_level1(screen)
    pygame.quit()
