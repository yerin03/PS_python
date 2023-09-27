N, M, K = map(int, input().split())
fireballs = []
for _ in range(M):
    _r, _c, _m, _s, _d = list(map(int, input().split()))
    fireballs.append([_r-1, _c-1, _m, _s, _d])

# 격자 상태와 이동 방향 초기화
MAP = [[[] for _ in range(N)] for _ in range(N)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# K번 파이어볼 이동
for _ in range(K):
    # 모든 파이어볼을 이동
    while fireballs:
        cr, cc, cm, cs, cd = fireballs.pop(0)
        nr = (cr + cs * dx[cd]) % N  # 범위를 벗어나면 원형으로 연결
        nc = (cc + cs * dy[cd]) % N
        MAP[nr][nc].append([cm, cs, cd])

    # 격자 상태를 기반으로 파이어볼 합치기/분리
    for r in range(N):
        for c in range(N):
            # 파이어볼이 2개 이상인 경우
            if len(MAP[r][c]) > 1:
                # 합쳐질 파이어볼의 총 질량, 총 속력, 홀수 방향 개수, 짝수 방향 개수, 파이어볼 개수 초기화
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(MAP[r][c])

                # 해당 격자에 있는 모든 파이어볼에 대해서
                while MAP[r][c]:
                    _m, _s, _d = MAP[r][c].pop(0)
                    sum_m += _m  # 질량 누적
                    sum_s += _s  # 속력 누적
                    if _d % 2:  # 방향이 홀수면 홀수 방향 카운트
                        cnt_odd += 1
                    else:  # 방향이 짝수면 짝수 방향 카운트
                        cnt_even += 1

                # 모든 파이어볼의 방향이 홀수이거나 짝수인 경우
                if cnt_odd == cnt or cnt_even == cnt:
                    nd = [0, 2, 4, 6]
                else:  # 홀수와 짝수 방향이 섞여 있는 경우
                    nd = [1, 3, 5, 7]
                if sum_m//5:
                    for d in nd:
                        fireballs.append([r, c, sum_m//5, sum_s//cnt, d])

            # 파이어볼이 1개인 경우
            elif len(MAP[r][c]) == 1:
                fireballs.append([r, c] + MAP[r][c].pop())

# 남아있는 파이어볼의 질량 합 출력
print(sum([f[2] for f in fireballs]))
