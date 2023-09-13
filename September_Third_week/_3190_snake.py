from collections import deque

N = int(input())  # 보드 크기
K = int(input())  # 사과 개수
apple = [[0] * (N+1) for _ in range(N+1)]  # 사과 위치

for _ in range(K):
    a, b = map(int, input().split())
    apple[a][b] = 1

L = int(input())  # 방향 변환 횟수
directions = {}
for _ in range(L):
    x, c = input().split()
    directions[int(x)] = c

# 뱀 초기화
snake = deque([(1, 1)])

# 뱀 방향 (상, 우, 하, 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dir_idx = 1  # 초기 방향은 오른쪽
time = 0  # 게임 시간

while True:
    time += 1
    head = snake[0]
    nx, ny = head[0] + dx[dir_idx], head[1] + dy[dir_idx]

    # 벽 또는 자신의 몸에 부딪히면 종료
    if nx <= 0 or nx > N or ny <= 0 or ny > N or (nx, ny) in snake:
        break

    # 사과가 있으면
    if apple[nx][ny] == 1:
        apple[nx][ny] = 0
    else:
        snake.pop()  # 꼬리 줄임

    snake.appendleft((nx, ny))

    # 방향 변경
    if time in directions:
        if directions[time] == "L":
            dir_idx = (dir_idx - 1) % 4
        else:
            dir_idx = (dir_idx + 1) % 4

print(time)