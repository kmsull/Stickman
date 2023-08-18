import pygame

class Rope:
    def __init__(self, hookPosition, endPos, length):
        self.length = 20
        self.start = hookPosition
        self.end = endPos
        

    def update(self, gravity):
        self.end.y += gravity

        # Keep the rope's length constant
        displacement = self.end - self.start
        displacement_length = displacement.length()
        
        if displacement_length != 0:  # Avoid division by zero
            scaling_factor = self.length / displacement_length
            displacement *= scaling_factor
            self.end = self.start + displacement

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
    
    def constrain_length(self):
     displacement = self.end - self.start
     if displacement.length() != 0:
         scaling_factor = self.length / displacement.length()
         displacement *= scaling_factor
         self.end = self.start + displacement