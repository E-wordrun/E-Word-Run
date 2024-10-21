import pygame
import sys

pygame.init()

# 화면 크기 설정
size = [1280, 832]
screen = pygame.display.set_mode(size)

# 초기 상태는 'main' 화면
current_screen = 'main'

# 이미지 로드
def load_images():
    try:
        background = pygame.image.load('image/start_background.png')
        background = pygame.transform.scale(background, (1280, 832))
        play = pygame.image.load('image/play-button.png')
        play = pygame.transform.scale(play, (285, 183))
    except pygame.error as e:
        print(f"이미지를 불러올 수 없습니다: {e}")
        pygame.quit()
        sys.exit()
    return background, play

background, play = load_images()

# 버튼 좌표 및 크기 설정
play_rect = play.get_rect()
play_rect.center = (size[0]//2, size[1]//2+50)

# 펫 선택 화면 함수 (choosePet.py의 내용을 이곳에 추가)
def choose_pet_screen():
    
    pet1Text = pygame.image.load('image/초등.png')
    pet1Text = pygame.transform.scale(pet1Text, (73, 38))
    
    pet2Text = pygame.image.load('image/중등.png')
    pet2Text = pygame.transform.scale(pet2Text, (73, 38))
    
    pet3Text = pygame.image.load('image/고등.png')
    pet3Text = pygame.transform.scale(pet3Text, (73, 38))
    
    elementPet = pygame.image.load('image/pet1.png')
    elementPet = pygame.transform.scale(elementPet, (100, 100))
    
    middlePet = pygame.image.load('image/pet2.png')
    middlePet = pygame.transform.scale(middlePet, (100, 100))
    
    highPet = pygame.image.load('image/pet3.png')
    highPet = pygame.transform.scale(highPet, (100, 100))
    
    background = pygame.image.load('image/choose.png')  
    background = pygame.transform.scale(background, (1280, 832))
    screen.blit(background, (0, 0))
    screen.blit(pet1Text, (315,100))
    screen.blit(pet2Text, (585,182))
    screen.blit(pet3Text, (858,85))
    screen.blit(elementPet, (300, 151))    
    screen.blit(middlePet, (568, 260))   
    screen.blit(highPet, (860, 140))   
    
    pygame.display.update()
    
# 게임 루프
#choo = 1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if current_screen == 'main':
        # 메인 화면 그리기
        screen.blit(background, (0, 0))
        screen.blit(play, play_rect)

        # 마우스 클릭 감지
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # play 버튼 클릭 시 화면 전환
        if play_rect.collidepoint(mouse_pos) and mouse_click[0]:
            current_screen = 'choose_pet'

    elif current_screen == 'choose_pet':
        # 펫 선택 화면 출력
        choose_pet_screen()

    pygame.display.update()

pygame.quit()
sys.exit()
