import pygame
from projectile import Laser

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        self.x = 450
        self.y = 510
        self.pic = pygame.image.load("./assets/cannon.png")
        self.rect = self.pic.get_rect()
        self.rect.center = (self.x, self.y)
        self.alive = True
        self.speed = 8
        self.angle = 0
        self.shoot_cooldown = 0
        self.shoot_cooldown_max = 10
    
    def update(self, enemies):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        if self.alive:
            # get angle btwn plyr and mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.angle = toolbox.angleBetweenPoints(self.x, self.y, mouse_x, mouse_y)

    def shoot():
        self.screen.blit(self.pic, self.rect)