import sys
sys.stdin = open('input.txt')

# 기본 입력
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time_table = [list(map(int, input().split())) for _ in range(N)]

    # 정렬
    print(time_table)
    time_table.sort(key=lambda x: (x[1], x[0]))
    start, end = time_table[0][0], time_table[0][1]
    cnt = 1
    for i in range(1, len(time_table)):
        cur_start, cur_end = time_table[i][0], time_table[i][1]
        if end <= cur_start: # 현재 시작이, 이전 끝나는 시간과 같거나 크면
            start, end = cur_start, cur_end
            cnt += 1 #

    print(f'#{tc} {cnt}')