from collections import deque

N, M, K = map(int, input().split())  # 미로의 크기, 참가자 수, 게임 시간 입력받기
maze = []  # 미로 정보를 저장할 리스트
for _ in range(N):
    maze.append(list(map(int, input().split())))

participants = []  # 참가자들의 초기 위치를 저장할 리스트
for _ in range(M):
    r, c = map(int, input().split())
    participants.append((r, c))

exit_r, exit_c = map(int, input().split())  # 출구의 위치 입력받기

dx = [-1, 1, 0, 0]  # 상하좌우 이동을 위한 리스트
dy = [0, 0, -1, 1]

time = 0  # 현재까지 경과된 시간
total_distance = 0  # 참가자들의 이동 거리 합을 저장할 변수

while time < K:
    # BFS를 이용하여 미로 탈출 여부 확인
    visited = [[False] * N for _ in range(N)]
    queue = deque(participants)
    distance = 0  # 현재 시간대에 이동한 거리
    while queue:
        size = len(queue)
        for _ in range(size):
            r, c = queue.popleft()
            if (r, c) == (exit_r, exit_c):
                total_distance += distance  # 출구에 도착한 참가자의 이동 거리를 더함
            for i in range(4):
                nr, nc = r + dx[i], c + dy[i]
                if 1 <= nr <= N and 1 <= nc <= N and not visited[nr - 1][nc - 1]:
                    visited[nr - 1][nc - 1] = True
                    queue.append((nr, nc))
        distance += 1  # 시간 증가
    # 미로 회전
    rotated_maze = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotated_maze[j][N - 1 - i] = maze[i][j]
    maze = rotated_maze
    # 벽의 내구도를 1씩 감소
    for i in range(N):
        for j in range(N):
            if maze[i][j] > 0:
                maze[i][j] -= 1
    time += 1  # 시간 증가

# 결과 출력
print(total_distance)  # 참가자들의 이동 거리 합 출력
print(exit_r, exit_c)  # 출구의 위치 출력
