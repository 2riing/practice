import sys
sys.stdin = open('input.txt')


N = int(input()) # 회의의 수

times = [list(map(int, input().split())) for _ in range(N)]
# tiems[i][0] : 시작시간 times[i][1] : 종료시간

cnt = 1
EndTime = 0

times = sorted(times, key=lambda time: time[0]) # 시작시간 기준 정렬
times = sorted(times, key=lambda time: time[1])

for i in range(len(times)):
    if EndTime <= times[i][0]:
        cnt += 1
        EndTime = times[i][1]

print(cnt)

# 최대를 구해야 하는데,,