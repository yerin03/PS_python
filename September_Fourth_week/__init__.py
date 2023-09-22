from collections import deque

# N: 나라의 크기, L과 R은 인구 차이 범위
n, l, r = map(int, input().split())
# 각 나라의 인구수를 2차원 배열로 입력받음
A = [list(map(int, input().split())) for _ in range(n)]

# 상, 하, 좌, 우로 이동하기 위한 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# bfs 함수를 사용하여 인접한 나라들과의 인구 차이를 계산하고, 연합을 형성하는 나라들의 좌표를 반환
def bfs(i, j):
    queue = deque()
    union = []
    queue.append((i, j))
    union.append((i, j))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            # nx, ny는 다음 방문할 좌표, 아직 방문하지 않았고 범위 내에 있을 때
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                # 인구 차이가 l과 r 사이일 경우
                if l <= abs(A[nx][ny] - A[x][y]) <= r:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    union.append((nx, ny))
    return union


result = 0
# 무한 반복을 통해 인구 이동을 계속 진행
while True:
    # 방문 여부를 저장하는 배열
    visited = [[0 for _ in range(n)] for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)

                # 연합이 형성된 경우
                if len(country) > 1:
                    flag = 1
                    # 연합 국가의 인구의 평균을 계산
                    people = sum(A[x][y] for x, y in country) // len(country)

                    # 연합 국가의 인구를 평균 값으로 업데이트
                    for x, y in country:
                        A[x][y] = people

    # 연합이 형성되지 않았을 경우, 인구 이동 종료
    if flag == 0:
        print(result)
        break

    # 인구 이동 일수를 1 증가
    result += 1
