import sys
sys.stdin = open('input.txt')

N = int(input())
grade = list(map(int,input().split()))
# 본인 점수중에 최대값 =M
M = max(grade)
# 모든 점수 / M * 100
for i in range(N):
    grade[i] = grade[i]/M*100
print(sum(grade)/N)