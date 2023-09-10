
n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

sumA,sumB = 0,0

for i in range(n):
    for j in range(n):

        #standard = i
        if 10*i+j == 10*i+i:
            continue
        elif 10*i+j < 10*i+i:
            sumA += arr[i][j]
        elif 10*i+j > 10*i+i:
            sumB += arr[i][j]



