import pygame
import sys

pygame.init()

size = [1280, 832]
screen = pygame.display.set_mode(size)

try:
    blur_background = pygame.image.load('image/blur-background.png')  
    blur_background = pygame.transform.scale(blur_background, (1280, 832))
    
    input_bar = pygame.image.load('image/inputbox.png')  
    input_bar = pygame.transform.scale(input_bar, (383, 296))
    
except pygame.error as e:
    print(f"이미지를 불러올 수 없습니다: {e}")
    pygame.quit()
    sys.exit()


font = pygame.font.Font(None, 52)  # 폰트 크기 변경
input_text = ""  # 입력된 텍스트 초기화
cursor_visible = True  # 커서 표시 상태

# 백스페이스 상태 확인
backspace_pressed = False
backspace_start_time = 0  # 백스페이스 키가 눌린 시간
backspace_interval = 40  # 백스페이스 키로 -> 글자 삭제 시간 (ms)

cursor_y = 415  

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # 입력 활성화 상태를 따로 두지 않고 모든 키 입력을 처리
            if event.key == pygame.K_BACKSPACE:  # 백스페이스로 문자 삭제
                backspace_pressed = True
                backspace_start_time = pygame.time.get_ticks()  # 현재 시간 저장
            elif event.key == pygame.K_RETURN:  # Enter 키는 아무 작업도 하지 않음
                pass
            else:  # 다른 키는 텍스트에 추가
                input_text += event.unicode
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:  # 백스페이스 키를 떼면 상태 초기화
                backspace_pressed = False

    # 백스페이스 -> 일정 간격으로 문자 삭제
    if backspace_pressed:
        current_time = pygame.time.get_ticks()  # 현재 시간
        if current_time - backspace_start_time > backspace_interval:  # 지정한 간격이 지나면
            if input_text:  # 텍스트가 비어있지 않을 때만 삭제
                input_text = input_text[:-1]  # 마지막 문자 삭제
            backspace_start_time = current_time  # 시작 시간 업데이트

    
    screen.blit(blur_background, (0, 0))
    screen.blit(input_bar, (450, 300))

 
    text_surface = font.render(input_text, True, (0, 0, 0))  # 텍스트 색상은 검은색
    screen.blit(text_surface, (500, 400))   

    # 커서 항상 표시 (입력 활성화와 상관없이)
    cursor_x = 500 + text_surface.get_width()  
    cursor_height = 30   
    pygame.draw.rect(screen, (0, 0, 0), (cursor_x, cursor_y - cursor_height // 2, 2, cursor_height))  

    pygame.display.update()

pygame.quit()
