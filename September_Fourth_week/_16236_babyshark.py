from collections import deque

# BFS 탐색을 위한 방향 설정 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, size, arr):
    visited = [[-1] * N for _ in range(N)]  # 각 위치까지의 거리를 저장하기 위한 배열
    q = deque([(x, y)])
    visited[x][y] = 0  # 시작 위치의 거리는 0

    edible = []  # 먹을 수 있는 물고기들의 위치와 거리를 저장할 리스트

    while q:
        x, y = q.popleft()

        for i in range(4):  # 상, 하, 좌, 우 방향을 체크
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                # 물고기의 크기가 상어의 크기보다 작거나 같은 경우 이동할 수 있음
                if arr[nx][ny] <= size:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1  # 거리 정보 갱신

                # 물고기의 크기가 상어의 크기보다 작은 경우 먹을 수 있음
                if 0 < arr[nx][ny] < size:
                    edible.append((visited[nx][ny], nx, ny))  # 거리와 위치 정보 저장

    if not edible:  # 먹을 수 있는 물고기가 없는 경우
        return -1, -1, -1, -1

    # 먹을 수 있는 물고기 중에서 거리가 짧은 순, 위쪽에 있는 순, 왼쪽에 있는 순으로 정렬
    edible.sort()
    return edible[0][0], edible[0][1], edible[0][2], arr[edible[0][1]][edible[0][2]]


N = int(input())  # 공간의 크기 입력
arr = [list(map(int, input().split())) for _ in range(N)]  # 공간의 상태 입력

# 아기 상어의 초기 위치 찾기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            x, y = i, j
            arr[i][j] = 0  # 아기 상어의 초기 위치를 빈 칸으로 설정

size, eat, time = 2, 0, 0  # 아기 상어의 초기 크기, 먹은 물고기 수, 시간

while True:
    # BFS로 가장 가까운 물고기를 찾기
    dist, nx, ny, fish_size = bfs(x, y, size, arr)
    if dist == -1:  # 먹을 수 있는 물고기가 없는 경우 종료
        break

    eat += 1  # 물고기 먹기
    if eat == size:  # 먹은 물고기의 수가 상어의 크기와 같으면
        size += 1  # 크기를 1 증가시키고
        eat = 0  # 먹은 물고기의 수를 초기화

    arr[nx][ny] = 0  # 먹은 물고기의 위치를 빈 칸으로 설정
    time += dist  # 시간 갱신 (이동 거리만큼 시간 증가)
    x, y = nx, ny  # 상어의 위치 갱신

print(time)  # 결과 출력
