import pygame

def handle_inputs(playerPosition):
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        playerPosition += pygame.Vector2(1, 0)
    if keys[pygame.K_a]:
        playerPosition += pygame.Vector2(-1, 0)

    if keys[pygame.K_d] & keys[pygame.K_LSHIFT]:
        playerPosition += pygame.Vector2(2, 0)
    if keys[pygame.K_a] & keys[pygame.K_LSHIFT]:
        playerPosition += pygame.Vector2(-2, 0)
            
    return