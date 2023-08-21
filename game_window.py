import pygame
from player.stickman_player import Player
from world.testing_level import platform, deathBox  
from player.arm import draw_arm
from grapple.ropeSegmentTest import Rope
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

platforms = pygame.sprite.Group()
platforms.add(PT1)
platforms.add(PT2)

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
   
        mouse_pos = pygame.mouse.get_pos()
        dist_to_player = (P1.pos - mouse_pos).length()
        num_segments = math.ceil(dist_to_player / ROPE_SEGMENT_LENGTH)
        
        rope_segments = []
        
        rope_len = dist_to_player / num_segments
        length_vector = pygame.math.Vector2(ROPE_SEGMENT_LENGTH, 0)
        for i in range(num_segments):
            start = mouse_pos
            end = start + length_vector
            rope = Rope(start, end, ROPE_SEGMENT_LENGTH)
            rope_segments.append(rope)
            previous_rope = rope
        rope_segments[-1].end = P1.pos
        spawnedRopes.append(rope_segments)
  screen.fill("white")  

  draw_lives_text(screen, width, height, P1.lives)

  P1.move(ACC, FRIC, width, height)    

  
  gravity_vector = pygame.Vector2(0, GRAVITY)
  
  previous_segment = None
  for rope_segments in spawnedRopes:
      for segment in rope_segments[:-1]:
          if previous_segment:
              segment.start = previous_segment.end
          
          segment.update(GRAVITY, speed_factor)
          segment.handle_collision(platforms) 
          pygame.draw.line(screen, (0,0,0), segment.start, segment.end)
          pygame.draw.circle(screen, 'black', segment.start, 1)
          pygame.draw.circle(screen, 'black', segment.end, 1)
          previous_segment = segment
          rope_segments[-1].start = rope_segments[-2].end 
          rope_segments[-1].end = P1.pos

  is_jumping = P1.handle_collision(platforms, deathboxSprite)

  playerSprites.draw(screen)
  theDeathBox.draw_platform(screen)
  draw_arm(screen, P1.pos, armImage, P1.direction)   

  for platform in platforms:
    platform.draw_platform(screen)

  pygame.display.flip()
  clock.tick(120)

pygame.quit()