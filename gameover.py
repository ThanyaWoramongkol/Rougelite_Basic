import pygame
from setting import *

class GameOverScreen:
    def __init__(self, screen):
        self.screen = screen

    def show_game_over(self, elapsed_time, exp):
        # Load the background image
        background_image = pygame.image.load("./Asset/GameOver.png")
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGTH))

        # Draw the background image
        self.screen.blit(background_image, (0, 0))

        # Header Text
        game_over_text = pygame.font.Font(UI_OUTLINE, 48).render("Game Over", True, MENU_BUTTON_COLOR)
        self.screen.blit(game_over_text, (MENU_WIDTH_CENTER - game_over_text.get_width() // 2, MENU_HEIGTH_CENTER - 250))

        # Time Text
        elapsed_minutes = int(elapsed_time / 60000)
        elapsed_seconds = int((elapsed_time % 60000) / 1000)
        elapsed_text = pygame.font.Font(UI_FONT, 36).render(f"Time : {elapsed_minutes:02d}:{elapsed_seconds:02d}", True, MENU_BUTTON_COLOR)
        self.screen.blit(elapsed_text, (MENU_WIDTH_CENTER - elapsed_text.get_width() // 2, MENU_HEIGTH_CENTER - 150))

        # Score Text
        exp_show = str(int(exp))
        exp_text = pygame.font.Font(UI_FONT, 36).render(f"Score : {exp_show}", True, MENU_BUTTON_COLOR)
        self.screen.blit(exp_text, (MENU_WIDTH_CENTER - exp_text.get_width() // 2, MENU_HEIGTH_CENTER - 100))
        

        pygame.display.update()

