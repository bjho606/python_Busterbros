# 1_ 에서 가져옴
import pygame
import os

# --------------------------------------------------------------------------------
# 기본 초기화 (반드시 해야하는 것들)

pygame.init()

# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("팡게임")

# FPS
clock = pygame.time.Clock()

# --------------------------------------------------------------------------------
# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__)    # 현재 파일의 위치를 반환
image_path = os.path.dirname("C:/JB/Coding/Python/Practice/inflearn_lecture/resources/background2.png")

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background2.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage2.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character2.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xpos = screen_width/2 - character_width/2
character_ypos = screen_height - stage_height - character_height

# 캐릭터 이동 방향 (좌우)
character_to_x = 0
# 캐릭터 이동 속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon2.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한 번에 여러 발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10


# [이벤트 루프]
running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:   # 무기 발사
                weapon_xpos = character_xpos + character_width/2 - weapon_width/2
                weapon_ypos = character_ypos    # 캐릭터의 머리 위에서 발사한다고 배치
                weapons.append([weapon_xpos, weapon_ypos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. 게임 캐릭터 위치 정의 (이동, 경계값 처리 등)
    character_xpos += character_to_x

    if character_xpos < 0:
        character_xpos = 0
    elif character_xpos > screen_width - character_width:
        character_xpos = screen_width - character_width

    # 무기 위치 조정
    # weapon1 100, 200 -> 180, 160, 140, ...
    # weapon2 500, 200 -> 180, 160, 140, ...
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]    # 무기 위치를 위로
    # weapons_temp = []     # 한 줄 for 풀어서 쓰면 이렇다...
    # for w in weapons:
    #     weapons_temp.append([w[0], w[1] - weapon_speed])
    # weapons = weapons_temp

    # 천장에 닿은 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]
    # weapons_temp = []
    # for w in weapons:
    #     if w[1] > 0:
    #         weapons_temp.append([w[0], w[1]])
    # weapons = weapons_temp

    # 4. 충돌 처리
    
    # 5. 화면에 그리기
    screen.blit(background, (0, 0))

    # 무기를 먼저 그려서 나머지 배경에 가려지도록 한다
    for weapon_xpos, weapon_ypos in weapons:
        screen.blit(weapon, (weapon_xpos, weapon_ypos))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_xpos, character_ypos))


    pygame.display.update()

pygame.quit()
