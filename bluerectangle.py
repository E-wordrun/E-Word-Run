import pygame
import sys

# 초기화
pygame.init()

# 색상 정의
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# 화면 크기 설정
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# 제목 설정
pygame.display.set_caption("Pygame Simple Game")

# 사각형 위치와 크기
rect_x = 50
rect_y = 50
rect_width = 50
rect_height = 50
rect_speed = 5

# 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키보드 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    # 화면 흰색으로 채우기
    screen.fill(WHITE)

    # 사각형 그리기
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))

    # 화면 업데이트
    pygame.display.flip()

    # FPS 설정 (초당 60 프레임)
    pygame.time.Clock().tick(60)

# 종료 처리
pygame.quit()
sys.exit()
