import sys

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


# L : 현재까지 선택된 정사각형 갯수
# L이 4가 되면 최대값 res 갱신
#그렇지 않으면 방문하지 않은 위치로 이동하고, 위치값을 total에 더한 후, L값을 1증가시켜 재귀 호출을 한다.

#DFS
def DFS(x, y, L, total):
    global res
    if res >= total + max_pos * (4 - L):
        return
    if L == 4:
        res = max(res, total)
        return  #4칸을 돌면 == 테트로미노를 만들면
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
                if L == 2: #ㅗ 이모양
                    visit[nx][ny] = 1
                    DFS(x, y, L + 1, total + board[nx][ny])
                    visit[nx][ny] = 0
                visit[nx][ny] = 1
                DFS(nx, ny, L + 1, total + board[nx][ny])
                visit[nx][ny] = 0

max_pos = max(map(max, board))
res = 0
for i in range(N):
    for j in range(M):
        visit[i][j] = 1
        DFS(i, j, 1, board[i][j])
        visit[i][j] = 0
print(res)