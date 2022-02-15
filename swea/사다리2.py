import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    N = int(input())

    matrix = []
    for _ in range(100):
        matrix.append([0] + list(map(int, input().split())) + [0])  # 0으로 둘러싼 배열
    x , y = 0 , 99

    for i in range(102):
        if matrix[y][i] == 2: #(x, 100)에 있는 시작점 찾기
            break
    x = i


    while y > 0: #(x, 0)에 도달할 때 까지 반복
        if matrix[y][x - 1] == 1: #좌 검사 후 좌 끝까지 탐색&이동 및 위로 한칸 이동
            curx = x - 1 # 현재 좌표 저장
            if curx > 0: # 현재 x가 0보다 크면
                while matrix[y][curx-1] == 1: # 좌측 값이 1인동안 반복
                    curx -= 1 # 좌측으로 이동
            x = curx # x에 현재 좌표 저장
            y -= 1 # 위로 올라가기

        elif matrix[y][x + 1] == 1: #우 검사 후 우측 끝까지 탐색&이동 및 위로 한칸 이동
            curx = x + 1
            if curx < 99:
                while matrix[y][curx+1] == 1:
                    curx += 1
            x = curx
            y -= 1

        else:
            y -= 1


    print(f'#{tc} {x-1}')