import pygame
import random
from enemy import Enemy
from player import Player

# Start the game
pygame.init()
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True

enemy_spawn_timer_max = 100
enemy_spawn_timer = enemy_spawn_timer_max

# load all the pics for our game
background_pic = pygame.image.load("./assets/Cave2.jpg")
enemy_pic = pygame.image.load("./assets/bat_up.png")

mr_player = Player(screen, 0, 0)

playerGroup = pygame.sprite.Group()
enemiesGroup = pygame.sprite.Group()

Player.containers = playerGroup
Enemy.containers = enemiesGroup

game_started = False

def StartGame():
    global game_started
    global mr_player
    
    game_started = True
    mr_player.__init__(screen, game_width/2, game_height/2)


##################### Loop ###########################################################
while running:
    # Makes the game stop if the player clicks the X or presses esc
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
        if game_started:
            # deal with player input
            keys = pygame.key.get_pressed()
            if pygame.mouse.get_pressed()[0]:
                mr_player.shoot()
        screen.blit(background_pic,(0, 0))
        #screen.blit(enemy_pic,(100, 100))
        if not game_started:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    StartGame()
                    break
        


        # Make enemy spawn happen
        enemy_spawn_timer -= 1
        if enemy_spawn_timer <= 0:
            new_enemy = Enemy(screen, 0, 0, mr_player)
            side_to_spawn = 0 #random.randint(0, 3) # 0=top, 1=bottom, 2=left, 3=right
            if side_to_spawn == 0:
                new_enemy.x = random.randint(0, game_width)
                new_enemy.y = -new_enemy.image.get_height()
            elif side_to_spawn == 1:
                new_enemy.x = random.randint(0, game_width)
                new_enemy.y = game_height + new_enemy.image.get_height()
            elif side_to_spawn == 2:
                new_enemy.x = -new_enemy.image.get_width()
                new_enemy.y = random.randint(0, game_height)
            elif side_to_spawn == 3:
                new_enemy.x = game_width + new_enemy.image.get_width()
                new_enemy.y = random.randint(0, game_height)
            enemy_spawn_timer = enemy_spawn_timer_max

        mr_player.update(screen)
        
        for enemy in enemiesGroup:
            enemy.update(screen)
        # Tell pygame to update the screen
        pygame.display.flip()
        clock.tick(50)
        pygame.display.set_caption("MY GAME fps: " + str(clock.get_fps()))


