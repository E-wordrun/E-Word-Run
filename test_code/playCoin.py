import pygame
import sys
import math

pygame.init()

# 화면 크기 설정
size = [1280, 832]
screen = pygame.display.set_mode(size)
screen_width, screen_height = size  # 화면 크기 변수로 저장
pygame.display.set_caption("E-Word-Run")
# 아이콘 이미지 불러오기 (예: "icon.png" 이미지 파일)
icon_image = pygame.image.load("image/coin.png")
# 아이콘 설정
pygame.display.set_icon(icon_image)

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
play_rect.center = (size[0] // 2, size[1] // 2 + 70)

# 펫 선택 화면 함수
pet = 0
def choose_pet_screen():
    global pet
    
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
    global is_jumping, velocity_y, score 
    score = 0
   
    font = pygame.font.Font(None, 50)

    scoreBox = pygame.image.load('image/scorebox.png')
    scoreBox = pygame.transform.scale(scoreBox, (291, 103))
    
    coin = pygame.image.load('image/coin.png')
    coin = pygame.transform.scale(coin, (40, 40))
    
    roadCoins = {}
    try:
        coins = pygame.image.load('image/coin.png')
        coins = pygame.transform.scale(coins, (35, 35))
        roadCoins = {f'roadCoin{i}': coins for i in range(1, 28)}
        print("Coin image loaded successfully!")  # 성공적으로 로드되었는지 확인
    except pygame.error as e:
        print(f"Failed to load coin image: {e}")
        
    # 폭탄 이미지
    boom = pygame.image.load('image/장애물1.png')
    boom = pygame.transform.scale(boom, (35, 35))
    
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
    
    if pet == 1:
        withPet = pygame.image.load('image/pet1.png')
    elif pet == 2:
        withPet = pygame.image.load('image/pet2.png')
    elif pet == 3:
        withPet = pygame.image.load('image/pet3.png')
    withPet = pygame.transform.flip(withPet, True, False)
    withPet = pygame.transform.scale(withPet, (80, 80))

    character_frame_index = 0
    character_frame_rate = 2  # 초당 10 프레임
    character_rect = character_frames[0].get_rect()
    character_rect.center = (200, screen_height - 250)

    # 점프 관련 변수 설정
    is_jumping = False
    jump_speed = 40  # 점프 속도
    gravity = 4      # 중력
    velocity_y = 4   # y축 속도

    # 배경 설정
    background = pygame.image.load('image/background.png')
    background = pygame.transform.scale(background, (screen_width, screen_height))  
    background_width = background.get_rect().width
    background_x_pos = 0
    background_speed = 12
    
    # 캐릭터 초기 위치 저장
    character_start_y = character_rect.y
    
    # 펫의 초기 위치 및 위아래로 움직이는 애니메이션 설정
    pet_base_y = screen_height - 380  # 펫의 기본 y 위치
    pet_amplitude = 15  # 위아래로 움직이는 범위 (10픽셀)
    pet_frequency = 0.2  # 움직이는 속도 (값이 작을수록 느려짐)

    # 게임 루프
    frame_count = 0  # 프레임 카운트 추가

    # 코인 위치를 저장하는 리스트 초기화
    road_coins_positions = [i * 130 for i in range(28)]  # 초기 x 위치 설정
    positions = [i * 130 for i in range(28)]  # 초기 x 위치 설정
    boom_positions = [i * 130 for i in range(28)]
    
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
    
        # 코인 위치 업데이트
        for i in range(len(road_coins_positions)):
            road_coins_positions[i] -= background_speed
            # 코인이 화면 왼쪽으로 사라지면 마지막 코인 뒤로 이동
            if road_coins_positions[i] <= -50:  # 화면 밖으로 나가면
                road_coins_positions[i] = road_coins_positions[-1] + positions[i] + 130 # 마지막 코인의 뒤에서 재배치
        for i in range(len(boom_positions)):
            boom_positions[i] -= background_speed
            # 폭탄이 화면 왼쪽으로 사라지면 마지막 코인 뒤로 이동
            if boom_positions[i] <= -50:  # 화면 밖으로 나가면
                boom_positions[i] = boom_positions[-1] + positions[i] + 130 
        
        # 배경 그리기
        screen.blit(background, (background_x_pos, 0))
        screen.blit(background, (background_x_pos + background_width, 0))
        screen.blit(scoreBox, (910, 20))
        screen.blit(coin, (967, 50))  # 이동한 coin 위치로 그리기 15
    
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
    
        # 펫의 위아래 움직임 계산 (사인파 사용)
        pet_y_offset = pet_amplitude * math.sin(pet_frequency * frame_count)
        pet_y_position = pet_base_y + pet_y_offset
    
        # 캐릭터 및 펫 그리기
        screen.blit(current_character_frame, character_rect)
        screen.blit(withPet, (85, pet_y_position))  # 펫을 위아래로 움직임
        frame_count += 1  # 프레임 카운트 증가  
        
        boom_coll = True
        coin_coll = True
        # 코인 위치 업데이트 및 충돌 감지
        for i in range(len(road_coins_positions)):
            if i==7 or i==9 or i==13 or i==16 or i==21 or i==23 or i==27:
                coins_rect = coins.get_rect(topleft=(road_coins_positions[i], 447))
                boom_rect = boom.get_rect(topleft=(boom_positions[i], 577))
            else:
                coins_rect = coins.get_rect(topleft=(road_coins_positions[i], 577))
            if character_rect.colliderect(coins_rect):  # 캐릭터와 코인 충돌 감지
                road_coins_positions[i] = road_coins_positions[-1] + positions[i]  + 130
                if coin_coll:
                    score += 1
            if i==7 or i==9 or i==13 or i==16 or i==21 or i==23 or i==27:
                if character_rect.colliderect(boom_rect):
                    boom_positions[i] = boom_positions[-1] + positions[i]  + 130
                    score -= 10
            if i==7 or i==9 or i==13 or i==16 or i==21 or i==23 or i==27:
                screen.blit(boom, (boom_positions[i], 577))
                screen.blit(coins, (road_coins_positions[i], 447))  # 코인 위치에 그리기
            else:
                screen.blit(coins, (road_coins_positions[i], 577))  # 코인 위치에 그리기
        score_text = font.render(f"{score}", True, (0, 0, 0))
        screen.blit(score_text, (screen_width - 260, 54))


        pygame.display.update()  # 화면 업데이트
        clock.tick(60)
    
    
    # 게임 루프
running = True
clock = pygame.time.Clock() 

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
            current_screen = 'choose_pet'  # 'choose_pet'으로 변경

    elif current_screen == 'choose_pet':
        # 펫 선택 화면 출력
        choose_pet_screen()
        
        # 클릭 이벤트 처리
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 왼쪽 마우스 버튼 클릭
                mouse_pos = pygame.mouse.get_pos()  # 마우스 위치 가져오기

                # 각 펫의 이미지 좌표와 크기를 사용하여 Rect 객체 생성
                element_pet_rect = pygame.Rect(300, 151, 100, 100)  # elementPet의 위치와 크기
                middle_pet_rect = pygame.Rect(568, 260, 100, 100)  # middlePet의 위치와 크기
                high_pet_rect = pygame.Rect(860, 140, 100, 100)    # highPet의 위치와 크기

                # 각 Rect 객체와 마우스 위치의 충돌 여부 확인
                if element_pet_rect.collidepoint(mouse_pos):
                    pet = 1  # elementPet 클릭 시 pet 변수에 1을 할당
                    print(f"Selected pet: {pet}")

                if middle_pet_rect.collidepoint(mouse_pos):
                    pet = 2  # middlePet 클릭 시 pet 변수에 2를 할당
                    print(f"Selected pet: {pet}")

                if high_pet_rect.collidepoint(mouse_pos):
                    pet = 3  # highPet 클릭 시 pet 변수에 3을 할당
                    print(f"Selected pet: {pet}")
        if pet > 0:
            current_screen = 'play_pet' 

    elif current_screen == 'play_pet':
        play_pet()  # play_pet 함수 호출
    
    pygame.display.update()  # 화면 업데이트 추가
    

pygame.quit()
sys.exit()
