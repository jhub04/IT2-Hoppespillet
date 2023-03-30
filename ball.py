import pg
pg.init()
clock = pg.time.Clock()


width = 320
height = 240
speedX = 2
speedY = 2
black = (0, 0, 0)
running = True

screen = pg.display.set_mode((width, height))

ball = pg.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    ballrect = ballrect.move((speedX,speedY))
    if ballrect.left < 0 or ballrect.right > width:
        speedX = -speedX
    if ballrect.top < 0 or ballrect.bottom > height:
        speedY = -speedY

    screen.fill(black)
    screen.blit(ball, ballrect)
    

    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()