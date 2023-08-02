#  Main game file
# Avoid Clutter of functions besides main()
# Example file showing a basic pygame "game loop"
import pygame
from player.stickman_player import Player
from world.testing_level import platform
from player.arm import draw_arm
from grapple.ropeSegmentTest import spawn_rope


ACC = 0.25
FRIC = -0.12

armImage = pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\arm\\armR.png')

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

P1 = Player(playerPosition)
PT1 = platform(width, height)

platforms = pygame.sprite.Group()
platforms.add(PT1)

playerSprites = pygame.sprite.Group()
playerSprites.add(P1)



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
   
    width = screen.get_width()
    height = screen.get_height()
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    
    # RENDER YOUR GAME HERE
    
    # P1.draw_player(screen, playerColors[1])
    P1.move(ACC, FRIC, width)
    is_jumping = P1.handle_collision(platforms)
    PT1.draw_platform(screen)
    playerSprites.draw(screen)
    
    draw_arm(screen, P1.pos, armImage, P1.direction)
    
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(144)  # limits FPS to 144

pygame.quit()