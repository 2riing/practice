import sys
sys.stdin = open('input.txt')

L, P = list(map(int, input().split()))
arr = list(map(int, input().split()))

for i in range(len(arr)):
    arr[i] -= L*P
    print(arr[i],end=' ')

