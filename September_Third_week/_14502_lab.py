#https://great-park.tistory.com/104

from collections import deque
import copy
n,m = map(int,input().split())
#graph = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

#바이러스 BFS 로 구현
def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(room)

    #바이러스 큐에 넣기
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i,j))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue

            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                queue.append((nx,ny))


    global answer
    cnt = 0

    for i in range(n):
        cnt += tmp_graph[i].count(0)

    answer = max(answer, cnt)

# 벽세우기
def makeWall(cnt):

    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if room[i][j] == 0 :# 비어있는지 확인하고
                room[i][j] = 1 # 벽세우고
                makeWall(cnt+1) # 다음 벽 세우기
                room[i][j] = 0 #다시 벽 뿌시기

room = [list(map(int,input().split())) for _ in range(n)]
answer = 0
makeWall(0)
print(answer)






