#https://door-of-tabris.tistory.com/entry/%EB%B0%B1%EC%A4%80-15683%EB%B2%88-%EA%B0%90%EC%8B%9C%ED%8C%8C%EC%9D%B4%EC%8D%AC-1

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
cctvs = []
walls = 0

# 각 CCTV의 모든 방향 조합
directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 2], [0, 3], [1, 2], [1, 3]],
    [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    [[0, 1, 2, 3]]
]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            cctvs.append((i, j, office[i][j]))
        if office[i][j] == 6:
            walls += 1

min_area = float('inf')

def scan(office, x, y, d):
    nx, ny = x + dx[d], y + dy[d]
    while 0 <= nx < N and 0 <= ny < M and office[nx][ny] != 6:
        if office[nx][ny] == 0:
            office[nx][ny] = '#'
        nx += dx[d]
        ny += dy[d]

def dfs(office, idx):
    global min_area
    if idx == len(cctvs):
        count = sum(row.count(0) for row in office)
        min_area = min(min_area, count)
        return

    x, y, cctv_type = cctvs[idx]
    for d in directions[cctv_type]:
        temp = [row.copy() for row in office]
        for direction in d:
            scan(temp, x, y, direction)
        dfs(temp, idx + 1)

dfs(office, 0)
print(min_area)