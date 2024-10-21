import pygame

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 1280
screen_height = 832
screen = pygame.display.set_mode((screen_width, screen_height))

# 프레임 설정
clock = pygame.time.Clock()

# 캐릭터 애니메이션 프레임 로드 (GIF를 분리한 프레임 이미지)
character_frames = [
    pygame.image.load('image/character1.gif'),
    pygame.image.load('image/character2.gif'),
    pygame.image.load('image/character3.gif'),
    pygame.image.load('image/character4.gif'),
    pygame.image.load('image/character5.gif'),
    pygame.image.load('image/character6.gif'),
    pygame.image.load('image/character7.gif')
    # 추가적으로 프레임이 있으면 여기 더 추가
]

# 캐릭터 프레임 설정
character_frame_index = 0
character_frame_rate = 2  # 초당 10 프레임
character_rect = character_frames[0].get_rect()
character_rect.center = (250, screen_height-250)

# 배경 설정
background = pygame.image.load('image/background.png')
background = pygame.transform.scale(background, (screen_width, screen_height))  # 배경 크기 조정
background_width = background.get_rect().width

# 점프 관련 변수 설정
is_jumping = False
jump_speed = 40  # 점프할 때 속도 (위로 올라가는 힘)
gravity = 5      # 중력 (점프 후 캐릭터가 떨어지는 힘)
velocity_y = 5   # y축 속도 (위로 올라가는 속도)

# 배경 이동 속도
background_x_pos = 0
background_speed = 12

# 캐릭터 초기 위치 저장
character_start_y = character_rect.y

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 스페이스바를 누르면 점프 시작
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                velocity_y = -jump_speed  # 위로 점프하는 속도 설정

    # 배경 이동
    background_x_pos -= background_speed

    # 배경이 화면 밖으로 나가면 다시 처음으로 설정
    if background_x_pos <= -background_width:
        background_x_pos = 0

    # 배경 두 개를 연결해서 그리기 (배경이 움직이면서 끊김 없이 반복되도록)
    screen.blit(background, (background_x_pos, 0))
    screen.blit(background, (background_x_pos + background_width, 0))

    # 캐릭터 애니메이션 프레임 업데이트
    character_frame_index = (character_frame_index + 1) % (character_frame_rate * len(character_frames))
    current_character_frame = character_frames[character_frame_index // character_frame_rate]

    # 캐릭터 점프 처리
    if is_jumping:
        velocity_y += gravity  # 중력을 점프에 적용
        character_rect.y += velocity_y  # 캐릭터의 y 위치 갱신

        # 캐릭터가 처음 위치로 돌아오면 점프 종료
        if character_rect.y >= character_start_y:
            character_rect.y = character_start_y
            is_jumping = False
            velocity_y = 0

    # 캐릭터 그리기
    screen.blit(current_character_frame, character_rect)

    # 화면 업데이트
    pygame.display.update()

    # 프레임 속도 설정
    clock.tick(60)

pygame.quit()
