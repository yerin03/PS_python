N,M = map(int,input().split())
r,c,d = map(int,input().split())

room = [list(map(int,input().split())) for _ in  range(N)]
direction = [(-1,0),(0,1),(1,0),(0,-1)]

room[r][c] = 2  # 처음칸 색칠
cnt = 1


def solution():
    global cnt

    def dfs(x,y,d):
        global board,N,M,D,cnt

        #현재 위치에서 모든 방향으로 이동
        for _ in range (4):
            d=(d+3)%4
            nx=x+direction[d][0]
            ny=y+direction[d][1]

            #이동한 곳이 만약 0이라면
            if not room[nx][ny]:
                room[nx][ny]=2 #청소
                cnt+=1

                dfs(nx,ny,d)
                return

        if room[x-direction[d][0]][y-direction[d][1]] == 1: #후진했는데 벽이면
            return

        else:
            dfs(x-direction[d][0],y-direction[d][1],d) # 뒤가 빈칸이면 다시 dfs

    dfs(r,c,d)
    return cnt



print(solution())



