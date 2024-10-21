import pygame
import sys

pygame.init()

# 화면 크기 설정
size = [1280, 832]
screen = pygame.display.set_mode(size)
screen_width, screen_height = size  # 화면 크기 변수로 저장

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
    print("Images loaded successfully!")  # 추가된 코드
    return background, play

background, play = load_images()

# 버튼 좌표 및 크기 설정
play_rect = play.get_rect()
play_rect.center = (size[0] // 2, size[1] // 2 + 50)

# 펫 선택 화면 함수
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
    screen.blit(pet1Text, (315, 100))
    screen.blit(pet2Text, (585, 182))
    screen.blit(pet3Text, (858, 85))
    screen.blit(elementPet, (300, 151))    
    screen.blit(middlePet, (568, 260))   
    screen.blit(highPet, (860, 140))   
    
    pygame.display.update()

# 달리기 화면 with pet
def play_pet():
    global is_jumping, velocity_y  # 전역 변수 사용

    # 캐릭터 애니메이션 프레임 로드
    character_frames = [
        pygame.image.load('image/character1.gif'),
        pygame.image.load('image/character2.gif'),
        pygame.image.load('image/character3.gif'),
        pygame.image.load('image/character4.gif'),
        pygame.image.load('image/character5.gif'),
        pygame.image.load('image/character6.gif'),
        pygame.image.load('image/character7.gif')
    ]

    character_frame_index = 0
    character_frame_rate = 2  # 초당 10 프레임
    character_rect = character_frames[0].get_rect()
    character_rect.center = (250, screen_height - 250)

    # 점프 관련 변수 설정
    is_jumping = False
    jump_speed = 40  # 점프 속도
    gravity = 5      # 중력
    velocity_y = 5   # y축 속도

    # 배경 설정
    background = pygame.image.load('image/background.png')
    background = pygame.transform.scale(background, (screen_width, screen_height))  
    background_width = background.get_rect().width
    background_x_pos = 0
    background_speed = 12
    
    # 캐릭터 초기 위치 저장
    character_start_y = character_rect.y

    # 게임 루프
    while True:  # True로 변경하여 무한 루프를 유지
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # 종료 시 프로그램 종료
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not is_jumping:
                    is_jumping = True
                    velocity_y = -jump_speed

        # 배경 이동
        background_x_pos -= background_speed
        if background_x_pos <= -background_width:
            background_x_pos = 0

        # 배경 그리기
        screen.blit(background, (background_x_pos, 0))
        screen.blit(background, (background_x_pos + background_width, 0))

        # 캐릭터 애니메이션 프레임 업데이트
        character_frame_index = (character_frame_index + 1) % (character_frame_rate * len(character_frames))
        current_character_frame = character_frames[character_frame_index // character_frame_rate]

        # 캐릭터 점프 처리
        if is_jumping:
            velocity_y += gravity
            character_rect.y += velocity_y
            if character_rect.y >= character_start_y:  # 캐릭터가 바닥에 닿으면 점프 종료
                character_rect.y = character_start_y
                is_jumping = False
                velocity_y = 0

        # 캐릭터 그리기
        screen.blit(current_character_frame, character_rect)
        
        pygame.display.update()  # 화면 업데이트
        clock.tick(60)

# 게임 루프
running = True
clock = pygame.time.Clock()  # 시계 초기화
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 스페이스바를 누르면 점프 시작
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and current_screen == 'play_pet' and not is_jumping:
                is_jumping = True
                velocity_y = -15  # 위로 점프하는 속도 설정

    if current_screen == 'main':
        # 메인 화면 그리기
        screen.blit(background, (0, 0))
        screen.blit(play, play_rect)

        # 마우스 클릭 감지
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # play 버튼 클릭 시 화면 전환
        if play_rect.collidepoint(mouse_pos) and mouse_click[0]:
            current_screen = 'play_pet'  # 'choose_pet'으로 변경

    elif current_screen == 'choose_pet':
        # 펫 선택 화면 출력
        choose_pet_screen()

    elif current_screen == 'play_pet':
        play_pet()  # play_pet 함수 호출
    
    pygame.display.update()  # 화면 업데이트 추가
    

pygame.quit()
sys.exit()
