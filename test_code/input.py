import pygame
import sys
import json
import time

# JSON 파일을 불러오는 함수 : load_json()
def load_json():
    with open('words.json', 'r', encoding='utf-8') as file:
        return json.load(file)

pygame.init()

size = [1280, 832]
screen = pygame.display.set_mode(size)

# 배경과 기타 이미지 로드
try:
    blur_background = pygame.image.load('image/blur-background.png')
    blur_background = pygame.transform.scale(blur_background, (1280, 832))

    input_bar = pygame.image.load('image/inputbox.png')
    input_bar = pygame.transform.scale(input_bar, (383, 296))

    result_background = pygame.image.load('image/result.png')
    result_background = pygame.transform.scale(result_background, (608, 551))
    
    home_button = pygame.image.load('image/homebutton.png')
    home_button = pygame.transform.scale(home_button, (45, 45))

except pygame.error as e:
    print(f"이미지를 불러올 수 없습니다: {e}")
    pygame.quit()
    sys.exit()

font = pygame.font.Font('font/DungGeunMo.ttf', 52)
input_text = ""  # 입력된 텍스트 초기화
cursor_visible = True #커서 표시 상태
backspace_pressed = False 
backspace_start_time = 0 # 백스페이스 키가 눌린 시간
backspace_interval = 40 # 백스페이스 키로 -> 글자 삭제 시간 (ms)

cursor_y = 415

# JSON에서 단어 데이터를 가져옴
word_data = load_json()
current_word_index = 0  # 현재 단어 인덱스


# 틀렸습니다 메세지창 함수
def show_message(message):
    message_surface = font.render(message, True, (0, 0, 0))
    message_rect = message_surface.get_rect(center=(640, 416 - 20))  # 화면 중앙
    screen.blit(blur_background, (0, 0))  # 배경 다시 그리기
    pygame.draw.rect(screen, (255, 255, 255), (380, 350, 520, 100))  # 메시지 창 배경
    pygame.draw.rect(screen, (0, 0, 0), (380, 350, 520, 100), 2)  # 테두리
    screen.blit(message_surface, message_rect)
    pygame.display.update()
    
    pygame.time.wait(1500) #1.5초 대기

# 결과 화면으로 전환하는 함수
def show_result_screen():
    result_x = (1280 - 718) // 2 + 60
    result_y = (832 - 667) // 2 + 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 배경 및 결과 화면 출력
        screen.blit(blur_background, (0, 0))
        screen.blit(result_background, (result_x, result_y))
        screen.blit(home_button, (22, 20))
        pygame.display.update()

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                backspace_pressed = True
                backspace_start_time = pygame.time.get_ticks()
            elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                # 엔터나 스페이스바를 눌렀을 때 결과 확인
                correct_english = word_data['elementary'][current_word_index]['english']
                if input_text.lower() == correct_english.lower():  # 대소문자 구분 없이 비교
                    input_text = ""  # 맞으면 입력 필드를 초기화 - 임시
                    current_word_index += 1  # 다음 단어로 넘어감 - 임시
                    if current_word_index >= len(word_data['elementary']):
                        # 모든 단어를 맞추면 게임 종료- 임시!.
                        running = False
                else:
                    # 틀린 경우 메세지창 표시 후 -> 결과 화면으로 전환
                    show_message("틀렸습니다!")
                    show_result_screen()
                    running = False
            else:
                input_text += event.unicode
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                backspace_pressed = False

    if backspace_pressed:
        current_time = pygame.time.get_ticks()
        if current_time - backspace_start_time > backspace_interval:
            if input_text:
                input_text = input_text[:-1]
            backspace_start_time = current_time

    screen.blit(blur_background, (0, 0))
    screen.blit(input_bar, (450, 300))

    # 현재 단어 표시 (한국어)
    korean_word = word_data['elementary'][current_word_index]['korean']
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

pygame.quit()
