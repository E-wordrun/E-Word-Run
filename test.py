### 1. pygame 선언
import pygame                  # pygame 라이브러리 임포트
pygame.init()                  # pygame 모듈 초기화

#### 2. pygame에 사용되는 전역변수 선언
Color = (255, 255, 255)        # 하얀색 (RGB 값)으로 배경색 설정
size = [1280, 832]              # 게임 창의 크기를 [400, 300]으로 설정 (너비, 높이)
screen = pygame.display.set_mode(size)  # 설정된 크기의 게임 화면 생성
done = False                   # 게임 루프의 종료 조건 (False일 동안 게임이 계속 실행됨)
clock = pygame.time.Clock()    # 게임의 프레임 속도를 조절할 수 있는 시계 객체 생성


#### 3. pygame 무한루프 : 게임 본체
def runGame():
    global done                # 전역 변수 'done'을 사용하기 위해 global 키워드 선언
    while not done:            # done이 False인 동안 게임이 실행됨
        clock.tick(10)         # 게임 루프를 초당 10번 실행 (FPS 10)
        screen.fill(Color)     # 매 프레임마다 화면을 하얀색으로 채움

        # pygame 이벤트 처리 루프
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 게임 창의 'X' 버튼을 누르면 발생하는 이벤트
                done = True                # done을 True로 변경하여 while 루프를 종료
        pygame.display.update()   # 화면을 업데이트하여 변경 사항을 반영 (새로고침)


#### 4. pygame 게임 종료
runGame()                         # 게임 실행 함수 호출
pygame.quit()                     # pygame 모듈을 종료하여 모든 리소스 해제
