import sys
n = int(sys.stdin.readline())


# 방향 1세대 :  > ^   2세대 : > ^ < v  3세대 : > ^ < ^ < v < ^

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

board = [[0]*101  for _ in range(101)]

for _ in range(n) :
    y,x,d,g = map(int,sys.stdin.readline().split())

    #시작표시
    board[y][x] = 1
    curve = [d]

    for i in range(g):

        for _ in range(g):
            for i in range(len(curve) - 1, -1, -1):
                curve.append((curve[i] + 1) % 4)


        for i in range(len(curve)):
            y, x = y + dy[curve[i]], x + dx[curve[i]]
            board[y][x] = 1

result = 0 # 사각형 개수 세기
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            result += 1
print(result)



