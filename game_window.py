#  Main game file
# Avoid Clutter of functions besides main()
# Example file showing a basic pygame "game loop"
import pygame
from player.stickman_player import Player
from world.testing_level import platform, deathBox
from player.arm import draw_arm
from grapple.ropeSegmentTest import spawn_rope
from textDisplay.lives import draw_lives_text

ACC = 0.25
FRIC = -0.12

# Windows Path = D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\arm\\armR.png
# Mac Path = /Users/kendawg/Desktop/Coding Proj/Stickman/player/tempTextures/arm/armR.png
# path = /Users/kendawg/Desktop/Coding Proj/Stickman/player/tempTextures/


armImage = pygame.image.load('/Users/kendawg/Desktop/Coding Proj/Stickman/player/tempTextures/arm/armR.png')

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

theDeathBox = deathBox(width, 30, height)

P1 = Player(playerPosition)
PT1 = platform(width/3, pygame.Vector2(200,300))
PT2 = platform(width/3, pygame.Vector2(width - 600, height - 100))
#PT3 = platform(width/3, pygame.Vector2(width - 600, height - 500))

platforms = pygame.sprite.Group()
platforms.add(PT1)
platforms.add(PT2)
#platforms.add(PT3)

playerSprites = pygame.sprite.Group()
playerSprites.add(P1)


deathboxSprite = pygame.sprite.Group()
deathboxSprite.add(theDeathBox)

while running:
    # Check for a non-negative # of lives
    if P1.lives < 0:
        running = False

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

    draw_lives_text(screen, width, height, P1.lives)


    # P1.draw_player(screen, playerColors[1])
    P1.move(ACC, FRIC, width, height)
    is_jumping = P1.handle_collision(platforms, deathboxSprite)
    playerSprites.draw(screen)
    theDeathBox.draw_platform(screen)
    draw_arm(screen, P1.pos, armImage, P1.direction)
    
    for platform in platforms:
        platform.draw_platform(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # limits FPS to 144

pygame.quit()