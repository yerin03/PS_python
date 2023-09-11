
n = int(input())
number = list(map(int,input().split()))
B,C = map(int,input().split())

cnt = 0


for num in number:

    num -= B
    cnt += 1

    if num > 0:
        cnt+= (num//C)

        if num % C !=0 :
            cnt+=1

print(cnt)






