import pygame

def draw_level(screen, width, height):
    levelRect = pygame.Rect(width/3, 3*(height/4), width/3, height/4)
    pygame.draw.rect(screen, "black", levelRect, 5)
    return levelRect