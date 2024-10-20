import pygame
import sys

pygame.init()

size = [1280, 832]
screen = pygame.display.set_mode(size)

try:
    background = pygame.image.load('image/blur-background.png')  
    background = pygame.transform.scale(background, (1280, 832))
    
    resultBackground = pygame.image.load('image/result.png')
    resultBackground = pygame.transform.scale(resultBackground, (608, 551))  
    
    homeButton = pygame.image.load('image/homebutton.png')
    homeButton = pygame.transform.scale(homeButton, (45, 45))
    
    # 가운데로 가져오기
    result_x = (1280 - 718) // 2 + 60
    result_y = (832 - 667) // 2 +50

except pygame.error as e:
    print(f"이미지를 불러올 수 없습니다: {e}")
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
    screen.blit(resultBackground, (result_x, result_y))
    screen.blit(homeButton, (22,20) )
    pygame.display.update()

# Pygame 종료
pygame.quit()
