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

run = True

while run:
    pygame.time.delay(10)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and player1y>=0:
        player1y-=speedy
    if keys[pygame.K_s] and player1y<=600:
        player1y+=speedy


    if keys[pygame.K_UP] and player2y>=0:
        player2y-=speedy
    if keys[pygame.K_DOWN] and player2y<=600:
        player2y+=speedy

    win.fill((0,0,0))
    pygame.draw.rect(win,(255,255,255),(player1x,player1y,width,height))
    pygame.draw.rect(win, (255, 255, 255), (player2x, player2y, width, height))
    pygame.draw.circle(win, (255, 0, 0), (ballx, bally),10)
    bally += ballSpeedy
    ballx += ballSpeedx
    if bally>=690:
        ballSpeedy=ballSpeedy*-1
    if bally<=10:
        ballSpeedy=ballSpeedy*-1

    if ballx>=player2x+10:
        ballSpeedx = ballSpeedx*-1



pygame.quit()
