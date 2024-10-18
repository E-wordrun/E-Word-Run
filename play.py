import pygame
import sys

pygame.init()

size = [1280, 832]
screen = pygame.display.set_mode(size)

try:
    background = pygame.image.load('image/background.png')  
    background = pygame.transform.scale(background, (1280, 832))
   
except pygame.error as e:
    pygame.quit()
    sys.exit()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    screen.blit(background, (0, 0))
    pygame.display.update()

 
pygame.quit()
