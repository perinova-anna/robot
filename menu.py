import pygame

# Funkce pro zobrazení menu
def display_menu(screen):
    font = pygame.font.Font(None, 60)
    screen.fill((0, 0, 0))

    button_width, button_height = 60, 60 #velikost tlačítka
    padding = 20

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

        x_pos = (300 - (button_width * 2 + padding)) + (col * (button_width + padding))
        y_pos = (50 + row * (button_height + padding)) #sem bych potřebovala dát střed, aby to nebylo na pixely

        text = font.render(str(i + 1), True, (65, 255, 255))
        text_rect = text.get_rect(center=(x_pos + button_width // 2, y_pos + button_height // 2))

        pygame.draw.rect(screen, (0, 0, 0), (x_pos, y_pos, button_width, button_height))
        pygame.draw.rect(screen, (255, 255, 255), (x_pos, y_pos, button_width, button_height), 3)
        screen.blit(text, text_rect)

    pygame.display.update()
