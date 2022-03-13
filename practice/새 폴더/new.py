import sys
sys.stdin =  open('input.txt')

N, K = map(int, input().split()) # N : 학생 수  K : 최대 인원 수
student = [list(map(int, input().split())) for _ in range(N)] # S:성별 Y: 학년

year_0 = [0]*7
year_1 = [0]*7

for i in range(N):
    if student[i][0] ==0: # 성별이 0인 여학생인 경우
        year_0[student[i][1]] += 1
    else: # 성별 남학생
        year_1[student[i][1]] += 1

cnt = 0
for k in range(1, len(year_0)): # 여학생
    if year_0[k] > 0:
        if year_0[k] // K > 0:
            if year_0[k]%K == 0:
                cnt += year_0[k]//K
            else:
                cnt += (year_0[k]//K + 1)
        else:
            cnt += 1

for j in range(1, len(year_1)):
    if year_1[j] > 0:
        if year_1[j] // K > 0:
            if year_1[j] % K == 0:
                cnt += year_1[j]//K
            else:
                cnt += (year_1[j]//K + 1)
        else:
            cnt += 1
print(year_1)
print(cnt)

# 답 왜 안나오는지
