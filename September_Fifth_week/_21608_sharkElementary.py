N = int(input())  # N 입력받기
students = {}  # 학생들의 좋아하는 학생 목록을 저장할 딕셔너리 생성

# 학생들의 좋아하는 학생 목록 저장
for _ in range(N ** 2):
    info = list(map(int, input().split()))
    student_num = info[0]
    favorite_students = info[1:]
    students[student_num] = favorite_students

dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
dy = [0, 0, -1, 1]

satisfaction = 0  # 전체 학생의 만족도를 저장할 변수


# 학생들의 자리를 정하는 함수
def seat_students():
    global satisfaction
    for student in students.keys():
        favorite_list = students[student]  # 현재 학생이 좋아하는 학생 목록
        max_empty_adjacent = -1  # 가장 많은 빈 칸과 인접한 칸의 개수
        max_favorite_adjacent = -1  # 가장 많은 좋아하는 학생과 인접한 칸의 개수
        selected_seat = ()  # 선택된 자리의 좌표

        # 교실의 모든 칸을 탐색하며 조건에 맞는 자리 찾기
        for i in range(N):
            for j in range(N):
                if classroom[i][j] == 0:  # 빈 칸인 경우에만 확인
                    empty_adjacent = 0  # 빈 칸과 인접한 칸의 개수
                    favorite_adjacent = 0  # 좋아하는 학생과 인접한 칸의 개수

                    # 상, 하, 좌, 우 칸 확인
                    for k in range(4):
                        nx, ny = i + dx[k], j + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if classroom[nx][ny] == 0:  # 빈 칸인 경우
                                empty_adjacent += 1
                            elif classroom[nx][ny] in favorite_list:  # 좋아하는 학생이 인접한 경우
                                favorite_adjacent += 1

                    # 현재 자리가 가장 좋은 자리인지 확인
                    if favorite_adjacent > max_favorite_adjacent or \
                            (favorite_adjacent == max_favorite_adjacent and empty_adjacent > max_empty_adjacent) or \
                            (favorite_adjacent == max_favorite_adjacent and empty_adjacent == max_empty_adjacent and i <
                             selected_seat[0]) or \
                            (
                                    favorite_adjacent == max_favorite_adjacent and empty_adjacent == max_empty_adjacent and i ==
                                    selected_seat[0] and j < selected_seat[1]):
                        max_favorite_adjacent = favorite_adjacent
                        max_empty_adjacent = empty_adjacent
                        selected_seat = (i, j)

        # 선택된 자리에 학생 배치
        classroom[selected_seat[0]][selected_seat[1]] = student

        # 만족도 계산
        satisfaction += max_favorite_adjacent ** max_empty_adjacent


# 교실 초기화 (0은 빈 칸을 의미)
classroom = [[0 for _ in range(N)] for _ in range(N)]

# 학생들을 차례대로 자리에 배치
seat_students()

# 전체 학생의 만족도 출력
print(satisfaction)
