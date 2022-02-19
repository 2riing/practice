# 9개의 서로 다른 자연수
# 이중 최대 값을 찾고 인덱스 받아 오기

#
# N = []
# for i in range(9):
#     N.append(int(input()))
# print(max(N))
# print(N.index(max(N))+1)

import sys
sys.stdin = open('input.txt')

arr = [int(input()) for _ in range(9)]
#
# print(arr)

max_num = 0
max_count = 0
for i in range(9):
    if max_num < arr[i]:
        max_num = arr[i]
print(max_num)

for j in range(9):
    if arr[j] == max_num:
        max_count = j
print(max_count+1)





# max = 0
# cnt = 0
# for i in range(9):
#     num = int(input())
#     if num > max:
#         max = num
#         cnt += 1
# print(max)
# print(cnt)
