from itertools import combinations

# 거리 계산 함수
def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# 도시의 치킨 거리 계산 함수
def city_chicken_distance(chicken_positions):
    total_distance = 0
    for home in homes:
        total_distance += min([distance(home, chicken) for chicken in chicken_positions])
    return total_distance

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

# 집과 치킨집의 위치를 찾는다.
homes = []
chickens = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            homes.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

# 치킨집들 중에서 M개를 고르는 모든 조합을 찾아 도시의 치킨 거리를 계산
result = float('inf')
for chicken_positions in combinations(chickens, M):
    result = min(result, city_chicken_distance(chicken_positions))

print(result)
