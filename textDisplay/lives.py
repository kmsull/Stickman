import pygame
import os

def draw_lives_text(screen, screen_width, screen_height, playerLives):
    # Set the font and size
    font_path = os.path.join(os.path.dirname(__file__), 'fonts', 'Adventure.otf')
    font = pygame.font.Font(font_path, 36)

    # Create a text surface
    text_surface = font.render("Lives: " + str(playerLives), True, "red")

    #  Blit the text surface onto the screen
    screen.blit(text_surface, (screen_width - text_surface.get_width() - 20, 0 + text_surface.get_height() + 5))
