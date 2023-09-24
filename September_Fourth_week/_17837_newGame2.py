dx = [0, 0, -1, 1]  # →, ←, ↑, ↓
dy = [1, -1, 0, 0]

def change_dir(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    elif d == 3:
        return 2

def move(horse_num):
    x, y, d = horse[horse_num]
    nx, ny = x + dx[d], y + dy[d]

    if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
        horse[horse_num][2] = change_dir(d)
        nx, ny = x + dx[horse[horse_num][2]], y + dy[horse[horse_num][2]]
        if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
            return

    movable_horse = []
    for i, key in enumerate(horse_map[x][y]):
        if key == horse_num:
            movable_horse.extend(horse_map[x][y][i:])
            horse_map[x][y] = horse_map[x][y][:i]
            break

    if board[nx][ny] == 1:
        movable_horse.reverse()

    for h_num in movable_horse:
        horse_map[nx][ny].append(h_num)
        horse[h_num][:2] = [nx, ny]

    if len(horse_map[nx][ny]) >= 4:
        return True
    return False


n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
horse_map = [[[] for _ in range(n)] for _ in range(n)]
horse = [list(map(int, input().split())) for _ in range(k)]

for i in range(k):
    horse[i][0] -= 1
    horse[i][1] -= 1
    horse[i][2] -= 1
    horse_map[horse[i][0]][horse[i][1]].append(i)

turn = 0
while turn <= 1000:
    turn += 1
    for i in range(k):
        finish = move(i)
        if finish:
            print(turn)
            exit()

print(-1)

