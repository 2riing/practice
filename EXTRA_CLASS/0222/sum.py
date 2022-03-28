import sys
sys.stdin=open('input.txt')


for tc in range(1, 11):
    T = int(input())
    matrix = [list(map(int,input().split())) for _ in range(100)]

    def cross_sum(mx):
        crs_sum1 = 0
        crs_sum2 = 0
        for i in range(100):
            crs_sum1 += mx[i][i]
            crs_sum2 += mx[i][99-i]
        if crs_sum1 > crs_sum2:
            return crs_sum1
        else:
            return crs_sum2

    def row_sum(mx):
        r_max = 0
        for i in range(100):
            r_sum = 0
            for j in range(100):
                r_sum += mx[i][j]
                if r_sum > r_max:
                    r_max = r_sum
        return r_max

    def col_sum(mx):
        r_max = 0
        for i in range(100):
            c_sum = 0
            for j in range(100):
                c_sum += mx[j][i]
                if c_sum > r_max:
                    r_max = c_sum
        return r_max

    max_list = [cross_sum(matrix), row_sum(matrix), col_sum(matrix)]


    print(f'#{tc} {max(max_list)}')