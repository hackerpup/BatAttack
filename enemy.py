import pygame
import toolbox
import math
import random

# enemy class
class Enemy (pygame.sprite.Sprite):
    def __init__(self, screen, x, y, player):
        # enemy variables
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.x = 100
        self.y = 100
        self.screen = screen
        self.image = pygame.image.load("./assets/bat_up.png")
        self.image2 = pygame.image.load("./assets/bat_down.png")
        self.animation_timer_max = 16
        self.animation_timer = self.animation_timer_max
        self.animation_frame = 0
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.player = player
        self.angle = 0
        self.speed = 0.9
        

    def update(self, screen):
        self.animation_timer -= 1
        self.angle = toolbox.angleBetweenPoints(self.x, self.y, self.player.x, self.player.y)

        angle_rads = math.radians(self.angle)
        self.x_move = math.cos(angle_rads) * self.speed
        self.y_move = -math.sin(angle_rads) * self.speed
        new_x = self.x + self.x_move
        new_y = self.y + self.y_move
        self.x = new_x
        self.y = new_y
        self.rect.center = (self.x, self.y)
        self.screen.blit(self.image, self.rect)