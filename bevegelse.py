# Example file showing a circle moving on screen
import pg

# pg setup
pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = True

player_x = 50
player_y = 100

while running:
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pg.draw.circle(screen, "red", (player_x, player_y), 40)

    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        player_y -= 300 * dt
    if keys[pg.K_DOWN]:
        player_y += 300 * dt
    if keys[pg.K_LEFT]:
        player_x -= 300 * dt
    if keys[pg.K_RIGHT]:
        player_x += 300 * dt

    # flip() the display to put your work on screen
    pg.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pg.quit()