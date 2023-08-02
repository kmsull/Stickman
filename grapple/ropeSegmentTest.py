import pygame

def spawn_rope(screen):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP: 
            spawnPos = pygame.mouse.get_pos()
            return pygame.draw.line(screen, "black", spawnPos, spawnPos + pygame.Vector2(40, 0))
    
            
            
    