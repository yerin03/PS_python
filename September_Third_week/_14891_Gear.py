status = [list(map(int,input().split())) for _ in range(4)]

K = int(input())

num = [list(map(int,input().split())) for _ in range(K)]

arr = [1,2,3,4,5]

cnt = 0


def shift(arr, direction):

    if direction == 1 :
        return arr[-1:] + arr[:-1]

    else :
        return arr[1:]+arr[0:1]

for i in range (K) :

    #기준
    gear,direction = num[i]
    gears_to_rotate = [(gear,direction)]

    d = direction
    for j in range(gear - 1, 0, -1):
        if status[j][6] != status[j - 1][2]:
            d = -d
            gears_to_rotate.append((j, d))
        else:
            break

    d = direction
    for j in range(gear, 4):
        if status[j - 1][2] != status[j][6]:
            d = -d
            gears_to_rotate.append((j, d))
        else:
            break

    for g, d in gears_to_rotate:
        status[g - 1] = shift(status[g - 1], d)

score = 0

for i in range(4):
    if status[i][0] == 1:
        score += 2 ** i

print(score)








