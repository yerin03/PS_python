def can_go(road, l):
    # road의 길이를 n으로 설정
    n = len(road)
    # 길의 길이만큼의 visited 리스트를 생성 (경사로가 설치된 위치를 체크하기 위해)
    visited = [0] * n

    # 길의 각 위치를 확인하기 위한 반복문
    for i in range(n - 1):
        # 인접한 두 칸의 높이 차이가 1보다 크면 지나갈 수 없음
        if abs(road[i] - road[i + 1]) > 1:
            return False

        # 현재 위치의 높이가 다음 위치보다 클 경우 (높이가 낮아지는 경우)
        if road[i] > road[i + 1]:
            # 다음 칸의 높이를 temp에 저장
            temp = road[i + 1]
            # 경사로를 설치해야 하는 위치를 확인하기 위한 반복문
            for j in range(i + 1, i + 1 + l):
                # 범위를 벗어나거나, 높이가 temp와 다르거나, 이미 경사로가 설치된 경우
                if j >= n or road[j] != temp or visited[j]:
                    return False
                # 경사로를 설치했다고 체크
                visited[j] = 1

        # 현재 위치의 높이가 다음 위치보다 낮을 경우 (높이가 높아지는 경우)
        if road[i] < road[i + 1]:
            # 현재 칸의 높이를 temp에 저장
            temp = road[i]
            # 경사로를 설치해야 하는 위치를 확인하기 위한 반복문
            for j in range(i, i - l + 1, -1):
                # 범위를 벗어나거나, 높이가 temp와 다르거나, 이미 경사로가 설치된 경우
                if j < 0 or road[j] != temp or visited[j]:
                    return False
                # 경사로를 설치했다고 체크
                visited[j] = 1

    # 위의 조건들을 모두 통과했다면, 해당 길은 지나갈 수 있음
    return True

n, l = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

# 행 검사
for row in road:
    if can_go(row, l):
        cnt += 1

# 열 검사
for col in zip(*road):
    if can_go(col, l):
        cnt += 1

print(cnt)
