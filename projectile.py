import pygame
import toolbox
import math
#from explosion import Explosion

class CannonBall(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, angle):
        self.screen = screen
        self.x = x
        self.y = y
        self.angle = angle
        self.image = pygame.image.load("./assets/cannonball.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.image, self.rect = toolbox.getRotatedImage(self.image, self.rect, self.angle)
        self.speed = 10
        self.angle_rads = math.radians(self.angle)
        self.x_move = math.cos(self.angle_rads) * self.speed
        self.y_move = -math.sin(self.angle_rads) * self.speed
        self.damage = 6
        

    def update(self):
        self.x += self.x_move
        self.y += self.y_move
        self.rect.center = (self.x, self.y)

        # despawn balloons
        if self.x < -self.image.get_width():
            self.kill()
        elif self.x > self.screen.get_width() + self.image.get_width():
            self.kill()
        elif self.y < -self.image.get_height():
            self.kill()
        elif self.y > self.screen.get_height() + self.image.get_height():
            self.kill()

            
        self.screen.blit(self.image, self.rect)

