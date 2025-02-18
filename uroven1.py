import pygame
import sys

def start_level1(screen):
    # Nastavení počátečních pozic a proměnných
    x, y = 250, 250  # Počáteční pozice čtverce
    width, height = 50, 50  # Rozměry čtverce
    velocity = 5  # Rychlost pohybu
    font = pygame.font.Font(None, 36)
    text_input = ""  # Text, který bude uživatel zadávat
    clock = pygame.time.Clock()

    running = True
    while running:
        # Čistíme obrazovku
        screen.fill((255, 255, 255))  # Bílá barva pozadí
        
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

        # Pohyb čtverce pomocí kláves
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= velocity
        if keys[pygame.K_RIGHT]:
            x += velocity
        if keys[pygame.K_UP]:
            y -= velocity
        if keys[pygame.K_DOWN]:
            y += velocity
        
        # Zobrazení čtverce
        pygame.draw.rect(screen, (255, 0, 50), (x, y, width, height))
        
        # Zobrazení textového pole
        input_box = pygame.Rect(50, 350, 500, 40)  # Textové pole
        pygame.draw.rect(screen, (0, 0, 0), input_box, 2)  # Rámeček
        text_surface = font.render(text_input, True, (0, 0, 0))  # Text v textovém poli
        screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))  # Zobrazení textu

        pygame.display.update()
        clock.tick(60)  # FPS
