from tkinter import font
import pygame
import sys
import json 
import time
import random

def load_json():
    # 파일을 읽기 모드 열고, 파일이 자동으로 닫히도록 보장하는 with 구문을 사용
    with open('words.json', 'r', encoding='utf-8') as file:
        # JSON 문자열을 읽고, 이를 Python 딕셔너리와 같은 자료형으로 변환하여 반환
        return json.load(file)

pygame.init()

# 게임 상태 변수
current_screen = 'main'
# globals() 프로그램 전체에서 전역 변수 선언
# global 전역 변수임을 사용하겠다고 명시
globals() ['font'] = pygame.font.Font(None, 50)
globals() ['level'] = ''
globals() ['score'] = 0
globals() ['pet'] = 0

# 화면 크기 설정
size = [1280, 832]
screen = pygame.display.set_mode(size)
screen_width, screen_height = size  # 화면 크기 변수로 저장
# 창 제목
pygame.display.set_caption("E-Word-Run")
# 아이콘 이미지 불러오기 (예: "icon.png" 이미지 파일)
icon_image = pygame.image.load("image/coin.png")
# 아이콘 설정
pygame.display.set_icon(icon_image)

# 이미지 로드
def load_images():
    try:
        background = pygame.image.load('image/start_background.png')
        background = pygame.transform.scale(background, (1280, 832))
        play = pygame.image.load('image/play-btn.png')
        play = pygame.transform.scale(play, (300, 100))
    except pygame.error as e:
        print(f"이미지를 불러올 수 없습니다: {e}")
        pygame.quit()
        sys.exit()
    print("Images loaded successfully!")  # 추가된 코드
    return background, play

background, play = load_images()

# 버튼 크기 가져오기
play_rect = play.get_rect()
# 버튼 위치 설정
play_rect.center = (size[0] // 2, size[1] // 2 + 70)

# 펫 선택 화면 함수
def choose_pet_screen():
    global current_word_index
    current_word_index = 0
    global pet
    pet = 0
    
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
    
    
    running = True
    while running:
    
        screen.blit(background, (0, 0))
        screen.blit(pet1Text, (315, 100))
        screen.blit(pet2Text, (585, 182))
        screen.blit(pet3Text, (858, 85))
        screen.blit(elementPet, (300, 151))    
        screen.blit(middlePet, (568, 260))   
        screen.blit(highPet, (860, 140))   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 클릭 이벤트 처리
            # MOUSEBUTTONDOWN : 마우스 버튼이 눌림
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 1: 왼쪽 마우스 버튼
                # 2: 가운데 마우스 버튼 (휠)
                # 3: 오른쪽 마우스 버튼
                if event.button == 1:  # 왼쪽 마우스 버튼 클릭
                    mouse_pos = pygame.mouse.get_pos()  # 마우스 위치 가져오기

                    # 각 펫의 이미지 좌표와 크기를 사용하여 Rect 객체 생성
                    element_pet_rect = pygame.Rect(300, 151, 100, 100)  # elementPet의 위치(300, 151)와 크기(100, 100)
                    middle_pet_rect = pygame.Rect(568, 260, 100, 100)  # middlePet의 위치와 크기
                    high_pet_rect = pygame.Rect(860, 140, 100, 100)    # highPet의 위치와 크기

                    # 각 Rect 객체와 마우스 위치의 충돌 여부 확인
                    if element_pet_rect.collidepoint(mouse_pos):
                        pet = 1  # elementPet 클릭 시 pet 변수에 1을 할당
                        globals() ['level'] = 'elementary'
                        print(f"Selected pet: {pet}")

                    if middle_pet_rect.collidepoint(mouse_pos):
                        pet = 2  # middlePet 클릭 시 pet 변수에 2를 할당
                        globals() ['level'] = 'middle'
                        print(f"Selected pet: {pet}")

                    if high_pet_rect.collidepoint(mouse_pos):
                        pet = 3  # highPet 클릭 시 pet 변수에 3을 할당
                        globals() ['level'] = 'high'
                        print(f"Selected pet: {pet}")
            # 펫을 선택했다면 
            if pet > 0:
                # 점수 초기화
                globals() ['score'] = -2
                running = False
                play_pet()  # play_pet 함수 호출

            pygame.display.update()



# 배경과 기타 이미지 로드
try:
    blur_background = pygame.image.load('image/blur-background.png')
    blur_background = pygame.transform.scale(blur_background, (1280, 832))

    input_bar = pygame.image.load('image/inputbox.png')
    input_bar = pygame.transform.scale(input_bar, (383, 296))

    result_background = pygame.image.load('image/result.png')
    result_background = pygame.transform.scale(result_background, (608, 551))

except pygame.error as e:
    print(f"이미지를 불러올 수 없습니다: {e}")
    pygame.quit()
    sys.exit()

# 틀렸습니다 메세지창 함수
def show_message(message):
    font = pygame.font.Font('font/DungGeunMo.ttf', 52) 
    message_surface = font.render(message, True, (0, 0, 0))
    message_rect = message_surface.get_rect(center=(640, 416 - 20))  # 화면 중앙
    screen.blit(blur_background, (0, 0))  # 배경 다시 그리기
    pygame.draw.rect(screen, (255, 255, 255), (380, 350, 520, 100))  # 메시지 창 배경
    pygame.draw.rect(screen, (0, 0, 0), (380, 350, 520, 100), 2)  # 테두리
    screen.blit(message_surface, message_rect)
    pygame.display.update()
    
    pygame.time.wait(1500) #1.5초 대기
    
    play_pet()
    
# 문제를 다 풀었을 때 메세지창 함수
def finish_message(message):
    font = pygame.font.Font('font/DungGeunMo.ttf', 52) 
    message_surface = font.render(message, True, (0, 0, 0))
    message_rect = message_surface.get_rect(center=(640, 416 - 20))  # 화면 중앙
    screen.blit(blur_background, (0, 0))  # 배경 다시 그리기
    pygame.draw.rect(screen, (255, 255, 255), (380, 350, 520, 100))  # 메시지 창 배경
    pygame.draw.rect(screen, (0, 0, 0), (380, 350, 520, 100), 2)  # 테두리
    screen.blit(message_surface, message_rect)
    pygame.display.update()
    
    pygame.time.wait(1500) #1.5초 대기
    
    show_result_screen(globals() ['score'])
    
# 결과 화면으로 전환하는 함수
def show_result_screen(score_result):
    result_x = (1280 - 718) // 2 + 60
    result_y = (832 - 667) // 2 + 50
    home_button = pygame.image.load('image/home.png')
    home_button = pygame.transform.scale(home_button, (45, 45))
    running = True
    while running:
        home_button_rect = home_button.get_rect(topleft=(22, 20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 마우스 위치 가져오기
                mouse_pos = pygame.mouse.get_pos()

                # 마우스가 home_button_rect와 충돌하는지 확인
                if home_button_rect.collidepoint(mouse_pos):
                    print('go back home~!')
                    main()
                    running = False

        # 배경 및 결과 화면 출력
        screen.blit(blur_background, (0, 0))
        screen.blit(result_background, (result_x, result_y))
        screen.blit(home_button, (22, 20))
        score_text_result = font.render(f"{score_result}", True, (0, 0, 0))
        text_rect = score_text_result.get_rect()
        score_width = text_rect.width
        screen.blit(score_text_result, (screen_width // 2 - score_width // 2 + 7, screen_height // 2 + 16))

        pygame.display.update()
        
# 게임 루프
current_word_index = 0  # 현재 단어 인덱스  
def quiz():
    global current_word_index
    font = pygame.font.Font('font/DungGeunMo.ttf', 52)
    input_text = ""  # 입력된 텍스트 초기화
    cursor_y = 415

    # JSON에서 단어 데이터를 가져옴
    word_data = load_json()  
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    # 엔터를 눌렀을 때 결과 확인
                    correct_english = word_data[globals()['level']][current_word_index]['english']
                    if input_text.lower().replace(" ", "") != correct_english.lower():  # 대소문자 구분 없이 비교
                        globals()['score'] -= 12 #10점 감소
                        show_message("틀렸습니다!")
                        play_pet()
                    else:
                        globals() ['score'] += 8 #10점 증가
                        current_word_index += 1  # 다음 단어로 넘어감 
                        if current_word_index >= len(word_data[globals()['level']]):
                            finish_message(globals()['level'] + " master")
                        input_text = ""  # 맞으면 입력 필드를 초기화 
                        play_pet()  # 게임 계속 진행
                         
                else:
                    # 문자 입력
                    input_text += event.unicode

        screen.blit(blur_background, (0, 0))
        screen.blit(input_bar, (450, 300))

        # 현재 단어 표시 (한국어)
        korean_word = word_data[globals()['level']][current_word_index]['korean']
        korean_surface = font.render(korean_word, True, (0, 0, 0))
        screen.blit(korean_surface, (580, 250))  # 한국어 단어의 위치

        # 입력된 텍스트 표시
        text_surface = font.render(input_text, True, (0, 0, 0))
        screen.blit(text_surface, (500, 378))

        # 커서 표시
        cursor_x = 500 + text_surface.get_width()
        cursor_height = 30
        pygame.draw.rect(screen, (0, 0, 0), (cursor_x, cursor_y - cursor_height // 2 - 5, 2, cursor_height))

        pygame.display.update()    

    
    
    
    

# 달리기 화면 with pet
def play_pet():
    global is_jumping, velocity_y, pet

    scoreBox = pygame.image.load('image/scorebox.png')
    scoreBox = pygame.transform.scale(scoreBox, (291, 103))
    
    coin = pygame.image.load('image/coin.png')
    coin = pygame.transform.scale(coin, (40, 40))
    
    roadCoins = {}
    try:
        coins = pygame.image.load('image/coin.png')
        # 크기 바꿈
        coins = pygame.transform.scale(coins, (35, 35))
        # {'roadCoin1': 100, 'roadCoin2': 100, 'roadCoin3': 100, ...,'roadCoin27': 100}
        roadCoins = {f'roadCoin{i}': coins for i in range(1, 28)}
        print("Coin image loaded successfully!")  # 성공적으로 로드되었는지 확인
    except pygame.error as e:
        print(f"Failed to load coin image: {e}")
        
    # 폭탄 이미지
    boom = pygame.image.load('image/장애물1.png')
    # 크기 바꿈
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
    
    # 펫 선택 결과
    if pet == 1:
        withPet = pygame.image.load('image/pet1.png')
    elif pet == 2:
        withPet = pygame.image.load('image/pet2.png')
    elif pet == 3:
        withPet = pygame.image.load('image/pet3.png')
    # 이미지 수평으로 뒤집기
    withPet = pygame.transform.flip(withPet, True, False)
    withPet = pygame.transform.scale(withPet, (80, 80))

    character_frame_index = 0
    character_frame_rate = 2  # 초당 2 프레임
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
    background_speed = 9.7
    
    # 캐릭터 초기 위치 저장
    character_start_y = character_rect.y

    # 게임 루프
    frame_count = 0  # 프레임 카운트 추가

    # 코인 위치를 저장하는 리스트 초기화
    # [0, 130, 260, 390, 520, 650, 780, 910, ... ]
    road_coins_positions = [i * 130 for i in range(28)]  # 초기 x 위치 설정
    positions = [i * 130 for i in range(28)]  # 초기 x 위치 설정
    # 폭탄 위치를 저장하는 리스트 초기화
    boom_positions = [i * 130 for i in range(28)]
    
    # 폭탄 위치 램덤 생성
    # 0 ~ 27 에서 4 ~ 26 중 하나
    min_value = 4
    max_value = 26
    # 폭탄이 몇 번째에 나올지
    numbers = []
    # 폭탄 6개
    while len(numbers) < 6:
        num = random.randint(min_value, max_value)
        # 새로운 숫자가 이미 리스트에 없고, +2 또는 -2의 차이가 없는 경우에만 추가
        # for x in numbers : 리스트에서 하나씩 꺼내오고 , any(abs(num - x) <= 2 : 차이가 2이하인 수가 하나라도 있는지
        if num not in numbers and not any(abs(num - x) <= 2 for x in numbers):
            numbers.append(num)
    
    cnt = 0
    # 게임 루프
    while True:  # True로 변경하여 무한 루프를 유지
        cnt += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # 종료 시 프로그램 종료
            if event.type == pygame.KEYDOWN:  # 키가 눌렸을 때
                if event.key == pygame.K_SPACE and not is_jumping:  # 스페이스바가 눌리고, 현재 점프 중이 아니면
                    is_jumping = True  # 점프 상태로 설정
                    velocity_y = -jump_speed  # y축 속도를 음수로 설정하여 위로 점프하게 함

    
        # 배경 이동
        background_x_pos -= background_speed  # 배경의 x 위치를 왼쪽으로 이동
        if background_x_pos <= -background_width:  # 배경이 화면을 완전히 벗어났을 때
            background_x_pos = 0  # 배경을 화면의 시작 위치로 리셋

    
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
        # 이어지는 배경
        screen.blit(background, (background_x_pos + background_width, 0))
        screen.blit(scoreBox, (910, 20))
        screen.blit(coin, (967, 50))
    
        # 캐릭터 애니메이션 프레임 업데이트, 프레임의 순환
        character_frame_index = (character_frame_index + 1) % (character_frame_rate * len(character_frames))
        # 현재 애니메이션 프레임
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
        # pet_y_offset = pet_amplitude * math.sin(pet_frequency * frame_count)
        # pet_y_position = pet_base_y + pet_y_offset
    
        # 캐릭터 및 펫 그리기
        screen.blit(current_character_frame, character_rect)
        screen.blit(withPet, (85, screen_height-380)) 
        frame_count += 1  # 프레임 카운트 증가  
        
        boom_coll = True
        coin_coll = True
        # 폭탄 터지는 이미지
        booom = pygame.image.load('image/booom.png')
        booom = pygame.transform.scale(booom, (50, 50))
        
        # 코인 위치 업데이트 및 충돌 감지
        for i in range(len(road_coins_positions)):
            # 폭탄이 있을 자리인지 
            if i in numbers:
                screen.blit(boom, (boom_positions[i], 577))
                screen.blit(coins, (road_coins_positions[i], 447))  # 코인 위치에 그리기
            else:
                screen.blit(coins, (road_coins_positions[i], 577))  # 코인 위치에 그리기
            if i in numbers:
                coins_rect = coins.get_rect(topleft=(road_coins_positions[i], 447))
                boom_rect = boom.get_rect(topleft=(boom_positions[i], 577))
            else:
                coins_rect = coins.get_rect(topleft=(road_coins_positions[i], 577))
            if character_rect.colliderect(coins_rect):  # 캐릭터와 코인 충돌 감지
                road_coins_positions[i] = road_coins_positions[-1] + positions[i]  + 130
                if coin_coll:
                    globals() ['score'] += 1
            if i in numbers:
                # 폭탄과 충돌
                if character_rect.colliderect(boom_rect):
                    pygame.display.update()
                    screen.blit(booom, boom_rect)
                    score_text = font.render(f"{globals() ['score']}", True, (0, 0, 0))
                    screen.blit(score_text, (screen_width - 260, 54))
                    pygame.display.update()
                    pygame.time.wait(500) #1.5초 대기
                    # score 값 넘기기
                    show_result_screen(globals() ['score'])
                    running = False
        score_text = font.render(f"{globals() ['score']}", True, (0, 0, 0))
        screen.blit(score_text, (screen_width - 260, 54))
        
        if cnt % 100 == 0:
            quiz()

        pygame.display.update()  # 화면 업데이트
        clock.tick(60)
        
        
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # 메인 화면 그리기
        screen.blit(background, (0, 0))
        screen.blit(play, play_rect)
        # 화면 갱신 pygame.display.update()보다 부드럽게 화면 업데이트
        pygame.display.flip()

        # 마우스 클릭 감지
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # play 버튼 클릭 시 화면 전환
        # collidepoint : mouse_pos 좌표가 play_rect의 내부에 있는지 확인 -> true, false
        if play_rect.collidepoint(mouse_pos) and mouse_click[0]:
            choose_pet_screen()  # 화면 전환
    
    
    # 게임 루프
running = True
clock = pygame.time.Clock() 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # main 함수 호출
    main()
    
    pygame.display.update()  # 화면 업데이트 추가
    

pygame.quit()
sys.exit()
