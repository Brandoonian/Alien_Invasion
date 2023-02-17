import sys
import pygame
from settings import Settings
from ship import Ship

class Alien_Invasion:
    """Overall class to manage game assets and behaviors."""
    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        # Set the background color.
        self. bg_color = (0, 0, 0)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    # Make game instance, and run game.
    ai = Alien_Invasion()
    ai.run_game()