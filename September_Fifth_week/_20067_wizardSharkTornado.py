n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
x, y = n // 2, n // 2
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

windx = [
    # left
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],
    # down
    [-1, -1, 0, 0, 2, 0, 0, 1, 1],
    # right
    [1, -1, 2, -2, 0, 1, -1, 1, -1],
    # up
    [1, 1, 0, 0, -2, 0, 0, -1, -1]
]

windy = [
    # left
    [1, 1, 0, 0, -2, 0, 0, -1, -1],
    # down
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],
    # right
    [-1, -1, 0, 0, 2, 0, 0, 1, 1],
    # up
    [1, -1, 2, -2, 0, 1, -1, 1, -1]
]

rate = [1, 1, 2, 2, 5, 7, 7, 10, 10]

out_sand = 0

def is_out(nx, ny):
    return nx < 0 or nx >= n or ny < 0 or ny >= n

length = 1
direction = 0
count = 0

while True:
    for _ in range(length):
        x += dx[direction]
        y += dy[direction]

        if is_out(x, y):
            break

        if data[y][x] == 0:
            continue

        tmp_sand = data[y][x]
        remain_sand = tmp_sand

        for i in range(9):
            nx = x + windx[direction][i]
            ny = y + windy[direction][i]
            move_sand = (tmp_sand * rate[i]) // 100
            remain_sand -= move_sand

            if is_out(nx, ny):
                out_sand += move_sand
            else:
                data[ny][nx] += move_sand

        nx = x + dx[direction]
        ny = y + dy[direction]

        if is_out(nx, ny):
            out_sand += remain_sand
        else:
            data[ny][nx] += remain_sand

        data[y][x] = 0

    count += 1
    direction = (direction + 1) % 4

    if count == 2:
        count = 0
        length += 1

    if x == 0 and y == 0:
        break

print(out_sand)