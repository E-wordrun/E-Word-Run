# import pygame

# # 초기화
# pygame.init()

# # 화면 크기 설정
# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))

# # 색상
# WHITE = (255, 255, 255)

# # 프레임 설정
# clock = pygame.time.Clock()

# # 캐릭터 설정
# character = pygame.image.load('image/pet1.png')
# character_rect = character.get_rect()
# character_rect.center = (screen_width // 2, screen_height - 100)

# # 배경 설정
# background = pygame.image.load('image/background.png')
# background_width = background.get_rect().width

# # 배경 이동 속도
# background_x_pos = 0
# background_speed = 5

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # 배경 이동
#     background_x_pos -= background_speed

#     # 배경이 화면 밖으로 나가면 다시 처음으로 설정
#     if background_x_pos <= -background_width:
#         background_x_pos = 0

#     # 화면 흰색으로 채우기
#     screen.fill(WHITE)

#     # 배경 두 개를 연결해서 그리기 (배경이 움직이면서 끊김 없이 반복되도록)
#     screen.blit(background, (background_x_pos, 0))
#     screen.blit(background, (background_x_pos + background_width, 0))

#     # 캐릭터 그리기
#     screen.blit(character, character_rect)

#     # 화면 업데이트
#     pygame.display.update()

#     # 프레임 속도 설정
#     clock.tick(60)

# pygame.quit()


import pygame

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 색상
WHITE = (255, 255, 255)

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
character_frame_rate = 10  # 초당 10 프레임
character_rect = character_frames[0].get_rect()
character_rect.center = (screen_width // 2, screen_height - 100)

# 배경 설정
background = pygame.image.load('image/background.png')
background_width = background.get_rect().width

# 배경 이동 속도
background_x_pos = 0
background_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 배경 이동
    background_x_pos -= background_speed

    # 배경이 화면 밖으로 나가면 다시 처음으로 설정
    if background_x_pos <= -background_width:
        background_x_pos = 0

    # 화면 흰색으로 채우기
    screen.fill(WHITE)

    # 배경 두 개를 연결해서 그리기 (배경이 움직이면서 끊김 없이 반복되도록)
    screen.blit(background, (background_x_pos, 0))
    screen.blit(background, (background_x_pos + background_width, 0))

    # 캐릭터 애니메이션 프레임 업데이트
    character_frame_index = (character_frame_index + 1) % (character_frame_rate * len(character_frames))
    current_character_frame = character_frames[character_frame_index // character_frame_rate]

    # 캐릭터 그리기
    screen.blit(current_character_frame, character_rect)

    # 화면 업데이트
    pygame.display.update()

    # 프레임 속도 설정
    clock.tick(60)

pygame.quit()
