# Example file showing a basic pg "game loop"
import pygame as pg

# pg setup
pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = True

class Figur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Spiller(Figur):
    def __init__(self, x, y, fartY):
        super().__init__(x, y)
        self.fartY = fartY
    
    def hopp(self):
        pass

    def fall(self):
        pass

    def er_over_hinder(self):
        pass

    def tegn(self):
        pg.draw.circle(screen, (0, 255, 0), [self.x, self.y], 30, 0)


class Hinder(Figur):
    def __init__(self, x, y, fartX):
        super().__init__(x, y)
        self.fartX = fartX
    
    def tegn(self):
        pass

while running:
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # LAG SPILLET DITT HER:

    spiller = Spiller(640,720 ,100)
    spiller.tegn()

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()