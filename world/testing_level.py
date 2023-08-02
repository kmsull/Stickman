import pygame

class platform(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 1))
        self.surf.fill("black")
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 50))
    def draw_platform(self, screen):
        pygame.draw.rect(screen, "black", self.rect, 1)