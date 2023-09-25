n = int(input())
blue = [[0]*6 for _ in range(4)]
green = [[0]*4 for _ in range(6)]
score = 0

# 파란색 보드에 블록을 떨어트리는 함수
def drop_blue(t, x):
    y =0
    # 1번 블록 또는 2번 블록의 경우
    if t in [1, 2]:
        # 블록을 떨어트릴 수 있는 위치를 찾는다.
        for i in range(6):
            if blue[x][i] == 1:
                break
            y += 1
        y -= 1
        # 2번 블록의 경우 한 칸 더 떨어트린다.
        if t == 2:
            blue[x][y-1] = 1
        blue[x][y] = 1
    # 3번 블록의 경우
    else:
        # 블록을 떨어트릴 수 있는 위치를 찾는다.
        for i in range(6):
            if blue[x][i] == 1 or blue[x+1][i] == 1:
                break
            y += 1
        y -= 1
        # 블록을 두 칸에 걸쳐 떨어트린다.
        blue[x][y], blue[x+1][y] = 1, 1

# 초록색 보드에 블록을 떨어트리는 함수
def drop_green(t, y):
    x = 0
    # 1번 블록 또는 3번 블록의 경우
    if t in [1,3]:
        # 블록을 떨어트릴 수 있는 위치를 찾는다.
        for i in range(6):
            if green[i][y] == 1:
                break
            x += 1
        x -= 1
        # 3번 블록의 경우 한 칸 더 떨어트린다.
        if t == 3:
            green[x-1][y] = 1
        green[x][y] = 1
    # 2번 블록의 경우
    else:
        # 블록을 떨어트릴 수 있는 위치를 찾는다.
        for i in range(6):
            if green[i][y] == 1 or green[i][y+1] == 1:
                break
            x += 1
        x -= 1
        # 블록을 두 칸에 걸쳐 떨어트린다.
        green[x][y], green[x][y+1] = 1, 1

# 지워질 블록을 처리하는 함수
def delete(c, idx):
    if c == 'b':  # 파란색 보드의 경우
        # 지워질 블록을 위로 올린다.
        for i in range(idx, -1, -1):
            if i == 0:
                for j in range(4):
                    blue[j][i] = 0
            else:
                for j in range(4):
                    blue[j][i] = blue[j][i-1]

    elif c == 'g':  # 초록색 보드의 경우
        # 지워질 블록을 왼쪽으로 옮긴다.
        for i in range(idx, -1, -1):
            if i == 0:
                for j in range(4):
                    green[i][j] = 0
            else:
                for j in range(4):
                    green[i][j] = green[i-1][j]

# 블록을 떨어트리는 동작 수행
for _ in range(n):
    t, x, y = map(int, input().split())
    # 블록 떨어트리기
    drop_blue(t, x)
    drop_green(t, y)

    # 블록이 가득 차면 해당 행 또는 열을 지운다.
    for i in range(6):
        b_cnt = 0
        for j in range(4):
            if blue[j][i] == 1:
                b_cnt += 1
        if b_cnt == 4:
            delete('b', i)
            score += 1
    for i in range(6):
        b_cnt = 0
        for j in range(4):
            if green[i][j] == 1:
                b_cnt += 1
        if b_cnt == 4:
            delete('g', i)
            score += 1

    # 스페셜존 처리
    for i in range(2):
        for j in range(4):
            if blue[j][i] == 1:
                delete('b', 5)
                break

    for i in range(2):
        for j in range(4):
            if green[i][j] == 1:
                delete('g', 5)
                break

# 남아있는 블록의 개수를 계산한다.
count = 0
for i in range(4):
    for j in range(6):
        if blue[i][j] == 1:
            count += 1
        if green[j][i] == 1:
            count += 1

# 결과 출력
print(score)
print(count)
