import pygame
import sys

pygame.init()

size = [1280, 832]
screen = pygame.display.set_mode(size)

try:
    background = pygame.image.load('image/choose.png')  
    background = pygame.transform.scale(background, (1280, 832))
    
    elementPet = pygame.image.load('image/pet1.png')
    elementPet = pygame.transform.scale(elementPet, (100, 100))
    
     
    result_x = (1280 - 100) // 2   
    result_y = (832 - 100) // 2   

except pygame.error as e:
    print(f"펫 이미지를 불러올 수 없습니다: {e}")
    pygame.quit()
    sys.exit()

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 배경 이미지 그리기
    screen.blit(background, (0, 0))
    screen.blit(elementPet, (result_x, result_y))   #나중에 간격 수정 예정..
    pygame.display.update()

pygame.quit()
