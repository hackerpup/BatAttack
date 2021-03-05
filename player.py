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
        self.angle = 0 
        self.shoot_cooldown = 0
        self.shoot_cooldown_max = 10
    
    def update(self, enemies):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        if self.alive:
            pic_to_rotate = self.pic
            # get angle btwn plyr and mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.angle = toolbox.angleBetweenPoints(self.x, self.y, mouse_x, mouse_y)
            pic_to_draw, pic_rect = toolbox.getRotatedImage(pic_to_rotate, self.rect, self.angle)
            self.screen.blit(pic_to_draw, pic_rect)

    def shoot(self):
        if self.shoot_cooldown <= 0 and self.alive:
            CannonBall(self.screen, self.x, self.y, self.angle)

    def move(self, x_movement, y_movement, crates):
        if self.alive:
            # make sure player doesnt run into crate
            test_rect = self.rect
            test_rect.x += self.speed * x_movement
            test_rect.y += self.speed * y_movement
            collision = False
            for crate in crates:
                if not crate.just_placed:
                    if test_rect.colliderect(crate.rect):
                        collision = True

            if not collision:
                self.x += self.speed * x_movement
                self.y += self.speed * y_movement

