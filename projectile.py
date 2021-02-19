import pygame
import toolbox
import math
#from explosion import Explosion

class Laser(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, angle):
        self.screen = screen
        self.x = x
        self.y = y
        self.angle = angle
        self.image = pygame.image.load("./assets/laser.png")
