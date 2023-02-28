import pygame.font


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings = ai_game.stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)    # Tells Python to round the value of stats.score to the nearest 10's place and store it in rounded score.
        score_str = "Score: ""{:,}".format(rounded_score)    # Inserts commas into numbers when converting a numerical value to a string.
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.bg_color)  # We then render the image on the screen by passing the screen's background color and the text color.

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()  # We create a rect.
        self.score_rect.right = self.screen_rect.right - 20  # We set the right edge of rect 20 pixels from the right edge of the screen.
        self.score_rect.top = 20  # We set the top edge 20 pixels beneath the top of the screen.

    def show_score(self):
        """Draw scores and levels to the screen."""
        self.screen.blit(self.score_image, self.score_rect)  # Draws the score image onscreen at the location that score_rect specifies.
        self.screen.blit(self.high_score_imgage, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)    # We round the high_score to the nearest 10 and format it with commas.
        high_score_str = "High Score: ""{:,}".format(high_score)
        self.high_score_imgage = self.font.render(high_score_str, True,
                                        self.text_color, self.settings.bg_color)    # We generate an image from high_score.

        # Center the high score at the top of the screen.
        self.high_score_rect =self.high_score_imgage.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx    # Center the highscore rect horizontally.
        self.high_score_rect.top = self.score_rect.top    # We set the image's 'top' attribute to match the top of the score image.

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()    # Updates the value of high_score.

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = "Lvl: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
                                self.text_color, self.settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
