import pygame as pg
import sys
import random

pg.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 920, 600
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Hoppe Spill")

clock = pg.time.Clock()

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((40, 40))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 50, SCREEN_HEIGHT - 40
        self.jump_height = 20
        self.is_jumping = False
        self.gravity = 10

    def update(self):
        if self.is_jumping:
            self.rect.y -= self.jump_height
            self.jump_height -= 1
            if self.jump_height < -20:
                self.is_jumping = False
                self.jump_height = 20
        else:
            if self.rect.y < SCREEN_HEIGHT - 40:
                self.rect.y += self.gravity
                self.gravity += 1
            else:
                self.gravity = 10

    def jump(self):
        if self.rect.y == SCREEN_HEIGHT - 40:
            self.is_jumping = True



class Obstacle(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((40, 40))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = SCREEN_WIDTH, SCREEN_HEIGHT - 40

    def update(self):
        self.rect.x -= 10

player = Player()
obstacles = pg.sprite.Group()
sprites = pg.sprite.Group()
sprites.add(player)

font = pg.font.Font(None, 36)

score = 0
score_timer = pg.time.get_ticks()

def draw_text(screen, text, font, color=(255, 0, 0)):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    screen.blit(text_surface, text_rect)


obstacle_counter = 0
min_space_between_obstacles = 30  # You can adjust this value to control the space between obstacles

while True:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.jump()

    if obstacle_counter >= min_space_between_obstacles:
        if random.randint(1, 100) <= 1:
            obstacle = Obstacle()
            obstacles.add(obstacle)
            sprites.add(obstacle)
            obstacle_counter = 0  # Reset the counter when an obstacle is spawned
    else:
        obstacle_counter += 1

    sprites.update()
    screen.fill((0, 0, 0))
    sprites.draw(screen)

    current_time = pg.time.get_ticks()
    if current_time - score_timer >= 1000:  # Check if 1 second (1000 ms) has passed
        score += 1
        score_timer = current_time

    text = f"Distanse: {score}"
    draw_text(screen, text, font)

    if pg.sprite.spritecollideany(player, obstacles):
        pg.quit()
        sys.exit()

    pg.display.flip()

