import pygame

class Rope:
    def __init__(self, hookPosition, endPos, length):
        self.length = 10
        self.start = hookPosition
        self.end = endPos
        self.velocity = pygame.Vector2(0, 0)
        

    def update(self, gravity, speed_factor):
        self.velocity.y += gravity * speed_factor

        self.end += self.velocity * speed_factor  # Update the rope's position based on velocity

        # Keep the rope's length constant
        displacement = self.end - self.start
        displacement_length = displacement.length()
        
        if displacement_length != 0:
            scaling_factor = self.length / displacement_length
            displacement *= scaling_factor
            self.end = self.start + displacement

    def handle_collision(self, platforms):
        for platform in platforms:
            if self.check_collision(platform):
                self.end.y = platform.rect.top
                self.velocity.y = 0

    def newRope(self, hookPosition):
        start_position = hookPosition
        end_position = hookPosition + pygame.Vector2(self.length, 0)
        rope = Rope(start_position, end_position, self.length)
        
        ropes = []
        
        ropes.append(rope)
        
        for x in range(10):
            start_position = end_position
            end_position = hookPosition + pygame.Vector2(self.length, 0)
            rope = Rope(start_position, end_position, self.length)
            ropes.append(rope)
        return ropes
    
    def check_collision(self, platform):
        # Check if either the start or end of the rope segment intersects with the platform
        rope_start_rect = pygame.Rect(self.start, (1, 1))  # Create a small rectangle at the rope start point
        rope_end_rect = pygame.Rect(self.end, (1, 1))  # Create a small rectangle at the rope end point
        return rope_start_rect.colliderect(platform.rect) or rope_end_rect.colliderect(platform.rect)
    
