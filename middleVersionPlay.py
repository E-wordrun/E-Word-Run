import pygame
import sys

pygame.init()

size = [1280, 832]
screen = pygame.display.set_mode(size)

try:
    background = pygame.image.load('image/background.png')  
    background = pygame.transform.scale(background, (1280, 832))
    
    scoreBox = pygame.image.load('image/scorebox.png')
    scoreBox = pygame.transform.scale(scoreBox, (291, 119))
    
    coin = pygame.image.load('image/coin.png')
    coin = pygame.transform.scale(coin, (50, 57))
    
    pet1 = pygame.image.load('image/pet1.png')
    pet1 = pygame.transform.scale(pet1, (90, 92))
    
    pet1 = pygame.image.load('image/pet1.png')
    pet1 = pygame.transform.scale(pet1, (90, 92))
    
    pet1 = pygame.image.load('image/pet1.png')
    pet1 = pygame.transform.scale(pet1, (90, 92))
    
    
    character = pygame.image.load('image/character.gif')
    character = pygame.transform.scale(character, (350, 352))
   
except pygame.error as e:
    pygame.quit()
    sys.exit()

# 캐릭터의 초기 위치
character_x = 5
character_y = 387
character_speed = 5  # 이동 속도

# pet1의 상대적인 위치 (캐릭터 바로 왼쪽에 위치)
pet1_offset_x = pet1.get_width()  # pet1의 너비만큼 왼쪽으로 이동
pet1_offset_y = 0   # y축은 동일하게 유지

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키보드 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  # 왼쪽 방향키
        character_x -= character_speed
    if keys[pygame.K_RIGHT]:  
        character_x += character_speed
    if keys[pygame.K_UP]:   
        character_y -= character_speed
    if keys[pygame.K_DOWN]:  
        character_y += character_speed

    screen.blit(background, (0, 0))
    screen.blit(scoreBox, (910, 20))
    screen.blit(coin, (970, 40))
    
    screen.blit(pet1, (character_x + pet1_offset_x - 50, character_y + pet1_offset_y + 130))  
    screen.blit(character, (character_x, character_y))   
    pygame.display.update()

pygame.quit()
