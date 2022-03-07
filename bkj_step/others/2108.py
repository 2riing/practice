

from unittest import result


N = int(input())

for i in range(N):
    list_num = int(input())

result = []

# 산술평균
sum(list_num)/len(list_num)

# 중앙값


# 최빈값
for i in list_num:
    list_num.count(i)

# 범위
result += max(list_num) - min(list_num)