import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))

max_num = arr[0]
min_num = arr[0]

for i in range(1,N):
    if max_num < arr[i]:
        max_num = arr[i]

for i in range(1, N):
    if min_num > arr[i]:
        min_num = arr[i]

print(f'{min_num} {max_num}')