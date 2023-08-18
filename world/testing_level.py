import pygame

class platform(pygame.sprite.Sprite):
    def __init__(self, WIDTH, pos):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 15))
        self.surf.fill("black")
        self.rect = self.surf.get_rect(center = (pos.x, pos.y))
    def draw_platform(self, screen):
        pygame.draw.rect(screen, "black", self.rect, 1)

class deathBox(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT, screenHeight):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, HEIGHT))
        self.surf.fill("red")
        self.rect = self.surf.get_rect(topleft = (0, screenHeight))
    def draw_platform(self, screen):
        pygame.draw.rect(screen, "red", self.rect, 1)