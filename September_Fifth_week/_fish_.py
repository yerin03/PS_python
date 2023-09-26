directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]  # 8개 방향

def fish_move(board, fish_pos):
    for i in range(1, 17):
        if not fish_pos[i]:  # 물고기가 먹혔으면
            continue
        x, y, d = fish_pos[i]
        for _ in range(8):  # 8방향 확인
            nx, ny = x + directions[d][0], y + directions[d][1]
            if 0 <= nx < 4 and 0 <= ny < 4 and board[nx][ny] != -1:  # 이동 가능하다면
                if board[nx][ny]:  # 다른 물고기가 있다면
                    temp = board[nx][ny]
                    fish_pos[temp] = (x, y, fish_pos[temp][2])
                board[nx][ny], board[x][y] = i, board[nx][ny]
                fish_pos[i] = (nx, ny, d)
                break
            d = (d + 1) % 8

def shark_move(board, fish_pos, x, y, d, eat):
    fish_move(board, fish_pos)
    max_eat = eat
    nx, ny = x + directions[d][0], y + directions[d][1]
    while 0 <= nx < 4 and 0 <= ny < 4:  # 상어가 이동할 수 있는 범위
        if board[nx][ny]:  # 물고기가 있다면
            temp_board = [row[:] for row in board]
            temp_fish_pos = fish_pos.copy()
            fish_num = temp_board[nx][ny]
            temp_board[nx][ny] = -1
            temp_board[x][y] = 0
            temp_fish_pos[fish_num] = []
            #max_eat = max(





