import pygame
vec = pygame.Vector2
class Player(pygame.sprite.Sprite):
    
    
    def __init__(self, pos):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.direction = 0
        self.pos = pos
        self.vel = pygame.Vector2(0,0)
        self.acc = pygame.Vector2(0,0)
        self.is_jumping = False
        
        self.standingSprite = []
        self.standingSprite.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\standing\\standing1.png'))
        self.standingSprite.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\standing\\standing2.png'))
        
        self.walkLeft = []
        self.walkLeft.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\walkLeft\\walkingL1.png'))
        self.walkLeft.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\walkLeft\\walkingL2.png'))
        self.walkLeft.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\walkLeft\\walkingL3.png'))
        self.walkLeft.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\walkLeft\\walkingL4.png'))
        self.walkLeft.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\walkLeft\\walkingL5.png'))
        self.walkLeft.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\walkLeft\\walkingL6.png'))
        self.walkLeft.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\walkLeft\\walkingL7.png'))
        
        self.walkRight = []
        self.walkRight.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\walkRight\\walkingR1.png'))
        self.walkRight.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\walkRight\\walkingR2.png'))
        self.walkRight.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\walkRight\\walkingR3.png'))
        self.walkRight.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\walkRight\\walkingR4.png'))
        self.walkRight.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\walkRight\\walkingR5.png'))
        self.walkRight.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\walkRight\\walkingR6.png'))
        self.walkRight.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\walkRight\\walkingR7.png'))
        
        self.jumpRight = []
        self.jumpRight.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\jumpRight\\jumpR1.png'))
        self.jumpRight.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\jumpRight\\jumpR2.png'))
        self.jumpRight.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\jumpRight\\jumpR3.png'))
        self.jumpRight.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\jumpRight\\jumpR4.png'))
        self.jumpRight.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\jumpRight\\jumpR5.png'))
        self.jumpRight.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\jumpRight\\jumpR6.png'))
        self.jumpRight.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\jumpRight\\jumpR7.png'))
        self.jumpRight.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\jumpRight\\jumpR8.png'))
        self.jumpRight.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\jumpRight\\jumpR9.png'))
        
        self.jumpLeft = []
        self.jumpLeft.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\jumpLeft\\jumpL1.png'))
        self.jumpLeft.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\jumpLeft\\jumpL2.png'))
        self.jumpLeft.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\jumpLeft\\jumpL3.png'))
        self.jumpLeft.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\jumpLeft\\jumpL4.png'))
        self.jumpLeft.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\jumpLeft\\jumpL5.png'))
        self.jumpLeft.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\jumpLeft\\jumpL6.png'))
        self.jumpLeft.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\jumpLeft\\jumpL7.png'))
        self.jumpLeft.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\jumpLeft\\jumpL8.png'))
        self.jumpLeft.append(pygame.image.load('D:\\HOME\\PERSONAL\\CODING\\Stickman\\Stickman\\player\\tempTextures\\jumpLeft\\jumpL9.png'))
        
        self.curSprite = 0
        self.image = self.standingSprite[self.curSprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        
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
    
    def move(self, ACC, FRIC, WIDTH):
        
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
        if pressed_keys[pygame.K_SPACE]:
            if self.is_jumping == False:
                self.is_jumping = True
                self.jump()
        if self.is_jumping:
            if self.direction == 1:   
                self.image = self.jumpRight[4]
            if self.direction == 0:
                self.image = self.jumpLeft[4]
            
                                
                                
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        # self.hitbox.x = self.pos.x - 22  # Update hitbox x-coordinate
        # self.hitbox.y = self.pos.y - 15  # Update hitbox y-coordinate
           
        self.rect.midbottom = self.pos
    
    
        
    def jump(self):
        self.vel.y = -15
        
    def handle_collision(self, elements):
        hits = pygame.sprite.spritecollide(self, elements, False)
        if hits:
            self.is_jumping = False
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0
            
        
        
