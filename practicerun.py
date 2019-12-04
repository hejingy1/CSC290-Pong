import pygame

pygame.init()

# win = pygame.display.set_mode((1300, 700))

pygame.display.set_caption("Pong")


ballx = 650
bally = 350
ballSpeedy = 3
ballSpeedx = 3
width = 20
height = 100
speedy = 5


screen_h = 500
screen_w = 700

run = True


# class of setups
class Design:
    def __init__(self):
        pass

    def screen(self):
        # screen size
        d_w = 700
        d_h = 500

        # setup the color
        w = (200, 200, 200)
        b = (0, 0, 0)
        # brighter color
        b_w = (255, 255, 255)

        # setup the starting screen
        screen = pygame.display.set_mode([d_w, d_h])
        screen.fill(b)
        game.display.set_caption('Pong')

        # setup the buttons
        mouse = pygame.mouse.get_pos()
        if d_w / 2 < mouse[0] < d_w / 2 + 100 and d_h - 100 < mouse[
            1] < d_h - 75:
            pygame.draw.rect(gameDisplay, s_w, (d_w / 2, d_h - 100, 100, 25))
        else:
            pygame.draw.rect(gameDisplay, w, (d_w / 2, d_h - 100, 100, 25))
        if d_w / 2 < mouse[0] < d_w / 2 + 100 and d_h - 250 < mouse[
            1] < d_h - 225:
            pygame.draw.rect(gameDisplay, s_w, (d_w / 2, d_h - 100, 100, 25))
        else:
            pygame.draw.rect(gameDisplay, w, (d_w / 2, d_h - 100, 100, 25))
        font = pygame.font.Font('freesansbold.ttf', 50)


class Paddle():
    """A paddle for Pong.

    === Attributes ===
    key1: either pygame.K_UP or pygame.K_w
    key2: either pygame.K_DOWN or pygame.K_s
    x: the x coordinate of this paddle
    y: the y coordinate of this paddle
    """

    def __init__(self, key1, key2, xpos, ypos):
        """Creates a paddle
        """
        self.key1 = key1
        self.key2 = key2
        self.x = xpos
        self.y = ypos

    def move(self):
        """
        Moves the paddle up or down.

        """
        key = pygame.key.get_pressed()

        if key[self.key1] and self.y >= 0:
            self.y -= speedy

        if key[self.key2] and self.y <= 400:
            self.y += speedy


class Ball:
    """A ball for Pong.

    === Attributes ===
    speed: speed of this ball
    xcoor: the x coordinate of this ball
    ycoor: the y coordinate of this ball

    """

    def __init__(self):
        """Creates a ball
        """
        self.xcoor = 250
        self.ycoor = 350
        self.speed = 1

    def move(self, xdir, ydir):
        """Moves the ball
        """
        self.xcoor += self.speed * xdir
        self.ycoor += self.speed * ydir


win = pygame.display.set_mode((700, 500))
run = True
player1 = Paddle(pygame.K_w, pygame.K_s, 0, 300)
player2 = Paddle(pygame.K_UP, pygame.K_DOWN, 680, 300)

while run:
    pygame.time.delay(10)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] or keys[pygame.K_s]:
        player1.move()

    if keys[pygame.K_UP] or keys[pygame.K_DOWN]:
        player2.move()

    win.fill((0, 0, 0))
    # construct the all three objects that can be use
    pygame.draw.rect(win, (255, 255, 255), (player1.x, player1.y, width, height))
    pygame.draw.rect(win, (255, 255, 255), (player2.x, player2.y, width, height))
    pygame.draw.circle(win, (255, 0, 0), (ballx, bally), 10)

pygame.quit()
