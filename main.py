import pygame
import sys
from setting import *
from level import Level
from menu import Menu
from gameover import GameOverScreen

class Game:
    def __init__(self):
        pygame.init()

        # General setup
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Rougelite Basic')
        self.clock = pygame.time.Clock()

        # Initialize game components
        self.level = Level()
        self.main_menu = Menu()
        self.game_over_screen = GameOverScreen(self.screen)

        # Game state
        self.game_over = False

        # Timer setup
        self.start_time = pygame.time.get_ticks()
        self.timer_font = pygame.font.Font(UI_FONT, UI_TIMER_SIZE)
        self.game_duration = 15 * 1000 * 60

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.handle_events()

            if self.main_menu.show_main_menu:
                self.main_menu.render_main_menu(self.screen)
                self.handle_menu_events()

            else:
                if not self.game_over:
                    self.screen.fill('white')
                    self.level.run()

                    # Update and display the timer
                    elapsed_time = pygame.time.get_ticks() - self.start_time
                    self.display_timer(elapsed_time)

                    # Check player's health
                    if self.level.player.health <= 0 or elapsed_time >= self.game_duration:
                        self.game_over = True

                    pygame.display.update()
                    self.clock.tick(FPS)

                else:
                    self.game_over_screen.show_game_over(elapsed_time, self.level.player.exp)

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.main_menu.start_button.collidepoint(event.pos):
                    # Transition to the game level
                    self.main_menu.show_main_menu = False

                    # Reset game-over state and timer
                    self.game_over = False
                    self.start_time = pygame.time.get_ticks()

                elif self.main_menu.quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

    def display_timer(self, elapsed_time):
        # Calculate minutes and seconds
        minutes = int(elapsed_time / 60000)
        seconds = int((elapsed_time % 60000) / 1000)

        # Create a text surface for the timer
        timer_text = self.timer_font.render(f"{minutes:02d}:{seconds:02d}", True, (255, 255, 255))

        # Get the rectangle of the text surface
        timer_rect = timer_text.get_rect(center=(MENU_WIDTH_CENTER, 20))

        # Blit the timer text onto the screen
        self.screen.blit(timer_text, timer_rect)

if __name__ == '__main__':
    game = Game()
    game.run()
