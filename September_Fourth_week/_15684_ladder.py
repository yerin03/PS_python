n, m, h = map(int, input().split())  # 세로선 개수, 가로선 개수, 놓을 수 있는 위치의 개수 입력
visited = [[False] * (n+1) for _ in range(h+1)]  # 사다리의 위치를 표시할 2차원 리스트 초기화
combi = []  # 사다리를 놓을 수 있는 위치를 저장할 리스트 초기화

# m개의 가로선의 위치 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    visited[a][b] = True

# 사다리 게임 결과를 확인하는 함수
def check():
    for i in range(1, n+1):
        now = i
        for j in range(1, h+1):
            if visited[j][now-1]:  # 왼쪽에 사다리가 있으면 왼쪽으로 이동
                now -= 1
            elif visited[j][now]:  # 현재 위치에 사다리가 있으면 오른쪽으로 이동
                now += 1
        # 게임을 마친 후, 시작 위치와 도착 위치가 다르면 False 반환
        if now != i:
            return False
    return True  # 모든 세로선이 원래 위치로 돌아오면 True 반환

# DFS 방식으로 사다리를 놓는 함수
def dfs(depth, idx):
    global answer
    if depth >= answer:  # 현재까지 놓은 사다리의 개수가 answer 이상이면 리턴
        return
    if check():  # 현재 상태에서 게임 결과가 성립되면
        answer = depth  # answer 업데이트
        return

    for c in range(idx, len(combi)):  # 사다리를 놓을 수 있는 모든 위치에 대해 탐색
        x, y = combi[c]
        # 현재 위치의 왼쪽, 오른쪽에 사다리가 없을 경우에만 사다리 놓기
        if not visited[x][y-1] and not visited[x][y+1]:
            visited[x][y] = True
            dfs(depth+1, c+1)  # 다음 위치를 탐색
            visited[x][y] = False  # 사다리 놓은 상태를 되돌리기

# 사다리를 놓을 수 있는 위치 찾기
for i in range(1,h+1):
    for j in range(1, n):
        if not visited[i][j-1] and not visited[i][j] and not visited[i][j+1]:
            combi.append([i, j])  # 사다리를 놓을 수 있는 위치를 combi 리스트에 저장

answer = 4  # 최대로 놓을 수 있는 사다리의 개수 설정
dfs(0, 0)  # DFS 시작

print(answer if answer < 4 else -1)  # 결과 출력. 3개 이하로 문제의 답이 나오면 그 값을, 그렇지 않으면 -1 출력
