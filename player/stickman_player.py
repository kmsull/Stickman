import pygame
import os

vec = pygame.Vector2
class Player(pygame.sprite.Sprite):
    
    
    def __init__(self, pos):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.direction = 0
        self.pos = pos
        self.startingPos = self.pos
        self.vel = pygame.Vector2(0,0)
        self.acc = pygame.Vector2(0,0)
        self.is_jumping = False
        
        self.lives = 5

        self.standingSprite = []
        self.walkLeft = []
        self.walkRight = []
        self.jumpRight = []
        self.jumpLeft = []
        self.duck = []

        # Load Images
        #self.load_mac_images()
        # self.load_win_images()
        self.load_images()

        self.curSprite = 0
        self.image = self.standingSprite[self.curSprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
    
    def load_images(self):
        # Get the path to the tempTextures folder relative to the script's location
        tempTextures_folder = os.path.join(os.path.dirname(__file__), "tempTextures")

        # Standing Sprite
        self.standingSprite.append(pygame.image.load(os.path.join(tempTextures_folder, 'standing', 'standing1.png')))
        self.standingSprite.append(pygame.image.load(os.path.join(tempTextures_folder, 'standing', 'standing2.png')))

        # Duck
        #self.standingSprite.append(pygame.image.load(os.path.join(tempTextures_folder, 'duck', 'duckR.png')))
        #self.standingSprite.append(pygame.image.load(os.path.join(tempTextures_folder, 'duck', 'duckL.png')))

        # Walk Left
        self.walkLeft.append(pygame.image.load(os.path.join(tempTextures_folder, 'walkLeft', 'walkingL1.png')))
        self.walkLeft.append(pygame.image.load(os.path.join(tempTextures_folder, 'walkLeft', 'walkingL2.png')))
        self.walkLeft.append(pygame.image.load(os.path.join(tempTextures_folder, 'walkLeft', 'walkingL3.png')))
        self.walkLeft.append(pygame.image.load(os.path.join(tempTextures_folder, 'walkLeft', 'walkingL4.png')))
        self.walkLeft.append(pygame.image.load(os.path.join(tempTextures_folder, 'walkLeft', 'walkingL5.png')))
        self.walkLeft.append(pygame.image.load(os.path.join(tempTextures_folder, 'walkLeft', 'walkingL6.png')))
        self.walkLeft.append(pygame.image.load(os.path.join(tempTextures_folder, 'walkLeft', 'walkingL7.png')))
        # ... Add other images

        # Walk Right
        self.walkRight.append(pygame.image.load(os.path.join(tempTextures_folder, 'walkRight', 'walkingR1.png')))
        self.walkRight.append(pygame.image.load(os.path.join(tempTextures_folder, 'walkRight', 'walkingR2.png')))
        self.walkRight.append(pygame.image.load(os.path.join(tempTextures_folder, 'walkRight', 'walkingR3.png')))
        self.walkRight.append(pygame.image.load(os.path.join(tempTextures_folder, 'walkRight', 'walkingR4.png')))
        self.walkRight.append(pygame.image.load(os.path.join(tempTextures_folder, 'walkRight', 'walkingR5.png')))
        self.walkRight.append(pygame.image.load(os.path.join(tempTextures_folder, 'walkRight', 'walkingR6.png')))
        self.walkRight.append(pygame.image.load(os.path.join(tempTextures_folder, 'walkRight', 'walkingR7.png')))
        # ... Add other images

        # Jump Right
        self.jumpRight.append(pygame.image.load(os.path.join(tempTextures_folder, 'jumpRight', 'jumpR1.png')))
        self.jumpRight.append(pygame.image.load(os.path.join(tempTextures_folder, 'jumpRight', 'jumpR2.png')))
        self.jumpRight.append(pygame.image.load(os.path.join(tempTextures_folder, 'jumpRight', 'jumpR3.png')))
        self.jumpRight.append(pygame.image.load(os.path.join(tempTextures_folder, 'jumpRight', 'jumpR4.png')))
        self.jumpRight.append(pygame.image.load(os.path.join(tempTextures_folder, 'jumpRight', 'jumpR5.png')))
        self.jumpRight.append(pygame.image.load(os.path.join(tempTextures_folder, 'jumpRight', 'jumpR6.png')))
        self.jumpRight.append(pygame.image.load(os.path.join(tempTextures_folder, 'jumpRight', 'jumpR7.png')))
        self.jumpRight.append(pygame.image.load(os.path.join(tempTextures_folder, 'jumpRight', 'jumpR8.png')))
        self.jumpRight.append(pygame.image.load(os.path.join(tempTextures_folder, 'jumpRight', 'jumpR9.png')))

        # Jump Left
        self.jumpLeft.append(pygame.image.load(os.path.join(tempTextures_folder, 'jumpLeft', 'jumpL1.png')))
        self.jumpLeft.append(pygame.image.load(os.path.join(tempTextures_folder, 'jumpLeft', 'jumpL2.png')))
        self.jumpLeft.append(pygame.image.load(os.path.join(tempTextures_folder, 'jumpLeft', 'jumpL3.png')))
        self.jumpLeft.append(pygame.image.load(os.path.join(tempTextures_folder, 'jumpLeft', 'jumpL4.png')))
        self.jumpLeft.append(pygame.image.load(os.path.join(tempTextures_folder, 'jumpLeft', 'jumpL5.png')))
        self.jumpLeft.append(pygame.image.load(os.path.join(tempTextures_folder, 'jumpLeft', 'jumpL6.png')))
        self.jumpLeft.append(pygame.image.load(os.path.join(tempTextures_folder, 'jumpLeft', 'jumpL7.png')))
        self.jumpLeft.append(pygame.image.load(os.path.join(tempTextures_folder, 'jumpLeft', 'jumpL8.png')))
        self.jumpLeft.append(pygame.image.load(os.path.join(tempTextures_folder, 'jumpLeft', 'jumpL9.png')))
    
    def death_respawn(self):
        self.lives -= 1
        self.pos = (50,50)

    def walk_right(self):
        self.curSprite += 0.1
        if self.curSprite >= len(self.walkRight):
            self.curSprite = 0
        self.image = self.walkRight[int(self.curSprite)]
    
    def stand_still(self):
        self.image = self.standingSprite[0]
        
        
    def walk_left(self):
        self.curSprite += 0.1
        if self.curSprite >= len(self.walkLeft):
            self.curSprite = 0
        self.image = self.walkLeft[int(self.curSprite)]
    def jump_left(self):
        for x in self.jumpLeft:
            self.image = x
    
    def jump_right(self):
        for x in self.jumpRight:
            self.image = x
    
    def duck(self):
        if self.direction == 0:
            self.image = self.duck[0]
        if self.direction == 1:
            self.image = self.duck[1]

    def move(self, ACC, FRIC, WIDTH, HEIGHT):
        self.acc = pygame.Vector2(0,0.5)
        if self.direction == 1:
            self.image = self.standingSprite[0]
        if self.direction == 0:
            self.image =self.standingSprite[1]
        pressed_keys = pygame.key.get_pressed()            
        if pressed_keys[pygame.K_a]:
            self.acc.x = -ACC
            self.direction = 0
            self.curSprite += 0.1
            if self.curSprite >= len(self.walkLeft):
                self.curSprite = 0
            self.image = self.walkLeft[int(self.curSprite)]
        if pressed_keys[pygame.K_d]:
            self.direction = 1
            self.acc.x = ACC
            self.curSprite += 0.1
            if self.curSprite >= len(self.walkRight):
                self.curSprite = 0
            self.image = self.walkRight[int(self.curSprite)]
        if pressed_keys[pygame.K_a] & pressed_keys[pygame.K_LSHIFT]:
            self.direction = 0
            self.acc.x = (-ACC)*2
        if pressed_keys[pygame.K_d] & pressed_keys[pygame.K_LSHIFT]:
            self.direction = 1
            self.acc.x = (ACC)*2
        if pressed_keys[pygame.K_s]:
            self.duck()
            self.acc.x = 0
        if pressed_keys[pygame.K_SPACE]:
            if self.is_jumping == False:
                self.is_jumping = True
                self.jump()
            if self.direction == 1:
                self.image = self.jumpRight[4]
            if self.direction == 0:
                self.image = self.jumpLeft[4]


        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        # Handle Player moviing off screen
        # *TEMPORARY* Need to create a longer level
        # And a window to follow the player

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        # self.hitbox.x = self.pos.x - 22  # Update hitbox x-coordinate
        # self.hitbox.y = self.pos.y - 15  # Update hitbox y-coordinate
           
        self.rect.midbottom = self.pos
    
    
        
    def jump(self):
        self.vel.y = -15
        self.curSprite += 0.1


    def handle_collision(self, elements, deathBox):
        hits = pygame.sprite.spritecollide(self, elements, False)
        dead = pygame.sprite.spritecollide(self, deathBox, False)
        if hits:
            for platform in hits:
                if self.vel.y > 0:  # If the player is moving downwards (falling)
                    self.pos.y = platform.rect.top + 1
                    self.vel.y = 0
                    self.is_jumping = False
                elif self.vel.y < 0:  # If the player is moving upwards (jumping)
                    self.pos.y = platform.rect.bottom + self.rect.height + 1
                    self.vel.y = 0
        if dead:
            self.death_respawn()
            
