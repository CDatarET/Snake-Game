import pygame 

print("hello world")  
pygame.init()
color = (0,0,0)
rectColor = (0,255,0) 

canvas = pygame.display.set_mode((500,500)) 

pygame.display.set_caption("Snake") 

exit = False
  
while not exit: 
    canvas.fill(color)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
  
    pygame.draw.rect(canvas, rectColor, pygame.Rect(250,250,20,20)) 
    pygame.display.update() 