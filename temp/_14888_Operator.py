
N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))

max_value = -1e9
min_value = 1e9

# dfs 함수 정의
def dfs(num, idx, add, sub, mul, div):

    global max_value, min_value

    if idx == N:

        max_value = max(max_value, num)
        min_value = min(min_value, num)
        return

    if add > 0:
        dfs(num + nums[idx], idx + 1, add - 1, sub, mul, div)
    if sub > 0:
        dfs(num - nums[idx], idx + 1, add, sub - 1, mul, div)
    if mul > 0:
        dfs(num * nums[idx], idx + 1, add, sub , mul -1, div)
    if div > 0:
        dfs(int(num / nums[idx]), idx + 1, add, sub, mul, div -1)

# dfs 함수 호출
dfs(nums[0], 1, op[0], op[1], op[2], op[3])
# 최댓값과 최솟값 결과 출력
print(max_value)
print(min_value)