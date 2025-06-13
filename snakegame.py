import pygame
import random

print("hello world")
pygame.init()
color = (0,0,0)

snakeColor = (0,255,0)
state = 'r'
x = 250
y = 250
body = [(x,y)]

appleColor = (255,0,0)
appleX = random.choice(range(0, 476, 25))
appleY = random.choice(range(0, 476, 25))

canvas = pygame.display.set_mode((500,500))

pygame.display.set_caption("Snake")

exit = False
while not exit: 
    canvas.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if(state != 'l' and state != 'r'):
            state = 'l'
        
    if keys[pygame.K_RIGHT]:
        if(state != 'r' and state != 'l'):
            state = 'r'
    if keys[pygame.K_UP]:
        if(state != 'u' and state != 'd'):
            state = 'u'
    if keys[pygame.K_DOWN]:
        if(state != 'd' and state != 'u'):
            state = 'd'

    if(state == 'u' and state != 'd'):
        y = y - 25
    elif(state == 'd' and state != 'u'):
        y = y + 25
    elif(state == 'r' and state != 'l'):
        x = x + 25
    elif(state == 'l' and state != 'r'):
        x = x - 25

    apple = pygame.Rect(appleX, appleY, 25, 25)
    pygame.draw.rect(canvas, appleColor, pygame.Rect(appleX, appleY, 25, 25))

    snake = pygame.Rect(x, y, 25, 25)
    for segment in body:
        pygame.draw.rect(canvas, snakeColor, pygame.Rect(segment[0], segment[1], 25, 25))

    nh = (x,y)
    body.append(nh)

    if snake.colliderect(apple):
        appleX = random.choice(range(0, 476, 25))
        appleY = random.choice(range(0, 476, 25))
    else:
        body.pop(0)

    pygame.display.update()
    pygame.time.Clock().tick(10)
