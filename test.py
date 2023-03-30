import pg
import sys
import random

pg.init()

SKJERM_BREDDE, SKJERM_HOYDE = 800, 300
screen = pg.display.set_mode((SKJERM_BREDDE, SKJERM_HOYDE))
pg.display.set_caption("Dino Run")

clock = pg.time.Clock()

class Dino(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((40, 40))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 50, SKJERM_HOYDE - 40
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
            if self.rect.y < SKJERM_HOYDE - 40:
                self.rect.y += self.gravity
                self.gravity += 1
            else:
                self.gravity = 10

    def jump(self):
        if self.rect.y == SKJERM_HOYDE - 40:
            self.is_jumping = True



class Obstacle(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((40, 40))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = SKJERM_BREDDE, SKJERM_HOYDE - 40

    def update(self):
        self.rect.x -= 5

player = Dino()
obstacles = pg.sprite.Group()
sprites = pg.sprite.Group()
sprites.add(player)

while True:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.jump()

    if random.randint(1, 100) <= 2:
        obstacle = Obstacle()
        obstacles.add(obstacle)
        sprites.add(obstacle)

    sprites.update()
    screen.fill((0, 0, 0))
    sprites.draw(screen)

    if pg.sprite.spritecollideany(player, obstacles):
        pg.quit()
        sys.exit()

    pg.display.flip()
