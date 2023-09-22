from itertools import combinations
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(viruses, lab):
    queue = deque(viruses)
    visited = [[False for _ in range(N)] for _ in range(N)]
    time = [[0 for _ in range(N)] for _ in range(N)]

    for virus in viruses:
        visited[virus[0]][virus[1]] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and lab[nx][ny] != 1:
                visited[nx][ny] = True
                time[nx][ny] = time[x][y] + 1
                queue.append((nx, ny))

    max_time = 0
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 0 and not visited[i][j]:
                return -1
            if lab[i][j] != 1:
                max_time = max(max_time, time[i][j])

    return max_time


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
virus_positions = [(i, j) for i in range(N) for j in range(N) if lab[i][j] == 2]

min_time = float('inf') #초기값ㅇ르 무한대로 설정
for comb in combinations(virus_positions, M):
    time = bfs(comb, lab)
    if time != -1:
        min_time = min(min_time, time)

print(min_time if min_time != float('inf') else -1)
