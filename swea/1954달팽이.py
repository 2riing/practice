import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pan = [[0]*N for _ in range(N)]

    k = 1
    row, col, i, cnt = 0, -1, 0, 0

    def Trun(row, col, cnt, k, i):
        if cnt == N*N:
            return
        else:
            for _ in range(N-i):
                cnt += 1
                col += k
                pan[row][col] = cnt
                if cnt == N * N:
                    return
            for _ in range(N-1-i):
                cnt += 1
                row += k
                pan[row][col] = cnt
                if cnt == N * N:
                    return
            k *= -1
            return Trun(row, col, cnt, k, i+1)
    result = []
    Trun(row, col, cnt, k, i)
    print(f'#{tc}')
    for i in range(len(pan)):
        print(*pan[i])
