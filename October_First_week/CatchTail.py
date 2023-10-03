from copy import deepcopy

n, m, k = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]

# 길 정보
tracks = [[0] * n for _ in range(n)]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def initMAP():
    newMAP = deepcopy(tracks)
    for team in teams:
        for idx, tpos in enumerate(team):
            if idx == 0:
                newMAP[tpos[0]][tpos[1]] = 1
            elif idx == len(team) - 1:
                newMAP[tpos[0]][tpos[1]] = 3
            else:
                newMAP[tpos[0]][tpos[1]] = 2
    return newMAP


def set_track_dfs(i, j, visited):
    visited[i][j] = True  # 사이클 때문에
    tracks[i][j] = 4
    for di, dj in dirs:
        if 0 <= i + di < n and 0 <= j + dj < n and not visited[i + di][j + dj] and 1 <= MAP[i + di][j + dj] <= 4:
            set_track_dfs(i + di, j + dj, visited)


def get_team_dfs(i, j, team):  # 머리부터 꼬리까지 위치 정보 저장
    team.append([i, j])
    for di, dj in dirs:
        if 0 <= i + di < n and 0 <= j + dj < n and 1 <= MAP[i + di][j + dj] <= 3 and [i + di, j + dj] not in team:
            if MAP[i][j] == 1 and MAP[i + di][j + dj] != 2:
                continue
            get_team_dfs(i + di, j + dj, team)


def move(team):
    after_move = []
    hi, hj = team[0]  # 머리 위치
    for di, dj in dirs:
        if 0 <= hi + di < n and 0 <= hj + dj < n and (MAP[hi + di][hj + dj] == 3 or MAP[hi + di][hj + dj] == 4):
            after_move.append([hi + di, hj + dj])  # 갱신된 머리 위치
    last_pos = team[0]  # 기존 머리 위치
    for i in range(1, len(team)):  # 나머지 2, 3 이동 -> last_pos로 이동
        ni, nj = last_pos  # 이동
        after_move.append([ni, nj])
        last_pos = team[i]
    return after_move


def get_trajectory(r):
    trajectory = []  # 공이 지나가는 궤적 순서대로 담은 배열
    side, p = divmod(r, n)
    if side % 4 == 0:
        for j in range(n): trajectory.append((p, j))
    elif side % 4 == 1:
        for i in range(n - 1, -1, -1): trajectory.append((i, p))
    elif side % 4 == 2:
        for j in range(n - 1, -1, -1): trajectory.append((n - p - 1, j))
    elif side % 4 == 3:
        for i in range(n): trajectory.append((i, n - p - 1))
    return trajectory


# 궤적에 맞게 던졌을 때 어느 팀의 몇번째 인간이 가장 먼저 맞는가?! 이에 따라 점수 계산하기
def throw_ball(trajectory, teams):
    for tpos in trajectory:  # 궤적 순
        for x in range(len(teams)):
            for idx, pos in enumerate(teams[x]):
                if tuple(pos) == tpos:  # 가장 먼저 맞은 닝겐
                    teams[x] = teams[x][::-1]  # reverse
                    return (idx + 1) * (idx + 1)
    return 0


# 팀 정보 저장 (각 팀별 인원 위치 정보)
teams = []  # m개의 팀
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        # 경로 정보도 따로 저장
        if not visited[i][j] and 1 <= MAP[i][j] <= 4:
            set_track_dfs(i, j, visited)
        if MAP[i][j] == 1:
            team = []
            tmp_team = get_team_dfs(i, j, team)
            teams.append(team)

total_score = 0
for r in range(k):
    # 모든 팀은 한칸씩 이동
    for i in range(len(teams)):
        teams[i] = move(teams[i])
    # 라운드에 맞게 공 던져서 점수 계산, 필요시 공 맞은 팀 조작
    trajectory = get_trajectory(r)
    total_score += throw_ball(trajectory, teams)
    MAP = initMAP()

print(total_score)