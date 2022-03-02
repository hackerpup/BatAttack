import pygame
import toolbox
from enemy import Enemy
from projectile import CannonBall

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        self.x = 450
        self.y = 510
        self.screen = screen
        self.pic = pygame.image.load("./assets/cannon.png")
        self.rect = self.pic.get_rect()
        self.rect.center = (self.x, self.y)
        self.alive = True
        self.speed = 8
        self.speed_x = 8
        self.speed_y = 8
        self.angle = 0
        self.shoot_cooldown = 0
        self.shoot_cooldown_max = 10
        self.score = 0
    
    def update(self, enemies):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1


        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen.get_width():
            self.rect.right = self.screen.get_width()
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen.get_height():
            self.rect.bottom = self.screen.get_height()
        #self.x = self.rect.centerx
        #self.y = self.rect.centery

        if self.alive:
            
            # get angle btwn plyr and mouse
            pic_to_rotate = self.pic
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.angle = toolbox.angleBetweenPoints(self.x, self.y, mouse_x, mouse_y)
            
            pic_to_draw, pic_rect = toolbox.getRotatedImage(pic_to_rotate, self.rect, self.angle-90)
            self.screen.blit(pic_to_draw, pic_rect)  # its the line below that causes a few problems
            



    def shoot(self):
        if self.shoot_cooldown <= 0 and self.alive:
            CannonBall(self.screen, self.x, self.y, self.angle)

        self.shoot_cooldown = self.shoot_cooldown_max

    def move(self, x_movement, y_movement):
        if self.alive:
            # make sure player doesnt run into crate

            #if not collision:
            self.x += self.speed * x_movement
            self.y += self.speed * y_movement


    def getScore(self, score):
        if self.alive:
            self.score += score
