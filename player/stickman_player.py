import pygame

def draw_player(playerPosition, screen, playerColor):
    mousePos = pygame.mouse.get_pos()
    playerHitbox = pygame.Rect(playerPosition.x + -22, playerPosition.y + -15, 45, 107) 
    pygame.draw.rect(screen, playerColor, playerHitbox, 1)  
    pygame.draw.circle(screen, playerColor, playerPosition, 15) # Head
    pygame.draw.line(screen, playerColor, playerPosition, playerPosition + pygame.Vector2(0, 50), 5) # Body 
    pygame.draw.line(screen, playerColor, playerPosition + pygame.Vector2(0, 50), (playerPosition + pygame.Vector2(0, 50)) +  pygame.Vector2(20, 40), 5) # Legs
    pygame.draw.line(screen, playerColor, playerPosition + pygame.Vector2(0, 50), (playerPosition + pygame.Vector2(0, 50)) +  pygame.Vector2(-20, 40), 5) # legs
    pygame.draw.line(screen, playerColor, playerPosition + pygame.Vector2(2, 25), (playerPosition + pygame.Vector2(0, 50)) +  pygame.Vector2(20, -5),5)
    pygame.draw.line(screen, playerColor, playerPosition + pygame.Vector2(-2, 25), (playerPosition + pygame.Vector2(0, 50)) +  pygame.Vector2(-20, -5), 5)
    return playerHitbox