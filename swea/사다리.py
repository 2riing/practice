import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())

    matrix = []
    for _ in range(100):
        matrix.append([0] + list(map(int, input().split())) + [0])  # 퍼즐의 모든 면에 0으로 덮어씀
    x , y = 0 , 99

    for i in range(102):
        if matrix[y][i] == 2: #(x, 100)에 있는 시작점 찾기
            break
    x = i


    while y > 0: #(x, 0)에 도달할 때 까지 반복
        if matrix[y-1][x]:  # 위 값이 1이면 위로
            flag = 0
            y -= 1
            if matrix[y][x-1]:  # 왼쪽 값 탐색해서 1이면 왼쪽으로
                x -= 1
                flag = 1 # flag left ==1
                if matrix[y - 1][x]:
                    y -= 1
                    flag = 0
            elif matrix[y][x + 1]:  # 오른쪽 값 탐색해서 1이면 오른쪽으로
                x += 1 # flag right == -1
                flag = -1
                if matrix[y - 1][x]:
                    y -= 1
                    flag = 0
            else :
                y -= 1
        elif flag == 1 : # flog ==1 왼쪽
            if matrix[y - 1][x]:
                y -= 1
                flag = 0
            if matrix[y][x-1]:
                x -= 1
        elif flag == -1: # flag right == -1
            if matrix[y][x + 1]:
                x += 1
            if matrix[y - 1][x]:
                y -= 1
                flag = 0

    print(f'#{tc} {x}')