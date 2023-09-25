# 그래프 정보 (각 위치에서 이동할 수 있는 다음 위치의 정보)
# 특정 위치에서 2가지 방향으로 갈 수 있는 경우는 2개의 위치 정보가 있음 (예: [6, 21])
graph = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], [12], [13], [14], [15],
         [16, 27], [17], [18], [19], [20], [32], [22], [23], [24], [30], [26], [24], [28], [29], [24],
         [31], [20], [32]]

# 각 위치에서 얻을 수 있는 점수
score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28,
         30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]

dice = list(map(int, input().split()))
answer = 0

# 깊이 우선 탐색(DFS)을 사용한 백트래킹 함수
def backtracking(depth, result, horses):
    global answer

    # 모든 주사위를 사용한 경우
    if depth == 10:
        answer = max(answer, result)
        return

    for i in range(4):  # 각 말에 대해서
        x = horses[i]  # 현재 말의 위치

        if len(graph[x]) == 2:  # 만약 2가지 방향으로 갈 수 있는 경우
            x = graph[x][1]  # 파란 길로 이동
        else:
            x = graph[x][0]  # 빨간 길로 이동

        # 주사위 값 만큼 말 이동
        for _ in range(1, dice[depth]):
            x = graph[x][0]

        # 목적지에 도착했거나, 다른 말이 그 위치에 없는 경우
        if x == 32 or (x < 32 and x not in horses):
            before = horses[i]  # 현재 말의 위치 저장
            horses[i] = x  # 말 위치 갱신

            # 다음 주사위 사용하여 재귀 호출
            backtracking(depth + 1, result + score[x], horses)

            horses[i] = before  # 말 위치 원래대로 복구

# 백트래킹 시작 (깊이 0, 초기 점수 0, 모든 말의 초기 위치는 0)
backtracking(0, 0, [0, 0, 0, 0])
print(answer)  # 최대 점수 출력
