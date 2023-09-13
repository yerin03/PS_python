N, M, x, y, K = map(int, input().split())
dice = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

# 주사위 상태 초기화
dice_state = [0] * 6

# 주사위 이동 방향 (동, 서, 북, 남)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


# 주사위 굴리기 함수
def roll_dice(direction):
    if direction == 1:  # 동쪽
        dice_state[0], dice_state[2], dice_state[3], dice_state[5] = dice_state[3], dice_state[0], dice_state[5], \
        dice_state[2]
    elif direction == 2:  # 서쪽
        dice_state[0], dice_state[2], dice_state[3], dice_state[5] = dice_state[2], dice_state[5], dice_state[0], \
        dice_state[3]
    elif direction == 3:  # 북쪽
        dice_state[0], dice_state[1], dice_state[4], dice_state[5] = dice_state[4], dice_state[0], dice_state[5], \
        dice_state[1]
    else:  # 남쪽
        dice_state[0], dice_state[1], dice_state[4], dice_state[5] = dice_state[1], dice_state[5], dice_state[0], \
        dice_state[4]


# 주사위 이동 및 출력
for command in commands:
    nx, ny = x + dx[command - 1], y + dy[command - 1]

    if nx < 0 or nx >= N or ny < 0 or ny >= M:  # 지도를 벗어나는 경우 무시
        continue

    roll_dice(command)  # 주사위 굴리기

    if dice[nx][ny] == 0:  # 이동한 칸에 쓰여 있는 수가 0인 경우
        dice[nx][ny] = dice_state[5]
    else:  # 이동한 칸에 쓰여 있는 수가 0이 아닌 경우
        dice_state[5] = dice[nx][ny]
        dice[nx][ny] = 0

    x, y = nx, ny  # 주사위 위치 업데이트
    print(dice_state[0])  # 주사위 상단 숫자 출력