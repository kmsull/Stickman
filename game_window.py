import pygame
from player.stickman_player import Player
from world.testing_level import platform, deathBox  
from player.arm import draw_arm
from grapple.ropeSegmentTest import Rope, Segment
from textDisplay.lives import draw_lives_text
import os
import math

ACC = 0.25
FRIC = -0.12
ROPE_SEGMENT_LENGTH = 10
GRAVITY = 0.5
speed_factor = .5


tempTextures_folder = os.path.join(os.path.dirname(__file__),"player", "tempTextures")       
armImage = pygame.image.load(os.path.join(tempTextures_folder, 'arm', 'armR.png'))


pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
clock = pygame.time.Clock()

playerColors = ["blue", "red", "green"]
playerPosition = pygame.Vector2(width/2, height/2)

theDeathBox = deathBox(width, 30, height)    
P1 = Player(playerPosition)

PT1 = platform(width/3, pygame.Vector2(250,550))
PT2 = platform(width/3, pygame.Vector2(width - 600, height - 100))
PT3 = platform(width/3, pygame.Vector2(width - 600, height - 350))

platforms = pygame.sprite.Group()
platforms.add(PT1)
platforms.add(PT2)
platforms.add(PT3)

playerSprites = pygame.sprite.Group()
playerSprites.add(P1)

spawnedRopes = []
rope_segments = []

deathboxSprite = pygame.sprite.Group()
deathboxSprite.add(theDeathBox)


running = True
while running:

  if P1.lives < 0:
    running = False

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
      running = False

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        rope = Rope(P1.pos)
        spawnedRopes.append(rope)
            
  screen.fill("white")  

  draw_lives_text(screen, width, height, P1.lives)

  P1.move(ACC, FRIC, width, screen)    

  
  for rope in spawnedRopes:
    rope.update(screen, GRAVITY, speed_factor, platforms, P1.pos)
    for segment in rope.segments:
      segment.draw(screen)

  is_jumping = P1.handle_collision(platforms, deathboxSprite)

  playerSprites.draw(screen)
  theDeathBox.draw_platform(screen)
  draw_arm(screen, P1.pos, armImage, P1.direction)   

  for platform in platforms:
    platform.draw_platform(screen)

  pygame.display.flip()
  clock.tick(120)

pygame.quit()