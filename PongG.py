import pygame
pygame.init()

win = pygame.display.set_mode((1300,700))

pygame.display.set_caption("Pong")

player1x = 0
player1y = 300
player2x = 1280
player2y = 300
ballx = 650
bally = 350
ballSpeedy = 3
ballSpeedx = 3
width = 20
height = 100
speedy = 5
vel = 5


screen_h = 500
screen_w = 700


run = True


#class of setups
class design():
    def __init__():
        
    def screen():
        #screen size
        d_w = 700
        d_h = 500
        
        #setup the color
        w = (200, 200, 200)
        b = (0, 0, 0)
        #brighter color
        b_w = (255, 255, 255)

        #setup the starting screen
        screen = pygame.display.set_mode([d_w, d_h])
        screen.fill(b)
        game.display.set_caption('Pong')

        #setup the buttons
        mouse = pygame.mouse.get_pos()
        if d_w / 2 < mouse[0] < d_w / 2 + 100 and d_h - 100 < mouse[1] < d_h - 75:
            pygame.draw.rect(gameDisplay, s_w, (d_w / 2, d_h - 100, 100, 25))
        else:
            pygame.draw.rect(gameDisplay, w, (d_w / 2, d_h - 100, 100, 25))
        if d_w / 2 < mouse[0] < d_w / 2 + 100 and d_h - 250 < mouse[1] < d_h - 225:
            pygame.draw.rect(gameDisplay, s_w, (d_w / 2, d_h - 100, 100, 25))
        else:
            pygame.draw.rect(gameDisplay, w, (d_w / 2, d_h - 100, 100, 25))
        font = pygame.font.Font('freesansbold.ttf', 50)


class Paddle:

    """A paddle for Pong.

    === Attributes ===
    key1: either pygame.K_UP or pygame.K_w
    key2: either pygame.K_DOWN or pygame.K_s
    speed: speed of this paddle
    x_loc: the x coordinate of this paddle
    y_loc: the y coordinate of this paddle
    w: width of this paddle
    h: height of this paddle

    """

    paddle_w = 10
    paddle_h = 100

    def __init__(self, key1, key2):
        """Creates a paddle
        """
        self.key1 = key1
        self.key2 = key2
        self.speed = 5
        self.x_loc = screen_w - paddle_w
        self.y_loc = screen_h/2 - paddle_h/2
        self.w = paddle_w
        self.h = paddle_h

    def move(self):
        """Moves the paddle
        """
        if pygame.key.get_pressed()[self.key1]:  # up/w key
            if self.y_loc - self.speed > 0:
                self.y_loc -= self.speed

        elif pygame.key.get_pressed()[self.key2]:  # down/s key
            if self.y_loc + self.speed < screen_h - self.h:
                self.y_loc += self.speed

class Ball:

    """A paddle for Pong.

    === Attributes ===
    key1: either pygame.K_UP or pygame.K_w
    key2: either pygame.K_DOWN or pygame.K_s
    speed: speed of this paddle
    x_loc: the x coordinate of this paddle
    y_loc: the y coordinate of this paddle
    w: width of this paddle
    h: height of this paddle

    """

    def __init__(self):
        """Creates a ball
        """
        self.xcoor = 650
        self.ycoor = 350
        self.speed = 1

    def move(self, xdir, ydir):
        """Moves the ball
        """
        self.xcoor += self.speed * xdir
        self.ycoor += self.speed * ydir


while run:
    pygame.time.delay(10)
    pygame.display.update()
    #keeping the loop running until the game is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    #trying out different value to put into the code
    #test different case and demonstrate how the game will be hehave like
    #codes that helps teammates to build their individual class
    if keys[pygame.K_w] and player1y>=0:
        player1y-=speedy
    if keys[pygame.K_s] and player1y<=600:
        player1y+=speedy


    if keys[pygame.K_UP] and player2y>=0:
        player2y-=speedy
    if keys[pygame.K_DOWN] and player2y<=600:
        player2y+=speedy

    win.fill((0,0,0))
    #construct the all three objects that can be use
    pygame.draw.rect(win,(255,255,255),(player1x,player1y,width,height))
    pygame.draw.rect(win, (255, 255, 255), (player2x, player2y, width, height))
    pygame.draw.circle(win, (255, 0, 0), (ballx, bally),10)
    bally += ballSpeedy
    ballx += ballSpeedx
    #testing boundaries
    if bally>=690:
        ballSpeedy=ballSpeedy*-1
    if bally<=10:
        ballSpeedy=ballSpeedy*-1

    if ballx>=player2x+10:
        ballSpeedx = ballSpeedx*-1



pygame.quit()
