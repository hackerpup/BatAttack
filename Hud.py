import pygame
import toolbox

class HUD():
    def __init__(self, screen, player):
            self.screen = screen
            self.player = player

            self.state = 'ingame'
            

            self.hud_font = pygame.font. SysFont("default", 30)
            self.hud_font_med = pygame.font.SysFont("default", 50)
            self.hud_font_big = pygame.font.SysFont("default", 80)

            self.score_text = self.hud_font.render("Beep boop", True, (255, 255, 255))



    def update(self):
        if self.state == 'ingame':
            # draw score text
            self.score_text = self.hud_font.render("Score: " + str(self.player.score), True, (255, 255, 255))
            self.screen.blit(self.score_text, (10, 10))
