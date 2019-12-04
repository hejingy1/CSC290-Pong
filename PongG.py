import pygame

pygame.init()

win = pygame.display.set_mode((1300,700))

pygame.display.set_caption("Pong")
player1x = 0
player1y = 300
player2x = 1295
player2y = 300
player1 = 0
player2 = 0
ballx = 650
bally = 150
ballSpeedy = 5
ballSpeedx = 5
width = 5
height = 100
speedy = 5
vel = 5
gamestart = True
gameend = False

run = True

while run:

    pygame.time.delay(10)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and player1y>=0 and gameend==False:
        player1y-=speedy
    if keys[pygame.K_s] and player1y<=600 and gameend==False:
        player1y+=speedy

    if keys[pygame.K_r] and player1y<=600 and gameend==False:
        pygame.time.wait(1000)

    if keys[pygame.K_UP] and player2y>=0 and gameend==False:
        player2y-=speedy
    if keys[pygame.K_DOWN] and player2y<=600 and gameend==False:
        player2y+=speedy

    win.fill((0,0,0))

    myfont = pygame.font.SysFont("monospace", 70)
    label = myfont.render(str(player1), 1, (255, 255, 0))
    win.blit(label, (100, 100))

    myfont = pygame.font.SysFont("monospace", 70)
    label = myfont.render(str(player2), 1, (255, 255, 0))
    win.blit(label, (1200, 100))

    pygame.draw.line(win, (255,0,0), (650,0),(650,700),5)
    pygame.draw.rect(win,(255,255,255),(player1x,player1y,width,height))
    pygame.draw.rect(win, (255, 255, 255), (player2x, player2y, width, height))
    pygame.draw.circle(win, (255, 0, 0), (ballx, bally),10)
    bally += ballSpeedy
    ballx += ballSpeedx
    if bally>=690:
        ballSpeedy=ballSpeedy*-1
    if bally<=10:
        ballSpeedy=ballSpeedy*-1

    if ballx>player2x-15 and ballx<player2x+5 and bally>player2y and bally<player2y+100:
        ballSpeedx = ballSpeedx*-1

    if ballx<15 and ballx>-5 and bally>player1y and bally<player1y+100:
        ballSpeedx = ballSpeedx*-1

    if ballx<-10:
        player2=player2+1
        ballx = 650
        bally = 350
        ballSpeedx = ballSpeedx * -1
    if ballx>1350:
        player1=player1+1
        ballx = 650
        bally = 350
        ballSpeedx = ballSpeedx * -1

    if(gameend):
        ballSpeedx = 0
        ballSpeedy = 0
        myfont = pygame.font.SysFont("monospace", 50)
        label = myfont.render("Game over(Press Space to restart)", 1, (255, 255, 0))
        win.blit(label, (200, 100))
        if keys[pygame.K_SPACE]:
            player1 = 0
            player2 = 0
            gameend = False
            ballSpeedy = 5
            ballSpeedx = 5


    if(player1==5):
        gameend = True
    if(player2 == 5):
        gameend = True

pygame.quit()
