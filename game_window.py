#  Main game file
# Avoid Clutter of functions besides main()
# Example file showing a basic pygame "game loop"
import pygame
from player.stickman_player import draw_player
from world.testing_level import draw_level
from player.inputs import handle_inputs

GRAVITY = 3
JUMPVELO = -50

def handle_collision(elements, element):
    for thing in elements:
        if element.colliderect(thing):
            return True
    return False

# pygame setup
pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

playerColors = ["blue", "red", "green"]

playerPosition = pygame.Vector2(width/2, height/2)
is_jumping = False

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not is_jumping:
                    is_jumping = True
    width = screen.get_width()
    height = screen.get_height()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    
    # RENDER YOUR GAME HERE
    level_rect = draw_level(screen, width, height)
    handle_inputs(playerPosition)
    
    if is_jumping:
        playerPosition += pygame.Vector2(0, JUMPVELO)
        is_jumping = False
    
    if not is_jumping:
        playerPosition.y += GRAVITY
    
    
    hitbox = draw_player(playerPosition, screen, playerColors[1])
    if handle_collision([level_rect], hitbox):
        playerPosition.y = level_rect.top - hitbox.height + 16
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 120

pygame.quit()