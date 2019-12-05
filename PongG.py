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


# class of setups
class Design():
    def __init__(self):
        # setup the screen
        self.width = 700
        self.height = 500
        self.white = (100, 100, 100)
        self.black = (0, 0, 0)
        self.bright_white = (255, 255, 255)
        self.gold = (255, 255, 0)
        self.starting_screen()

    def starting_screen(self):
        # setup the starting screen
        playing = True
        while playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
            screen = pygame.display.set_mode([self.width, self.height], pygame.HWSURFACE | pygame.DOUBLEBUF)
            screen.fill(self.black)
            pygame.display.set_caption('Pong')
            font = pygame.font.Font("freesansbold.ttf", 120)
            game_name = font.render("PONG", True, self.gold)
            screen.blit(game_name, [180, 100])

            #setup the buttons
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            font = pygame.font.Font("freesansbold.ttf", 50)
            play = font.render("Play", True, self.black)
            quit = font.render("Quit", True, self.black)

            if self.width - 400 < mouse[0] < self.width - 290 and self.height - 100 < mouse[1] < self.height - 50:
                a = pygame.draw.rect(screen, self.bright_white, [self.width - 400, self.height - 100, 110, 50])
                screen.blit(quit, a)
                if click[0] == 1:
                    pygame.quit()
            else:
                b = pygame.draw.rect(screen, self.white, [self.width - 400, self.height - 100, 110, 50])
                screen.blit(quit, b)
            if self.width - 400 < mouse[0] < self.width - 290 and self.height - 180 < mouse[1] < self.height - 130:
                c = pygame.draw.rect(screen, self.bright_white, [self.width - 400, self.height - 180, 110, 50])
                screen.blit(play, c)
                if click[0] == 1:
                    playing = False
            else:
                d = pygame.draw.rect(screen, self.white, [self.width - 400, self.height - 180, 110, 50])
                screen.blit(play, d)

            font = pygame.font.Font("freesansbold.ttf", 30)
            helper = font.render("?", True, self.gold)
            message1 = "Player 1: Arrow keys"
            message2 = "Player 2: W and S keys"
            message3 = "Get 5 points to win"
            message4 = "Good Luck!"
            screen.blit(helper, [self.width - 270, self.height - 165])

            if self.width - 270 < mouse[0] < self.width - 250 and self.height - 165 < mouse[1] < self.height - 135:
                pygame.draw.rect(screen, self.white, [150, 50, 400, 300])
                help_message1 = font.render(message1, True, self.black)
                help_message2 = font.render(message2, True, self.black)
                help_message3 = font.render(message3, True, self.black)
                help_message4 = font.render(message4, True, self.black)
                screen.blit(help_message1, [155, 60])
                screen.blit(help_message2, [155, 140])
                screen.blit(help_message3, [155, 220])
                screen.blit(help_message4, [155, 300])
            pygame.display.update()
            
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
        key = pygame.key.get_pressed()

        if key[self.key1] and self.y >= 0:
            self.y -= speedy

        if key[self.key2] and self.y <= 500:
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
        self.xcoor = 650
        self.ycoor = 350
        self.speed = 1

    def move(self, xdir, ydir):
        """Moves the ball
        """
        self.xcoor += self.speed * xdir
        self.ycoor += self.speed * ydir


#win = pygame.display.set_mode((700, 500))
selecting = Design()
player1 = Paddle(pygame.K_w, pygame.K_s, 0, 300)
player2 = Paddle(pygame.K_UP, pygame.K_DOWN, 680, 300)

run = True

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
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] or keys[pygame.K_s]:
        player1.move()

    if keys[pygame.K_UP] or keys[pygame.K_DOWN]:
        player2.move()

    win.fill((0, 0, 0))
    # construct the all three objects that can be use
    pygame.draw.rect(win, (255, 255, 255),
                     (player1.x, player1.y, width, height))
    pygame.draw.rect(win, (255, 255, 255),
                     (player2.x, player2.y, width, height))

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

