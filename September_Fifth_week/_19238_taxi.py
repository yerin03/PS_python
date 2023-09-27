# 스타트 택시
from collections import deque
import sys

input = sys.stdin.readline

N, M, fuel = map(int, input().split())

# 지도
arr = [[]]
for _ in range(N):
    arr.append([0] + list(map(int, input().split())))

# 현재 위치
taxi = list(map(int, input().split()))

# 사람들 정보
people = []
for _ in range(M):
    people.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 가장 가까운 승객을 찾는 함수
def find_person():
    tx, ty = taxi
    dist_map = get_dist(tx, ty)  # 현재 택시 위치에서 모든 위치까지의 거리를 계산
    people.sort(key=lambda p: (-dist_map[p[0]][p[1]], -p[0], -p[1]))
    # 거리가 가장 가까운 승객을 먼저 선택하고, 거리가 같으면 행과 열이 작은 순서로 정렬
    sx, sy, ex, ey = people.pop()  # 승객 정보를 가져옴
    return [sx, sy, ex, ey, dist_map[sx][sy]]

def drive():
    global taxi
    global fuel
    # 픽업
    sx, sy, ex, ey, dist = find_person()  # 가장 가까운 승객 정보를 가져옴
    if dist == -1:
        return False  # 픽업할 승객이 없으면 실패
    fuel -= dist  # 픽업까지 가는데 필요한 연료 소모
    if fuel < 0:
        return False  # 연료 부족 시 실패
    # 픽아웃
    used = get_dist(sx, sy)  # 승객의 현재 위치에서 목적지까지의 거리를 계산
    if used[ex][ey] == -1:
        return False  # 목적지까지 갈 수 없는 경우 실패
    fuel -= used[ex][ey]  # 목적지까지 가는데 필요한 연료 소모
    if fuel < 0:
        return False  # 연료 부족 시 실패
    fuel += used[ex][ey] * 2  # 승객을 픽업하고 목적지까지 이동한 후 연료 충전
    taxi = [ex, ey]  # 택시 위치 업데이트
    return True


def get_dist(a, b):
    q = deque()
    q.append((a, b))
    visited = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
    visited[a][b] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 < nx <= N and 0 < ny <= N and visited[nx][ny] == -1:
                if not arr[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return visited


for _ in range(M):
    if not drive():
        fuel = -1
        break

print(fuel)
