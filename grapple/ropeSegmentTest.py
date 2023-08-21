import pygame
import math

class Rope:
    def __init__(self, playerPos):
        self.segments = []
        self.segmentLength = 10
        self.ropeLength = 0
        self.numSegments = 0
        self.startPos = pygame.Vector2(0,0)
        self.create_rope(playerPos)
    def create_rope(self, playerPos):
        self.startPos = pygame.mouse.get_pos()
        dist_to_player = (playerPos - self.startPos).length()
        self.numSegments = math.ceil(dist_to_player / self.segmentLength) + 1
        self.ropeLength = dist_to_player / self.numSegments
        
        direction_vector = playerPos - self.startPos  # Calculate the direction vector
        segment_length_vector = direction_vector.normalize() * self.segmentLength
        
        for i in range(self.numSegments - 1):  # Loop up to the second-to-last segment
            start = self.startPos + segment_length_vector * i
            end = start + segment_length_vector
            ropeSegment = Segment(start, end, self.segmentLength, self.startPos)
            self.segments.append(ropeSegment)
        
        # Create the last segment with a fixed length attached to playerPos
        last_segment_start = self.segments[-1].end
        last_segment_end = playerPos
        last_ropeSegment = Segment(last_segment_start, last_segment_end, self.segmentLength, self.startPos)
        self.segments.append(last_ropeSegment)
    
    def update(self, screen, Gravity, Speed, platforms, playerPos):
        i = 0
        for segment in self.segments:
            segment.update(Gravity, Speed, platforms, i, self.segments, playerPos)
            i += 1
        
class Segment:
    def __init__(self, start, end, length, ropeStart):
        self.length = length
        self.start = start
        self.end = end
        self.ropeStart = ropeStart
        self.velocity = pygame.Vector2(0, 0)
    
    def draw(self, screen):
        pygame.draw.line(screen, (0,0,0), self.start, self.end)
        pygame.draw.circle(screen, 'black', self.start, 1)
        pygame.draw.circle(screen, 'black', self.end, 1)
    
    def update(self, gravity, speed_factor, platforms, index, segments, playerPos):
        if index == 0:
            self.start = self.ropeStart
        else:
            self.start = segments[index - 1].end
        self.velocity.y += gravity * speed_factor
        
        self.end += self.velocity * speed_factor  # Update the rope's position based on velocity

        # Keep the rope's length constant
        displacement = self.end - self.start
        displacement_length = displacement.length()
        
        if displacement_length != 0:
            scaling_factor = self.length / displacement_length
            displacement *= scaling_factor
            self.end = self.start + displacement
        self.handle_collision(platforms)
        
    def handle_collision(self, platforms):
        for platform in platforms:
            if self.check_collision(platform):
                self.end.y = platform.rect.top
                self.velocity.y = 0
    def check_collision(self, platform):
        # Check if either the start or end of the rope segment intersects with the platform
        rope_start_rect = pygame.Rect(self.start, (1, 1))  # Create a small rectangle at the rope start point
        rope_end_rect = pygame.Rect(self.end, (1, 1))  # Create a small rectangle at the rope end point
        return rope_start_rect.colliderect(platform.rect) or rope_end_rect.colliderect(platform.rect)