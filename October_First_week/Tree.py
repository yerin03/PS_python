n, m, k, c = map(int, input().split())

grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)


def propagate_weed(x, y, remaining_years):
    if remaining_years == 0 or grid[x][y] == -1:
        return

    grid[x][y] = -1
    for dx in range(-k, k + 1):
        for dy in range(-k, k + 1):
            if 0 <= x + dx < n and 0 <= y + dy < n:
                propagate_weed(x + dx, y + dy, remaining_years - 1)


def simulate_growth():
    new_grid = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == -1:
                new_grid[i][j] = -1
            else:
                num_trees = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if 0 <= i + dx < n and 0 <= j + dy < n and grid[i + dx][j + dy] != -1:
                            num_trees += 1
                new_grid[i][j] = num_trees
    return new_grid


for _ in range(m):
    grid = simulate_growth()
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                propagate_weed(i, j, c)

total_trees = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] > 0:
            total_trees += grid[i][j]

print(total_trees)
